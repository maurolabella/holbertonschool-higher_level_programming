#!/usr/bin/python3
"""Tasks 2.Append to a file"""


def append_write(filename="", text=""):
    """
    Write a function that appends a string at
    the end of a text file (UTF8) and returns
    the number of characters added
    """
    with open(filename, 'a') as file:
        lines = file.write(text)
    return lines
