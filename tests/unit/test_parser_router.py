import pytest

from sql_to_code import parsers
from sql_to_code import parser_router

test_enum_sql = """
    CREATE TYPE "process_state" AS ENUM (
        'verification',
        'assessment',
        'processing'
    );
"""

test_table_sql = """
    CREATE TABLE "process" (
        "process_id" int PRIMARY KEY,
        "booking_id" int,
        "ticket_id" int,
        "state" process_state,
        "created_at" timestamp DEFAULT (now()),
        "updated_at" timestamp
    );
"""

test_alter_sql = """
    ALTER TABLE "issue"
        ADD FOREIGN KEY ("process_id")
        REFERENCES "process" ("process_id");
"""


@pytest.mark.parametrize(
    "test_sql, expected_parser",
    [
        (test_enum_sql, parsers.enum_parser),
        (test_table_sql, parsers.table_parser),
        (test_alter_sql, parsers.alter_parser),
    ],
)
def test_parser_router(test_sql, expected_parser):
    parser = parser_router.get_parser(test_sql)

    assert parser == expected_parser
