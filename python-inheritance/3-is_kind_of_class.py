#!/usr/bin/python3
"""
Module that defines a function is_kind_of_class to check
if an object is an instance of a class or a subclass of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of a_class or a subclass of it,
    otherwise returns False.
    """
    return isinstance(obj, a_class)
