# IST603 Advanced OOP Test 1 - January 2026
## University of Buea - Department of Computer Science
**Academic Year: 2025/2026**  
**Instructors: Dr. Nkweteyim D. / Dr. Achankeng P.**

---

## Exam Overview

This document contains complete solutions to the IST603 Advanced OOP Test 1, covering Object-Oriented Design (UML class diagrams), Python language basics, and Java programming (abstract classes, interfaces, inheritance, and polymorphism).

**Total Marks: 30**  
**Pages: 2**

---

## Section A

---

## Question 1: Object-Oriented Design (5 marks)

### a) Name each of the relationship types of a class diagram depicted on the right. (3 marks)

**Answer:**

Based on the Pizza Shop UML class diagram, the relationship types are:

1. **Generalization (Inheritance)**
   - `Pickup` → `Order` (Pickup is a subclass of Order)
   - `Delivery` → `Order` (Delivery is a subclass of Order)
   - `Pizza` → `Item` (Pizza is a subclass of Item)
   - `Drink` → `Item` (Drink is a subclass of Item)

2. **Association**
   - `Customer` ↔ `Order` (Customer places Order)
   - `Order` ↔ `Item` (Order contains Items)

**Explanation:**

**Generalization (Inheritance):**
- Represented by a solid line with a hollow arrowhead pointing from the subclass to the superclass
- Indicates an "is-a" relationship
- `Pickup` and `Delivery` are types of `Order` (specialization)
- `Pizza` and `Drink` are types of `Item` (specialization)
- Subclasses inherit attributes and methods from their parent classes

**Association:**
- Represented by a solid line connecting two classes
- Indicates a "has-a" or "uses" relationship
- `Customer` places `Order` - a customer can have multiple orders
- `Order` contains `Item` - an order can contain multiple items

---

### b) Answer the following questions based on the UML class diagram: (2 marks)

#### i) List the members of class `Order`; in each case, state the type of the member. (0.5 marks)

**Answer:**

**Members of class `Order`:**

1. **Attributes:**
   - `-String orderID` (private attribute, type: String)
   - `-Date timestamp` (private attribute, type: Date)

2. **Note:** Since `Order` is an abstract class, it may have abstract methods, but only attributes are shown in the diagram.

**Member Types:**
- **Attributes:** Instance variables that store data
- **Methods:** Functions that define behavior (not shown in diagram but implied by abstract class)

**Visibility:**
- The `-` sign indicates **private** visibility (encapsulation)

---

#### ii) State the meanings of the `-` and `+` signs against class members. (0.5 marks)

**Answer:**

**Visibility Modifiers in UML:**

- **`-` (Minus sign):** Indicates **private** visibility
  - The member is accessible only within the class itself
  - Not accessible to subclasses or other classes
  - Provides encapsulation and data hiding
  - Example: `-String orderID` can only be accessed within the `Order` class

- **`+` (Plus sign):** Indicates **public** visibility
  - The member is accessible from anywhere (within the class, subclasses, and other classes)
  - Provides open access to the member
  - Example: `+processPayment()` can be called from any class

**Other UML Visibility Modifiers:**
- **`#` (Hash/Pound sign):** Indicates **protected** visibility (accessible within the class and its subclasses)
- **`~` (Tilde):** Indicates **package** visibility (accessible within the same package)

**Purpose:**
- Visibility modifiers control access to class members
- They enforce encapsulation, one of the core principles of OOP
- They help maintain data integrity and prevent unauthorized access

---

#### iii) Redraw the `Customer` and `Order` classes to include the following modification to include an association to indicate that one customer can place zero, one, or many orders. (0.5 marks)

**Answer:**

**Modified UML Class Diagram:**

```
┌──────────────┐
│   Customer   │
├──────────────┤
│ -customerID  │
│ -name        │
└──────────────┘
       │
       │ placesOrder
       │ 0..*
       │
       ▼
┌──────────────┐
│    Order      │
├──────────────┤
│ -orderID      │
│ -timestamp    │
└──────────────┘
```

**Multiplicity Notation:**
- **`0..*`** on the `Order` side means:
  - **0** = A customer can have zero orders (optional)
  - **`*`** = A customer can have many orders (unlimited)
  - This represents a **one-to-many** relationship

**Relationship:**
- One `Customer` can place **zero, one, or many** `Order` objects
- Each `Order` belongs to exactly one `Customer`
- The association is named `placesOrder` (or `places`)

**Alternative Notation:**
- `0..*` can also be written as `*` (zero or more)
- `1..*` would mean "one or many" (at least one required)

---

#### iv) Redraw the `Order` and `Item` classes to include the following modification to include an association to indicate that `Items` are part of a specific `Order`; if the order is deleted, the line items for that specific order are also deleted. (0.5 marks)

**Answer:**

**Modified UML Class Diagram:**

```
┌──────────────┐
│    Order      │
├──────────────┤
│ -orderID      │
│ -timestamp    │
└──────────────┘
       │
       │ contains
       │ 1..*
       │
       │ (filled diamond)
       ▼
┌──────────────┐
│     Item      │
├──────────────┤
│ -itemID       │
│ -price        │
└──────────────┘
```

**Composition Relationship:**
- The **filled diamond** (solid diamond) on the `Order` side indicates **composition**
- This is a strong "has-a" relationship where:
  - `Item` objects are **part of** an `Order`
  - `Item` objects **cannot exist independently** of an `Order`
  - If the `Order` is deleted, all its `Item` objects are **automatically deleted** (cascade delete)

**Multiplicity:**
- **`1..*`** on the `Item` side means:
  - An `Order` must contain **at least one** `Item` (mandatory)
  - An `Order` can contain **many** `Item` objects

**Key Characteristics of Composition:**
- **Ownership:** Order owns the Items
- **Lifecycle dependency:** Items are created and destroyed with the Order
- **Exclusivity:** An Item belongs to only one Order
- **Strong relationship:** More restrictive than aggregation

**Difference from Aggregation:**
- **Aggregation** (hollow diamond): Items can exist independently, weaker relationship
- **Composition** (filled diamond): Items cannot exist independently, stronger relationship

---

## Question 2: Python Language Basics (10 marks)

Given:
- `words = ['red', 'blue', 'tree', 'cup', 'dish']`
- `phrase = '6 cars 9 boats for rent'`
- `a = 'sandwich'` (already given: Type: string, Value: 'sandwich')

List in the table the type of variable and its value after being assigned the expression.

---

### b) `b = a[4] + a[-2]`

**Answer:**

**Type:** string  
**Value:** `'wh'`

**Explanation:**
- `a = 'sandwich'`
- String indices for `'sandwich'`:
  - Forward: 0='s', 1='a', 2='n', 3='d', 4='w', 5='i', 6='c', 7='h'
  - Backward: -1='h', -2='c', -3='i', -4='w', -5='d', -6='n', -7='a', -8='s'
- `a[4]` = character at index 4 = `'w'`
- `a[-2]` = character at index -2 (second from the end) = `'c'`
- `b = 'w' + 'c'` = `'wc'` (string concatenation)

---

### c) `c = words[-2] + words[1]`

**Answer:**

**Type:** string  
**Value:** `'cupblue'`

**Explanation:**
- `words = ['red', 'blue', 'tree', 'cup', 'dish']`
- Indices: 0='red', 1='blue', 2='tree', 3='cup', 4='dish'
- Backward indices: -1='dish', -2='cup', -3='tree', -4='blue', -5='red'
- `words[-2]` = `'cup'`
- `words[1]` = `'blue'`
- `c = 'cup' + 'blue'` = `'cupblue'` (string concatenation)

---

### d) `d = phrase[3] + phrase[-3]`

**Answer:**

**Type:** string  
**Value:** `'ar'`

**Explanation:**
- `phrase = '6 cars 9 boats for rent'`
- String indices:
  - Forward: 0='6', 1=' ', 2='c', 3='a', 4='r', 5='s', 6=' ', 7='9', 8=' ', 9='b', 10='o', 11='a', 12='t', 13='s', 14=' ', 15='f', 16='o', 17='r', 18=' ', 19='r', 20='e', 21='n', 22='t'
  - Backward: -1='t', -2='n', -3='e', -4='r', -5=' ', -6='r', -7='o', -8='f', ...
- `phrase[3]` = character at index 3 = `'a'`
- `phrase[-3]` = character at index -3 (third from the end) = `'e'`
- `d = 'a' + 'e'` = `'ae'` (string concatenation)

---

### e) `e = len(words)`

**Answer:**

**Type:** int  
**Value:** `5`

**Explanation:**
- `words = ['red', 'blue', 'tree', 'cup', 'dish']`
- `len(words)` returns the number of elements in the list
- The list contains 5 elements
- `e = 5`

---

### f) `f = len(a)`

**Answer:**

**Type:** int  
**Value:** `8`

**Explanation:**
- `a = 'sandwich'`
- `len(a)` returns the number of characters in the string
- `'sandwich'` has 8 characters: s-a-n-d-w-i-c-h
- `f = 8`

---

### g) `g = len(a) <= len('house')`

**Answer:**

**Type:** bool  
**Value:** `False`

**Explanation:**
- `a = 'sandwich'`
- `len(a)` = 8
- `len('house')` = 5
- `8 <= 5` evaluates to `False`
- `g = False`

---

### h) `h = a[1:4]`

**Answer:**

**Type:** string  
**Value:** `'and'`

**Explanation:**
- `a = 'sandwich'`
- `a[1:4]` is a slice from index 1 (inclusive) to index 4 (exclusive)
- Indices: 0='s', 1='a', 2='n', 3='d', 4='w'
- Slice `a[1:4]` includes indices 1, 2, 3 = `'and'`
- `h = 'and'`

---

### i) `i = 'be'.join(['top', 'cat', 'go'])`

**Answer:**

**Type:** string  
**Value:** `'topbecatbego'`

**Explanation:**
- `'be'.join(['top', 'cat', 'go'])` joins the list elements with `'be'` as the separator
- The `join()` method inserts the separator string between each element
- Result: `'top' + 'be' + 'cat' + 'be' + 'go'` = `'topbecatbego'`
- `i = 'topbecatbego'`

---

### j) `j = 12 // 5 + 3.4`

**Answer:**

**Type:** float  
**Value:** `5.4`

**Explanation:**
- `12 // 5` = integer division (floor division) = `2`
- `2 + 3.4` = `5.4` (when adding int and float, result is float)
- `j = 5.4`

**Note:** `//` is the floor division operator in Python, which returns the integer part of the division.

---

### k) `k = (8 % 5) + 5 / 4`

**Answer:**

**Type:** float  
**Value:** `4.25`

**Explanation:**
- `8 % 5` = modulo operation (remainder) = `3` (8 divided by 5 is 1 with remainder 3)
- `5 / 4` = division = `1.25` (regular division returns float)
- `3 + 1.25` = `4.25`
- `k = 4.25`

**Note:** `%` is the modulo operator, `+` has same precedence, evaluated left to right.

---

## Section B: Java Programming Language

**Instructions:** All questions in this section are related to the Java Programming Language. (Answer on a separate sheet from Section A).

---

## Exercise I: University E-Payment Management System (11 marks)

Develop a Java-based E-Payment Management System for a university. The system should handle various payment types (tuition, health fee, hostel fees) and multiple payment methods (mobile money, bank transfer). Break down your Java code according to the sub-questions below. Use print statements for any method functionality not explicitly given.

---

### a) Create an `abstract class` named `Payment`. (4 marks)

**Requirements:**
- It must have two `protected` attributes: `matricule` (likely a student ID) and `amount`.
- Implement a constructor to initialize these attributes.
- Include an `abstract method` called `processPayment()`.
- Include a `concrete method` called `printReceipt()` that will display the `matricule` and the `amount` paid.
- The class should be properly documented so that developer documentation can be easily generated (implying Javadoc comments).

**Answer:**

```java
/**
 * Abstract class representing a payment in the University E-Payment Management System.
 * This class serves as the base class for different types of payments (tuition, health fee, hostel fees).
 * 
 * @author Your Name
 * @version 1.0
 */
public abstract class Payment {
    
    /**
     * The student's matriculation number (student ID).
     */
    protected String matricule;
    
    /**
     * The amount to be paid.
     */
    protected double amount;
    
    /**
     * Constructor to initialize a Payment object.
     * 
     * @param matricule The student's matriculation number
     * @param amount The payment amount
     */
    public Payment(String matricule, double amount) {
        this.matricule = matricule;
        this.amount = amount;
    }
    
    /**
     * Abstract method to process the payment.
     * Must be implemented by subclasses to define specific payment processing logic.
     */
    public abstract void processPayment();
    
    /**
     * Concrete method to print the payment receipt.
     * Displays the matricule and the amount paid.
     */
    public void printReceipt() {
        System.out.println("=== PAYMENT RECEIPT ===");
        System.out.println("Matricule: " + matricule);
        System.out.println("Amount Paid: " + amount);
        System.out.println("======================");
    }
    
    /**
     * Getter method for matricule.
     * 
     * @return The student's matriculation number
     */
    public String getMatricule() {
        return matricule;
    }
    
    /**
     * Getter method for amount.
     * 
     * @return The payment amount
     */
    public double getAmount() {
        return amount;
    }
}
```

**Key Points:**
- **Abstract class:** Cannot be instantiated directly
- **Protected attributes:** Accessible to subclasses and same package
- **Abstract method:** Must be implemented by subclasses
- **Concrete method:** Has implementation, can be inherited
- **Javadoc comments:** `/** */` format for documentation generation

---

### b) Create two subclasses that extend the `Payment` class: `TuitionPayment` and `HostelPayment`. (2 marks)

**Requirements:**
- Each of these subclasses must define (implement) the `processPayment()` method.
- This method should simply display a message indicating the specific type of payment being processed.

**Answer:**

```java
/**
 * Class representing a tuition payment.
 * Extends the Payment abstract class.
 */
public class TuitionPayment extends Payment {
    
    /**
     * Constructor to initialize a TuitionPayment object.
     * 
     * @param matricule The student's matriculation number
     * @param amount The tuition payment amount
     */
    public TuitionPayment(String matricule, double amount) {
        super(matricule, amount);
    }
    
    /**
     * Implements the abstract processPayment() method.
     * Displays a message indicating that tuition payment is being processed.
     */
    @Override
    public void processPayment() {
        System.out.println("Processing tuition payment for matricule: " + matricule);
        System.out.println("Amount: " + amount);
    }
}
```

```java
/**
 * Class representing a hostel payment.
 * Extends the Payment abstract class.
 */
public class HostelPayment extends Payment {
    
    /**
     * Constructor to initialize a HostelPayment object.
     * 
     * @param matricule The student's matriculation number
     * @param amount The hostel payment amount
     */
    public HostelPayment(String matricule, double amount) {
        super(matricule, amount);
    }
    
    /**
     * Implements the abstract processPayment() method.
     * Displays a message indicating that hostel payment is being processed.
     */
    @Override
    public void processPayment() {
        System.out.println("Processing hostel payment for matricule: " + matricule);
        System.out.println("Amount: " + amount);
    }
}
```

**Key Points:**
- **Inheritance:** `extends Payment` keyword
- **Constructor:** Calls `super()` to initialize parent class attributes
- **Method Override:** `@Override` annotation (optional but recommended)
- **Implementation:** Each subclass provides its own implementation of `processPayment()`

---

### c) Create an `interface` named `PaymentMethod`. (2 marks)

**Requirements:**
- This interface should declare a method `pay(double amount)`.
- Implement this interface in two separate classes: `MobileMoneyPayment` and `BankTransferPayment`.
- Each of these implementation classes must provide its own implementation for the `pay()` method.

**Answer:**

```java
/**
 * Interface defining the contract for payment methods.
 * Any class implementing this interface must provide a pay() method.
 */
public interface PaymentMethod {
    
    /**
     * Processes a payment for the given amount.
     * 
     * @param amount The amount to be paid
     */
    void pay(double amount);
}
```

```java
/**
 * Class implementing mobile money payment method.
 */
public class MobileMoneyPayment implements PaymentMethod {
    
    private String phoneNumber;
    
    /**
     * Constructor to initialize MobileMoneyPayment.
     * 
     * @param phoneNumber The mobile money phone number
     */
    public MobileMoneyPayment(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    
    /**
     * Implements the pay() method from PaymentMethod interface.
     * Processes payment via mobile money.
     * 
     * @param amount The amount to be paid
     */
    @Override
    public void pay(double amount) {
        System.out.println("Processing mobile money payment...");
        System.out.println("Phone Number: " + phoneNumber);
        System.out.println("Amount: " + amount);
        System.out.println("Payment successful via mobile money!");
    }
}
```

```java
/**
 * Class implementing bank transfer payment method.
 */
public class BankTransferPayment implements PaymentMethod {
    
    private String accountNumber;
    private String bankName;
    
    /**
     * Constructor to initialize BankTransferPayment.
     * 
     * @param accountNumber The bank account number
     * @param bankName The name of the bank
     */
    public BankTransferPayment(String accountNumber, String bankName) {
        this.accountNumber = accountNumber;
        this.bankName = bankName;
    }
    
    /**
     * Implements the pay() method from PaymentMethod interface.
     * Processes payment via bank transfer.
     * 
     * @param amount The amount to be paid
     */
    @Override
    public void pay(double amount) {
        System.out.println("Processing bank transfer payment...");
        System.out.println("Bank: " + bankName);
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Amount: " + amount);
        System.out.println("Payment successful via bank transfer!");
    }
}
```

**Key Points:**
- **Interface:** Uses `interface` keyword, methods are implicitly abstract
- **Implementation:** Uses `implements` keyword
- **Contract:** All implementing classes must provide `pay()` method
- **Polymorphism:** Can use `PaymentMethod` reference to call `pay()` on any implementation

---

### d) Create a `Main` class to demonstrate the system's functionality. (3 marks)

**Requirements:**
- Create at least one object of each defined payment type (e.g., an instance of `TuitionPayment` and `HostelPayment`).
- Process payments using different payment methods (e.g., call `pay()` on `MobileMoneyPayment` and `BankTransferPayment` instances).
- Demonstrate polymorphism by using `Payment` and `PaymentMethod` references.

**Answer:**

```java
/**
 * Main class to demonstrate the University E-Payment Management System.
 */
public class Main {
    
    public static void main(String[] args) {
        
        System.out.println("=== UNIVERSITY E-PAYMENT MANAGEMENT SYSTEM ===\n");
        
        // Create payment objects (polymorphism with Payment reference)
        Payment tuitionPayment = new TuitionPayment("ST2024001", 50000.0);
        Payment hostelPayment = new HostelPayment("ST2024002", 30000.0);
        
        // Create payment method objects (polymorphism with PaymentMethod reference)
        PaymentMethod mobileMoney = new MobileMoneyPayment("+237681234567");
        PaymentMethod bankTransfer = new BankTransferPayment("1234567890", "Afriland First Bank");
        
        // Demonstrate payment processing
        System.out.println("--- Processing Tuition Payment ---");
        tuitionPayment.processPayment();
        tuitionPayment.printReceipt();
        
        System.out.println("\n--- Processing Hostel Payment ---");
        hostelPayment.processPayment();
        hostelPayment.printReceipt();
        
        // Demonstrate payment methods
        System.out.println("\n--- Using Mobile Money Payment Method ---");
        mobileMoney.pay(50000.0);
        
        System.out.println("\n--- Using Bank Transfer Payment Method ---");
        bankTransfer.pay(30000.0);
        
        // Demonstrate polymorphism: Using Payment reference
        System.out.println("\n--- Polymorphism Example: Payment Reference ---");
        Payment[] payments = {
            new TuitionPayment("ST2024003", 45000.0),
            new HostelPayment("ST2024004", 25000.0)
        };
        
        for (Payment payment : payments) {
            payment.processPayment();
            payment.printReceipt();
            System.out.println();
        }
        
        // Demonstrate polymorphism: Using PaymentMethod reference
        System.out.println("--- Polymorphism Example: PaymentMethod Reference ---");
        PaymentMethod[] methods = {
            new MobileMoneyPayment("+237699876543"),
            new BankTransferPayment("9876543210", "UBA Bank")
        };
        
        for (PaymentMethod method : methods) {
            method.pay(10000.0);
            System.out.println();
        }
    }
}
```

**Expected Output:**

```
=== UNIVERSITY E-PAYMENT MANAGEMENT SYSTEM ===

--- Processing Tuition Payment ---
Processing tuition payment for matricule: ST2024001
Amount: 50000.0
=== PAYMENT RECEIPT ===
Matricule: ST2024001
Amount Paid: 50000.0
======================

--- Processing Hostel Payment ---
Processing hostel payment for matricule: ST2024002
Amount: 30000.0
=== PAYMENT RECEIPT ===
Matricule: ST2024002
Amount Paid: 30000.0
======================

--- Using Mobile Money Payment Method ---
Processing mobile money payment...
Phone Number: +237681234567
Amount: 50000.0
Payment successful via mobile money!

--- Using Bank Transfer Payment Method ---
Processing bank transfer payment...
Bank: Afriland First Bank
Account Number: 1234567890
Amount: 30000.0
Payment successful via bank transfer!

--- Polymorphism Example: Payment Reference ---
Processing tuition payment for matricule: ST2024003
Amount: 45000.0
=== PAYMENT RECEIPT ===
Matricule: ST2024003
Amount Paid: 45000.0
======================

Processing hostel payment for matricule: ST2024004
Amount: 25000.0
=== PAYMENT RECEIPT ===
Matricule: ST2024004
Amount Paid: 25000.0
======================

--- Polymorphism Example: PaymentMethod Reference ---
Processing mobile money payment...
Phone Number: +237699876543
Amount: 10000.0
Payment successful via mobile money!

Processing bank transfer payment...
Bank: UBA Bank
Account Number: 9876543210
Amount: 10000.0
Payment successful via bank transfer!
```

**Key Points Demonstrated:**
- **Object Creation:** Instances of `TuitionPayment`, `HostelPayment`, `MobileMoneyPayment`, `BankTransferPayment`
- **Polymorphism:** Using `Payment` and `PaymentMethod` references
- **Method Calls:** Calling `processPayment()`, `printReceipt()`, and `pay()`
- **Runtime Polymorphism:** Different implementations called based on actual object type

---

## Exercise II: Theoretical Questions (4 marks)

### a) What terminal/CLI command will you write to generate the documentation from this program? (1 mark)

**Answer:**

```bash
javadoc -d docs Payment.java TuitionPayment.java HostelPayment.java PaymentMethod.java MobileMoneyPayment.java BankTransferPayment.java Main.java
```

**Explanation:**
- **`javadoc`** is the Java documentation generator tool
- **`-d docs`** specifies the output directory (creates a `docs` folder)
- List all `.java` files to be documented
- Alternatively, you can use: `javadoc -d docs *.java` (if all Java files are in the same directory)

**Additional Options:**
- `-author` - Include @author tags
- `-version` - Include @version tags
- `-private` - Include private members
- `-html` - Generate HTML documentation (default)

**Example with options:**
```bash
javadoc -d docs -author -version *.java
```

---

### b) What is the use of packages in Java? (1 mark)

**Answer:**

**Packages in Java serve several important purposes:**

1. **Organization:** Packages organize related classes and interfaces into logical groups, making code easier to manage and navigate.

2. **Namespace Management:** Packages prevent naming conflicts by providing a unique namespace. Classes with the same name can exist in different packages.

3. **Access Control:** Packages provide package-level access control. Classes in the same package can access package-private members.

4. **Modularity:** Packages help create modular, reusable code structures that can be easily imported and used in other projects.

5. **Logical Grouping:** Related functionality is grouped together (e.g., `java.util` for utility classes, `java.io` for input/output).

6. **Code Reusability:** Packages allow code to be organized into libraries that can be easily shared and reused.

**Example:**
```java
package com.university.payment;

public class Payment {
    // Class implementation
}
```

**Import Statement:**
```java
import com.university.payment.Payment;
```

---

### c) What is the difference between a package private member, and a protected member? (1 mark)

**Answer:**

**Package Private Member:**
- **Visibility:** Accessible only within the **same package**
- **Keyword:** No access modifier (default visibility)
- **Access:** Can be accessed by classes in the same package only
- **Inheritance:** NOT accessible to subclasses in different packages

**Protected Member:**
- **Visibility:** Accessible within the **same package** AND to **subclasses** (even in different packages)
- **Keyword:** `protected`
- **Access:** Can be accessed by:
  - Classes in the same package
  - Subclasses (even if in different packages)
- **Inheritance:** Accessible to subclasses regardless of package

**Key Difference:**
- **Package private:** Same package only
- **Protected:** Same package + subclasses (any package)

**Example:**

```java
// Package: com.university.payment
public class Payment {
    String packagePrivateMember;  // Package private
    protected String protectedMember;  // Protected
}

// Same package
class PaymentProcessor {
    void method() {
        Payment p = new Payment();
        p.packagePrivateMember = "OK";  // ✓ Accessible
        p.protectedMember = "OK";       // ✓ Accessible
    }
}

// Different package
package com.university.student;
import com.university.payment.Payment;

class StudentPayment extends Payment {
    void method() {
        // packagePrivateMember = "ERROR";  // ✗ NOT accessible
        protectedMember = "OK";              // ✓ Accessible (subclass)
    }
}
```

---

### d) What is the advantage of a static method over a non-static method in Java? (1 mark)

**Answer:**

**Advantages of Static Methods:**

1. **No Object Instantiation Required:**
   - Static methods can be called directly using the class name without creating an object
   - Example: `Math.sqrt(25)` instead of `new Math().sqrt(25)`
   - More efficient and convenient for utility methods

2. **Memory Efficiency:**
   - Static methods belong to the class, not instances
   - Only one copy exists in memory regardless of how many objects are created
   - Reduces memory overhead

3. **Class-Level Functionality:**
   - Appropriate for operations that don't depend on instance data
   - Useful for utility methods, helper functions, and factory methods

4. **Can Access Static Members:**
   - Static methods can directly access other static members (variables and methods)
   - Useful for maintaining class-level state

**Example:**

```java
public class MathUtils {
    // Static method - can be called without object
    public static int add(int a, int b) {
        return a + b;
    }
    
    // Non-static method - requires object
    public int multiply(int a, int b) {
        return a * b;
    }
}

// Usage:
int sum = MathUtils.add(5, 3);  // ✓ No object needed

MathUtils utils = new MathUtils();
int product = utils.multiply(5, 3);  // Requires object
```

**When to Use Static Methods:**
- Utility functions (e.g., `Math.max()`, `Collections.sort()`)
- Factory methods
- Methods that don't need instance state
- Helper methods that operate on parameters only

**Limitations:**
- Cannot access non-static (instance) members directly
- Cannot use `this` or `super` keywords
- Cannot be overridden (but can be hidden)

---

## Summary

### Key Concepts Covered:

1. **UML Class Diagrams:**
   - Generalization (inheritance)
   - Association relationships
   - Composition relationships
   - Multiplicity notation
   - Visibility modifiers (-, +, #, ~)

2. **Python Basics:**
   - String indexing and slicing
   - List operations
   - String concatenation
   - `len()` function
   - `join()` method
   - Arithmetic operations (//, %, /)

3. **Java OOP Concepts:**
   - Abstract classes
   - Inheritance (`extends`)
   - Interfaces (`implements`)
   - Polymorphism
   - Method overriding
   - Access modifiers (protected, package-private)
   - Static methods
   - Javadoc documentation

4. **Design Patterns:**
   - Abstract class pattern
   - Interface pattern
   - Polymorphism demonstration

---

## Additional Notes

### Best Practices:

1. **UML Diagrams:**
   - Use appropriate relationship types
   - Specify multiplicities clearly
   - Use correct visibility modifiers

2. **Python Programming:**
   - Understand string indexing (positive and negative)
   - Know the difference between `//` (floor division) and `/` (regular division)
   - Remember that `join()` inserts the separator between elements

3. **Java Programming:**
   - Always document classes and methods with Javadoc
   - Use `@Override` annotation for clarity
   - Follow naming conventions
   - Understand when to use abstract classes vs interfaces

### Common Mistakes to Avoid:

1. Confusing composition (filled diamond) with aggregation (hollow diamond)
2. Incorrect string indexing (off-by-one errors)
3. Forgetting to call `super()` in subclass constructors
4. Not implementing all abstract methods in subclasses
5. Confusing package-private with protected visibility

---

**End of Solutions**

**Course:** IST603 - Advanced Object-Oriented Programming  
**Institution:** University of Buea, Department of Computer Science  
**Test Date:** January 23, 2026  
**Total Marks: 30**
