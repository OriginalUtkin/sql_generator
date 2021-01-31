from dataclasses import dataclass


@dataclass
class AlterTableContext:
    source_table_name: str
    foreign_key_name: str
    result_table_name: str
    result_table_field_name: str
