from sql_to_code.context import Context

FIELD_TYPES = {
    "int": "Integer",
    "char": "String",
    "varchar": "String",
    "text": "Text",
    "date": "Date",
    "boolean": "Boolean",
    "timestamp": "DateTime",
    "time": "Time",
}


def remap(context: Context):
    for table in context.tables:
        for field in table.schema:
            try:
                field.type = FIELD_TYPES[field.type]
            except KeyError:
                enum_found = False

                for enum in context.enums:
                    if enum.name == field.type:
                        enum_found = True

                if not enum_found:
                    raise
