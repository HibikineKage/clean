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
        self.test_cleanrc_path = test_cleanrc_path
        self.env = {
            'CLEANRC_PATH': str(self.test_cleanrc_path)
        }  # type: dict[str, str]

    def test_add_config(self):
        runner = CliRunner()
        runner.invoke(cli.add, ['hogehoge', 'fugafuga'], env=self.env)
        c = config.Config(config_path=self.test_cleanrc_path)
        path_list = c.list_glob_path()
        self.assertIn({"glob": "hogehoge", "path": "fugafuga"}, path_list)

    def test_add_same_config(self):
        """Cannot add same path config to a cleanrc
        """
        c = config.Config(config_path=self.test_cleanrc_path)
        path_list = c.list_glob_path()
        self.assertEqual(path_list.count({"glob": "fuga", "path": "hoge"}), 1)

        runner = CliRunner()
        runner.invoke(cli.add, ['fuga', 'hoge'], env=self.env)

        c = config.Config(config_path=self.test_cleanrc_path)
        path_list = c.list_glob_path()
        self.assertEqual(path_list.count({"glob": "fuga", "path": "hoge"}), 1)

    def test_list_config(self):
        runner = CliRunner()
        result = runner.invoke(cli.list, env=self.env)
        self.assertEqual("[0] fuga => hoge\n", result.output)

    def test_delete_config(self):
        test_value = {"glob": "fuga", "path": "hoge"}  # type: dict[str, str]
        c = config.Config(config_path=self.test_cleanrc_path)  # type: Config
        path_list = c.list_glob_path()  # type: list[dict[str, str]]
        index = path_list.index(test_value)
        runner = CliRunner()
        r = runner.invoke(cli.delete, [str(index)], env=self.env)
        c = config.Config(config_path=self.test_cleanrc_path)
        path_list = c.list_glob_path()
        self.assertNotIn({"glob": "fuga", "path": "hoge"}, path_list)


if __name__ == '__main__':
    unittest.main()
