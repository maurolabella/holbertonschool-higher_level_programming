#!/usr/bin/python3
"""Base Class Main File"""

import json
import os.path
import csv


class Base():
    """
    Base: class creation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ instance creation"""
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
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

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
        if any([isinstance(element, Base) is not True or type(element)
               != sample_type for element in list_objs]):
            raise TypeError(
                "list_objs must have all same type Base-related instances")
        filename = cls.__name__+".json"
        if list_objs:
            content = [element.to_dictionary() for element in list_objs]
        else:
            content = []
        with open(filename, "w") as file:
            file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """static method returning the \
        list of the JSON string representation"""
        if type(json_string) != str:
            raise TypeError("json_string must be a string representation")
        list = []
        if json_string:
            content = json.loads(json_string)
            if all([type(element) == dict for element in content]):
                return content
            else:
                raise ValueError("json_string must contain dictionaries")
        else:
            return list

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__+".json"
        list = []
        if not os.path.exists(filename):
            return list
        else:
            with open(filename, "r") as file:
                dictionary = cls.from_json_string(file.read())
        for elements in dictionary:
            list.append(cls.create(**elements))
        return list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to CSV"""
        if type(list_objs) != list:
            raise TypeError("list_objs must be a list")
        sample_type = type(list_objs[0])
        if any([isinstance(element, cls) is not True or type(element)
               != sample_type for element in list_objs]):
            raise TypeError(
                "list_objs must have all same type Base-related instances")
        filename = cls.__name__+".csv"
        rectangle_fields = ['id', 'width', 'height', 'x', 'y']
        square_fields = ['id', 'size', 'x', 'y']
        if list_objs:
            content = [element.to_dictionary() for element in list_objs]
        else:
            content = []
        with open(filename, "w") as file:
            if cls.__name__ == "Rectangle":
                recorder = csv.DictWriter(file, fieldnames=rectangle_fields)
            else:
                recorder = csv.DictWriter(file, fieldnames=square_fields)
            recorder.writeheader()
            recorder.writerows(content)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes from CSV"""
        filename = cls.__name__+".csv"
        head = []
        new_list = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                csvreader = csv.reader(file, delimiter=',')
                head = next(csvreader)
                for row in csvreader:
                    row_elem = [int(e) for e in row]
                    row_dictionary = dict((x, y) for x, y in zip(
                        head, row_elem))
                    new_list.append(cls.create(**row_dictionary))
        return new_list
