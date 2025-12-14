#!/usr/bin/python3
"""
This module defines a function to add two integers.
The function ensures that the parameters are integers or floats
and raises a TypeError if they are not.
Floats are cast to integers before addition.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Parameters:
    a (int or float): The first number to add.
    b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
    int: The sum of a and b, both casted to integers.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
