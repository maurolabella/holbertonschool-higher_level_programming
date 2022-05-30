#!/usr/bin/python3
"""Square 2"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print() should print, and str() should
        return, the square description:
        [Square] <width>/<height>"""
        return "[Square] " + str(self.__size) + "/"+str(self.__size)
