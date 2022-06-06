"""
Square Tests
"""
import unittest
import os
from models.square import Square
from models.base import Base


class SquareTest(unittest.TestCase):
    """Square tests"""

    def test_square_isinstance(self):
        """isinstance"""
        r1 = Square(2)
        self.assertEqual(isinstance(r1, Base), True)

    def test_square_none(self):
        """None"""
        with self.assertRaises(TypeError) as x:
            r = Square(None)
        self.assertEqual(
            'width must be an integer',
            str(x.exception))

    def test_square_empty(self):
        """Empty values"""
        with self.assertRaises(TypeError) as x:
            r = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(x.exception))

    def test_square_strings(self):
        """string values"""
        with self.assertRaises(TypeError) as x:
            r = Square("1")
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Square(10, 2, "2")
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 0, "Holberton")
        self.assertEqual(
            "y must be an integer",
            str(x.exception))

    def test_square_float(self):
        """Float values"""
        with self.assertRaises(TypeError) as x:
            r = Square(0.1)
        self.assertEqual(
            'width must be an integer',
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 5, 0.1)
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 0, 0.1)
        self.assertEqual(
            "y must be an integer",
            str(x.exception))


if __name__ == '__main__':
    unittest.main()
