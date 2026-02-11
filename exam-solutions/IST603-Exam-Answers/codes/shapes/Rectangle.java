import java.util.List;
import java.util.Arrays;

public class Rectangle extends Polygon {
  private int width;
  private int height;

  public Rectangle(int width, int height) {
    super("Rectangle", Arrays.asList(width, height, width, height));
    this.width = width;
    this.height = height;
    if (width <= 0 || height <= 0) {
      throw new IllegalArgumentException("Width and height must be positive");
    }
  }

  public Rectangle(List<Integer> sides) {
    super("Rectangle", sides);
    if (sides.size() != 4) {
      throw new IllegalArgumentException("Rectangle must have exactly 4 sides");
    }
    if (!isValidRectangle()) {
      throw new IllegalArgumentException("Invalid rectangle: opposite sides must be equal");
    }
    this.width = Math.min(sides.get(0), sides.get(1));
    this.height = Math.max(sides.get(0), sides.get(1));
  }

  private boolean isValidRectangle() {
    if (sideLengths.size() != 4)
      return false;

    // Sort the sides and check if they form two pairs
    List<Integer> sortedSides = sideLengths.stream().sorted().collect(java.util.stream.Collectors.toList());
    return sortedSides.get(0).equals(sortedSides.get(1)) &&
        sortedSides.get(2).equals(sortedSides.get(3));
  }

  public int computeArea() {
    return width * height;
  }

  public int getWidth() {
    return width;
  }

  public int getHeight() {
    return height;
  }

  public boolean isSquare() {
    return width == height;
  }

  public int getDiagonal() {
    return (int) Math.sqrt(width * width + height * height);
  }

  @Override
  public String toString() {
    String type = isSquare() ? "Square" : "Rectangle";
    return super.toString().replace("Rectangle", type) +
        " with width=" + width + ", height=" + height +
        " (Area: " + computeArea() + ", Diagonal: " + String.format("%.2f", getDiagonal()) + ")";
  }
}