#!/usr/bin/python3
"""
Module that defines a BaseGeometry class with area() and integer_validator methods.
"""


class BaseGeometry:
    """
    BaseGeometry class: serves as a base for geometry classes.
    """

    def area(self):
        """
        Public instance method that raises an Exception
        because it is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        Raises TypeError if value is not an integer.
        Raises ValueError if value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
