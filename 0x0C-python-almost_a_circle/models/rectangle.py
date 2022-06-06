#!/usr/bin/python3
"""Rectangle"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle : class definition
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ : class instantiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns area"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle"""
        for y in range(self.__y):
            print()
        for x in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """__str__"""
        return ("[Rectangle] ("+str(self.id)+") "+str(self.__x)+"/" +
                str(self.__y)+" - "+str(self.__width)+"/"+str(self.__height))

    def update(self, *args, **kwargs):
        """
        updates class Rectangle assigning an argument
        to each attribute
        """
        if args:
            atts = ['id', 'width', 'height', 'x', 'y']
            mapped = zip(atts, args)
            for key, value in mapped:
                setattr(self, key, value)
            return
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation
        of a rectangle
        """
        dict_rectangle = {}
        for key, value in vars(self).items():
            dict_rectangle[key.split("__")[-1]] = value
        return dict_rectangle
