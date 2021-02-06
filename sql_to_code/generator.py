import os
from pathlib import Path
from typing import List

from black import FileMode, format_str
from jinja2 import Environment, FileSystemLoader

from . import mappers
from .context import Context, create_context
from .utils import get_file_content, parse_commands

path = Path(__file__).parent.absolute()

env = Environment(loader=FileSystemLoader(os.path.join(path, "templates")))


def generate(template_name: str, context: Context) -> str:
    template = env.get_template(template_name)

    models_text = template.render(g=context)

    return models_text


GENERATOR_CONFIGS = {"sqlalchemy": (mappers.sqlalchemy_mapper, "sqlalchemy.template")}


def generate_models(input_sql: str, generator: str, output_file: str) -> None:
    file_content: str = get_file_content(filename=input_sql)
    raw_sql_commands: List[str] = parse_commands(content=file_content)
    context: Context = create_context(raw_sql_commands)

    remmaper, output_template = GENERATOR_CONFIGS[generator]

    remmaper.remap(context)
    models_text = generate(output_template, context)

    formatted_models_text = format_str(models_text, mode=FileMode())

    with open(output_file, "w") as output:
        output.write(formatted_models_text)
