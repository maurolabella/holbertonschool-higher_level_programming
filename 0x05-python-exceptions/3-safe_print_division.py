#!/usr/bin/python3

from unittest import result


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except Exception:
        pass
    finally:
        if result is not None:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
    return result
