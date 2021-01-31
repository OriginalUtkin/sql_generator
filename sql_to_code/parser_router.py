from .parsers import alter_parser, table_parser, enum_parser

parser_route_rules = [
    (lambda sql_text: "CREATE TYPE" in sql_text, enum_parser),
    (lambda sql_text: "CREATE TABLE" in sql_text, table_parser),
    (lambda sql_text: "ALTER TABLE" in sql_text, alter_parser),
]


class ParserNotFound(Exception):
    pass


def get_parser(sql_text):
    for find_route, parser in parser_route_rules:
        if find_route(sql_text):
            return parser

    raise ParserNotFound(sql_text)
