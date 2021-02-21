from sql_to_code.utils import get_file_content, parse_commands


def test_parse_sql_commands() -> None:
    result_commands = [
        "CREATE TYPE \"process_state\" AS ENUM (\n  'verification',\n  'assessment',\n  'processing'\n);",
        "CREATE TYPE \"issue_type\" AS ENUM (\n  'could_not_verify',\n  'segment_not_available',\n  'priority_boarding_sold_out',\n  'schedule_change',\n  'invalid_pax_name',\n  'price_change',\n  'vpn_issues'\n);",
        "CREATE TYPE \"user_action_type\" AS ENUM (\n  'send_email'\n);",
        "CREATE TYPE \"passenger_segment_state\" AS ENUM (\n  'pending',\n  'issue',\n  'processed',\n  'not_processed'\n);",
        'CREATE TABLE "process" (\n  "process_id" int PRIMARY KEY,\n  "booking_id" int,\n  "ticket_id" int,\n  "state" process_state,\n  "created_at" timestamp DEFAULT (now()),\n  "updated_at" timestamp\n);',
        'CREATE TABLE "issue" (\n  "issue_id" int PRIMARY KEY,\n  "process_id" int,\n  "type" issue_type,\n  "created_at" timestamp DEFAULT (now())\n);',
        'CREATE TABLE "user_action" (\n  "email" varchar,\n  "type" user_action_type,\n  "issue_id" int,\n  "process_id" int,\n  "passenger_segment_id" int,\n  "created_at" timestamp DEFAULT (now())\n);',
        'CREATE TABLE "passenger_segment" (\n  "passenger_segment_id" int PRIMARY KEY,\n  "process_id" int,\n  "passenger_id" int,\n  "segment_id" varchar,\n  "state" passenger_segment_state,\n  "issue_id" int,\n  "updated_at" timestamp,\n  "created_at" timestamp DEFAULT (now())\n);',
        'ALTER TABLE "issue" ADD FOREIGN KEY ("process_id") REFERENCES "process" ("process_id");',
        'ALTER TABLE "user_action" ADD FOREIGN KEY ("issue_id") REFERENCES "issue" ("issue_id");',
        'ALTER TABLE "user_action" ADD FOREIGN KEY ("process_id") REFERENCES "process" ("process_id");',
        'ALTER TABLE "user_action" ADD FOREIGN KEY ("passenger_segment_id") REFERENCES "passenger_segment" ("passenger_segment_id");',
        'ALTER TABLE "passenger_segment" ADD FOREIGN KEY ("process_id") REFERENCES "process" ("process_id");',
        'ALTER TABLE "passenger_segment" ADD FOREIGN KEY ("issue_id") REFERENCES "issue" ("issue_id");\n',
    ]
    sql_text = get_file_content("tests/test_sql/test_schema.sql")

    commands = parse_commands(sql_text)

    assert commands == result_commands
