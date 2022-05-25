#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "value", getattr(magic_string, "value", -1) + 1)
    return "BestSchool" + ", BestSchool" * magic_string.value
