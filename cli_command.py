import ast
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
from loguru import logger
from docstring_parser import parse
from xoa_driver import enums as xoa_enum



@dataclass
class ParameterInfo:
    py_type: str
    description: str


def extract_docstring(full_comment: Optional[str] = '') -> Dict[str, ParameterInfo]:
    docstring = parse(full_comment)
    result = {}
    for param in docstring.params:
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
    def cli_type(self):
        new_type = self.type_in_str
        if self.type_in_str == 'int':
            new_type = 'integer'
        elif self.type_in_str == 'str':
            new_type = 'string'
        elif 'indices' in self.name:
            new_type = 'indices'
        elif 'ipv4_address' in self.name:
            new_type = 'ipv4_address'
        return new_type


@dataclass
class CLICommand:
    code: int = field(init=False)
    name: str = ''
    description: str = ''
    is_support_action_set: bool = False
    is_support_action_get: bool = False
    front_indices: FrontIndices = field(init=False)
    tail_indices: List[str] = field(default_factory=list)
    tail_parameters_get: List[TailParameter] = field(default_factory=list)
    tail_parameters_set: List[TailParameter] = field(default_factory=list)

    def __post_init__(self):
        self.front_indices = FrontIndices()

    def enable_support_action(self, method: str):
        if method == 'set':
            self.is_support_action_set = True
        elif method == 'get':
            self.is_support_action_get = True


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

    for stmt in command_stmt.body[1:]:
        if isinstance(stmt, ast.AnnAssign):
            variable_name: str = getattr(stmt.target, 'id')
            if variable_name in ('_module', '_port'):
                command.front_indices.mark_index_exist(variable_name)
            if variable_name == 'code':
                command.code = stmt.value.value # type: ignore
            elif 'xindex' in variable_name:
                command.tail_indices.append(variable_name[1:]) # remove '_'

        if isinstance(stmt, ast.FunctionDef) and stmt.name in ('set', 'get'):
            command.enable_support_action(stmt.name)
            docstring = extract_docstring(ast.get_docstring(stmt))

            for arg in stmt.args.args[1:]: # first arg must be self? skip it
                arg_type = ''
                description = arg.arg
                if param_info := docstring.get(arg.arg):
                    arg_type = param_info.py_type
                    description = param_info.description
                else:
                    logger.warning(f"docsting mssing: {command.name}, {stmt.name}, {arg.arg}")

                current_parameter = TailParameter(
                    name=arg.arg,
                    type_in_str=arg_type,
                    description=description
                )

                if not arg_type: # try to get type manually
                    if isinstance(arg.annotation, ast.Name):
                        current_parameter.type_in_str = arg.annotation.id
                    elif not is_fake_literal_value_exists(arg.arg):
                        logger.warning(f"literal missing: {command.name}, {stmt.name}, {arg.arg}") # for debug
                        if isinstance(arg.annotation.slice, ast.Tuple):
                            current_parameter.type_in_str = str(arg.annotation.slice.elts)
                        elif isinstance(arg.annotation.slice, ast.Attribute):
                            current_parameter.type_in_str = str(arg.annotation.slice.attr)
                        else:
                            current_parameter.type_in_str = f"{arg.annotation.value.attr}[{arg.annotation.slice.id}]"

                tail_parameters: List[TailParameter] = getattr(command, f"tail_parameters_{stmt.name}")
                tail_parameters.append(current_parameter)

    return command