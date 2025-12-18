#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits
from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle defined by width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
