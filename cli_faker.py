from dataclasses import dataclass
from enum import Enum
from typing import List
from xoa_driver import enums as xoa_enums
from cli_command import CLICommand, TailParameter


class FakerOutputMode(Enum):
    SYNTAX_NAME = 0
    EXAMPLE_LITERAL = 1

    @property
    def by_name(self):
        return self == FakerOutputMode.SYNTAX_NAME


@dataclass
class CLICommandFaker:
    command: CLICommand

    def generate_front_indices(self, output_mode: FakerOutputMode) -> str:
        result = []
        if self.command.front_indices.is_module_index_exist:
            result.append('<module-index>' if output_mode.by_name else '0')
        if self.command.front_indices.is_port_index_exist:
            result.append('<port-index>' if output_mode.by_name else '1')
        return '/'.join(result)

    def generate_tail_indices(self, output_mode: FakerOutputMode) -> str:
        if not self.command.tail_indices:
            return ''

        result = []
        for index_name in self.command.tail_indices:
            result.append(f"<{index_name}>" if output_mode.by_name else '0')
        result = ', '.join(result)
        return f"[{result}]"

    def try_get_xoa_enum_first_member(self, enum_name: str) -> str:
        name = ''
        if isinstance(enum_name, str) and ( e := getattr(xoa_enums, enum_name, None)):
            name = list(e)[0].name
        return name

    def get_parameter_literal(self, parameter: TailParameter) -> str:
        literal = '?L'
        if (e := self.try_get_xoa_enum_first_member(parameter.type_in_str)):
            literal = e
        elif 'ipv4' in parameter.name.lower() or 'ipv4' in parameter.type_in_str.lower():
            literal = '192.168.1.100'
        elif 'subnet_mask' in parameter.name:
            literal = '255.255.255.0'
        elif 'gateway' in parameter.name:
            literal = '192.168.1.1'
        elif 'ipv6' in parameter.name:
            literal = '::1'
        elif parameter.name == 'timestamp':
            literal = '2147483647'
        elif parameter.name == 'module_ports':
            literal = '0 0 0 1'
        elif parameter.is_int_list or 'indices' in parameter.name:
            literal = '0 1'
        elif parameter.type_in_str == 'int':
            literal = '1'
        elif parameter.type_in_str == 'str':
            literal = 'word'

        return literal

    def generate_tail_parameters(self, output_mode: FakerOutputMode, parameters: List[TailParameter]) -> str:
        result = []
        for param in parameters:
            result.append(f"<{param.name}>" if output_mode.by_name else self.get_parameter_literal(param))
        return ' '.join(result)

    def generate_parameters_set(self, output_mode: FakerOutputMode) -> str:
        return self.generate_tail_parameters(output_mode, self.command.tail_parameters_set)

    def generate_parameters_get(self, output_mode: FakerOutputMode) -> str:
        return ' '.join(filter(
            None,
            [self.generate_tail_parameters(output_mode, self.command.tail_parameters_get), '?']
        ))

    def generate_method_example(self, output_mode: FakerOutputMode, method_parameters: str) -> str:
        result = [
            self.generate_front_indices(output_mode),
            self.command.name,
            self.generate_tail_indices(output_mode),
            method_parameters,
        ]
        return ' '.join(filter(None, result))

    @property
    def syntax_set(self) -> str:
        """skip checking current command is support set action
        """
        output_mode = FakerOutputMode.SYNTAX_NAME
        return self.generate_method_example(output_mode, self.generate_parameters_set(output_mode))

    @property
    def syntax_get(self) -> str:
        output_mode = FakerOutputMode.SYNTAX_NAME
        return self.generate_method_example(output_mode, self.generate_parameters_get(output_mode))

    @property
    def example_set(self) -> str:
        """skip checking current command is support set action
        """
        output_mode = FakerOutputMode.EXAMPLE_LITERAL
        return self.generate_method_example(output_mode, self.generate_parameters_set(output_mode))

    @property
    def example_get(self) -> str:
        output_mode = FakerOutputMode.EXAMPLE_LITERAL
        return self.generate_method_example(output_mode, self.generate_parameters_get(output_mode))