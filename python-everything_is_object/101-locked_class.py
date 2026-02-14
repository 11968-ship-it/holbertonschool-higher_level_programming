#!/usr/bin/python3
"""Defines a restricted attribute class."""


class LockedClass:
    """
    Prevent user from creating new instance attributes
    except if the new instance attribute is called 'first_name'.
    """
    __slots__ = ["first_name"]
