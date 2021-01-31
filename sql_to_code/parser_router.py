from . import parsers

parser_route_rules = [
    (lambda sql_text: "CREATE TYPE" in sql_text, parsers.enum.parser),
    (lambda sql_text: "CREATE TABLE" in sql_text, parsers.table_parser),
    (lambda sql_text: "ALTER TABLE" in sql_text, parsers.alter_parser),
]


class ParserNotFound(Exception):
    pass


def get_parser(sql_text):
    for find_route, parser in parser_route_rules:
        if find_route(sql_text):
            return parser

    raise ParserNotFound(sql_text)
