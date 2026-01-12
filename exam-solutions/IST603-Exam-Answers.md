# IST603 - Object-Oriented Programming with Java and Python
## Exam Answers - First Semester Examination 2022/2023

**University of Buea, Faculty of Science**  
**Department: Computer Science**  
**Course Code: IST603**  
**Course Title: Object-Oriented Programming with Java and Python**  
**Date: 24/01/2023**  
**Instructor: Denis Nkweteyim**

---

## QUESTION 1 (10 + 4 = 14 marks)

### Part a) Briefly explain the following object-oriented programming concepts (10 marks)

#### (i) Abstraction (2 marks)

**Definition:**
Abstraction is the process of hiding complex implementation details and showing only the essential features or interface of an object to the user. It focuses on what an object does rather than how it does it.

**Key Points:**
- **Simplification:** Abstraction simplifies complex systems by exposing only relevant features
- **Interface vs. Implementation:** It separates the interface (what can be done) from the implementation (how it's done)
- **Real-world Analogy:** Like driving a car - you use the steering wheel, pedals, and gear shift without needing to understand the engine mechanics
- **Benefits:**
  - Reduces complexity for users
  - Allows changes to implementation without affecting users
  - Makes code more maintainable and understandable

**Example:**
```python
# Abstract concept: A vehicle can start and stop
class Vehicle:
    def start(self):
        pass  # Implementation hidden
    
    def stop(self):
        pass  # Implementation hidden

# User doesn't need to know how engine works internally
```

In Java, abstraction is achieved through:
- Abstract classes (classes with `abstract` keyword)
- Interfaces
- Abstract methods (methods without body)

---

#### (ii) Encapsulation (2 marks)

**Definition:**
Encapsulation is the bundling of data (attributes/variables) and methods (functions) that operate on that data into a single unit called a class. It also involves restricting direct access to some of the object's components, typically by making data private and providing controlled access through public methods.

**Key Points:**
- **Data Hiding:** Internal data is hidden from outside access
- **Access Modifiers:** Use of private, protected, and public keywords to control access
- **Controlled Access:** Access to data is controlled through getter and setter methods
- **Benefits:**
  - Protects data from unauthorized access and modification
  - Makes code more secure and less error-prone
  - Allows validation of data before modification
  - Changes to internal implementation don't affect external code

**Example:**
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute (encapsulated)
    
    def deposit(self, amount):  # Controlled access
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")
    
    def get_balance(self):  # Getter method
        return self.__balance
```

In Java:
```java
public class BankAccount {
    private double balance;  // Encapsulated (private)
    
    public void deposit(double amount) {  // Controlled access
        if (amount > 0) {
            balance += amount;
        }
    }
    
    public double getBalance() {  // Getter method
        return balance;
    }
}
```

---

#### (iii) Composition (2 marks)

**Definition:**
Composition is a "has-a" relationship between classes where one class contains an instance of another class as part of its structure. The contained object cannot exist independently of the container - if the container is destroyed, the contained objects are also destroyed.

**Key Points:**
- **"Has-a" Relationship:** One object is composed of other objects
- **Strong Ownership:** The composed objects are owned by the container
- **Lifecycle Dependency:** Composed objects exist only as long as the container exists
- **Cannot Exist Independently:** The parts cannot exist without the whole

**Example:**
```python
class Engine:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        print(f"Engine with {self.power} HP started")

class Car:
    def __init__(self, brand, engine_power):
        self.brand = brand
        self.engine = Engine(engine_power)  # Composition: Car HAS-A Engine
    
    def start(self):
        print(f"{self.brand} car:")
        self.engine.start()

# Usage
car = Car("Toyota", 150)
car.start()
# When car is destroyed, engine is also destroyed
```

**Composition vs. Aggregation:**
- **Composition:** Strong "has-a" relationship, parts cannot exist without whole (e.g., House-Room)
- **Aggregation:** Weak "has-a" relationship, parts can exist independently (e.g., University-Student)

---

#### (iv) Inheritance (2 marks)

**Definition:**
Inheritance is a mechanism in OOP where a new class (child/subclass) is created from an existing class (parent/superclass). The child class inherits all attributes and methods from the parent class and can add new attributes/methods or override existing ones.

**Key Points:**
- **"Is-a" Relationship:** Child class is a type of parent class
- **Code Reusability:** Avoids code duplication by reusing parent class code
- **Hierarchical Structure:** Creates a class hierarchy
- **Extensibility:** Child classes can extend parent functionality
- **Method Overriding:** Child classes can provide specific implementations

**Example:**
```python
class Animal:  # Parent/Superclass
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Some sound")

class Dog(Animal):  # Child/Subclass
    def make_sound(self):  # Override parent method
        print("Woof!")
    
    def fetch(self):  # New method
        print(f"{self.name} is fetching")

# Usage
dog = Dog("Buddy")
print(dog.name)  # Inherited attribute
dog.make_sound()  # Overridden method
dog.fetch()  # New method
```

In Java:
```java
class Animal {
    protected String name;
    
    public Animal(String name) {
        this.name = name;
    }
    
    public void makeSound() {
        System.out.println("Some sound");
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);  // Call parent constructor
    }
    
    @Override
    public void makeSound() {  // Override
        System.out.println("Woof!");
    }
}
```

---

#### (v) Polymorphism (2 marks)

**Definition:**
Polymorphism means "many forms" - it allows objects of different classes to be treated as objects of a common superclass. The same interface can be used to represent different underlying forms. There are two main types: compile-time (method overloading) and runtime (method overriding).

**Key Points:**
- **"One Interface, Many Forms":** Same method name, different implementations
- **Runtime Polymorphism:** Achieved through method overriding (late binding)
- **Compile-time Polymorphism:** Achieved through method overloading (early binding)
- **Flexibility:** Allows writing code that works with multiple types
- **Dynamic Method Dispatch:** The method called is determined at runtime based on object type

**Example (Runtime Polymorphism - Method Overriding):**
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Override
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Override
        return 3.14159 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 3), Circle(2)]

for shape in shapes:  # Same interface, different forms
    print(f"Area: {shape.area()}")
```

**Method Overloading (Compile-time Polymorphism):**
```python
# Python doesn't support true overloading, but we can simulate
class Calculator:
    def add(self, a, b=0, c=0):  # Default parameters simulate overloading
        return a + b + c

calc = Calculator()
print(calc.add(5))      # 5
print(calc.add(5, 3))   # 8
print(calc.add(5, 3, 2)) # 10
```

In Java (with true overloading):
```java
class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public int add(int a, int b, int c) {  // Overloaded method
        return a + b + c;
    }
    
    public double add(double a, double b) {  // Different parameter types
        return a + b;
    }
}
```

**Benefits:**
- Increases flexibility and extensibility
- Simplifies code maintenance
- Enables generic programming

---

### Part b) Write the output you would get from the following Python code fragments (4 marks)

#### Fragment i) Python String Slicing (1 mark)

**Code:**
```python
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
```

**Detailed Explanation:**

**String:** `"Hello, World!"`
- Indices: `H(0) e(1) l(2) l(3) o(4) ,(5)  (6) W(7) o(8) r(9) l(10) d(11) !(12)`
- Negative indices: `!(-1) d(-2) l(-3) r(-4) o(-5) W(-6)  (-7) ,(-8) o(-9) l(-10) l(-11) e(-12) H(-13)`

**Output Analysis:**

1. **`print(b[2:5])`**
   - Start at index 2: `l`
   - End before index 5: `o` (index 4 is included)
   - Slice: `b[2:5]` = `"llo"`
   - **Output: `llo`**

2. **`print(b[:5])`**
   - Start from beginning (index 0)
   - End before index 5: `o` (index 4 is included)
   - Slice: `b[0:5]` = `"Hello"`
   - **Output: `Hello`**

3. **`print(b[2:])`**
   - Start at index 2: `l`
   - End at the end of string (default)
   - Slice: `b[2:]` = `"llo, World!"`
   - **Output: `llo, World!`**

4. **`print(b[-5:-2])`**
   - Start at index -5: `W` (from the end)
   - End before index -2: `d` (index -3 is included)
   - Negative indices: `W(-5) o(-4) r(-3) l(-2) d(-1)`
   - Slice: `b[-5:-2]` = `"Wor"` (includes -5, -4, -3, stops before -2)
   - **Output: `Wor`**

**Note:** The handwritten output in the image shows "orld" for `b[-5:-2]`, but the correct output is `"Wor"` because:
- `b[-5]` = `'W'` (5th from end)
- `b[-4]` = `'o'`
- `b[-3]` = `'r'`
- `b[-2]` = `'l'` (excluded because slice is `[-5:-2)`, open-ended on right)

**Complete Output:**
```
llo
Hello
llo, World!
Wor
```

---

#### Fragment ii) Python Dictionary (1 mark)

**Code:**
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
```

**Detailed Explanation:**

**Key Concept: Dictionary Keys Must Be Unique**
- In Python dictionaries, duplicate keys are not allowed
- When duplicate keys are present, the **last value overwrites previous values**
- This happens during dictionary creation, not at runtime

**Dictionary Creation Process:**
1. `"brand": "Ford"` → Added
2. `"model": "Mustang"` → Added
3. `"year": 1964` → Added
4. `"year": 2020` → **Overwrites** the previous `"year": 1964`

**Final Dictionary:**
```python
{
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020  # Only this value remains
}
```

**Output:**
```
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

**Note:** The output format may vary slightly (single vs. double quotes), but the content will be:
- `brand: 'Ford'`
- `model: 'Mustang'`
- `year: 2020` (not 1964)

---

#### Fragment iii) Python Dictionary and `.values()` (2 marks)

**Code:**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
car["color"] = "red"
car["year"] = 2020
print(x)
```

**Detailed Explanation:**

**Key Concept: Dictionary View Objects**
- `dict.values()` returns a **view object**, not a copy
- View objects are **dynamic** - they reflect changes to the dictionary in real-time
- The view is like a "window" into the dictionary's values

**Step-by-Step Execution:**

1. **Initial Dictionary:**
   ```python
   car = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
   }
   ```

2. **Create View Object:**
   ```python
   x = car.values()
   ```
   - `x` is a `dict_values` view object
   - It references the values in `car`, not a copy

3. **First Print:**
   ```python
   print(x)
   ```
   - Prints the current values: `dict_values(['Ford', 'Mustang', 1964])`
   - **Output: `dict_values(['Ford', 'Mustang', 1964])`**

4. **Modify Dictionary:**
   ```python
   car["color"] = "red"    # Add new key-value pair
   car["year"] = 2020      # Update existing value
   ```
   - Dictionary now: `{"brand": "Ford", "model": "Mustang", "year": 2020, "color": "red"}`
   - The view object `x` automatically reflects these changes

5. **Second Print:**
   ```python
   print(x)
   ```
   - Prints the updated values: `dict_values(['Ford', 'Mustang', 2020, 'red'])`
   - Notice: `1964` changed to `2020`, and `'red'` was added
   - **Output: `dict_values(['Ford', 'Mustang', 2020, 'red'])`**

**Complete Output:**
```
dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 2020, 'red'])
```

**Important Notes:**
- View objects are **live references**, not copies
- If you want a snapshot/copy, use: `list(car.values())` or `list(x)`
- The same behavior applies to `dict.keys()` and `dict.items()`

---

## QUESTION 2 ([3+2+2+2+4] * 2 = 26 marks)

### Part a) Python Implementation (13 marks)

#### i) Write class `Shape` (3 marks)

**Code:**
```python
class Shape():
    def __init__(self):
        # Store the string 'shape' in instance variable shape
        self.shape = 'shape'
    
    def __str__(self):
        # Return string: "I am a shape" where shape is replaced by instance variable
        return f"I am a {self.shape}"
```

**Detailed Explanation:**

**`__init__` Method:**
- Constructor that initializes the object
- `self.shape = 'shape'` creates an instance variable storing the string 'shape'
- Every `Shape` object will have `self.shape = 'shape'`

**`__str__` Method:**
- Special method that returns a string representation of the object
- Called automatically by `print()` and `str()` functions
- Uses f-string formatting to insert `self.shape` into the template string
- Returns: `"I am a shape"` (where `shape` comes from `self.shape`)

**Alternative Implementation (without f-strings):**
```python
def __str__(self):
    return "I am a " + self.shape
```

---

#### ii) Write class `Polygon` (subclass of `Shape`) (2 marks)

**Code:**
```python
class Polygon(Shape):
    def __init__(self):
        # Call parent constructor (optional, but good practice)
        super().__init__()
        # Assign 'polygon' to instance variable shape
        self.shape = 'polygon'
        # Assign None to list instance variable side_lengths
        self.side_lengths = None
    
    def compute_perimeter(self):
        # Return sum of values in side_lengths using sum() function
        return sum(self.side_lengths)
    
    def get_number_of_edges(self):
        # Return length of side_lengths list using len() function
        return len(self.side_lengths)
```

**Detailed Explanation:**

**Inheritance:**
- `class Polygon(Shape)` makes `Polygon` inherit from `Shape`
- `Polygon` gets all attributes and methods from `Shape`

**`__init__` Method:**
- `super().__init__()` calls parent constructor (initializes `self.shape = 'shape'`)
- `self.shape = 'polygon'` **overrides** the parent's value
- `self.side_lengths = None` initializes the list variable as `None`

**`compute_perimeter` Method:**
- Uses Python's built-in `sum()` function
- `sum(self.side_lengths)` adds all values in the list
- Returns the total perimeter

**`get_number_of_edges` Method:**
- Uses Python's built-in `len()` function
- `len(self.side_lengths)` returns the number of items in the list
- This equals the number of edges/sides

**Note:** These methods assume `self.side_lengths` is not `None`. In production code, you'd add validation.

---

#### iii) Write class `Rectangle` (subclass of `Polygon`) (2 marks)

**Code:**
```python
class Rectangle(Polygon):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        # Assign 'rectangle' to instance variable shape
        self.shape = 'rectangle'
        # Initialize side_lengths with [1, 1, 1, 1]
        self.side_lengths = [1, 1, 1, 1]
```

**Detailed Explanation:**

**Inheritance:**
- `Rectangle` inherits from `Polygon`, which inherits from `Shape`
- Multi-level inheritance: `Shape` → `Polygon` → `Rectangle`

**`__init__` Method:**
- `super().__init__()` calls `Polygon.__init__()`, which sets `self.shape = 'polygon'` and `self.side_lengths = None`
- `self.shape = 'rectangle'` overrides to 'rectangle'
- `self.side_lengths = [1, 1, 1, 1]` initializes with four sides of length 1 each
- A rectangle has 4 sides, so the list has 4 elements

**Inherited Methods:**
- `Rectangle` automatically inherits:
  - `compute_perimeter()` from `Polygon` (will return 1+1+1+1 = 4)
  - `get_number_of_edges()` from `Polygon` (will return 4)
  - `__str__()` from `Shape` (will return "I am a rectangle")

---

#### iv) Write class `Triangle` (subclass of `Polygon`) (2 marks)

**Code:**
```python
class Triangle(Polygon):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        # Assign 'triangle' to instance variable shape
        self.shape = 'triangle'
        # Initialize side_lengths with [2, 2, 2]
        self.side_lengths = [2, 2, 2]
```

**Detailed Explanation:**

**Similar to Rectangle:**
- Inherits from `Polygon`
- Overrides `self.shape` to 'triangle'
- Initializes `self.side_lengths = [2, 2, 2]` (3 sides for a triangle)
- Each side has length 2

**Inherited Methods:**
- `compute_perimeter()` will return 2+2+2 = 6
- `get_number_of_edges()` will return 3
- `__str__()` will return "I am a triangle"

---

#### v) Write the outputs (4 marks)

**Code:**
```python
# (v-1)
s = Shape()
print(s)

# (v-2)
p = Polygon()
print(p)

# (v-3)
rect = Rectangle()
print(rect)
rect.compute_perimeter()

# (v-4)
tri = Triangle()
print(tri)
tri.compute_perimeter()
```

**Detailed Output Analysis:**

**(v-1) `s = Shape()` and `print(s)`**
- Creates `Shape` object: `self.shape = 'shape'`
- `print(s)` calls `__str__()` method
- Returns: `"I am a shape"`
- **Output: `I am a shape`**

**(v-2) `p = Polygon()` and `print(p)`**
- Creates `Polygon` object: `self.shape = 'polygon'`
- `print(p)` calls `__str__()` (inherited from `Shape`)
- Returns: `"I am a polygon"` (uses `self.shape` which is 'polygon')
- **Output: `I am a polygon`**

**(v-3) `rect = Rectangle()` and `print(rect)` and `rect.compute_perimeter()`**
- Creates `Rectangle` object: `self.shape = 'rectangle'`, `self.side_lengths = [1, 1, 1, 1]`
- `print(rect)` calls `__str__()` (inherited from `Shape`, uses `self.shape = 'rectangle'`)
- Returns: `"I am a rectangle"`
- `rect.compute_perimeter()` calls inherited method from `Polygon`
- Returns: `sum([1, 1, 1, 1]) = 4`
- **Output:**
  ```
  I am a rectangle
  ```
  (Note: `compute_perimeter()` returns 4 but doesn't print it - would need `print(rect.compute_perimeter())`)

**(v-4) `tri = Triangle()` and `print(tri)` and `tri.compute_perimeter()`**
- Creates `Triangle` object: `self.shape = 'triangle'`, `self.side_lengths = [2, 2, 2]`
- `print(tri)` returns: `"I am a triangle"`
- `tri.compute_perimeter()` returns: `sum([2, 2, 2]) = 6`
- **Output:**
  ```
  I am a triangle
  ```
  (Note: `compute_perimeter()` returns 6 but doesn't print it)

**Complete Output:**
```
I am a shape
I am a polygon
I am a rectangle
I am a triangle
```

**Note:** The `compute_perimeter()` calls return values but don't print them. If the question expected printed output, you would need:
```python
print(rect.compute_perimeter())  # Output: 4
print(tri.compute_perimeter())   # Output: 6
```

---

### Part b) Java Implementation (13 marks)

#### i) Write class `Shape` (3 marks)

**Code:**
```java
public class Shape {
    // Instance variable to store the string 'shape'
    private String shape;
    
    // Constructor
    public Shape() {
        this.shape = "shape";
    }
    
    // Override toString() method (equivalent to __str__ in Python)
    @Override
    public String toString() {
        return "I am a " + this.shape;
    }
}
```

**Detailed Explanation:**

**Class Declaration:**
- `public class Shape` declares a public class
- In Java, class name must match filename (`Shape.java`)

**Instance Variable:**
- `private String shape;` - private instance variable (encapsulation)
- Type: `String` (Java uses String, not string)

**Constructor:**
- `public Shape()` - no-argument constructor
- `this.shape = "shape";` - initializes instance variable
- `this` keyword refers to current object (like `self` in Python)

**toString() Method:**
- `@Override` annotation indicates we're overriding `Object.toString()`
- Called automatically by `System.out.println()` (like `__str__` in Python)
- Returns concatenated string: `"I am a " + this.shape`

**Alternative (using String.format):**
```java
public String toString() {
    return String.format("I am a %s", this.shape);
}
```

---

#### ii) Write class `Polygon` (subclass of `Shape`) (2 marks)

**Code:**
```java
import java.util.ArrayList;

public class Polygon extends Shape {
    // Instance variable for side lengths (using ArrayList or array)
    private ArrayList<Integer> sideLengths;
    // Alternative: private int[] sideLengths;
    
    // Constructor
    public Polygon() {
        super();  // Call parent constructor
        this.shape = "polygon";  // Override shape
        this.sideLengths = null;  // Initialize as null
    }
    
    // Method to compute perimeter
    public int computePerimeter() {
        int sum = 0;
        for (int length : this.sideLengths) {
            sum += length;
        }
        return sum;
    }
    
    // Method to get number of edges
    public int getNumberOfEdges() {
        return this.sideLengths.size();
    }
}
```

**Detailed Explanation:**

**Inheritance:**
- `extends Shape` makes `Polygon` inherit from `Shape`
- `Polygon` gets all public/protected members from `Shape`

**Instance Variable:**
- `private ArrayList<Integer> sideLengths;` - list of integers
- Alternative: `private int[] sideLengths;` (array instead of ArrayList)
- Initialized as `null` in constructor

**Constructor:**
- `super()` calls parent constructor (`Shape()`)
- `this.shape = "polygon"` - Note: `shape` must be `protected` in `Shape` for this to work, or provide a setter method

**Better Implementation (with protected access):**
```java
// In Shape class, change to:
protected String shape;  // protected so subclasses can access

// Or provide setter:
public void setShape(String shape) {
    this.shape = shape;
}
```

**computePerimeter() Method:**
- Uses enhanced for-loop to iterate through `sideLengths`
- Sums all values and returns total

**getNumberOfEdges() Method:**
- Uses `ArrayList.size()` to get number of elements
- Equivalent to `len()` in Python

**Note:** In practice, add null checks:
```java
public int computePerimeter() {
    if (this.sideLengths == null) {
        return 0;
    }
    // ... rest of code
}
```

---

#### iii) Write class `Rectangle` (subclass of `Polygon`) (2 marks)

**Code:**
```java
import java.util.ArrayList;
import java.util.Arrays;

public class Rectangle extends Polygon {
    // Constructor
    public Rectangle() {
        super();  // Call parent constructor
        this.shape = "rectangle";  // Override shape
        // Initialize sideLengths with [1, 1, 1, 1]
        this.sideLengths = new ArrayList<Integer>(Arrays.asList(1, 1, 1, 1));
    }
}
```

**Detailed Explanation:**

**Inheritance:**
- `extends Polygon` - inherits from `Polygon` (which inherits from `Shape`)
- Multi-level inheritance: `Shape` → `Polygon` → `Rectangle`

**Constructor:**
- `super()` calls `Polygon()` constructor
- `this.shape = "rectangle"` overrides to "rectangle"
- `new ArrayList<Integer>(Arrays.asList(1, 1, 1, 1))` creates ArrayList with four 1s
- Alternative: use array and convert:
  ```java
  this.sideLengths = new ArrayList<>();
  this.sideLengths.add(1);
  this.sideLengths.add(1);
  this.sideLengths.add(1);
  this.sideLengths.add(1);
  ```

**Inherited Methods:**
- Automatically has `computePerimeter()` (returns 4)
- Automatically has `getNumberOfEdges()` (returns 4)
- Automatically has `toString()` (returns "I am a rectangle")

---

#### iv) Write class `Triangle` (subclass of `Polygon`) (2 marks)

**Code:**
```java
import java.util.ArrayList;
import java.util.Arrays;

public class Triangle extends Polygon {
    // Constructor
    public Triangle() {
        super();  // Call parent constructor
        this.shape = "triangle";  // Override shape
        // Initialize sideLengths with [2, 2, 2]
        this.sideLengths = new ArrayList<Integer>(Arrays.asList(2, 2, 2));
    }
}
```

**Detailed Explanation:**

**Similar to Rectangle:**
- Inherits from `Polygon`
- Overrides `shape` to "triangle"
- Initializes `sideLengths` with three 2s: `[2, 2, 2]`

**Inherited Behavior:**
- `computePerimeter()` returns 6 (2+2+2)
- `getNumberOfEdges()` returns 3
- `toString()` returns "I am a triangle"

---

#### v) Write corresponding Java statements (4 marks)

**Code:**
```java
// (v-1)
Shape s = new Shape();
System.out.println(s);

// (v-2)
Polygon p = new Polygon();
System.out.println(p);

// (v-3)
Rectangle rect = new Rectangle();
System.out.println(rect);
int perimeter1 = rect.computePerimeter();
// System.out.println(perimeter1);  // Would print: 4

// (v-4)
Triangle tri = new Triangle();
System.out.println(tri);
int perimeter2 = tri.computePerimeter();
// System.out.println(perimeter2);  // Would print: 6
```

**Output:**
```
I am a shape
I am a polygon
I am a rectangle
I am a triangle
```

**Detailed Explanation:**

**Java Syntax Differences:**
- Object creation: `new Shape()` (Java) vs `Shape()` (Python)
- Print: `System.out.println()` (Java) vs `print()` (Python)
- Type declarations: `Shape s` (Java) vs implicit (Python)
- Method calls: `rect.computePerimeter()` (same concept)

**Output Behavior:**
- `System.out.println(s)` automatically calls `toString()` method
- Same behavior as Python's `print()` calling `__str__()`

**Note on computePerimeter():**
- Method returns a value but doesn't print it
- To see the value, use: `System.out.println(rect.computePerimeter());`

---

## QUESTION 3 ([3+3+3+6] * 2 = 30 marks)

### Part c) Java Implementation (15 marks)

#### i) Write class `Member` (Abstract) (3 marks)

**Code:**
```java
public abstract class Member {
    // Attributes
    protected String name;
    protected String address;
    
    // Constructor
    public Member(String name, String address) {
        this.name = name;
        this.address = address;
    }
    
    // Getter methods
    public String getName() {
        return this.name;
    }
    
    public String getAddress() {
        return this.address;
    }
    
    // Abstract method - must be implemented by subclasses
    public abstract int getFee();
}
```

**Detailed Explanation:**

**Abstract Class:**
- `abstract class Member` - cannot be instantiated directly
- Serves as a base class for `StandardMember` and `SeniorMember`
- Can contain both concrete and abstract methods

**Attributes:**
- `protected String name;` - `protected` allows subclasses to access
- `protected String address;` - same as above

**Constructor:**
- `public Member(String name, String address)` - takes name and address
- Initializes instance variables
- Called by subclasses using `super(name, address)`

**Getter Methods:**
- `getName()` and `getAddress()` return values
- Concrete methods (have implementation)

**Abstract Method:**
- `public abstract int getFee();` - no body, ends with semicolon
- **Must** be implemented by all concrete subclasses
- Forces subclasses to define fee calculation

**Why Abstract:**
- `Member` represents a concept that shouldn't be instantiated
- Different member types have different fee structures
- Polymorphism: can treat all members uniformly via `Member` reference

---

#### ii) Write class `StandardMember` (3 marks)

**Code:**
```java
public class StandardMember extends Member {
    // Standard membership fee is fixed at 30
    private static final int STANDARD_FEE = 30;
    
    // Constructor
    public StandardMember(String name, String address) {
        super(name, address);  // Call parent constructor
    }
    
    // Implement abstract method getFee()
    @Override
    public int getFee() {
        return STANDARD_FEE;  // Always returns 30
    }
}
```

**Detailed Explanation:**

**Class Declaration:**
- `extends Member` - inherits from abstract `Member` class
- **Must** implement `getFee()` method (required by abstract parent)

**Constant:**
- `private static final int STANDARD_FEE = 30;` - fixed fee value
- `static`: belongs to class, not instance (shared by all objects)
- `final`: cannot be changed (constant)
- Convention: UPPERCASE for constants

**Constructor:**
- `super(name, address)` calls parent constructor `Member(name, address)`
- Passes parameters to initialize `name` and `address`
- No additional initialization needed

**getFee() Implementation:**
- `@Override` annotation indicates overriding abstract method
- Always returns 30 (the standard membership fee)
- Satisfies the abstract method requirement

**Inherited Methods:**
- Automatically has `getName()` and `getAddress()` from `Member`

---

#### iii) Write class `SeniorMember` (3 marks)

**Code:**
```java
public class SeniorMember extends Member {
    // Attribute: membership fee (set when object is created)
    private int fee;
    
    // Constructor
    public SeniorMember(String name, String address, int fee) {
        super(name, address);  // Call parent constructor
        this.fee = fee;  // Set the fee attribute
    }
    
    // Implement abstract method getFee()
    @Override
    public int getFee() {
        return this.fee;  // Return the fee set in constructor
    }
}
```

**Detailed Explanation:**

**Class Declaration:**
- `extends Member` - inherits from abstract `Member`
- Must implement `getFee()` method

**Attribute:**
- `private int fee;` - instance variable to store fee
- Each `SeniorMember` can have a different fee (unlike `StandardMember`)

**Constructor:**
- `public SeniorMember(String name, String address, int fee)`
- Takes three parameters: name, address, and fee
- `super(name, address)` initializes parent attributes
- `this.fee = fee` sets the fee for this specific senior member

**getFee() Implementation:**
- Returns `this.fee` - the fee set when object was created
- Different from `StandardMember` which always returns 30

**Key Difference:**
- `StandardMember`: fee is fixed (30) for all standard members
- `SeniorMember`: fee is variable, set per member during creation

---

#### iv) Write class `Society` (6 marks)

**Code:**
```java
import java.util.ArrayList;

public class Society {
    // Attributes
    private String name;
    private ArrayList<Member> society;  // List to store Member objects
    
    // Constructor
    public Society(String societyName) {
        this.name = societyName;
        this.society = new ArrayList<Member>();  // Initialize empty list
    }
    
    // Add a StandardMember to the society
    public void addStandardMember(String name, String address) {
        StandardMember sm = new StandardMember(name, address);
        this.society.add(sm);  // Add to ArrayList
    }
    
    // Add a SeniorMember to the society
    public void addSeniorMember(String name, String address, int fee) {
        SeniorMember sm = new SeniorMember(name, address, fee);
        this.society.add(sm);  // Add to ArrayList
    }
    
    // Calculate total fees of all members
    public int getFeeTotal() {
        int total = 0;
        for (int i = 0; i < this.society.size(); i++) {
            Member mb = this.society.get(i);  // Get member at index i
            total += mb.getFee();  // Add member's fee to total (polymorphism!)
        }
        return total;
    }
    
    // Print all members (provided as guide)
    public void printAllMembers() {
        for (int i = 0; i < this.society.size(); i++) {
            Member mb = (Member) this.society.get(i);
            System.out.println("i = " + i + " Name=" + mb.getName() +
                             " Address = " + mb.getAddress() + 
                             " Fees = " + mb.getFee());
        }
    }
}
```

**Detailed Explanation:**

**Class Declaration:**
- Not inheriting from anything (standalone class)
- Manages a collection of `Member` objects

**Attributes:**
- `private String name;` - society name
- `private ArrayList<Member> society;` - list storing `Member` objects
- Note: Uses `Member` type (parent class), can store `StandardMember` and `SeniorMember` due to polymorphism

**Constructor:**
- `public Society(String societyName)` - takes society name
- `this.society = new ArrayList<Member>();` - creates empty ArrayList

**addStandardMember() Method:**
- Takes name and address (fee is fixed at 30 for standard members)
- Creates new `StandardMember` object
- `this.society.add(sm)` adds to ArrayList
- Polymorphism: `StandardMember` is added as `Member` type

**addSeniorMember() Method:**
- Takes name, address, and fee (variable fee)
- Creates new `SeniorMember` object with specified fee
- Adds to ArrayList

**getFeeTotal() Method:**
- Iterates through all members in ArrayList
- Uses traditional for-loop (like `printAllMembers()` example)
- `Member mb = this.society.get(i)` - gets member at index i
- `mb.getFee()` - calls `getFee()` on each member
- **Polymorphism in action:** 
  - If `mb` is `StandardMember`, returns 30
  - If `mb` is `SeniorMember`, returns its specific fee
  - Java determines correct method at runtime (dynamic dispatch)
- Sums all fees and returns total

**Polymorphism Benefits:**
- Can treat all members uniformly
- Don't need to check member type
- Code works for current and future member types

**Usage Example:**
```java
Society club = new Society("Tennis Club");
club.addStandardMember("John", "123 Main St");
club.addSeniorMember("Jane", "456 Oak Ave", 50);
club.addStandardMember("Bob", "789 Pine Rd");
int total = club.getFeeTotal();  // Returns: 30 + 50 + 30 = 110
```

---

### Part d) Python Implementation (15 marks)

#### i) Write class `Member` (Abstract) (3 marks)

**Code:**
```python
from abc import ABC, abstractmethod

class Member(ABC):  # ABC = Abstract Base Class
    # Constructor
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    # Getter methods
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    # Abstract method - must be implemented by subclasses
    @abstractmethod
    def getFee(self):
        pass  # No implementation, must be overridden
```

**Detailed Explanation:**

**Abstract Base Class:**
- `from abc import ABC, abstractmethod` - import abstract base class tools
- `class Member(ABC)` - inherit from `ABC` to make class abstract
- Python doesn't have `abstract` keyword like Java, uses `ABC` module

**Constructor:**
- `def __init__(self, name, address)` - Python constructor
- `self.name = name` - instance variables (no type declarations)

**Getter Methods:**
- `getName()` and `getAddress()` - return instance variables
- Can't directly access `self.name` from outside (encapsulation convention)

**Abstract Method:**
- `@abstractmethod` decorator marks method as abstract
- `def getFee(self): pass` - no implementation
- Subclasses **must** implement this method
- Trying to instantiate `Member` directly raises `TypeError`

**Alternative (without ABC - less strict):**
```python
class Member:
    def getFee(self):
        raise NotImplementedError("Subclass must implement getFee()")
```

---

#### ii) Write class `StandardMember` (3 marks)

**Code:**
```python
class StandardMember(Member):
    # Class constant for standard fee
    STANDARD_FEE = 30
    
    # Constructor
    def __init__(self, name, address):
        super().__init__(name, address)  # Call parent constructor
    
    # Implement abstract method
    def getFee(self):
        return StandardMember.STANDARD_FEE  # Always returns 30
```

**Detailed Explanation:**

**Inheritance:**
- `class StandardMember(Member)` - inherits from `Member`
- Must implement `getFee()` (required by abstract parent)

**Class Constant:**
- `STANDARD_FEE = 30` - class variable (shared by all instances)
- Convention: UPPERCASE for constants
- Access: `StandardMember.STANDARD_FEE` or `self.STANDARD_FEE`

**Constructor:**
- `super().__init__(name, address)` - calls parent constructor
- Python 3 syntax (Python 2 would use `Member.__init__(self, name, address)`)

**getFee() Implementation:**
- Returns `STANDARD_FEE` (always 30)
- Satisfies abstract method requirement

---

#### iii) Write class `SeniorMember` (3 marks)

**Code:**
```python
class SeniorMember(Member):
    # Constructor
    def __init__(self, name, address, fee):
        super().__init__(name, address)  # Call parent constructor
        self.fee = fee  # Set fee attribute (variable per member)
    
    # Implement abstract method
    def getFee(self):
        return self.fee  # Return the fee set in constructor
```

**Detailed Explanation:**

**Similar to Java Version:**
- Inherits from `Member`
- Takes `fee` parameter in constructor
- Stores fee as instance variable: `self.fee`
- `getFee()` returns `self.fee` (can vary per member)

**Key Points:**
- Fee is instance variable (not class constant)
- Each `SeniorMember` can have different fee
- Must implement `getFee()` to satisfy abstract method

---

#### iv) Write class `Society` (6 marks)

**Code:**
```python
class Society:
    # Constructor
    def __init__(self, societyName):
        self.name = societyName
        self.society = []  # Python list (equivalent to Java ArrayList)
    
    # Add a StandardMember to the society
    def addStandardMember(self, name, address):
        sm = StandardMember(name, address)
        self.society.append(sm)  # Add to list (equivalent to ArrayList.add())
    
    # Add a SeniorMember to the society
    def addSeniorMember(self, name, address, fee):
        sm = SeniorMember(name, address, fee)
        self.society.append(sm)  # Add to list
    
    # Calculate total fees of all members
    def getFeeTotal(self):
        total = 0
        for i in range(len(self.society)):  # Iterate through list
            mb = self.society[i]  # Get member at index i
            total += mb.getFee()  # Add member's fee (polymorphism!)
        return total
    
    # Print all members (equivalent to Java version)
    def printAllMembers(self):
        for i in range(len(self.society)):
            mb = self.society[i]
            print(f"i = {i} Name={mb.getName()} "
                  f"Address = {mb.getAddress()} Fees = {mb.getFee()}")
```

**Detailed Explanation:**

**Constructor:**
- `self.society = []` - creates empty Python list
- Equivalent to Java's `new ArrayList<Member>()`

**addStandardMember() Method:**
- Creates `StandardMember` object
- `self.society.append(sm)` - adds to list (equivalent to `ArrayList.add()`)

**addSeniorMember() Method:**
- Creates `SeniorMember` object with specified fee
- Adds to list

**getFeeTotal() Method:**
- Uses `for i in range(len(self.society))` - traditional indexing loop
- `mb = self.society[i]` - gets member at index i
- `mb.getFee()` - calls `getFee()` on each member
- **Polymorphism:** Python determines correct method based on object type
- Sums all fees and returns total

**Python-Style Alternative (more Pythonic):**
```python
def getFeeTotal(self):
    total = 0
    for member in self.society:  # Direct iteration (more Pythonic)
        total += member.getFee()
    return total

# Or even more Pythonic:
def getFeeTotal(self):
    return sum(member.getFee() for member in self.society)
```

**printAllMembers() Method:**
- Similar structure to `getFeeTotal()`
- Uses f-string formatting (Python 3.6+)
- Equivalent functionality to Java version

**Usage Example:**
```python
club = Society("Tennis Club")
club.addStandardMember("John", "123 Main St")
club.addSeniorMember("Jane", "456 Oak Ave", 50)
club.addStandardMember("Bob", "789 Pine Rd")
total = club.getFeeTotal()  # Returns: 30 + 50 + 30 = 110
club.printAllMembers()
```

**Output:**
```
i = 0 Name=John Address = 123 Main St Fees = 30
i = 1 Name=Jane Address = 456 Oak Ave Fees = 50
i = 2 Name=Bob Address = 789 Pine Rd Fees = 30
```

---

## KEY CONCEPTS DEMONSTRATED

### Question 1:
- **OOP Concepts:** Abstraction, Encapsulation, Composition, Inheritance, Polymorphism
- **Python Basics:** String slicing, dictionary behavior, view objects

### Question 2:
- **Inheritance:** Single and multi-level inheritance
- **Method Overriding:** `__str__()` in Python, `toString()` in Java
- **Constructor Chaining:** `super()` calls
- **Polymorphism:** Same interface, different implementations

### Question 3:
- **Abstract Classes:** Defining base classes that cannot be instantiated
- **Abstract Methods:** Forcing subclasses to implement specific methods
- **Polymorphism:** Treating different object types uniformly through parent class references
- **Collections:** Using `ArrayList` (Java) and `List` (Python) to manage objects
- **Dynamic Method Dispatch:** Runtime determination of which method to call

---

## COMPARISON: Java vs Python

| Feature | Java | Python |
|---------|------|--------|
| Abstract Class | `abstract class` | `from abc import ABC` |
| Abstract Method | `abstract methodName();` | `@abstractmethod` decorator |
| Inheritance | `extends` | `class Child(Parent)` |
| Constructor Call | `super()` | `super().__init__()` |
| List/Array | `ArrayList<Type>` | `list` or `[]` |
| Type Declaration | Required | Optional (duck typing) |
| Access Modifiers | `private`, `protected`, `public` | Convention-based (`_` prefix) |
| String Formatting | `+` or `String.format()` | f-strings or `.format()` |

---

## PRACTICAL TIPS FOR EXAM

1. **Abstract Classes:** Remember that abstract classes cannot be instantiated
2. **Polymorphism:** When you have a parent class reference, method calls use the actual object's type
3. **Inheritance Chain:** `super()` always calls the immediate parent
4. **Method Overriding:** Use `@Override` in Java, `@abstractmethod` in Python
5. **Collections:** Java uses typed collections (`ArrayList<Member>`), Python uses generic lists
6. **String Representation:** Java uses `toString()`, Python uses `__str__()`

---

*End of Exam Answers*
