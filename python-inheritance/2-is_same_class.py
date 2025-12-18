#!/usr/bin/python3
"""
Module that defines a function is_same_class to check if an object
is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified
    class, otherwise returns False.
    """
    return type(obj) is a_class
