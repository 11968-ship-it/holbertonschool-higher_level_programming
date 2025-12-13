#!/usr/bin/python3
"""Defines a square with a private attribute size."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square with a private size."""
        self.__size = size
