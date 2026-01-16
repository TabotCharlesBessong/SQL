# Question 1: Multiple Choice Questions on Arrays
## IST603 CA Test - January 2024
## Java Language
**Total Marks: 1 × 6 = 6 marks**

---

## Instructions
Write the letter corresponding to the correct answer selected from the answer grid below.

---

## Question 1(a): Array Parameter Passing

**Question:** When you pass an array to a method, the method receives _________

**Answer Options:**
- A: A copy of the array
- B: A copy of the first element
- C: The reference of the array
- D: The length of the array

### Solution:

**Answer: C - The reference of the array**

**Explanation:**
In Java, arrays are objects, and when you pass an array to a method, you're passing the reference (memory address) to that array, not a copy of the array itself. This means:
- The method receives a reference to the same array object
- Any modifications made to the array elements inside the method will affect the original array
- This is different from primitive types, which are passed by value

**Example:**
```java
public static void modifyArray(int[] arr) {
    arr[0] = 100;  // This modifies the original array
}

public static void main(String[] args) {
    int[] myArray = {1, 2, 3};
    modifyArray(myArray);
    System.out.println(myArray[0]);  // Output: 100 (original array was modified)
}
```

---

## Question 1(b): Array Element Transformation

**Code Fragment (a):**
```java
int[] a = {0, 2, 4, 1, 3};
for(int i = 0; i < a.length; i++)
  a[i] = a[(a[i] + 3) % a.length];
```

**Question:** What is the value of `a[0]` after the following code is executed?

**Answer Options:**
- A: 1
- B: 2
- C: 3
- D: 4

### Solution:

**Answer: A - 1**

**Step-by-step execution:**

Initial array: `a = {0, 2, 4, 1, 3}`

**Iteration 0 (i = 0):**
- Current `a[0] = 0`
- Calculate: `(a[0] + 3) % a.length = (0 + 3) % 5 = 3 % 5 = 3`
- `a[0] = a[3] = 1`
- Array becomes: `{1, 2, 4, 1, 3}`

**Iteration 1 (i = 1):**
- Current `a[1] = 2`
- Calculate: `(a[1] + 3) % a.length = (2 + 3) % 5 = 5 % 5 = 0`
- `a[1] = a[0] = 1` (using updated value from iteration 0)
- Array becomes: `{1, 1, 4, 1, 3}`

**Iteration 2 (i = 2):**
- Current `a[2] = 4`
- Calculate: `(a[2] + 3) % a.length = (4 + 3) % 5 = 7 % 5 = 2`
- `a[2] = a[2] = 4` (no change)
- Array remains: `{1, 1, 4, 1, 3}`

**Iteration 3 (i = 3):**
- Current `a[3] = 1`
- Calculate: `(a[3] + 3) % a.length = (1 + 3) % 5 = 4 % 5 = 4`
- `a[3] = a[4] = 3`
- Array becomes: `{1, 1, 4, 3, 3}`

**Iteration 4 (i = 4):**
- Current `a[4] = 3`
- Calculate: `(a[4] + 3) % a.length = (3 + 3) % 5 = 6 % 5 = 1`
- `a[4] = a[1] = 1` (using updated value from iteration 1)
- Final array: `{1, 1, 4, 3, 1}`

**Final Answer:** `a[0] = 1`

---

## Question 1(c): Array Element Transformation (Continued)

**Code Fragment (a):** (Same as above)
```java
int[] a = {0, 2, 4, 1, 3};
for(int i = 0; i < a.length; i++)
  a[i] = a[(a[i] + 3) % a.length];
```

**Question:** What is the value of `a[1]` after the following code is executed?

**Answer Options:**
- A: 1
- B: 2
- C: 3
- D: 4

### Solution:

**Answer: A - 1**

**Explanation:**
Using the same step-by-step execution from Question 1(b), after all iterations:
- Final array: `{1, 1, 4, 3, 1}`
- `a[1] = 1`

**Final Answer:** `a[1] = 1`

---

## Question 1(d): Octal Literal in Array

**Code Fragment (b):**
```java
public class Test {
  public static void main(String[] args){
    int[] x = {120, 200, 016};
    for(int i = 0; i < x.length; i++)
      System.out.print(x[i] + " ");
  }
}
```

**Question:** What is the result of compiling and running the following code?

**Answer Options:**
- A: 120 200 016
- B: 120 200 16
- C: 120 200 14
- D: Compile time error

### Solution:

**Answer: C - 120 200 14**

**Explanation:**
In Java, a numeric literal starting with `0` (zero) is interpreted as an octal (base-8) number:
- `016` in octal = `1 × 8¹ + 6 × 8⁰ = 8 + 6 = 14` in decimal
- The array `x` contains: `{120, 200, 14}` (decimal values)
- The output will be: `120 200 14`

**Note:** The literal `016` is not printed as "016" - it's converted to its decimal equivalent (14) when stored in the array.

**Final Answer:** `120 200 14`

---

## Question 1(e): Decimal Literal Replacement

**Code Fragment (b):** (Modified)
```java
public class Test {
  public static void main(String[] args){
    int[] x = {120, 200, 16};  // 016 replaced by 16
    for(int i = 0; i < x.length; i++)
      System.out.print(x[i] + " ");
  }
}
```

**Question:** What is the result of compiling and running the following code if `016` on the third line is replaced by `16`?

**Answer Options:**
- A: 120 200 016
- B: 120 200 16
- C: 120 200 14
- D: 120 200 014

### Solution:

**Answer: B - 120 200 16**

**Explanation:**
When `016` is replaced by `16`:
- `16` is a decimal (base-10) literal (no leading zero)
- The array `x` contains: `{120, 200, 16}` (decimal values)
- The output will be: `120 200 16`

**Final Answer:** `120 200 16`

---

## Question 1(f): Finding Maximum Element Index

**Code Fragment (c):**
```java
public class Test {
  public static void main(String args[]){
    double[] myList = {1, 5, 5, 5, 1};
    double max = myList[0];
    int indexOfMax = 0;
    for(int i=1; i < myList.length; i++){
      if(myList[i] > max){
        max = myList[i];
        indexOfMax = i;
      }
    }
    System.out.println(indexOfMax);
  }
}
```

**Question:** What is the output when the code fragment in (c) below is run?

**Answer Options:**
- A: 0
- B: 1
- C: 2
- D: 3

### Solution:

**Answer: B - 1**

**Step-by-step execution:**

Initial values:
- `myList = {1, 5, 5, 5, 1}`
- `max = myList[0] = 1`
- `indexOfMax = 0`

**Iteration 1 (i = 1):**
- `myList[1] = 5`
- `5 > 1` (true)
- `max = 5`
- `indexOfMax = 1`

**Iteration 2 (i = 2):**
- `myList[2] = 5`
- `5 > 5` (false)
- No update to `max` or `indexOfMax`

**Iteration 3 (i = 3):**
- `myList[3] = 5`
- `5 > 5` (false)
- No update to `max` or `indexOfMax`

**Iteration 4 (i = 4):**
- `myList[4] = 1`
- `1 > 5` (false)
- No update to `max` or `indexOfMax`

**Final values:**
- `max = 5`
- `indexOfMax = 1`

**Output:** `1`

**Note:** The algorithm finds the index of the first occurrence of the maximum value. Since the condition is `>` (not `>=`), it only updates when a strictly greater value is found, so it keeps the first index (1) where the maximum value (5) was found.

**Final Answer:** `1`

---

## Summary of Answers

| Question | Answer | Key Concept |
|----------|--------|-------------|
| (a) Array parameter passing | **C** | Arrays are passed by reference |
| (b) `a[0]` after transformation | **A** | Array element transformation with modulo |
| (c) `a[1]` after transformation | **A** | Array element transformation (continued) |
| (d) Octal literal `016` | **C** | Octal to decimal conversion (016 = 14) |
| (e) Decimal literal `16` | **B** | Decimal literal (16 = 16) |
| (f) Index of maximum element | **B** | Finding first occurrence of maximum value |

---

**End of Question 1**
