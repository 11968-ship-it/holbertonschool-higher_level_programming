#!/usr/bin/python3
"""
0-add_integer module

This module contains a function that adds two integers.
"""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert to int *after* type check
    # This handles standard floats by truncating them
    # and large ints without overflow problems.
    return int(a) + int(b)
