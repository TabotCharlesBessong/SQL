package exam_prep.IST603.assignment.part5;

import java.util.Scanner;

/**
 * Write a Java program that:
 * <ul>
 *   <li>Accepts two numbers from the user.</li>
 *   <li>Divides the first number by the second.</li>
 * </ul>
 *
 * Handle the following exceptions:
 * <ul>
 *   <li>ArithmeticException (division by zero)</li>
 *   <li>NumberFormatException (invalid input)</li>
 *   <li>A general Exception block for unexpected errors</li>
 * </ul>
 *
 * Ensure a finally block is used to display a completion message.
 */
public class DivisionWithExceptions {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter the first number: ");
            String firstInput = scanner.nextLine();

            System.out.print("Enter the second number: ");
            String secondInput = scanner.nextLine();

            int num1 = Integer.parseInt(firstInput);
            int num2 = Integer.parseInt(secondInput);

            int result = num1 / num2; // may throw ArithmeticException if num2 == 0

            System.out.println("Result: " + num1 + " / " + num2 + " = " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero is not allowed.");
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid input. Please enter whole numbers.");
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            System.out.println("Division operation completed (Java).");
            scanner.close();
        }
    }
}

