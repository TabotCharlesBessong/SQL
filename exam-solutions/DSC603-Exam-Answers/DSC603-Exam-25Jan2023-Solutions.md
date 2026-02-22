# DSC 603 – Data Mining  
## Exam Solutions (25 January 2023)

**University of Buea, Faculty of Science**  
**Department: Computer Science**  
**Course Code: DSC 603**  
**Date: 25/01/2023**  
**Time: 3 Hours (08:00–11:00)**  
**Total: 70 marks (attempt all questions)**

---

## Question 1 — Data Pre-processing (18 marks)

### Part a) State 3 reasons why data cleaning is important (3 marks)

1. **To remove redundancy** — Duplicate or repeated data can bias analysis and waste storage; cleaning identifies and reduces redundancy.  
2. **To ensure completeness** — Missing values can make models unreliable; cleaning handles missing data (e.g. by filling, imputation, or flagging).  
3. **To ensure consistency** — Inconsistent encodings, units, or formats (e.g. “M” vs “Male”) can invalidate mining; cleaning standardizes and reconciles data.

---

### Part b) Data integration

#### (i) State the objective of data integration (1 mark)

**Objective:** To combine data from **multiple sources** (databases, files, systems) into a **single, unified** representation so that mining and analysis can be performed over one consistent dataset.

#### (ii) Two categories of redundant data in data preprocessing (2 marks)

1. **Tuple / record-level redundancy** — The same or very similar real-world entity appears in multiple records (e.g. duplicate customers). Detected by key or similarity matching; handled by merging or deleting duplicates.  
2. **Attribute / dimension-level redundancy** — Two or more attributes carry the same or highly correlated information (e.g. age and date_of_birth). Detected by correlation analysis or dependency analysis; handled by dropping or merging redundant attributes.

#### (iii) Tests and data types for correlation analysis to detect redundant data (1 mark)

- **Numeric attributes:** Use **Pearson correlation coefficient** (or similar). Tests: correlation test (e.g. t-test on correlation).  
- **Categorical / nominal attributes:** Use **Chi-square (χ²) test of independence**. If the test shows dependence, the attributes may be redundant.  
- **Data types:** Correlation analysis is applied to **numeric** data; **Chi-square** is applied to **categorical** (nominal) data.

---

### Part c) Data reduction

#### (i) State the need for data reduction (3 marks)

Data reduction is needed to:

- **Reduce storage and I/O** — Smaller datasets are cheaper to store and faster to load.  
- **Save time** — Mining algorithms run faster on reduced data while still preserving the main structure.  
- **Reduce curse of dimensionality** — Fewer dimensions or fewer objects can improve model quality and interpretability.  
- **Keep only the most relevant information** — Noise and irrelevant dimensions/objects can be dropped or compressed.

#### (ii) Objective of each data reduction technique (3 marks)

- **Dimensionality reduction:** To **reduce the number of attributes (features)** while preserving as much useful information as possible (e.g. via feature selection or feature extraction), so that models are simpler and less prone to overfitting.  
- **Numerosity reduction:** To **reduce the number of data objects (tuples)** by replacing them with a smaller representation (e.g. sampling, clustering, or parametric models), possibly with **lossless** (exact reconstruction) or **lossy** (approximate) compression.

#### (iii) Curse of dimensionality and two approaches (1 + 4 marks)

**(iii-1) Curse of dimensionality**

As the **number of dimensions (attributes)** increases, data become increasingly **sparse** in the feature space: distances between points become similar, density estimates become unreliable, and learning (e.g. classification, clustering) becomes harder and more expensive. This is the “curse of dimensionality.”

**(iii-2)**

- **Wavelet transforms:** A signal (e.g. a row or a dimension) is decomposed into **wavelet coefficients** at different scales. **Few coefficients** (e.g. the largest ones) are kept and the rest are set to zero, giving a **compressed representation**. Good for **multiresolution** and **noise reduction**; often used for signal and image compression before mining.  
- **Principal Components Analysis (PCA):** PCA finds **linear combinations** of the original attributes (principal components) that capture the **maximum variance** in the data. By keeping only the first few components, we **reduce dimensions** with minimal loss of variance. The result is a **lower-dimensional**, uncorrelated representation of the data, useful for visualization and as input to other mining algorithms.

---

## Question 2 — Association Rules Mining (20 marks)

### Part a) Objective of association rules mining (2 marks)

**Objective:** To discover **frequent patterns** (frequent itemsets) and **association rules** that express how items (or attributes) **co-occur** in data (e.g. market baskets), so that we can find relationships such as “if customers buy X they often buy Y” (with **support** and **confidence**).

---

### Part b) Apriori property and its benefit (4 marks)

**Apriori property:** If an itemset is **frequent**, then **all its non-empty subsets** are also frequent. Equivalently: if **any** subset of an itemset is **infrequent**, then that itemset is infrequent.

**Benefit in the Apriori algorithm:** The algorithm generates candidates of size \(k\) only from **frequent itemsets of size \(k-1\)** (L_{k-1}). Any itemset that has an infrequent subset is **never generated** as a candidate. This **prunes** a huge number of candidates and makes the search feasible on large transaction databases.

---

### Part c) Apriori: candidates and frequent itemsets (8 marks)

**Given:** 5 transactions; **min_support = 40%** ⇒ minimum count = 2.

**Transactions:**

| TID | Items |
|-----|--------|
| 1   | Bread, Butter, Milk |
| 2   | Bread, Butter |
| 3   | Beer, Cookies, Diapers |
| 4   | Milk, Diapers, Bread, Butter |
| 5   | Beer, Diapers |

**1-itemsets (from given support counts):**

| Itemset | Support | Frequent? |
|---------|--------|-----------|
| {Bread}   | 3 | ✓ |
| {Butter}  | 3 | ✓ |
| {Milk}    | 2 | ✓ |
| {Beer}    | 2 | ✓ |
| {Cookies} | 1 | ✗ |
| {Diapers} | 3 | ✓ |

**L₁ =** {Bread}, {Butter}, {Milk}, {Beer}, {Diapers}

**C₂ and L₂:**

| Candidate | Transactions | Count | In L₂? |
|-----------|----------------|-------|--------|
| {Bread, Butter}   | 1, 2, 4 | 3 | ✓ |
| {Bread, Milk}     | 1, 4    | 2 | ✓ |
| {Bread, Beer}     | —       | 0 | ✗ |
| {Bread, Diapers}  | 4       | 1 | ✗ |
| {Butter, Milk}    | 1, 4    | 2 | ✓ |
| {Butter, Beer}    | —       | 0 | ✗ |
| {Butter, Diapers} | 4       | 1 | ✗ |
| {Milk, Beer}      | —       | 0 | ✗ |
| {Milk, Diapers}   | 4       | 1 | ✗ |
| {Beer, Diapers}   | 3, 5    | 2 | ✓ |

**L₂ =** {Bread, Butter}, {Bread, Milk}, {Butter, Milk}, {Beer, Diapers}

**C₃ (join L₂):** Only one 3-itemset possible from L₂: **{Bread, Butter, Milk}**

| Candidate | Transactions | Count | In L₃? |
|-----------|----------------|-------|--------|
| {Bread, Butter, Milk} | 1, 4 | 2 | ✓ |

**L₃ =** {Bread, Butter, Milk}. No C₄ (no 4-itemset from L₃).

**Largest frequent itemsets:** **{Bread, Butter, Milk}** (and all its subsets in L₁, L₂).

---

### Part d) Association rules and strong rules (6 marks)

**min_confidence = 70%.**

**Rules from 2-itemsets:**

| Rule | Support(A∪B) | Support(A) | Confidence |
|------|----------------|------------|------------|
| Bread → Butter | 3 | 3 | 3/3 = **100%** ✓ |
| Butter → Bread | 3 | 3 | **100%** ✓ |
| Bread → Milk | 2 | 3 | 66.7% |
| Milk → Bread | 2 | 2 | **100%** ✓ |
| Butter → Milk | 2 | 3 | 66.7% |
| Milk → Butter | 2 | 2 | **100%** ✓ |
| Beer → Diapers | 2 | 2 | **100%** ✓ |
| Diapers → Beer | 2 | 3 | 66.7% |

**Rules from 3-itemset {Bread, Butter, Milk}:**

| Rule | Confidence | Strong? |
|------|------------|--------|
| Bread → Butter ∧ Milk | 2/3 ≈ 66.7% | No |
| Butter → Bread ∧ Milk | 2/3 ≈ 66.7% | No |
| Milk → Bread ∧ Butter | 2/2 = **100%** ✓ | Yes |
| Bread ∧ Butter → Milk | 2/3 ≈ 66.7% | No |
| Bread ∧ Milk → Butter | 2/2 = **100%** ✓ | Yes |
| Butter ∧ Milk → Bread | 2/2 = **100%** ✓ | Yes |

**All strong association rules (confidence ≥ 70%):**

1. Bread → Butter (100%)  
2. Butter → Bread (100%)  
3. Milk → Bread (100%)  
4. Milk → Butter (100%)  
5. Beer → Diapers (100%)  
6. Milk → Bread ∧ Butter (100%)  
7. Bread ∧ Milk → Butter (100%)  
8. Butter ∧ Milk → Bread (100%)  

---

## Question 3 — Decision Tree and Bayesian Classifier (18 marks)

### Part a) Decision tree (Oak vs Pine) using Information Gain

**Training data (Density, Grain, Hardness → Class):**

| # | Density | Grain | Hardness | Class |
|---|---------|-------|----------|--------|
| 1 | Heavy | Small | Hard | Oak |
| 2 | Heavy | Large | Hard | Oak |
| 3 | Heavy | Small | Hard | Oak |
| 4 | Light | Large | Soft | Oak |
| 5 | Light | Large | Hard | Pine |
| 6 | Heavy | Small | Soft | Pine |
| 7 | Heavy | Large | Soft | Pine |
| 8 | Heavy | Small | Soft | Pine |

**Formulas:**  
\( \mathrm{Info}(D) = -\sum p_i \log_2(p_i) \),  
\( \mathrm{Info}_A(D) = \sum \frac{|D_j|}{|D|} \mathrm{Info}(D_j) \),  
\( \mathrm{Gain}(A) = \mathrm{Info}(D) - \mathrm{Info}_A(D) \).

**Step 1 — Root:** D has 4 Oak, 4 Pine ⇒ \(\mathrm{Info}(D) = 1\).

- **Density:** Heavy (6): 3 Oak, 3 Pine ⇒ Info = 1; Light (2): 1 Oak, 1 Pine ⇒ Info = 1.  
  \(\mathrm{Info}_{\mathrm{Density}}(D) = 1\) ⇒ Gain(Density) = 0.  
- **Grain:** Small (4): 2 Oak, 2 Pine; Large (4): 2 Oak, 2 Pine ⇒ \(\mathrm{Info}_{\mathrm{Grain}}(D) = 1\) ⇒ Gain(Grain) = 0.  
- **Hardness:** Hard (4): 3 Oak, 1 Pine; Soft (4): 1 Oak, 3 Pine.  
  \(\mathrm{Info}(\mathrm{Hard}) = -\frac{3}{4}\log_2\frac{3}{4} - \frac{1}{4}\log_2\frac{1}{4} \approx 0.811\). Same for Soft.  
  \(\mathrm{Info}_{\mathrm{Hardness}}(D) \approx 0.811\) ⇒ **Gain(Hardness) ≈ 0.189** (maximum).

**Root = Hardness.**

**Step 2 — Hardness = Hard** (examples 1, 2, 3, 5): 3 Oak, 1 Pine.

- Density: Heavy (1,2,3) → 3 Oak; Light (5) → 1 Pine ⇒ Info = 0 ⇒ **Gain = 0.811**.  
- Grain: Small (1,3) → 2 Oak; Large (2,5) → 1 Oak, 1 Pine ⇒ Info = 0.5 ⇒ Gain = 0.311.  
⇒ Split on **Density**: Heavy → **Oak**, Light → **Pine**.

**Step 3 — Hardness = Soft** (examples 4, 6, 7, 8): 1 Oak, 3 Pine.

- Density: Heavy (6,7,8) → 3 Pine; Light (4) → 1 Oak ⇒ Info = 0 ⇒ **Gain = 0.811**.  
⇒ Split on **Density**: Heavy → **Pine**, Light → **Oak**.

**Decision tree (text):**

```
                    [Hardness]
                    /        \
              Hard /          \ Soft
                  /            \
            [Density]        [Density]
            /     \            /     \
      Heavy/       \Light  Heavy/       \Light
          /         \          /         \
       Oak         Pine     Pine         Oak
```

**(ii) Classification rules**

1. IF Hardness = Hard AND Density = Heavy THEN Class = Oak.  
2. IF Hardness = Hard AND Density = Light THEN Class = Pine.  
3. IF Hardness = Soft AND Density = Heavy THEN Class = Pine.  
4. IF Hardness = Soft AND Density = Light THEN Class = Oak.

---

### Part b) Bayesian classifier (Dogs vs Cats)

**(i) What X and Cᵢ represent**

- **X** is the **feature vector** (description of an instance), e.g. (Sound, Fur, Colour).  
- **Cᵢ** is the **i-th class** (e.g. Dog or Cat).

**(ii) What a Bayesian classifier seeks to do**

It **assigns** the instance **X to the class Cᵢ** that has the **highest posterior probability** P(Cᵢ|X), i.e. it chooses the most probable class given the observed attributes.

**(iii) Naive Bayesian assumption and simplification**

**Assumption:** Attributes are **conditionally independent** given the class. So  
\( P(X|C_i) = P(x_1,x_2,\ldots,x_n|C_i) = \prod_k P(x_k|C_i) \).

**Simplification:** We do **not** need to estimate the full joint \( P(x_1,\ldots,x_n|C_i) \), only the **per-attribute conditional probabilities** \( P(x_k|C_i) \), which are easier to estimate from counts and avoid data sparsity.

**(iv) Probabilities from training data**

| P(·) | Value |
|------|--------|
| P(Dog) | 4/8 = **1/2** |
| P(Cat) | 4/8 = **1/2** |
| P(Sound=Meow \| Dog) | 1/4 |
| P(Sound=Bark \| Dog) | 3/4 |
| P(Fur=Coarse \| Dog) | 3/4 |
| P(Fur=Fine \| Dog) | 1/4 |
| P(Colour=Brown \| Dog) | 2/4 = 1/2 |
| P(Colour=Black \| Dog) | 2/4 = 1/2 |
| P(Sound=Meow \| Cat) | 3/4 |
| P(Sound=Bark \| Cat) | 1/4 |
| P(Fur=Coarse \| Cat) | 1/4 |
| P(Fur=Fine \| Cat) | 3/4 |
| P(Colour=Brown \| Cat) | 2/4 = 1/2 |
| P(Colour=Black \| Cat) | 2/4 = 1/2 |

**(v) Classify X = (Sound=Bark, Fur=Coarse, Colour=Brown)**

\( P(X|Dog) = P(Bark|Dog)\,P(Coarse|Dog)\,P(Brown|Dog) = \frac{3}{4}\cdot\frac{3}{4}\cdot\frac{1}{2} = \frac{9}{32} \).  
\( P(X|Cat) = P(Bark|Cat)\,P(Coarse|Cat)\,P(Brown|Cat) = \frac{1}{4}\cdot\frac{1}{4}\cdot\frac{1}{2} = \frac{1}{32} \).

\( P(Dog|X) \propto \frac{9}{32}\cdot\frac{1}{2} = \frac{9}{64} \),  
\( P(Cat|X) \propto \frac{1}{32}\cdot\frac{1}{2} = \frac{1}{64} \).

So **P(Dog|X) > P(Cat|X)** ⇒ **Class = Dog.**

---

## Question 4 — Data Warehousing and OLAP (20 marks, 4 each)

### 1. What is a Data Warehouse? Difference from a database (4 marks)

**Data warehouse:** A **subject-oriented**, **integrated**, **time-variant**, **nonvolatile** collection of data used to support **management decision-making**. It is built by integrating data from multiple operational sources and is optimized for **analysis and reporting**, not day-to-day transactions.

**Differences (warehouse vs database):**

| Aspect | Database (operational) | Data warehouse |
|--------|------------------------|------------------|
| Purpose | Day-to-day transactions (OLTP) | Analysis, reporting, decision support (OLAP) |
| Data | Current, detailed, frequently updated | Historical, summarized, rarely updated |
| Design | Normalized, application-oriented | Denormalized, subject-oriented (e.g. sales, customer) |
| Users | Clerks, operational staff | Analysts, managers |
| Queries | Many small, simple reads/writes | Fewer, complex analytical queries |
| Size/usage | MB–GB, high transaction throughput | GB–TB, query throughput |

---

### 2. What is a warehouse schema? Star schema (4 marks)

**Warehouse schema:** The **logical structure** (tables, dimensions, facts, relationships) used to organize and store data in the data warehouse. Common types: star, snowflake, fact constellation.

**Star schema:** One **fact table** at the centre containing **measures** (e.g. sales amount, quantity) and **foreign keys** to **dimension tables**. Each **dimension table** (e.g. time, product, location, customer) is **denormalized** and linked directly to the fact table. When drawn, the fact table is in the middle and dimensions radiate out like a star. Benefits: simple queries, fast joins, and intuitive model for OLAP.

---

### 3. Phases of data warehouse architecture (4 marks)

Typical phases:

1. **Data sources** — Operational DBs, external systems, files.  
2. **Extract** — Data is **extracted** from sources.  
3. **Transform** — **Cleaning**, integration, conversion (e.g. units, codes), aggregation.  
4. **Load** — Loaded into the warehouse (full or incremental).  
5. **Storage** — Warehouse DB (and possibly data marts).  
6. **Metadata** — Definitions, lineage, refresh info.  
7. **Access / presentation** — OLAP servers, reporting tools, front-end applications for querying and analysis.

(Can be described as ETL + storage + metadata + front-end.)

---

### 4. Bitmap indexing vs B-tree indexing in the data warehouse (4 marks)

**Bitmap index:** One **bit vector per distinct value** of the indexed column; bit \(i\) = 1 if row \(i\) has that value. **Good for:** low–medium cardinality (e.g. category, year), **read-heavy** OLAP, and combining several conditions with AND/OR. **Limitation:** high cardinality and frequent updates can be costly.

**B-tree index:** A **balanced tree** on key values; supports range queries and ordered access. **Good for:** unique or high-cardinality attributes (e.g. IDs, timestamps), point and range lookups. **Limitation:** less efficient than bitmaps for multi-predicate AND/OR on categorical dimensions in OLAP.

In a warehouse, **bitmaps** are often used on **dimension attributes** in star schemas for fast slice/dice; **B-trees** are used for **primary/foreign keys** and **range** filters.

---

### 5. What is OLAP? How is OLAP used in data mining? (4 marks)

**OLAP (On-Line Analytical Processing):** Technology that allows users to **interactively analyze multidimensional data** (e.g. cubes) using operations such as **roll-up**, **drill-down**, **slice**, **dice**, and **pivot**. Data are organized by dimensions and measures; OLAP provides fast aggregation and exploration.

**Use in data mining:**

- **Data preparation:** OLAP helps **select** and **aggregate** the right subset of data (e.g. by region, time) for mining.  
- **Exploration:** Analysts **explore** summaries and drill down to find interesting regions or time periods before applying mining.  
- **Integration:** Mining can run **on top of** the warehouse/OLAP layer (e.g. mine patterns in a cube or in cube materializations).  
- **Interpretation:** OLAP is used to **visualize and drill** into mining results (e.g. rules or clusters) in the context of dimensions and measures.

---

*End of solutions for the 25 January 2023 exam.*
