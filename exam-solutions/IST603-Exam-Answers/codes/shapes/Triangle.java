import java.util.List;
import java.util.Arrays;

public class Triangle extends Polygon {

  public Triangle(int side1, int side2, int side3) {
    super("Triangle", Arrays.asList(side1, side2, side3));
    if (!isValidTriangle()) {
      throw new IllegalArgumentException("Invalid triangle: sides do not satisfy triangle inequality");
    }
  }

  public Triangle(List<Integer> sides) {
    super("Triangle", sides);
    if (sides.size() != 3) {
      throw new IllegalArgumentException("Triangle must have exactly 3 sides");
    }
    if (!isValidTriangle()) {
      throw new IllegalArgumentException("Invalid triangle: sides do not satisfy triangle inequality");
    }
  }

  private boolean isValidTriangle() {
    if (sideLengths.size() != 3)
      return false;
    int a = sideLengths.get(0);
    int b = sideLengths.get(1);
    int c = sideLengths.get(2);
    return (a + b > c) && (a + c > b) && (b + c > a);
  }

  public double computeArea() {
    // Using Heron's formula
    double s = computePerimeter() / 2.0; // semi-perimeter
    double a = sideLengths.get(0);
    double b = sideLengths.get(1);
    double c = sideLengths.get(2);
    return Math.sqrt(s * (s - a) * (s - b) * (s - c));
  }

  public String getTriangleType() {
    int a = sideLengths.get(0);
    int b = sideLengths.get(1);
    int c = sideLengths.get(2);

    if (a == b && b == c) {
      return "Equilateral";
    } else if (a == b || b == c || a == c) {
      return "Isosceles";
    } else {
      return "Scalene";
    }
  }

  @Override
  public String toString() {
    return super.toString() + " with sides " + sideLengths +
        " (Type: " + getTriangleType() + ", Area: " + String.format("%.2f", computeArea()) + ")";
  }
}