# IST601 CA Test on ER Diagramming - January 2026
## University of Buea - Database Management
**First Semester 2025-2026**

---

## Exam Overview

This document contains complete solutions to the IST601 CA Test on ER Diagramming, covering Entity-Relationship modeling, notation systems (Chen, Crow's Foot, MySQL Workbench), and database design principles.

**Total Marks: 30**

---

## Question 1: ER Diagramming MCQ Questions (6 marks)

### a) Which component is represented by a rectangle in Chen's notation?

**Answer: B) Entity set**

**Explanation:**
In Chen's notation:
- **Rectangle** represents an **Entity Set**
- **Diamond** represents a **Relationship Set**
- **Oval** represents an **Attribute**
- **Underlined oval** represents a **Key Attribute**

---

### b) What does a "double rectangle" symbolize in an ER diagram?

**Answer: C) Weak entity set**

**Explanation:**
- A **single rectangle** represents a **Strong Entity Set** (has its own primary key)
- A **double rectangle** represents a **Weak Entity Set** (depends on another entity for identification)
- **Multivalued attribute** is represented by a **double oval**
- **Derived attribute** is represented by a **dashed oval**

---

### c) A "derived attribute" (such as Age calculated from Birthdate) is represented by:

**Answer: B) A dashed oval**

**Explanation:**
In ER diagram notation:
- **Single oval** = Simple attribute
- **Double oval** = Multivalued attribute
- **Dashed oval** = Derived attribute (computed from other attributes)
- **Underlined oval** = Key attribute
- **Rectangle** = Entity set

Example: Age can be calculated from Birthdate, so it's a derived attribute.

---

### d) Which term describes a relationship where an entity is associated with itself?

**Answer: C) Recursive**

**Explanation:**
- **Binary relationship:** Involves two entity sets
- **Ternary relationship:** Involves three entity sets
- **Recursive relationship:** An entity set has a relationship with itself (also called unary relationship)
- **Redundant relationship:** A relationship that can be derived from other relationships

Example: An Employee manages other Employees (Employee → Manages → Employee)

---

### e) In a One-to-Many (1:N) relationship between "Department" and "Employee," where should the 'N' be placed?

**Answer: B) On the line connecting to the Employee entity**

**Explanation:**
In Chen's notation, cardinality is shown as:
- **1** on the "one" side (Department)
- **N** on the "many" side (Employee)

The relationship reads: "One Department has Many Employees"

```
Department ──────< Has >────── Employee
           1                    N
```

---

### f) When using (min, max) notation, what does (0, N) indicate?

**Answer: B) Optional participation with a maximum of many**

**Explanation:**
In (min, max) notation:
- **First number (min):** Minimum participation (0 = optional, 1 = mandatory)
- **Second number (max):** Maximum participation (1 = one, N = many)

**(0, N)** means:
- **0** = Optional participation (entity may or may not participate)
- **N** = Maximum of many (unlimited)

Example: A Customer (0, N) Places Orders means a customer can place zero or many orders (optional participation, many maximum).

---

## Question 2: Definitions and Crow's Foot Notation (7 marks)

### a) Give a one-line definition for each of the following concepts (3 marks)

#### i) Weak entity set

**Answer:** An entity set that cannot be uniquely identified by its own attributes alone and depends on another entity set (owner entity) for its existence and identification.

---

#### ii) Composite Attribute

**Answer:** An attribute that can be divided into smaller sub-parts representing more basic attributes with independent meanings.

**Example:** Address can be divided into Street, City, State, ZipCode.

---

#### iii) Cardinality (ER diagram)

**Answer:** The maximum number of relationship instances that an entity can participate in within a relationship set.

**Example:** In a "Manages" relationship between Employee and Department, if cardinality is 1:1, one employee manages one department.

---

#### iv) Cardinality (Relational model)

**Answer:** The number of tuples (rows) in a relation or the number of distinct values in a column.

**Note:** In relational model context, cardinality often refers to the number of rows in a table.

---

#### v) Degree (ER diagram)

**Answer:** The number of entity sets that participate in a relationship set.

**Types:**
- **Unary/Degree 1:** One entity set (recursive)
- **Binary/Degree 2:** Two entity sets
- **Ternary/Degree 3:** Three entity sets

---

#### vi) Degree (Relational model)

**Answer:** The number of attributes (columns) in a relation.

**Example:** A relation with 5 columns has a degree of 5.

---

### b) Precisely define in not more than 5 words, each of the cardinalities depicted on the right using the crow's foot notation. In each case, state the participation constraint. (4 marks)

#### A: Mandatory One-to-One

**Definition:** One entity must relate to exactly one other entity.

**Participation Constraint:** **Mandatory** (Total participation) on both sides.

**Crow's Foot Notation:**
```
Entity A ──────|| Relationship ||────── Entity B
```
- Single vertical line on both ends = mandatory one-to-one
- Both entities must participate in the relationship

---

#### B: Optional One

**Definition:** One entity may relate to zero or one other entity.

**Participation Constraint:** **Optional** (Partial participation) on the side with the circle.

**Crow's Foot Notation:**
```
Entity A ──────o| Relationship |────── Entity B
```
- Circle (o) on one end = optional participation
- Single vertical line on the other = one (maximum)
- Entity A may or may not participate, but if it does, it relates to exactly one Entity B

---

#### C: Mandatory One-to-Many

**Definition:** One entity must relate to one or many other entities.

**Participation Constraint:** **Mandatory** (Total participation) on the "many" side.

**Crow's Foot Notation:**
```
Entity A ──────| Relationship >────── Entity B
```
- Single vertical line on one end = one (from Entity A)
- Crow's foot (three lines) on the other = many (to Entity B)
- Entity B must participate (mandatory), and one Entity A can relate to many Entity B instances

---

#### D: Optional One-to-Many

**Definition:** One entity may relate to zero or many other entities.

**Participation Constraint:** **Optional** (Partial participation) on the "many" side.

**Crow's Foot Notation:**
```
Entity A ──────o| Relationship >────── Entity B
```
- Circle (o) and single vertical line on one end = optional one (from Entity A)
- Crow's foot (three lines) on the other = many (to Entity B)
- Entity B may or may not participate (optional), and one Entity A can relate to zero or many Entity B instances

---

## Question 3: ER Diagram Design and Relational Model (17 marks)

### a) Retail Store Scenario (8 marks)

#### Business Rules:
1. A Customer can place multiple Orders, but each Order belongs to only one Customer
2. An Order can contain multiple Products, and a single Product can appear in many different Orders

#### Entities and Attributes:
- **Customer:** CustomerID (key), Name, Email
- **Order:** OrderID (key), Date, TotalAmount
- **Product:** ProductID (key), ProductName, Price

---

#### i) Design an ER Diagram for the retail store. Use Chen notation. Ensure all relationship sets are labeled with 1, M, or N (4 marks)

**Solution:**

```
┌─────────────┐
│  Customer   │
├─────────────┤
│ CustomerID │◄──┐
│ Name       │   │
│ Email      │   │
└─────────────┘   │
                  │
                  │ Places
                  │ (1, N)
                  │
┌─────────────┐   │
│    Order    │   │
├─────────────┤   │
│  OrderID    │◄──┘
│   Date      │
│ TotalAmount │
└─────────────┘
       │
       │ Contains
       │ (M, N)
       │
       ▼
┌─────────────┐
│   Product   │
├─────────────┤
│  ProductID  │
│ ProductName │
│    Price    │
└─────────────┘
```

**Explanation:**
- **Customer ── Places ── Order:** 1:N relationship
  - One Customer can place many Orders (N)
  - Each Order belongs to one Customer (1)
- **Order ── Contains ── Product:** M:N relationship
  - One Order can contain many Products (N)
  - One Product can appear in many Orders (M)
- Since Order-Product is M:N, we need an associative entity or relationship attributes (e.g., Quantity, UnitPrice)

**Enhanced ER Diagram with Relationship Attributes:**

```
┌─────────────┐
│  Customer   │
├─────────────┤
│ CustomerID │◄──┐
│ Name       │   │
│ Email      │   │
└─────────────┘   │
                  │
                  │ Places
                  │ (1, N)
                  │
┌─────────────┐   │
│    Order    │   │
├─────────────┤   │
│  OrderID    │◄──┘
│   Date      │
│ TotalAmount │
└─────────────┘
       │
       │ Contains
       │ (M, N)
       │
       │ ┌─────────────┐
       │ │  Quantity   │ (Relationship Attribute)
       │ │  UnitPrice  │
       │ └─────────────┘
       │
       ▼
┌─────────────┐
│   Product   │
├─────────────┤
│  ProductID  │
│ ProductName │
│    Price    │
└─────────────┘
```

---

#### ii) Redraw the ER diagram using Crow's Foot notation. (4 marks)

**Solution:**

```
┌─────────────┐
│  Customer   │
├─────────────┤
│ CustomerID │◄──┐
│ Name       │   │
│ Email      │   │
└─────────────┘   │
                  │
                  │ Places
                  │
┌─────────────┐   │
│    Order    │   │
├─────────────┤   │
│  OrderID    │◄──┘
│   Date      │
│ TotalAmount │
└─────────────┘
       │
       │ Contains
       │
       │ ┌─────────────┐
       │ │  Quantity   │
       │ │  UnitPrice  │
       │ └─────────────┘
       │
       ▼
┌─────────────┐
│   Product   │
├─────────────┤
│  ProductID  │
│ ProductName │
│    Price    │
└─────────────┘
```

**Crow's Foot Notation Details:**
- **Customer ── Places ── Order:**
  - Customer side: Single vertical line (one)
  - Order side: Crow's foot (many)
  - Order participation: Mandatory (each order must have a customer)
  
- **Order ── Contains ── Product:**
  - Order side: Crow's foot (many)
  - Product side: Crow's foot (many)
  - Both sides: Optional (an order may have no products initially, a product may not be in any order)

**Visual Representation:**
```
Customer ──────| Places >────── Order ──────< Contains >────── Product
         (1)                    (N)          (M)                (N)
```

---

### b) Employees and Dependents Scenario (9 marks)

#### Business Rules:
1. A company database tracks Employees and their Dependents (spouses/children)
2. An Employee has a unique EmployeeID plus name and birthdate as additional attributes
3. A Dependent is identified by their Name only within the context of a specific employee. If an employee is deleted, their dependents must also be removed

---

#### i) Identify the strong and weak entity types. In each case, give a reason for your choice (2 marks)

**Answer:**

**Strong Entity: Employee**

**Reason:**
- Employee has a unique identifier (EmployeeID) that can uniquely identify each employee independently
- Employee can exist without depending on any other entity
- EmployeeID serves as the primary key

**Weak Entity: Dependent**

**Reason:**
- Dependent does not have a unique identifier of its own
- Dependent is identified by its Name only within the context of a specific Employee (partial key)
- Dependent cannot exist independently - it depends on Employee for its existence
- The full identification requires both EmployeeID (from owner) and Name (partial key)
- If an Employee is deleted, their Dependents must also be removed (existence dependency)

---

#### ii) MySQL Workbench uses the relationship types depicted on the right. Give two terms used to differentiate the relationship types that use dashed and solid lines. (2 marks)

**Answer:**

1. **Identifying Relationship** (Solid/Dashed line distinction in some tools, but more commonly):
   - **Identifying Relationship:** Uses a **solid line** - the foreign key is part of the primary key of the dependent entity
   - **Non-Identifying Relationship:** Uses a **dashed line** - the foreign key is not part of the primary key

2. **Alternative Terms:**
   - **Strong Relationship** (Solid) vs **Weak Relationship** (Dashed)
   - **Mandatory Relationship** (Solid) vs **Optional Relationship** (Dashed)

**For MySQL Workbench specifically:**
- **Solid line:** Identifying relationship (foreign key is part of primary key)
- **Dashed line:** Non-identifying relationship (foreign key is a regular attribute)

**In the context of Employee-Dependent:**
- Since Dependent is a weak entity and its primary key includes EmployeeID, the relationship should use a **solid line** (identifying relationship).

---

#### iii) Draw the correct ER diagram using MySQL Workbench that shows the relationship between Employees and Dependents (2 marks)

**Solution:**

```
┌──────────────┐
│   Employee   │
├──────────────┤
│ EmployeeID  │◄──┐ (PK)
│    Name     │   │
│  Birthdate  │   │
└──────────────┘   │
                   │
                   │ Has
                   │ (Identifying Relationship)
                   │ Solid Line
                   │
┌──────────────┐   │
│  Dependent   │   │
├──────────────┤   │
│ EmployeeID  │◄──┘ (PK, FK) ───┐
│    Name     │                  │
│ Relationship│                  │
│  Birthdate  │                  │
└──────────────┘                  │
                                  │
                    (Composite Primary Key:
                     EmployeeID + Name)
```

**MySQL Workbench Notation:**
- **Employee:** Strong entity with EmployeeID as primary key
- **Dependent:** Weak entity with composite primary key (EmployeeID, Name)
- **Relationship:** Solid line (identifying relationship) from Employee to Dependent
- **Cardinality:** 1:N (One Employee has many Dependents)
- **Participation:** Total participation on Dependent side (every dependent must belong to an employee)

**Visual Representation:**
```
Employee ──────|| Has >────── Dependent
  (1)                        (N)
  [Strong]                  [Weak]
                            PK: (EmployeeID, Name)
                            FK: EmployeeID → Employee.EmployeeID
```

---

#### iv) Write the relational models you would get from the relationship between Employees and Dependents if you used (2 marks)

##### iv-1) the relationship type with a solid line

**Relational Model:**

```sql
Employee(EmployeeID, Name, Birthdate)
  PK: EmployeeID

Dependent(EmployeeID, Name, Relationship, Birthdate)
  PK: (EmployeeID, Name)
  FK: EmployeeID → Employee(EmployeeID)
```

**Explanation:**
- **Solid line** = Identifying relationship
- Foreign key (EmployeeID) is **part of the primary key** of Dependent
- Composite primary key: (EmployeeID, Name)
- This is the correct model for a weak entity

---

##### iv-2) the relationship type with a dashed line

**Relational Model:**

```sql
Employee(EmployeeID, Name, Birthdate)
  PK: EmployeeID

Dependent(DependentID, EmployeeID, Name, Relationship, Birthdate)
  PK: DependentID
  FK: EmployeeID → Employee(EmployeeID)
```

**Explanation:**
- **Dashed line** = Non-identifying relationship
- Foreign key (EmployeeID) is **not part of the primary key**
- A new surrogate key (DependentID) is created as the primary key
- EmployeeID becomes a regular foreign key attribute
- This treats Dependent as a strong entity, which contradicts the business rule

---

#### v) Which of the 2 relational models in iv) is correct? (1 mark)

**Answer: iv-1) The relationship type with a solid line**

**Reason:**
1. **Business Rule Compliance:** The scenario states that "A Dependent is identified by their Name only within the context of a specific employee" - this is the definition of a weak entity, requiring an identifying relationship (solid line).

2. **Weak Entity Characteristics:** 
   - Dependent has no unique identifier of its own
   - Dependent's primary key must include the owner's key (EmployeeID)
   - Dependent has existence dependency on Employee

3. **Data Integrity:** The solid line model ensures that:
   - Dependents cannot exist without an Employee
   - The composite key (EmployeeID, Name) correctly identifies each dependent
   - Cascade deletion is properly represented (if Employee is deleted, Dependents are deleted)

4. **The dashed line model is incorrect** because:
   - It treats Dependent as a strong entity with its own primary key
   - It violates the business rule that Dependent is identified only within the context of Employee
   - It allows Dependents to exist independently, which contradicts the requirement

---

## Summary

### Key Concepts Covered:

1. **ER Notation Systems:**
   - Chen Notation (rectangles, diamonds, ovals)
   - Crow's Foot Notation (cardinality symbols)
   - MySQL Workbench Notation (solid vs dashed lines)

2. **Entity Types:**
   - Strong entities (independent existence, own primary key)
   - Weak entities (dependent existence, composite primary key)

3. **Relationship Types:**
   - Identifying (solid line, FK part of PK)
   - Non-identifying (dashed line, FK not part of PK)
   - Cardinalities: 1:1, 1:N, M:N

4. **Relational Model Translation:**
   - Strong entities → Relations with simple PK
   - Weak entities → Relations with composite PK (owner's PK + partial key)
   - 1:N relationships → FK in N-side
   - M:N relationships → New relation or relationship attributes

---

## Additional Notes

### Best Practices for ER Diagramming:

1. **Start with entities:** Identify all entity sets first
2. **Define relationships:** Determine how entities relate
3. **Set cardinalities:** Carefully read business rules for 1:1, 1:N, M:N
4. **Identify weak entities:** Look for entities that depend on others
5. **Choose correct notation:** Use appropriate notation for the context
6. **Verify constraints:** Check participation (mandatory/optional) and cardinality

### Common Mistakes to Avoid:

1. Confusing strong and weak entities
2. Incorrect cardinality placement
3. Using wrong notation for the context
4. Missing composite keys for weak entities
5. Incorrect foreign key placement in relational model

---

**End of Solutions**

**Course:** IST601 - Database Management  
**Institution:** University of Buea  
**Semester:** First Semester 2025-2026  
**Test Date:** January 2026  
**Total Marks:** 30
