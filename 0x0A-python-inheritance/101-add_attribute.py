#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, attr_name, value):
    """Write a function that adds a new attribute"""
    if hasattr(obj, '__dict__') is True:
        setattr(obj, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
