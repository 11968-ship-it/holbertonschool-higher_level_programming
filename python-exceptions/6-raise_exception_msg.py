#!/usr/bin/python3
"""
This module defines a function that raises a NameError exception
with a custom message.
"""


def raise_exception_msg(message=""):
    """
    Raises a NameError exception with the given message.

    Args:
        message (str): The message to be used in the exception.
    """
    raise NameError(message)
