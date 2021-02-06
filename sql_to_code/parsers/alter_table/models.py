from dataclasses import dataclass


@dataclass
class ForeignKey:
    table_name: str
    field_name: str


@dataclass
class AlterTable:
    table_name: str
    field_name: str
    refer_to: ForeignKey
