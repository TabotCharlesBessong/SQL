# QUESTION 3(c) - JAVA CODE SOLUTION

---

## Question (c): Write Java code that does the following:

(i) Creates a Shape array of size 6.
(ii) Creates an instance of each of the 6 shapes and stores them in the array.
(iii) Uses a for loop to iterate through the array and for every iteration, calls the `printOrigin()` and `printDetails()` methods.

---

## Complete Solution:

```java
public class ShapeTest {
    public static void main(String[] args) {
        // (i) Create Shape array of size 6
        Shape[] shapes = new Shape[6];
        
        // (ii) Create instances of each of the 6 shapes
        // The 6 shapes are: Rectangle, Triangle, Square, Ellipse, Circle, Sector
        
        shapes[0] = new Rectangle(5.0, 3.0, 1.0, 2.0);  // width=5, height=3, x=1, y=2
        shapes[1] = new Triangle(4.0, 6.0, 3.0, 4.0);   // base=4, height=6, x=3, y=4
        shapes[2] = new Square(4.0, 5.0, 6.0);          // side=4, x=5, y=6
        shapes[3] = new Ellipse(3.0, 2.0, 7.0, 8.0);    // a=3, b=2, x=7, y=8
        shapes[4] = new Circle(5.0, 9.0, 10.0);         // radius=5, x=9, y=10
        shapes[5] = new Sector(6.0, Math.PI/3, 11.0, 12.0); // radius=6, angle=π/3, x=11, y=12
        
        // (iii) Iterate through array and call methods
        for (Shape shape : shapes) {
            shape.printOrigin();
            shape.printDetails();
            System.out.println();  // Blank line for readability
        }
    }
}
```

---

## Alternative Solution (using traditional for loop):

```java
public class ShapeTest {
    public static void main(String[] args) {
        // (i) Create Shape array of size 6
        Shape[] shapes = new Shape[6];
        
        // (ii) Create instances of each of the 6 shapes
        shapes[0] = new Rectangle(5.0, 3.0, 1.0, 2.0);
        shapes[1] = new Triangle(4.0, 6.0, 3.0, 4.0);
        shapes[2] = new Square(4.0, 5.0, 6.0);
        shapes[3] = new Ellipse(3.0, 2.0, 7.0, 8.0);
        shapes[4] = new Circle(5.0, 9.0, 10.0);
        shapes[5] = new Sector(6.0, Math.PI/3, 11.0, 12.0);
        
        // (iii) Iterate using traditional for loop
        for (int i = 0; i < shapes.length; i++) {
            shapes[i].printOrigin();
            shapes[i].printDetails();
            System.out.println();
        }
    }
}
```

---

## Expected Output:

```
x:1.0 y:2.0
Rectangle: width=5.0, height=3.0, area=15.0

x:3.0 y:4.0
Triangle: base=4.0, height=6.0, area=12.0

x:5.0 y:6.0
Square: side=4.0, area=16.0

x:7.0 y:8.0
Ellipse: a=3.0, b=2.0, area=18.84955592153876

x:9.0 y:10.0
Circle: radius=5.0, area=78.53981633974483, circumference=31.41592653589793

x:11.0 y:12.0
Sector: radius=6.0, angle=1.0471975511965976, area=18.84955592153876

```

---

## Notes:

1. **Polymorphism**: All shapes are stored as `Shape` references, demonstrating polymorphism.
2. **Dynamic Dispatch**: When calling `printDetails()`, Java uses runtime polymorphism to call the correct overridden method for each shape type.
3. **Abstract Class**: Shape is abstract, so we cannot instantiate it directly. We can only create instances of its concrete subclasses.
4. **Array Declaration**: `Shape[] shapes = new Shape[6];` creates an array that can hold Shape references.
5. **For-Each Loop**: The enhanced for loop (`for (Shape shape : shapes)`) is preferred in modern Java, but traditional for loop is also acceptable.

