#!/usr/bin/python3
"""
Module that defines a BaseGeometry class with an area() method
that is not implemented.
"""


class BaseGeometry:
    """
    BaseGeometry class: serves as a base for geometry classes.
    """

    def area(self):
        """
        Public instance method that raises an Exception
        when called because it is not implemented.
        """
        raise Exception("area() is not implemented")
