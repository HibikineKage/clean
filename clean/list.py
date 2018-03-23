import click
from .config import Config


def list_configs():
    config = Config()
    glob_paths = config.list_glob_path()
    if len(glob_paths) == 0:
        click.echo(
            'No path settings. To add new setting, please use "clean add".')
    for i in enumerate(config.list_glob_path()):
        click.echo('[{}] {} => {}'.format(i[0], i[1]['glob'], i[1]['path']))
