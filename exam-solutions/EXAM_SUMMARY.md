# EXAM SOLUTIONS SUMMARY - IST603

**Quick Reference Guide for All Questions**

---

## QUESTION 1 - ASSORTED (30 marks)

### Part (a) - OOP Concepts (8 marks)

| Concept | Definition |
|---------|-----------|
| **Encapsulation** | Bundling data and methods into a class, hiding internal details |
| **Composition** | "Has-a" relationship - one class contains another as a member |
| **Inheritance** | "Is-a" relationship - child class inherits from parent class |
| **Polymorphism** | Objects of different types treated through the same interface |

---

### Part (b) - Exception Handling (3 marks)

**Given Code:**
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
    if (x == 1) throw new IOException();
    if (x == 0) throw new ArithmeticException();
    System.out.println(5);
}
```

| Question | Answer |
|----------|--------|
| **m(1) output** | `4` then `3` |
| **m(0) output** | `4` then `2` |

---

### Part (c) - Inheritance and Method Overriding (5 marks)

**Given Code:**
```java
class A {
    private int x;
    public A(int x) { this.x = x; }
    public void m() { System.out.println(x - 1); }
}

class B extends A {
    private int y;
    public B(int y) {
        super(y - 1);
        this.y = y;
    }
    public void m() { System.out.println(y + 1); }
}
```

| Question | Answer |
|----------|--------|
| **new A(3).m()** | `2` |
| **new B(3).m()** | `4` |
| **((A)(new B(3))).m()** | `4` (dynamic dispatch) |

---

### Part (d) - Constructor Chaining (2 marks)

**Output:**
```
bbb
aaa
```

**Explanation:** Test(5) → Test(int) → Test(String) → Test() → prints "bbb", then "aaa"

---

### Part (e) - Object Reference Passing (2 marks)

**Output:**
```
output = 2
output = 1
```

**Explanation:** Reference passed by value; reassignment in m() doesn't affect original object.

---

### Part (f) - Python Output (10 marks)

| Code Snippet | Output |
|-------------|--------|
| **(i)** `for x in [10, 20]: print(x)` | `10` then `20` |
| **(ii)** `[2*x for x in [1,2,3,4,5,6,7]]` | `[2, 4, 6, 8, 10, 12, 14]` |
| **(iii)** `print(x, y)` (x undefined) | `NameError` (or if x=20 from (i): `20 Chair` then `20 Table`) |
| **(iv)** Negative indexing + list comprehension | `40`<br>`[20, 30, 40]`<br>`['HelloDear', 'HelloBye', 'GoodDear', 'GoodBye']` |
| **(v)** `student[1]["age"]` | `27` |

---

## QUESTION 3 - SHAPES INHERITANCE (45 marks)

### Part (a) - Theoretical Questions

| Question | Answer |
|----------|--------|
| **Abstract vs Concrete Classes** | Abstract: Cannot be instantiated, may have abstract methods<br>Concrete: Can be instantiated, all methods implemented |
| **Which shapes are abstract?** | **Shape** is abstract. All others (Rectangle, Triangle, Square, Ellipse, Circle, Sector) are concrete. |
| **Abstract vs Concrete Methods** | Abstract: Declaration only, no implementation<br>Concrete: Full implementation provided |

---

### Part (b) - Java Implementation

**Inheritance Hierarchy:**
```
Shape (abstract)
├── Rectangle
│   └── Square
├── Triangle
└── Ellipse
    └── Circle
        └── Sector
```

**Key Answers:**
- **Shape:** `abstract class Shape` with abstract `getArea()` and `printDetails()`
- **All subclasses:** Extend appropriate parent, implement abstract methods
- **Formulae:** See detailed solutions in QUESTION_3B_JAVA_SOLUTIONS.md

---

### Part (c) - Java Code

**Answer:**
```java
Shape[] shapes = new Shape[6];
shapes[0] = new Rectangle(5.0, 3.0, 1.0, 2.0);
shapes[1] = new Triangle(4.0, 6.0, 3.0, 4.0);
shapes[2] = new Square(4.0, 5.0, 6.0);
shapes[3] = new Ellipse(3.0, 2.0, 7.0, 8.0);
shapes[4] = new Circle(5.0, 9.0, 10.0);
shapes[5] = new Sector(6.0, Math.PI/3, 11.0, 12.0);

for (Shape shape : shapes) {
    shape.printOrigin();
    shape.printDetails();
    System.out.println();
}
```

---

### Part (d) - Python Implementation

**Equivalent to Question (b) and (c) in Python**

See QUESTION_3D_PYTHON_SOLUTIONS.md for complete Python implementations.

**Key Differences:**
- Use `from abc import ABC, abstractmethod`
- Use `@abstractmethod` decorator
- Use `super().__init__()` instead of `super()`
- Use lists instead of arrays
- Use f-strings for formatted output

---

## FORMULAE REFERENCE

| Shape | Area Formula |
|-------|-------------|
| Triangle | 0.5 × base × height |
| Rectangle | width × height |
| Square | side² |
| Ellipse | π × a × b |
| Circle | π × r² |
| Sector | 0.5 × r² × θ (θ in radians) |

---

## STUDY TIPS

1. **Understand the inheritance hierarchy** - know which classes extend which
2. **Abstract vs Concrete** - Shape is abstract, all others are concrete
3. **Method Overriding** - All subclasses override `printDetails()` and `getArea()`
4. **Polymorphism** - Shape array/list can hold any shape subclass
5. **Constructor Chaining** - Always call `super()` first
6. **Exception Handling** - Order matters (most specific catch first)

---

## FILE STRUCTURE

- **QUESTION_1_SOLUTIONS.md** - Detailed Question 1 solutions
- **QUESTION_1F_PYTHON_OUTPUT.md** - Python output solutions
- **QUESTION_3A_THEORETICAL.md** - Theoretical OOP questions
- **QUESTION_3B_JAVA_SOLUTIONS.md** - Java implementation with placeholders
- **QUESTION_3C_JAVA_CODE.md** - Java code for Question 3(c)
- **QUESTION_3D_PYTHON_SOLUTIONS.md** - Python implementation with placeholders
- **QUICK_REFERENCE_PLACEHOLDERS.md** - All placeholder answers (A, B, C, D, E)
- **Shape.java** - Complete compilable Java code
- **shapes.py** - Complete runnable Python code
- **README.md** - Overview and usage instructions

