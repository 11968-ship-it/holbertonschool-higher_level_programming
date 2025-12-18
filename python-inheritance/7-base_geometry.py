#!/usr/bin/python3
"""
This module defines a BaseGeometry class with an area method
that is not implemented and a validator for positive integers.
"""


class BaseGeometry:
    """
    BaseGeometry class with an area method and integer validator.
    """

    def area(self):
        """
        Public instance method that raises an Exception
        indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): Name of the parameter.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        # Reject all non-int types and bool
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        # Reject zero or negative numbers
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
