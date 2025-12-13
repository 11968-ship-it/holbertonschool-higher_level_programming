#!/usr/bin/python3
"""Defines a square with private size, getter/setter, and area method."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square with optional size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

