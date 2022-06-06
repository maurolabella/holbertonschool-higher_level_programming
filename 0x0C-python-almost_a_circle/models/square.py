#!/usr/bin/python3
"""Square Class Creation"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__"""
        super().__init__(size, size, x, y, id=None)

    def __str__(self):
        """__str__"""
        return (
            "["+str(type(self).__name__)+"] ("+str(self.id)+") \
            "+str(self.x)+"/" + str(self.y)+" - "+str(self.width))

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        updates class Square assigning an argument
        to each attribute
        """
        if args:
            atts = ['id', 'size', 'x', 'y']
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
        of a square
        """
        dict_square = {}
        for key, value in vars(self).items():
            if key.split("__")[-1] == "width":
                dict_square["size"] = value
            elif key.split("__")[-1] == "height":
                pass
            else:
                dict_square[key.split("__")[-1]] = value
        return dict_square
