#!/usr/bin/python3

from unittest import result


def safe_print_division(a, b):
    t = None
    try:
        t = a / b
    except Exception:
        pass
    finally:
        if t is not None:
            print("Inside result: {:.1f}".format(t))
        else:
            print("Inside result: None")
    return t
