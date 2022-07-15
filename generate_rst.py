import sys
from ast import ClassDef, parse
from glob import glob
from loguru import logger
from typing import Generator, List
from cli_command import CLICommand, CLICommandFaker, parse_command_ast
from astpp import pdp


RST_TEMPLATE = '''``{name}``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    {syntax}

:Description:
    {description}

:Actions:
    {actions}

:Parameter:
    {parameter}

:Example:
    .. code-block::

        {example}

'''


class RSTMaker:
    def __init__(self):
        pass

    def generate_parameter_description(self, command: CLICommand):
        result = []
        for param in command.tail_parameters_set:
            name_with_type = f"{param.name}: <{param.cli_type}>"
            whole_line = f"``{name_with_type}``, {param.description}\n"
            result.append(whole_line)

        return '\n    '.join(result)

    def generate_actions(self, command: CLICommand):
        result = [
            'set' if command.actions.is_set_support else '',
            'get' if command.actions.is_get_support else '',
        ]
        return ', '.join(filter(None, result))

    def generate_syntax(self, faker: CLICommandFaker):
        result = []
        if faker.command.actions.is_set_support:
            result.extend(['# set', faker.syntax_set + '\n' if faker.command.actions.is_set_support else ''])
        if faker.command.actions.is_get_support:
            result.extend(['# get', faker.syntax_get])
        return '\n    '.join(filter(None, result))

    def generate_example(self, faker: CLICommandFaker):
        result = []
        if faker.command.actions.is_set_support:
            result.extend(
                [
                    '# set',
                    f"input:  {faker.example_set}",
                    'output: <OK>' + '\n' if faker.command.actions.is_set_support else ''
                ]
            )
        if faker.command.actions.is_get_support:
            result.extend(
                [
                    '# get',
                    f"input:  {faker.example_get}",
                    f"output: {faker.example_set}",
                ]
            )
        return '\n        '.join(filter(None, result))

    def generate_single_command_rst(self, command: CLICommand) -> str:
        faker = CLICommandFaker(command)
        return RST_TEMPLATE.format(**{
            'name': command.name,
            'description': command.description,
            'syntax': self.generate_syntax(faker),
            'example': self.generate_example(faker),
            'actions': self.generate_actions(command),
            'parameter': self.generate_parameter_description(command),
        })

    def generate_all(self, source_code: str) -> Generator[str, None, None]:
        tree = parse(source_code)
        # pdp(tree)
        for stmt in tree.body:
            if isinstance(stmt, ClassDef):
                cli_command = parse_command_ast(stmt)
                rst = self.generate_single_command_rst(cli_command)
                yield rst


def read_file(filepath: str):
    with open(filepath, 'r') as fp:
        return fp.read()


def run():
    command_path = sys.argv[1]
    command_filepaths = glob(command_path)
    rst_maker = RSTMaker()
    for filepath in command_filepaths:
        source_code = read_file(filepath)
        for rst in rst_maker.generate_all(source_code):
            print(rst)


if __name__ == "__main__":
    run()