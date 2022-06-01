#!/usr/bin/python3
"""Tasks: Student to JSON"""


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

    def to_json(self):
        """returns a dictionary representation
        of a Student instance"""
        return self.__dict__
