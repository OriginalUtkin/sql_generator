from sql_to_code.parsers.create_table import models, parser
from sql_to_code.utils import get_file_content, parse_commands


def test_table_parser() -> None:
    attributes = [
        models.Attribute("process_id", "int", False, None, True, False),
        models.Attribute("booking_id", "int", False, None, False, True),
        models.Attribute("ticket_id", "int", False, None, False, True),
        models.Attribute("created_at", "timestamp", False, None, False, True),
        models.Attribute("updated_at", "timestamp", False, None, False, True),
    ]

    sql_text = get_file_content("tests/test_sql/test_schema_table.sql")

    commands = parse_commands(sql_text)

    table = parser.parse(commands[0])

    assert table.name == "process"
    assert table.schema == attributes
