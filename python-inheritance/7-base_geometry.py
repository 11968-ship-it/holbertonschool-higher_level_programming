#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Public instance method area() that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as a positive integer.

        Args:
            name (str): Name of the variable
            value: The value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
