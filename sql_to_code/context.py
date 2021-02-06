from typing import List

from .models import Context, ForeignKeyContext, TableContext
from .parser_router import get_parser
from .parsers import Enumeration, ForeignKey, ParserOutput, Table


def create_context(raw_sql_commands: List[str]) -> Context:
    context = Context()

    for command in raw_sql_commands:
        parser = get_parser(sql_text=command)
        result: ParserOutput = parser.parse(command)

        if isinstance(result, Table):
            context.tables.append(TableContext(table=result))

        if isinstance(result, Enumeration):
            context.enums.append(result)

        if isinstance(result, ForeignKey):
            for table_context in context.tables:
                if table_context.table.name == result.table_name:
                    attr = list(
                        filter(
                            lambda atr: atr.name == result.field_name,
                            table_context.table.schema,
                        )
                    )[0]
                    table_context.alter_tables.append(
                        ForeignKeyContext(result, attr.type)
                    )

    return context
