"""Run file moving."""

import glob
from pathlib import Path

import click

from .config import Config


def move(is_fake=True, is_silent=False, is_recursive=False):
    """Move files as config setting."""
    config = Config()
    for i in config.list_glob_path():
        move_into = Path(i['path'])
        if move_into.exists():
            if not move_into.is_dir():
                click.echo(
                    '{} already exists. The file move setting will ignore.'.
                    format(str(move_into)))
                break
        else:
            move_into.mkdir(parents=True)

        for file in [Path(x) for x in glob.glob(i['glob'])]:
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
