#!/usr/bin/python3
"""class creation"""


class Square:
    """Square - an empty class Square thad defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optionally selected size and position"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
            self.position = position

    def area(self):
        """Public instance method: def area(self)"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ To retrieve private size information"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set entity's value to the value specified"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """To retrieve private position information"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set a new value position"""
        if((type(value) is not tuple) or (len(value) != 2) or
           (type(value[0]) is not int) or (type(value[1]) is not int)
           or (value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """my_print - Method that prints in stdout the square"""
        if(self.__size > 0):
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                print("#"*self.__size, end="")
                print("")
        else:
            print("")
