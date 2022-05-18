#!/usr/bin/python3
"""class module"""


class Rectangle:
    """define rectangle class"""

    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """String representation"""
        res = ""
        if(self.__width * self.__height == 0):
            return res
        else:
            for i in range(self.__height):
                res += str(self.print_symbol) * self.__width + '\n'
        return res[:-1]

    def __repr__(self):
        """String representation generator for eval"""
        res = "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"
        return res

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

    def __del__(self):
        """Instance of Rectangle Deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle"""
        if(type(rect_1) is not Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if(type(rect_2) is not Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if(rect_2.area() > rect_1.area()):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """creates square"""
        return cls(size, size)
