#!/usr/bin/python3
"""
 
This module defines a function that adds two integers.
It ensures the arguments are integers or floats, casting floats to integers.
All operations return an integer value.
"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    a and b must be integers or floats; floats are casted to integers.
    Raises a TypeError if a or b are not integers or floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
