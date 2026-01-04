# QUICK REFERENCE - PLACEHOLDER ANSWERS

This document provides quick reference answers for all placeholder letters (A, B, C, D, E) in the exam questions.

---

## QUESTION 3(b) - JAVA IMPLEMENTATION

### (i) Class Shape

- **A:** `abstract class Shape {`
- **B:** `this.x = x; this.y = y;`
- **C:** `public abstract void printDetails();`
- **D:** `public abstract double getArea();`

---

### (ii) Class Ellipse

- **A:** `public class Ellipse extends Shape {`
- **B:** `super(x, y);`
- **C:** `this.a = a; this.b = b;`
- **D:** `Math.PI * a * b`
- **E:** `"Ellipse: a=" + a + ", b=" + b + ", area=" + getArea()`

**Note:** The exam fragment shows `private double base, height;` but mathematically, ellipses use semi-axes `a` and `b`. Use `a` and `b` for the correct implementation.

---

### (iii) Class Circle

- **A:** `public class Circle extends Ellipse {`
- **B:** `super(radius, radius, x, y); this.radius = radius;`
- **C:** `return Math.PI * radius * radius;`

---

### (iv) Class Sector

- **A:** `public class Sector extends Circle {`
- **B:** `super(radius, x, y); this.angle = angle;`
- **C:** `return 0.5 * getRadius() * getRadius() * angle;`
- **D:** `System.out.println("Sector: radius=" + getRadius() + ", angle=" + angle + ", area=" + getArea());`

**Note:** Requires `getRadius()` method in Circle class.

---

### (v) Class Rectangle

- **A:** `public class Rectangle extends Shape {`
- **B:** `super(x, y); this.width = width; this.height = height;`
- **C:** `return width * height;`
- **D:** `System.out.println("Rectangle: width=" + width + ", height=" + height + ", area=" + getArea());`

---

### (vi) Class Square

- **A:** `public class Square extends Rectangle {`
- **B:** `super(side, side, x, y); this.side = side;`

---

### (vii) Class Triangle

- **A:** `public class Triangle extends Shape {`
- **B:** `super(x, y); this.base = base; this.height = height;`
- **C:** `return 0.5 * base * height;`
- **D:** `System.out.println("Triangle: base=" + base + ", height=" + height + ", area=" + getArea());`

---

## QUESTION 3(d) - PYTHON IMPLEMENTATION

### (i) Class Shape

- **A:** `class Shape(ABC):`
- **B:** `self.x = x` and `self.y = y`
- **C:** `def __init__(self, x, y):`
- **D:** `@abstractmethod` followed by `def printDetails(self): pass`
- **E:** `@abstractmethod` followed by `def getArea(self): pass`

**Note:** Requires `from abc import ABC, abstractmethod` at top of file.

---

### (ii) Class Ellipse

- **A:** `class Ellipse(Shape):`
- **B:** `super().__init__(x, y)`
- **C:** `self.a = a` and `self.b = b`
- **D:** `self.a * self.b` (in context: `return math.pi * self.a * self.b`)
- **E:** `f"Ellipse: a={self.a}, b={self.b}, area={self.getArea()}"`

---

### (iii) Class Circle

- **A:** `class Circle(Ellipse):`
- **B:** `super().__init__(radius, radius, x, y); self.radius = radius`
- **C:** `return math.pi * self.radius * self.radius`

---

### (iv) Class Sector

- **A:** `class Sector(Circle):`
- **B:** `super().__init__(radius, x, y); self.angle = angle`
- **C:** `return 0.5 * self.radius * self.radius * self.angle`
- **D:** `print(f"Sector: radius={self.radius}, angle={self.angle}, area={self.getArea()}")`

---

### (v) Class Rectangle

- **A:** `class Rectangle(Shape):`
- **B:** `super().__init__(x, y); self.width = width; self.height = height`
- **C:** `return self.width * self.height`
- **D:** `print(f"Rectangle: width={self.width}, height={self.height}, area={self.getArea()}")`

---

### (vi) Class Square

- **A:** `class Square(Rectangle):`
- **B:** `super().__init__(side, side, x, y); self.side = side`

---

### (vii) Class Triangle

- **A:** `class Triangle(Shape):`
- **B:** `super().__init__(x, y); self.base = base; self.height = height`
- **C:** `return 0.5 * self.base * self.height`
- **D:** `print(f"Triangle: base={self.base}, height={self.height}, area={self.getArea()}")`

---

## IMPORTANT NOTES

1. **Abstract Classes:** Shape is abstract in both Java and Python
2. **Method Overriding:** All subclasses override `printDetails()` and `getArea()`
3. **Constructor Chaining:** Always call `super()` constructor/initializer first
4. **Java:** Use `@Override` annotation for clarity (not required but recommended)
5. **Python:** Use `@abstractmethod` decorator for abstract methods
6. **Imports:** 
   - Java: No special imports needed for basic classes
   - Python: `from abc import ABC, abstractmethod` and `import math`

---

## FORMULAE REFERENCE

- **Triangle:** Area = 0.5 × base × height
- **Rectangle:** Area = width × height  
- **Square:** Area = side²
- **Ellipse:** Area = π × a × b
- **Circle:** Area = π × r²
- **Sector:** Area = 0.5 × r² × θ (θ in radians)

