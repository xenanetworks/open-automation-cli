import dataclasses
import json
import sys
from glob import glob
from ast import ClassDef, parse
from typing import Dict, Generator
from xmp_command import parse_command_ast


def generate_command_from_source(filepath: str) -> Generator[Dict, None, None]:
    source_code = ''
    with open(filepath, 'r') as fp:
        source_code = fp.read()

    tree = parse(source_code)
    # pdp(tree)
    for stmt in tree.body:
        if isinstance(stmt, ClassDef):
            xmp_command = parse_command_ast(stmt)
            command = dataclasses.asdict(xmp_command)
            yield command


def run():
    all_commands = []
    command_path = sys.argv[1]
    command_filepaths = glob(command_path)
    for filepath in command_filepaths:
        for command in generate_command_from_source(filepath):
            all_commands.append(command)

    print(json.dumps(all_commands, indent=2))

if __name__ == "__main__":
    run()