from dataclasses import dataclass
from typing import List


@dataclass
class Enumeration:
    name: str
    values: List[str]
