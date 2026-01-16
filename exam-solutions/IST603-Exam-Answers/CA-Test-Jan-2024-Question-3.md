# Question 3: Loop Constructs
## IST603 CA Test - January 2024
## Python Language
**Total Marks: 2 × 3 = 6 marks**

---

## Instructions
Imagine you are writing an interactive console application that performs the following steps repeatedly:
1. Prints the prompt "Enter an integer"
2. Reads an integer as input
3. If the input integer is `0`, the application exits. Otherwise, it displays the number read and then restarts the process from step 1.

Write **code fragments** (not complete programs) that would implement this logic using the following loop constructs for iteration:

---

## Part i) Using a `for` Loop

### Solution:

**Code Fragment:**
```python
while True:
    print("Enter an integer")
    num = int(input())
    if num == 0:
        break
    print(num)
```

**Alternative using `for` loop with range:**
```python
# Note: This is less natural for this use case, but demonstrates for loop usage
for _ in iter(int, 1):  # Using iter() with sentinel
    print("Enter an integer")
    num = int(input())
    if num == 0:
        break
    print(num)
```

**Most Practical Approach:**
Since a `for` loop in Python requires an iterable and we don't know how many iterations we need, the most practical approach is to use a `while True` loop with a `break` statement. However, if we must use a `for` loop, we can use:

```python
from itertools import count

for _ in count():  # Infinite iterator
    print("Enter an integer")
    num = int(input())
    if num == 0:
        break
    print(num)
```

**Explanation:**
- `itertools.count()` creates an infinite iterator
- The `for` loop iterates indefinitely until `break` is encountered
- When `num == 0`, the loop exits via `break`

**Note:** In practice, `while True` is more idiomatic for this use case, but the above demonstrates how to use a `for` loop for an indefinite iteration pattern.

---

## Part ii) Using a `while` Loop

### Solution:

**Code Fragment:**
```python
num = 1  # Initialize to non-zero value to enter loop
while num != 0:
    print("Enter an integer")
    num = int(input())
    if num != 0:
        print(num)
```

**Alternative (more explicit):**
```python
num = None
while num != 0:
    print("Enter an integer")
    num = int(input())
    if num != 0:
        print(num)
```

**Most Common Approach:**
```python
while True:
    print("Enter an integer")
    num = int(input())
    if num == 0:
        break
    print(num)
```

**Explanation:**
- The `while` loop continues as long as the condition is `true`
- First approach: Initialize `num` to a non-zero value to enter the loop, then check if `num != 0` to continue
- Second approach: Use `while True` with a `break` statement when `num == 0`
- The number is printed only if it's not zero (before the loop exits)

**Key Points:**
- `while num != 0` ensures the loop continues until zero is entered
- The number is displayed before checking if it's zero (in the first approach)
- The `while True` approach is more common and clearer

---

## Part iii) Using a `do..while` Loop

### Solution:

**Code Fragment:**
```python
# Python doesn't have a native do-while loop, so we emulate it
while True:
    print("Enter an integer")
    num = int(input())
    print(num)
    if num == 0:
        break
```

**Alternative (more explicit do-while emulation):**
```python
# Emulate do-while: execute at least once, then check condition
while True:
    print("Enter an integer")
    num = int(input())
    print(num)
    if num == 0:
        break
```

**Explanation:**
Python does **not** have a native `do..while` loop construct. However, we can emulate its behavior using a `while True` loop with a `break` statement.

**Do-While Behavior:**
- A `do..while` loop executes the loop body **at least once** before checking the condition
- The condition is checked **after** each iteration
- The loop continues while the condition is `true`

**Emulation Strategy:**
1. Use `while True:` to create an infinite loop
2. Execute the loop body (print prompt, read input, print number)
3. Check the exit condition (`if num == 0: break`) at the **end** of the loop body
4. This ensures the body executes at least once before checking the condition

**Comparison with Other Languages:**
```java
// Java do-while syntax (for reference)
do {
    System.out.println("Enter an integer");
    int num = Integer.parseInt(input.readLine());
    System.out.println(num);
} while (num != 0);
```

The Python emulation achieves the same behavior:
- Loop body executes first
- Condition is checked after the body
- Loop continues until condition is false

**Key Points:**
- Python doesn't have `do..while`, so we use `while True` with `break`
- The condition check is placed at the **end** of the loop body
- This ensures the body executes at least once (do-while behavior)

---

## Summary

| Loop Type | Python Implementation | Key Characteristic |
|-----------|----------------------|-------------------|
| `for` | `for _ in count():` with `break` | Requires infinite iterator |
| `while` | `while num != 0:` or `while True:` | Condition checked before iteration |
| `do..while` | `while True:` with `break` at end | Emulated; body executes at least once |

---

## Complete Code Examples (for reference)

### For Loop Approach:
```python
from itertools import count

for _ in count():
    print("Enter an integer")
    num = int(input())
    if num == 0:
        break
    print(num)
```

### While Loop Approach:
```python
num = 1
while num != 0:
    print("Enter an integer")
    num = int(input())
    if num != 0:
        print(num)
```

### Do-While Emulation:
```python
while True:
    print("Enter an integer")
    num = int(input())
    print(num)
    if num == 0:
        break
```

---

**End of Question 3**
