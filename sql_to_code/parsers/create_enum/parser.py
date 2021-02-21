from pyparsing import *

from .models import Enumeration

enum_schema = (
    CaselessKeyword("create type")
    + QuotedString('"')("enum_name")
    + CaselessKeyword("as enum")
    + CaselessKeyword("(")
    + Group(OneOrMore(QuotedString("'") + Optional(Suppress(","))))("enum_values")
    + CaselessKeyword(");")
)


def parse(sql_text: str):
    result = enum_schema.parseString(sql_text)

    return Enumeration(result.enum_name, result.enum_values.asList())
