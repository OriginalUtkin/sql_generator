from typing import List
from dataclasses import dataclass


@dataclass
class EnumContext:
    name: str
    values: List[str]
