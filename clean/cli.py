import click
from .add import add_new_config


@click.group()
def cli():
    pass


@click.command()
@click.argument('regexp')
@click.argument('path')
def add(regexp: str, path: str):
    """Add new file move setting.

    Arguments:
        regexp {str} -- file matcher
        path {str} -- where to move the file
    """
    if add_new_config(regexp, path):
        click.echo('Add new setting: {} => {}'.format(regexp, path))
    else:
        click.echo('Command failed.')
        exit(1)


cli.add_command(add)