#!/usr/bin/python3
"""
Module that defines a function inherits_from to check if an
object is an instance of a class that inherited from a
specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from a_class, otherwise returns False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
