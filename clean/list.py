import click
from .config import Config


def list_configs():
    config = Config()
    for i in config.get_config()['path']:
        click.echo('{} => {}'.format(i['regexp'], i['path']))
