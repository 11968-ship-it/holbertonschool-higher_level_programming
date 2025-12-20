#!/usr/bin/python3
"""BaseGeometry module.

Defines a BaseGeometry class with an unimplemented area method
and an integer_validator method for input validation.
"""


class BaseGeometry:
    """BaseGeometry class

    Provides a blueprint for geometric shapes and input validation.
    """

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
