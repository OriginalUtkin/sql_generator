from dataclasses import dataclass, field
from typing import List, Union

from ..alter_table.models import ReferenceTo

default_type = Union[int, str, type(None)]


@dataclass
class Attribute:
    name: str
    type: str
    is_default: bool
    default: default_type
    primary_key: bool
    nullable: bool
    foreign_key: ReferenceTo = field(default=None)


@dataclass
class Table:
    name: str
    schema: List[Attribute]

    @property
    def class_name(self):
        return self.name.replace("_", " ").capitalize().replace(" ", "")
