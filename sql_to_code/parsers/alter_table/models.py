from dataclasses import dataclass


@dataclass
class Reference:
    table_name: str
    field_name: str


@dataclass
class ForeignKey:
    refer_from: Reference
    refer_to: Reference
