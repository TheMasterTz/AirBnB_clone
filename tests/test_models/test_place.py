#!/usr/bin/python3
"""Test module"""

import unittest
from models.place import Place

class TestMyPlace(unittest.TestCase):
    """New class to test class Place"""

    def setUp(self):
        """Setting up"""
        self.new = Place()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.new, Place)
        self.assertIsInstance(self.new.city_id, str)
        self.assertIsInstance(self.new.user_id, str)
        self.assertIsInstance(self.new.name, str)
        self.assertIsInstance(self.new.description, str)
        self.assertIsInstance(self.new.number_rooms, int)
        self.assertIsInstance(self.new.number_bathrooms, int)
        self.assertIsInstance(self.new.max_guest, int)
        self.assertIsInstance(self.new.price_by_night, int)
        self.assertIsInstance(self.new.latitude, float)
        self.assertIsInstance(self.new.city_id, str)
        self.assertIsInstance(self.new.longitude, float)
        self.assertIsInstance(self.new.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
