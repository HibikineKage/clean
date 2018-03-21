"""Config file manager.
"""

from pathlib import Path
import json
import click
config_file_name = '.cleanrc'
default_config_path = Path.home() / config_file_name


def is_valid_glob_path(glob_and_path):
    if not 'path' in glob_and_path:
        return False
    if not 'glob' in glob_and_path:
        return False
    return True


class Config:
    """Config file manager class.

    Returns:
        Config -- config file instance

    """

    def __init__(self, config_path=default_config_path):
        """initialize config class.

        Keyword Arguments:
            config_path {Path} -- set config file path (default: {default_config_path})
        """

        self.config_path = config_path
        if not self.config_path.is_file():
            if self.config_path.exists():
                click.echo(
                    'Can\'t create file. Same name something is exist. Please check your home\'s {}.'.
                    format(config_file_name))
                exit(1)
            self.create_new_config_file()

        self.load_file()

    def add_glob_path(self, glob: str, path: str):
        self.config['path'].append({'glob': glob, 'path': path})
        self.save_file()
        return True

    def delete_glob_path(self, id: int):
        """Delete registered glob and path by id.

        Arguments:
            id {int} -- the glob and path's id which you want to delete.

        Returns:
            {{'glob': string, 'path': string}} -- the setting you destroy.

        """
        deleted_path = self.config['path'].pop(id)
        self.save_file()
        return deleted_path

    def list_glob_path(self):
        return [i for i in self.config['path'] if is_valid_glob_path(i)]

    def save_file(self):
        with self.config_path.open(mode='w', encoding='utf_8') as f:
            f.write(json.dumps(self.config))

    def create_new_config_file(self):
        with self.config_path.open(mode='w', encoding='utf_8') as f:
            self.config = {'path': []}
            f.write(json.dumps(self.config))

    def get_config(self):
        return self.config

    def load_file(self):
        with self.config_path.open(encoding='utf_8') as f:
            config_text = f.read()
            self.config = json.loads(config_text)
