import re

from .models import EnumContext

NAME_REGEX = re.compile('CREATE TYPE "(?P<name>\w+)"')
VALUE_REGEX = re.compile("'(\w+)'")


def parse(sql_text: str):
    name = NAME_REGEX.search(sql_text).groupdict()["name"]
    values = VALUE_REGEX.findall(sql_text)

    return EnumContext(name, values)
