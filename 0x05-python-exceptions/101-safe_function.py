#!/usr/bin/python3

def safe_function(fct, *args):
    from sys import stderr
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        result = None
    return (res)
