#!/usr/bin/python3
def square_matrix_map(matrix=[]):
	return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))

    # return [(list(map(lambda x: x**2, row))) for row in matrix]
		# return [list(map(lambda x: x**2,matrix))]


