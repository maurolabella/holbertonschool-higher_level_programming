#!/usr/bin/python3
def magic_string():
    i = getattr(magic_string, "value", -1)
    setattr(magic_string, "value", i + 1)

    return "BestSchool" + ", BestSchool" * magic_string.value
