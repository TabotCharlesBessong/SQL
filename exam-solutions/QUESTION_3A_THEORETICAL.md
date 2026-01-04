# QUESTION 3(a) - THEORETICAL OOP QUESTIONS

---

## (i) Abstract vs Concrete Classes

### Abstract Classes:
- **Cannot be instantiated directly** - you cannot create objects from an abstract class
- May contain **abstract methods** (methods without implementation, only declaration)
- Can contain **concrete methods** (methods with implementation)
- Used as a base/template for other classes
- In Java, declared with `abstract` keyword
- In Python, typically implemented using ABC (Abstract Base Class) module

### Concrete Classes:
- **Can be instantiated directly** - you can create objects from a concrete class
- All methods have implementations
- Can be used to create objects immediately

### Which shapes belong to abstract classes?

From the inheritance hierarchy, **Shape** should be an abstract class because:
- It serves as a base class for all other shapes
- It likely defines abstract methods like `getArea()` that must be implemented by subclasses
- Different shapes have different ways to calculate area, so Shape itself shouldn't be instantiable

All other classes (Rectangle, Triangle, Square, Ellipse, Circle, Sector) are **concrete classes** because:
- They can be instantiated directly
- They have specific implementations for area calculations
- They represent actual, usable shapes

**Answer:** **Shape** is the abstract class. All other shapes (Rectangle, Triangle, Square, Ellipse, Circle, Sector) are concrete classes.

---

## (ii) Abstract vs Concrete Methods

### Abstract Methods:
- **Only have a declaration/signature, no implementation**
- Must be implemented by subclasses (in Java) or raise NotImplementedError (in Python)
- Force subclasses to provide their own implementation
- In Java: declared with `abstract` keyword and ends with `;`
- In Python: typically declared using `@abstractmethod` decorator

**Java Example:**
```java
abstract double getArea();  // No body, just declaration
```

**Python Example:**
```python
@abstractmethod
def getArea(self):
    raise NotImplementedError
```

### Concrete Methods:
- **Have a complete implementation**
- Provide actual functionality
- Can be called directly
- Can be inherited by subclasses (which may override them)

**Java Example:**
```java
public void printOrigin() {
    System.out.println("x:" + x + " y:" + y);
}
```

**Python Example:**
```python
def printOrigin(self):
    print(f"x:{self.x} y:{self.y}")
```

**Key Differences:**
1. **Implementation:** Abstract methods have no body; concrete methods have full implementation
2. **Usage:** Abstract methods cannot be called directly; concrete methods can be executed
3. **Inheritance:** Abstract methods must be implemented by subclasses; concrete methods can be inherited as-is or overridden
4. **Class Type:** Only abstract classes can contain abstract methods (in Java); concrete classes cannot have abstract methods unless they're also abstract

