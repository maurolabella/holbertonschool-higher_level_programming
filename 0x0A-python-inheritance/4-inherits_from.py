#!/usr/bin/python3
"Only sub class of"


def inherits_from(obj, a_class):
    """returns True if the oject is an instance of class inheriting directly or indirectly from a specified class"""

    return (type(obj) != a_class and isinstance(obj, a_class))
