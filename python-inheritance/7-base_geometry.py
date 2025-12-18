#!/usr/bin/python3
"""Module defining the BaseGeometry class."""

class BaseGeometry:
    """BaseGeometry class for validating integers and
    calculating areas.
    """

    def area(self):
        """Calculate the area. Not implemented in BaseGeometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
