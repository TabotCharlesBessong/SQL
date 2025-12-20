# Database Assignment - ER Diagrams and Relational Models

This directory contains the solutions for your database assignment tasks.

## Files Overview

### 1. University Community ER Diagram
**File:** `university-community-er.puml`

This PlantUML file contains the complete ER diagram for the university community system with:
- **People** entity (supertype) with overlapping specialization to **Employees** and **Students**
- **Employees** entity with disjoint, total specialization to:
  - **Civil Servants** (categorized by IndexCategory)
  - **Contract Workers** (categorized by ContractCategory)
  - **Temporary Employees** (categorized by RateCategory)
- **Academic Departments** and **Work Departments**
- **Programmes**, **Courses**, and **Semesters**
- **Enrollment** entity for the M:N relationship between Students, Courses, and Semesters
- **Qualification** entity (converted from multi-valued attribute)

**Key Features:**
- Overlapping specialization: People → Employees, Students (some people can be both)
- Disjoint specialization: Employees → CServs, CWrks, Temps (mutually exclusive)
- Multi-valued attribute converted to separate entity
- Derived attribute (tsal) noted

### 2. Employee-Factory System (Crow's Feet Notation)
**Files:** 
- `employee-factory-crowsfeet.puml` - ER diagram in Crow's Feet notation
- `employee-factory-relational-model.sql` - Relational model implementation

**Features:**
- Recursive relationship: Employee supervises Employee (1:N)
- Employee works at Factory (N:1)
- Employee manages Factory (1:1)
- Derived attribute: throughput in Factory

**Relational Model Notes:**
- Recursive relationship implemented via `supervisor_ID` foreign key
- 1:1 manages relationship uses unique constraint on `manager_ID`
- All foreign keys properly constrained

### 3. Car-Customer-Employee-Invoice System
**File:** `car-customer-invoice-relational-model.sql`

This file contains the relational model conversion of the ER diagram with:
- Four main entities: CAR, CUSTOMER, EMPLOYEE, INVOICE
- Four intersection tables for M:N relationships:
  - CAR_CUSTOMER
  - CAR_EMPLOYEE
  - CUSTOMER_INVOICE
  - EMPLOYEE_INVOICE

**Key Features:**
- All M:N relationships properly converted to intersection tables
- Composite primary keys in intersection tables
- Proper foreign key constraints with CASCADE options
- Indexes for performance optimization

## How to Use PlantUML Files

### Option 1: Online Viewer
1. Go to http://www.plantuml.com/plantuml/uml/
2. Copy and paste the contents of any `.puml` file
3. The diagram will be rendered automatically

### Option 2: VS Code Extension
1. Install the "PlantUML" extension in VS Code
2. Open any `.puml` file
3. Press `Alt+D` (or right-click → Preview) to view the diagram

### Option 3: Command Line
```bash
# Install PlantUML (requires Java)
# Download from: https://plantuml.com/download

# Generate PNG
java -jar plantuml.jar university-community-er.puml

# Generate SVG
java -jar plantuml.jar -tsvg university-community-er.puml
```

## How to Use SQL Files

The SQL files contain complete CREATE TABLE statements with:
- Primary keys
- Foreign keys with proper constraints
- Indexes for performance
- Detailed comments explaining the design decisions

You can execute these directly in your MySQL/PostgreSQL database:
```sql
-- Example
SOURCE assignment/employee-factory-relational-model.sql;
```

## Design Decisions

### University Community System
1. **Multi-valued attribute handling**: `quals` converted to separate `Qualification` entity
2. **Overlapping specialization**: People can be both Employees and Students
3. **Disjoint specialization**: Employees are exactly one of CServs, CWrks, or Temps
4. **Derived attributes**: `tsal` is calculated (hours × sal-rate from RateCategory)

### Employee-Factory System
1. **Recursive relationship**: Self-referencing foreign key with NULL allowed for top-level employees
2. **1:1 relationship**: Unique constraint ensures one manager per factory
3. **Derived attributes**: `throughput` not stored, calculated as needed

### Car-Customer-Invoice System
1. **M:N relationships**: All converted to intersection tables with composite keys
2. **CASCADE options**: Used to maintain referential integrity
3. **Additional attributes**: Can be added to intersection tables if needed (e.g., SaleDate)

## Notes

- All diagrams follow standard ER modeling conventions
- Relational models include proper normalization
- Foreign key constraints ensure referential integrity
- Indexes are included for common query patterns

