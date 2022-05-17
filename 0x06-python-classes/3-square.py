#!/usr/bin/python3
"""create class"""


class Square:
    """Square - an empty class Square thad defines a square"""

    def __init__(self, size=0):
        """Instantiation with optionally selected size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """Public instance method: def area(self)"""
        return (self.__size ** 2)
