# QUESTION 3(b) - JAVA IMPLEMENTATION SOLUTIONS

---

## (i) Class Shape

**Placeholders to fill:**
- A: First line (class declaration with abstract keyword and extends)
- B: Constructor code
- C: printDetails() method
- D: getArea() method

**Complete Solution:**

```java
abstract class Shape {
    private double x, y;
    
    // A: First line - abstract class declaration
    // Answer A: abstract class Shape {
    
    // B: Constructor
    public Shape(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    public void printOrigin() {
        System.out.println("x:" + x + " y:" + y);
    }
    
    // C: printDetails() method (abstract, must be implemented by subclasses)
    public abstract void printDetails();
    
    // D: getArea() method (abstract, must be implemented by subclasses)
    public abstract double getArea();
    
    // Getter methods for x and y (useful for subclasses)
    public double getX() { return x; }
    public double getY() { return y; }
}
```

**Answers:**
- **A:** `abstract class Shape {`
- **B:** `this.x = x; this.y = y;` (or two separate lines)
- **C:** `public abstract void printDetails();`
- **D:** `public abstract double getArea();`

---

## (ii) Class Ellipse

**Placeholders to fill:**
- A: First line (class declaration)
- B: Call superclass constructor
- C: Initializations
- D: getArea() return statement
- E: printDetails() print statement

**Complete Solution:**

```java
public class Ellipse extends Shape {
    private double a, b;  // semi-axes
    
    // A: First line
    // Answer A: public class Ellipse extends Shape {
    
    public Ellipse(double a, double b, double x, double y) {
        // B: Call superclass constructor
        super(x, y);
        
        // C: Initializations
        this.a = a;
        this.b = b;
    }
    
    public double getArea() {
        return Math.PI * a * b;  // D
    }
    
    public void printDetails() {
        System.out.println("Ellipse: a=" + a + ", b=" + b + ", area=" + getArea());  // E
    }
}
```

**Answers:**
- **A:** `public class Ellipse extends Shape {`
- **B:** `super(x, y);`
- **C:** `this.a = a; this.b = b;`
- **D:** `Math.PI * a * b`
- **E:** `"Ellipse: a=" + a + ", b=" + b + ", area=" + getArea()`

---

## (iii) Class Circle

**Placeholders to fill:**
- A: First line
- B: Constructor code
- C: getArea() code

**Complete Solution:**

```java
public class Circle extends Ellipse {
    private double radius;
    
    // A: First line
    // Answer A: public class Circle extends Ellipse {
    
    // B: Constructor
    public Circle(double radius, double x, double y) {
        super(radius, radius, x, y);  // Circle is ellipse with a = b = radius
        this.radius = radius;
    }
    
    public double getCircumference() {
        return 2 * Math.PI * radius;
    }
    
    // C: getArea() - override or use inherited method
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
```

**Answers:**
- **A:** `public class Circle extends Ellipse {`
- **B:** `super(radius, radius, x, y); this.radius = radius;`
- **C:** `return Math.PI * radius * radius;`

---

## (iv) Class Sector

**Placeholders to fill:**
- A: First line
- B: Constructor code
- C: getArea() code
- D: printDetails() code

**Complete Solution:**

```java
public class Sector extends Circle {
    private double angle;  // in radians
    
    // A: First line
    // Answer A: public class Sector extends Circle {
    
    // B: Constructor
    public Sector(double radius, double angle, double x, double y) {
        super(radius, x, y);
        this.angle = angle;
    }
    
    // C: getArea() - Sector area = 1/2 * r^2 * θ
    @Override
    public double getArea() {
        return 0.5 * getRadius() * getRadius() * angle;
    }
    
    // D: printDetails()
    @Override
    public void printDetails() {
        System.out.println("Sector: radius=" + getRadius() + ", angle=" + angle + 
                          ", area=" + getArea());
    }
    
    // Helper method to get radius (if Circle doesn't expose it)
    private double getRadius() {
        // Access radius through reflection or store it
        // Since Circle has radius, we need a getter in Circle
        // For now, assuming we can access it
        return super.getRadius();  // Need getter in Circle
    }
}
```

**Better Solution (assuming Circle has radius getter):**

```java
public class Sector extends Circle {
    private double angle;
    
    // A: First line
    // Answer A: public class Sector extends Circle {
    
    // B: Constructor
    public Sector(double radius, double angle, double x, double y) {
        super(radius, x, y);
        this.angle = angle;
    }
    
    // C: getArea()
    @Override
    public double getArea() {
        double radius = getRadius();  // Assuming Circle has getRadius()
        return 0.5 * radius * radius * angle;
    }
    
    // D: printDetails()
    @Override
    public void printDetails() {
        System.out.println("Sector: radius=" + getRadius() + ", angle=" + angle + 
                          ", area=" + getArea());
    }
}
```

**Note:** Circle class should have a getRadius() method. If not, we can store radius in Sector too.

**Answers:**
- **A:** `public class Sector extends Circle {`
- **B:** `super(radius, x, y); this.angle = angle;`
- **C:** `return 0.5 * getRadius() * getRadius() * angle;` (or with stored radius)
- **D:** `System.out.println("Sector: radius=" + getRadius() + ", angle=" + angle + ", area=" + getArea());`

---

## (v) Class Rectangle

**Placeholders to fill:**
- A: First line
- B: Constructor code
- C: getArea() code
- D: printDetails() code

**Complete Solution:**

```java
public class Rectangle extends Shape {
    private double width, height;
    
    // A: First line
    // Answer A: public class Rectangle extends Shape {
    
    // B: Constructor
    public Rectangle(double width, double height, double x, double y) {
        super(x, y);
        this.width = width;
        this.height = height;
    }
    
    // C: getArea()
    @Override
    public double getArea() {
        return width * height;
    }
    
    // D: printDetails()
    @Override
    public void printDetails() {
        System.out.println("Rectangle: width=" + width + ", height=" + height + 
                          ", area=" + getArea());
    }
}
```

**Answers:**
- **A:** `public class Rectangle extends Shape {`
- **B:** `super(x, y); this.width = width; this.height = height;`
- **C:** `return width * height;`
- **D:** `System.out.println("Rectangle: width=" + width + ", height=" + height + ", area=" + getArea());`

---

## (vi) Class Square

**Placeholders to fill:**
- A: First line
- B: Constructor code

**Complete Solution:**

```java
public class Square extends Rectangle {
    private double side;
    
    // A: First line
    // Answer A: public class Square extends Rectangle {
    
    // B: Constructor
    public Square(double side, double x, double y) {
        super(side, side, x, y);  // Square is rectangle with width = height = side
        this.side = side;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Square: side=" + side + ", area=" + getArea());
    }
}
```

**Answers:**
- **A:** `public class Square extends Rectangle {`
- **B:** `super(side, side, x, y); this.side = side;`

---

## (vii) Class Triangle

**Placeholders to fill:**
- A: First line
- B: Constructor code
- C: getArea() code
- D: printDetails() code

**Complete Solution:**

```java
public class Triangle extends Shape {
    private double base, height;
    
    // A: First line
    // Answer A: public class Triangle extends Shape {
    
    // B: Constructor
    public Triangle(double base, double height, double x, double y) {
        super(x, y);
        this.base = base;
        this.height = height;
    }
    
    // C: getArea()
    @Override
    public double getArea() {
        return 0.5 * base * height;
    }
    
    // D: printDetails()
    @Override
    public void printDetails() {
        System.out.println("Triangle: base=" + base + ", height=" + height + 
                          ", area=" + getArea());
    }
}
```

**Answers:**
- **A:** `public class Triangle extends Shape {`
- **B:** `super(x, y); this.base = base; this.height = height;`
- **C:** `return 0.5 * base * height;`
- **D:** `System.out.println("Triangle: base=" + base + ", height=" + height + ", area=" + getArea());`

