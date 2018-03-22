import unittest
from unittest import TestCase
from clean.config import Config
from os import path
from pathlib import Path


class TestConfig(TestCase):
    """test class of config.py
    """

    def setUp(self):
        current_dir = Path(__file__).parent.resolve()
        self.test_cleanrc_path = current_dir / '.cleanrc'
        cleanrc_template_path = current_dir / '.cleanrc.template'
        with self.test_cleanrc_path.open('w', encoding='utf_8') as f:
            with cleanrc_template_path.open('r', encoding='utf_8') as template:
                f.write(template.read())

    def test_list_glob_path(self):
        """test method for Config.list_glob_path
        """
        config = Config(config_path=self.test_cleanrc_path)
        path_list = config.list_glob_path()
        self.assertEqual(path_list, [{"glob": "fuga", "path": "hoge"}])

    def test_add_glob_path(self):
        """Test method for Config.add_glob_path
        """
        config = Config(config_path=self.test_cleanrc_path)
        is_success = config.add_glob_path('hogehoge', 'fugafuga')
        self.assertTrue(is_success)
        config = Config(config_path=self.test_cleanrc_path)
        path_list = config.list_glob_path()
        self.assertIn({"glob": "hogehoge", "path": "fugafuga"}, path_list)

    def test_add_same_glob_path(self):
        """Test same glob path to add a cleanrc will fail
        """
        config = Config(config_path=self.test_cleanrc_path)
        is_success = config.add_glob_path('fuga', 'hoge')
        self.assertFalse(is_success)
        config = Config(config_path=self.test_cleanrc_path)
        path_list = config.list_glob_path()
        self.assertEqual(1, path_list.count({"glob": "fuga", "path": "hoge"}))

    def test_delete_glob_path(self):
        """Test method for Config.delete_glob_path.
        """
        config = Config(config_path=self.test_cleanrc_path)
        deleted_config = config.delete_glob_path(0)
        self.assertEqual(deleted_config, {"glob": "fuga", "path": "hoge"})
        config = Config(config_path=self.test_cleanrc_path)
        path_list = config.list_glob_path()
        self.assertNotIn({"glob": "fuga", "path": "hoge"}, path_list)


if __name__ == '__main__':
    unittest.main()