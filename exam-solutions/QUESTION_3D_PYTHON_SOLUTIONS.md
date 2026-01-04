# QUESTION 3(d) - PYTHON IMPLEMENTATION SOLUTIONS

**Note:** Question (d) asks to "Repeat Question (b) and (c), but this time using Python"

---

## (i) Class Shape

**Placeholders to fill:**
- A: First line (class declaration)
- B: Provide lines of code for the initializer
- C: That takes parameters x and y
- D: printDetails() method
- E: getArea() method

**Complete Solution:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    # A: First line
    # Answer A: class Shape(ABC):
    
    def __init__(self, x, y):
        # B: Provide lines of code for the initializer
        # C: That takes parameters x and y
        self.x = x
        self.y = y
    
    def printOrigin(self):
        print(f"x:{self.x} y:{self.y}")
    
    # D: printDetails() method (abstract)
    @abstractmethod
    def printDetails(self):
        pass
    
    # E: getArea() method (abstract)
    @abstractmethod
    def getArea(self):
        pass
```

**Answers:**
- **A:** `class Shape(ABC):`
- **B:** `self.x = x` and `self.y = y`
- **C:** `def __init__(self, x, y):`
- **D:** `@abstractmethod` followed by `def printDetails(self): pass`
- **E:** `@abstractmethod` followed by `def getArea(self): pass`

---

## (ii) Class Ellipse

**Placeholders to fill:**
- A: First line
- B: Call superclass initializer
- C: Initializations
- D: getArea() return statement
- E: printDetails() print statement

**Complete Solution:**

```python
import math

class Ellipse(Shape):
    # A: First line
    # Answer A: class Ellipse(Shape):
    
    def __init__(self, a, b, x, y):
        # B: Call superclass initializer
        super().__init__(x, y)
        
        # C: Initializations
        self.a = a
        self.b = b
    
    def getArea(self):
        return math.pi * self.a * self.b  # D
    
    def printDetails(self):
        print(f"Ellipse: a={self.a}, b={self.b}, area={self.getArea()}")  # E
```

**Answers:**
- **A:** `class Ellipse(Shape):`
- **B:** `super().__init__(x, y)`
- **C:** `self.a = a` and `self.b = b`
- **D:** `self.a * self.b`
- **E:** `f"Ellipse: a={self.a}, b={self.b}, area={self.getArea()}"`

---

## (iii) Class Circle

**Placeholders to fill:**
- A: First line
- B: Code for initializer
- C: Code for getArea()

**Complete Solution:**

```python
class Circle(Ellipse):
    # A: First line
    # Answer A: class Circle(Ellipse):
    
    def __init__(self, radius, x, y):
        # B: Code for initializer
        super().__init__(radius, radius, x, y)  # Circle is ellipse with a = b = radius
        self.radius = radius
    
    def getCircumference(self):
        return 2 * math.pi * self.radius
    
    # C: Code for getArea()
    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def printDetails(self):
        print(f"Circle: radius={self.radius}, area={self.getArea()}, "
              f"circumference={self.getCircumference()}")
```

**Answers:**
- **A:** `class Circle(Ellipse):`
- **B:** `super().__init__(radius, radius, x, y); self.radius = radius`
- **C:** `return math.pi * self.radius * self.radius`

---

## (iv) Class Sector

**Placeholders to fill:**
- A: First line
- B: Code for initializer
- C: Code for getArea()
- D: Code for printDetails()

**Complete Solution:**

```python
class Sector(Circle):
    # A: First line
    # Answer A: class Sector(Circle):
    
    def __init__(self, radius, angle, x, y):
        # B: Code for initializer
        super().__init__(radius, x, y)
        self.angle = angle  # angle in radians
    
    # C: Code for getArea()
    def getArea(self):
        return 0.5 * self.radius * self.radius * self.angle
    
    # D: Code for printDetails()
    def printDetails(self):
        print(f"Sector: radius={self.radius}, angle={self.angle}, area={self.getArea()}")
```

**Answers:**
- **A:** `class Sector(Circle):`
- **B:** `super().__init__(radius, x, y); self.angle = angle`
- **C:** `return 0.5 * self.radius * self.radius * self.angle`
- **D:** `print(f"Sector: radius={self.radius}, angle={self.angle}, area={self.getArea()}")`

---

## (v) Class Rectangle

**Placeholders to fill:**
- A: First line
- B: Code for initializer
- C: Code for getArea()
- D: Code for printDetails()

**Complete Solution:**

```python
class Rectangle(Shape):
    # A: First line
    # Answer A: class Rectangle(Shape):
    
    def __init__(self, width, height, x, y):
        # B: Code for initializer
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    # C: Code for getArea()
    def getArea(self):
        return self.width * self.height
    
    # D: Code for printDetails()
    def printDetails(self):
        print(f"Rectangle: width={self.width}, height={self.height}, area={self.getArea()}")
```

**Answers:**
- **A:** `class Rectangle(Shape):`
- **B:** `super().__init__(x, y); self.width = width; self.height = height`
- **C:** `return self.width * self.height`
- **D:** `print(f"Rectangle: width={self.width}, height={self.height}, area={self.getArea()}")`

---

## (vi) Class Square

**Placeholders to fill:**
- A: First line
- B: Code for initializer

**Complete Solution:**

```python
class Square(Rectangle):
    # A: First line
    # Answer A: class Square(Rectangle):
    
    def __init__(self, side, x, y):
        # B: Code for initializer
        super().__init__(side, side, x, y)  # Square is rectangle with width = height = side
        self.side = side
    
    def printDetails(self):
        print(f"Square: side={self.side}, area={self.getArea()}")
```

**Answers:**
- **A:** `class Square(Rectangle):`
- **B:** `super().__init__(side, side, x, y); self.side = side`

---

## (vii) Class Triangle

**Placeholders to fill:**
- A: First line
- B: Code for initializer
- C: Code for getArea()
- D: Code for printDetails()

**Complete Solution:**

```python
class Triangle(Shape):
    # A: First line
    # Answer A: class Triangle(Shape):
    
    def __init__(self, base, height, x, y):
        # B: Code for initializer
        super().__init__(x, y)
        self.base = base
        self.height = height
    
    # C: Code for getArea()
    def getArea(self):
        return 0.5 * self.base * self.height
    
    # D: Code for printDetails()
    def printDetails(self):
        print(f"Triangle: base={self.base}, height={self.height}, area={self.getArea()}")
```

**Answers:**
- **A:** `class Triangle(Shape):`
- **B:** `super().__init__(x, y); self.base = base; self.height = height`
- **C:** `return 0.5 * self.base * self.height`
- **D:** `print(f"Triangle: base={self.base}, height={self.height}, area={self.getArea()}")`

---

## Question (c) Equivalent in Python

**Python code that does the following:**
(i) Creates a list of 6 shapes
(ii) Creates an instance of each of the 6 shapes and stores them in the list
(iii) Uses a for loop to iterate through the list and for every iteration, calls the `printOrigin()` and `printDetails()` methods

**Complete Solution:**

```python
def main():
    # (i) Create list of 6 shapes
    shapes = []
    
    # (ii) Create instances of each of the 6 shapes
    shapes.append(Rectangle(5.0, 3.0, 1.0, 2.0))  # width=5, height=3, x=1, y=2
    shapes.append(Triangle(4.0, 6.0, 3.0, 4.0))   # base=4, height=6, x=3, y=4
    shapes.append(Square(4.0, 5.0, 6.0))          # side=4, x=5, y=6
    shapes.append(Ellipse(3.0, 2.0, 7.0, 8.0))    # a=3, b=2, x=7, y=8
    shapes.append(Circle(5.0, 9.0, 10.0))         # radius=5, x=9, y=10
    shapes.append(Sector(6.0, math.pi/3, 11.0, 12.0))  # radius=6, angle=π/3, x=11, y=12
    
    # (iii) Iterate through list and call methods
    for shape in shapes:
        shape.printOrigin()
        shape.printDetails()
        print()  # Blank line for readability

if __name__ == "__main__":
    main()
```

---

## Alternative Solution (using list comprehension or direct list creation):

```python
def main():
    # (i) & (ii) Create list with instances
    shapes = [
        Rectangle(5.0, 3.0, 1.0, 2.0),
        Triangle(4.0, 6.0, 3.0, 4.0),
        Square(4.0, 5.0, 6.0),
        Ellipse(3.0, 2.0, 7.0, 8.0),
        Circle(5.0, 9.0, 10.0),
        Sector(6.0, math.pi/3, 11.0, 12.0)
    ]
    
    # (iii) Iterate through list
    for shape in shapes:
        shape.printOrigin()
        shape.printDetails()
        print()

if __name__ == "__main__":
    main()
```

