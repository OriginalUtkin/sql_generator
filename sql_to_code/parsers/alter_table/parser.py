import re

from .models import ForeignKey, Reference

from pyparsing import *


table_name_schema = CaselessKeyword("alter table") + QuotedString('"')("table_name")
foreign_key_schema = CaselessKeyword("add foreign key") + QuotedString(
    '("', endQuoteChar='")'
)("foreign_key")
reference_table = CaselessKeyword("references") + QuotedString('"')("reference_table")
reference_table_column_name = QuotedString('("', endQuoteChar='")')(
    "reference_table_column_name"
)

add_foreign_key_schema = (
    table_name_schema
    + foreign_key_schema
    + reference_table
    + reference_table_column_name
)


def parse(sql_text: str):
    result = add_foreign_key_schema.parseString(sql_text)

    return ForeignKey(
        refer_from=Reference(
            table_name=result.table_name, field_name=result.foreign_key
        ),
        refer_to=Reference(
            table_name=result.reference_table,
            field_name=result.reference_table_column_name,
        ),
    )
