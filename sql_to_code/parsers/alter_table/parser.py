import re

from .models import AlterTable

source_table_name_regex = re.compile('ALTER TABLE "(?P<table_name>\w+)"')
foreign_key_name_regex = re.compile('ADD FOREIGN KEY \("(?P<foreign_key>\w+)"\)')
result_table_name_regex = re.compile('REFERENCES "(?P<result_table_name>\w+)"')
result_table_field_name_regex = re.compile(
    'REFERENCES "\w+" \("(?P<result_table_field_name>\w+)"\);'
)


def parse(sql_text: str):
    source_table_name = source_table_name_regex.search(sql_text).groupdict()[
        "table_name"
    ]
    foreign_key_name = foreign_key_name_regex.search(sql_text).groupdict()[
        "foreign_key"
    ]
    result_table_name = result_table_name_regex.search(sql_text).groupdict()[
        "result_table_name"
    ]
    result_table_field_name = result_table_field_name_regex.search(
        sql_text
    ).groupdict()["result_table_field_name"]

    return AlterTable(
        source_table_name, foreign_key_name, result_table_name, result_table_field_name,
    )
