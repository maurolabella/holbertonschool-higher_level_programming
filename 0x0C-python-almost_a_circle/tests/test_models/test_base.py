#!/usr/bin/python3
"""
Base class tests
"""
import unittest
import os
# from models import base
from models.base import Base


class BaseTest(unittest.TestCase):
    """Class cases:"""

    def setUp(self):
        Base.__nb_objects = 0

    def test_base_id_evolution(self):
        """id assignment behaviour"""
        r1 = Base()
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        


if __name__ == '__main__':
    unittest.main()
