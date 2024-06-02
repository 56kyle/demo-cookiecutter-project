"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Demo Cookiecutter Project."""


if __name__ == "__main__":
    main(prog_name="demo-cookiecutter-project")  # pragma: no cover
