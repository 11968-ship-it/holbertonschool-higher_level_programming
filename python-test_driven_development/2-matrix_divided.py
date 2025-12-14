#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a
given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with elements divided by div,
        rounded to 2 decimals.

    Raises:
        TypeError: If matrix elements are not all lists of integers/floats.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is 0.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check all elements are int/float
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Check all rows are the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check div != 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix elements
    return [[round(item / div, 2) for item in row] for row in matrix]
