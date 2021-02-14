from sql_to_code.context import create_context
from sql_to_code.models import Context
from sql_to_code.parsers import Attribute, Enumeration, Reference, Table
from sql_to_code.utils import get_file_content, parse_commands

test_context = Context(
    tables=[
        Table(
            name="process",
            schema=[
                Attribute(
                    name="process_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=True,
                    nullable=False,
                    foreign_key=None,
                ),
                Attribute(
                    name="booking_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="ticket_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="state",
                    type="process_state",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="created_at",
                    type="timestamp",
                    is_default=True,
                    default="",
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="updated_at",
                    type="timestamp",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
            ],
        ),
        Table(
            name="issue",
            schema=[
                Attribute(
                    name="issue_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=True,
                    nullable=False,
                    foreign_key=None,
                ),
                Attribute(
                    name="process_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=Reference(
                        table_name="process", field_name="process_id"
                    ),
                ),
                Attribute(
                    name="type",
                    type="issue_type",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="created_at",
                    type="timestamp",
                    is_default=True,
                    default="",
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
            ],
        ),
        Table(
            name="user_action",
            schema=[
                Attribute(
                    name="id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=True,
                    nullable=False,
                    foreign_key=None,
                ),
                Attribute(
                    name="email",
                    type="varchar",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="type",
                    type="user_action_type",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="issue_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=Reference(table_name="issue", field_name="issue_id"),
                ),
                Attribute(
                    name="process_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=Reference(
                        table_name="process", field_name="process_id"
                    ),
                ),
                Attribute(
                    name="passenger_segment_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=Reference(
                        table_name="passenger_segment",
                        field_name="passenger_segment_id",
                    ),
                ),
                Attribute(
                    name="created_at",
                    type="timestamp",
                    is_default=True,
                    default="",
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
            ],
        ),
        Table(
            name="passenger_segment",
            schema=[
                Attribute(
                    name="passenger_segment_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=True,
                    nullable=False,
                    foreign_key=None,
                ),
                Attribute(
                    name="process_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=Reference(
                        table_name="process", field_name="process_id"
                    ),
                ),
                Attribute(
                    name="passenger_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="segment_id",
                    type="varchar",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="state",
                    type="passenger_segment_state",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="issue_id",
                    type="int",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=Reference(table_name="issue", field_name="issue_id"),
                ),
                Attribute(
                    name="updated_at",
                    type="timestamp",
                    is_default=False,
                    default=None,
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
                Attribute(
                    name="created_at",
                    type="timestamp",
                    is_default=True,
                    default="",
                    primary_key=False,
                    nullable=True,
                    foreign_key=None,
                ),
            ],
        ),
    ],
    enums=[
        Enumeration(
            name="process_state", values=["verification", "assessment", "processing"]
        ),
        Enumeration(
            name="issue_type",
            values=[
                "could_not_verify",
                "segment_not_available",
                "priority_boarding_sold_out",
                "schedule_change",
                "invalid_pax_name",
                "price_change",
                "vpn_issues",
            ],
        ),
        Enumeration(name="user_action_type", values=["send_email"]),
        Enumeration(
            name="passenger_segment_state",
            values=["pending", "issue", "processed", "not_processed"],
        ),
    ],
)


def test_create_context() -> None:
    sql_file = get_file_content("tests/test_sql/test_schema.sql")
    sql_commands = parse_commands(sql_file)

    context = create_context(sql_commands)
    assert context == test_context
