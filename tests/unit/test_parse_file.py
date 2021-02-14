from sql_to_code.utils import get_file_content, parse_commands


def test_parse_sql_commands() -> None:
    result_commands = [
        "CREATE TYPE \"process_state\" AS ENUM (  'verification',  'assessment',  'processing');",
        "CREATE TYPE \"issue_type\" AS ENUM (  'could_not_verify',  'segment_not_available',  'priority_boarding_sold_out',  'schedule_change',  'invalid_pax_name',  'price_change',  'vpn_issues');",
        "CREATE TYPE \"user_action_type\" AS ENUM (  'send_email');",
        "CREATE TYPE \"passenger_segment_state\" AS ENUM (  'pending',  'issue',  'processed',  'not_processed');",
        'CREATE TABLE "process" (  "process_id" int PRIMARY KEY,  "booking_id" int,  "ticket_id" int,  "state" process_state,  "created_at" timestamp DEFAULT (now()),  "updated_at" timestamp);',
        'CREATE TABLE "issue" (  "issue_id" int PRIMARY KEY,  "process_id" int,  "type" issue_type,  "created_at" timestamp DEFAULT (now()));',
        'CREATE TABLE "user_action" (  "id" int PRIMARY KEY,  "email" varchar,  "type" user_action_type,  "issue_id" int,  "process_id" int,  "passenger_segment_id" int,  "created_at" timestamp DEFAULT (now()));',
        'CREATE TABLE "passenger_segment" (  "passenger_segment_id" int PRIMARY KEY,  "process_id" int,  "passenger_id" int,  "segment_id" varchar,  "state" passenger_segment_state,  "issue_id" int,  "updated_at" timestamp,  "created_at" timestamp DEFAULT (now()));',
        'ALTER TABLE "issue" ADD FOREIGN KEY ("process_id") REFERENCES "process" ("process_id");',
        'ALTER TABLE "user_action" ADD FOREIGN KEY ("issue_id") REFERENCES "issue" ("issue_id");',
        'ALTER TABLE "user_action" ADD FOREIGN KEY ("process_id") REFERENCES "process" ("process_id");',
        'ALTER TABLE "user_action" ADD FOREIGN KEY ("passenger_segment_id") REFERENCES "passenger_segment" ("passenger_segment_id");',
        'ALTER TABLE "passenger_segment" ADD FOREIGN KEY ("process_id") REFERENCES "process" ("process_id");',
        'ALTER TABLE "passenger_segment" ADD FOREIGN KEY ("issue_id") REFERENCES "issue" ("issue_id");',
    ]
    sql_text = get_file_content("tests/test_sql/test_schema.sql")

    commands = parse_commands(sql_text)

    assert commands == result_commands
