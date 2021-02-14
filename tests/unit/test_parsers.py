import pytest
from sql_to_code import parsers
from sql_to_code.parsers import (
    Attribute,
    Enumeration,
    ForeignKey,
    ParserOutput,
    Reference,
    create_table,
)
from sql_to_code.utils import get_file_content, parse_commands

sql_test_files_root = "tests/test_sql"


@pytest.mark.parametrize(
    "fixture_sql_filename, parser, expected_result",
    [
        (
            f"{sql_test_files_root}/test_schema_enum.sql",
            parsers.create_enum.parser,
            Enumeration(
                name="process_state",
                values=["verification", "assessment", "processing"],
            ),
        ),
        (
            f"{sql_test_files_root}/test_schema_alter.sql",
            parsers.alter_table.parser,
            ForeignKey(
                refer_from=Reference(table_name="issue", field_name="process_id"),
                refer_to=Reference(table_name="process", field_name="process_id"),
            ),
        ),
    ],
)
def test_parsers(fixture_sql_filename, parser, expected_result: ParserOutput) -> None:
    sql_text = get_file_content(fixture_sql_filename)
    result = parser.parse(sql_text)

    assert result == expected_result


def test_table_parser() -> None:
    attributes = [
        Attribute("process_id", "int", False, None, True, False),
        Attribute("booking_id", "int", False, None, False, True),
        Attribute("ticket_id", "int", False, None, False, True),
        Attribute("created_at", "timestamp", False, None, False, True),
        Attribute("updated_at", "timestamp", False, None, False, True),
    ]

    sql_text = get_file_content("tests/test_sql/test_schema_table.sql")

    commands = parse_commands(sql_text)

    table = create_table.parser.parse(commands[0])

    assert table.name == "process"
    assert table.schema == attributes
