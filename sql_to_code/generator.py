from typing import Dict
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("./templates"))


def generate(template_name: str, context: Dict):
    template = env.get_template(template_name)

    models_text = template.render(**context)

    return models_text
