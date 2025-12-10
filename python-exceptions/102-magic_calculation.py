#!/usr/bin/python3
"""
This module defines a function magic_calculation that performs
a calculation based on given bytecode logic.
"""


def magic_calculation(a, b):
    """
    Performs a calculation:
    - Loops i from 1 to 2
    - If i > a, raises Exception and sets result to a + b
    - Otherwise, adds (a ** b) / i to result

    Args:
        a (int or float)
        b (int or float)

    Returns:
        result of calculation
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception:
            result = a + b
            break
    return result
