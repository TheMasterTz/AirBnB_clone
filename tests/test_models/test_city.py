#!/usr/bin/python3
"""Test module"""

import unittest
from models.city import City

class TestMyCity(unittest.TestCase):
    """New class to test class City"""
    def setUp(self):
        """Setting up"""
        self.new = City()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        self.assertIsInstance(self.new, City)

    def test_name(self):
        self.assertIsInstance(self.new.name, str)

    def test_id(self):
        self.assertIsInstance(self.new.state_id, str)

if __name__ == '__main__':
    unittest.main()
