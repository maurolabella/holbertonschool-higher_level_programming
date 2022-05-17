#!/usr/bin/python3
"""class creation"""


class Square:
    """Square - an empty class Square thad defines a square"""

    def __init__(self, size=0):
        """Instantiation with optional selected size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
