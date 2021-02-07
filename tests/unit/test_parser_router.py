import pytest
from sql_to_code import parser_router, parsers
from sql_to_code.utils import get_file_content

sql_test_files_root = "tests/test_sql"


@pytest.mark.parametrize(
    "test_sql, expected_parser",
    [
        (f"{sql_test_files_root}/test_schema_enum.sql", parsers.create_enum.parser),
        (f"{sql_test_files_root}/test_schema_alter.sql", parsers.alter_table.parser),
        (f"{sql_test_files_root}/test_schema_table.sql", parsers.create_table.parser),
    ],
)
def test_parser_router(test_sql, expected_parser) -> None:
    sql_text = get_file_content(test_sql)

    parser = parser_router.get_parser(sql_text)

    assert parser == expected_parser
