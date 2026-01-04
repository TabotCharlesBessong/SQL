# QUESTION 1 SOLUTIONS
**Course:** IST603 - Object-Oriented Programming with Java and Python

---

## Part (a) - OOP Concepts

### (i) Encapsulation
Encapsulation is the bundling of data (attributes/variables) and methods (functions) that operate on that data into a single unit called a class. It also involves hiding the internal details of how a class works from the outside world, typically using access modifiers (private, protected, public). This ensures data integrity and prevents unauthorized access.

### (ii) Composition
Composition is a "has-a" relationship where one class contains an instance of another class as a member variable. The contained object cannot exist independently of the containing object in a strong composition (aggregation is a weaker form where the contained object can exist independently). For example, a Car class might have a Wheel object - the car is composed of wheels.

### (iii) Inheritance
Inheritance is an "is-a" relationship where a child class (subclass/derived class) inherits attributes and methods from a parent class (superclass/base class). This promotes code reusability and establishes a hierarchical relationship. For example, a Dog class might inherit from an Animal class.

### (iv) Polymorphism
Polymorphism means "many forms" and allows objects of different classes to be treated through the same interface. It enables a single interface to represent different underlying forms. In Java, this is achieved through method overriding (runtime polymorphism) and method overloading (compile-time polymorphism).

---

## Part (b) - Java Exception Handling

Given the code:
```java
public static void m(int x) {
    try {
        m2(x);
        System.out.println(1);
    } catch (ArithmeticException e) {
        System.out.println(2);
    } catch (Exception e) {
        System.out.println(3);
    }
}

public static void m2(int x) throws IOException {
    System.out.println(4);
    if (x == 1) {
        throw new IOException();
    }
    if (x == 0) {
        throw new ArithmeticException();
    }
    System.out.println(5);
}
```

### (i) Output of m(1):
1. m2(1) is called
2. Prints: 4
3. x == 1, so throws IOException
4. IOException is caught by catch (Exception e) block (since IOException extends Exception)
5. Prints: 3

**Answer:**
```
4
3
```

### (ii) Output of m(0):
1. m2(0) is called
2. Prints: 4
3. x == 0, so throws ArithmeticException
4. ArithmeticException is caught by catch (ArithmeticException e) block (more specific match)
5. Prints: 2

**Answer:**
```
4
2
```

---

## Part (c) - Java Inheritance and Method Overriding

Given the code:
```java
class A {
    private int x;
    public A(int x) {
        this.x = x;
    }
    public void m() {
        System.out.println(x - 1);
    }
}

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
```

### (i) Output of new A(3).m():
- Creates A with x = 3
- Calls m() which prints (x - 1) = (3 - 1) = 2

**Answer:** `2`

### (ii) Output of new B(3).m():
- Creates B with y = 3
- Calls super(y - 1) = super(2), so A's constructor sets x = 2
- B's y = 3
- Calls B's overridden m() method, which prints (y + 1) = (3 + 1) = 4

**Answer:** `4`

### (iii) Output of ((A)(new B(3))).m():
- Creates B object but casts to A reference
- However, in Java, method overriding uses dynamic dispatch (runtime polymorphism)
- The actual object type is B, so B's m() method is called
- Same as (ii): prints (y + 1) = (3 + 1) = 4

**Answer:** `4`

---

## Part (d) - Java Constructor Chaining

Given the code:
```java
class Test {
    int var;

    Test(double var) {
        this.var = (int) var;
    }

    Test(int var) {
        this("aaa");
    }

    Test(String s) {
        this();
        System.out.println(s);
    }

    Test() {
        System.out.println("bbb");
    }

    public static void main(String[] args) {
        Test t = new Test(5);
    }
}
```

**Execution flow for new Test(5):**
1. Test(5) calls Test(int var) constructor
2. Test(int var) calls this("aaa") → Test(String s) constructor
3. Test(String s) calls this() → Test() constructor (no-args)
4. Test() executes first: prints "bbb"
5. Returns to Test(String s): prints "aaa"
6. Returns to Test(int var): completes (var is not set in this constructor)

**Answer:**
```
bbb
aaa
```

---

## Part (e) - Java Object Reference Passing

Given the code:
```java
class Test {
    int x;

    public Test(int x) {
        this.x = x;
    }

    public static void m(Test o) {
        o = new Test(2);
        System.out.println("output = " + o.x);
    }

    public static void main(String[] args) {
        Test o = new Test(1);
        m(o);
        System.out.println("output = " + o.x);
    }
}
```

**Execution flow:**
1. main creates Test object: o.x = 1
2. m(o) is called - the reference is passed by value
3. Inside m(), parameter o is reassigned to a new Test(2) object
4. This reassignment does NOT affect the original object in main
5. Prints: "output = 2" (from the new object created in m)
6. Back in main, original o still has x = 1
7. Prints: "output = 1"

**Answer:**
```
output = 2
output = 1
```

