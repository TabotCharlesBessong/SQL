"""
Write a Python program that:

- Accepts two numbers from the user.
- Divides the first number by the second.

Handle the following exceptions:
- ZeroDivisionError (division by zero)
- ValueError (invalid input when converting to a number)
- A general Exception block for any other unexpected errors.

Ensure a finally block is used to display a completion message.
"""


def divide_numbers() -> None:
    try:
        first = input("Enter the first number: ")
        second = input("Enter the second number: ")

        num1 = float(first)
        num2 = float(second)

        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Division operation completed (Python).")


def main() -> None:
    divide_numbers()


if __name__ == "__main__":
    main()

