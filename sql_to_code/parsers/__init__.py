from typing import Union

from . import alter_table, create_enum, create_table
from .alter_table.models import AlterTableContext
from .create_enum.models import EnumContext
from .create_table.models import Table

ParserOutput = Union[Table, EnumContext, AlterTableContext]
