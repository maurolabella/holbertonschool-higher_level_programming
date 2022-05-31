#!/usr/bin/python3
"""Tasks: Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes an Object
    to a text file, using JSON representation"""

    with open(filename, 'w') as file:
        lines = file.write(json.dumps(my_obj))
    return lines
