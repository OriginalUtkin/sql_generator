from typing import Union

from . import alter_table, create_enum, create_table
from .alter_table.models import AlterTable, ForeignKey
from .create_enum.models import Enumeration
from .create_table.models import Attribute, Table

ParserOutput = Union[Table, Enumeration, AlterTable]
