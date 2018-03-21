"""Delete file move setting(s)."""

from pathlib import Path
import click
from .config import Config


def delete_config(id: int):
    config = Config()
    return config.delete_glob_path(id)
