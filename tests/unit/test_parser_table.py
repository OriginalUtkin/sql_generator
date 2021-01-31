from sql_to_code.parsers.create_table import parser
from sql_to_code.parsers.create_table import models
from sql_to_code.utils import get_file_content, parse_commands


def test_table_parser() -> None:
    attributes = [
        models.Attribute("process_id", "int", True),
        models.Attribute("booking_id", "int", False),
        models.Attribute("ticket_id", "int", False),
        models.Attribute("created_at", "timestamp", False),
        models.Attribute("updated_at", "timestamp", False),
    ]

    sql_text = get_file_content("tests/fixtures_sql/test_schema_table.sql")

    commands = parse_commands(sql_text)

    table = parser.parse(commands[0])

    assert table.name == "process"
    assert table.schema == attributes
