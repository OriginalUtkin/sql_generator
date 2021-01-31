import re
from typing import List

from .models import Attribute, Table, default_type

regex_name_schema: str = r'CREATE TABLE "([\S\d]+)"\s*\(\s*(.+)\s*\);'
name_and_type_regex = r"(^[\S\d]+)\s([\S]+)\s*"
default_regex = r"DEFAULT\s+(.?)+\s*"


def parse(sql_text: str) -> Table:
    table_name, schema = re.findall(regex_name_schema, sql_text)[0]
    all_attributes: List[str] = schema.split(",")
    schema: List[str] = map(
        lambda attribute: attribute.strip().replace('"', ""), all_attributes
    )
    attributes = parse_attributes(schema)

    return Table(table_name, attributes)


def parse_attributes(schema) -> List[Attribute]:
    attributes = list()

    for attribute in schema:
        name, a_type = re.findall(pattern=name_and_type_regex, string=attribute)[0]

        is_pk = "PRIMARY KEY" in attribute.upper()
        is_default = not is_pk and "DEFAULT" in attribute.upper()

        attributes.append(
            Attribute(
                name=name,
                type=a_type,
                primary_key=is_pk,
                nullable="NOT NULL" not in attribute.upper() and not is_pk,
                is_default=is_default,
                default=parse_default(attribute) if is_default else None,
            )
        )

    return attributes


def parse_default(sql_command: str) -> default_type:
    return re.findall(default_regex, sql_command)[0]
