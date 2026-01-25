# DSC603 CA Test - January 2026
## Data Mining - Continuous Assessment
**University of Buea**

---

## Exam Overview

**Course Code:** DSC603  
**Course Title:** Data Mining  
**Test Type:** Continuous Assessment (CA)  
**Date:** January 2026  
**Total Marks:** 30 (Part A: 15 marks, Part B: 15 marks)

**Instructions:**
- Answer Part A and Part B in separate examination booklets
- Show all calculations and steps clearly

---

## Part A: Data Pre-processing and Frequent Pattern Mining (15 marks)

---

## Question 1: Data Pre-processing (8 marks)

### a) Equal-Frequency Binning and Smoothing by Bin Boundaries (4 marks)

#### Dataset:
```
8, 9, 15, 16, 21, 21, 24, 26, 27, 30, 30, 34
```

**Total values (n) = 12**

#### i) Place the dataset into three equal-frequency bins

**Step 1: Calculate bin size**
- Number of bins = 3
- Values per bin = 12 / 3 = 4 values per bin

**Step 2: Sort the data (already sorted)**
```
8, 9, 15, 16, 21, 21, 24, 26, 27, 30, 30, 34
```

**Step 3: Divide into 3 bins (4 values each)**

**Bin 1 (Low):**
- Values: 8, 9, 15, 16
- Range: [8, 16]
- Bin boundaries: Min = 8, Max = 16

**Bin 2 (Medium):**
- Values: 21, 21, 24, 26
- Range: [21, 26]
- Bin boundaries: Min = 21, Max = 26

**Bin 3 (High):**
- Values: 27, 30, 30, 34
- Range: [27, 34]
- Bin boundaries: Min = 27, Max = 34

**Answer:**
```
Bin 1: [8, 9, 15, 16]    Range: [8, 16]
Bin 2: [21, 21, 24, 26]  Range: [21, 26]
Bin 3: [27, 30, 30, 34]  Range: [27, 34]
```

---

#### ii) Show the results of smoothing the data by bin boundaries

**Smoothing by bin boundaries:** Replace each value with the nearest bin boundary value.

**Bin 1: [8, 9, 15, 16]**
- Boundaries: Min = 8, Max = 16
- 8 → 8 (nearest to min boundary)
- 9 → 8 (closer to min: |9-8|=1, |9-16|=7)
- 15 → 16 (closer to max: |15-8|=7, |15-16|=1)
- 16 → 16 (nearest to max boundary)

**Bin 2: [21, 21, 24, 26]**
- Boundaries: Min = 21, Max = 26
- 21 → 21 (nearest to min boundary)
- 21 → 21 (nearest to min boundary)
- 24 → 26 (closer to max: |24-21|=3, |24-26|=2)
- 26 → 26 (nearest to max boundary)

**Bin 3: [27, 30, 30, 34]**
- Boundaries: Min = 27, Max = 34
- 27 → 27 (nearest to min boundary)
- 30 → 27 (closer to min: |30-27|=3, |30-34|=4)
- 30 → 27 (closer to min: |30-27|=3, |30-34|=4)
- 34 → 34 (nearest to max boundary)

**Answer:**
```
Original:  8,  9, 15, 16, 21, 21, 24, 26, 27, 30, 30, 34
Smoothed:  8,  8, 16, 16, 21, 21, 26, 26, 27, 27, 27, 34
```

**Smoothed Dataset:**
```
8, 8, 16, 16, 21, 21, 26, 26, 27, 27, 27, 34
```

---

### b) Equal-Width Binning and Histogram (4 marks)

#### Dataset:
```
5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215
```

**Total values (n) = 12**

#### i) Place the dataset into three equal-width bins

**Step 1: Find min and max values**
- Min (X_min) = 5
- Max (X_max) = 215
- Range = 215 - 5 = 210

**Step 2: Calculate bin width**
- Number of bins = 3
- Bin width = (X_max - X_min) / Number of bins
- Bin width = (215 - 5) / 3 = 210 / 3 = 70

**Step 3: Define bin boundaries**

**Bin 1:**
- Lower boundary: 5
- Upper boundary: 5 + 70 = 75
- Range: [5, 75) (inclusive of 5, exclusive of 75, but typically we include the max value in the last bin)

**Bin 2:**
- Lower boundary: 75
- Upper boundary: 75 + 70 = 145
- Range: [75, 145)

**Bin 3:**
- Lower boundary: 145
- Upper boundary: 145 + 70 = 215
- Range: [145, 215] (inclusive of 215)

**Step 4: Assign values to bins**

**Bin 1: [5, 75)**
- Values: 5, 10, 11, 13, 15, 35
- Count: 6 values

**Bin 2: [75, 145)**
- Values: 92
- Count: 1 value

**Bin 3: [145, 215]**
- Values: 204, 215
- Count: 2 values

**Note:** Values 50, 55, 72 fall in Bin 1 range [5, 75)

**Corrected Assignment:**
- Bin 1 [5, 75): 5, 10, 11, 13, 15, 35, 50, 55, 72 (9 values)
- Bin 2 [75, 145): 92 (1 value)
- Bin 3 [145, 215]: 204, 215 (2 values)

**Answer:**
```
Bin 1: [5, 75)    → Values: 5, 10, 11, 13, 15, 35, 50, 55, 72  (9 values)
Bin 2: [75, 145)  → Values: 92                                  (1 value)
Bin 3: [145, 215] → Values: 204, 215                            (2 values)
```

---

#### ii) Sketch the corresponding histogram

**Histogram Representation:**

```
Frequency
    |
 10 |     █████████
    |     █████████
  9 |     █████████
    |     █████████
  8 |     █████████
    |     █████████
  7 |     █████████
    |     █████████
  6 |     █████████
    |     █████████
  5 |     █████████
    |     █████████
  4 |     █████████
    |     █████████
  3 |     █████████
    |     █████████
  2 |     █████████     ███
    |     █████████     ███
  1 |     █████████     ███     ███
    |     █████████     ███     ███
  0 |_____█████████_____███_____███_____
        [5,75)    [75,145)  [145,215]
        
        Bin Ranges
```

**Text Description:**
- X-axis: Bin ranges [5, 75), [75, 145), [145, 215]
- Y-axis: Frequency (count of values)
- Bin 1 [5, 75): Height = 9
- Bin 2 [75, 145): Height = 1
- Bin 3 [145, 215]: Height = 2

---

### c) Min-Max Normalization (3 marks)

#### Dataset:
```
Marks: [20, 50, 80, 100, 150]
```

**Given:**
- Score to normalize: X = 80
- Original range: X_min = 20, X_max = 150
- Formula: X' = a + ((X - X_min) × (b - a)) / (X_max - X_min)

---

#### i) Normalize to range [0, 1]

**Given:**
- a = 0 (new min)
- b = 1 (new max)
- X = 80
- X_min = 20
- X_max = 150

**Calculation:**
```
X' = 0 + ((80 - 20) × (1 - 0)) / (150 - 20)
X' = (60 × 1) / 130
X' = 60 / 130
X' = 0.4615 ≈ 0.462
```

**Answer: Normalized value = 0.462**

---

#### ii) Normalize to range [1, 10]

**Given:**
- a = 1 (new min)
- b = 10 (new max)
- X = 80
- X_min = 20
- X_max = 150

**Calculation:**
```
X' = 1 + ((80 - 20) × (10 - 1)) / (150 - 20)
X' = 1 + (60 × 9) / 130
X' = 1 + 540 / 130
X' = 1 + 4.1538
X' = 5.1538 ≈ 5.15
```

**Answer: Normalized value = 5.15**

---

## Question 2: Frequent Pattern Mining (6 marks)

### Transaction Database

**Transactions:**
- **T1:** {Bread, Cheese, Egg, Juice}
- **T2:** {Bread, Cheese, Juice}
- **T3:** {Bread, Milk}
- **T4:** {Bread, Juice, Milk}
- **T5:** {Cheese, Juice, Milk}

**Total transactions (n) = 5**

**Thresholds:**
- Minimum Support = 60% = 0.6
- Minimum Confidence = 75% = 0.75

**Minimum Support Count = 5 × 0.6 = 3 transactions**

---

### a) Illustrate the steps to follow in using the Apriori property to mine frequent patterns

**Apriori Algorithm Steps:**

#### Step 1: Generate Candidate 1-itemsets (C₁)

Count frequency of each item:

| Item   | Count | Support |
|--------|-------|---------|
| Bread  | 4     | 4/5 = 80% |
| Cheese | 3     | 3/5 = 60% |
| Egg    | 1     | 1/5 = 20% |
| Juice  | 4     | 4/5 = 80% |
| Milk   | 3     | 3/5 = 60% |

**Frequent 1-itemsets (L₁):**
- {Bread}: 4 (≥ 3) ✓
- {Cheese}: 3 (≥ 3) ✓
- {Juice}: 4 (≥ 3) ✓
- {Milk}: 3 (≥ 3) ✓
- {Egg}: 1 (< 3) ✗ (pruned)

**L₁ = {Bread, Cheese, Juice, Milk}**

---

#### Step 2: Generate Candidate 2-itemsets (C₂)

Join L₁ with itself (combinations of frequent 1-itemsets):

| Itemset        | Count | Support |
|----------------|-------|---------|
| {Bread, Cheese}| 2     | 2/5 = 40% |
| {Bread, Juice} | 3     | 3/5 = 60% |
| {Bread, Milk}  | 2     | 2/5 = 40% |
| {Cheese, Juice}| 3     | 3/5 = 60% |
| {Cheese, Milk} | 1     | 1/5 = 20% |
| {Juice, Milk}  | 2     | 2/5 = 40% |

**Frequent 2-itemsets (L₂):**
- {Bread, Juice}: 3 (≥ 3) ✓
- {Cheese, Juice}: 3 (≥ 3) ✓
- Others: < 3 ✗ (pruned)

**L₂ = {{Bread, Juice}, {Cheese, Juice}}**

---

#### Step 3: Generate Candidate 3-itemsets (C₃)

Join L₂ with itself (only if first k-1 items are the same):

From L₂ = {{Bread, Juice}, {Cheese, Juice}}

**Check for common prefix:**
- {Bread, Juice} and {Cheese, Juice} don't share a common first item
- Cannot form 3-itemset

**Alternative approach:** Check if {Bread, Cheese, Juice} is frequent:
- {Bread, Cheese, Juice}: Appears in T1, T2 → Count = 2 (< 3) ✗

**L₃ = {} (empty - no frequent 3-itemsets)**

---

#### Step 4: Stop (no more frequent itemsets)

**Final Frequent Itemsets:**
- **L₁:** {Bread}, {Cheese}, {Juice}, {Milk}
- **L₂:** {Bread, Juice}, {Cheese, Juice}
- **L₃:** {} (empty)

---

### b) Determine all strong association rules

**Strong association rules** must satisfy:
1. Support ≥ 60% (minimum support)
2. Confidence ≥ 75% (minimum confidence)

**Confidence Formula:**
```
Confidence(A → B) = Support(A ∪ B) / Support(A)
```

---

#### From Frequent 1-itemsets:

**No rules possible** (need at least 2 items for a rule)

---

#### From Frequent 2-itemsets:

**Rule 1: Bread → Juice**
- Support({Bread, Juice}) = 3/5 = 60% ✓
- Support({Bread}) = 4/5 = 80%
- Confidence = 60% / 80% = 0.75 = 75% ✓
- **Strong Rule:** ✓

**Rule 2: Juice → Bread**
- Support({Bread, Juice}) = 3/5 = 60% ✓
- Support({Juice}) = 4/5 = 80%
- Confidence = 60% / 80% = 0.75 = 75% ✓
- **Strong Rule:** ✓

**Rule 3: Cheese → Juice**
- Support({Cheese, Juice}) = 3/5 = 60% ✓
- Support({Cheese}) = 3/5 = 60%
- Confidence = 60% / 60% = 1.0 = 100% ✓
- **Strong Rule:** ✓

**Rule 4: Juice → Cheese**
- Support({Cheese, Juice}) = 3/5 = 60% ✓
- Support({Juice}) = 4/5 = 80%
- Confidence = 60% / 80% = 0.75 = 75% ✓
- **Strong Rule:** ✓

---

**Answer: All Strong Association Rules**

1. **Bread → Juice** (Support: 60%, Confidence: 75%)
2. **Juice → Bread** (Support: 60%, Confidence: 75%)
3. **Cheese → Juice** (Support: 60%, Confidence: 100%)
4. **Juice → Cheese** (Support: 60%, Confidence: 75%)

---

## Part B: Data Warehousing and Data Mining Concepts (15 marks)

---

## Question 3: Data Warehouse Concepts (8 marks)

### a) What is a data warehouse and how is it different from a database? (1+1 = 2 marks)

#### Data Warehouse Definition:

A **data warehouse** is a subject-oriented, integrated, time-variant, and non-volatile collection of data that supports management's decision-making process. It is a centralized repository that stores historical and aggregated data from multiple sources, organized for query and analysis rather than transaction processing.

**Key Characteristics:**
- **Subject-oriented:** Organized around major subjects (e.g., sales, customers, products)
- **Integrated:** Data from multiple sources is combined and made consistent
- **Time-variant:** Historical data is maintained over time
- **Non-volatile:** Data is not updated or deleted, only loaded and queried

---

#### Differences between Data Warehouse and Database:

| Aspect | Database | Data Warehouse |
|--------|----------|----------------|
| **Purpose** | Transaction processing (OLTP) | Analytical processing (OLAP) |
| **Data Type** | Current, operational data | Historical, aggregated data |
| **Update Frequency** | Real-time, frequent updates | Periodic batch loads |
| **Data Volume** | Smaller, current records | Large, historical data |
| **Users** | Operational staff, applications | Business analysts, decision-makers |
| **Query Type** | Simple, frequent, short transactions | Complex, analytical queries |
| **Normalization** | Highly normalized (3NF) | Denormalized (star/snowflake schema) |
| **Optimization** | Optimized for writes | Optimized for reads |
| **Data Sources** | Single application/system | Multiple heterogeneous sources |
| **Time Focus** | Current state | Historical trends |

**Summary:**
- **Database:** Designed for day-to-day operations, handles current transactions
- **Data Warehouse:** Designed for analysis, stores historical data for decision-making

---

### b) Explain the architecture of data mining systems (3 marks)

**Data Mining System Architecture:**

A data mining system typically consists of the following components:

#### 1. **Data Sources Layer**
- **Operational Databases:** Transactional systems (OLTP)
- **Data Warehouses:** Historical, aggregated data
- **Data Marts:** Department-specific data subsets
- **Flat Files:** CSV, Excel, text files
- **External Data Sources:** Web data, social media, IoT sensors

#### 2. **Data Integration and Cleaning Layer**
- **ETL Processes (Extract, Transform, Load):**
  - **Extract:** Gather data from various sources
  - **Transform:** Clean, normalize, aggregate, and format data
  - **Load:** Store transformed data in target system
- **Data Cleaning:** Handle missing values, outliers, inconsistencies
- **Data Integration:** Combine data from multiple sources
- **Data Transformation:** Normalization, discretization, feature selection

#### 3. **Data Storage Layer**
- **Data Warehouse:** Centralized repository
- **Data Marts:** Subject-specific warehouses
- **Operational Data Store (ODS):** Intermediate storage
- **Data Cubes:** Multi-dimensional data structures

#### 4. **Data Mining Engine**
- **Algorithms:** Classification, clustering, association rules, regression, etc.
- **Pattern Discovery:** Finding hidden patterns and relationships
- **Model Building:** Creating predictive or descriptive models
- **Techniques:**
  - Decision trees
  - Neural networks
  - Association rules (Apriori, FP-Growth)
  - Clustering (K-means, hierarchical)
  - Classification (Naive Bayes, SVM)

#### 5. **Pattern Evaluation Layer**
- **Interestingness Measures:** Support, confidence, lift
- **Statistical Tests:** Significance testing
- **Validation:** Cross-validation, holdout testing
- **Model Assessment:** Accuracy, precision, recall, F-measure

#### 6. **Knowledge Base**
- **Domain Knowledge:** Business rules, constraints
- **Metadata:** Data dictionaries, schemas
- **User Knowledge:** Prior knowledge, expectations
- **Pattern Templates:** Known patterns to guide search

#### 7. **User Interface Layer**
- **Query Interface:** Allow users to specify mining tasks
- **Visualization Tools:** Charts, graphs, dashboards
- **Report Generation:** Present discovered patterns
- **Interactive Mining:** User-guided exploration

#### 8. **Application Layer**
- **Business Applications:** CRM, fraud detection, market analysis
- **Decision Support Systems:** Help managers make decisions
- **Reporting Tools:** Generate business reports

**Architecture Flow:**
```
Data Sources → ETL → Data Warehouse → Data Mining Engine → Pattern Evaluation → Knowledge Base → User Interface → Applications
```

---

### c) What are the key components of a Data Warehouse? (3 marks)

**Key Components of a Data Warehouse:**

#### 1. **Data Sources**
- **Operational Systems:** Transactional databases (OLTP)
- **External Sources:** Third-party data, market data
- **Legacy Systems:** Older applications and databases
- **Flat Files:** CSV, Excel, text files

#### 2. **ETL (Extract, Transform, Load) Tools**
- **Extract:** Pull data from source systems
- **Transform:** Clean, validate, aggregate, and format data
  - Data cleaning (handle missing values, duplicates)
  - Data transformation (normalization, calculations)
  - Data integration (combine from multiple sources)
- **Load:** Load transformed data into the warehouse

#### 3. **Data Warehouse Database**
- **Central Repository:** Stores integrated, historical data
- **Storage Architecture:**
  - Relational databases (RDBMS)
  - Columnar databases (optimized for analytics)
  - Distributed storage systems
- **Data Organization:**
  - Star schema
  - Snowflake schema
  - Fact constellation schema

#### 4. **Metadata**
- **Technical Metadata:** Data types, schemas, ETL processes
- **Business Metadata:** Business definitions, data lineage
- **Operational Metadata:** Data quality, load statistics
- **Metadata Repository:** Central catalog of all metadata

#### 5. **Data Marts**
- **Departmental Subsets:** Focused on specific business areas
- **Examples:** Sales data mart, HR data mart, Finance data mart
- **Benefits:** Faster access, easier management

#### 6. **OLAP (Online Analytical Processing) Engine**
- **Multi-dimensional Analysis:** Analyze data across dimensions
- **OLAP Operations:**
  - **Roll-up:** Aggregate to higher levels
  - **Drill-down:** Navigate to detailed levels
  - **Slice:** Select specific dimension value
  - **Dice:** Select specific values from multiple dimensions
  - **Pivot:** Rotate data view

#### 7. **Query and Reporting Tools**
- **Ad-hoc Query Tools:** Allow users to create custom queries
- **Reporting Tools:** Generate standard and custom reports
- **Dashboard Tools:** Visual representation of key metrics
- **BI Tools:** Business Intelligence platforms

#### 8. **Data Mining Tools**
- **Pattern Discovery:** Find hidden patterns
- **Predictive Analytics:** Forecast future trends
- **Classification and Clustering:** Group and categorize data

#### 9. **Data Warehouse Administration**
- **Security:** Access control, authentication, authorization
- **Performance Tuning:** Indexing, partitioning, optimization
- **Backup and Recovery:** Data protection strategies
- **Monitoring:** Track system performance and data quality

#### 10. **User Access Tools**
- **Query Interfaces:** SQL, MDX (Multi-dimensional Expressions)
- **Visualization Tools:** Charts, graphs, heat maps
- **Mobile Access:** Access from mobile devices
- **API Access:** Programmatic access for applications

**Summary:**
The key components work together to extract data from sources, transform and integrate it, store it in an organized manner, and provide tools for analysis and decision-making.

---

## Question 4: Data Warehouse Schema and Cuboids (7 marks)

### Scenario

**Data Warehouse Dimensions:**
- **Date** (D)
- **Student** (S)
- **Location** (L)
- **University** (U)

**Measures:**
- **Count** (number of students)
- **Fees** (lodging fee paid by student)

**Business Rules:**
- Fee is the lodging fee that a student pays when attending a university at a given date
- Students can be **male or female**
- Students can be on **public or private programs**
- Each category has its own fee

---

### a) Draw a constellation schema diagram for the data warehouse (3 marks)

**Constellation Schema (Fact Constellation):**

A constellation schema has multiple fact tables sharing dimension tables.

**Dimensions:**
1. **Date Dimension (Dim_Date)**
   - DateID (PK)
   - Date
   - Day, Month, Year
   - Quarter, Semester

2. **Student Dimension (Dim_Student)**
   - StudentID (PK)
   - StudentName
   - Gender (Male/Female)
   - ProgramType (Public/Private)

3. **Location Dimension (Dim_Location)**
   - LocationID (PK)
   - City
   - Region
   - Country

4. **University Dimension (Dim_University)**
   - UniversityID (PK)
   - UniversityName
   - UniversityType
   - Address

**Fact Table:**
**Fact_StudentFees**
- DateID (FK → Dim_Date)
- StudentID (FK → Dim_Student)
- LocationID (FK → Dim_Location)
- UniversityID (FK → Dim_University)
- Count (Measure)
- Fees (Measure)

**Schema Diagram:**

```
                    ┌──────────────┐
                    │  Dim_Date    │
                    ├──────────────┤
                    │ DateID (PK)  │
                    │ Date         │
                    │ Day, Month   │
                    │ Year         │
                    └──────┬───────┘
                           │
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        │                  │                  │
┌───────▼───────┐  ┌───────▼───────┐  ┌───────▼───────┐
│ Dim_Student   │  │Dim_Location   │  │Dim_University │
├───────────────┤  ├───────────────┤  ├───────────────┤
│ StudentID(PK) │  │ LocationID(PK)│  │ UniversityID  │
│ StudentName   │  │ City          │  │ UniversityName │
│ Gender        │  │ Region        │  │ UniversityType│
│ ProgramType   │  │ Country       │  │ Address       │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           │
                  ┌────────▼─────────┐
                  │ Fact_StudentFees│
                  ├──────────────────┤
                  │ DateID (FK)      │
                  │ StudentID (FK)   │
                  │ LocationID (FK)   │
                  │ UniversityID (FK)│
                  │ Count (Measure)  │
                  │ Fees (Measure)   │
                  └──────────────────┘
```

**Text Description:**
- **Fact Table:** Fact_StudentFees (center)
- **Dimension Tables:** Dim_Date, Dim_Student, Dim_Location, Dim_University (surrounding)
- **Relationships:** Many-to-one from Fact to each Dimension
- **Measures:** Count and Fees stored in the fact table

---

### b) Starting with the base cuboid [date as D, students as S, location as L, university as U], represent the cuboid of this problem (4 marks)

**Base Cuboid:** [D, S, L, U] - All dimensions at the lowest level

**Cuboid Lattice:**

A cuboid represents a specific level of aggregation. The full lattice includes all possible combinations of dimensions.

**Notation:**
- **D** = Date dimension
- **S** = Student dimension
- **L** = Location dimension
- **U** = University dimension
- **ALL** = Aggregated (dimension removed)

---

#### All Possible Cuboids:

**Level 4 (Base Cuboid - 0 dimensions aggregated):**
1. **[D, S, L, U]** - Base cuboid (most detailed)

**Level 3 (1 dimension aggregated - 4 cuboids):**
2. **[ALL, S, L, U]** - Aggregate over Date
3. **[D, ALL, L, U]** - Aggregate over Student
4. **[D, S, ALL, U]** - Aggregate over Location
5. **[D, S, L, ALL]** - Aggregate over University

**Level 2 (2 dimensions aggregated - 6 cuboids):**
6. **[ALL, ALL, L, U]** - Aggregate over Date and Student
7. **[ALL, S, ALL, U]** - Aggregate over Date and Location
8. **[ALL, S, L, ALL]** - Aggregate over Date and University
9. **[D, ALL, ALL, U]** - Aggregate over Student and Location
10. **[D, ALL, L, ALL]** - Aggregate over Student and University
11. **[D, S, ALL, ALL]** - Aggregate over Location and University

**Level 1 (3 dimensions aggregated - 4 cuboids):**
12. **[ALL, ALL, ALL, U]** - Aggregate over Date, Student, Location
13. **[ALL, ALL, L, ALL]** - Aggregate over Date, Student, University
14. **[ALL, S, ALL, ALL]** - Aggregate over Date, Location, University
15. **[D, ALL, ALL, ALL]** - Aggregate over Student, Location, University

**Level 0 (All dimensions aggregated - 1 cuboid):**
16. **[ALL, ALL, ALL, ALL]** - Apex cuboid (total aggregation)

---

#### Cuboid Representation:

```
                    [ALL, ALL, ALL, ALL]
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
[ALL,ALL,ALL,U]    [ALL,ALL,L,ALL]    [ALL,S,ALL,ALL]    [D,ALL,ALL,ALL]
        │                  │                  │                  │
        └──────────────────┼──────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
[ALL,ALL,L,U]    [ALL,S,ALL,U]    [ALL,S,L,ALL]    [D,ALL,ALL,U]    [D,ALL,L,ALL]    [D,S,ALL,ALL]
        │                  │                  │                  │                  │
        └──────────────────┼──────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
[ALL,S,L,U]    [D,ALL,L,U]    [D,S,ALL,U]    [D,S,L,ALL]
        │                  │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    [D, S, L, U]
                  (Base Cuboid)
```

**Total Number of Cuboids:**
- Formula: 2^n where n = number of dimensions
- n = 4 dimensions
- Total cuboids = 2^4 = 16 cuboids

**Answer:**
The cuboid lattice contains **16 cuboids** total:
- 1 base cuboid: [D, S, L, U]
- 4 cuboids with 1 dimension aggregated
- 6 cuboids with 2 dimensions aggregated
- 4 cuboids with 3 dimensions aggregated
- 1 apex cuboid: [ALL, ALL, ALL, ALL]

Each cuboid represents a different level of data aggregation, allowing for analysis at various granularities from detailed (base) to highly summarized (apex).

---

## Summary

### Part A: Data Pre-processing and Frequent Pattern Mining (15 marks)
- **Question 1:** Equal-frequency/equal-width binning, smoothing, min-max normalization
- **Question 2:** Apriori algorithm for frequent pattern mining, association rule generation

### Part B: Data Warehousing and Data Mining Concepts (15 marks)
- **Question 3:** Data warehouse definition, differences from databases, system architecture, components
- **Question 4:** Constellation schema design, cuboid lattice representation

---

## Key Formulas

### Min-Max Normalization:
```
X' = a + ((X - X_min) × (b - a)) / (X_max - X_min)
```

### Support:
```
Support(A) = (Number of transactions containing A) / (Total transactions)
```

### Confidence:
```
Confidence(A → B) = Support(A ∪ B) / Support(A)
```

### Number of Cuboids:
```
Total Cuboids = 2^n
where n = number of dimensions
```

---

**End of Solutions**

**Course:** DSC603 - Data Mining  
**Institution:** University of Buea  
**Test Date:** January 2026  
**Total Marks:** 30
