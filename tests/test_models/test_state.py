#!/usr/bin/python3
"""Test module"""

import unittest
from models.state import State

class TestMyState(unittest.TestCase):
    """New class to test class State"""

    def setUp(self):
        """Setting up"""
        self.new = State()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        self.assertIsInstance(self.new, State)

    def test_if_str(self):
        """check if the attribute is str"""
        self.assertIsInstance(self.new.name, str)

if __name__ == '__main__':
    unittest.main()
