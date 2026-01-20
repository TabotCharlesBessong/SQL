# Question 1: Assorted Java Code
## IST603 - Object-Oriented Programming with Java and Python
**Total Marks: 2 + 3 + 1.5 + 1.5 = 8 marks**

---

## Part a) Exception Handling Analysis

### Given Code (Figure a):

```java
public static void m(int x) {
    try {
        m2(x);
        System.out.println(1);
    } catch (ArithmeticException e) {
        System.out.println(2);
    } catch (Exception e) {
        // empty catch block
    }
    System.out.println(3);
}

public static void m2(int x) throws IOException {
    System.out.println(4);
    if (x == 1) {
        throw new IOException();
    }
    if (x == 0) {
        throw new ArithmeticException();
    }
    System.out.println(5);
}
```

### i) Output for m(1):

**Step-by-step execution:**
1. `m(1)` is called
2. `try` block executes: calls `m2(1)`
3. `m2(1)` executes:
   - Prints `4`
   - `x == 1` is true, so throws `new IOException()`
   - Execution stops in `m2`
4. `IOException` is thrown but not caught by `ArithmeticException` catch block
5. `IOException` is caught by the general `catch (Exception e)` block (empty, does nothing)
6. After try-catch, prints `3`

**Output:**
```
4
3
```

### ii) Output for m(0):

**Step-by-step execution:**
1. `m(0)` is called
2. `try` block executes: calls `m2(0)`
3. `m2(0)` executes:
   - Prints `4`
   - `x == 0` is true, so throws `new ArithmeticException()`
   - Execution stops in `m2`
4. `ArithmeticException` is caught by `catch (ArithmeticException e)` block
5. Prints `2`
6. After try-catch, prints `3`

**Output:**
```
4
2
3
```

---

## Part b) Inheritance and Method Overriding Analysis

### Given Code (Figure b):

```java
class A {
    private int x;
    
    public A(int x) {
        this.x = x;
    }
    
    public void m() {
        System.out.println(x - 1);
    }
}

class B extends A {
    private int y;
    
    public B(int y) {
        super(y - 1);
        this.y = y;
    }
    
    public void m() {
        System.out.println(y + 1);
    }
}
```

### i) Output for (new A(3)).m():

**Step-by-step execution:**
1. `new A(3)` creates an instance of class A
   - Constructor `A(3)` sets `this.x = 3`
2. `.m()` is called on the A instance
3. A's `m()` method executes: `System.out.println(x - 1)`
   - `x = 3`, so prints `3 - 1 = 2`

**Output:**
```
2
```

### ii) Output for (new B(3)).m():

**Step-by-step execution:**
1. `new B(3)` creates an instance of class B
   - Constructor `B(3)` is called
   - `super(y - 1)` is called, which is `super(3 - 1)` = `super(2)`
   - A's constructor `A(2)` sets `this.x = 2` (in A)
   - Back in B's constructor, `this.y = 3` is set
2. `.m()` is called on the B instance
3. Since B overrides `m()`, B's `m()` method executes: `System.out.println(y + 1)`
   - `y = 3`, so prints `3 + 1 = 4`

**Output:**
```
4
```

### iii) Output for ((A)(new B(3))).m():

**Step-by-step execution:**
1. `new B(3)` creates an instance of class B (same as above)
   - `x = 2` (in A), `y = 3` (in B)
2. `(A)(new B(3))` casts the B instance to type A
   - This is an upcast, which is always valid
   - The object is still a B instance, just referenced as type A
3. `.m()` is called
4. **Important:** Even though the reference type is A, the actual object is B
   - Java uses **dynamic method dispatch** (runtime polymorphism)
   - The overridden method in B is called, not A's method
   - B's `m()` executes: `System.out.println(y + 1)`
   - `y = 3`, so prints `3 + 1 = 4`

**Output:**
```
4
```

**Key Concept:** Method overriding uses dynamic binding - the actual object type determines which method is called, not the reference type.

---

## Part c) Constructor Overloading and Chaining

### Given Code (Figure c):

```java
class Test {
    int var;
    
    Test(double var) {
        this.var = (int) var;
    }
    
    Test(int var) {
        this("aaa");
    }
    
    Test(String s) {
        this();
        System.out.println(s);
    }
    
    Test() {
        System.out.println("bbb");
    }
    
    public static void main(String[] args) {
        Test t = new Test(5);
    }
}
```

### Output Analysis:

**Step-by-step execution:**
1. `new Test(5)` is called in main
2. `Test(int var)` constructor is invoked (matches `5` as int)
3. `Test(int var)` calls `this("aaa")`
4. `Test(String s)` constructor is invoked with `s = "aaa"`
5. `Test(String s)` first calls `this()`
6. `Test()` constructor is invoked (no-arg constructor)
7. `Test()` prints `"bbb"` and returns
8. Back in `Test(String s)`, prints `"aaa"` and returns
9. Back in `Test(int var)`, constructor completes
10. `var` is never set (the `this.var = (int) var;` line is in a different constructor)

**Output:**
```
bbb
aaa
```

---

## Part d) Object Passing and Member Access

### Given Code (Figure d):

```java
class Test {
    int x;
    
    Test(int x) {
        this.x = x;
    }
    
    public static void m(Test o) {
        o = new Test(2);
        System.out.println("output = " + o.x);
    }
    
    public static void main(String[] args) {
        Test o = new Test(1);
        m(o);
        System.out.println("output = " + o.x);
    }
}
```

### Output Analysis:

**Step-by-step execution:**
1. `main` method starts
2. `Test o = new Test(1)` creates an object with `x = 1`
3. `m(o)` is called, passing the reference to the Test object
4. **Important:** Java passes object references by value
   - The parameter `o` in method `m` is a copy of the reference
   - Initially, `o` in `m` points to the same object (with `x = 1`)
5. Inside `m`, `o = new Test(2)` creates a NEW object and assigns it to the local parameter `o`
   - This does NOT affect the original object in `main`
   - The local `o` now points to a new object with `x = 2`
6. `System.out.println("output = " + o.x)` prints `"output = 2"`
7. Method `m` returns
8. Back in `main`, the original `o` still points to the original object with `x = 1`
9. `System.out.println("output = " + o.x)` prints `"output = 1"`

**Output:**
```
output = 2
output = 1
```

**Key Concept:** Java passes object references by value. Reassigning the parameter in the method does not change the original reference in the caller.

---

## Summary

| Question | Output |
|----------|--------|
| a-i) m(1) | `4`<br>`3` |
| a-ii) m(0) | `4`<br>`2`<br>`3` |
| b-i) (new A(3)).m() | `2` |
| b-ii) (new B(3)).m() | `4` |
| b-iii) ((A)(new B(3))).m() | `4` |
| c) new Test(5) | `bbb`<br>`aaa` |
| d) Object passing | `output = 2`<br>`output = 1` |

---

**End of Question 1**
