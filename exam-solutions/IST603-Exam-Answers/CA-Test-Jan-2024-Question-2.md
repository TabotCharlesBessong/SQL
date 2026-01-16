# Question 2: Write the Output of Each Code Snippet
## IST603 CA Test - January 2024
## Java Language
**Total Marks: 1 × 5 = 5 marks**

---

## Instructions
Write the output of each of the following code snippets.

---

## Question 2(a): String Array with Post-increment

**Code Snippet (a):**
```java
String[] nums = {"One", "Two", "Three", "Four", "Five", "Six", "Sev"};
for(int i = 0; i < nums.length; i++) {
  if (nums[i++].length() % 3 == 0) {
    continue;
  }
  System.out.println(nums[i]);
  break;
}
```

### Solution:

**Output:**
```
Four
```

**Step-by-step execution:**

Initial array: `nums = {"One", "Two", "Three", "Four", "Five", "Six", "Sev"}`

String lengths and modulo 3:
- "One" = 3 chars → 3 % 3 = 0 ✓
- "Two" = 3 chars → 3 % 3 = 0 ✓
- "Three" = 5 chars → 5 % 3 = 2 ✗
- "Four" = 4 chars → 4 % 3 = 1 ✗
- "Five" = 4 chars → 4 % 3 = 1 ✗
- "Six" = 3 chars → 3 % 3 = 0 ✓
- "Sev" = 3 chars → 3 % 3 = 0 ✓

**Iteration 0 (i = 0):**
1. Evaluate condition: `nums[i++]`
   - Current `i = 0`
   - Access `nums[0] = "One"`
   - `"One".length() = 3`
   - `3 % 3 = 0` → condition is `true`
   - After access, `i` becomes `1` (post-increment)
2. Condition is `true`, so `continue` executes
3. **Important:** In Java, `continue` in a for loop skips the rest of the loop body but **still executes the increment expression** (`i++` in the for loop header)
4. After `continue`, the for loop increment executes: `i++` → `i` becomes `2`
5. Loop condition checked: `i < nums.length` → `2 < 7` → `true`, continue to next iteration

**Iteration 1 (i = 2):**
1. Evaluate condition: `nums[i++]`
   - Current `i = 2`
   - Access `nums[2] = "Three"`
   - `"Three".length() = 5`
   - `5 % 3 = 2` → condition is `false`
   - After access, `i` becomes `3` (post-increment)
2. Condition is `false`, so skip the `continue` statement
3. Execute: `System.out.println(nums[i])`
   - `i = 3` (after post-increment from step 1)
   - `nums[3] = "Four"`
   - Prints: `Four`
4. Execute: `break` → exits the loop immediately
5. The for loop increment (`i++`) does **NOT** execute because of `break`

**Final Output:** `Four`

**Key Points:**
- `nums[i++]` uses post-increment: accesses `nums[i]` first, then increments `i`
- `continue` in a for loop still executes the increment expression in the for loop header
- `break` exits the loop immediately, skipping the increment expression
- The first string with length not divisible by 3 is "Three" at index 2, but we print `nums[3]` because `i` was incremented by the post-increment operator

---

## Question 2(b): Variable Shadowing with Class and Local Variables

**Code Snippet (b):**
```java
public class MyLoop {
  private static final int i = 99;
  public static void main(String[] args) {
    for (int i=0; i < 100; i++) {
      System.out.print(i);
      i++;
      break;
    }
    System.out.print(i);
  }
}
```

### Solution:

**Output:**
```
099
```

**Step-by-step execution:**

1. **Class-level variable:** `private static final int i = 99;`
   - This is a class variable (static) with value `99`

2. **Local variable in main method:**
   - `for (int i=0; i < 100; i++)` declares a **local variable** `i` that shadows the class variable
   - Inside the for loop, `i` refers to the local variable, not the class variable

3. **For loop execution:**
   - `int i=0` initializes local `i = 0`
   - Condition `i < 100` → `0 < 100` → `true`
   - Loop body executes:
     - `System.out.print(i)` → prints `0` (local `i`)
     - `i++` → local `i` becomes `1`
     - `break` → exits the loop immediately
   - Loop increment `i++` is NOT executed because of `break`

4. **After the loop:**
   - The local variable `i` (from the for loop) goes out of scope
   - `System.out.print(i)` → refers to the class variable `i = 99`
   - Prints `99`

**Final Output:** `099`

**Key Concepts:**
- **Variable Shadowing:** The local variable `i` in the for loop shadows the class variable `i`
- **Scope:** After the for loop, the local `i` is out of scope, so the class variable `i` is accessible again
- **Break Statement:** The `break` exits the loop immediately, so the loop increment doesn't execute

---

## Question 2(c): Switch Statement with Fall-Through

**Code Snippet (c):**
```java
public class MyLoop {
  public static void main(String[] args) {
    byte b = 3;
    int i = 0;
    switch(b) {
      case 3: i = i + 4;
      case 2: i = i + 2;
    }
    System.out.println(i);
  }
}
```

### Solution:

**Output:**
```
6
```

**Step-by-step execution:**

1. `byte b = 3;` → `b = 3`
2. `int i = 0;` → `i = 0`
3. `switch(b)` → matches `case 3:`
4. **Case 3 executes:**
   - `i = i + 4` → `i = 0 + 4 = 4`
   - **No `break` statement** → execution falls through to the next case
5. **Case 2 executes (fall-through):**
   - `i = i + 2` → `i = 4 + 2 = 6`
   - No more cases, switch ends
6. `System.out.println(i)` → prints `6`

**Final Output:** `6`

**Key Concept:** Switch statement fall-through behavior - when there's no `break` statement, execution continues to the next case.

---

## Question 2(d): Switch Statement with Print Inside Case

**Code Snippet (d):**
```java
public class MyLoop {
  public static void main(String[] args) {
    byte b = 3;
    int i = 0;
    switch(b) {
      case 3: i = i + 4;
      System.out.println(i);
      case 2: i = i + 2;
    }
  }
}
```

### Solution:

**Output:**
```
4
```

**Step-by-step execution:**

1. `byte b = 3;` → `b = 3`
2. `int i = 0;` → `i = 0`
3. `switch(b)` → matches `case 3:`
4. **Case 3 executes:**
   - `i = i + 4` → `i = 0 + 4 = 4`
   - `System.out.println(i)` → prints `4`
   - **No `break` statement** → execution falls through to the next case
5. **Case 2 executes (fall-through):**
   - `i = i + 2` → `i = 4 + 2 = 6`
   - No more statements, switch ends
6. **No print statement after switch** → nothing else is printed

**Final Output:** `4`

**Note:** The value of `i` becomes `6` after case 2, but there's no print statement after the switch, so only `4` is printed.

---

## Question 2(e): Switch Statement with Break Statements

**Code Snippet (e):**
```java
public class MyLoop {
  public static void main(String[] args) {
    byte b = 3;
    int i = 0;
    switch(b) {
      case 3: i = i + 4; break;
      case 2: i = i + 2; break;
    }
    System.out.println(i);
  }
}
```

### Solution:

**Output:**
```
4
```

**Step-by-step execution:**

1. `byte b = 3;` → `b = 3`
2. `int i = 0;` → `i = 0`
3. `switch(b)` → matches `case 3:`
4. **Case 3 executes:**
   - `i = i + 4` → `i = 0 + 4 = 4`
   - `break;` → exits the switch statement immediately
5. **Case 2 is NOT executed** (because of `break` in case 3)
6. `System.out.println(i)` → prints `4`

**Final Output:** `4`

**Key Concept:** The `break` statement prevents fall-through, so only case 3 executes.

---

## Summary of Outputs

| Question | Code Snippet | Output |
|----------|--------------|--------|
| (a) | String array with post-increment | `Four` |
| (b) | Variable shadowing | `099` |
| (c) | Switch fall-through | `6` |
| (d) | Switch with print inside case | `4` |
| (e) | Switch with break | `4` |

---

## Key Concepts Demonstrated

1. **Post-increment operator (`i++`):** Returns the value before incrementing
2. **Variable shadowing:** Local variables can shadow class/instance variables
3. **Switch statement fall-through:** Without `break`, execution continues to next case
4. **Break statement:** Exits the switch statement immediately
5. **Scope:** Local variables are only accessible within their scope

---

**End of Question 2**
