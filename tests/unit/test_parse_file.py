from sql_to_code.utils import get_file_content, parse_commands


def test_parser() -> None:
    sql_text = get_file_content("tests/fixtures_sql/test_schema.sql")

    commands = parse_commands(sql_text)

    assert len(commands) == 14
