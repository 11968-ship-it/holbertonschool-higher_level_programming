#!/usr/bin/python3
"""
This module defines a function that executes another function safely.
If an exception occurs, it prints the error to stderr and returns None.
"""


def safe_function(fct, *args):
    """
    Executes a function with provided arguments safely.

    Args:
        fct (function): The function to execute.
        *args: Arguments to pass to the function.

    Returns:
        The result of the function if successful, otherwise None.
        If an exception occurs, prints it to stderr.
    """
    import sys

    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
