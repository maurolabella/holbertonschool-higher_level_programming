#!/usr/bin/python3
"""class module"""


class Rectangle:
    """define rectangle class"""

    def __init__(self, width=0, height=0):
        """set height and width"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """width retrieve function"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """"height retrieve function"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area retrieve function"""
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter retrieve function"""
        if (self.area() == 0):
            return 0
        return ((self.__height + self.__width) * 2)
