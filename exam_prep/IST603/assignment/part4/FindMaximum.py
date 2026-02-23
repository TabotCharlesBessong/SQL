"""
Generic method find_maximum() with bounded type parameters.
Accepts a sequence of numbers (int, float, etc.) and returns the maximum value.
Uses typing.TypeVar(bound=...) to restrict to numeric types.
"""

from numbers import Real
from typing import TypeVar

T = TypeVar("T", bound=Real)


def find_maximum(array: list[T]) -> T:
    """
    Bounded type parameter T: must be a subtype of Real (int, float, etc.),
    so only numeric types are allowed. Type checkers will reject non-numeric types.
    """
    if not array:
        raise ValueError("Array must not be empty")
    maximum = array[0]
    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]
    return maximum


def main() -> None:
    ints = [3, 7, 2, 9, 1]
    print("Max int:", find_maximum(ints))  # 9

    floats = [3.14, 2.71, 1.41]
    print("Max float:", find_maximum(floats))  # 3.14

    mixed_numeric = [10, 5.5, 20]  # int and float both Real
    print("Max (mixed):", find_maximum(mixed_numeric))  # 20


if __name__ == "__main__":
    main()
