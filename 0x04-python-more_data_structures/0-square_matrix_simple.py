#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = matrix.copy()
    for j in range(len(matrix)):
        nmatrix[j] = list(map(lambda x: x**2, matrix[j]))
    return (nmatrix)
