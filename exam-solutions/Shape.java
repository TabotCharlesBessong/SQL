// Complete Java Implementation for Question 3
import java.util.*;

// Abstract base class
abstract class Shape {
    private double x, y;
    
    public Shape(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    public void printOrigin() {
        System.out.println("x:" + x + " y:" + y);
    }
    
    public abstract void printDetails();
    public abstract double getArea();
    
    public double getX() { return x; }
    public double getY() { return y; }
}

// Rectangle class
class Rectangle extends Shape {
    private double width, height;
    
    public Rectangle(double width, double height, double x, double y) {
        super(x, y);
        this.width = width;
        this.height = height;
    }
    
    @Override
    public double getArea() {
        return width * height;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Rectangle: width=" + width + ", height=" + height + 
                          ", area=" + getArea());
    }
}

// Square class
class Square extends Rectangle {
    private double side;
    
    public Square(double side, double x, double y) {
        super(side, side, x, y);
        this.side = side;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Square: side=" + side + ", area=" + getArea());
    }
}

// Triangle class
class Triangle extends Shape {
    private double base, height;
    
    public Triangle(double base, double height, double x, double y) {
        super(x, y);
        this.base = base;
        this.height = height;
    }
    
    @Override
    public double getArea() {
        return 0.5 * base * height;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Triangle: base=" + base + ", height=" + height + 
                          ", area=" + getArea());
    }
}

// Ellipse class
class Ellipse extends Shape {
    private double a, b;
    
    public Ellipse(double a, double b, double x, double y) {
        super(x, y);
        this.a = a;
        this.b = b;
    }
    
    @Override
    public double getArea() {
        return Math.PI * a * b;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Ellipse: a=" + a + ", b=" + b + ", area=" + getArea());
    }
}

// Circle class
class Circle extends Ellipse {
    private double radius;
    
    public Circle(double radius, double x, double y) {
        super(radius, radius, x, y);
        this.radius = radius;
    }
    
    public double getRadius() {
        return radius;
    }
    
    public double getCircumference() {
        return 2 * Math.PI * radius;
    }
    
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Circle: radius=" + radius + ", area=" + getArea() + 
                          ", circumference=" + getCircumference());
    }
}

// Sector class
class Sector extends Circle {
    private double angle;
    
    public Sector(double radius, double angle, double x, double y) {
        super(radius, x, y);
        this.angle = angle;
    }
    
    @Override
    public double getArea() {
        return 0.5 * getRadius() * getRadius() * angle;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Sector: radius=" + getRadius() + ", angle=" + angle + 
                          ", area=" + getArea());
    }
}

// Test class for Question 3(c)
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
        
        // (iii) Iterate through array and call methods
        for (Shape shape : shapes) {
            shape.printOrigin();
            shape.printDetails();
            System.out.println();
        }
    }
}

