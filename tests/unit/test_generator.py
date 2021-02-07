from unittest.mock import call

from sql_to_code.generator import generate_models


def test_generate_models(mocker) -> None:
    test_file_name = "_result_models.py"
    open_mock = mocker.patch("sql_to_code.generator.open")

    generate_models("tests/test_sql/test_schema.sql", "sqlalchemy", test_file_name)

    assert open_mock
    assert open_mock.call_args == call(test_file_name, "w")
