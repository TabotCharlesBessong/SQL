
class B extends A {
  private int y;

  public B(int y) {
    super(y - 1);
    this.y = y;
  }

  public void m() {
    System.out.println(y + 1);
  }
}
