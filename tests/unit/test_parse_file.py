from sql_to_code.utils import get_file_content

from sql_to_code.parsers.command_parser import parse_commands


def test_parser() -> None:
    sql_text = get_file_content("tests/fixtures_sql/test_schema.sql")

    commands = parse_commands(sql_text)

    assert len(commands) == 14
