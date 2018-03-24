"""Run file moving."""

from pathlib import Path

import click

from .config import Config


def move(is_fake=True, is_silent=False, is_recursive=False):
    """Move files as config setting."""
    config = Config()
    cwd = Path.cwd()
    for i in config.list_glob_path():
        move_into = Path(i['path'])
        for file in cwd.glob(i['glob']):
            file_name = file.name
            move_to = move_into / file_name
            if (move_to.exists()):
                click.echo('{} already exists. The file will not move.'.format(
                    str(move_to)))
                continue
            if not is_silent:
                click.echo('{} => {}'.format(str(file), str(move_to)))
            if is_fake:
                continue
            file.rename(move_to)
