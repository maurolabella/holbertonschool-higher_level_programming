#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
	# m=len(matrix)
	# n=len(matrix[0])
	# for i in range(0,m):
	# 	for j in range(0,n):
	# 		print("{:d}".format(matrix[i][j]),end="")
	# 		if(j!=(n-1)):
	# 			print(" ",end="")
	# 	print("$")
	for row in matrix:
		for elem in row:
			print("{:d}".format(elem), end="")
			if (row.index(elem) + 1) < len(row):
				print(" ", end="")
		print("\n", end="")
