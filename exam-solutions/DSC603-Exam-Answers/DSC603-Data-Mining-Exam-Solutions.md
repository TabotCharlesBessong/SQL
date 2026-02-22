# DSC 603 – Data Mining  
## Exam Solutions (January 2023)

**University of Buea, Faculty of Science**  
**Department: Computer Science**  
**Course Code: DSC 603**  
**Date: Thursday 05/01/2023**  
**Time: 13:00 – 14:30**

---

## Document structure

This document gives full solutions for:

1. **Question 1 (Compulsory):** Similarity measures – Euclidean distance and cosine similarity ranking  
2. **Question 2 (Elective):** Data warehousing – star schema, OLAP operations, bitmap indexing  
3. **Bitmap indexing (short):** Definition, advantages, problems  
4. **Question 3 (Elective):** Curse of dimensionality – aggregate cells and iceberg cube  

---

## Question 1 (Compulsory) — 15 marks  
### Similarity measures in two-dimensional data

**Given:**

| Point | A1   | A2   |
|-------|------|------|
| x1    | 1.5  | 1.7  |
| x2    | 2.0  | 1.9  |
| x3    | 1.6  | 1.8  |
| x4    | 1.2  | 1.5  |
| x5    | 1.5  | 1.0  |

**Query point:** \( x = (1.4,\, 1.6) \)

**Formulas:**

- **Euclidean distance:**  
  \( d(i,j) = \sqrt{(x_{i1}-x_{j1})^2 + (x_{i2}-x_{j2})^2 + \cdots + (x_{in}-x_{jn})^2} \)

- **Cosine similarity:**  
  \( s(x,y) = \frac{x^T \cdot y}{\|x\| \cdot \|y\|} \)

---

### Part 1: Euclidean distance ranking

For each database point \( x_i \), compute \( d(x, x_i) \):

\[
d(x, x_i) = \sqrt{(1.4 - x_{i1})^2 + (1.6 - x_{i2})^2}
\]

| Point | Calculation | \( d(x, x_i) \) |
|-------|-------------|------------------|
| x1 | \( \sqrt{(0.1)^2 + (0.1)^2} = \sqrt{0.02} \) | **0.141** |
| x2 | \( \sqrt{(0.6)^2 + (0.3)^2} = \sqrt{0.45} \) | **0.671** |
| x3 | \( \sqrt{(0.2)^2 + (0.2)^2} = \sqrt{0.08} \) | **0.283** |
| x4 | \( \sqrt{(0.2)^2 + (0.1)^2} = \sqrt{0.05} \) | **0.224** |
| x5 | \( \sqrt{(0.1)^2 + (0.6)^2} = \sqrt{0.37} \) | **0.608** |

**Ranking by Euclidean distance (ascending; smaller = more similar):**

1. **x1** (0.141)  
2. **x4** (0.224)  
3. **x3** (0.283)  
4. **x5** (0.608)  
5. **x2** (0.671)  

---

### Part 2: Cosine similarity ranking

\( \|x\| = \sqrt{1.4^2 + 1.6^2} = \sqrt{1.96 + 2.56} = \sqrt{4.52} \approx 2.126 \)

\( s(x, y) = \dfrac{x \cdot y}{\|x\| \cdot \|y\|} \)

| Point | \( x \cdot x_i \) | \( \|x_i\| \) | \( s(x, x_i) \) |
|-------|-------------------|---------------|------------------|
| x1 | 1.4×1.5 + 1.6×1.7 = 4.82 | \( \sqrt{5.14} \approx 2.267 \) | **0.999** |
| x2 | 2.8 + 3.04 = 5.84 | \( \sqrt{7.61} \approx 2.759 \) | **0.992** |
| x3 | 2.24 + 2.88 = 5.12 | \( \sqrt{5.80} \approx 2.408 \) | **0.999** |
| x4 | 1.68 + 2.4 = 4.08 | \( \sqrt{3.69} \approx 1.921 \) | **0.999** |
| x5 | 2.1 + 1.6 = 3.70 | \( \sqrt{3.25} \approx 1.803 \) | **0.966** |

**Ranking by cosine similarity (descending; larger = more similar):**

1. **x1** (0.999)  
2. **x3** (0.999)  
3. **x4** (0.999)  
4. **x2** (0.992)  
5. **x5** (0.966)  

---

### Summary

- **Euclidean:** x1 → x4 → x3 → x5 → x2 (emphasizes geometric closeness).  
- **Cosine:** x1, x3, x4 (tie at ~0.999) → x2 → x5 (emphasizes direction / angle).  
- x5 is last for cosine (different direction from the query) but not last for Euclidean.

---

## Question 2 (Elective) — 15 marks  
### Data warehouse: dimensions, measures, star schema, OLAP, bitmap indexing

**Scenario:**

- **Dimensions:** date, spectator, location, game  
- **Measures:** count, charge (fare paid by a spectator for a game on a given date)  
- **Spectator categories:** students, adults, seniors (each with a charge rate)  

---

### Part 2a: Star schema diagram (5 marks)

**Star schema:** one central **fact table** (events/transactions) and several **dimension tables** (date, spectator, location, game).

- **Fact table:** e.g. `Spectator_Event`  
  - Keys: `date_key`, `spectator_key`, `location_key`, `game_key`  
  - Measures: `count`, `charge`  
- **Dimension tables:**  
  - `Dim_Date`: date_key, date, year, month, day, …  
  - `Dim_Spectator`: spectator_key, category (student / adult / senior), charge_rate, …  
  - `Dim_Location`: location_key, venue_name (e.g. GM Place), city, …  
  - `Dim_Game`: game_key, game_name, sport, …

```
                    Dim_Date
                         |
                         | date_key
                         |
    Dim_Spectator ------[Fact: Spectator_Event]----- Dim_Location
    (spectator_key)      date_key, spectator_key,    (location_key)
                         location_key, game_key,
                         count, charge
                         |
                         | game_key
                         |
                    Dim_Game
```

**Text description:**

- **Fact table – Spectator_Event:**  
  `date_key` (FK), `spectator_key` (FK), `location_key` (FK), `game_key` (FK), `count`, `charge`  
- **Dim_Date:** date_key (PK), date, year, month, day  
- **Dim_Spectator:** spectator_key (PK), category (student/adult/senior), charge_rate  
- **Dim_Location:** location_key (PK), venue_name (e.g. GM Place), city, region  
- **Dim_Game:** game_key (PK), game_name, sport  

Charge is the fare paid by a spectator for a game on a given date; it can be derived from spectator category (student/adult/senior) and stored or computed.

---

### Part 2b: OLAP operations (5 marks)

**Goal:** Total charge paid by **student** spectators at **GM Place** in **2021**.

**Base cuboid:** \( [\textit{date as } D,\ \textit{spectator as } S,\ \textit{location as } L,\ \textit{game as } G] \), measure: sum(charge).

**Operations:**

1. **Slice on Date (year = 2021)**  
   Restrict the cube to the 2021 slice (e.g. all dates in 2021).  
   Result: cuboid still [D, S, L, G] but only 2021 rows.

2. **Slice on Location (venue = GM Place)**  
   Restrict to the GM Place slice.  
   Result: [D, S, L, G] with only GM Place.

3. **Slice on Spectator (category = student)**  
   Restrict to student spectators.  
   Result: [D, S, L, G] with only student.

4. **Roll-up / aggregation on dimensions not needed for the query**  
   Aggregate over **game** (and possibly date if we only need yearly total) so that the measure is **sum(charge)** for (2021, student, GM Place).  
   So we effectively reduce to a smaller cuboid, e.g. [year, spectator_category, location] or [date, spectator, location], and then read the cell (2021, student, GM Place).

**Sequence in words:**

- Start from base cuboid [D, S, L, G].  
- **Slice** on date → keep only 2021.  
- **Slice** on location → keep only GM Place.  
- **Slice** on spectator → keep only students.  
- **Roll-up** (aggregate) to get total charge (e.g. over game, and over day/month if only year is needed).  
- The result is one number: total charge paid by students at GM Place in 2021.

---

### Part 2c: Bitmap indexing in this cube (5 marks)

**Idea:** For each dimension (or important attribute), keep a **bitmap** per distinct value: one bit per row in the fact table; bit = 1 if that row has that value.

**Use in this warehouse:**

- **Dimension attributes:** date (e.g. year), spectator category (student/adult/senior), location (e.g. GM Place), game.  
- For “student spectators at GM Place in 2021” we can:  
  - AND the bitmap for “year = 2021” with the bitmap for “spectator = student” and “location = GM Place”.  
  - The result bitmap marks exactly the fact rows that satisfy the condition; then sum(charge) over those rows gives the total charge.  
- Same idea applies to other OLAP filters (slice/dice); bitmaps make multi-dimensional selection and aggregation efficient.

**Why it helps:**

- **Fast logical operations:** AND/OR of bitmaps to combine several slice conditions.  
- **Good for low–medium cardinality:** e.g. year, spectator category, venue – few distinct values, so few bitmaps.  
- **Efficient for star schema:** each dimension key or category can have a bitmap; joins and filters reduce to bitmap operations before touching the fact table heavily.

---

## Bitmap indexing (standalone) — 5 marks total

### a) What is bitmap indexing? (2 marks)

**Bitmap index:** For a column (or dimension attribute), one **bit vector** per distinct value. Each vector has one bit per row (or per tuple) in the table. The bit for value \( v \) and row \( i \) is 1 if row \( i \) has value \( v \) in that column, and 0 otherwise.

- **Structure:** One bitmap per distinct value; length = number of rows.  
- **Query:** To find rows where column = \( v \), use the bitmap for \( v \); to combine conditions (e.g. column1 = a AND column2 = b), AND the corresponding bitmaps.  
- **Use:** Common in data warehouses and OLAP for dimensions with moderate cardinality.

---

### b) Advantages and problems (3 marks)

**Advantages:**

1. **Fast logical operations:** AND, OR, NOT on bitmaps to combine multiple conditions; very fast and cache-friendly.  
2. **Space-efficient for low cardinality:** Few distinct values ⇒ few bitmaps; bits are compact.  
3. **Good for read-heavy, analytical workloads:** Typical in OLAP (aggregations, slice/dice).  
4. **Efficient for star schema:** Dimension attributes (category, year, venue) often have low cardinality; bitmap index on these speeds up filtering before joining to the fact table.

**Problems / limitations:**

1. **High cardinality:** Many distinct values (e.g. customer_id, transaction_id) ⇒ many long bitmaps; space and maintenance cost grow.  
2. **Updates:** Insert/update/delete require updating one or more bitmaps; can be costly in write-heavy systems.  
3. **Sparse bitmaps:** If a value appears in very few rows, the bitmap is mostly zeros; still stored in full unless compressed.  
4. **Not ideal for all data types:** Best for categorical or integer attributes; less natural for long text or floating-point ranges without discretization.

---

## Question 3 (Elective) — 15 marks  
### Curse of dimensionality, aggregate cells, iceberg cube

**Setting:** 5-dimensional base cuboid with **two base cells**:

- \( (a_1, a_2, a_3, a_4, a_5) \)  
- \( (a_1, a_2, b_3, b_4, b_5) \)  

So the two cells agree on dimensions 1 and 2, and differ on dimensions 3, 4, and 5.

---

### Part 3a: Define an aggregate cell (3 marks)

**Aggregate cell:** An aggregate cell is a cell in a **cuboid** that is **above** the base cuboid in the lattice (i.e. it has at least one dimension rolled up to “all” or “*”). It represents the aggregation (e.g. count, sum) of all base cells that match on the non-starred dimensions.

- **Base cell:** A cell in the base cuboid; no dimension is “*”; it corresponds to one specific combination of dimension values.  
- **Aggregate cell:** Same as above but at least one dimension is “*”; it aggregates over that dimension.  
- **Example:** \( (a_1, a_2, *, *, *) \) is an aggregate cell (dims 3, 4, 5 rolled up); it aggregates both given base cells.  
- **Example:** \( (*, *, *, *, *) \) is the apex cell (all dimensions rolled up); it aggregates the whole cube.

So: an aggregate cell is any cell in the cube lattice that is not only in the base cuboid, i.e. it has at least one “*” and holds an aggregated measure over the corresponding set of base cells.

---

### Part 3b: Number of nonempty aggregate cells (3 marks)

**Nonempty aggregate cell:** A cell (in any cuboid) whose measure (e.g. count) is ≥ 1 given the two base cells.

- The two base cells agree on dims 1 and 2 (values \( a_1, a_2 \)) and differ on dims 3, 4, 5 (e.g. \( a_3 \) vs \( b_3 \), etc.).  
- For each **cuboid** (subset of dimensions \( S \subseteq \{1,2,3,4,5\} \)), the number of distinct dimension value combinations in the data for that subset is:
  - 1 for dim 1 and dim 2 (only \( a_1 \), \( a_2 \) appear),
  - 2 for dim 3, 4, 5 (e.g. \( a_3 \) or \( b_3 \), etc.).
- So for a cuboid defined by subset \( S \), the number of cells that get at least one count is:
  \[
  \prod_{i \in S} \text{(number of distinct values in base for dimension } i) = 2^{|S \cap \{3,4,5\}|}.
  \]
- Total number of **nonempty** cells (base + all cuboids) is:
  \[
  \sum_{S \subseteq \{1,2,3,4,5\}} 2^{|S \cap \{3,4,5\}|}.
  \]
- For each \( k = |S \cap \{3,4,5\}| \), there are \( \binom{3}{k} \times 2^2 \) subsets \( S \) (choose \( k \) from \( \{3,4,5\} \), and any subset of \( \{1,2\} \)). So:
  \[
  \sum_{k=0}^{3} \binom{3}{k} \cdot 4 \cdot 2^k = 4 \bigl( 1 + 3\cdot 2 + 3\cdot 4 + 1\cdot 8 \bigr) = 4 \times 27 = \mathbf{108}.
  \]

**Answer:** There are **108** nonempty aggregate cells (including the 2 base cells and all cells in higher-level cuboids that have count ≥ 1).

---

### Part 3c: Iceberg cube (min_support = 2)

#### (i) What is an iceberg cube? (3 marks)

**Iceberg cube:** A cube in which we **materialize only cells** whose measure satisfies an **iceberg condition**, e.g. \( \texttt{HAVING count(*)} \geq \textit{min\_support} \). So we do not materialize the full cube; we keep only “above the water” (cells above the threshold). This reduces size and computation when many cells have low count (sparse, high-dimensional cubes).

---

#### (ii) Number of aggregate cells in the iceberg cube (min_support = 2) (3 marks)

With **minimum support count = 2**, we keep only cells that **aggregate both** base cells.

- The two base cells agree only on dimensions 1 and 2 (\( a_1, a_2 \)) and differ on 3, 4, 5.  
- A cell has count 2 only if both base cells are aggregated into it, i.e. the cell has “*” on dimensions 3, 4, and 5. So the only such cells are those with:
  - dim 1: \( a_1 \) or *  
  - dim 2: \( a_2 \) or *  
  - dim 3, 4, 5: *  

So the cuboids that can have a cell with count 2 are those that include only dimensions 1 and/or 2 (and star out 3,4,5). That gives:

- \( (*, *, *, *, *) \): 1 cell (apex), count = 2  
- \( (a_1, *, *, *, *) \): 1 cell, count = 2  
- \( (*, a_2, *, *, *) \): 1 cell, count = 2  
- \( (a_1, a_2, *, *, *) \): 1 cell, count = 2  

**Answer:** There are **4** aggregate cells in the iceberg cube when min_support = 2.

(If the question asks only for “aggregate” cells excluding the base, then we have 4; if base cells are included and they each have count 1, they are not in the iceberg with min_support = 2, so the iceberg cube has 4 cells.)

---

#### (iii) Show the cells (3 marks)

The four cells in the iceberg cube (count ≥ 2) are:

1. \( (*, *, *, *, *) \) — apex; count = 2  
2. \( (a_1, *, *, *, *) \) — roll-up on dims 2,3,4,5; count = 2  
3. \( (*, a_2, *, *, *) \) — roll-up on dims 1,3,4,5; count = 2  
4. \( (a_1, a_2, *, *, *) \) — roll-up on dims 3,4,5; count = 2  

Each of these aggregates both base cells \( (a_1,a_2,a_3,a_4,a_5) \) and \( (a_1,a_2,b_3,b_4,b_5) \).

---

## End of solutions

*These solutions are consistent with standard data mining and data warehousing definitions and the DSC603 course material.*
