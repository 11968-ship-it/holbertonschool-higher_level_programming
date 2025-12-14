#!/usr/bin/python3
"""
Module that provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The number to divide by.

    Returns:
        list of lists of float: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not all the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists of numbers
    if not isinstance(matrix, list) or not matrix or any(
        not isinstance(row, list) or not row for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all elements are integers/floats
    for row in matrix:
        if any(not isinstance(ele, (int, float)) for ele in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all rows are of the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Divide all elements by div and round to 2 decimal places
    new_matrix = [
        [round(ele / div, 2) for ele in row] for row in matrix
    ]

    return new_matrix
