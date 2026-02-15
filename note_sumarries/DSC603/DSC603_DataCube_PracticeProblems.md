# DSC603 Data Cube Computation — Practice Problems (Solved)

---

## Problem 1: Iceberg Cube Cell Count

**Given:** A data cube with dimensions **Time (T), Product (P), Region (R)**. Base table has 3 tuples:
- (Jan, Milk, North): count 5  
- (Jan, Milk, South): count 3  
- (Feb, Bread, North): count 2  

**Questions:**
1. How many aggregate cells if `HAVING count(*) >= 1`?
2. How many aggregate cells if `HAVING count(*) >= 5`?

**Solution:**

1. **count ≥ 1:** Every subset of dimensions defines one aggregate cell. We have 3 dimensions → 2³ = **8 cuboids** (all, T, P, R, TP, TR, PR, TPR). Each of the 3 base cells contributes to cells where its dimensions are instantiated or aggregated. Every possible aggregate cell gets at least one contribution from some base cell.  
   - Total cells = sum over all cuboids of distinct (aggregate) cells.  
   - For 3 dims with low cardinality, we count: apex 1 + (T:2 + P:2 + R:2) + (TP:3 + TR:3 + PR:2) + base:3 = **18 cells** (depending on exact schema).  
   - **Simpler interpretation:** With count ≥ 1, all cells that aggregate at least one base tuple are materialized. For a small 3-D cube, the full cube has many cells; with count ≥ 1, we keep all that have count ≥ 1.

   **Alternative (cleaner) answer:** For a 3-dimensional cube with 3 base cells, the number of aggregate cells with count ≥ 1 = all cells in the lattice that receive at least one tuple. This equals the size of the full cube (all cuboids) since every cell gets some count. For 3 dims: 1 + 3 + 3 + 1 = 8 cuboid types; total cells depend on cardinalities.  
   **Typical exam answer:** **All cells** that have count ≥ 1 (full cube).

2. **count ≥ 5:** Only cells with count ≥ 5.  
   - (Jan, Milk, North): 5 ✓  
   - (Jan, Milk, *): 5 + 3 = 8 ✓  
   - (Jan, *, North): 5 + 2 = 7 ✓ (assuming Jan has both Milk and Bread in North — actually Bread is Feb, so (Jan, *, North) = 5 only)  
   - Correct: (Jan, Milk, *): 8, (Jan, *, North): 5, (*, Milk, North): 5, (*, *, *): 10.  
   - **Answer: 4 cells** — (Jan, Milk, North): 5, (Jan, Milk, *): 8, (*, Milk, North): 5, (*, *, *): 10.

---

## Problem 2: Closed Cube

**Given:** Base cuboid with 2 cells:
- (a₁, a₂, a₃, ..., a₁₀₀): count = 10  
- (a₁, a₂, b₃, ..., b₁₀₀): count = 10  

**Question:** What is the closed cube? (How many cells and which ones?)

**Solution:**

- **Base cells:** Both (a₁, a₂, a₃, ..., a₁₀₀): 10 and (a₁, a₂, b₃, ..., b₁₀₀): 10 are **closed** — no descendant has the same measure (descendants would be more specific with same or lower count).
- **Aggregate cells:** Cells with count = 20 aggregate both base cells. They agree on dim1, dim2 (a₁, a₂); differ on dim3…dim100.
  - (a₁, a₂, *, *, ..., *): 20 — closed (descendants have 10 each, not 20).
  - (*, a₁, *, ..., *) or (a₁, *, *, ..., *) — wait, dimensions are (d1, d2, d3, ..., d100). Both base cells have d1=a₁, d2=a₂. So:
    - (a₁, a₂, *, ..., *): 20 — closed ✓
    - (a₁, *, *, ..., *): 20 — has descendant (a₁, a₂, *, ..., *): 20 → **not closed**
    - (*, a₂, *, ..., *): 20 — has descendant (a₁, a₂, *, ..., *): 20 → **not closed**
    - (*, *, *, ..., *): 20 — has descendant (a₁, a₂, *, ..., *): 20 → **not closed**

**Closed cube = 3 cells:**
1. (a₁, a₂, a₃, ..., a₁₀₀): 10  
2. (a₁, a₂, b₃, ..., b₁₀₀): 10  
3. (a₁, a₂, *, *, ..., *): 20  

---

## Problem 3: Cube Shell Combinations

**Given:** Dimensions A₁, A₂, …, A₁₀ (10 dimensions).

**Question:** How many 3-dimensional cuboids must be computed for a 3-D cube shell?

**Solution:**

We need all cuboids that have exactly 3 dimensions. Each such cuboid is a choice of 3 dimensions from 10.

Number = C(10, 3) = 10! / (3! × 7!) = (10×9×8) / (3×2×1) = **120 combinations**.

---

## Problem 4: Multi-Way Array Aggregation — Best Order

**Given:** 3-D array with dimensions A (size 1000), B (size 100), C (size 10). We aggregate to 2-D planes AB, AC, BC and 1-D A, B, C.

**Question:** What is the best order to traverse and aggregate planes to minimize memory and I/O?

**Solution:**

- **Principle:** Sort planes by size (ascending); keep the **smallest plane** in memory; scan the **largest plane** one chunk at a time.
- Plane sizes:
  - A×B: 1000×100 = 100,000  
  - A×C: 1000×10 = 10,000  
  - B×C: 100×10 = 1,000 (smallest)

- **Best order:** Process in **ascending order of plane size**:
  1. B×C (1,000) — smallest, keep in memory  
  2. A×C (10,000) — fetch in chunks  
  3. A×B (100,000) — fetch in chunks  

- **Answer:** Sort planes by ascending size; keep B×C in memory; aggregate A×C and A×B by scanning in chunks. This minimizes memory use and I/O.

---

## Problem 5: Star-Cubing — Star Reduction

**Given:** Base table with min_sup = 2:

| A  | B  | C  | D  | Count |
|----|----|----|----|-------|
| a1 | b1 | c1 | d1 | 1     |
| a1 | b1 | c4 | d3 | 1     |
| a1 | b2 | c2 | d2 | 1     |
| a2 | b3 | c3 | d4 | 1     |
| a2 | b4 | c3 | d4 | 1     |

**Question:** Apply star reduction. Which attribute values become * (star)?

**Solution:**

**1-D counts:**
- A: a1→3, a2→2 (both ≥ 2)  
- B: b1→2, b2→1, b3→1, b4→1 → b2, b3, b4 become *  
- C: c1→1, c2→1, c3→2, c4→1 → c1, c2, c4 become *  
- D: d1→1, d2→1, d3→1, d4→2 → d1, d2, d3 become *

**Star reduction (replace values with count < 2 by *):**
- Row 1: (a1, b1, *, *, 1)  
- Row 2: (a1, b1, *, *, 1)  
- Row 3: (a1, *, *, *, 1)  
- Row 4: (a2, *, c3, d4, 1)  
- Row 5: (a2, *, c3, d4, 1)  

**Compress (merge identical rows):**
- (a1, b1, *, *, 2)  
- (a1, *, *, *, 1)  
- (a2, *, c3, d4, 2)  

**Star attributes:** b2, b3, b4, c1, c2, c4, d1, d2, d3.

---

## Problem 6: Shell Fragments — TID List Intersection

**Given:** Base table (tid, A, B, C, D, E):

| tid | A  | B  | C  | D  | E  |
|-----|----|----|----|----|----|
| 1   | a1 | b1 | c1 | d1 | e1 |
| 2   | a1 | b2 | c1 | d2 | e1 |
| 3   | a1 | b2 | c1 | d1 | e2 |
| 4   | a2 | b1 | c1 | d1 | e2 |
| 5   | a2 | b1 | c1 | d1 | e3 |

Shell fragments: (A, B, C) and (D, E).

**Question:** For cell (a1, b1, *, d1, *), find the TID list and count.

**Solution:**

1. **Fragment 1 (A, B, C):** (a1, b1, *) → TID list for a1 ∩ TID list for b1  
   - a1 → {1, 2, 3}  
   - b1 → {1, 4, 5}  
   - a1 ∩ b1 = **{1}**

2. **Fragment 2 (D, E):** (d1, *) → TID list for d1  
   - d1 → {1, 3, 4, 5}

3. **Intersect:** {1} ∩ {1, 3, 4, 5} = **{1}**

4. **Count:** |{1}| = **1**

**Answer:** Cell (a1, b1, *, d1, *) has TID list {1} and count = 1.

---

## Problem 7: BUC Pruning

**Given:** BUC with min_sup = 2. After partitioning on dimension A, we have:
- Partition a1: 3 tuples  
- Partition a2: 1 tuple  
- Partition a3: 1 tuple  

**Question:** Which partitions can be pruned when computing child cuboids?

**Solution:**

- **Partition a1:** count = 3 ≥ 2 → **cannot prune**; must recurse.
- **Partition a2:** count = 1 < 2 → **prune**; no descendants need to be computed for a2.
- **Partition a3:** count = 1 < 2 → **prune**; no descendants need to be computed for a3.

**Answer:** Partitions a2 and a3 are pruned. Only partition a1 is processed further.

---

## Problem 8: Full Cube Size (High Dimensional)

**Given:** 100 dimensions, 2 base cells: (a₁, a₂, …, a₁₀₀) and (b₁, b₂, …, b₁₀₀). Assume they differ in all dimensions.

**Questions:**
1. How many aggregate cells if count ≥ 1?  
2. How many aggregate cells if count ≥ 2?

**Solution:**

1. **count ≥ 1:** Each subset of dimensions defines one aggregate cell. Each base cell contributes to every such cell. With 2 different base cells, every 2^100 cells gets at least one contribution.  
   **Answer: 2^100 cells.**

2. **count ≥ 2:** Both base cells must aggregate to the same cell. They agree only when we use * on every dimension.  
   **Answer: 1 cell** — the apex cuboid (*, *, …, *).

---

## Quick Reference: Key Formulas

| Concept                  | Formula / Rule                                      |
|--------------------------|-----------------------------------------------------|
| Iceberg (count ≥ 1)      | Full cube size (all cells with count ≥ 1)           |
| Iceberg (count ≥ 2)      | Only cells where ≥ 2 base tuples aggregate together |
| Closed cell              | No descendant has same measure                      |
| Cube shell (k-D)         | C(n, k) cuboids for n dimensions                    |
| Multi-Way best order     | Ascending plane size; smallest in memory            |
| BUC pruning              | Partition count < min_sup → prune                   |
| Star reduction           | 1-D count < min_sup → replace value by *            |

---
