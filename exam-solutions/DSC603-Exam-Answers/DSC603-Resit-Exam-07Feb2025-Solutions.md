# DSC 603 – Data Mining  
## Resit Examination Solutions (07 Feb 2025)

**University of Buea, Faculty of Science**  
**Department:** Computer Science  
**Course Code:** DSC603 – Data Mining  
**Exam:** First Semester Resit 2024/2025  
**Date:** 07/02/2025  

---

## Section A

### Question 1 (2 + 5 + 7 + 6 = 20 marks) — Frequent Pattern Mining

#### (a) Objective of frequent pattern mining (2 marks)

To **discover itemsets / patterns that occur frequently** in a large dataset (above a given **minimum support**), in order to **find associations and correlations** (e.g. in market-basket data) that can be used for tasks like recommendation, prediction, and decision support.

---

#### (b) Apriori property and its benefit (5 marks)

- **Apriori property:**  
  If an itemset is **frequent**, then **all of its non‑empty subsets are also frequent**.  
  Equivalently, if an itemset is **infrequent**, then **all of its supersets must be infrequent**.

- **Benefit in Apriori algorithm:**  
  - Provides a **pruning rule**: when generating candidates, **any candidate whose subset is not frequent is discarded**, so we avoid counting its support.  
  - This **reduces the number of candidates** and **database scans**, making frequent‑itemset mining **much more efficient and scalable** on large datasets.

---

#### (c) Apriori on the given transactions (min_support = 40%, min_conf = 70%) (7 marks)

Transactions (5 total):

1. {Bread, Butter, Milk}  
2. {Bread, Butter}  
3. {Beer, Cookies, Diapers}  
4. {Milk, Diapers, Bread, Butter}  
5. {Beer, Diapers}

Minimum support = 40% of 5 = **2 transactions**.

**Step 1 – C₁ and L₁**

Supports:

- Bread: 3; Butter: 3; Milk: 2; Beer: 2; Diapers: 3; Cookies: 1

Frequent 1‑itemsets (L₁, support ≥ 2):

- **L₁ = {Bread, Butter, Milk, Beer, Diapers}**

---

**Step 2 – C₂ and L₂**

All 2‑item candidates from L₁ and their supports:

- {Bread, Butter}: 3  
- {Bread, Milk}: 2  
- {Bread, Beer}: 0  
- {Bread, Diapers}: 1  
- {Butter, Milk}: 2  
- {Butter, Beer}: 0  
- {Butter, Diapers}: 1  
- {Milk, Beer}: 0  
- {Milk, Diapers}: 1  
- {Beer, Diapers}: 2  

Frequent 2‑itemsets:

- **L₂ = { {Bread, Butter} (3), {Bread, Milk} (2), {Butter, Milk} (2), {Beer, Diapers} (2) }**

---

**Step 3 – C₃ and L₃**

- Join step: from pairs in L₂ we get candidate  
  **C₃ = {Bread, Butter, Milk}**.  
- Support({Bread, Butter, Milk}) = 2 (T1, T4) → frequent.

Thus:

- **L₃ = { {Bread, Butter, Milk} (2) }**

No 4‑item candidates can be generated from a single 3‑itemset, so Apriori stops.

**All frequent itemsets:**

- **Level 1:** {Bread}, {Butter}, {Milk}, {Beer}, {Diapers}  
- **Level 2:** {Bread, Butter}, {Bread, Milk}, {Butter, Milk}, {Beer, Diapers}  
- **Level 3:** {Bread, Butter, Milk}

Largest frequent itemset: **{Bread, Butter, Milk}**.

---

#### (d) Association rules with one item on the RHS (min_conf = 70%) (6 marks)

Use frequent 2‑ and 3‑itemsets.

Supports (from part (c)):

- supp(Bread) = 3; supp(Butter) = 3; supp(Milk) = 2; supp(Beer) = 2; supp(Diapers) = 3  
- supp(Bread, Butter) = 3; supp(Bread, Milk) = 2; supp(Butter, Milk) = 2; supp(Beer, Diapers) = 2  
- supp(Bread, Butter, Milk) = 2

**Rules from 2‑itemsets**

- From {Bread, Butter}:  
  - Bread → Butter: 3/3 = **100%** ✔  
  - Butter → Bread: 3/3 = **100%** ✔

- From {Bread, Milk}:  
  - Bread → Milk: 2/3 ≈ 66.7% ✘  
  - Milk → Bread: 2/2 = **100%** ✔

- From {Butter, Milk}:  
  - Butter → Milk: 2/3 ≈ 66.7% ✘  
  - Milk → Butter: 2/2 = **100%** ✔

- From {Beer, Diapers}:  
  - Beer → Diapers: 2/2 = **100%** ✔  
  - Diapers → Beer: 2/3 ≈ 66.7% ✘

**Rules from 3‑itemset {Bread, Butter, Milk}**

- Bread → {Butter, Milk}: 2/3 ≈ 66.7% ✘  
- Butter → {Bread, Milk}: 2/3 ≈ 66.7% ✘  
- Milk → {Bread, Butter}: 2/2 = **100%** ✔

**Strong association rules (confidence ≥ 70%):**

1. Bread → Butter  
2. Butter → Bread  
3. Milk → Bread  
4. Milk → Butter  
5. Beer → Diapers  
6. Milk → Bread, Butter

---

## Question 2 (3 + 2 + 3 + 8 = 16 marks) — Clustering

#### (a) Hierarchical agglomerative clustering (3 marks)

Points: {2, 4, 7, 8, 12, 14}; after three iterations clusters are  
C₁ = {2, 4}, C₂ = {7, 8}, C₃ = {12, 14}.

1. **Single‑link distance(C₁, C₂)**  
   Distances between all pairs: |2−7|=5, |2−8|=6, |4−7|=3, |4−8|=4 → **min = 3**.

2. **Complete‑link distance(C₁, C₂)**  
   Same distances → **max = 6**.

3. **Next merge under single linkage**  
   d(C₁,C₂)=3; d(C₁,C₃)=8; d(C₂,C₃)=4 → smallest is 3 → **C₁ and C₂ merge next**.

---

#### (b) Three clusters from the dendrogram (2 marks)

Cut the dendrogram at a level that yields **3 main branches**:

- **Cluster 1:** {BA, NA}  
- **Cluster 2:** {RM, FI}  
- **Cluster 3:** {MI, TO}

---

#### (c) k‑means cluster centres after first iteration (3 marks)

Given points:  
P1(0,6), P2(6,0), P3(2,2), P4(4,4), P5(6,6), P6(5,5), P7(7,7)  
After first iteration:

- C₁ = {P1, P2}  
- C₂ = {P3, P4, P5}  
- C₃ = {P6, P7}

**Centers (means):**

- **C₁:** ((0+6)/2, (6+0)/2) = **(3, 3)**  
- **C₂:** ((2+4+6)/3, (2+4+6)/3) = **(4, 4)**  
- **C₃:** ((5+7)/2, (5+7)/2) = **(6, 6)**

---

#### (d) Next iteration of k‑means (8 marks)

Using centers C₁(3,3), C₂(4,4), C₃(6,6):

| Point | C₁ (3,3) | C₂ (4,4) | C₃ (6,6) | Closest cluster |
|-------|----------|----------|----------|-----------------|
| P1(0,6) | 18 | 20 | 36 | C₁ |
| P2(6,0) | 18 | 20 | 36 | C₁ |
| P3(2,2) | 2  | 8  | 32 | C₁ |
| P4(4,4) | 2  | 0  | 8  | C₂ |
| P5(6,6) | 18 | 8  | 0  | C₃ |
| P6(5,5) | 8  | 2  | 2  | C₂ (tie broken in favour of C₂) |
| P7(7,7) | 32 | 18 | 2  | C₃ |

**Clusters after this iteration:**

- **C₁ = {P1, P2, P3}**  
- **C₂ = {P4, P6}**  
- **C₃ = {P5, P7}**

---

## Section B

### Question 3 (20 marks) — Data Mining and Data Warehousing

#### (a) Differentiate data mining and data warehousing (3 marks)

- **Data warehousing:**  
  - Centralized process of **collecting, cleaning, integrating, and storing historical data** from multiple sources in a **data warehouse** for decision support.  
  - Focus on **data storage, integration, and organization** (ETL, schema design).  
  - Output: an **integrated repository** of subject‑oriented, time‑variant, non‑volatile data.

- **Data mining:**  
  - Process of **discovering patterns, rules, and models** from (often warehouse) data using algorithms (classification, clustering, association rules, etc.).  
  - Focus on **pattern discovery and knowledge extraction**.  
  - Output: **patterns, rules, and predictive models**.

---

#### (b) Concepts (3 marks)

**(i) Data warehouse vs data mart**

- **Data warehouse:** Enterprise‑wide, large, integrates data from **many operational sources**, serves whole organization.  
- **Data mart:** Smaller, **department‑level** subset (e.g. sales, marketing), focused on one subject area, often derived from the warehouse.

**(ii) Base cuboid vs apex cuboid**

- **Base cuboid:** Lowest level of aggregation in a data cube; all dimensions at their **detail level** (largest cuboid).  
- **Apex cuboid:** Highest level of aggregation; all dimensions at the **ALL** level (e.g. “total sales over all products, locations, times”) — usually a **single cell**.

**(iii) Dimension vs fact**

- **Dimension:** Descriptive attribute used to **slice, dice, and group** facts (e.g. Time, Location, Product).  
- **Fact:** Numerical **measure** to be analyzed (e.g. sales amount, quantity); stored in the fact table and interpreted in the context of dimensions.

---

#### (c) Three main forms of multidimensional data model (6 marks)

1. **Star schema**  
   - One central **fact table** linked to several **denormalized dimension tables** (star shape).  
   - Simple structure, few joins, **fast queries**, but more redundancy.

2. **Snowflake schema**  
   - Fact table + **normalized dimension tables** (dimensions split into sub‑tables).  
   - Less redundancy and better integrity, but **more joins** and more complex.

3. **Fact constellation (galaxy) schema**  
   - **Multiple fact tables** share common dimensions.  
   - Supports multiple related business processes but is **most complex** to design and query.

---

#### (d) Four main characteristics of a data warehouse (2 marks)

According to the classic definition, a data warehouse is:

1. **Subject‑oriented** – organized around key subjects (customer, product, sales).  
2. **Integrated** – data from different sources is made **consistent** (naming, encoding, units).  
3. **Time‑variant** – keeps **historical data** (e.g. 5–10 years) with explicit/implicit time element.  
4. **Non‑volatile** – data is **stable**: mainly **loaded and read**, not updated transaction‑by‑transaction.

---

#### (e) Difference between OLTP and OLAP (6 marks)

| Aspect | **OLTP** (On‑Line Transaction Processing) | **OLAP** (On‑Line Analytical Processing) |
|--------|------------------------------------------|-------------------------------------------|
| **Purpose** | Run day‑to‑day operations | Support analysis and decision‑making |
| **Data** | Current, detailed, highly normalized | Historical, summarized, often star/snowflake |
| **Workload** | Many short UPDATE/INSERT/DELETE transactions | Fewer, complex SELECT queries with aggregations |
| **Users** | Clerks, operational staff | Analysts, managers, executives |
| **Response time** | Very fast (ms) | Seconds–minutes acceptable |
| **Updates** | Continuous, real‑time | Periodic bulk loads (ETL), mostly read‑only |

OLTP systems **capture and update** operational data; OLAP systems **analyze** integrated historical data (often from a warehouse) for business intelligence.

---

### Question 4 (15 marks) — Decision Tree Construction

Given attributes **time, gender, area** and target **risk (low, high)** with the 8 training examples, using **information gain** we obtain:

1. **Root entropy:** H(T) = 1.0 (4 low, 4 high).  
2. **Information gains at root:** IG(time) = 0.062, IG(gender) = 0.049, IG(area) = 0.549 → highest for **area**, so root = area.

**Final learned tree (one possible form):**

```text
                    [area]
                   /      \
            urban /        \ rural
                /          \
             [low]         [time]
             (leaf)      /    |    \
                       1-2   2-7   >7
                      /       |      \
                  [high]   [high]   [gender]
                                /        \
                           female        male
                            /             \
                        [low]           [high]
```

**Equivalent decision rules:**

1. IF area = urban THEN risk = low  
2. IF area = rural AND time = 1–2 THEN risk = high  
3. IF area = rural AND time = 2–7 THEN risk = high  
4. IF area = rural AND time = >7 AND gender = female THEN risk = low  
5. IF area = rural AND time = >7 AND gender = male THEN risk = high  

These rules correctly classify all 8 training examples.

---

**End of solutions**

