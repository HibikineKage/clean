from pathlib import Path
import click


def show_cwd():
    click.echo(str(Path.cwd()))