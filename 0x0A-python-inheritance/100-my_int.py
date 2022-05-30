#!/usr/bin/python3
"""12.My integer"""


class MyInt(int):
    """is a rebel MyInt has == and != inverted"""

    def __eq__(self, n):
        return super().__ne__(n)

    def __ne__(self, n):
        return super().__eq__(n)
