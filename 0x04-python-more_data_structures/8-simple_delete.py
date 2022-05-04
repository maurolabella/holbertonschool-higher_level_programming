#!/usr/bin/python3

from logging import exception


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
