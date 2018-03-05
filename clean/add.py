"""Add new file move setting."""

from pathlib import Path
import click
from .config import Config


def add_new_config(glob: str, path: str):
    config = Config()
    return config.add_glob_path(glob, path)
