from typing import List

from .models import Context, TableContext
from .parser_router import get_parser
from .parsers import AlterTable, Enumeration, ParserOutput, Table


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
            for table_context in context.tables:
                if table_context.table.name == result.table_name:
                    table_context.alter_tables.append(result)

    return context
