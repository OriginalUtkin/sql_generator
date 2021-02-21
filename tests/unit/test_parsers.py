import pytest
from sql_to_code import parsers
from sql_to_code.parsers import (
    Table,
    Attribute,
    Enumeration,
    ForeignKey,
    ParserOutput,
    Reference,
)
from sql_to_code.utils import get_file_content

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
                refer_from=Reference(table_name="issue", field_name="process_id_test"),
                refer_to=Reference(table_name="process", field_name="process_id"),
            ),
        ),
        (
            f"{sql_test_files_root}/test_schema_table.sql",
            parsers.create_table.parser,
            Table(
                name="process",
                schema=[
                    Attribute(
                        name="process_id",
                        type="int",
                        default=None,
                        is_unique=False,
                        is_nullable=True,
                        is_primary_key=False,
                        foreign_key=None,
                    ),
                    Attribute(
                        name="booking_id",
                        type="int",
                        default="10",
                        is_unique=False,
                        is_nullable=True,
                        is_primary_key=False,
                        foreign_key=None,
                    ),
                    Attribute(
                        name="state",
                        type="process_state",
                        default='"verification"',
                        is_unique=False,
                        is_nullable=False,
                        is_primary_key=False,
                        foreign_key=None,
                    ),
                    Attribute(
                        name="created_at",
                        type="timestamp",
                        default=None,
                        is_unique=False,
                        is_nullable=True,
                        is_primary_key=False,
                        foreign_key=None,
                    ),
                    Attribute(
                        name="updated_at",
                        type="timestamp",
                        default=None,
                        is_unique=False,
                        is_nullable=True,
                        is_primary_key=False,
                        foreign_key=None,
                    ),
                ],
            ),
        ),
    ],
)
def test_parsers(fixture_sql_filename, parser, expected_result: ParserOutput) -> None:
    sql_text = get_file_content(fixture_sql_filename)
    result = parser.parse(sql_text)

    assert result == expected_result
