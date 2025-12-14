#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given divisor and return a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor number.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with divided values rounded to 2 decimals.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = None
    for row in matrix:
        if not isinstance(row, list):  # Removed "or row == []"
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
