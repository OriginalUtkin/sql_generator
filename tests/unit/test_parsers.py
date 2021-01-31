import pytest

from sql_to_code import parsers
from sql_to_code.utils import get_file_content


@pytest.mark.parametrize(
    "fixture_sql_filename, parser",
    [("tests/fixtures_sql/test_schema_enum.sql", parsers.enum_parser)],
)
def test_parser(fixture_sql_filename, parser):
    sql_text = get_file_content(fixture_sql_filename)

    result = parser(sql_text)
