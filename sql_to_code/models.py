from dataclasses import dataclass, field
from typing import List

from sql_to_code.parsers.alter_table.models import AlterTable
from sql_to_code.parsers.create_enum.models import Enumeration
from sql_to_code.parsers.create_table.models import Table


@dataclass
class TableContext:
    table: Table
    alter_tables: List[AlterTable] = field(default_factory=list)


@dataclass
class Context:
    tables: List[TableContext] = field(default_factory=list)
    enums: List[Enumeration] = field(default_factory=list)
