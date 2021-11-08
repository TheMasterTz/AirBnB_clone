#!/usr/bin/python3
import unittest
from datetime import datetime
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Setting up instances"""
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_attributes(self):
        """Testing that attributes are set"""
        self.model.name = 'jhon'
        self.model.number = 23
        self.assertEqual(self.model.name, 'jhon')
        self.assertEqual(self.model.number, 23)

    def test_is_create(self):
        """check that the instance has been created"""
        self.assertEqual(self.model.__class__.__name__, "BaseModel")
        self.assertTrue(self.model)

    def test_str(self):
        """checking that the string formats are correct"""
        self.assertEqual(type(self.model.id), str)

        strr = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__)
        self.assertEqual(self.model.__str__(), strr)

    def test_datetime(self):
        """Test for """
        self.assertEqual(type(self.model.created_at), datetime)
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_UpdatedAt(self):
        """Test time is updated"""
        old = self.model.updated_at
        created = self.model.created_at
        self.assertEqual(old, self.model.updated_at)
        self.assertEqual(created, self.model.created_at)

        self.model.save()
        new = BaseModel()

        self.assertNotEqual(old, self.model.updated_at)
        self.assertEqual(created, self.model.created_at)
        self.assertIsNot(old, new)

    def test_ClassInstance(self):
        """checks if the instance is part of the BaseModel class"""
        self.assertEqual(type(self.model), BaseModel)
        self.assertIsInstance(self.model, BaseModel)

    def test_Instances(self):
        """Test many instances"""
        Ins1 = BaseModel()
        Ins2 = BaseModel()
        Ins3 = BaseModel()
        Ins4 = BaseModel()

        self.assertIsInstance(Ins1.id, str)
        self.assertIsInstance(Ins1.updated_at, datetime)
        self.assertIsInstance(Ins1.created_at, datetime)

        self.assertIsInstance(Ins2.id, str)
        self.assertIsInstance(Ins2.updated_at, datetime)
        self.assertIsInstance(Ins2.created_at, datetime)

        self.assertIsInstance(Ins3.id, str)
        self.assertIsInstance(Ins3.updated_at, datetime)
        self.assertIsInstance(Ins3.created_at, datetime)

        self.assertIsInstance(Ins4.id, str)
        self.assertIsInstance(Ins4.updated_at, datetime)
        self.assertIsInstance(Ins4.created_at, datetime)

    def test_dictionary(self):
        """Test for dictionary"""
        self.model.number = 42
        dictionary = self.model.to_dict()
        self.assertEqual(type(dictionary), dict)
        self.assertIsInstance(dictionary['id'], str)
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)
        self.assertIsInstance(dictionary['__class__'], str)
        self.assertIsInstance(dictionary['number'], int)


if __name__ == '__main__':
    unittest.main()
