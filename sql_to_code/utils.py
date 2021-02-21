from typing import List


def get_file_content(filename: str):
    content = None

    with open(filename, "r") as file:
        content = file.read()

    return content


def parse_commands(content: str) -> List[str]:
    commands = content.split("\n\n")

    return commands
