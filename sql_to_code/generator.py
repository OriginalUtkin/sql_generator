import os
from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from .context import Context, create_context
from .mappers import sqlalchemy_mapper
from .utils import get_file_content, parse_commands

path = Path(__file__).parent.absolute()

env = Environment(loader=FileSystemLoader(os.path.join(path, "templates")))


def generate(template_name: str, context: Context):
    template = env.get_template(template_name)

    models_text = template.render(g=context)

    return models_text


def generate_models(input_sql: str) -> None:
    file_content: str = get_file_content(filename=input_sql)
    raw_sql_commands: List[str] = parse_commands(content=file_content)
    context: Context = create_context(raw_sql_commands)

    sqlalchemy_mapper.remap(context)

    text = generate("sqlalchemy.template", context)

    print(text)
