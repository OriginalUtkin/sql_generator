import re
from typing import List

from .models import Table, Attribute

regex_table_name: str = r'CREATE TABLE "([\S\d]+)"'
regex_table_schema: str = r'CREATE TABLE "[\S\d]+\"\s*\(\s*(.+)\s*\);'


def parse(sql_text: str) -> Table:
    table_name: str = re.findall(regex_table_name, sql_text)[0]
    all_attributes: List[str] = re.findall(regex_table_schema, sql_text)[0].split(",")
    schema: List[str] = map(
        lambda attribute: attribute.strip().replace('"', ""), all_attributes
    )
    attributes = parse_attributes(schema)

    return Table(table_name, attributes)


def parse_attributes(schema) -> List[Attribute]:
    name_and_type_regex = r"(^[\S\d]+)\s([\S]+)\s*"
    attributes = list()

    for attribute in schema:
        name, a_type = re.findall(pattern=name_and_type_regex, string=attribute)[0]
        attributes.append(Attribute(name, a_type, "PRIMARY KEY" in attribute.upper()))

    return attributes
