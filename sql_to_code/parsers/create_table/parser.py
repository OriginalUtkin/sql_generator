from pyparsing import (
    CaselessKeyword,
    Group,
    Literal,
    MatchFirst,
    OneOrMore,
    Optional,
    QuotedString,
    Suppress,
    Word,
    alphanums,
    alphas,
)
from pyparsing import pyparsing_common as ppc
from pyparsing import quotedString

from .models import Attribute, Table

# table schema
create_table = CaselessKeyword("create table")
table_name = MatchFirst(QuotedString('"'))("table_name")

# field schema
column_name = QuotedString('"')("column_name")

# column type:
# "(" ")" - because of varchar(40)
# "_" - because of enums like process_type
column_type = Word(alphas, alphanums + "(" + ")" + "_")("column_type")
is_primary_key = CaselessKeyword("primary key")
is_unique = CaselessKeyword("unique")("is_unique")

date_time_now = Word("now()")
default_value = quotedString | ppc.real | ppc.signed_integer | date_time_now
has_default = CaselessKeyword("default") + default_value("default_value")

is_not_null = CaselessKeyword("not null")("is_not_null")


table_columns = OneOrMore(
    Group(
        column_name
        + column_type
        + (
            Optional(is_not_null)
            & Optional(has_default)
            & Optional(is_unique)
            & Optional(is_primary_key)
        )
        + Optional(Suppress(","))
    )
)("table_columns")

create_table_schema = (
    create_table + table_name + Literal("(") + table_columns + Literal(");")
)


def parse(sql_text: str) -> Table:
    result = create_table_schema.parseString(sql_text)

    table = Table(
        result.table_name,
        [
            Attribute(
                name=column.column_name,
                type=column.column_type,
                default=column.default_value if column.default_value else None,
                is_unique=bool(column.is_unique),
                is_nullable=not bool(column.is_not_null),
                is_primary_key=bool(column.is_primary_key),
            )
            for column in result.table_columns
        ],
    )

    return table
