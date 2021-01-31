import pytest

from sql_to_code import parsers
from sql_to_code.utils import get_file_content


@pytest.mark.parametrize(
    "fixture_sql_filename, parser",
    [
        ("tests/fixtures_sql/test_schema_enum.sql", parsers.enum.parser),
        ("tests/fixtures_sql/test_schema_alter.sql", parsers.alter_table.parser),
    ],
)
def test_parsers(fixture_sql_filename, parser):
    sql_text = get_file_content(fixture_sql_filename)

    result = parser.parse(sql_text)
