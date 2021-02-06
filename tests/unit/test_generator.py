from sql_to_code.generator import generate_models


def test_generate_models():
    generate_models("tests/test_sql/test_schema.sql")
