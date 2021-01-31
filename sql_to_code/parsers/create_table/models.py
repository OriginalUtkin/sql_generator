from typing import List

from dataclasses import dataclass


@dataclass
class Attribute:
    name: str
    type: str
    primary_key: bool


@dataclass
class Table:
    name: str
    schema: List[Attribute]
