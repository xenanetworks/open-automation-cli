import dataclasses
import json
import sys
from glob import glob
from ast import ClassDef, parse
from typing import Dict, Generator, List
from xoa_driver import enums as xoa_enums
from xmp_command import XMPCommand, parse_command_ast


class DocsMaker:
    def __init__(self):
        pass

    def generate_all(self, filepath: str) -> Generator[Dict, None, None]:
        source_code = ''
        with open(filepath, 'r') as fp:
            source_code = fp.read()

        tree = parse(source_code)
        # pdp(tree)
        for stmt in tree.body:
            if isinstance(stmt, ClassDef):
                xmp_command = parse_command_ast(stmt)
                d = dataclasses.asdict(xmp_command)
                yield d


def run():
    result = []
    command_path = sys.argv[1]
    command_filepaths = glob(command_path)
    docs_maker = DocsMaker()
    for filepath in command_filepaths:
        for d in docs_maker.generate_all(filepath):
            result.append(d)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    run()