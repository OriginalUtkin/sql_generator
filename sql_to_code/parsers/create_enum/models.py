from dataclasses import dataclass
from typing import List


@dataclass
class EnumContext:
    name: str
    values: List[str]
