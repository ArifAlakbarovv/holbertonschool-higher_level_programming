#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for row in new_matrix:
        for i in row:
            i = i**2
    return new_matrix
