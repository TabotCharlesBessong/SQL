package exam_prep.IST603.assignment.part6;

import java.util.Scanner;

/**
 * Practical Question 2 – User-Defined Exception (Java version)
 *
 * Create a custom exception class InvalidAgeException.
 *
 * Tasks:
 * - Throw the exception if a user enters an age below 18.
 * - Catch the exception and display a meaningful error message.
 * - Demonstrate the use of throw and throws.
 *
 * Test the program with valid and invalid age values.
 */
public class UserDefinedExceptionDemo {

    /**
     * Custom checked exception for invalid age values.
     */
    static class InvalidAgeException extends Exception {
        private final int age;

        public InvalidAgeException(int age, String message) {
            super(message);
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    /**
     * Validate that age is at least 18.
     *
     * Demonstrates the use of `throws` in the method signature and
     * `throw` inside the method body.
     */
    public static void validateAge(int age) throws InvalidAgeException {
        if (age < 18) {
            // Demonstrates `throw`:
            throw new InvalidAgeException(age, "Age must be at least 18.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter your age: ");
            String input = scanner.nextLine();
            int age = Integer.parseInt(input);

            // May throw InvalidAgeException (declared with `throws`).
            validateAge(age);

            System.out.println("Access granted. Age is valid (18 or older).");
        } catch (InvalidAgeException e) {
            System.out.println("InvalidAgeException caught: " + e.getMessage()
                    + " (you entered " + e.getAge() + ")");
        } catch (NumberFormatException e) {
            System.out.println("Error: Please enter a whole number for age.");
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            System.out.println("Age validation (Java) finished.");
            scanner.close();
        }
    }
}

