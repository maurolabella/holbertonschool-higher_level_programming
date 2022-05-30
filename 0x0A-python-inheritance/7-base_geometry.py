#!/usr/bin/python3
"""Integer validator"""

from typing import Type


class BaseGeometry():
    """Class BaseGeometry"""

    def area(self):
        """Write a class BaseGeometry (based on 5-base_geometry.py)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
