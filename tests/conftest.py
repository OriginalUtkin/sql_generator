import pytest
import pathlib
from typing import List


@pytest.fixture
def commands_file() -> List[str]:
    file_path = f"{str(pathlib.Path(__file__).parent.absolute())}/test_schema.sql"

    with open(file_path, "r") as file:
        yield file.read()
