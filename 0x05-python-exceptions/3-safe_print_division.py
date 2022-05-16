#!/usr/bin/python3

from unittest import result


def safe_print_division(a, b):
    t = None
    try:
        t = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(t))
    return t
