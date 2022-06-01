#!/usr/bin/python3
"""Tasks: 11.Student to disk and reload"""


class Student():
    """defines student by:
    first_name
    last_name
    age
    """

    def __init__(self, first_name, last_name, age):
        """_init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation (json)
        of a Student instance"""
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            json_obj = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    json_obj[key] = value
            return json_obj
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        instance"""
        for key, value in json.items():
            self.__dict__[key] = value
