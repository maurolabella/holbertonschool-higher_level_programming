#!/usr/bin/python3
"""class module"""


class Rectangle:
    """define rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width retrieve function"""
        return self.width

    @width.setter
    def width(self, value):
        """width setter"""
        if(type(value) is not int):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """"height retrieve function"""
        return self.height

    @height.setter
    def height(self, value):
        """height setter"""
        if(type(value) is not int):
            raise TypeError("height must be an integer")
        elif(value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area retrieve function"""
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter retrieve function"""
        return ((self.__height + self.__width) * 2)
