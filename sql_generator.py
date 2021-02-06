from typing import List

import click
from sql_to_code.parser_router import get_parser
from sql_to_code.parsers import AlterTable, Enumeration, ParserOutput, Table
from sql_to_code.utils import get_file_content, parse_commands

from .models import Context, TableContext


@click.command()
@click.option("--input_sql", help="Path to file with raw sql commands.")
def generate_models(input_sql: str) -> None:
    file_content: str = get_file_content(filename=input_sql)
    raw_sql_commands: List[str] = parse_commands(content=file_content)

    context = Context()

    for command in raw_sql_commands:
        parser = get_parser(sql_text=command)
        result: ParserOutput = parser.parse(command)

        if isinstance(result, Table):
            context.tables.append(TableContext(table=result))

        if isinstance(result, Enumeration):
            context.enums.append(result)


if __name__ == "__main__":
    generate_models()
