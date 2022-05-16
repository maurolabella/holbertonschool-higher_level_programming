#!/usr/bin/python3

from unittest import result


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except:
        pass
    finally:
        if result == None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(result))
    return result
