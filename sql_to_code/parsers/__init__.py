from typing import Union

from . import alter_table, create_enum, create_table
from .alter_table.models import AlterTable
from .create_enum.models import Enumeration
from .create_table.models import Table

ParserOutput = Union[Table, Enumeration, AlterTable]
