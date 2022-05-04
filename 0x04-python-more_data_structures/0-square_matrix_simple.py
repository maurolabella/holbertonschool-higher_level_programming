#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    col_numb = len(matrix[0])
    mtrx = [[row[i]**2 for i in range(col_numb)] for row in matrix]
    return mtrx
