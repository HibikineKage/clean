"""Console commands.
"""

import click
from .add import add_new_config
from .delete import delete_config
from .list import list_configs
from .cwd import show_cwd
from .move import move


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
        exit(0)
    else:
        click.echo('Command failed.')
        exit(1)


@click.command()
@click.argument('id', type=int)
def delete(id: int):
    """Delete a file move setting.

    Arguments:
        id {int} -- the setting id
    """
    deleted_setting = delete_config(id)
    if deleted_setting:
        regexp, path = deleted_setting
        click.echo('Deleted setting: {} => {}.'.format(regexp, path))
        exit(0)
    else:
        click.echo('Command failed.')
        exit(1)


@click.command()
def list():
    """Show the list of file move settings.
    """
    list_configs()
    exit(0)


@click.command()
def cwd():
    """Show the current working directory.
    """
    show_cwd()
    exit(0)


@click.command()
@click.option('--silent', 'is_silent', flag_value=True, default=False)
@click.option('--fake', '-f', 'is_fake', flag_value=True, default=False)
@click.option(
    '--recursive', '-r', 'is_recursive', flag_value=True, default=False)
def run(is_fake, is_silent, is_recursive):
    """Clean your current directory.
    """
    move(is_fake, is_silent, is_recursive)
    exit(0)


cli.add_command(add)
cli.add_command(list)
cli.add_command(cwd)
cli.add_command(run)
cli.add_command(delete)
