import pytest

from sql_to_code import parsers
from sql_to_code import parser_router
from sql_to_code.utils import get_file_content


@pytest.mark.parametrize(
    "test_sql, expected_parser",
    [
        ("tests/fixtures_sql/test_schema_enum.sql", parsers.enum.parser),
        ("tests/fixtures_sql/test_schema_table.sql", parsers.table_parser),
        ("tests/fixtures_sql/test_schema_alter.sql", parsers.alter_parser),
    ],
)
def test_parser_router(test_sql, expected_parser):
    sql_text = get_file_content(test_sql)

    parser = parser_router.get_parser(sql_text)

    assert parser == expected_parser
