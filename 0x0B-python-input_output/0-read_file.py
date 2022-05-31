#!/usr/bin/python3
"""Task 0.Read file"""


def read_file(filename=""):
    """Write a function that reads 
    a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r') as file:
        filexcontent = file.read()
    print(filexcontent, end="")
