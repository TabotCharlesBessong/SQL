package codes.five;

class A {
  private int x;

  public A(int x) {
    this.x = x;
  }

  public void m() {
    System.out.println(x - 1);
    System.out.println("from A");
  }
}
