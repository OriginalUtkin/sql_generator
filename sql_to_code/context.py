from typing import Any, List

from .models import Context
from .parser_router import get_parser
from .parsers import Attribute, Enumeration, ForeignKey, ParserOutput, Table


def create_context(raw_sql_commands: List[str]) -> Context:
    context = Context()

    for command in raw_sql_commands:
        parser = get_parser(sql_text=command)
        result: ParserOutput = parser.parse(command)

        if isinstance(result, Table):
            context.tables.append(result)

        if isinstance(result, Enumeration):
            context.enums.append(result)

        if isinstance(result, ForeignKey):
            table: Table = find_field(context.tables, result.refer_from.table_name)
            attribute: Attribute = find_field(
                table.schema, result.refer_from.field_name
            )

            attribute.foreign_key = result.refer_to

    return context


def find_field(iterable: List[Any], equivalent_to: str):
    return next(filter(lambda elem: elem.name == equivalent_to, iterable))
