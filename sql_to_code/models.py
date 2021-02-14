from dataclasses import dataclass, field
from typing import List

from sql_to_code.parsers.create_enum.models import Enumeration
from sql_to_code.parsers.create_table.models import Table


@dataclass
class Context:
    tables: List[Table] = field(default_factory=list)
    enums: List[Enumeration] = field(default_factory=list)
