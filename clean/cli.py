import click
from .add import add_new_config
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
    else:
        click.echo('Command failed.')
        exit(1)


@click.command()
def list():
    """Show the list of file move settings.
    """

    list_configs()


@click.command()
def cwd():
    """Show the current working directory.
    """

    show_cwd()


@click.command()
@click.option('--silent', 'is_silent', flag_value=True, default=False)
@click.option('--fake', '-f', 'is_fake', flag_value=True, default=False)
@click.option(
    '--recursive', '-r', 'is_recursive', flag_value=True, default=False)
def run(is_fake, is_silent, is_recursive):
    """Clean your current directory.
    """

    move(is_fake, is_silent, is_recursive)


cli.add_command(add)
cli.add_command(list)
cli.add_command(cwd)
cli.add_command(run)