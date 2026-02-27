"""
Demonstration of polymorphism in Python.

This example shows:
- A common interface defined in a base class (`Shape.area`).
- Multiple subclasses (`Circle`, `Rectangle`, `Triangle`) implementing that interface.
- Runtime polymorphism: the same method call behaves differently depending on the object's class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from math import pi
from typing import List


class Shape(ABC):
    """Abstract base class that defines a common interface for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        raise NotImplementedError

    def describe(self) -> str:
        """Non-abstract method shared by all shapes."""
        return f"{self.__class__.__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


def print_shape_info(shape: Shape) -> None:
    """
    Function that works with the base type `Shape`.
    At runtime, the correct `area()` implementation (Circle/Rectangle/Triangle)
    is called depending on the actual object passed in.
    """
    print(shape.describe())


def main() -> None:
    shapes: List[Shape] = [
        Circle(3.0),
        Rectangle(4.0, 5.0),
        Triangle(6.0, 2.0),
    ]

    for shape in shapes:
        print_shape_info(shape)


if __name__ == "__main__":
    main()

