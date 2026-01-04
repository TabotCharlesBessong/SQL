# QUESTION 1(f) - PYTHON OUTPUT SOLUTIONS

---

## (i) List Iteration

```python
numbers = [10, 20]
for x in numbers:
    print(x)
```

**Output:**
```
10
20
```

**Explanation:** Iterates through the list and prints each element.

---

## (ii) List Comprehension

```python
alst = [1,2,3,4,5,6,7]
pow2 = [2*x for x in alst]
print(pow2)
```

**Output:**
```
[2, 4, 6, 8, 10, 12, 14]
```

**Explanation:** List comprehension multiplies each element by 2: [2*1, 2*2, 2*3, ..., 2*7].

---

## (iii) Undefined Variable Error

```python
items = ["Chair", "Table"]
for y in items:
    print(x, y)  # Note: 'x' is not defined in this scope
```

**Output:**
```
NameError: name 'x' is not defined
```

**Explanation:** Variable `x` is not defined in this scope. If `x` were defined elsewhere (e.g., from snippet (i)), and assuming it retains its last value (20), the output would be:
```
20 Chair
20 Table
```

However, if run independently, this code will raise a NameError.

---

## (iv) Negative Indexing and Nested List Comprehension

```python
samplelist = [10,20,30,40,50]
print(samplelist[-2])
print(samplelist[-4:-1])
reslist = [x+y for x in ['Hello', 'Good'] for y in ['Dear', 'Bye']]
print(reslist)
```

**Output:**
```
40
[20, 30, 40]
['HelloDear', 'HelloBye', 'GoodDear', 'GoodBye']
```

**Explanation:**
- `samplelist[-2]` accesses the second element from the end: 40
- `samplelist[-4:-1]` slices from -4 to -1 (exclusive): [20, 30, 40]
- The nested list comprehension creates all combinations: 'Hello'+'Dear', 'Hello'+'Bye', 'Good'+'Dear', 'Good'+'Bye'

---

## (v) Nested Dictionary Access

```python
student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
print(student[1]["age"])
```

**Output:**
```
27
```

**Explanation:** Accesses the nested dictionary: student[1] gets the first student's dictionary, then ["age"] gets the value '27'.

