# DSC 603 - Data Mining
## Exam Answers - First Semester Examination 2022/2023

**University of Buea, Faculty of Science**  
**Department: Computer Science**  
**Course Code: DSC 603**  
**Course Title: Data Mining**  
**Date: Thursday 05/01/2023**  
**Time: 13:00 - 14:30 (1h30)**  
**Instructor: Dr M. NYAMSI**  
**Venue: D005 - FS**

---

## File Structure

This folder contains detailed answers to all exam questions, with each question in its own file:

- **Question-1.md** - Data Similarity Calculations (15 marks - Compulsory)
- **Question-2.md** - Data Warehousing: Star Schema and OLAP (15 marks - Elective)
- **Question-3.md** - Data Cube Concepts: Aggregate Cells and Iceberg Cubes (15 marks - Elective)

**Total: 45 marks**

---

## Question Breakdown

### Question 1: Data Similarity (15 marks - Compulsory)
- **Task:** Rank database points based on similarity with query point
- **Methods:**
  - Euclidean Distance calculations
  - Cosine Similarity calculations
- **Data:** 5 two-dimensional data points, 1 query point
- **Output:** Rankings for both similarity measures with detailed calculations

### Question 2: Data Warehousing (15 marks - Elective)
- **Part 1:** Star Schema Diagram (5 marks)
  - Fact table and dimension tables
  - Relationships and attributes
- **Part 2:** OLAP Operations (5 marks)
  - Slice, dice, roll-up operations
  - Query: Total charge by student spectators at GM Place in 2021
- **Part 3:** Bitmap Indexing (5 marks)
  - Explanation of bitmap indexing
  - Advantages and problems

### Question 3: Data Cube Concepts (15 marks - Elective)
- **Part 1:** Bitmap Indexing (5 marks)
  - Definition of bitmap indexing
  - Advantages and problems
- **Part 2:** Aggregate Cells (6 marks)
  - Definition of aggregate cells
  - Calculation of number of nonempty aggregate cells
  - 5-dimensional cube with 2 base cells
- **Part 3:** Iceberg Cube (9 marks)
  - Definition of iceberg cube
  - Calculation with minimum support = 2
  - Listing of cells in iceberg cube

---

## Key Topics Covered

1. **Similarity Measures**
   - Euclidean Distance
   - Cosine Similarity
   - Comparison and interpretation

2. **Data Warehousing**
   - Star Schema design
   - OLAP operations (slice, dice, roll-up)
   - Bitmap indexing

3. **Data Cubes**
   - Aggregate cells
   - Iceberg cubes
   - Minimum support threshold
   - Multi-dimensional data analysis

---

## Study Tips

1. **Similarity Calculations:**
   - Practice both Euclidean distance and cosine similarity
   - Understand when to use each measure
   - Note the differences in rankings

2. **Star Schema:**
   - Understand fact tables vs dimension tables
   - Know how to draw star schema diagrams
   - Understand relationships (one-to-many)

3. **OLAP Operations:**
   - Learn slice, dice, roll-up, drill-down
   - Practice identifying which operations are needed for queries
   - Understand aggregation levels

4. **Bitmap Indexing:**
   - Know when to use (low cardinality)
   - Understand advantages and limitations
   - Practice with examples

5. **Data Cubes:**
   - Understand base cells vs aggregate cells
   - Learn how to count aggregate cells
   - Understand iceberg cube concept and minimum support

---

## Formulas Reference

### Euclidean Distance
```
d(x, y) = √[(x₁ - y₁)² + (x₂ - y₂)² + ... + (xn - yn)²]
```

### Cosine Similarity
```
s(x, y) = (x · y) / (||x|| × ||y||)
```

Where:
- x · y = dot product
- ||x|| = magnitude (Euclidean norm)

---

## Notes

- All answers include detailed step-by-step calculations
- Examples are provided throughout for clarity
- Diagrams and visual representations are described
- Key concepts are explained with context
- Practical applications are included where relevant

---

**Good luck with your studies!**
