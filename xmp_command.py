import ast
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
from loguru import logger
from docstring_parser import parse
from xoa_driver import enums as xoa_enums
from xoa_driver.internals.core.protocol.fields import data_types


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
class CommandMethodStruct:
    name: str
    doc: Optional[str] = ''
    args: Optional[OrderedDict] = field(default_factory=OrderedDict)

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


@dataclass
class XMPCommand:
    code: int = -1
    name: str = ''
    description: str = ''
    support_push: bool = False
    data_to_server: Optional[CommandDataStruct] = None
    data_from_server: Optional[CommandDataStruct] = None
    methods: List["CommandMethodStruct"] = field(default_factory=list)

    def __post_init__(self):
        pass

    def set_transmit_data(self, method: str, data: CommandDataStruct):
        if method == 'SetDataAttr':
            self.data_to_server = data
        elif method == 'GetDataAttr':
            self.data_from_server = data




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

def update_field_description(command_data_struct: CommandDataStruct, field_descriptions: Optional[Dict[str, str]], description: str):
    if not command_data_struct:
        return

    for f in command_data_struct.fields:
        if field_descriptions:
            f.description = field_descriptions.get(f.name, f.description)
        else:
            f.description = description


def parse_command_ast(command_stmt: ast.ClassDef) -> XMPCommand:
    """you better have 'example_ast_tree.txt' in spilt view if you wanna debug this function
    """
    command = XMPCommand(name=command_stmt.name)
    if (isinstance(comment_expr := command_stmt.body[0], ast.Expr)): # if first statment is Expr type, assume it is description
        command.description = comment_expr.value.value.strip().split('..', 1)[0]  # type: ignore

    fixed_args = []
    get_data_description = ''
    set_data_parameters = None
    for stmt in command_stmt.body:
        if isinstance(stmt, ast.AnnAssign):
            variable_name: str = getattr(stmt.target, 'id')
            if variable_name == 'code':
                command.code = stmt.value.value # type: ignore
            elif variable_name == 'pushed':
                command.support_push = stmt.value.value # type: ignore
            elif variable_name == 'pushed':
                command.is_support_push = stmt.value.value # type: ignore
            elif variable_name in ('_module', '_port') or 'xindex' in variable_name:
                fixed_args.append(variable_name[1:]) # remove '_'

        elif isinstance(stmt, ast.ClassDef) and stmt.name in ('SetDataAttr', 'GetDataAttr'):
            command_data_struct = CommandDataStruct(fields=[])
            for body_stmt in stmt.body:
                if isinstance(body_stmt, ast.AnnAssign):
                    # logger.debug(command_stmt.name)
                    field_struct = parse_DataAttr_field(body_stmt)
                    command_data_struct.fields.append(field_struct)
                    # logger.debug(field_struct)
            command.set_transmit_data(stmt.name, command_data_struct)

        elif isinstance(stmt, ast.FunctionDef) and stmt.name in ('set', 'get'):
            docstring = ast.get_docstring(stmt, clean=False)
            parsed_docstring = parse(docstring)
            docstring_parameter = extract_parameter_from_docstring(parsed_docstring)

            method_struct = CommandMethodStruct(
                name=f"cmd_{stmt.name}",
                doc=docstring,
            )
            for fa in fixed_args:
                method_struct.args[fa] = 'int'

            for arg in stmt.args.args[1:]: # first arg must be self? skip it
                arg_type = docstring_type = ''
                if (annotation_type := getattr(arg.annotation, 'id', None)):
                    arg_type = annotation_type

                if param_info := docstring_parameter.get(arg.arg):
                    docstring_type = param_info.py_type

                    # if docstring_type and docstring_type != arg_type and '[' not in docstring_type: # just for find out type not match
                    #     logger.warning(f"docstring typing not match: {command.name}, {stmt.name}, {arg.arg}: {arg_type}({docstring_type})")
                else:
                    logger.warning(f"docstring mssing: {command.name}, {stmt.name}, {arg.arg}")

                if not arg_type: # try to get type manually
                    if isinstance(arg.annotation.slice, ast.Tuple):
                        arg_type = str(arg.annotation.slice.elts)
                    elif isinstance(arg.annotation.slice, ast.Attribute):
                        arg_type = str(arg.annotation.slice.attr)
                    else:
                        arg_type = f"{arg.annotation.value.attr}[{arg.annotation.slice.id}]"
                    if 'ast.' in arg_type: # it means fail to get type
                        arg_type = docstring_type

                if hasattr(xoa_enums, arg_type):
                    arg_type = 'int'

                method_struct.args[arg.arg] = arg_type

            # for update (Set,Get)DataAttr
            if stmt.name == 'get' and parsed_docstring and parsed_docstring.returns:
                get_data_description = parsed_docstring.returns.description
            elif stmt.name == 'set':
                set_data_parameters = docstring_parameter

            command.methods.append(method_struct)


    update_field_description(command.data_from_server, set_data_parameters, get_data_description)
    update_field_description(command.data_to_server, set_data_parameters, get_data_description)

    return command