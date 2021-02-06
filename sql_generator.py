from typing import List

import click
from models import Context, TableContext
from sql_to_code.parser_router import get_parser
from sql_to_code.parsers import AlterTable, Enumeration, ParserOutput, Table
from sql_to_code.utils import get_file_content, parse_commands


def create_context(raw_sql_commands: List[str]) -> Context:
    context = Context()

    for command in raw_sql_commands:
        parser = get_parser(sql_text=command)
        result: ParserOutput = parser.parse(command)

        if isinstance(result, Table):
            context.tables.append(TableContext(table=result))

        if isinstance(result, Enumeration):
            context.enums.append(result)

        if isinstance(result, AlterTable):
            for table in context.tables:
                if table.table.name == result.source_table_name:
                    table.alter_tables.append(result)

    return context


def _generate_models(input_sql: str) -> None:
    file_content: str = get_file_content(filename=input_sql)
    raw_sql_commands: List[str] = parse_commands(content=file_content)
    _: Context = create_context(raw_sql_commands)


@click.command()
@click.option("--input_sql", help="Path to file with raw sql commands.")
def generate_models(input_sql: str) -> None:
    _generate_models(input_sql)


if __name__ == "__main__":
    generate_models()
