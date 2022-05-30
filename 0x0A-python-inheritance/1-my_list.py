#!/usr/bin/python3
"""1.My list"""


class MyList(list):
    """ MyList inherit from Python's standard list"""

    def print_sorted(self):
        "prints the list sorted by ascending"
        print(sorted(self))
