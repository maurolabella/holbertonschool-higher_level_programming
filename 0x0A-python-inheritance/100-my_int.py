#!/usr/bin/python3
"""12.My integer"""


class MyInt(int):
    """is a rebel MyInt has == and != inverted"""

    def __eq__(self, n):
        """Yes"""
        return super().__ge__(n)

    def __ge__(self, n):
        """Yes"""
        return super().__eq__(n)
