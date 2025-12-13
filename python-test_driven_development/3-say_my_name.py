#!/usr/bin/python3
"""
3-say_my_name module

This module contains a function that prints "My name is <first name> <last name>".
"""

def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Always include a space after first_name, even if last_name is empty
    print("My name is {} {}".format(first_name, last_name))
