#!/usr/bin/python3
"""
Base class tests
"""
import unittest
import os
from models import base
from models.base import Base


class BaseTest(unittest.TestCase):
    """Class cases:"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_id_evolution(self):
        """id assignment behaviour"""
        r1 = Base()
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_non_automated_id(self):
        """Specific Id"""
        r1 = Base(123)
        self.assertEqual(r1.id, 123)

    def test_stringed_id(self):
        """String id"""
        a = Base("Papurri")
        self.assertEqual(a.id, "Papurri")

    def test_none(self):
        """None id"""
        a = Base(None)
        self.assertEqual(a.id, 1)

    def test_negative(self):
        """Negative id"""
        a = Base(-2)
        self.assertEqual(a.id, -2)


if __name__ == '__main__':
    unittest.main()
