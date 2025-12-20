#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        pi = 3.141592653589793
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        pi = 3.141592653589793
        return 2 * pi*
