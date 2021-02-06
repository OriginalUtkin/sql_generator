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


def remap(context: Context) -> None:
    remap_tables(context)
    remap_alter_tables(context)


def remap_tables(context: Context) -> None:
    for output in context.tables:
        for field in output.table.schema:
            try:
                field.type = FIELD_TYPES[field.type]
            except KeyError:
                enum_found = False

                for enum in context.enums:
                    if enum.name == field.type:
                        enum_found = True

                if not enum_found:
                    raise


def remap_alter_tables(context: Context) -> None:
    for output in context.tables:
        for alter_table in output.alter_tables:
            alter_table.attribute_type = FIELD_TYPES[alter_table.attribute_type]
