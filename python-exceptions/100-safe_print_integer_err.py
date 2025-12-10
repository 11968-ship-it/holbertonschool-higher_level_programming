#!/usr/bin/python3
"""
This module defines a function that safely prints an integer.
If the value is not an integer, it prints the error to stderr.
"""


def safe_print_integer_err(value):
    """
    Prints an integer value followed by a new line.

    Args:
        value: The value to print.

    Returns:
        True if value is an integer and printed correctly, False otherwise.
        If False, the exception is printed to stderr.
    """
    import sys

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
