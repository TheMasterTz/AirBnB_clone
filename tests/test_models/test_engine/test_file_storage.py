#!/usr/bin/python3
"""Test module"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class to check FileStorage class"""
    def setUp(self):
        """Setting up instances"""
        self.model = BaseModel()
        self.file_storage = FileStorage()

    def tearDown(self):
        """Cleaning up"""
        del self.model
        del self.file_storage

    def test_if_Instance(self):
        """Check if the instances belong to the classes"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.file_storage, FileStorage)

    def test_dictionary_JSON(self):
        """Check type of every val in the dict"""
        self.model.number = 42
        dictionary = self.model.to_dict()
        self.assertEqual(type(dictionary), dict)
        self.assertIsInstance(dictionary['id'], str)
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)
        self.assertIsInstance(dictionary['__class__'], str)
        self.assertIsInstance(dictionary['number'], int)

    def test_if_attributes_exist(self):
        """Check if FileStorage has the 2 public attributes"""
        self.assertTrue(hasattr(self.file_storage, 'classes'))
        self.assertTrue(hasattr(self.file_storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.file_storage, '_FileStorage__objects'))

    def test_all(self):
        """Check is all() returns a dictionary"""
        self.assertEqual(type(self.file_storage.all()), dict)

    def test_save(self):
        """Check if save() creates a file"""
        self.model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_empty_file(self):
        """Check if the file is not empty"""
        self.assertFalse(os.stat('file.json') == 0)

if __name__ == '__main__':
    unittest.main()
