#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """create a function to represent Pascal's triangle"""
    list = []
    if n <= 0:
        return list
    for i in range(n):
        row = [1]
        if i > 0:
            for k in range(i):
                row.append(sum(list[-1][k:k+2]))
        list.append(row)
    return list
