#!/usr/bin/python3
"""Tasks: From JSON string to Object"""

import json


def from_json_string(my_str):
    """"Write a function that returns an
    object(Python data structure"""
    return json.loads(my_str)
