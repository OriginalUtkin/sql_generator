from sql_to_code.parsers.command_parser import parse_commands


def test_parser(commands_file) -> None:
    commands = parse_commands(commands_file)

    assert len(commands) == 14

