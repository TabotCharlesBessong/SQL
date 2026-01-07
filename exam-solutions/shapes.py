# Complete Python Implementation for Question 3
from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def printOrigin(self):
        print(f"x:{self.x} y:{self.y}")
    
    @abstractmethod
    def printDetails(self):
        pass
    
    @abstractmethod
    def getArea(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height, x, y):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def getArea(self):
        return self.width * self.height
    
    def printDetails(self):
        print(f"Rectangle: width={self.width}, height={self.height}, area={self.getArea()}")

# Square class
class Square(Rectangle):
    def __init__(self, side, x, y):
        super().__init__(side, side, x, y)
        self.side = side
    
    def printDetails(self):
        print(f"Square: side={self.side}, area={self.getArea()}")

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height, x, y):
        super().__init__(x, y)
        self.base = base
        self.height = height
    
    def getArea(self):
        return 0.5 * self.base * self.height
    
    def printDetails(self):
        print(f"Triangle: base={self.base}, height={self.height}, area={self.getArea()}")

# Ellipse class
class Ellipse(Shape):
    def __init__(self, a, b, x, y):
        super().__init__(x, y)
        self.a = a
        self.b = b
    
    def getArea(self):
        return math.pi * self.a * self.b
    
    def printDetails(self):
        print(f"Ellipse: a={self.a}, b={self.b}, area={self.getArea()}")

# Circle class
class Circle(Ellipse):
    def __init__(self, radius, x, y):
        super().__init__(radius, radius, x, y)
        self.radius = radius
    
    def getCircumference(self):
        return 2 * math.pi * self.radius
    
    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def printDetails(self):
        print(f"Circle: radius={self.radius}, area={self.getArea()}, "
              f"circumference={self.getCircumference()}")

# Sector class
class Sector(Circle):
    def __init__(self, radius, angle, x, y):
        super().__init__(radius, x, y)
        self.angle = angle
    
    def getArea(self):
        return 0.5 * self.radius * self.radius * self.angle
    
    def printDetails(self):
        print(f"Sector: radius={self.radius}, angle={self.angle}, area={self.getArea()}")

# Test function for Question 3(c) equivalent in Python
def main():
    # (i) Create list of 6 shapes
    shapes = []
    
    # (ii) Create instances of each of the 6 shapes
    shapes.append(Rectangle(5.0, 3.0, 1.0, 2.0))
    shapes.append(Triangle(4.0, 6.0, 3.0, 4.0))
    shapes.append(Square(4.0, 5.0, 6.0))
    shapes.append(Ellipse(3.0, 2.0, 7.0, 8.0))
    shapes.append(Circle(5.0, 9.0, 10.0))
    shapes.append(Sector(6.0, math.pi/3, 11.0, 12.0))
    
    # (iii) Iterate through list and call methods
    for shape in shapes:
        shape.printOrigin()
        shape.printDetails()
        print()

if __name__ == "__main__":
    main()





