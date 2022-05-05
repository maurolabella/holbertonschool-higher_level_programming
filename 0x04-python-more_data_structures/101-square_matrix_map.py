#!/usr/bin/python3

from numpy import square


def square_matrix_map(matrix=[]):
    square = []
    for row in matrix:
        square.append(list(map(lambda x: x**2, row)))

    # col_numb = len(square)
    # mtrx = [[row[i]**2 for i in range(col_numb)] for row in square]
    return square
