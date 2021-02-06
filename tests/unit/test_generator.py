import os

from sql_to_code.generator import generate_models

test_file_name = "_result_models.py"


def test_generate_models():
    generate_models("tests/test_sql/test_schema.sql", "sqlalchemy", test_file_name)

    os.remove(test_file_name)
