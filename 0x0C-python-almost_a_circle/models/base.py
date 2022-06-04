#!/usr/bin/python3
"""Base Class Main File"""

import json
from pydoc import classname


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
            raise TypeError("list_dictionaries must have dictionaries\
              as elements")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON 
        string representation of list_objs 
        to a file
        """
        if type(list_objs) != list:
            raise TypeError("list_objs must be a list")
        sample_type = type(list_objs[0])
        if any(isinstance(element, Base) != True or type(element)
               != sample_type for element in list_objs):
            raise TypeError(
                "list_objs must have all same type Base-related instances")
        filename = cls.__name__+".json"
        if list_objs:
            content = [element.to_dictionary() for element in list_objs]
        else:
            content = []
        with open(filename, "w") as file:
            file.write(cls.to_json_string(content))

