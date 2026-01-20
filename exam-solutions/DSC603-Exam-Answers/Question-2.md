# Question 2: Data Warehousing - Star Schema and OLAP
## DSC 603 - Data Mining
**Total Marks: 15 marks (Elective)**

---

## Problem Statement

**Data Warehouse Scenario:**
A data warehouse has four dimensions:
- **Date**
- **Spectator** (categorized as: students, adults, seniors - each with different charge rates)
- **Location** (e.g., GM Place)
- **Game**

Two measures:
- **Count** (number of spectators)
- **Charge** (fare paid by spectator)

**Tasks:**
1. Draw a star schema diagram
2. Describe OLAP operations to list total charge paid by student spectators at GM Place in 2021
3. Explain bitmap indexing (assuming part 3 continues from question about bitmap indexing)

---

## Part 1: Star Schema Diagram (5 marks)

### **Star Schema Overview**

**Star Schema Structure:**
- **Central Fact Table:** Contains measures and foreign keys to dimension tables
- **Dimension Tables:** Surround the fact table (like a star)
- **One-to-Many Relationship:** Each dimension table relates to the fact table

### **Fact Table: FACT_TICKET_SALES**

**Attributes:**
- **Primary Key:** Ticket_ID (surrogate key)
- **Foreign Keys:**
  - Date_ID (→ DIM_DATE)
  - Spectator_ID (→ DIM_SPECTATOR)
  - Location_ID (→ DIM_LOCATION)
  - Game_ID (→ DIM_GAME)
- **Measures:**
  - Count (number of tickets/spectators)
  - Charge (fare amount paid)

### **Dimension Tables**

#### **1. DIM_DATE**
- **Primary Key:** Date_ID
- **Attributes:**
  - Date (full date)
  - Day
  - Week
  - Month
  - Quarter
  - Year
  - Day_of_Week
  - Is_Weekend (boolean)

#### **2. DIM_SPECTATOR**
- **Primary Key:** Spectator_ID
- **Attributes:**
  - Spectator_Type (student, adult, senior)
  - Charge_Rate (rate per ticket for this spectator type)
  - Description

#### **3. DIM_LOCATION**
- **Primary Key:** Location_ID
- **Attributes:**
  - Location_Name (e.g., "GM Place")
  - City
  - State/Province
  - Capacity
  - Address

#### **4. DIM_GAME**
- **Primary Key:** Game_ID
- **Attributes:**
  - Game_Name
  - Game_Type
  - Sport_Type
  - Season
  - Description

### **Star Schema Diagram**

```
                    ┌─────────────────────┐
                    │   DIM_DATE          │
                    ├─────────────────────┤
                    │ Date_ID (PK)        │
                    │ Date                │
                    │ Day, Month, Year    │
                    │ Quarter, Week       │
                    └──────────┬──────────┘
                               │
                               │ 1
                               │
                               │ Many
                    ┌──────────┴──────────┐
                    │                     │
        ┌───────────┴──────────┐         │
        │                       │         │
┌───────┴────────┐    ┌────────┴───────┐ │
│ DIM_SPECTATOR  │    │ DIM_LOCATION   │ │
├────────────────┤    ├────────────────┤ │
│Spectator_ID(PK)│    │Location_ID(PK) │ │
│Spectator_Type  │    │Location_Name   │ │
│Charge_Rate     │    │City            │ │
│Description     │    │Capacity        │ │
└───────┬────────┘    └────────┬───────┘ │
        │                      │         │
        │ 1                    │ 1       │ 1
        │                      │         │
        │ Many                 │ Many    │ Many
        │                      │         │
        └──────────┬───────────┴─────────┘
                   │
        ┌──────────┴──────────────────┐
        │   FACT_TICKET_SALES         │
        ├─────────────────────────────┤
        │ Ticket_ID (PK)              │
        │ Date_ID (FK)                │
        │ Spectator_ID (FK)           │
        │ Location_ID (FK)            │
        │ Game_ID (FK)                │
        │ Count (Measure)             │
        │ Charge (Measure)            │
        └──────────┬──────────────────┘
                   │
                   │ Many
                   │
        ┌──────────┴─────────┐
        │    DIM_GAME        │
        ├────────────────────┤
        │ Game_ID (PK)       │
        │ Game_Name          │
        │ Game_Type          │
        │ Sport_Type         │
        │ Season             │
        └────────────────────┘
```

### **Textual Representation**

**Relationships:**
- FACT_TICKET_SALES (1) ←→ (Many) DIM_DATE
- FACT_TICKET_SALES (1) ←→ (Many) DIM_SPECTATOR
- FACT_TICKET_SALES (1) ←→ (Many) DIM_LOCATION
- FACT_TICKET_SALES (1) ←→ (Many) DIM_GAME

**Key Points:**
- Fact table is at the center
- Dimension tables surround it (star shape)
- Each dimension relates to fact table via foreign key
- Measures (Count, Charge) are in the fact table
- Dimensions contain descriptive attributes

---

## Part 2: OLAP Operations (5 marks)

### **Base Cuboid**
Given: `[date as D, spectator as S, location as L, game as G]`

This represents the **base cuboid** with all dimensions at their lowest level (most detailed).

### **Query Goal**
"List the total charge paid by student spectators at GM Place in 2021"

**Required Output:**
- Total Charge
- Filtered by:
  - Spectator Type = "Student"
  - Location = "GM Place"
  - Year = 2021

### **OLAP Operations Required**

#### **Step 1: Slice Operation**

**Slice on Spectator Dimension:**
- **Operation:** Slice on `Spectator_Type = "Student"`
- **Result:** Cuboid containing only student spectator data
- **Effect:** Filters the cube to show only student spectator transactions

**Slice on Location Dimension:**
- **Operation:** Slice on `Location_Name = "GM Place"`
- **Result:** Cuboid containing only GM Place data
- **Effect:** Filters the cube to show only transactions at GM Place

**Slice on Date Dimension:**
- **Operation:** Slice on `Year = 2021`
- **Result:** Cuboid containing only 2021 data
- **Effect:** Filters the cube to show only transactions in 2021

**Combined Slicing:**
After all three slices:
- Only student spectator transactions
- Only at GM Place
- Only in 2021
- All games (Game dimension not filtered)

#### **Step 2: Roll-up Operation**

**Roll-up on Date Dimension:**
- **From:** Day level → **To:** Year level
- **Operation:** Aggregate from detailed date to year level
- **Effect:** Groups all 2021 dates together

**Roll-up on Game Dimension (Optional but implied):**
- **From:** Individual game level → **To:** ALL level (or aggregate across all games)
- **Operation:** Aggregate across all games
- **Effect:** Sums charge across all games (since query asks for total)

**Roll-up on Spectator Dimension:**
- **From:** Individual spectator level → **To:** Spectator Type level (already at student level from slice)

**Resulting Cuboid:**
After roll-up, we have aggregated data at:
- Date: Year level (2021)
- Spectator: Student type
- Location: GM Place
- Game: ALL (aggregated across all games)

#### **Step 3: Dice Operation (Alternative View)**

**Dice Operation:**
- **Operation:** Select a subcube with specific dimension values
- **Conditions:**
  - Spectator = "Student"
  - Location = "GM Place"
  - Date (Year) = 2021
  - Game = ALL (or all games)

**Result:** Subcube with specified constraints

#### **Step 4: Aggregate (Sum) Operation**

**Aggregate Measure:**
- **Operation:** SUM(Charge)
- **Effect:** Sums the Charge measure across all matching records
- **Result:** Total charge paid by student spectators at GM Place in 2021

### **Complete OLAP Operation Sequence**

**Option 1: Step-by-Step**

1. **Slice (Spectator):** Filter to Spectator_Type = "Student"
2. **Slice (Location):** Filter to Location_Name = "GM Place"
3. **Slice (Date):** Filter to Year = 2021
4. **Roll-up (Game):** Aggregate to ALL games (sum across all games)
5. **Roll-up (Date):** Already at year level after slice
6. **Aggregate:** SUM(Charge) to get total

**Option 2: Using Dice**

1. **Dice:** Create subcube with:
   - Spectator = "Student"
   - Location = "GM Place"
   - Year = 2021
   - Game = ALL
2. **Aggregate:** SUM(Charge) measure

### **SQL Equivalent (for Understanding)**

```sql
SELECT 
    SUM(Charge) AS Total_Charge
FROM 
    FACT_TICKET_SALES f
    JOIN DIM_DATE d ON f.Date_ID = d.Date_ID
    JOIN DIM_SPECTATOR s ON f.Spectator_ID = s.Spectator_ID
    JOIN DIM_LOCATION l ON f.Location_ID = l.Location_ID
WHERE 
    s.Spectator_Type = 'Student'
    AND l.Location_Name = 'GM Place'
    AND d.Year = 2021;
```

### **Resulting Cuboid**

**Dimensions (after operations):**
- Date: 2021 (rolled up to year)
- Spectator: Student (sliced)
- Location: GM Place (sliced)
- Game: ALL (rolled up)

**Measure:**
- Total_Charge = SUM of all Charge values meeting the criteria

---

## Part 3: Bitmap Indexing (5 marks)

### **What is Bitmap Indexing?**

**Definition:**
Bitmap indexing is a special type of database index that uses bitmaps (arrays of bits) to represent the presence or absence of attribute values. Each distinct value in a column has its own bitmap, where each bit corresponds to a row - 1 if the row has that value, 0 if it doesn't.

### **Structure of Bitmap Index**

**Basic Concept:**
- For each distinct value in a column, create a bitmap
- Each bitmap has one bit per row in the table
- Bit = 1 if row has that value, Bit = 0 otherwise

**Example:**
Consider the `Spectator_Type` column with values: Student, Adult, Senior

| Row ID | Spectator_Type | Student Bitmap | Adult Bitmap | Senior Bitmap |
|--------|---------------|---------------|-------------|---------------|
| 1 | Student | 1 | 0 | 0 |
| 2 | Adult | 0 | 1 | 0 |
| 3 | Student | 1 | 0 | 0 |
| 4 | Senior | 0 | 0 | 1 |
| 5 | Student | 1 | 0 | 0 |
| 6 | Adult | 0 | 1 | 0 |

**Bitmap for "Student":** 101010
**Bitmap for "Adult":** 010001
**Bitmap for "Senior":** 000100

### **Advantages of Bitmap Indexing**

#### **1. Efficient for Low-Cardinality Columns (0.5 marks)**
- **Low Cardinality:** Columns with few distinct values (like Spectator_Type: Student/Adult/Senior)
- **Space Efficient:** Bitmaps are compact (1 bit per row)
- **Fast Queries:** Bitwise operations (AND, OR) are very fast
- **Ideal for:** Categorical data, status fields, gender, etc.

#### **2. Fast Query Performance (0.5 marks)**
- **Bitwise Operations:** AND, OR, NOT operations are extremely fast
- **Multi-Column Filters:** Can combine multiple bitmaps quickly
- **Example:** To find "Student AND GM Place", AND the Student bitmap with GM Place bitmap
- **No Full Table Scan:** Direct bitmap access, no need to scan all rows

#### **3. Efficient Storage (0.5 marks)**
- **Compact:** Each bitmap uses 1 bit per row
- **Compression:** Bitmaps compress well (especially with many zeros)
- **Low Overhead:** Minimal storage overhead for low-cardinality columns
- **Better than B-tree:** For low-cardinality columns, smaller than B-tree indexes

#### **4. Excellent for OLAP/Data Warehousing (0.5 marks)**
- **Star Schema:** Perfect for dimension tables (low cardinality attributes)
- **Aggregations:** Fast aggregation queries
- **OLAP Operations:** Efficient for slice, dice, roll-up operations
- **Star Joins:** Efficient joins in star schemas

#### **5. Support for Complex Queries (0.5 marks)**
- **Multiple Conditions:** Can combine multiple bitmaps with AND/OR
- **Range Queries:** Can handle range queries on categorical data
- **COUNT Queries:** Very fast COUNT operations (count 1s in bitmap)

### **Problems/Disadvantages of Bitmap Indexing**

#### **1. High Cardinality Issues (0.5 marks)**
- **Problem:** Not suitable for high-cardinality columns (many distinct values)
- **Reason:** Would require many bitmaps (one per value)
- **Example:** If a column has 1 million distinct values, need 1 million bitmaps
- **Storage:** Storage overhead becomes prohibitive
- **Solution:** Use B-tree indexes for high-cardinality columns

#### **2. Update Overhead (0.5 marks)**
- **Problem:** Updates require modifying multiple bitmaps
- **Locking:** Bitmap updates can cause locking issues
- **Maintenance:** Insertions/deletions require updating all relevant bitmaps
- **OLTP Systems:** Not ideal for frequently updated data (OLTP)
- **Better for:** Read-heavy workloads (OLAP, data warehouses)

#### **3. Storage for Large Tables (0.5 marks)**
- **Large Bitmaps:** For very large tables, bitmaps can be large
- **Memory:** May require significant memory to load bitmaps
- **I/O:** Large bitmaps may require multiple I/O operations
- **Compression:** Compression helps but adds complexity

#### **4. Limited Query Types (0.5 marks)**
- **Equality Only:** Most efficient for equality queries
- **Range Queries:** Less efficient for range queries (though possible)
- **Text Search:** Not suitable for text search or LIKE queries
- **Complex Operations:** Less efficient for complex operations

### **Example Application to This Data Warehouse**

**Good Candidates for Bitmap Indexing:**

1. **DIM_SPECTATOR.Spectator_Type**
   - Low cardinality: 3 values (Student, Adult, Senior)
   - Perfect for bitmap index
   - Fast filtering by spectator type

2. **DIM_LOCATION.Location_Name**
   - Moderate cardinality (if not too many locations)
   - Good for bitmap index
   - Fast filtering by location

3. **DIM_DATE.Year, Quarter, Month**
   - Year: Low cardinality (few years)
   - Quarter: 4 values
   - Month: 12 values
   - All good candidates

**Query Example:**
To find "Student spectators at GM Place in 2021":
1. Load Student bitmap from DIM_SPECTATOR
2. Load GM Place bitmap from DIM_LOCATION
3. Load 2021 bitmap from DIM_DATE
4. AND all three bitmaps together
5. Result bitmap shows matching rows
6. Use result to access fact table efficiently

**Performance Benefit:**
- Very fast compared to full table scan
- Efficient for star schema queries
- Perfect for OLAP operations

---

## Summary

### **Star Schema:**
- Central fact table (FACT_TICKET_SALES)
- Four dimension tables (Date, Spectator, Location, Game)
- Measures: Count and Charge

### **OLAP Operations:**
- **Slice:** Filter by Student, GM Place, 2021
- **Roll-up:** Aggregate Game dimension to ALL
- **Aggregate:** SUM(Charge) to get total

### **Bitmap Indexing:**
- **Advantages:** Fast queries, efficient storage (low cardinality), excellent for OLAP
- **Disadvantages:** High cardinality issues, update overhead, better for read-heavy workloads

---

**End of Question 2**
