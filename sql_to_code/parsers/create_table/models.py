from dataclasses import dataclass, field
from typing import List, Union

from ..alter_table.models import Reference

default_type = Union[int, str, type(None)]


@dataclass
class Attribute:
    name: str
    type: str
    default: default_type
    is_unique: bool
    is_nullable: bool
    is_primary_key: bool
    foreign_key: Reference = field(default=None)

    @property
    def has_default(self):
        return self.default is not None

    @property
    def has_foreign_key(self):
        return self.foreign_key is not None


@dataclass
class Table:
    name: str
    schema: List[Attribute]

    @property
    def class_name(self):
        return self.name.replace("_", " ").capitalize().replace(" ", "")
