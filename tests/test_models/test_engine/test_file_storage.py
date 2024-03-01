#!/usr/bin/python3
"""Unittest for FileStorage class"""
from models.engine.file_storage import FileStorage
from models.engine import file_storage
from models.base_model import BaseModel
from models import storage
import unittest
from os import path


class TestFileStorage(unittest.TestCase):
    """Class to test the FileStorage class"""

    def test_documentation(self):
        """Test for documentation in the module, class and methods"""
        self.assertTrue(len(file_storage.__doc__) > 1)
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_attributes(self):
        """Test the attributes"""
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        """Test the all method"""
        instance = BaseModel()
        objs = storage.all()
        self.assertNotEqual(len(objs), 0)

    def test_new(self):
        """Test the new method"""
        inst1 = BaseModel()
        objs = len(storage.all())
        self.assertTrue(objs > 0)
        inst2 = BaseModel()
        objs2 = len(storage.all())
        self.assertNotEqual(objs, objs2)

    def test_reload(self):
        """Test the reload method"""
        objs1 = len(storage.all())
        storage.reload()
        objs2 = len(storage.all())
        self.assertEqual(objs2, objs1)


if __name__ == "__main__":
    """Executes the tests"""
    unittest.main()
