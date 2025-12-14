#!/usr/bin/python3
"""
This module provides a function to print a formatted name.

The function ensures that the provided first and last names are strings
and prints them in the format: "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the provided first and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
