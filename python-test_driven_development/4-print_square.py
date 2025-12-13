#!/usr/bin/python3
"""
4-print_square module

This module contains a function that prints a square with the character #.
"""

def print_square(size):
    """Prints a square of # characters with the given size."""
    # Type check
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Value check
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print square
    for _ in range(size):
        print("#" * size)
