# oop/polymorphism_demo.py
import math
from typing import Protocol


class Shape:
    """Base class for shapes demonstrating polymorphism via method overriding."""

    def area(self) -> float:
        """Return the area of the shape.

        Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement area().")


class Rectangle(Shape):
    """Rectangle shape with length and width."""

    def __init__(self, length: float, width: float) -> None:
        self.length = float(length)
        self.width = float(width)

    def area(self) -> float:
        """Area = length × width."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius: float) -> None:
        self.radius = float(radius)

    def area(self) -> float:
        """Area = π × r²."""
        return math.pi * (self.radius ** 2)
