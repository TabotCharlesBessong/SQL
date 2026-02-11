import java.util.List;

public class Polygon extends Shape {
  protected List<Integer> sideLengths;

  public Polygon(String shape, List<Integer> sideLengths) {
    super(shape);
    this.sideLengths = sideLengths;
  }

  public int computePerimeter(){
    if (sideLengths == null || sideLengths.isEmpty()) {
      return 0;
    }
    int perimeter = 0;
    for (Integer length : sideLengths) {
      perimeter += length;
    }
    return perimeter;
  }

  public int getNumberOfSides() {
    if (sideLengths == null) {
      return 0;
    }
    return sideLengths.size();
  }
}
