from typing import List

from sql_to_code.parsers import ParserOutput, Table

FIELD_TYPES = {
    "int": "Integer",
    "char": "String",
    "varchar": "String",
    "text": "Text",
    "date": "Date",
    "boolean": "Boolean",
    "time": "Time",
}


def remap(context: List[ParserOutput]):
    for output in context:
        if isinstance(output, Table):
            for field in output.schema:
                field.type = FIELD_TYPES[field.type]
