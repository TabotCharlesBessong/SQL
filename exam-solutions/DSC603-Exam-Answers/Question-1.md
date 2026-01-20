# Question 1: Data Similarity Calculations
## DSC 603 - Data Mining
**Total Marks: 1.5 × 10 = 15 marks (Compulsory)**

---

## Problem Statement

**Given Data Set:**
- x₁ = (1.5, 1.7)
- x₂ = (2.0, 1.9)
- x₃ = (1.6, 1.8)
- x₄ = (1.2, 1.5)
- x₅ = (1.5, 1.0)

**Query Point:**
- x = (1.4, 1.6)

**Task:**
Rank the database points (x₁ to x₅) based on similarity with the query point using:
1. **Euclidean Distance** (smaller distance = more similar)
2. **Cosine Similarity** (larger value = more similar)

---

## Formulas

### Euclidean Distance
```
d(i, j) = √[(xi₁ - xj₁)² + (xi₂ - xj₂)² + ... + (xin - xjn)²]
```

For 2-dimensional points:
```
d(x, y) = √[(x₁ - y₁)² + (x₂ - y₂)²]
```

### Cosine Similarity
```
s(x, y) = (xᵀ · y) / (||x|| × ||y||)
```

Where:
- **xᵀ · y** = dot product (sum of products of corresponding components)
- **||x||** = magnitude (Euclidean norm) = √(x₁² + x₂² + ... + xn²)
- **||y||** = magnitude of y

For 2-dimensional vectors:
```
s(x, y) = (x₁y₁ + x₂y₂) / (√(x₁² + x₂²) × √(y₁² + y₂²))
```

---

## Part 1: Euclidean Distance Calculations

### Step 1: Calculate Euclidean Distance for Each Point

**Query Point:** x = (1.4, 1.6)

**For x₁ = (1.5, 1.7):**
```
d(x, x₁) = √[(1.4 - 1.5)² + (1.6 - 1.7)²]
         = √[(-0.1)² + (-0.1)²]
         = √[0.01 + 0.01]
         = √0.02
         = 0.1414
```

**For x₂ = (2.0, 1.9):**
```
d(x, x₂) = √[(1.4 - 2.0)² + (1.6 - 1.9)²]
         = √[(-0.6)² + (-0.3)²]
         = √[0.36 + 0.09]
         = √0.45
         = 0.6708
```

**For x₃ = (1.6, 1.8):**
```
d(x, x₃) = √[(1.4 - 1.6)² + (1.6 - 1.8)²]
         = √[(-0.2)² + (-0.2)²]
         = √[0.04 + 0.04]
         = √0.08
         = 0.2828
```

**For x₄ = (1.2, 1.5):**
```
d(x, x₄) = √[(1.4 - 1.2)² + (1.6 - 1.5)²]
         = √[(0.2)² + (0.1)²]
         = √[0.04 + 0.01]
         = √0.05
         = 0.2236
```

**For x₅ = (1.5, 1.0):**
```
d(x, x₅) = √[(1.4 - 1.5)² + (1.6 - 1.0)²]
         = √[(-0.1)² + (0.6)²]
         = √[0.01 + 0.36]
         = √0.37
         = 0.6083
```

### Step 2: Rank by Euclidean Distance

**Summary Table:**

| Point | Coordinates | Euclidean Distance | Rank |
|-------|------------|-------------------|------|
| x₁ | (1.5, 1.7) | 0.1414 | **1 (Most Similar)** |
| x₄ | (1.2, 1.5) | 0.2236 | **2** |
| x₃ | (1.6, 1.8) | 0.2828 | **3** |
| x₅ | (1.5, 1.0) | 0.6083 | **4** |
| x₂ | (2.0, 1.9) | 0.6708 | **5 (Least Similar)** |

**Ranking (Euclidean Distance - Smaller is Better):**
1. **x₁** (distance = 0.1414) - Closest to query point
2. **x₄** (distance = 0.2236)
3. **x₃** (distance = 0.2828)
4. **x₅** (distance = 0.6083)
5. **x₂** (distance = 0.6708) - Farthest from query point

---

## Part 2: Cosine Similarity Calculations

### Step 1: Calculate Magnitudes

**Query Point:** x = (1.4, 1.6)
```
||x|| = √(1.4² + 1.6²)
      = √(1.96 + 2.56)
      = √4.52
      = 2.126
```

**Magnitude of Database Points:**

**For x₁ = (1.5, 1.7):**
```
||x₁|| = √(1.5² + 1.7²)
       = √(2.25 + 2.89)
       = √5.14
       = 2.267
```

**For x₂ = (2.0, 1.9):**
```
||x₂|| = √(2.0² + 1.9²)
       = √(4.0 + 3.61)
       = √7.61
       = 2.759
```

**For x₃ = (1.6, 1.8):**
```
||x₃|| = √(1.6² + 1.8²)
       = √(2.56 + 3.24)
       = √5.80
       = 2.408
```

**For x₄ = (1.2, 1.5):**
```
||x₄|| = √(1.2² + 1.5²)
       = √(1.44 + 2.25)
       = √3.69
       = 1.921
```

**For x₅ = (1.5, 1.0):**
```
||x₅|| = √(1.5² + 1.0²)
       = √(2.25 + 1.0)
       = √3.25
       = 1.803
```

### Step 2: Calculate Dot Products

**Query Point:** x = (1.4, 1.6)

**For x₁ = (1.5, 1.7):**
```
x · x₁ = (1.4 × 1.5) + (1.6 × 1.7)
       = 2.1 + 2.72
       = 4.82
```

**For x₂ = (2.0, 1.9):**
```
x · x₂ = (1.4 × 2.0) + (1.6 × 1.9)
       = 2.8 + 3.04
       = 5.84
```

**For x₃ = (1.6, 1.8):**
```
x · x₃ = (1.4 × 1.6) + (1.6 × 1.8)
       = 2.24 + 2.88
       = 5.12
```

**For x₄ = (1.2, 1.5):**
```
x · x₄ = (1.4 × 1.2) + (1.6 × 1.5)
       = 1.68 + 2.4
       = 4.08
```

**For x₅ = (1.5, 1.0):**
```
x · x₅ = (1.4 × 1.5) + (1.6 × 1.0)
       = 2.1 + 1.6
       = 3.7
```

### Step 3: Calculate Cosine Similarity

**Query Point Magnitude:** ||x|| = 2.126

**For x₁:**
```
s(x, x₁) = (x · x₁) / (||x|| × ||x₁||)
         = 4.82 / (2.126 × 2.267)
         = 4.82 / 4.819
         = 1.0002
         ≈ 1.000
```

**For x₂:**
```
s(x, x₂) = (x · x₂) / (||x|| × ||x₂||)
         = 5.84 / (2.126 × 2.759)
         = 5.84 / 5.866
         = 0.9956
```

**For x₃:**
```
s(x, x₃) = (x · x₃) / (||x|| × ||x₃||)
         = 5.12 / (2.126 × 2.408)
         = 5.12 / 5.119
         = 0.9998
         ≈ 1.000
```

**For x₄:**
```
s(x, x₄) = (x · x₄) / (||x|| × ||x₄||)
         = 4.08 / (2.126 × 1.921)
         = 4.08 / 4.084
         = 0.9990
```

**For x₅:**
```
s(x, x₅) = (x · x₅) / (||x|| × ||x₅||)
         = 3.7 / (2.126 × 1.803)
         = 3.7 / 3.833
         = 0.9653
```

### Step 4: Rank by Cosine Similarity

**Summary Table:**

| Point | Coordinates | Cosine Similarity | Rank |
|-------|------------|------------------|------|
| x₁ | (1.5, 1.7) | 1.000 | **1 (Most Similar)** |
| x₃ | (1.6, 1.8) | 1.000 | **2** |
| x₄ | (1.2, 1.5) | 0.9990 | **3** |
| x₂ | (2.0, 1.9) | 0.9956 | **4** |
| x₅ | (1.5, 1.0) | 0.9653 | **5 (Least Similar)** |

**Ranking (Cosine Similarity - Larger is Better):**
1. **x₁** (similarity = 1.000) - Most similar direction/angle
2. **x₃** (similarity = 1.000) - Same angle as x₁
3. **x₄** (similarity = 0.9990)
4. **x₂** (similarity = 0.9956)
5. **x₅** (similarity = 0.9653) - Least similar direction

---

## Comparison and Analysis

### Key Observations

**Euclidean Distance Ranking:**
1. x₁ (0.1414)
2. x₄ (0.2236)
3. x₃ (0.2828)
4. x₅ (0.6083)
5. x₂ (0.6708)

**Cosine Similarity Ranking:**
1. x₁ (1.000) / x₃ (1.000) - tie
2. x₄ (0.9990)
3. x₂ (0.9956)
4. x₅ (0.9653)

### Differences Between Rankings

**Why the Rankings Differ:**
- **Euclidean Distance** measures **absolute distance** in the coordinate space (magnitude + direction)
- **Cosine Similarity** measures **angle/direction** only, ignoring magnitude

**Specific Differences:**
1. **x₁ and x₃:** 
   - Euclidean: x₁ is closer (0.1414 vs 0.2828)
   - Cosine: Both have same angle (both = 1.000)

2. **x₄ and x₃:**
   - Euclidean: x₄ is closer (0.2236 vs 0.2828)
   - Cosine: x₃ is more similar (1.000 vs 0.9990) - very close

3. **x₂:**
   - Euclidean: Second farthest (0.6708)
   - Cosine: Moderate similarity (0.9956) - has similar direction but different magnitude

4. **x₅:**
   - Euclidean: Fourth closest (0.6083)
   - Cosine: Least similar (0.9653) - has different direction

### When to Use Each Measure

**Euclidean Distance:**
- Use when **magnitude matters** (e.g., actual position in space)
- Sensitive to scale differences
- Good for clustering, k-NN when distance is meaningful

**Cosine Similarity:**
- Use when **direction/angle matters** more than magnitude
- **Scale-invariant** (normalizes for magnitude)
- Good for text similarity, recommendation systems, when magnitude is less important

**In This Case:**
- Query point: (1.4, 1.6)
- Points x₁, x₃, x₄ all have very similar directions (cosine ≈ 1.0)
- But x₁ is closest in absolute distance
- The difference in rankings shows that cosine similarity finds points with similar "direction" while Euclidean finds points that are close in the 2D space

---

## Final Answer Summary

### Euclidean Distance Ranking (Smallest to Largest):
1. **x₁** - distance = 0.1414
2. **x₄** - distance = 0.2236
3. **x₃** - distance = 0.2828
4. **x₅** - distance = 0.6083
5. **x₂** - distance = 0.6708

### Cosine Similarity Ranking (Largest to Smallest):
1. **x₁** - similarity = 1.000
2. **x₃** - similarity = 1.000
3. **x₄** - similarity = 0.9990
4. **x₂** - similarity = 0.9956
5. **x₅** - similarity = 0.9653

---

**End of Question 1**
