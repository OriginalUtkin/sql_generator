from sql_to_code.parsers.table_parser import table_parser
from sql_to_code.parsers.command_parser import parse_commands
from sql_to_code.utils import get_file_content
from sql_to_code.parsers.table_parser import Attribute


def test_table_parser() -> None:
    attributes = [
        Attribute("process_id", "int", True),
        Attribute("booking_id", "int", False),
        Attribute("ticket_id", "int", False),
        Attribute("created_at", "timestamp", False),
        Attribute("updated_at", "timestamp", False)
    ]

    file = get_file_content("tests/test_schema_table.sql")
    create_table_command: str = parse_commands(file)[0]
    command = table_parser(create_table_command)

    assert command.name == "process"
    assert command.schema == attributes






