# Descriptive Statistics - Question 4
## Two-Dimensional Data Similarity Analysis

---

## Problem Statement

Suppose we have the following two-dimensional data set:

| Point | A1  | A2  |
|-------|-----|-----|
| x1    | 1.5 | 1.7 |
| x2    | 2.0 | 1.9 |
| x3    | 1.6 | 1.8 |
| x4    | 1.2 | 1.5 |
| x5    | 1.5 | 1.0 |

**Query Point:** x = (1.4, 1.6)

**Task:** Consider the data as two-dimensional data points. Given a new data point x = (1.4, 1.6) as a query, **rank the database points based on similarity** with the query using:
1. **Euclidean distance**
2. **Cosine similarity**

---

## Mathematical Formulas

### Euclidean Distance

For two points i and j in n-dimensional space:

```
d(i, j) = √[(xi1 - xj1)² + (xi2 - xj2)² + ··· + (xin - xjn)²]
```

**For 2D:**
```
d(i, j) = √[(xi1 - xj1)² + (xi2 - xj2)²]
```

**Interpretation:** 
- **Smaller distance** = **More similar**
- Measures straight-line distance between points

---

### Cosine Similarity

For two vectors x and y:

```
s(x, y) = (x^T · y) / (||x|| · ||y||)

Where:
- x^T · y = dot product (sum of element-wise products)
- ||x|| = magnitude of vector x = √(x1² + x2² + ... + xn²)
- ||y|| = magnitude of vector y
```

**For 2D:**
```
s(x, y) = (x1·y1 + x2·y2) / (√(x1² + x2²) · √(y1² + y2²))
```

**Interpretation:**
- **Larger similarity** = **More similar**
- Range: -1 to 1 (for our positive values: 0 to 1)
- Measures angle between vectors (direction similarity)

---

## Solution

### Query Point
```
Q = (1.4, 1.6)
```

### Database Points
```
x1 = (1.5, 1.7)
x2 = (2.0, 1.9)
x3 = (1.6, 1.8)
x4 = (1.2, 1.5)
x5 = (1.5, 1.0)
```

---

## Part 1: Euclidean Distance Ranking

### Distance Calculations

#### **Distance from Q to x1**
```
x1 = (1.5, 1.7)
Q = (1.4, 1.6)

d(Q, x1) = √[(1.5 - 1.4)² + (1.7 - 1.6)²]
         = √[(0.1)² + (0.1)²]
         = √[0.01 + 0.01]
         = √0.02
         = 0.1414
```

---

#### **Distance from Q to x2**
```
x2 = (2.0, 1.9)
Q = (1.4, 1.6)

d(Q, x2) = √[(2.0 - 1.4)² + (1.9 - 1.6)²]
         = √[(0.6)² + (0.3)²]
         = √[0.36 + 0.09]
         = √0.45
         = 0.6708
```

---

#### **Distance from Q to x3**
```
x3 = (1.6, 1.8)
Q = (1.4, 1.6)

d(Q, x3) = √[(1.6 - 1.4)² + (1.8 - 1.6)²]
         = √[(0.2)² + (0.2)²]
         = √[0.04 + 0.04]
         = √0.08
         = 0.2828
```

---

#### **Distance from Q to x4**
```
x4 = (1.2, 1.5)
Q = (1.4, 1.6)

d(Q, x4) = √[(1.2 - 1.4)² + (1.5 - 1.6)²]
         = √[(-0.2)² + (-0.1)²]
         = √[0.04 + 0.01]
         = √0.05
         = 0.2236
```

---

#### **Distance from Q to x5**
```
x5 = (1.5, 1.0)
Q = (1.4, 1.6)

d(Q, x5) = √[(1.5 - 1.4)² + (1.0 - 1.6)²]
         = √[(0.1)² + (-0.6)²]
         = √[0.01 + 0.36]
         = √0.37
         = 0.6083
```

---

### Euclidean Distance Summary Table

| Point | Coordinates | Distance from Q | Rank |
|-------|-------------|-----------------|------|
| x1    | (1.5, 1.7)  | 0.1414         | **1** ⭐ Most Similar |
| x4    | (1.2, 1.5)  | 0.2236         | **2** |
| x3    | (1.6, 1.8)  | 0.2828         | **3** |
| x5    | (1.5, 1.0)  | 0.6083         | **4** |
| x2    | (2.0, 1.9)  | 0.6708         | **5** Least Similar |

---

### **✅ Euclidean Distance Ranking (Most to Least Similar):**
```
1. x1 (distance = 0.1414)  ⭐ MOST SIMILAR
2. x4 (distance = 0.2236)
3. x3 (distance = 0.2828)
4. x5 (distance = 0.6083)
5. x2 (distance = 0.6708)  ⭐ LEAST SIMILAR
```

---

## Part 2: Cosine Similarity Ranking

### Similarity Calculations

#### **Cosine Similarity: Q and x1**
```
Q = (1.4, 1.6)
x1 = (1.5, 1.7)

Dot product:
Q · x1 = (1.4 × 1.5) + (1.6 × 1.7)
       = 2.1 + 2.72
       = 4.82

Magnitude of Q:
||Q|| = √(1.4² + 1.6²)
      = √(1.96 + 2.56)
      = √4.52
      = 2.1260

Magnitude of x1:
||x1|| = √(1.5² + 1.7²)
       = √(2.25 + 2.89)
       = √5.14
       = 2.2672

Cosine Similarity:
s(Q, x1) = 4.82 / (2.1260 × 2.2672)
         = 4.82 / 4.8196
         = 0.9999
```

---

#### **Cosine Similarity: Q and x2**
```
Q = (1.4, 1.6)
x2 = (2.0, 1.9)

Q · x2 = (1.4 × 2.0) + (1.6 × 1.9)
       = 2.8 + 3.04
       = 5.84

||Q|| = 2.1260 (calculated above)

||x2|| = √(2.0² + 1.9²)
       = √(4.0 + 3.61)
       = √7.61
       = 2.7586

s(Q, x2) = 5.84 / (2.1260 × 2.7586)
         = 5.84 / 5.8648
         = 0.9957
```

---

#### **Cosine Similarity: Q and x3**
```
Q = (1.4, 1.6)
x3 = (1.6, 1.8)

Q · x3 = (1.4 × 1.6) + (1.6 × 1.8)
       = 2.24 + 2.88
       = 5.12

||Q|| = 2.1260

||x3|| = √(1.6² + 1.8²)
       = √(2.56 + 3.24)
       = √5.80
       = 2.4083

s(Q, x3) = 5.12 / (2.1260 × 2.4083)
         = 5.12 / 5.1200
         = 1.0000
```

---

#### **Cosine Similarity: Q and x4**
```
Q = (1.4, 1.6)
x4 = (1.2, 1.5)

Q · x4 = (1.4 × 1.2) + (1.6 × 1.5)
       = 1.68 + 2.4
       = 4.08

||Q|| = 2.1260

||x4|| = √(1.2² + 1.5²)
       = √(1.44 + 2.25)
       = √3.69
       = 1.9209

s(Q, x4) = 4.08 / (2.1260 × 1.9209)
         = 4.08 / 4.0850
         = 0.9988
```

---

#### **Cosine Similarity: Q and x5**
```
Q = (1.4, 1.6)
x5 = (1.5, 1.0)

Q · x5 = (1.4 × 1.5) + (1.6 × 1.0)
       = 2.1 + 1.6
       = 3.7

||Q|| = 2.1260

||x5|| = √(1.5² + 1.0²)
       = √(2.25 + 1.0)
       = √3.25
       = 1.8028

s(Q, x5) = 3.7 / (2.1260 × 1.8028)
         = 3.7 / 3.8327
         = 0.9653
```

---

### Cosine Similarity Summary Table

| Point | Coordinates | Dot Product | ||Point|| | Similarity | Rank |
|-------|-------------|-------------|-----------|------------|------|
| x3    | (1.6, 1.8)  | 5.12        | 2.4083    | 1.0000     | **1** ⭐ Most Similar |
| x1    | (1.5, 1.7)  | 4.82        | 2.2672    | 0.9999     | **2** |
| x4    | (1.2, 1.5)  | 4.08        | 1.9209    | 0.9988     | **3** |
| x2    | (2.0, 1.9)  | 5.84        | 2.7586    | 0.9957     | **4** |
| x5    | (1.5, 1.0)  | 3.7         | 1.8028    | 0.9653     | **5** Least Similar |

---

### **✅ Cosine Similarity Ranking (Most to Least Similar):**
```
1. x3 (similarity = 1.0000)  ⭐ MOST SIMILAR
2. x1 (similarity = 0.9999)
3. x4 (similarity = 0.9988)
4. x2 (similarity = 0.9957)
5. x5 (similarity = 0.9653)  ⭐ LEAST SIMILAR
```

---

## Comparison of Results

### Side-by-Side Rankings

| Rank | Euclidean Distance | Cosine Similarity |
|------|-------------------|-------------------|
| 1    | **x1** (0.1414)   | **x3** (1.0000)   |
| 2    | **x4** (0.2236)   | **x1** (0.9999)   |
| 3    | **x3** (0.2828)   | **x4** (0.9988)   |
| 4    | x5 (0.6083)       | x2 (0.9957)       |
| 5    | x2 (0.6708)       | **x5** (0.9653)   |

---

### Key Differences

| Aspect | Euclidean Distance | Cosine Similarity |
|--------|-------------------|-------------------|
| **Top ranked** | x1 | x3 |
| **Bottom ranked** | x2 | x5 |
| **Measures** | Absolute distance | Angular similarity (direction) |
| **Sensitive to** | Magnitude differences | Directional differences |
| **Best for** | Spatial proximity | Proportional relationships |

---

### Why Different Rankings?

1. **x3 vs x1:**
   - **Cosine:** x3 has perfect directional alignment (1.0000)
   - **Euclidean:** x1 is closer in absolute position (0.1414 vs 0.2828)

2. **x2 vs x5:**
   - **Euclidean:** Both are far from Q, but x5 is slightly closer
   - **Cosine:** x2 has better directional alignment than x5

3. **Key Insight:**
   - Euclidean focuses on **how close** points are
   - Cosine focuses on **what direction** they point in

---

## Visual Representation

### 2D Coordinate Plot

```
A2 (Vertical)
2.0 |                   x2(2.0,1.9)
    |                   ●
1.9 |
    |
1.8 |              x3(1.6,1.8)
    |              ●
1.7 |          x1(1.5,1.7)
    |          ●
1.6 |       Q(1.4,1.6)
    |       ⊕
1.5 |   x4(1.2,1.5)
    |   ●
1.4 |
    |
1.3 |
    |
1.2 |
    |
1.1 |
    |
1.0 |          x5(1.5,1.0)
    |          ●
0.9 |___________________________________
    1.0  1.2  1.4  1.6  1.8  2.0  A1 (Horizontal)

Legend:
⊕ = Query point Q
● = Database points
```

**Observations:**
- x1 and x3 are closest to Q spatially (Euclidean perspective)
- x1, x3, x4, x2 all have similar directions from origin (Cosine perspective)
- x5 points in a different direction (lower A2 value)

---

## Python Code for Verification

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define query point
Q = np.array([1.4, 1.6])

# Define database points
points = {
    'x1': np.array([1.5, 1.7]),
    'x2': np.array([2.0, 1.9]),
    'x3': np.array([1.6, 1.8]),
    'x4': np.array([1.2, 1.5]),
    'x5': np.array([1.5, 1.0])
}

print("="*80)
print("2D DATA SIMILARITY ANALYSIS")
print("="*80)
print(f"\nQuery Point Q: {Q}")

# Calculate Euclidean distances
print("\n" + "="*80)
print("EUCLIDEAN DISTANCE CALCULATIONS")
print("="*80)

euclidean_distances = {}
for name, point in points.items():
    dist = np.linalg.norm(point - Q)
    euclidean_distances[name] = dist
    print(f"\n{name} = {point}")
    print(f"  Distance from Q: {dist:.4f}")

# Sort by Euclidean distance (ascending - smaller is more similar)
sorted_euclidean = sorted(euclidean_distances.items(), key=lambda x: x[1])

print("\n📊 EUCLIDEAN DISTANCE RANKING (Most to Least Similar):")
for rank, (name, dist) in enumerate(sorted_euclidean, 1):
    marker = "⭐" if rank == 1 else "  "
    print(f"  {rank}. {name}: {dist:.4f} {marker}")

# Calculate Cosine similarities
print("\n" + "="*80)
print("COSINE SIMILARITY CALCULATIONS")
print("="*80)

cosine_similarities = {}
for name, point in points.items():
    dot_product = np.dot(Q, point)
    norm_Q = np.linalg.norm(Q)
    norm_point = np.linalg.norm(point)
    similarity = dot_product / (norm_Q * norm_point)
    cosine_similarities[name] = similarity
    
    print(f"\n{name} = {point}")
    print(f"  Dot product: {dot_product:.4f}")
    print(f"  ||Q||: {norm_Q:.4f}")
    print(f"  ||{name}||: {norm_point:.4f}")
    print(f"  Cosine Similarity: {similarity:.4f}")

# Sort by Cosine similarity (descending - larger is more similar)
sorted_cosine = sorted(cosine_similarities.items(), key=lambda x: x[1], reverse=True)

print("\n📊 COSINE SIMILARITY RANKING (Most to Least Similar):")
for rank, (name, sim) in enumerate(sorted_cosine, 1):
    marker = "⭐" if rank == 1 else "  "
    print(f"  {rank}. {name}: {sim:.4f} {marker}")

# Create comparison DataFrame
results_df = pd.DataFrame({
    'Point': list(points.keys()),
    'A1': [p[0] for p in points.values()],
    'A2': [p[1] for p in points.values()],
    'Euclidean_Dist': [euclidean_distances[k] for k in points.keys()],
    'Euclidean_Rank': [next(i for i, (n, _) in enumerate(sorted_euclidean, 1) if n == k) 
                        for k in points.keys()],
    'Cosine_Sim': [cosine_similarities[k] for k in points.keys()],
    'Cosine_Rank': [next(i for i, (n, _) in enumerate(sorted_cosine, 1) if n == k) 
                     for k in points.keys()]
})

print("\n" + "="*80)
print("COMPARISON TABLE")
print("="*80)
print(results_df.to_string(index=False))

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plot 1: Scatter plot with both metrics
ax1.scatter(Q[0], Q[1], s=300, c='red', marker='*', 
           edgecolors='black', linewidth=2, label='Query Q', zorder=5)

for name, point in points.items():
    ax1.scatter(point[0], point[1], s=150, alpha=0.7, edgecolors='black', linewidth=1.5)
    ax1.annotate(name, (point[0], point[1]), 
                xytext=(5, 5), textcoords='offset points', fontsize=11, fontweight='bold')
    # Draw line from Q to point
    ax1.plot([Q[0], point[0]], [Q[1], point[1]], 'k--', alpha=0.3, linewidth=1)

ax1.set_xlabel('A1', fontsize=13, fontweight='bold')
ax1.set_ylabel('A2', fontsize=13, fontweight='bold')
ax1.set_title('2D Data Points and Query', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)

# Plot 2: Ranking comparison
x_pos = np.arange(len(points))
width = 0.35

euclidean_ranks = [results_df[results_df['Point']==name]['Euclidean_Rank'].values[0] 
                   for name in points.keys()]
cosine_ranks = [results_df[results_df['Point']==name]['Cosine_Rank'].values[0] 
                for name in points.keys()]

bars1 = ax2.bar(x_pos - width/2, euclidean_ranks, width, label='Euclidean Distance Rank', alpha=0.8)
bars2 = ax2.bar(x_pos + width/2, cosine_ranks, width, label='Cosine Similarity Rank', alpha=0.8)

ax2.set_xlabel('Points', fontsize=13, fontweight='bold')
ax2.set_ylabel('Rank (1=Most Similar)', fontsize=13, fontweight='bold')
ax2.set_title('Ranking Comparison: Euclidean vs Cosine', fontsize=14, fontweight='bold')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(list(points.keys()))
ax2.set_ylim([0, 6])
ax2.invert_yaxis()  # Invert so rank 1 is at top
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('2d_similarity_analysis.png', dpi=300, bbox_inches='tight')
print("\n✅ Visualization saved as '2d_similarity_analysis.png'")
plt.show()

print("\n" + "="*80)
```

---

## Summary and Key Takeaways

### Final Rankings

| Metric | Top 3 Most Similar | Bottom 2 Least Similar |
|--------|-------------------|------------------------|
| **Euclidean** | x1, x4, x3 | x5, x2 |
| **Cosine** | x3, x1, x4 | x2, x5 |

---

### When to Use Each Metric?

| Use Euclidean Distance When: | Use Cosine Similarity When: |
|------------------------------|----------------------------|
| Absolute position matters | Direction/proportion matters |
| Measuring spatial proximity | Comparing patterns/trends |
| Data has same scale | Data has different scales |
| Finding nearest neighbors | Text analysis, recommendations |
| Clustering geographical data | Document similarity |

---

### Key Insights

1. **Different perspectives:** Same data, different rankings based on what "similarity" means

2. **Complementary metrics:** Using both provides richer understanding

3. **Context matters:** Choice of metric depends on application domain

4. **All points are similar:** All cosine values > 0.96, showing points are in similar direction

---

**End of Question 4**
