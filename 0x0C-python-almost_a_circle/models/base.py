#!/usr/bin/python3
"""Base Class Main File"""


class Base():
    """Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
