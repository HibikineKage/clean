import click
from click.testing import CliRunner
from unittest import TestCase
import unittest
from clean import cli, config
from pathlib import Path


class TestCli(TestCase):
    def setUp(self):
        current_dir = Path(__file__).parent.resolve()
        test_cleanrc_path = current_dir / '.cleanrc'
        cleanrc_template_path = current_dir / '.cleanrc.template'
        with test_cleanrc_path.open('w', encoding='utf_8') as f:
            with cleanrc_template_path.open('r', encoding='utf_8') as template:
                f.write(template.read())
        config.config_file_name = test_cleanrc_path

    def test_add_config(self):
        runner = CliRunner()
        runner.invoke(cli.add, ['hogehoge', 'fugafuga'], env={""})
        c = config.Config()
        path_list = c.list_glob_path()
        self.assertIn({"glob": "hogehoge", "path": "fugafuga"}, path_list)

    def test_list_config(self):
        runner = CliRunner()
        result = runner.invoke(cli.list)
        self.assertEqual("fuga => hoge", result.output)


if __name__ == '__main__':
    unittest.main()
