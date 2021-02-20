test_sql = """
CREATE TABLE "process" (
  "process_id" int(10) PRIMARY KEY,
  "booking_id" int DEFAULT 10,
  "ticket_id" int NOT NULL,
  "state" process_state DEFAULT "test" NOT NULL,
  "updated_at" timestamp with time zone
);
"""

from pyparsing import *

field_name = QuotedString('"')
field_type = Word(alphas, alphanums + "(" + ")")
is_primary_key = CaselessKeyword("primary key")
is_unique = CaselessKeyword("unique")
has_default = Combine(
    CaselessKeyword("default") + Word(alphanums + '"')("default"), adjacent=False
)
is_not_null = CaselessKeyword("not null")

sql_column_parser = OneOrMore(
    field_name
    + field_type
    + Optional(is_not_null)
    + Optional(has_default)
    + Optional(is_unique)
    + Optional(is_primary_key)
)

create_table = CaselessKeyword("CREATE TABLE")
table_name = MatchFirst(QuotedString('"'))("table_name")
fields = QuotedString("(", endQuoteChar=");")("fields")

sql_create_table_parser = create_table + table_name + fields


def test_pyparsing():
    t = test_sql.replace("\n", "")
    p = sql_create_table_parser.parseString(t)
    f = []

    for x in p.fields.split(","):
        ff = sql_column_parser.parseString(x)

        f.append(ff)

    print(p)
