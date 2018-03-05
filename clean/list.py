import click
from .config import Config


def list_configs():
    config = Config()
    for i in config.list_glob_path():
        click.echo('{} => {}'.format(i['glob'], i['path']))
