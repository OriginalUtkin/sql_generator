from pyparsing import CaselessKeyword, QuotedString, delimitedList

from .models import Enumeration

enum_schema = (
    CaselessKeyword("create type")
    + QuotedString('"')("enum_name")
    + CaselessKeyword("as enum")
    + CaselessKeyword("(")
    + delimitedList(QuotedString("'"))("enum_values")
    + CaselessKeyword(");")
)


def parse(sql_text: str):
    result = enum_schema.parseString(sql_text)

    return Enumeration(result.enum_name, list(result.enum_values))
