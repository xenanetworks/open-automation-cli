from asyncio.log import logger
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from xoa_driver import enums as xoa_enums
from cli_command import CLICommand, FieldStruct, TailParameter


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
        if isinstance(enum_name, str) and ( e := getattr(xoa_enums, enum_name, None) ):
            name = list(e)[0].name
        return name

    def get_parameter_literal(self, set_or_get_parameter: Optional[TailParameter] = None, DataAttr_parameter: Optional[FieldStruct] = None) -> str:
        literal = '?L'
        if set_or_get_parameter:
            param_name = set_or_get_parameter.name
            param_type = set_or_get_parameter.type_in_str
        else:
            logger.debug(DataAttr_parameter.type)
            param_name = DataAttr_parameter.name
            if DataAttr_parameter.enum:
                param_type = DataAttr_parameter.enum.name
            else:
                param_type = DataAttr_parameter.type.lower().replace('xmp', '')

        if (e := self.try_get_xoa_enum_first_member(param_type)):
            literal = e
        elif 'ipv4' in param_name.lower() or 'ipv4' in param_type.lower():
            literal = '192.168.1.100'
        elif 'wild' == param_name:
            literal = '0.0.0.0'
        elif 'subnet_mask' in param_name:
            literal = '255.255.255.0'
        elif 'gateway' in param_name:
            literal = '192.168.1.1'
        elif 'ipv6' in param_name:
            literal = '::1'
        elif param_name == 'timestamp':
            literal = '2147483647'
        elif param_name == 'module_ports':
            literal = '0 0 0 1'
        elif 'List[int]' in param_type or 'indices' in param_name or 'intlist' in param_type:
            literal = '0 1'
        elif param_type == 'int':
            literal = '1'
        elif param_type == 'str':
            literal = 'A String'
        elif param_type == 'long':
            literal = '123456789123'
        elif param_type == 'byte':
            literal = '123'
        elif self.command.name == 'PEF_IPV4SRCADDR' and 'value' == param_name:
            literal = '0.0.0.0'
        elif param_type == 'List[ProtocolOption]':
            literal = '0 1 2'
        return literal

    def generate_tail_parameters(self, output_mode: FakerOutputMode, parameters: List[TailParameter]) -> str:
        result = []
        for param in parameters:
            result.append(f"<{param.name}>" if output_mode.by_name else self.get_parameter_literal(set_or_get_parameter=param))
        return ' '.join(result)

    def generate_tail_parameters_from_GetDataAttr(self):
        if not self.command.data_from_server:
            return ''

        result = []
        logger.debug(self.command)
        for param in self.command.data_from_server.fields:
            logger.debug(param)
            result.append(self.get_parameter_literal(DataAttr_parameter=param))
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
        if self.command.is_support_action_set:
            output_mode = FakerOutputMode.EXAMPLE_LITERAL
            return self.generate_method_example(output_mode, self.generate_parameters_set(output_mode))
        else: # generate example from GetDataAttr field struct
            output_mode = FakerOutputMode.EXAMPLE_LITERAL
            return self.generate_method_example(output_mode, self.generate_tail_parameters_from_GetDataAttr())


    @property
    def example_get(self) -> str:
        output_mode = FakerOutputMode.EXAMPLE_LITERAL
        return self.generate_method_example(output_mode, self.generate_parameters_get(output_mode))