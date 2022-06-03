#!/usr/bin/python3
"""Search and update"""


def file_reader(filename):
    """file line generator"""
    with open(filename, "r") as file:
        for row in file:
            yield row


def append_after(filename="", search_string="", new_string=""):
    """
    Write a function that inserts a line of text 
    to a file, after each line containing 
    a specific string
    """
    new_content = []
    for line in file_reader(filename):
        if search_string in line:
            new_content.append(line)
            new_content.append(str(new_string))
        else:
            new_content.append(line)
    with open(filename, "w") as file:
        file.writelines(new_content)
