from typing import List

import click
from sql_to_code.parser_router import get_parser
from sql_to_code.parsers import ParserOutput
from sql_to_code.utils import get_file_content, parse_commands


@click.command()
@click.option("--input_sql", help="Path to file with raw sql commands.")
def generate_models(input_sql: str) -> None:
    file_content: str = get_file_content(filename=input_sql)
    raw_sql_commands: List[str] = parse_commands(content=file_content)

    context: List[ParserOutput] = []

    for command in raw_sql_commands:
        parser = get_parser(sql_text=command)
        result: ParserOutput = parser.parse(command)

        context.append(result)


if __name__ == "__main__":
    generate_models()
