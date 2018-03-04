from pathlib import Path
import json
config_file_name = '.cleanrc'
config_dir = Path.home() / config_file_name


class Config:
    def __init__(self):
        self.config_dir = config_dir
        if not self.config_dir.is_file():
            if self.config_dir.exists():
                click.echo(
                    'Can\'t create file. Same name something is exist. Please check your home\'s {}.'.
                    format(config_file_name))
                exit(1)
            self.create_new_config_file()

        self.load_file()

    def add_regexp_path(self, regexp: str, path: str):
        self.config['path'].append({'regexp': regexp, 'path': path})
        self.save_file()
        return True

    def save_file(self):
        with self.config_dir.open(mode='w', encoding='utf=8') as f:
            f.write(json.dumps(self.config))

    def create_new_config_file(self):
        with self.config_dir.open(mode='w', encoding='utf-8') as f:
            self.config = {'path': []}
            f.write(json.dumps(self.config))

    def get_config(self):
        return self.config

    def load_file(self):
        with self.config_dir.open(encoding='utf-8') as f:
            config_text = f.read()
            self.config = json.loads(config_text)
