from dataclasses import dataclass
from typing import List


@dataclass
class Enumeration:
    name: str
    values: List[str]

    @property
    def class_name(self):
        return self.name.replace("_", " ").title().replace(" ", "")
