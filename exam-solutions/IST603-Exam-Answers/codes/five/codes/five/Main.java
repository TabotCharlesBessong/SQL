package codes.five;

public class Main {
  public static void main(String[] args) {
    // A a = new A(3);
    // B b = new B(5);
    // Output for (new B(3)).m():
    // B b = new B(3);
    // a.m();
    // b.m();

    // Output for ((A)(new B(3))).m():
    ((A)(new B(3))).m();
  }
}
