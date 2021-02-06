import click
from sql_to_code.generator import GENERATOR_CONFIGS, generate_models


@click.command()
@click.option("-f", "--sql_file", help="Path to file with raw sql commands.")
@click.option(
    "-o", "--output_file", help="Path to output file", default="_result_models.py"
)
@click.option(
    "-g",
    "--generator",
    help="SQL generator",
    default=list(GENERATOR_CONFIGS.keys())[0],
    type=click.Choice(list(GENERATOR_CONFIGS.keys()), case_sensitive=False),
)
def generate_models_command(sql_file: str, generator: str, output_file: str) -> None:
    generate_models(sql_file, generator, output_file)


if __name__ == "__main__":
    generate_models_command()
