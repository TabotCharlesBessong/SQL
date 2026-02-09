# Summary: DSC603 Data Warehousing and On-Line Analytical Processing (OLAP)

## Document Outline
- Data Warehouse: Basic Concepts
- Data Warehouse Modeling: Data Cube and OLAP
- Data Warehouse Design and Usage
- Data Warehouse Implementation
- Data Generalization by Attribute-Oriented Induction
- Summary

---

## 1. Data Warehouse: Basic Concepts

### What Is a Data Warehouse?
- **Definitions (operational):**
  - A **decision support database** maintained separately from the organization’s operational database.
  - Provides a **solid platform of consolidated, historical data** for analysis.
- **Classic definition:** “A data warehouse is a **subject-oriented**, **integrated**, **time-variant**, and **nonvolatile** collection of data in support of management’s decision-making process.”
- **Data warehousing:** The process of constructing and using data warehouses.

### Four Properties

**Subject-oriented**
- Organized around major subjects (e.g., customer, product, sales).
- Focus on modeling and analysis for decision makers, not daily operations or transaction processing.
- Presents a simple, concise view on subject issues and excludes data not useful for decision support.

**Integrated**
- Built by integrating **multiple, heterogeneous sources** (e.g., relational DBs, flat files, on-line transaction records).
- **Data cleaning and integration** ensure consistency: naming, encoding, attribute measures, etc.
- **Example:** Hotel price—currency, tax, breakfast, etc. When data is moved to the warehouse, it is converted to a common representation.

**Time-variant**
- Time horizon is **much longer** than in operational systems.
  - Operational DB: current value data.
  - Data warehouse: historical perspective (e.g., past 5–10 years).
- Every key in the warehouse contains a **time element** (explicit or implicit).
- Operational keys may or may not contain a time element.

**Nonvolatile**
- **Physically separate** store of data transformed from the operational environment.
- **No operational updates** in the warehouse (no transaction processing, recovery, concurrency control).
- Only two kinds of operations: **initial loading** and **read access**.

### OLTP vs. OLAP

| | OLTP | OLAP |
|---|------|------|
| **Users** | Clerk, IT professional | Knowledge worker |
| **Function** | Day-to-day operations | Decision support |
| **DB design** | Application-oriented | Subject-oriented |
| **Data** | Current, up-to-date, detailed, flat relational, isolated | Historical, summarized, multidimensional, integrated |
| **Usage** | Repetitive | Ad-hoc |
| **Access** | Read/write, index/hash on primary key, lots of scans | Read, complex queries |
| **Unit of work** | Short, simple transaction | Complex query |
| **# records accessed** | Tens | Millions |
| **# users** | Thousands | Hundreds |
| **DB size** | 100 MB–GB | 100 GB–TB |
| **Metric** | Transaction throughput | Query throughput, response |

### Why a Separate Data Warehouse?
- **Performance:** DBMS tuned for OLTP (access methods, indexing, concurrency, recovery); warehouse tuned for OLAP (complex queries, multidimensional view, consolidation).
- **Different data needs:**
  - **Historical data:** Decision support needs history that operational DBs often do not keep.
  - **Consolidation:** Aggregation and summarization from heterogeneous sources.
  - **Data quality:** Reconciling inconsistent representations, codes, and formats across sources.
- **Note:** Some systems do OLAP directly on relational databases.

### Multi-Tiered Architecture (Example)
- **Data sources:** Operational DBs, other sources.
- **ETL:** Extract, Transform, Load; Refresh.
- **Monitor & Integrator,** **Metadata.**
- **Data storage:** Data Warehouse; Data Marts.
- **OLAP Server,** **OLAP Engine.**
- **Front-end tools:** Analysis, Query, Reports, Data mining.

### Three Data Warehouse Models
- **Enterprise warehouse:** All information about subjects spanning the entire organization.
- **Data mart:** Subset of corporate-wide data for a specific group (e.g., marketing data mart). Can be **independent** or **dependent** (sourced from the warehouse).
- **Virtual warehouse:** Set of views over operational databases; only some summary views may be materialized.

### Extraction, Transformation, and Loading (ETL)
- **Extraction:** Get data from multiple, heterogeneous, external sources.
- **Cleaning:** Detect and correct errors.
- **Transformation:** Convert from legacy/host format to warehouse format.
- **Load:** Sort, summarize, consolidate, compute views, check integrity, build indices and partitions.
- **Refresh:** Propagate updates from sources to the warehouse.

### Metadata Repository
Metadata defines warehouse objects. It stores:
- **Structure:** Schema, views, dimensions, hierarchies, derived data definitions, data mart locations and contents.
- **Operational:** Data lineage, currency (active/archived/purged), monitoring (usage, errors, audit).
- **Algorithms** used for summarization.
- **Mapping** from operational environment to the warehouse.
- **Performance-related** data (schema, views, derived definitions).
- **Business data:** Business terms, definitions, ownership, charging policies.

---

## 2. Data Warehouse Modeling: Data Cube and OLAP

### From Tables and Spreadsheets to Data Cubes
- Data warehouse is based on a **multidimensional data model**; data is viewed as a **data cube**.
- **Dimensions:** e.g., item (item_name, brand, type), time (day, week, month, quarter, year).
- **Fact table:** Contains **measures** (e.g., dollars_sold) and **keys** to each dimension table.
- **Base cuboid:** n-D base cube. **Apex cuboid:** 0-D, highest-level summarization. The **lattice of cuboids** forms the data cube.

### Cube: Lattice of Cuboids (Example)
- **0-D (apex):** all.
- **1-D:** time; item; location; supplier.
- **2-D:** time,item; time,location; time,supplier; item,location; item,supplier; location,supplier.
- **3-D:** time,item,location; time,item,supplier; time,location,supplier; item,location,supplier.
- **4-D (base):** time, item, location, supplier.

### Conceptual Modeling: Star, Snowflake, Fact Constellation
- **Star schema:** One **fact table** in the middle connected to **dimension tables**.
- **Snowflake schema:** Star schema refined by normalizing some dimension hierarchies into smaller dimension tables (snowflake shape).
- **Fact constellation:** Multiple fact tables share dimension tables (galaxy schema).

### Example: Star Schema
- **Fact table (Sales):** time_key, item_key, branch_key, location_key, **units_sold**, **dollars_sold**, **avg_sales** (measures).
- **Dimensions:** time (time_key, day, day_of_the_week, month, quarter, year), item (item_key, item_name, brand, type, supplier_type), branch (branch_key, branch_name, branch_type), location (location_key, street, city, state_or_province, country).

### Example: Snowflake Schema
- Same fact table; **location** normalized: location_key, street, **city_key** → city (city_key, city, state_or_province, country).
- **Item** normalized: item_key, item_name, brand, type, **supplier_key** → supplier (supplier_key, supplier_type).

### Example: Fact Constellation
- **Sales fact table:** time_key, item_key, branch_key, location_key, units_sold, dollars_sold, avg_sales.
- **Shipping fact table:** time_key, item_key, shipper_key, from_location, to_location, dollars_cost, units_shipped.
- **Shared dimensions:** time, location, item, branch; **shipper** dimension for shipping.

### Concept Hierarchy Example: Dimension “Location”
- Levels: **all** → **region** (e.g., Europe, Africa) → **country** (e.g., Nigeria, Cameroon, Spain, Germany) → **office/city** (e.g., Bafoussam, Buea, Frankfurt).

### Data Cube Measures: Three Categories
- **Distributive:** Result over n aggregates = result over full data without partitioning.  
  **E.g.,** count(), sum(), min(), max().
- **Algebraic:** Computed by an algebraic function of M arguments (M bounded), each from a distributive aggregate.  
  **E.g.,** avg(), min_N(), standard_deviation().
- **Holistic:** No constant bound on storage for subaggregates.  
  **E.g.,** median(), mode(), rank().

### Multidimensional Data Example
- **Sales volume** as a function of **product**, **month**, **region**.
- **Dimensions:** Product, Location, Time.
- **Hierarchical summarization paths:** e.g., Industry → Category → Product; Region → Country → City; Year → Quarter → Month → Week → Day.

### Sample Data Cube Example
- Total annual sales of **TVs in U.S.A.**; dimensions: Product (TV, VCR, PC), Date (1Qtr–4Qtr), Country (U.S.A., Canada, Mexico); measure: sum.

### Cuboids for That Cube
- 0-D: all.
- 1-D: product; date; country.
- 2-D: product,date; product,country; date,country.
- 3-D (base): product, date, country.

### Typical OLAP Operations
- **Roll-up (drill-up):** Summarize by climbing a hierarchy or reducing dimensions.
- **Drill-down (roll-down):** From higher-level summary to lower-level or detail; or add dimensions.
- **Slice and dice:** Project and select.
- **Pivot (rotate):** Reorient the cube (e.g., 3D to 2D planes) for visualization.
- **Others:** Drill across (more than one fact table); drill through (through cube to backend relational tables via SQL).

### Star-Net Query Model Example
- **Each circle = footprint.** Dimensions: Customer (Customer → Order → …), Product (Product Item → Product Line → Product Group), Location (City → Country → Region), Time (Daily → Qtrly → Annually), plus Shipping Method, Organization (Sales Person → District → Division), Promotion.

---

## 3. Data Warehouse Design and Usage

### Design: Four Views (Business Analysis Framework)
- **Top-down view:** Select relevant information for the warehouse.
- **Data source view:** What is captured, stored, and managed in operational systems.
- **Data warehouse view:** Fact tables and dimension tables.
- **Business query view:** End-user perspective on warehouse data.

### Data Warehouse Design Process
- **Approaches:** Top-down (overall design, mature) or bottom-up (experiments, prototypes), or combined.
- **Software engineering:** Waterfall (structured, stepwise) or spiral (rapid, iterative).
- **Typical steps:**
  1. Choose a **business process** to model (e.g., orders, invoices).
  2. Choose the **grain** (atomic level of data).
  3. Choose **dimensions** for each fact table record.
  4. Choose **measures** for each fact table record.

### Data Warehouse Development: Recommended Approach (Example)
- Define a high-level **corporate data model**.
- Build **data marts** (with model refinement).
- Evolve to **distributed data marts** then **multi-tier** or **enterprise data warehouse** (with model refinement).

### Data Warehouse Usage: Three Kinds of Applications
1. **Information processing:** Querying, basic statistics, reporting (crosstabs, tables, charts, graphs).
2. **Analytical processing:** Multidimensional analysis; OLAP (slice, dice, drill, pivot).
3. **Data mining:** Discovery of hidden patterns; associations, analytical models, classification and prediction; visualization.

### From OLAP to OLAM (On-Line Analytical Mining)
- **Why OLAM?**
  - High-quality data in DW (integrated, consistent, cleaned).
  - Existing infrastructure (ODBC, OLEDB, Web, reporting, OLAP).
  - OLAP-based exploration (drilling, dicing, pivoting).
  - On-line choice of mining functions, algorithms, and tasks.

---

## 4. Data Warehouse Implementation

### Efficient Data Cube Computation
- Cube = **lattice of cuboids.** Bottom = base cuboid; top = apex (one cell).
- **Number of cuboids:** For n dimensions with L_i levels each:  
  \( T = \prod_{i=1}^{n}(L_i + 1) \).
- **Materialization:** Full (every cuboid), none, or **partial** (choose which cuboids to materialize by size, sharing, access frequency, etc.).

### The “Compute Cube” Operator
- **DMQL example:**  
  `define cube sales [item, city, year]: sum(sales_in_dollars)`  
  `compute cube sales`
- **SQL-like (Gray et al. ’96):**  
  `SELECT item, city, year, SUM(amount) FROM SALES CUBE BY item, city, year`
- **Group-bys to compute:** (date, product, customer), (date, product), (date, customer), (product, customer), (date), (product), (customer), ().

### Indexing OLAP Data: Bitmap Index
- Index on one column; each **value** has a **bit vector** (length = number of rows in base table).
- **i-th bit = 1** if the i-th row has that value for the column.
- **Fast** bit operations; **not suitable for high-cardinality** domains.

### Bitmap Index Example
- **Base table:** Cust, Region, Type (e.g., C1 Asia Retail, C2 Europe Dealer, …).
- **Index on Region:** RecID vs. Asia, Europe, America (1/0).
- **Index on Type:** RecID vs. Retail, Dealer (1/0).

### Join Indices
- **Join index:** JI(R-id, S-id) for R ⋈ S.
- Materializes the join and speeds up relational join.
- In warehouses: links **dimension values** (e.g., city, product) to **rows in the fact table** (e.g., Sales). Can span multiple dimensions.

### Efficient Processing of OLAP Queries
- Map drill, roll, etc., to SQL and/or OLAP operations (e.g., dice = selection + projection).
- **Choose which materialized cuboid(s)** to use for the query.

#### Exercise (from document) – Which cuboid to use?
**Query:** On **{brand, province_or_state}** with condition **year = 2004**.  
**Materialized cuboids:**
1. {year, item_name, city}
2. {year, brand, country}
3. {year, brand, province_or_state}
4. {item_name, province_or_state} where year = 2004

**Answer:** Use **cuboid 3) {year, brand, province_or_state}**. It contains exactly the dimensions requested (brand, province_or_state) and the attribute needed for the condition (year). It can be sliced for year = 2004 and then used for brand and province_or_state.  
- (1) has city and item_name, not brand/province_or_state.  
- (2) has country, not province_or_state.  
- (4) has year only in the condition and item_name as dimension; it does not have brand and is less direct than (3).

### OLAP Server Architectures
- **ROLAP:** Relational or extended-relational DBMS + OLAP middleware; backend and aggregation logic optimized; **greater scalability**.
- **MOLAP:** Sparse **array-based** multidimensional storage; fast indexing to precomputed summaries.
- **HOLAP** (e.g., Microsoft SQL Server): Hybrid—e.g., low level relational, high level array.
- **Specialized SQL servers** (e.g., Redbricks): Optimized for star/snowflake schemas.

---

## 5. Data Generalization by Attribute-Oriented Induction

### Attribute-Oriented Induction (AOI)
- Proposed at KDD workshop 1989.
- Not limited to categorical data or specific measures.
- **Steps:**
  1. **Collect** task-relevant data (initial relation) via a relational query.
  2. **Generalize** by attribute removal or attribute generalization.
  3. **Aggregate** by merging identical generalized tuples and accumulating counts.
  4. **Present** results (with user interaction).

### Example: Describe Graduate Students
- **Step 1 – SQL:**  
  `Select * from student where student_status in {'Msc', 'MBA', 'PhD'}`
  (attributes: name, gender, major, birth_place, birth_date, residence, phone#, gpa).
- **Step 2:** Attribute-oriented induction (remove/generalize attributes).
- **Step 3:** Present as generalized relation, cross-tab, or rules.

### Class Characterization Example (Initial Relation)
- Rows: Name, Gender, Major, Birth-Place, Birth_date, Residence, Phone#, GPA (e.g., Jim Woodman M CS Vancouver…; Scott Lachance M CS Montreal…; Laura Lee F Physics Seattle…).
- **Removed:** Name, Birth_date, Phone#; **Retained/Generalized:** Gender; Major → Sci, Eng, Bus; Birth_place → Country; Birth_date → Age range; Residence → City; GPA → Excl, VG, …

### Class Characterization Example (Prime Generalized Relation)
- **Table:** Gender, Major, Birth_region, Age_range, Residence, GPA, **Count**  
  (e.g., M, Science, Canada, 20–25, Richmond, Very-good, 16; F, Science, Foreign, 25–30, Burnaby, Excellent, 22; …).
- **Cross-tab (Birth_Region × Gender):** Canada/ Foreign vs. M/F with totals (e.g., M Canada 16, M Foreign 14, F Canada 10, F Foreign 22; Total 62).

### Basic Principles of AOI
- **Data focusing:** Task-relevant data → initial relation.
- **Attribute removal:** Remove A if many distinct values and (1) no generalization operator on A, or (2) higher-level concepts for A are expressed by other attributes.
- **Attribute generalization:** If many distinct values and generalization operators exist, choose one and generalize A.
- **Attribute-threshold control:** Typically 2–8 (specified or default).
- **Generalized relation threshold:** Control final relation/rule size.

### Basic Algorithm
- **InitialRel:** Query → task-relevant data → initial relation.
- **PreGen:** From distinct-value counts per attribute, decide: remove or how high to generalize.
- **PrimeGen:** Execute generalization to the right level → “prime generalized relation” with counts.
- **Presentation:** User adjusts levels (drill), pivot, map to rules, cross-tabs, visualizations.

### Presentation of Generalized Results
- **Generalized relation:** Attributes generalized; counts or other aggregates.
- **Cross-tabulation:** Like contingency tables.
- **Visualization:** Pie charts, bar charts, curves, cubes, etc.
- **Quantitative characteristic rules:**  
  E.g., “grad(x) ⟹ birth_region(x)=Canada ∨ birth_region(x)=foreign” with percentages (e.g., 47% Canada, 53% foreign).

### Mining Class Comparisons
- **Goal:** Compare two or more classes.
- **Method:** Partition data into target and contrasting class(es); generalize both to same high-level concepts; compare tuples with same high-level description; for each tuple present **support** (within-class distribution) and **comparison** (between-class); highlight strong discriminant features.
- **Relevance analysis:** Find attributes that best distinguish classes.

### Concept Description vs. Cube-Based OLAP
- **Similar:** Data generalization; summarization at multiple levels; interactive drill, pivot, slice, dice.
- **Differences:**
  - OLAP: Systematic preprocessing, query-independent, can drill to low level.
  - AOI: Automated choice of level; may do dimension relevance/ranking when many dimensions; can work on data not in relational form.

---

## 6. Summary (From the Document)

- **Data warehousing:** Multi-dimensional model; data cube = dimensions + measures; star, snowflake, fact constellations; OLAP = drill, roll, slice, dice, pivot.
- **Architecture, design, usage:** Multi-tiered architecture; business analysis framework; information processing, analytical processing, data mining, OLAM.
- **Implementation:** Efficient cube computation; full/partial/no materialization; indexing (bitmap, join index); OLAP query processing; ROLAP, MOLAP, HOLAP.
- **Data generalization:** Attribute-oriented induction.

---

## Note on Exercises and Assignments

This PDF is a **57-slide lecture** on Data Warehousing and OLAP. It contains **one explicit exercise** (which materialized cuboid to select for a given query); the answer is provided in Section 4 above. There are no other numbered exercises or assignments in the document; the “answers” are the concepts and examples summarized here. If you have a separate problem set or assignment sheet, share it for answer drafting.
