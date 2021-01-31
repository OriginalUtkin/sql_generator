from typing import List
import pathlib


def parse_commands() -> List[str]:
    file_path = f"{str(pathlib.Path(__file__).parent.absolute())}/tests/test_schema.sql"

    sql_file = open(file_path, "r").read()
    raw_commands = sql_file.split('\n\n')
    commands = [command.replace('\n', '') for command in raw_commands]

    return commands


if __name__ == "__main__":
    file = parse_commands()




