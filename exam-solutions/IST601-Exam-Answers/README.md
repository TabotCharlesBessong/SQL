# IST601 CA Test on ER Diagramming - January 2025
## University of Buea - Database Management
**First Semester 2024-2025**

---

## Exam Overview

This repository contains complete solutions to the IST601 CA Test on ER Diagramming, covering Entity-Relationship modeling, notation systems, and database design principles.

**Total Marks: 30**

---

## Questions and Solutions

### Question 1: BANK Database ER Diagram (10 marks)
**File:** [Question-1.md](Question-1.md)

**Topics Covered:**
- Strong and weak entity identification
- Relationship sets and participation constraints
- (Min, Max) cardinality notation
- ER to Relational Model translation
- Total vs. Partial participation

**Key Concepts:**
- Entity Sets: BANK, BANK BRANCH, ACCOUNT, LOAN, CUSTOMER
- Relationships: BRANCHES, ACCTS, LOANS, A/C, L/C
- Primary and foreign key derivation

---

### Question 2: Manufacturing Database ER Diagram (10 marks)
**File:** [Question-2.md](Question-2.md)

**Topics Covered:**
- Chen notation for cardinalities
- ER diagram conversion between notations
- Relational model derivation
- Foreign key identification
- Parent-child relationship mapping

**Key Concepts:**
- Entity Sets: Lot, Production Units, Raw Materials
- Relationships: Includes, Created From
- Foreign key constraints and referential integrity

---

### Question 3: Higher Education Database EER Diagram (10 marks)
**File:** [Question-3.md](Question-3.md)

**Topics Covered:**
- Enhanced Entity-Relationship (EER) modeling
- Crow's feet notation
- Specialization/Generalization hierarchies
- Multi-valued attributes
- Composite keys and unique identifiers
- Weak entity identification

**Key Concepts:**
- University system modeling
- Student categorization (Undergraduate, Postgraduate, Certificate)
- Faculty-Department-Programme hierarchy
- Thesis supervisor relationships
- Multi-campus modeling

---

## Key Learning Objectives

### 1. ER Diagram Notations
- **Chen Notation:** Original ER notation with diamond shapes for relationships
- **Crow's Feet Notation:** Modern notation showing cardinality at relationship endpoints
- **Min-Max Notation:** Explicit (min, max) constraints on participation

### 2. Participation Constraints
- **Total Participation (Double Line):** Every entity must participate in the relationship
- **Partial Participation (Single Line):** Entity participation is optional

### 3. Cardinality Types
- **One-to-One (1:1):** Each entity associates with at most one other entity
- **One-to-Many (1:N):** One entity associates with multiple entities
- **Many-to-Many (M:N):** Multiple entities associate with multiple entities

### 4. ER to Relational Model Translation Rules
- Strong entities → Relations with primary keys
- Weak entities → Relations with composite keys (owner's PK + partial key)
- 1:N relationships → Foreign key in N-side relation
- M:N relationships → New relation with composite key from both entities
- Multi-valued attributes → Separate relation

### 5. EER (Enhanced ER) Concepts
- **Specialization:** Top-down process (general → specific)
- **Generalization:** Bottom-up process (specific → general)
- **Disjoint vs. Overlapping:** Can entity belong to multiple subtypes?
- **Total vs. Partial:** Must entity belong to a subtype?

---

## Database Design Best Practices

1. **Identify Entities First:** Start with major objects/concepts
2. **Define Relationships:** How entities interact
3. **Determine Cardinalities:** How many instances participate
4. **Apply Constraints:** Total/partial participation, keys
5. **Normalize:** Ensure data integrity and reduce redundancy
6. **Verify:** Check for completeness and correctness

---

## Notation Quick Reference

### Crow's Feet Notation
```
Entity ──────|< Relationship >|──────── Entity
             |                  |
        One to Many         Many to One

Entity ──────< Relationship >───── Entity
            Many to Many

Entity ──────|| Relationship ||──────── Entity
          One to One (mandatory both sides)

Entity ──────o| Relationship |o──────── Entity
          One to One (optional both sides)
```

### Min-Max Notation
```
(0, 1) = Optional, at most one
(1, 1) = Mandatory, exactly one
(0, N) = Optional, many
(1, N) = Mandatory, many
(M, N) = At least M, at most N
```

---

## Additional Resources

### Textbook References
- Elmasri & Navathe: "Fundamentals of Database Systems"
  - Chapter 3: Data Modeling Using the Entity-Relationship Model
  - Chapter 4: Enhanced Entity-Relationship (EER) Model
  - Chapter 9: Relational Database Design by ER-to-Relational Mapping

### Practice Tips
1. Draw before writing: Visualize the solution
2. Label everything clearly: Entities, relationships, attributes
3. Double-check cardinalities: Read requirements carefully
4. Verify foreign keys: Every FK must reference a PK
5. Test with sample data: Does the model support all use cases?

---

## Solution Approach

Each solution follows this structure:

1. **Problem Statement:** Clear presentation of the requirements
2. **Analysis:** Breaking down the diagram components
3. **Step-by-Step Solution:** Detailed explanations with reasoning
4. **Visual Representations:** ASCII diagrams and tables
5. **Verification:** Checking completeness and correctness
6. **Summary:** Final answer with key takeaways

---

## Grading Criteria

### Question 1 (10 marks)
- Part a: Strong/Weak entities (3 marks)
- Part b: Relationships with min-max constraints (4 marks)
- Part c: Relational model translation (3 marks)

### Question 2 (10 marks)
- Part a: Chen notation redrawing (3 marks)
- Part b: Relational model derivation (4 marks)
- Part c: Foreign key identification (3 marks)

### Question 3 (10 marks)
- Entity identification (2 marks)
- Relationship mapping (3 marks)
- EER features (specialization, multi-valued) (3 marks)
- Crow's feet notation correctness (2 marks)

---

## Contact & Contributions

For questions, corrections, or improvements, please refer to the course instructor or teaching assistant.

**Course:** IST601 - Database Management  
**Institution:** University of Buea  
**Semester:** First Semester 2024-2025  
**Exam Date:** January 2025

---

**End of README**
