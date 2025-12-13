#!/usr/bin/python3
"""
2-matrix_divided module

This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Returns a new matrix with each element divided by div and rounded to 2 decimals.
    """
    # Check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check matrix type
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        len(matrix) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check all elements are int/float and all rows have same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if any(not isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Divide elements and return new matrix
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
