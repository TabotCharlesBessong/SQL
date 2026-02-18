# University Course Management System - Database Normalization Exercise

## Overview
This exercise demonstrates the complete database design process from initial unnormalized design through normalization to Boyce-Codd Normal Form (BCNF). It includes identification of anomalies and step-by-step normalization.

## Folder Structure

```
university_course_management/
├── README.md                          (This file)
├── 01_scenario.md                     (Business scenario and requirements)
├── 02_entities_and_attributes.md      (Entity identification)
├── 03_er_diagram.md                   (ER diagram - text, Mermaid, and PlantUML)
├── 03_er_diagram.puml                 (Standalone PlantUML file for ER diagram)
├── 04_relational_schema.md            (Relational schema definition)
├── 05_create_tables_unnormalized.sql  (Unnormalized table creation)
├── 06_insert_data_unnormalized.sql   (Sample data for unnormalized table)
├── 07_identify_anomalies.md           (Insertion, deletion, update anomalies)
├── 08_normalization_process.md        (Step-by-step normalization: 1NF to BCNF)
├── 09_create_tables_normalized.sql    (Normalized tables - final design)
├── 10_insert_data_normalized.sql      (Sample data for normalized tables)
└── 11_test_queries.sql                (Queries to verify normalization benefits)
```

## How to Use This Exercise

### Step 1: Understand the Scenario
Read `01_scenario.md` to understand the business requirements and context.

### Step 2: Identify Entities
Review `02_entities_and_attributes.md` to see how entities and their attributes are identified from the scenario.

### Step 3: Create ER Diagram
Study `03_er_diagram.md` to understand the entity relationships. The Mermaid diagram can be rendered in Markdown viewers that support it.

### Step 4: Define Relational Schema
Review `04_relational_schema.md` to see the formal schema notation and relationships.

### Step 5: Create Unnormalized Database
Execute `05_create_tables_unnormalized.sql` to create the initial (problematic) design.

### Step 6: Insert Sample Data
Execute `06_insert_data_unnormalized.sql` to populate the unnormalized table with sample data.

### Step 7: Identify Anomalies
Read `07_identify_anomalies.md` and try the SQL examples to see:
- **Insertion Anomalies:** Cannot add students/courses/instructors without enrollments
- **Deletion Anomalies:** Deleting enrollments loses student/course/instructor information
- **Update Anomalies:** Must update multiple rows for simple changes

### Step 8: Understand Normalization Process
Study `08_normalization_process.md` to learn:
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- Boyce-Codd Normal Form (BCNF)

### Step 9: Create Normalized Database
Execute `09_create_tables_normalized.sql` to create the properly normalized database design.

### Step 10: Insert Data into Normalized Tables
Execute `10_insert_data_normalized.sql` to populate the normalized tables.

### Step 11: Test and Verify
Execute `11_test_queries.sql` to verify that:
- Insertion anomalies are eliminated
- Deletion anomalies are eliminated
- Update anomalies are eliminated
- Data integrity is maintained

## Key Learning Objectives

1. **Entity Identification:** Learn to identify entities, attributes, and relationships from a business scenario
2. **ER Modeling:** Create entity-relationship diagrams
3. **Relational Schema Design:** Convert ER diagrams to relational schemas
4. **Anomaly Recognition:** Identify insertion, deletion, and update anomalies
5. **Normalization:** Apply normalization rules (1NF → 2NF → 3NF → BCNF)
6. **SQL Implementation:** Create tables, insert data, and write queries

## Database Schema Summary

### Unnormalized Design (Problematic)
- **UnnormalizedEnrollment:** Single table with all attributes
- **Problems:** Redundancy, anomalies, data inconsistency

### Normalized Design (BCNF)
- **Student:** Student information (1 table)
- **Instructor:** Instructor information (1 table)
- **Course:** Course information (1 table)
- **Enrollment:** Enrollment relationships (1 table with foreign keys)
- **Benefits:** No redundancy, no anomalies, data integrity

**Important Design Decision:** InstructorID is stored in ENROLLMENT (not COURSE) because instructor assignment is per enrollment (per semester), not per course permanently. This allows the same course to be taught by different instructors in different semesters (e.g., CS101 by Dr. Johnson in Fall 2024, Dr. Lee in Spring 2025).

## Sample Data

The exercise includes:
- 8 students across different majors
- 4 instructors from different departments
- 6 courses from different departments
- 19 enrollment records across multiple semesters

## SQL Compatibility

The SQL files are written for MySQL/MariaDB syntax. For other databases (PostgreSQL, SQL Server, Oracle), you may need to adjust:
- `AUTO_INCREMENT` → `SERIAL` (PostgreSQL) or `IDENTITY` (SQL Server)
- `TEXT` → `VARCHAR(MAX)` (SQL Server) or `CLOB` (Oracle)
- Date functions may vary

## Practice Exercises

1. **Add More Data:** Insert additional students, courses, and enrollments
2. **Create Views:** Create views for common queries (e.g., student GPA view)
3. **Add Constraints:** Experiment with additional check constraints
4. **Performance:** Compare query performance between normalized and unnormalized designs
5. **Extend Schema:** Add new entities (e.g., Department, Prerequisites, Schedule)

## Exam Preparation Tips

1. **Memorize Normal Forms:** Know the definitions and requirements for each normal form
2. **Practice Anomaly Identification:** Be able to spot insertion, deletion, and update anomalies
3. **Understand Functional Dependencies:** Know how to identify and use FDs for normalization
4. **Practice ER Diagrams:** Be comfortable drawing ER diagrams from scenarios
5. **SQL Skills:** Practice writing CREATE TABLE, INSERT, UPDATE, DELETE, and SELECT statements

## Additional Resources

- Database normalization theory
- Functional dependency analysis
- ER modeling techniques
- SQL best practices
- Referential integrity constraints

---

**Created for IST601 Database Systems Exam Preparation**
