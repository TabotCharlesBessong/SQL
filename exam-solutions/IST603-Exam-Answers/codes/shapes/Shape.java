public class Shape {
  protected String shape;

  public Shape(String shape) {
    this.shape = shape;
  }

  @Override
  public String toString(){
    return "I am a " + shape;
  }
}
