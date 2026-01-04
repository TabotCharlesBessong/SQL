# EXAM SOLUTIONS - IST603: Object-Oriented Programming with Java and Python

**University:** University of Buea  
**Faculty:** Science  
**Department:** Computer Science  
**Course:** IST603 - Object-Oriented Programming with Java and Python  
**Examination:** First Semester Resit Examination 2024/2025

---

## Solution Files Overview

This directory contains comprehensive solutions to all exam questions:

### Question 1 Solutions
- **QUESTION_1_SOLUTIONS.md** - Complete solutions for Question 1 parts (a) through (e)
  - Part (a): OOP Concepts (Encapsulation, Composition, Inheritance, Polymorphism)
  - Part (b): Java Exception Handling
  - Part (c): Java Inheritance and Method Overriding
  - Part (d): Java Constructor Chaining
  - Part (e): Java Object Reference Passing

### Question 1(f) - Python Output
- **QUESTION_1F_PYTHON_OUTPUT.md** - Solutions for Python code output questions (i) through (v)

### Question 3 Solutions

#### Theoretical Questions
- **QUESTION_3A_THEORETICAL.md** - Theoretical OOP questions
  - (i) Abstract vs Concrete Classes
  - (ii) Abstract vs Concrete Methods

#### Java Implementation
- **QUESTION_3B_JAVA_SOLUTIONS.md** - Complete Java class implementations with placeholder answers
  - Class Shape (abstract base class)
  - Class Ellipse
  - Class Circle
  - Class Sector
  - Class Rectangle
  - Class Square
  - Class Triangle

- **QUESTION_3C_JAVA_CODE.md** - Java code for Question 3(c)
  - Creating Shape array
  - Instantiating shapes
  - Iterating and calling methods

- **Shape.java** - Complete, compilable Java implementation

#### Python Implementation
- **QUESTION_3D_PYTHON_SOLUTIONS.md** - Complete Python class implementations with placeholder answers
  - All shape classes equivalent to Java versions
  - Python code for Question 3(c) equivalent

- **shapes.py** - Complete, runnable Python implementation

---

## Running the Code

### Java
```bash
# Compile
javac Shape.java

# Run
java ShapeTest
```

### Python
```bash
# Run
python shapes.py
```

---

## Inheritance Hierarchy

```
Shape (abstract)
├── Rectangle
│   └── Square
├── Triangle
└── Ellipse
    └── Circle
        └── Sector
```

---

## Shape Formulae

- **Triangle:** Area = 0.5 × base × height
- **Rectangle:** Area = width × height
- **Square:** Area = side²
- **Ellipse:** Area = π × a × b
- **Circle:** Area = π × r², Circumference = 2πr
- **Sector:** Area = 0.5 × r² × θ (θ in radians)

---

## Notes

1. All solutions follow object-oriented programming principles
2. Abstract classes use abstract methods where appropriate
3. Method overriding demonstrates polymorphism
4. Both Java and Python implementations are functionally equivalent
5. Code is well-commented and follows best practices for university-level programming

---

## Study Tips

1. Review the inheritance hierarchy to understand relationships
2. Practice implementing abstract classes and methods
3. Understand polymorphism and method overriding
4. Review exception handling in Java
5. Compare Java and Python implementations to see syntax differences

