from dataclasses import dataclass


@dataclass
class ReferenceTo:
    table_name: str
    field_name: str


@dataclass
class ForeignKey:
    table_name: str
    field_name: str
    refer_to: ReferenceTo
