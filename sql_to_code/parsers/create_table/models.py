from dataclasses import dataclass
from typing import List, Union

default_type = Union[int, str, type(None)]


@dataclass
class Attribute:
    name: str
    type: str
    is_default: bool
    default: default_type
    primary_key: bool
    nullable: bool


@dataclass
class Table:
    name: str
    schema: List[Attribute]
