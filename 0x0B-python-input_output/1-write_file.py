#!/usr/bin/python3
"""Tasks: 1.Write to a file"""


def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text
    file (UTF8) and returns the number of characters
    written
                """
    with open(filename, 'w') as file:
        lines = file.write(text)
    return lines
