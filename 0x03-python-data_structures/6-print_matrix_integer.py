#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # print(f"{len(matrix)}")
    # print(f"{len(matrix[0])}")
	m=len(matrix)
	n=len(matrix[0])
	for i in range(0,m):
		for j in range(0,n):
			print("{:d}".format(matrix[i][j]),end="")
			if(j!=(n-1)):
				print(" ",end="")
		print("$")
