from typing import List


def parse_commands(content: str) -> List[str]:
    raw_commands = content.split("\n\n")
    commands = [command.replace("\n", "") for command in raw_commands]

    return commands
