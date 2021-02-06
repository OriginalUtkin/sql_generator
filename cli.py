import click
from sql_to_code.generator import generate_models


@click.command()
@click.option("--input_sql", help="Path to file with raw sql commands.")
def generate_models_command(input_sql: str) -> None:
    generate_models(input_sql)


if __name__ == "__main__":
    generate_models()
