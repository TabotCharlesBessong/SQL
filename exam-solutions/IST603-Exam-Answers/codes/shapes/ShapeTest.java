import java.util.Arrays;

public class ShapeTest {
  public static void main(String[] args) {
    System.out.println("=== Testing Triangle ===");
    try {
      // Valid triangle
      Triangle t1 = new Triangle(3, 4, 5);
      System.out.println("Triangle 1: " + t1);
      System.out.println("Perimeter: " + t1.computePerimeter());
      System.out.println("Number of sides: " + t1.getNumberOfSides());

      // Equilateral triangle
      Triangle t2 = new Triangle(Arrays.asList(5, 5, 5));
      System.out.println("Triangle 2: " + t2);

      // Invalid triangle (should throw exception)
      try {
        Triangle t3 = new Triangle(1, 2, 10);
      } catch (IllegalArgumentException e) {
        System.out.println("Error creating invalid triangle: " + e.getMessage());
      }

    } catch (Exception e) {
      System.out.println("Triangle error: " + e.getMessage());
    }

    System.out.println("\n=== Testing Rectangle ===");
    try {
      // Regular rectangle
      Rectangle r1 = new Rectangle(4, 6);
      System.out.println("Rectangle 1: " + r1);
      System.out.println("Perimeter: " + r1.computePerimeter());
      System.out.println("Number of sides: " + r1.getNumberOfSides());

      // Square
      Rectangle r2 = new Rectangle(5, 5);
      System.out.println("Rectangle 2 (Square): " + r2);

      // Rectangle from sides list
      Rectangle r3 = new Rectangle(Arrays.asList(3, 7, 3, 7));
      System.out.println("Rectangle 3: " + r3);

      // Invalid rectangle (should throw exception)
      try {
        Rectangle r4 = new Rectangle(Arrays.asList(1, 2, 3, 4));
      } catch (IllegalArgumentException e) {
        System.out.println("Error creating invalid rectangle: " + e.getMessage());
      }

    } catch (Exception e) {
      System.out.println("Rectangle error: " + e.getMessage());
    }
  }
}