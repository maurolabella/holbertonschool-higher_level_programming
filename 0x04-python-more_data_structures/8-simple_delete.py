#!/usr/bin/python3

from logging import exception


def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
        return a_dictionary
    except exception:
        return a_dictionary
