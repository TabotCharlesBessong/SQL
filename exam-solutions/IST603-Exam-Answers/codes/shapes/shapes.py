import math
from typing import List

class Shape:
    def __init__(self, shape: str):
        self.shape = shape
    
    def __str__(self):
        return f"I am a {self.shape}"

class Polygon(Shape):
    def __init__(self, shape: str, side_lengths: List[int]):
        super().__init__(shape)
        self.side_lengths = side_lengths
    
    def compute_perimeter(self) -> int:
        if not self.side_lengths:
            return 0
        return sum(self.side_lengths)
    
    def get_number_of_sides(self) -> int:
        return len(self.side_lengths) if self.side_lengths else 0

class Triangle(Polygon):
    def __init__(self, side1: int = None, side2: int = None, side3: int = None, sides: List[int] = None):
        if sides is not None:
            if len(sides) != 3:
                raise ValueError("Triangle must have exactly 3 sides")
            super().__init__("Triangle", sides)
        else:
            if side1 is None or side2 is None or side3 is None:
                raise ValueError("Must provide either 3 individual sides or a list of sides")
            super().__init__("Triangle", [side1, side2, side3])
        
        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle: sides do not satisfy triangle inequality")
    
    def _is_valid_triangle(self) -> bool:
        if len(self.side_lengths) != 3:
            return False
        a, b, c = self.side_lengths
        return (a + b > c) and (a + c > b) and (b + c > a)
    
    def compute_area(self) -> float:
        """Calculate area using Heron's formula"""
        s = self.compute_perimeter() / 2.0  # semi-perimeter
        a, b, c = self.side_lengths
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def get_triangle_type(self) -> str:
        a, b, c = self.side_lengths
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"
    
    def __str__(self):
        return (f"{super().__str__()} with sides {self.side_lengths} "
                f"(Type: {self.get_triangle_type()}, Area: {self.compute_area():.2f})")

class Rectangle(Polygon):
    def __init__(self, width: int = None, height: int = None, sides: List[int] = None):
        if sides is not None:
            if len(sides) != 4:
                raise ValueError("Rectangle must have exactly 4 sides")
            if not self._is_valid_rectangle_sides(sides):
                raise ValueError("Invalid rectangle: opposite sides must be equal")
            super().__init__("Rectangle", sides)
            sorted_sides = sorted(sides)
            self.width = sorted_sides[0]
            self.height = sorted_sides[2]
        else:
            if width is None or height is None:
                raise ValueError("Must provide either width/height or list of sides")
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive")
            super().__init__("Rectangle", [width, height, width, height])
            self.width = width
            self.height = height
    
    def _is_valid_rectangle_sides(self, sides: List[int]) -> bool:
        if len(sides) != 4:
            return False
        sorted_sides = sorted(sides)
        return sorted_sides[0] == sorted_sides[1] and sorted_sides[2] == sorted_sides[3]
    
    def compute_area(self) -> int:
        return self.width * self.height
    
    def is_square(self) -> bool:
        return self.width == self.height
    
    def get_diagonal(self) -> float:
        return math.sqrt(self.width**2 + self.height**2)
    
    def __str__(self):
        shape_type = "Square" if self.is_square() else "Rectangle"
        return (f"I am a {shape_type} with width={self.width}, height={self.height} "
                f"(Area: {self.compute_area()}, Diagonal: {self.get_diagonal():.2f})")

# Demo usage
if __name__ == "__main__":
    print("=== Testing Triangle ===")
    try:
        # Valid triangle
        t1 = Triangle(3, 4, 5)
        print(f"Triangle 1: {t1}")
        print(f"Perimeter: {t1.compute_perimeter()}")
        print(f"Number of sides: {t1.get_number_of_sides()}")
        
        # Equilateral triangle
        t2 = Triangle(sides=[5, 5, 5])
        print(f"Triangle 2: {t2}")
        
        # Invalid triangle (should raise exception)
        try:
            t3 = Triangle(1, 2, 10)
        except ValueError as e:
            print(f"Error creating invalid triangle: {e}")
            
    except Exception as e:
        print(f"Triangle error: {e}")
    
    print("\n=== Testing Rectangle ===")
    try:
        # Regular rectangle
        r1 = Rectangle(4, 6)
        print(f"Rectangle 1: {r1}")
        print(f"Perimeter: {r1.compute_perimeter()}")
        print(f"Number of sides: {r1.get_number_of_sides()}")
        
        # Square
        r2 = Rectangle(5, 5)
        print(f"Rectangle 2 (Square): {r2}")
        
        # Rectangle from sides list
        r3 = Rectangle(sides=[3, 7, 3, 7])
        print(f"Rectangle 3: {r3}")
        
        # Invalid rectangle (should raise exception)
        try:
            r4 = Rectangle(sides=[1, 2, 3, 4])
        except ValueError as e:
            print(f"Error creating invalid rectangle: {e}")
            
    except Exception as e:
        print(f"Rectangle error: {e}")