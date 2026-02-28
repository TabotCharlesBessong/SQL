package exam_prep.IST603.lambda;

/**
 * Simple calculator demonstrating lambda expressions for basic arithmetic operations.
 * 
 * Operations demonstrated:
 * - Addition
 * - Subtraction
 * - Multiplication
 * - Division
 * - Modulo
 * - Power
 */
public class Calculator {

    /**
     * Functional interface for arithmetic operations.
     */
    @FunctionalInterface
    interface Operation {
        double apply(double a, double b);
    }

    public static void main(String[] args) {
        // Lambda expressions for each operation
        Operation add = (a, b) -> a + b;
        Operation subtract = (a, b) -> a - b;
        Operation multiply = (a, b) -> a * b;
        Operation divide = (a, b) -> a / b;
        Operation modulo = (a, b) -> a % b;
        Operation power = (a, b) -> Math.pow(a, b);

        // Test values
        double num1 = 20.0;
        double num2 = 4.0;

        // Display results
        System.out.println("=== Calculator using Lambda Expressions ===\n");
        System.out.println("Operand 1: " + num1);
        System.out.println("Operand 2: " + num2 + "\n");
        
        System.out.println("Addition:      " + num1 + " + " + num2 + " = " + add.apply(num1, num2));
        System.out.println("Subtraction:   " + num1 + " - " + num2 + " = " + subtract.apply(num1, num2));
        System.out.println("Multiplication: " + num1 + " * " + num2 + " = " + multiply.apply(num1, num2));
        System.out.println("Division:      " + num1 + " / " + num2 + " = " + divide.apply(num1, num2));
        System.out.println("Modulo:        " + num1 + " % " + num2 + " = " + modulo.apply(num1, num2));
        System.out.println("Power:         " + num1 + " ^ " + num2 + " = " + power.apply(num1, num2));
    }
}
