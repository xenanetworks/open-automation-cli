import ast
from loguru import logger
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
from xoa_driver import enums as xoa_enums
from xoa_driver.internals.core.protocol.fields import data_types
from docstring_parser import parse


@dataclass
class ParameterInfo:
    py_type: str
    description: str


def extract_parameter_from_docstring(parsed_docstring) -> Dict[str, ParameterInfo]:
    result = {}
    for param in parsed_docstring.params:
        result[param.arg_name] = ParameterInfo(py_type=param.type_name, description=param.description)
    return result


@dataclass
class FrontIndices:
    is_module_index_exist: bool = False
    is_port_index_exist: bool = False

    def mark_index_exist(self, name: str):
        if name == '_module':
            self.is_module_index_exist = True
        elif name == '_port':
            self.is_port_index_exist = True


@dataclass
class TailParameter:
    name: str
    type_in_str: str
    description: str = ''

    @property
    def is_ipv4_address(self) -> bool:
        return self.name in ('ipv4_address', 'subnet_mask', 'gateway', 'wild') or 'ipv4' in self.type_in_str.lower()

    @property
    def is_int_list(self) -> bool:
        return 'List[int]' in self.type_in_str

    @property
    def cli_type(self):
        new_type = self.type_in_str
        if self.type_in_str == 'int':
            new_type = 'integer'
        elif self.type_in_str == 'str':
            new_type = 'string'
        elif 'indices' in self.name:
            new_type = 'indices'
        elif self.is_ipv4_address:
            new_type = 'ipv4_address'
        elif 'ipv6_address' in self.name:
            new_type = 'ipv6_address'
        elif self.is_int_list:
            new_type = 'integer list'
        return new_type


@dataclass
class EnumFieldStruct:
    name: str
    value: Optional[Union[str, int]]
    description: Optional[str]


@dataclass
class EnumStruct:
    name: str
    description: Optional[str]
    fields: List["EnumFieldStruct"]


@dataclass
class FieldStruct:
    name: str
    type: str
    enum: Optional["EnumStruct"] = None
    byte_size: Optional[int] = 0
    description: Optional[str] = ''


@dataclass
class CommandDataStruct:
    fields: List["FieldStruct"] = field(default_factory=list)

def try_get_xoa_enum(enum_name: str) -> Optional[EnumStruct]:
    struct = None
    if (enum := getattr(xoa_enums, enum_name, None)):
        struct = EnumStruct(name=enum_name, fields=[], description=enum.__doc__)
        for member in enum:
            struct.fields.append(EnumFieldStruct(
                name=member.name,
                value=member.value,
                description='',
            ))
    return struct


def parse_DataAttr_field(stmt: ast.AnnAssign) -> FieldStruct:
    arg = stmt.value.args[0]
    xmp_type_class_name = ''
    if isinstance(arg, ast.Attribute):
        xmp_type_class_name = str(arg.attr)
    else:
        xmp_type_class_name = str(arg.id)

    xmp_type_class = getattr(data_types, xmp_type_class_name, None)
    if not xmp_type_class:
        logger.debug(xmp_type_class_name)

    enum_struct = None
    if stmt.value.keywords:
        if isinstance(keyword := stmt.value.keywords[0], ast.keyword) and hasattr(keyword.value, 'id'):
            enum_struct = try_get_xoa_enum(keyword.value.id)
        else:
            logger.debug(ast.dump(stmt.value))

    field_struct = FieldStruct(
        name=stmt.target.id,
        type=xmp_type_class_name,
        byte_size=xmp_type_class.size if xmp_type_class else 0,
        enum=enum_struct,
    )
    return field_struct

def docstring_description_split_line(description: str):
    """:return:
            - the static IP address of the chassis
            - the subnet mask of the local network segment
            - the gateway of the local network segment
        :rtype: C_IPADDRESS.GetDataAttr

        :return: the port's ARP table used to reply to incoming ARP requests.
            * IP address to match to the Target IP address in the ARP requests,
            * The prefix used for address matching,
            * Whether the target MAC address will be patched with the part of the IP address that is not masked by the prefix,
            * The target MAC address to return in the ARP reply
        :rtype: P_ARPRXTABLE.GetDataAttr

        assume line that starts with '-' or '*' is field description
    """
    lines = [line.strip().replace('- ', '') for line in description.split('\n') if line and line.startswith('-')]
    if not lines:
        lines = [line.strip().replace('* ', '') for line in description.split('\n') if line and line.startswith('*')]
    return lines

def update_field_description(command_data_struct: CommandDataStruct, field_descriptions: Optional[Dict[str, str]], docstring_description: str):
    if not command_data_struct:
        return

    descriptions = docstring_description_split_line(docstring_description)
    for i, field in enumerate(command_data_struct.fields):
        if field_descriptions:
            field.description = field_descriptions.get(field.name, field.description)
        elif descriptions and len(docstring_description) > i - 1:
            field.description = descriptions[i]
        else:
            field.description = docstring_description

@dataclass
class CLICommand:
    code: int = field(init=False)
    name: str = ''
    description: str = ''
    is_support_action_set: bool = False
    is_support_action_get: bool = False
    is_support_push: bool = False
    front_indices: FrontIndices = field(init=False)
    tail_indices: List[str] = field(default_factory=list)
    tail_parameters_get: List[TailParameter] = field(default_factory=list)
    tail_parameters_set: List[TailParameter] = field(default_factory=list)
    data_to_server: Optional[CommandDataStruct] = None
    data_from_server: Optional[CommandDataStruct] = None

    def __post_init__(self):
        self.front_indices = FrontIndices()

    def enable_support_action(self, method: str):
        if method == 'set':
            self.is_support_action_set = True
        elif method == 'get':
            self.is_support_action_get = True

    def set_transmit_data(self, method: str, data: CommandDataStruct):
        if method == 'SetDataAttr':
            self.data_to_server = data
        elif method == 'GetDataAttr':
            self.data_from_server = data

KNOWN_ARG = ['subnet_mask', 'gateway', 'module_ports']
def is_fake_literal_value_exists(name: str):
    """if name == 'ip_address', value would be '192.168.100.1' this kind of logic
    """
    return name in KNOWN_ARG or 'address' in name or 'indices' in name

def parse_command_ast(command_stmt: ast.ClassDef) -> CLICommand:
    """you better have 'example_ast_tree.txt' in spilt view if you wanna debug this function
    """
    command = CLICommand(name=command_stmt.name)
    # if first statment is Expr type, assume it is description
    if (isinstance(comment_expr := command_stmt.body[0], ast.Expr)):
        command.description = comment_expr.value.value.strip()  # type: ignore

    get_data_description = ''
    set_data_parameters = None
    for stmt in command_stmt.body:
        if isinstance(stmt, ast.AnnAssign):
            variable_name: str = getattr(stmt.target, 'id')
            if variable_name in ('_module', '_port'):
                command.front_indices.mark_index_exist(variable_name)
            elif variable_name == 'code':
                command.code = stmt.value.value # type: ignore
            elif variable_name == 'pushed':
                command.is_support_push = stmt.value.value # type: ignore
            elif 'xindex' in variable_name:
                command.tail_indices.append(variable_name[1:]) # remove '_'

        elif isinstance(stmt, ast.ClassDef) and stmt.name in ('SetDataAttr', 'GetDataAttr'):
            command_data_struct = CommandDataStruct(fields=[])
            for body_stmt in stmt.body:
                if isinstance(body_stmt, ast.AnnAssign):
                    # logger.debug(command_stmt.name)
                    field_struct = parse_DataAttr_field(body_stmt)
                    command_data_struct.fields.append(field_struct)
                    # logger.debug(field_struct)
            command.set_transmit_data(stmt.name, command_data_struct)

        if isinstance(stmt, ast.FunctionDef) and stmt.name in ('set', 'get'):
            command.enable_support_action(stmt.name)
            docstring = ast.get_docstring(stmt, clean=False)
            parsed_docstring = parse(docstring)
            docstring_parameter = extract_parameter_from_docstring(parsed_docstring)


            for arg in stmt.args.args[1:]: # first arg must be self? skip it
                annotation_type = docstring_type = ''
                if (_type := getattr(arg.annotation, 'id', None)):
                    annotation_type = _type

                description = arg.arg
                if param_info := docstring_parameter.get(arg.arg):
                    docstring_type = param_info.py_type

                    if docstring_type and docstring_type != annotation_type and '[' not in docstring_type:
                        logger.warning(f"docstring typing not match: {command.name}, {stmt.name}, {arg.arg}: {annotation_type}({docstring_type})")
                    description = param_info.description
                else:
                    logger.warning(f"docstring mssing: {command.name}, {stmt.name}, {arg.arg}")

                current_parameter = TailParameter(
                    name=arg.arg,
                    type_in_str=annotation_type,
                    description=description
                )

                if not annotation_type and not is_fake_literal_value_exists(arg.arg): # try to get type manually
                    logger.warning(f"literal missing: {command.name}, {stmt.name}, {arg.arg}") # for debug
                    if isinstance(arg.annotation.slice, ast.Tuple):
                        current_parameter.type_in_str = str(arg.annotation.slice.elts)
                    elif isinstance(arg.annotation.slice, ast.Attribute):
                        current_parameter.type_in_str = str(arg.annotation.slice.attr)
                    else:
                        current_parameter.type_in_str = f"{arg.annotation.value.attr}[{arg.annotation.slice.id}]"

                    if 'ast.' in current_parameter.type_in_str:
                        current_parameter.type_in_str = docstring_type

                tail_parameters: List[TailParameter] = getattr(command, f"tail_parameters_{stmt.name}")
                tail_parameters.append(current_parameter)

            # for update (Set,Get)DataAttr
            if stmt.name == 'get' and parsed_docstring and parsed_docstring.returns:
                get_data_description = parsed_docstring.returns.description
            elif stmt.name == 'set':
                set_data_parameters = docstring_parameter

    update_field_description(command.data_from_server, set_data_parameters, get_data_description)
    update_field_description(command.data_to_server, set_data_parameters, get_data_description)


    return command