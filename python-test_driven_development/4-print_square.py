#!/usr/bin/python3
"""
This module provides a function that prints a square using the character '#'.

The function validates that the size is a non-negative integer before printing
the square. It raises appropriate exceptions for invalid input types or values.
"""


def print_square(size):
    """
    Prints a square with the character '#' of the given size.

    Args:
        size (int): The size of the square (length of each side).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
