#!/usr/bin/python3

from unittest import result


def safe_print_division(a, b):
    t = 0
    try:
        t = a / b
    except Exception:
        t = None
    finally:
        print("Inside result: {}".format(t))
        return t
