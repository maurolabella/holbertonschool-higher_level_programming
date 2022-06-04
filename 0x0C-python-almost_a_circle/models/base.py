#!/usr/bin/python3
"""Base Class Main File"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string
        representation of a list_dictionaries"""
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(element) != dict for element in list_dictionaries):
            raise TypeError("list_dicationaries must have dictionaries\
              as elements")
        return json.dumps(list_dictionaries)
