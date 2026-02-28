"""
Practical Question 2 – User-Defined Exception (Python version)

Create a custom exception class InvalidAgeException.

Tasks:
- Throw (raise) the exception if a user enters an age below 18.
- Catch the exception and display a meaningful error message.
- Demonstrate the use of a custom exception in a small program.

Test the program with valid and invalid age values.
"""


class InvalidAgeException(Exception):
    """Custom exception raised when an age is below the allowed minimum."""

    def __init__(self, age: int, message: str = "Age must be at least 18."):
        self.age = age
        super().__init__(message)


def validate_age(age: int) -> None:
    """
    Validate that age is at least 18.

    Raises InvalidAgeException if the age is too low.
    """
    if age < 18:
        # Equivalent of Java's `throw new InvalidAgeException(age);`
        raise InvalidAgeException(age)


def main() -> None:
    try:
        raw = input("Enter your age: ")
        age = int(raw)

        validate_age(age)
        print("Access granted. Age is valid (18 or older).")
    except InvalidAgeException as e:
        print(f"InvalidAgeException caught: {e} (you entered {e.age})")
    except ValueError:
        print("Error: Please enter a whole number for age.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Age validation (Python) finished.")


if __name__ == "__main__":
    # You can run this script multiple times to test:
    # - Valid value: 18, 25, etc.
    # - Invalid value: 10, 15, etc.
    main()

