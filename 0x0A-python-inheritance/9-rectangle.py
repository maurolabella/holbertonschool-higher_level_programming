#!/usr/bin/python3
"""Full rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """__init__"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method"""
        return(self.__height * self.__width)

    def __str__(self):
        """string representation"""
        return ("[Rectangle] " + str(self.__width)+"/"+str(self.__height))
