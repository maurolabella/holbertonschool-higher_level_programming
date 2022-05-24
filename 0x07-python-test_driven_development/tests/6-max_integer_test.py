#!/usr/bin/python3
"""
Unitest testing for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unitest for max_integer([...])
    """

    def test_case_1(self):
        """Test the case of no list introduced"""
        self.assertEqual(max_integer(), None)

    def test_case_2(self):
        """Test introducing hexadecimals"""
        self.assertEqual(max_integer([4, 5, 6, 0x3b85]), 15237)

    def test_case_3(self):
        """Test introducing negative numbers"""
        self.assertEqual(max_integer([-4, -5, -6, 0]), 0)

    def test_case_4(self):
        """Test introducing one number alone"""
        self.assertEqual(max_integer([0]), 0)

    def test_case_5(self):
        """Test introducing nothing"""
        self.assertEqual(max_integer([]), None)

    def test_case_6(self):
        """Test introducing string among numerical inputs"""
        self.assertRaises(TypeError, max_integer, [4, 5, 6, "jo"])

    def test_case_7(self):
        """Test introducing complex numbers as input"""
        self.assertRaises(TypeError, max_integer, [4, 5, 6, 5 - 6j])

    def test_case_8(self):
        """Test other iterables in addition to list as input : tuples"""
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_case_9(self):
        """Test other iterables in addition to list as input : dictionary_1"""
        self.assertRaises(TypeError, max_integer, {1, 2, 3})

    def test_case_10(self):
        """Test other iterables in addition to list as input : dictionary_2"""
        self.assertRaises(KeyError, max_integer, {"a": 1, "b": 2, "c": 3})

    def test_case_11(self):
        """Test other iterables : list of lists"""
        self.assertRaises(TypeError, max_integer, [1, 2, [1, 2, 3]])

    def test_case_12(self):
        """Test introducing string without numerical inputs"""
        try:
            max_integer(["a", "b", "c"])
        except Exception as e:
            self.fail("Unexpected exception %s" % e)


if __name__ == '__main__':
    unittest.main()
