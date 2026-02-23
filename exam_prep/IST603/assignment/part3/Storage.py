"""
Generic class Storage[T] that can store and retrieve an object of any type.
Uses typing.Generic so type checkers (e.g. mypy) can catch type errors at "compile" time.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class Storage(Generic[T]):
    def __init__(self) -> None:
        self._value: T | None = None

    def set(self, value: T) -> None:
        self._value = value

    def get(self) -> T:
        if self._value is None:
            raise ValueError("Storage is empty")
        return self._value


def main() -> None:
    # Store an Integer
    int_storage: Storage[int] = Storage()
    int_storage.set(42)
    n: int = int_storage.get()  # No cast needed; type is known
    print("Integer:", n)

    # Store a String
    str_storage: Storage[str] = Storage()
    str_storage.set("Hello")
    s: str = str_storage.get()  # No cast needed
    print("String:", s)

    # Generics / type hints prevent type errors when checked (e.g. mypy):
    # int_storage.set("wrong")   # Type checker error: argument has type "str"; "int" expected
    # bad: str = int_storage.get()  # Type checker error: "int" is not assignable to "str"
    # At runtime Python allows anything; use mypy/pyright for static checking.


if __name__ == "__main__":
    main()
