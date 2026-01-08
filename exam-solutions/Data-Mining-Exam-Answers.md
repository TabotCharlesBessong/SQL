# Data Mining Exam Answers
**University of Buea, Department of Computer Science**  
**First Semester Resit Examination 2024/2025**  
**Course Code: DSC603 - Data Mining**  
**Master's Level (MIST)**  
**Date: 7/02/2025**

---

## SECTION A

### QUESTION 1 (2+5+7+6 = 20 marks)

#### (a) State the objective of frequent patterns mining. (2 marks)

**Answer:**

The objective of **frequent pattern mining** is to discover patterns that appear frequently in a dataset. Specifically:

- **Identify itemsets, subsequences, or substructures** that occur with a frequency greater than or equal to a user-specified minimum support threshold
- **Find associations and correlations** among items in transactional databases or other data repositories
- **Discover regularities** in data that can be used for:
  - Market basket analysis
  - Association rule generation
  - Sequential pattern discovery
  - Structural pattern mining
- **Extract knowledge** about co-occurrence relationships that can support decision-making, recommendation systems, and predictive analytics

The core goal is to find patterns that are statistically significant and occur frequently enough to be meaningful for analysis and decision-making.

---

#### (b) State the Apriori property and explain its benefit in the context of the Apriori Algorithm for frequent patterns. (5 marks)

**Answer:**

**Apriori Property:**

**"If an itemset is frequent, then all of its subsets must also be frequent. Conversely, if an itemset is infrequent, then all of its supersets must also be infrequent."**

**Mathematical Formulation:**
- If itemset X is frequent (support(X) ≥ min_support), then ∀ Y ⊆ X, Y is also frequent
- If itemset X is infrequent (support(X) < min_support), then ∀ Z where X ⊆ Z, Z is also infrequent

**Benefits in the Apriori Algorithm:**

1. **Pruning Strategy (Candidate Generation Reduction):**
   - Before counting support, the algorithm can **prune candidate itemsets** whose subsets are not frequent
   - This dramatically **reduces the number of candidate itemsets** that need to be evaluated
   - Only generates candidates by joining frequent itemsets from the previous level

2. **Computational Efficiency:**
   - **Eliminates unnecessary database scans** for itemsets that cannot be frequent
   - Reduces the **search space exponentially** - if a 2-itemset is infrequent, we don't need to check any 3-itemsets, 4-itemsets, etc. containing it
   - Makes the algorithm **scalable** for large datasets

3. **Memory Optimization:**
   - **Reduces memory requirements** by not storing infrequent itemsets
   - Only maintains frequent itemsets at each level

4. **Algorithm Design:**
   - Enables the **level-wise (breadth-first) search** approach
   - Allows **systematic candidate generation** by joining frequent (k-1)-itemsets
   - Provides a **theoretical guarantee** that no frequent itemset will be missed

**Example:**
If {Bread, Butter} has support 30% (below min_support = 40%), then we know that {Bread, Butter, Milk}, {Bread, Butter, Beer}, etc. cannot be frequent and don't need to be checked.

---

#### (c) Apply the Apriori algorithm step-by-step. Show the generated candidate itemsets (Ck) and qualified frequent itemsets (Lk) until the largest frequent itemset(s) are generated. Clearly identify all frequent itemsets. (7 marks)

**Given Data:**
- **Transactions:**
  - T1: {Bread, Butter, Milk}
  - T2: {Bread, Butter}
  - T3: {Beer, Cookies, Diapers}
  - T4: {Milk, Diapers, Bread, Butter}
  - T5: {Beer, Diapers}
- **Total transactions:** 5
- **min_support = 40%** = 0.4 × 5 = **2 transactions**
- **min_confidence = 70%**

**Step 1: Generate C1 and Count Support**

| Itemset | Support Count | Support % |
|---------|--------------|-----------|
| {Bread} | 3 | 60% |
| {Butter} | 3 | 60% |
| {Milk} | 2 | 40% |
| {Beer} | 2 | 40% |
| {Cookies} | 1 | 20% |
| {Diapers} | 3 | 60% |

**L1 (Frequent 1-itemsets):**
| Itemset | Support Count |
|---------|--------------|
| {Bread} | 3 |
| {Butter} | 3 |
| {Milk} | 2 |
| {Beer} | 2 |
| {Diapers} | 3 |

*Note: {Cookies} is pruned (support = 1 < 2)*

---

**Step 2: Generate C2 and Count Support**

**C2 (Candidate 2-itemsets):** All pairs from L1
- {Bread, Butter}
- {Bread, Milk}
- {Bread, Beer}
- {Bread, Diapers}
- {Butter, Milk}
- {Butter, Beer}
- {Butter, Diapers}
- {Milk, Beer}
- {Milk, Diapers}
- {Beer, Diapers}

**Count Support:**
| Itemset | Transactions | Support Count | Support % |
|---------|--------------|---------------|-----------|
| {Bread, Butter} | T1, T2, T4 | 3 | 60% |
| {Bread, Milk} | T1, T4 | 2 | 40% |
| {Bread, Beer} | None | 0 | 0% |
| {Bread, Diapers} | T4 | 1 | 20% |
| {Butter, Milk} | T1, T4 | 2 | 40% |
| {Butter, Beer} | None | 0 | 0% |
| {Butter, Diapers} | T4 | 1 | 20% |
| {Milk, Beer} | None | 0 | 0% |
| {Milk, Diapers} | T4 | 1 | 20% |
| {Beer, Diapers} | T3, T5 | 2 | 40% |

**L2 (Frequent 2-itemsets):**
| Itemset | Support Count |
|---------|--------------|
| {Bread, Butter} | 3 |
| {Bread, Milk} | 2 |
| {Butter, Milk} | 2 |
| {Beer, Diapers} | 2 |

---

**Step 3: Generate C3 and Count Support**

**C3 (Candidate 3-itemsets):** Join L2 itemsets that share (k-1) = 1 common item
- From {Bread, Butter} and {Bread, Milk}: {Bread, Butter, Milk}
- From {Bread, Butter} and {Butter, Milk}: {Bread, Butter, Milk} (duplicate)
- From {Bread, Milk} and {Butter, Milk}: {Bread, Butter, Milk} (duplicate)

**Pruning:** Check if all subsets of {Bread, Butter, Milk} are in L2:
- {Bread, Butter} ✓ (in L2)
- {Bread, Milk} ✓ (in L2)
- {Butter, Milk} ✓ (in L2)

**C3 = {Bread, Butter, Milk}**

**Count Support:**
| Itemset | Transactions | Support Count | Support % |
|---------|--------------|---------------|-----------|
| {Bread, Butter, Milk} | T1, T4 | 2 | 40% |

**L3 (Frequent 3-itemsets):**
| Itemset | Support Count |
|---------|--------------|
| {Bread, Butter, Milk} | 2 |

---

**Step 4: Generate C4**

**C4 (Candidate 4-itemsets):** 
- Only one itemset in L3, so no 4-itemsets can be generated

**C4 = ∅**

**Algorithm terminates.**

---

**Summary of All Frequent Itemsets:**

| Level | Frequent Itemsets | Support Count |
|-------|------------------|---------------|
| **L1** | {Bread}, {Butter}, {Milk}, {Beer}, {Diapers} | 3, 3, 2, 2, 3 |
| **L2** | {Bread, Butter}, {Bread, Milk}, {Butter, Milk}, {Beer, Diapers} | 3, 2, 2, 2 |
| **L3** | {Bread, Butter, Milk} | 2 |

**Largest Frequent Itemset:** {Bread, Butter, Milk} (support = 2, 40%)

---

#### (d) Generate all possible association rules with one consequent from the frequent itemsets obtained in (c). Calculate the confidence of each rule and identify all the strong association rules. (6 marks)

**Answer:**

**Frequent Itemsets from (c):**
- L2: {Bread, Butter}, {Bread, Milk}, {Butter, Milk}, {Beer, Diapers}
- L3: {Bread, Butter, Milk}

**Formula:** Confidence(A → B) = Support(A ∪ B) / Support(A)

---

**Rules from 2-itemsets:**

**From {Bread, Butter} (support = 3):**
1. Bread → Butter
   - Confidence = Support({Bread, Butter}) / Support({Bread}) = 3/3 = **1.00 (100%)**
   - **Strong** (≥ 70%)

2. Butter → Bread
   - Confidence = Support({Bread, Butter}) / Support({Butter}) = 3/3 = **1.00 (100%)**
   - **Strong** (≥ 70%)

**From {Bread, Milk} (support = 2):**
3. Bread → Milk
   - Confidence = Support({Bread, Milk}) / Support({Bread}) = 2/3 = **0.67 (67%)**
   - **Not Strong** (< 70%)

4. Milk → Bread
   - Confidence = Support({Bread, Milk}) / Support({Milk}) = 2/2 = **1.00 (100%)**
   - **Strong** (≥ 70%)

**From {Butter, Milk} (support = 2):**
5. Butter → Milk
   - Confidence = Support({Butter, Milk}) / Support({Butter}) = 2/3 = **0.67 (67%)**
   - **Not Strong** (< 70%)

6. Milk → Butter
   - Confidence = Support({Butter, Milk}) / Support({Milk}) = 2/2 = **1.00 (100%)**
   - **Strong** (≥ 70%)

**From {Beer, Diapers} (support = 2):**
7. Beer → Diapers
   - Confidence = Support({Beer, Diapers}) / Support({Beer}) = 2/2 = **1.00 (100%)**
   - **Strong** (≥ 70%)

8. Diapers → Beer
   - Confidence = Support({Beer, Diapers}) / Support({Diapers}) = 2/3 = **0.67 (67%)**
   - **Not Strong** (< 70%)

---

**Rules from 3-itemsets:**

**From {Bread, Butter, Milk} (support = 2):**
9. Bread → Butter, Milk
   - Confidence = Support({Bread, Butter, Milk}) / Support({Bread}) = 2/3 = **0.67 (67%)**
   - **Not Strong** (< 70%)

10. Butter → Bread, Milk
    - Confidence = Support({Bread, Butter, Milk}) / Support({Butter}) = 2/3 = **0.67 (67%)**
    - **Not Strong** (< 70%)

11. Milk → Bread, Butter
    - Confidence = Support({Bread, Butter, Milk}) / Support({Milk}) = 2/2 = **1.00 (100%)**
    - **Strong** (≥ 70%)

12. Bread, Butter → Milk
    - Confidence = Support({Bread, Butter, Milk}) / Support({Bread, Butter}) = 2/3 = **0.67 (67%)**
    - **Not Strong** (< 70%)

13. Bread, Milk → Butter
    - Confidence = Support({Bread, Butter, Milk}) / Support({Bread, Milk}) = 2/2 = **1.00 (100%)**
    - **Strong** (≥ 70%)

14. Butter, Milk → Bread
    - Confidence = Support({Bread, Butter, Milk}) / Support({Butter, Milk}) = 2/2 = **1.00 (100%)**
    - **Strong** (≥ 70%)

---

**Summary Table:**

| Rule | Confidence | Strong? |
|------|-----------|--------|
| Bread → Butter | 100% | ✓ |
| Butter → Bread | 100% | ✓ |
| Bread → Milk | 67% | ✗ |
| Milk → Bread | 100% | ✓ |
| Butter → Milk | 67% | ✗ |
| Milk → Butter | 100% | ✓ |
| Beer → Diapers | 100% | ✓ |
| Diapers → Beer | 67% | ✗ |
| Bread → Butter, Milk | 67% | ✗ |
| Butter → Bread, Milk | 67% | ✗ |
| Milk → Bread, Butter | 100% | ✓ |
| Bread, Butter → Milk | 67% | ✗ |
| Bread, Milk → Butter | 100% | ✓ |
| Butter, Milk → Bread | 100% | ✓ |

---

**Strong Association Rules (Confidence ≥ 70%):**

1. **Bread → Butter** (Confidence: 100%)
2. **Butter → Bread** (Confidence: 100%)
3. **Milk → Bread** (Confidence: 100%)
4. **Milk → Butter** (Confidence: 100%)
5. **Beer → Diapers** (Confidence: 100%)
6. **Milk → Bread, Butter** (Confidence: 100%)
7. **Bread, Milk → Butter** (Confidence: 100%)
8. **Butter, Milk → Bread** (Confidence: 100%)

---

### QUESTION 2 (3+2+3+8 = 16 marks)

#### (a) Hierarchical Agglomerative Clustering (3 marks)

**Given:**
- Dataset: {2, 4, 7, 8, 12, 14}
- After 3 iterations: C1 = {2, 4}, C2 = {7, 8}, C3 = {12, 14}

**Answer:**

**(i) Distance between C1 and C2 using Single Linkage:**

**Single Linkage (Minimum Distance):** Distance between two clusters is the minimum distance between any point in C1 and any point in C2.

- Points in C1: {2, 4}
- Points in C2: {7, 8}
- Distances: |2-7| = 5, |2-8| = 6, |4-7| = 3, |4-8| = 4
- **Minimum distance = 3**

**Answer: Distance(C1, C2) = 3**

---

**(ii) Distance between C1 and C2 using Complete Linkage:**

**Complete Linkage (Maximum Distance):** Distance between two clusters is the maximum distance between any point in C1 and any point in C2.

- Points in C1: {2, 4}
- Points in C2: {7, 8}
- Distances: |2-7| = 5, |2-8| = 6, |4-7| = 3, |4-8| = 4
- **Maximum distance = 6**

**Answer: Distance(C1, C2) = 6**

---

**(iii) Clusters merged at next iteration using Single Linkage:**

**Distances between clusters (Single Linkage):**
- Distance(C1, C2) = min(|2-7|, |2-8|, |4-7|, |4-8|) = min(5, 6, 3, 4) = **3**
- Distance(C1, C3) = min(|2-12|, |2-14|, |4-12|, |4-14|) = min(10, 12, 8, 10) = **8**
- Distance(C2, C3) = min(|7-12|, |7-14|, |8-12|, |8-14|) = min(5, 7, 4, 6) = **4**

**Minimum inter-cluster distance = 3** (between C1 and C2)

**Answer: C1 and C2 are merged at the next iteration.**

**Resulting clusters:** {C1 ∪ C2} = {2, 4, 7, 8} and C3 = {12, 14}

---

#### (b) Dendrogram Clustering (2 marks)

**Given:** Dendrogram with labels: BA, NA, RM, FI, MI, TO

**Answer:**

To create **3 clusters** from the dendrogram, we need to cut the dendrogram at a height that results in 3 clusters. This means we identify the point where the dendrogram has 3 main branches.

**Clusters (based on dendrogram structure):**

**Cluster 1:** {BA, NA}
**Cluster 2:** {RM, FI}
**Cluster 3:** {MI, TO}

*Note: The exact clusters depend on the dendrogram structure shown. The answer should reflect the three main branches visible when cutting to create 3 clusters.*

---

#### (c) k-Means Cluster Centers (3 marks)

**Given:**
- Points: P1(0,6), P2(6,0), P3(2,2), P4(4,4), P5(6,6), P6(5,5), P7(7,7)
- After first iteration:
  - C1: {P1(0,6), P2(6,0)}
  - C2: {P3(2,2), P4(4,4), P5(6,6)}
  - C3: {P6(5,5), P7(7,7)}

**Answer:**

**Cluster Center Calculation:** Mean of all points in the cluster.

**C1 Center:**
- x-coordinate: (0 + 6) / 2 = 6 / 2 = **3**
- y-coordinate: (6 + 0) / 2 = 6 / 2 = **3**
- **C1 = (3, 3)**

**C2 Center:**
- x-coordinate: (2 + 4 + 6) / 3 = 12 / 3 = **4**
- y-coordinate: (2 + 4 + 6) / 3 = 12 / 3 = **4**
- **C2 = (4, 4)**

**C3 Center:**
- x-coordinate: (5 + 7) / 2 = 12 / 2 = **6**
- y-coordinate: (5 + 7) / 2 = 12 / 2 = **6**
- **C3 = (6, 6)**

**Answer:**
- **C1 = (3, 3)**
- **C2 = (4, 4)**
- **C3 = (6, 6)**

---

#### (d) k-Means Next Iteration (8 marks)

**Given:** Cluster centers from (c): C1(3,3), C2(4,4), C3(6,6)

**Answer:**

**Step 1: Calculate distances from each point to each cluster center**

**Distance formula:** d = √[(x₁ - x₂)² + (y₁ - y₂)²]

**For P1(0,6):**
- d(P1, C1) = √[(0-3)² + (6-3)²] = √[9 + 9] = √18 = **4.24**
- d(P1, C2) = √[(0-4)² + (6-4)²] = √[16 + 4] = √20 = **4.47**
- d(P1, C3) = √[(0-6)² + (6-6)²] = √[36 + 0] = √36 = **6.00**
- **Closest: C1** → Sum of squares = (4.24)² = **18**

**For P2(6,0):**
- d(P2, C1) = √[(6-3)² + (0-3)²] = √[9 + 9] = √18 = **4.24**
- d(P2, C2) = √[(6-4)² + (0-4)²] = √[4 + 16] = √20 = **4.47**
- d(P2, C3) = √[(6-6)² + (0-6)²] = √[0 + 36] = √36 = **6.00**
- **Closest: C1** → Sum of squares = (4.24)² = **18**

**For P3(2,2):**
- d(P3, C1) = √[(2-3)² + (2-3)²] = √[1 + 1] = √2 = **1.41**
- d(P3, C2) = √[(2-4)² + (2-4)²] = √[4 + 4] = √8 = **2.83**
- d(P3, C3) = √[(2-6)² + (2-6)²] = √[16 + 16] = √32 = **5.66**
- **Closest: C1** → Sum of squares = (1.41)² = **2**

**For P4(4,4):**
- d(P4, C1) = √[(4-3)² + (4-3)²] = √[1 + 1] = √2 = **1.41**
- d(P4, C2) = √[(4-4)² + (4-4)²] = √[0 + 0] = **0.00**
- d(P4, C3) = √[(4-6)² + (4-6)²] = √[4 + 4] = √8 = **2.83**
- **Closest: C2** → Sum of squares = (0.00)² = **0**

**For P5(6,6):**
- d(P5, C1) = √[(6-3)² + (6-3)²] = √[9 + 9] = √18 = **4.24**
- d(P5, C2) = √[(6-4)² + (6-4)²] = √[4 + 4] = √8 = **2.83**
- d(P5, C3) = √[(6-6)² + (6-6)²] = √[0 + 0] = **0.00**
- **Closest: C3** → Sum of squares = (0.00)² = **0**

**For P6(5,5):**
- d(P6, C1) = √[(5-3)² + (5-3)²] = √[4 + 4] = √8 = **2.83**
- d(P6, C2) = √[(5-4)² + (5-4)²] = √[1 + 1] = √2 = **1.41**
- d(P6, C3) = √[(5-6)² + (5-6)²] = √[1 + 1] = √2 = **1.41**
- **Closest: C2 or C3** (tie, choose C2) → Sum of squares = (1.41)² = **2**

**For P7(7,7):**
- d(P7, C1) = √[(7-3)² + (7-3)²] = √[16 + 16] = √32 = **5.66**
- d(P7, C2) = √[(7-4)² + (7-4)²] = √[9 + 9] = √18 = **4.24**
- d(P7, C3) = √[(7-6)² + (7-6)²] = √[1 + 1] = √2 = **1.41**
- **Closest: C3** → Sum of squares = (1.41)² = **2**

---

**Step 2: Fill the table**

| Point | C1 (3,3) | C2 (4,4) | C3 (6,6) | Closest Cluster |
|-------|----------|----------|----------|-----------------|
| P1(0,6) | 18 | 20 | 36 | C1 |
| P2(6,0) | 18 | 20 | 36 | C1 |
| P3(2,2) | 2 | 8 | 32 | C1 |
| P4(4,4) | 2 | 0 | 8 | C2 |
| P5(6,6) | 18 | 8 | 0 | C3 |
| P6(5,5) | 8 | 2 | 2 | C2 |
| P7(7,7) | 32 | 18 | 2 | C3 |

---

**Step 3: Determine clusters for next iteration**

Based on the closest cluster assignments:

- **C1:** {P1(0,6), P2(6,0), P3(2,2)}
- **C2:** {P4(4,4), P6(5,5)}
- **C3:** {P5(6,6), P7(7,7)}

**Answer:**
- **C1 = {P1, P2, P3}**
- **C2 = {P4, P6}**
- **C3 = {P5, P7}**

---

## SECTION B

### QUESTION 3 (20 marks)

#### (a) Differentiate data mining and data warehousing. (3 marks)

**Answer:**

**Data Warehousing:**
- **Definition:** A process of collecting, storing, and managing data from various sources in a centralized repository (data warehouse) for analytical purposes
- **Purpose:** To provide a unified, integrated view of organizational data for decision support
- **Focus:** Data storage, integration, and organization
- **Activities:** ETL (Extract, Transform, Load), data cleaning, data integration, data modeling
- **Output:** Structured, historical, and consolidated data repository
- **Time Orientation:** Historical data storage and management
- **Scope:** Infrastructure and architecture for data storage

**Data Mining:**
- **Definition:** The process of discovering patterns, relationships, and knowledge from large datasets using automated or semi-automated methods
- **Purpose:** To extract useful information, patterns, and insights from data
- **Focus:** Pattern discovery, knowledge extraction, and predictive modeling
- **Activities:** Classification, clustering, association rule mining, anomaly detection, prediction
- **Output:** Patterns, rules, models, and insights
- **Time Orientation:** Analysis and discovery from data
- **Scope:** Analytical techniques and algorithms

**Key Differences:**

| Aspect | Data Warehousing | Data Mining |
|--------|-----------------|-------------|
| **Primary Function** | Data storage and integration | Pattern discovery and analysis |
| **Stage** | Data preparation and storage | Data analysis and knowledge extraction |
| **Output** | Integrated data repository | Patterns, models, insights |
| **Techniques** | ETL, data modeling | Algorithms (classification, clustering, etc.) |
| **User Interaction** | Data retrieval and querying | Pattern exploration and model building |
| **Relationship** | Provides data for mining | Uses data from warehouse |

**Relationship:** Data warehousing provides the foundation (clean, integrated data) that data mining uses to discover patterns and knowledge.

---

#### (b) Distinguish between the following data warehouse concepts: (3 marks)

**Answer:**

**(i) Data warehouse and data mart:**

**Data Warehouse:**
- **Scope:** Enterprise-wide, covers entire organization
- **Size:** Large-scale, contains data from multiple subject areas
- **Data Sources:** Multiple operational systems across the organization
- **Users:** Organization-wide users, executives, analysts
- **Purpose:** Centralized repository for comprehensive business intelligence
- **Complexity:** High complexity, longer implementation time
- **Granularity:** Detailed and summarized data at multiple levels
- **Example:** Enterprise data warehouse containing sales, HR, finance, operations data

**Data Mart:**
- **Scope:** Departmental or functional area (e.g., sales, marketing, finance)
- **Size:** Smaller, focused on specific subject area
- **Data Sources:** Fewer sources, often subset of data warehouse or specific operational systems
- **Users:** Specific department or user group
- **Purpose:** Focused analytical support for specific business function
- **Complexity:** Lower complexity, faster implementation
- **Granularity:** Data at appropriate level for specific function
- **Example:** Sales data mart containing only sales-related data

**Relationship:** Data marts are often subsets of data warehouses, created for specific departments or functions.

---

**(ii) Base cuboid and apex cuboid:**

**Base Cuboid:**
- **Definition:** The lowest level of aggregation in a multidimensional data cube
- **Granularity:** Most detailed level, contains all dimensions at their lowest level
- **Size:** Largest cuboid (contains most data)
- **Dimensions:** All dimensions at base level (e.g., individual product, day, store, customer)
- **Example:** Sales data with dimensions: Product (individual items), Time (daily), Location (individual stores), Customer (individual customers)
- **Purpose:** Contains raw, detailed transactional data

**Apex Cuboid:**
- **Definition:** The highest level of aggregation in a multidimensional data cube
- **Granularity:** Most aggregated level, all dimensions aggregated (ALL level)
- **Size:** Smallest cuboid (contains least data - typically one value)
- **Dimensions:** All dimensions at ALL level (total aggregation)
- **Example:** Total sales across all products, all time periods, all locations, all customers (single aggregated value)
- **Purpose:** Provides overall summary/total

**Relationship:** They represent opposite ends of the aggregation hierarchy. Base cuboid has maximum detail, apex cuboid has maximum aggregation.

---

**(iii) Dimension and fact:**

**Dimension:**
- **Definition:** Descriptive attributes that provide context for measures
- **Purpose:** Used for grouping, filtering, and organizing data
- **Characteristics:** 
  - Categorical or descriptive data
  - Relatively stable (changes infrequently)
  - Hierarchical structure (e.g., Time: Year → Quarter → Month → Day)
- **Examples:** Time, Location, Product, Customer, Employee
- **Role:** Provides the "by what" for analysis (e.g., sales by time, by location, by product)
- **Storage:** Dimension tables in star schema

**Fact:**
- **Definition:** Numerical measures or metrics that represent business events or transactions
- **Purpose:** Quantifiable values that are analyzed
- **Characteristics:**
  - Numerical data (measures)
  - Frequently changing (transactional)
  - Additive or semi-additive
- **Examples:** Sales amount, quantity sold, profit, revenue, cost
- **Role:** Provides the "what" being measured (e.g., sales amount, profit)
- **Storage:** Fact table in star schema

**Relationship:** Facts are measured in the context of dimensions. For example, "Sales amount (fact) by Product, Time, and Location (dimensions)".

---

#### (c) Describe the three main forms of multidimensional data models for data warehouses. (6 marks)

**Answer:**

The three main forms of multidimensional data models are:

---

**1. Star Schema:**

**Structure:**
- **Central fact table** containing measures (facts) and foreign keys
- **Multiple dimension tables** surrounding the fact table (like a star)
- **One-to-many relationship** between fact table and each dimension table
- **Denormalized dimension tables** (dimension attributes stored together)

**Characteristics:**
- Simple and intuitive design
- Easy to understand and query
- Denormalized dimensions (redundancy for performance)
- Fast query performance (fewer joins)
- Larger storage requirements (due to denormalization)

**Example:**
```
Fact_Sales (fact_id, product_id, time_id, store_id, customer_id, sales_amount, quantity)
    ↓
Dimension_Product (product_id, product_name, category, brand)
Dimension_Time (time_id, date, month, quarter, year)
Dimension_Store (store_id, store_name, city, region)
Dimension_Customer (customer_id, customer_name, age_group, income)
```

**Advantages:**
- Simple structure
- Fast queries (fewer joins)
- Easy for business users to understand
- Good for OLAP operations

**Disadvantages:**
- Data redundancy in dimensions
- Less flexible for complex relationships
- Potential data inconsistency

---

**2. Snowflake Schema:**

**Structure:**
- **Central fact table** (same as star schema)
- **Normalized dimension tables** (dimensions are broken down into multiple related tables)
- **Hierarchical dimension structure** (dimensions have sub-dimensions)
- **More normalized** than star schema

**Characteristics:**
- Normalized dimensions (reduces redundancy)
- Hierarchical dimension relationships
- More complex structure (more tables)
- More joins required for queries
- Reduced storage requirements
- Better data integrity

**Example:**
```
Fact_Sales (fact_id, product_id, time_id, store_id, customer_id, sales_amount, quantity)
    ↓
Dimension_Product (product_id, product_name, category_id, brand_id)
    ↓
Dimension_Category (category_id, category_name, department_id)
Dimension_Brand (brand_id, brand_name, manufacturer_id)
```

**Advantages:**
- Reduced data redundancy
- Better data integrity
- More flexible for complex hierarchies
- Lower storage requirements

**Disadvantages:**
- More complex queries (more joins)
- Slower query performance
- More difficult to understand
- More complex maintenance

---

**3. Fact Constellation Schema (Galaxy Schema):**

**Structure:**
- **Multiple fact tables** sharing dimension tables
- **Shared dimensions** (conformed dimensions) used by multiple facts
- **Complex network structure** (like a constellation of stars)
- Can combine star and snowflake schemas

**Characteristics:**
- Multiple fact tables for different business processes
- Shared/conformed dimensions
- Most complex structure
- Supports multiple subject areas
- Allows analysis across different business processes

**Example:**
```
Fact_Sales (fact_id, product_id, time_id, store_id, sales_amount)
Fact_Inventory (fact_id, product_id, time_id, warehouse_id, quantity_on_hand)
    ↓ (shared dimensions)
Dimension_Product (product_id, product_name, category)
Dimension_Time (time_id, date, month, year)
Dimension_Store (store_id, store_name, location)
Dimension_Warehouse (warehouse_id, warehouse_name, location)
```

**Advantages:**
- Supports multiple business processes
- Allows cross-process analysis
- Flexible for complex business requirements
- Reuses dimensions (conformed dimensions)

**Disadvantages:**
- Most complex to design and maintain
- Requires careful dimension design (conformed dimensions)
- Can become very large
- More difficult for users to navigate

---

**Summary Comparison:**

| Aspect | Star Schema | Snowflake Schema | Fact Constellation |
|--------|-------------|------------------|-------------------|
| **Complexity** | Simple | Moderate | Complex |
| **Normalization** | Denormalized | Normalized | Mixed |
| **Joins** | Few | Moderate | Many |
| **Performance** | Fast | Moderate | Varies |
| **Storage** | Higher | Lower | Varies |
| **Flexibility** | Low | Moderate | High |
| **Use Case** | Single subject area | Single subject with hierarchies | Multiple subject areas |

---

#### (d) List the four main characteristics of a data warehouse. (2 marks)

**Answer:**

The four main characteristics of a data warehouse (as defined by Bill Inmon) are:

1. **Subject-Oriented:**
   - Data is organized around major subjects or business areas (e.g., sales, customers, products)
   - Focuses on analytical needs rather than operational processes
   - Provides a unified view of a particular subject

2. **Integrated:**
   - Data from multiple, heterogeneous sources is combined into a consistent format
   - Resolves inconsistencies in naming, coding, and formats
   - Provides a single, coherent view of organizational data

3. **Non-Volatile (Time-Variant):**
   - Data is stable and not frequently updated or deleted
   - Historical data is preserved (time series data)
   - Changes are additions (new data) rather than modifications
   - Supports trend analysis over time

4. **Time-Variant:**
   - Data contains historical information (snapshots over time)
   - Time is a key dimension in the data warehouse
   - Supports analysis of changes and trends over time periods
   - Data is associated with time periods (daily, weekly, monthly, etc.)

**Note:** Some sources combine "Non-Volatile" and "Time-Variant" or list them separately. The key point is that data warehouses maintain historical data that doesn't change frequently.

---

#### (e) Explain the difference between OLTP and OLAP. (6 marks)

**Answer:**

**OLTP (On-Line Transaction Processing):**

**Purpose:**
- Supports day-to-day operational transactions and business processes
- Handles routine business operations and real-time data entry

**Characteristics:**
- **Transaction-Oriented:** Processes individual transactions (insert, update, delete)
- **Current Data:** Stores current, up-to-date operational data
- **High Volume of Short Transactions:** Many small, frequent transactions
- **Normalized Database Design:** Highly normalized (3NF or higher) to reduce redundancy
- **Read/Write Intensive:** Frequent updates, inserts, and deletes
- **Response Time:** Fast response for individual transactions (milliseconds to seconds)
- **Users:** Operational staff, clerks, customer service representatives
- **Data Granularity:** Detailed, transaction-level data
- **Query Complexity:** Simple, standardized queries
- **Data Volume:** Moderate (current operational data)
- **Primary Function:** Data capture and transaction processing

**Examples:**
- Order entry systems
- Banking transaction systems (ATM, deposits, withdrawals)
- Inventory management systems
- Customer relationship management (CRM) systems
- Point-of-sale (POS) systems

**Database Operations:**
- INSERT, UPDATE, DELETE operations
- Simple SELECT queries for specific records
- Transaction processing (ACID properties)

---

**OLAP (On-Line Analytical Processing):**

**Purpose:**
- Supports analytical queries and decision-making
- Provides insights for strategic planning and business intelligence

**Characteristics:**
- **Analysis-Oriented:** Supports complex analytical queries and reporting
- **Historical Data:** Stores historical, aggregated, and summarized data
- **Low Volume of Complex Queries:** Fewer but more complex analytical queries
- **Denormalized Database Design:** Star schema, snowflake schema (denormalized for performance)
- **Read-Intensive:** Primarily read operations, infrequent updates
- **Response Time:** Longer response time acceptable (seconds to minutes for complex queries)
- **Users:** Analysts, executives, decision-makers, data scientists
- **Data Granularity:** Aggregated and summarized data at multiple levels
- **Query Complexity:** Complex queries with aggregations, groupings, and multi-dimensional analysis
- **Data Volume:** Large (historical and aggregated data)
- **Primary Function:** Data analysis and decision support

**Examples:**
- Business intelligence systems
- Data warehouses
- Executive information systems (EIS)
- Reporting and analytics platforms
- Data mining applications

**Database Operations:**
- Complex SELECT queries with aggregations (SUM, AVG, COUNT, etc.)
- Multi-dimensional analysis (drill-down, roll-up, slice, dice)
- Ad-hoc analytical queries
- Infrequent bulk loads (ETL processes)

---

**Key Differences Summary:**

| Aspect | OLTP | OLAP |
|--------|------|------|
| **Purpose** | Operational transactions | Analytical processing |
| **Data** | Current, detailed | Historical, aggregated |
| **Design** | Normalized | Denormalized (star/snowflake) |
| **Operations** | INSERT, UPDATE, DELETE | SELECT (complex queries) |
| **Transaction Volume** | High volume, short | Low volume, complex |
| **Response Time** | Fast (milliseconds) | Slower (seconds to minutes) |
| **Users** | Operational staff | Analysts, executives |
| **Query Type** | Simple, standardized | Complex, ad-hoc |
| **Data Updates** | Frequent, real-time | Infrequent, batch |
| **Focus** | Data capture | Data analysis |
| **Granularity** | Detailed transactions | Aggregated summaries |
| **ACID Properties** | Strictly enforced | Relaxed |

---

**Relationship:**
- OLTP systems are the **source** of data for OLAP systems
- Data flows from OLTP → ETL → Data Warehouse (OLAP)
- OLTP handles operational efficiency; OLAP supports strategic decision-making
- Both are essential: OLTP for day-to-day operations, OLAP for business intelligence

---

### QUESTION 4 (15 marks) - Decision Tree Construction

**Given:**
- **Attributes:** time, gender, area
- **Target:** risk (low, high)
- **Training Data:**
  - ID 1: time=1-2, gender=m, area=urban, risk=low
  - ID 2: time=2-7, gender=m, area=rural, risk=high
  - ID 3: time=>7, gender=f, area=rural, risk=low
  - ID 4: time=1-2, gender=f, area=rural, risk=high
  - ID 5: time=>7, gender=m, area=rural, risk=high
  - ID 6: time=1-2, gender=m, area=rural, risk=high
  - ID 7: time=2-7, gender=f, area=urban, risk=low
  - ID 8: time=2-7, gender=m, area=urban, risk=low

**Formulas:**
- Entropy: H(T) = -Σ(i=1 to k) pᵢ × log₂(pᵢ)
- Information Gain: IG(T, A) = H(T) - Σ(i=1 to m) (|Tᵢ|/|T|) × H(Tᵢ)

---

**Answer:**

**Step 1: Calculate Root Entropy**

Total instances: 8
- Risk = low: 4 instances (IDs: 1, 3, 7, 8)
- Risk = high: 4 instances (IDs: 2, 4, 5, 6)

H(Root) = -[P(low) × log₂(P(low)) + P(high) × log₂(P(high))]
H(Root) = -[(4/8) × log₂(4/8) + (4/8) × log₂(4/8)]
H(Root) = -[0.5 × log₂(0.5) + 0.5 × log₂(0.5)]
H(Root) = -[0.5 × (-1) + 0.5 × (-1)]
H(Root) = -[-0.5 - 0.5] = 1.0

---

**Step 2: Calculate Information Gain for Each Attribute**

**Attribute: time**

Values: {1-2, 2-7, >7}

**time = 1-2:** 3 instances (IDs: 1, 4, 6)
- low: 1 (ID 1)
- high: 2 (IDs: 4, 6)
- H(1-2) = -[(1/3) × log₂(1/3) + (2/3) × log₂(2/3)]
- H(1-2) = -[0.333 × (-1.585) + 0.667 × (-0.585)]
- H(1-2) = -[-0.528 - 0.390] = 0.918

**time = 2-7:** 3 instances (IDs: 2, 7, 8)
- low: 2 (IDs: 7, 8)
- high: 1 (ID 2)
- H(2-7) = -[(2/3) × log₂(2/3) + (1/3) × log₂(1/3)]
- H(2-7) = -[0.667 × (-0.585) + 0.333 × (-1.585)]
- H(2-7) = -[-0.390 - 0.528] = 0.918

**time = >7:** 2 instances (IDs: 3, 5)
- low: 1 (ID 3)
- high: 1 (ID 5)
- H(>7) = -[(1/2) × log₂(1/2) + (1/2) × log₂(1/2)]
- H(>7) = -[0.5 × (-1) + 0.5 × (-1)] = 1.0

IG(time) = H(Root) - [(3/8) × H(1-2) + (3/8) × H(2-7) + (2/8) × H(>7)]
IG(time) = 1.0 - [(3/8) × 0.918 + (3/8) × 0.918 + (2/8) × 1.0]
IG(time) = 1.0 - [0.344 + 0.344 + 0.25]
IG(time) = 1.0 - 0.938 = **0.062**

---

**Attribute: gender**

Values: {male, female}

**gender = male:** 5 instances (IDs: 1, 2, 5, 6, 8)
- low: 2 (IDs: 1, 8)
- high: 3 (IDs: 2, 5, 6)
- H(male) = -[(2/5) × log₂(2/5) + (3/5) × log₂(3/5)]
- H(male) = -[0.4 × (-1.322) + 0.6 × (-0.737)]
- H(male) = -[-0.529 - 0.442] = 0.971

**gender = female:** 3 instances (IDs: 3, 4, 7)
- low: 2 (IDs: 3, 7)
- high: 1 (ID 4)
- H(female) = -[(2/3) × log₂(2/3) + (1/3) × log₂(1/3)]
- H(female) = -[0.667 × (-0.585) + 0.333 × (-1.585)]
- H(female) = -[-0.390 - 0.528] = 0.918

IG(gender) = H(Root) - [(5/8) × H(male) + (3/8) × H(female)]
IG(gender) = 1.0 - [(5/8) × 0.971 + (3/8) × 0.918]
IG(gender) = 1.0 - [0.607 + 0.344]
IG(gender) = 1.0 - 0.951 = **0.049**

---

**Attribute: area**

Values: {urban, rural}

**area = urban:** 3 instances (IDs: 1, 7, 8)
- low: 3 (IDs: 1, 7, 8)
- high: 0
- H(urban) = -[(3/3) × log₂(3/3) + (0/3) × log₂(0/3)]
- H(urban) = -[1 × log₂(1) + 0] = -[1 × 0] = **0** (pure node)

**area = rural:** 5 instances (IDs: 2, 3, 4, 5, 6)
- low: 1 (ID 3)
- high: 4 (IDs: 2, 4, 5, 6)
- H(rural) = -[(1/5) × log₂(1/5) + (4/5) × log₂(4/5)]
- H(rural) = -[0.2 × (-2.322) + 0.8 × (-0.322)]
- H(rural) = -[-0.464 - 0.258] = 0.722

IG(area) = H(Root) - [(3/8) × H(urban) + (5/8) × H(rural)]
IG(area) = 1.0 - [(3/8) × 0 + (5/8) × 0.722]
IG(area) = 1.0 - [0 + 0.451]
IG(area) = **0.549**

---

**Step 3: Select Root Node**

**Information Gains:**
- IG(time) = 0.062
- IG(gender) = 0.049
- IG(area) = 0.549 ← **Highest**

**Root Node: area**

---

**Step 4: Build Tree - First Level**

```
                    [area]
                   /      \
            urban /        \ rural
                /          \
          [low] (pure)    [Continue]
          (3 instances)   (5 instances)
```

**urban branch:** All 3 instances have risk=low → **Leaf node: low**

**rural branch:** 5 instances remain (IDs: 2, 3, 4, 5, 6)
- low: 1 (ID 3)
- high: 4 (IDs: 2, 4, 5, 6)
- H(rural) = 0.722 (already calculated)

---

**Step 5: Calculate Information Gain for Remaining Attributes (rural branch)**

**Attribute: time (for rural branch)**

**time = 1-2:** 2 instances (IDs: 4, 6)
- low: 0
- high: 2
- H(1-2) = -[(0/2) × log₂(0/2) + (2/2) × log₂(2/2)] = 0 (pure - all high)

**time = 2-7:** 1 instance (ID 2)
- low: 0
- high: 1
- H(2-7) = 0 (pure - all high)

**time = >7:** 2 instances (IDs: 3, 5)
- low: 1 (ID 3)
- high: 1 (ID 5)
- H(>7) = -[(1/2) × log₂(1/2) + (1/2) × log₂(1/2)] = 1.0

IG(time) = H(rural) - [(2/5) × H(1-2) + (1/5) × H(2-7) + (2/5) × H(>7)]
IG(time) = 0.722 - [(2/5) × 0 + (1/5) × 0 + (2/5) × 1.0]
IG(time) = 0.722 - [0 + 0 + 0.4]
IG(time) = **0.322**

---

**Attribute: gender (for rural branch)**

**gender = male:** 3 instances (IDs: 2, 5, 6)
- low: 0
- high: 3
- H(male) = 0 (pure - all high)

**gender = female:** 2 instances (IDs: 3, 4)
- low: 1 (ID 3)
- high: 1 (ID 4)
- H(female) = -[(1/2) × log₂(1/2) + (1/2) × log₂(1/2)] = 1.0

IG(gender) = H(rural) - [(3/5) × H(male) + (2/5) × H(female)]
IG(gender) = 0.722 - [(3/5) × 0 + (2/5) × 1.0]
IG(gender) = 0.722 - [0 + 0.4]
IG(gender) = **0.322**

**Tie between time and gender (both 0.322).** Choose **time** (arbitrary choice, or use first attribute).

---

**Step 6: Continue Building Tree**

```
                    [area]
                   /      \
            urban /        \ rural
                /          \
          [low]        [time]
          (pure)      /   |   \
                    /     |     \
           1-2 /   2-7 |    >7 \
              /        |      \
        [high]    [high]   [Continue]
        (pure)    (pure)   (2 instances)
```

**time = 1-2 (rural):** 2 instances (IDs: 4, 6) → both high → **Leaf: high**
**time = 2-7 (rural):** 1 instance (ID 2) → high → **Leaf: high**
**time = >7 (rural):** 2 instances (IDs: 3, 5) → mixed (1 low, 1 high) → Continue

---

**Step 7: Final Split (time = >7, rural branch)**

Remaining: 2 instances (IDs: 3, 5)
- ID 3: gender=f, risk=low
- ID 5: gender=m, risk=high

Only **gender** attribute remains.

**gender = female:** 1 instance (ID 3) → low → **Leaf: low**
**gender = male:** 1 instance (ID 5) → high → **Leaf: high**

---

**Final Decision Tree:**

```
                        [area]
                       /      \
                urban /        \ rural
                    /          \
              [low]            [time]
              (pure)          /   |   \
                            /     |     \
                   1-2 /   2-7 |    >7 \
                      /        |      \
                [high]    [high]   [gender]
                (pure)    (pure)   /       \
                                 /         \
                          female /         \ male
                               /           \
                         [low]           [high]
                         (pure)          (pure)
```

---

**Decision Rules:**

1. **IF area = urban THEN risk = low**
2. **IF area = rural AND time = 1-2 THEN risk = high**
3. **IF area = rural AND time = 2-7 THEN risk = high**
4. **IF area = rural AND time = >7 AND gender = female THEN risk = low**
5. **IF area = rural AND time = >7 AND gender = male THEN risk = high**

---

**Verification:**

| ID | Path | Predicted | Actual | Match |
|----|------|-----------|--------|-------|
| 1 | urban → low | low | low | ✓ |
| 2 | rural, 2-7 → high | high | high | ✓ |
| 3 | rural, >7, female → low | low | low | ✓ |
| 4 | rural, 1-2 → high | high | high | ✓ |
| 5 | rural, >7, male → high | high | high | ✓ |
| 6 | rural, 1-2 → high | high | high | ✓ |
| 7 | urban → low | low | low | ✓ |
| 8 | urban → low | low | low | ✓ |

**All 8 instances correctly classified!**

---

## Summary

This exam covers fundamental data mining concepts:

1. **Frequent Pattern Mining:** Apriori algorithm, association rules
2. **Clustering:** Hierarchical agglomerative clustering, k-Means
3. **Data Warehousing:** Concepts, models, OLTP vs OLAP
4. **Classification:** Decision tree construction using information gain

These topics are essential for understanding data mining techniques and their applications in business intelligence and knowledge discovery.

