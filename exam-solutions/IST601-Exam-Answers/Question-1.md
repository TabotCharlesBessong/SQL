# Question 1: BANK Database ER Diagram Analysis
## IST601 - Database Management
**Total Marks: 10 marks**

---

## Problem Statement

Consider the ER diagram for part of a BANK database with the following specifications:

### Notation Rules:
- **Double line** from entity set to relationship set = **Total Participation Constraint**
- **Single line** from entity set to relationship set = **Partial Participation Constraint**
- Each bank can have multiple branches
- Each branch can have multiple accounts and loans

### Entity Sets and Attributes:

**1. BANK**
- `Code` (Primary Key)
- `Name`
- `Addr`

**2. BANK BRANCH**
- `Branch_no` (Primary Key)
- `Addr`

**3. ACCOUNT**
- `Accd_no` (Primary Key)
- `Balance`
- `Type`

**4. LOAN**
- `Loan_no` (Primary Key)
- `Amount`
- `Type`

**5. CUSTOMER**
- `Ssn` (Primary Key)
- `Name`
- `Phone`
- `Addr`

### Relationship Sets:

**1. BRANCHES** (between BANK and BANK BRANCH)
- BANK → BRANCHES: Single line, cardinality '1'
- BANK BRANCH → BRANCHES: Double line, cardinality 'N'

**2. ACCTS** (between BANK BRANCH and ACCOUNT)
- BANK BRANCH → ACCTS: Single line, cardinality '1'
- ACCOUNT → ACCTS: Double line, cardinality 'N'

**3. LOANS** (between BANK BRANCH and LOAN)
- BANK BRANCH → LOANS: Single line, cardinality '1'
- LOAN → LOANS: Double line, cardinality 'N'

**4. A/C** (between ACCOUNT and CUSTOMER)
- ACCOUNT → A/C: Single line, cardinality 'M'
- CUSTOMER → A/C: Single line, cardinality 'N'

**5. L/C** (between LOAN and CUSTOMER)
- LOAN → L/C: Single line, cardinality 'M'
- CUSTOMER → L/C: Single line, cardinality 'N'

### Required Tasks:
a) List the strong and weak entity sets in the diagram  
b) List all relationship sets with (min, max) constraints  
c) Translate to relational model

---

## Part (a): Strong and Weak Entity Sets

### Definitions:

**Strong Entity:**
- Has its own primary key
- Can exist independently
- Does not depend on another entity for identification

**Weak Entity:**
- Does not have a sufficient set of attributes to form a primary key
- Depends on a strong entity (owner entity) for identification
- Typically has a partial key + owner's key to form complete identification
- Always has total participation with its owner entity

### Analysis of Entity Sets:

**Examining Each Entity:**

**1. BANK**
- Primary Key: `Code`
- Independence: Can exist without any other entity
- **Classification: STRONG ENTITY**

**2. BANK BRANCH**
- Primary Key: `Branch_no`
- Total Participation: Yes (double line to BRANCHES)
- Dependency: Depends on BANK (a branch must belong to a bank)
- **Classification: WEAK ENTITY**
  - Owner Entity: BANK
  - Identifying Relationship: BRANCHES

**3. ACCOUNT**
- Primary Key: `Accd_no`
- Total Participation: Yes (double line to ACCTS)
- Dependency: Depends on BANK BRANCH (an account must belong to a branch)
- **Classification: WEAK ENTITY**
  - Owner Entity: BANK BRANCH
  - Identifying Relationship: ACCTS

**4. LOAN**
- Primary Key: `Loan_no`
- Total Participation: Yes (double line to LOANS)
- Dependency: Depends on BANK BRANCH (a loan must be issued by a branch)
- **Classification: WEAK ENTITY**
  - Owner Entity: BANK BRANCH
  - Identifying Relationship: LOANS

**5. CUSTOMER**
- Primary Key: `Ssn` (Social Security Number - unique identifier)
- Independence: Can exist without accounts or loans
- Partial Participation: In both A/C and L/C relationships
- **Classification: STRONG ENTITY**

### Answer for Part (a):

**Strong Entity Sets:**
1. **BANK** - Independent entity with primary key `Code`
2. **CUSTOMER** - Independent entity with primary key `Ssn`

**Weak Entity Sets:**
1. **BANK BRANCH** - Depends on BANK for existence
   - Owner: BANK
   - Identifying Relationship: BRANCHES
   - Partial Key: `Branch_no`

2. **ACCOUNT** - Depends on BANK BRANCH for existence
   - Owner: BANK BRANCH
   - Identifying Relationship: ACCTS
   - Partial Key: `Accd_no`

3. **LOAN** - Depends on BANK BRANCH for existence
   - Owner: BANK BRANCH
   - Identifying Relationship: LOANS
   - Partial Key: `Loan_no`

**Key Observation:** Total participation (double line) indicates that every instance must participate in the relationship, which is a characteristic of weak entities depending on their owner entities.

---

## Part (b): Relationship Sets with (Min, Max) Constraints

### Understanding Min-Max Notation:

**(min, max)** constraint on entity E's participation in relationship R means:
- **min**: Minimum number of relationship instances E must participate in
- **max**: Maximum number of relationship instances E can participate in

**Common Constraints:**
- **(0, 1)**: Optional, at most one (partial, one)
- **(1, 1)**: Mandatory, exactly one (total, one)
- **(0, N)**: Optional, many (partial, many)
- **(1, N)**: Mandatory, many (total, many)

### Conversion Rules from Diagram:

**Participation:**
- Single line → min = 0 (partial/optional)
- Double line → min = 1 (total/mandatory)

**Cardinality:**
- 1 → max = 1
- N or M → max = N (many)

---

### Relationship 1: BRANCHES

**Entities:** BANK ←→ BANK BRANCH

**Diagram Information:**
- BANK: Single line, cardinality '1'
- BANK BRANCH: Double line, cardinality 'N'

**Interpretation:**

**BANK side:**
- Single line (partial) → min = 0
- Cardinality '1' → max = 1
- **(0, 1)**: A bank may have zero or one branch in this relationship instance
  - Note: This seems unusual. In practice, this might mean each branch belongs to exactly one bank, but a bank may have no branches (newly established bank) or the relationship shows one branch at a time.

**BANK BRANCH side:**
- Double line (total) → min = 1
- Cardinality 'N' → max = N
- **(1, N)**: A bank branch must belong to exactly one bank
  - Actually, since cardinality is 'N' on branch side and '1' on bank side, it's a 1:N relationship
  - Let me reconsider: The '1' on BANK side and 'N' on BANK BRANCH side indicates one BANK to many BANK BRANCHES

**Correction:**

For 1:N relationship (one bank to many branches):
- **BANK participation in BRANCHES: (0, N)**
  - A bank can have 0 to many branches
  - Partial participation (single line) = optional
- **BANK BRANCH participation in BRANCHES: (1, 1)**
  - A branch must belong to exactly 1 bank
  - Total participation (double line) = mandatory

**BRANCHES Relationship:**
| Entity | Participation | Cardinality | (Min, Max) | Meaning |
|--------|---------------|-------------|------------|---------|
| BANK | Partial (single line) | 1 | **(0, N)** | A bank can have zero or many branches |
| BANK BRANCH | Total (double line) | N | **(1, 1)** | A branch must belong to exactly one bank |

---

### Relationship 2: ACCTS

**Entities:** BANK BRANCH ←→ ACCOUNT

**Diagram Information:**
- BANK BRANCH: Single line, cardinality '1'
- ACCOUNT: Double line, cardinality 'N'

**Interpretation (1:N relationship - one branch to many accounts):**

**ACCTS Relationship:**
| Entity | Participation | Cardinality | (Min, Max) | Meaning |
|--------|---------------|-------------|------------|---------|
| BANK BRANCH | Partial (single line) | 1 | **(0, N)** | A branch can have zero or many accounts |
| ACCOUNT | Total (double line) | N | **(1, 1)** | An account must belong to exactly one branch |

---

### Relationship 3: LOANS

**Entities:** BANK BRANCH ←→ LOAN

**Diagram Information:**
- BANK BRANCH: Single line, cardinality '1'
- LOAN: Double line, cardinality 'N'

**Interpretation (1:N relationship - one branch to many loans):**

**LOANS Relationship:**
| Entity | Participation | Cardinality | (Min, Max) | Meaning |
|--------|---------------|-------------|------------|---------|
| BANK BRANCH | Partial (single line) | 1 | **(0, N)** | A branch can issue zero or many loans |
| LOAN | Total (double line) | N | **(1, 1)** | A loan must be issued by exactly one branch |

---

### Relationship 4: A/C (Account-Customer)

**Entities:** ACCOUNT ←→ CUSTOMER

**Diagram Information:**
- ACCOUNT: Single line, cardinality 'M'
- CUSTOMER: Single line, cardinality 'N'

**Interpretation (M:N relationship - many accounts to many customers):**

This is a many-to-many relationship:
- A customer can have multiple accounts
- An account can have multiple customers (joint accounts)

**A/C Relationship:**
| Entity | Participation | Cardinality | (Min, Max) | Meaning |
|--------|---------------|-------------|------------|---------|
| ACCOUNT | Partial (single line) | M | **(0, N)** | An account can have zero or many customers |
| CUSTOMER | Partial (single line) | N | **(0, N)** | A customer can have zero or many accounts |

---

### Relationship 5: L/C (Loan-Customer)

**Entities:** LOAN ←→ CUSTOMER

**Diagram Information:**
- LOAN: Single line, cardinality 'M'
- CUSTOMER: Single line, cardinality 'N'

**Interpretation (M:N relationship - many loans to many customers):**

This is a many-to-many relationship:
- A customer can have multiple loans
- A loan can have multiple customers (co-borrowers)

**L/C Relationship:**
| Entity | Participation | Cardinality | (Min, Max) | Meaning |
|--------|---------------|-------------|------------|---------|
| LOAN | Partial (single line) | M | **(0, N)** | A loan can have zero or many customers |
| CUSTOMER | Partial (single line) | N | **(0, N)** | A customer can have zero or many loans |

---

### Complete Answer for Part (b):

**Summary Table of All Relationships:**

| Relationship | Entity 1 | (Min, Max) | Entity 2 | (Min, Max) | Type |
|--------------|----------|------------|----------|------------|------|
| **BRANCHES** | BANK | **(0, N)** | BANK BRANCH | **(1, 1)** | 1:N |
| **ACCTS** | BANK BRANCH | **(0, N)** | ACCOUNT | **(1, 1)** | 1:N |
| **LOANS** | BANK BRANCH | **(0, N)** | LOAN | **(1, 1)** | 1:N |
| **A/C** | ACCOUNT | **(0, N)** | CUSTOMER | **(0, N)** | M:N |
| **L/C** | LOAN | **(0, N)** | CUSTOMER | **(0, N)** | M:N |

**Detailed List:**

**1. BRANCHES (BANK to BANK BRANCH)**
- BANK: (0, N) - A bank can have zero or many branches
- BANK BRANCH: (1, 1) - A branch must belong to exactly one bank

**2. ACCTS (BANK BRANCH to ACCOUNT)**
- BANK BRANCH: (0, N) - A branch can manage zero or many accounts
- ACCOUNT: (1, 1) - An account must be held at exactly one branch

**3. LOANS (BANK BRANCH to LOAN)**
- BANK BRANCH: (0, N) - A branch can issue zero or many loans
- LOAN: (1, 1) - A loan must be issued by exactly one branch

**4. A/C (ACCOUNT to CUSTOMER)**
- ACCOUNT: (0, N) - An account can be owned by zero or many customers (joint accounts)
- CUSTOMER: (0, N) - A customer can own zero or many accounts

**5. L/C (LOAN to CUSTOMER)**
- LOAN: (0, N) - A loan can have zero or many customers (co-borrowers)
- CUSTOMER: (0, N) - A customer can have zero or many loans

---

## Part (c): Translation to Relational Model

### Translation Rules:

**Rule 1: Strong Entity → Relation**
- Entity attributes → Relation attributes
- Entity primary key → Relation primary key

**Rule 2: Weak Entity → Relation**
- Include owner's primary key as foreign key
- Weak entity's partial key + owner's primary key → Composite primary key
- Or, weak entity's identifier becomes primary key with foreign key constraint

**Rule 3: 1:N Binary Relationship**
- Add primary key of "1" side as foreign key in "N" side relation
- Total participation on N side means foreign key is NOT NULL

**Rule 4: M:N Binary Relationship**
- Create new relation with:
  - Primary keys of both entities as foreign keys
  - Composite primary key from both foreign keys
  - Any attributes of the relationship

---

### Step 1: Translate Strong Entities

**1. BANK Relation**

```
BANK (Code, Name, Addr)
  Primary Key: Code
```

**Schema:**
```sql
CREATE TABLE BANK (
    Code VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Addr VARCHAR(200)
);
```

---

**2. CUSTOMER Relation**

```
CUSTOMER (Ssn, Name, Phone, Addr)
  Primary Key: Ssn
```

**Schema:**
```sql
CREATE TABLE CUSTOMER (
    Ssn VARCHAR(11) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    Addr VARCHAR(200)
);
```

---

### Step 2: Translate Weak Entities

**3. BANK_BRANCH Relation**

Weak entity owned by BANK:
- Include owner's key (Code) as foreign key
- Total participation → NOT NULL foreign key

```
BANK_BRANCH (Branch_no, Addr, Code)
  Primary Key: Branch_no
  Foreign Key: Code REFERENCES BANK(Code)
```

*Alternative interpretation as truly weak:*
```
BANK_BRANCH (Code, Branch_no, Addr)
  Primary Key: (Code, Branch_no)
  Foreign Key: Code REFERENCES BANK(Code)
```

For this solution, we'll use the first interpretation (Branch_no is unique across all banks):

**Schema:**
```sql
CREATE TABLE BANK_BRANCH (
    Branch_no VARCHAR(20) PRIMARY KEY,
    Addr VARCHAR(200),
    Code VARCHAR(20) NOT NULL,
    FOREIGN KEY (Code) REFERENCES BANK(Code)
        ON DELETE CASCADE
);
```

---

**4. ACCOUNT Relation**

Weak entity owned by BANK_BRANCH:
- Include owner's key (Branch_no) as foreign key
- Total participation → NOT NULL foreign key

```
ACCOUNT (Accd_no, Balance, Type, Branch_no)
  Primary Key: Accd_no
  Foreign Key: Branch_no REFERENCES BANK_BRANCH(Branch_no)
```

**Schema:**
```sql
CREATE TABLE ACCOUNT (
    Accd_no VARCHAR(20) PRIMARY KEY,
    Balance DECIMAL(15, 2) DEFAULT 0.00,
    Type VARCHAR(20),
    Branch_no VARCHAR(20) NOT NULL,
    FOREIGN KEY (Branch_no) REFERENCES BANK_BRANCH(Branch_no)
        ON DELETE CASCADE
);
```

---

**5. LOAN Relation**

Weak entity owned by BANK_BRANCH:
- Include owner's key (Branch_no) as foreign key
- Total participation → NOT NULL foreign key

```
LOAN (Loan_no, Amount, Type, Branch_no)
  Primary Key: Loan_no
  Foreign Key: Branch_no REFERENCES BANK_BRANCH(Branch_no)
```

**Schema:**
```sql
CREATE TABLE LOAN (
    Loan_no VARCHAR(20) PRIMARY KEY,
    Amount DECIMAL(15, 2) NOT NULL,
    Type VARCHAR(20),
    Branch_no VARCHAR(20) NOT NULL,
    FOREIGN KEY (Branch_no) REFERENCES BANK_BRANCH(Branch_no)
        ON DELETE CASCADE
);
```

---

### Step 3: Translate M:N Relationships

**6. ACCOUNT_CUSTOMER Relation (from A/C relationship)**

M:N relationship between ACCOUNT and CUSTOMER:
- Create new relation
- Include both primary keys as foreign keys
- Composite primary key

```
ACCOUNT_CUSTOMER (Accd_no, Ssn)
  Primary Key: (Accd_no, Ssn)
  Foreign Key: Accd_no REFERENCES ACCOUNT(Accd_no)
  Foreign Key: Ssn REFERENCES CUSTOMER(Ssn)
```

**Schema:**
```sql
CREATE TABLE ACCOUNT_CUSTOMER (
    Accd_no VARCHAR(20),
    Ssn VARCHAR(11),
    PRIMARY KEY (Accd_no, Ssn),
    FOREIGN KEY (Accd_no) REFERENCES ACCOUNT(Accd_no)
        ON DELETE CASCADE,
    FOREIGN KEY (Ssn) REFERENCES CUSTOMER(Ssn)
        ON DELETE CASCADE
);
```

---

**7. LOAN_CUSTOMER Relation (from L/C relationship)**

M:N relationship between LOAN and CUSTOMER:
- Create new relation
- Include both primary keys as foreign keys
- Composite primary key

```
LOAN_CUSTOMER (Loan_no, Ssn)
  Primary Key: (Loan_no, Ssn)
  Foreign Key: Loan_no REFERENCES LOAN(Loan_no)
  Foreign Key: Ssn REFERENCES CUSTOMER(Ssn)
```

**Schema:**
```sql
CREATE TABLE LOAN_CUSTOMER (
    Loan_no VARCHAR(20),
    Ssn VARCHAR(11),
    PRIMARY KEY (Loan_no, Ssn),
    FOREIGN KEY (Loan_no) REFERENCES LOAN(Loan_no)
        ON DELETE CASCADE,
    FOREIGN KEY (Ssn) REFERENCES CUSTOMER(Ssn)
        ON DELETE CASCADE
);
```

---

### Complete Relational Model

**Summary of All Relations:**

**1. BANK**
```
BANK (Code, Name, Addr)
  PK: Code
```

**2. CUSTOMER**
```
CUSTOMER (Ssn, Name, Phone, Addr)
  PK: Ssn
```

**3. BANK_BRANCH**
```
BANK_BRANCH (Branch_no, Addr, Code)
  PK: Branch_no
  FK: Code → BANK(Code)
```

**4. ACCOUNT**
```
ACCOUNT (Accd_no, Balance, Type, Branch_no)
  PK: Accd_no
  FK: Branch_no → BANK_BRANCH(Branch_no)
```

**5. LOAN**
```
LOAN (Loan_no, Amount, Type, Branch_no)
  PK: Loan_no
  FK: Branch_no → BANK_BRANCH(Branch_no)
```

**6. ACCOUNT_CUSTOMER**
```
ACCOUNT_CUSTOMER (Accd_no, Ssn)
  PK: (Accd_no, Ssn)
  FK: Accd_no → ACCOUNT(Accd_no)
  FK: Ssn → CUSTOMER(Ssn)
```

**7. LOAN_CUSTOMER**
```
LOAN_CUSTOMER (Loan_no, Ssn)
  PK: (Loan_no, Ssn)
  FK: Loan_no → LOAN(Loan_no)
  FK: Ssn → CUSTOMER(Ssn)
```

---

### Relational Schema Diagram

```
┌──────────────────┐
│      BANK        │
├──────────────────┤
│ Code (PK)        │
│ Name             │
│ Addr             │
└──────────────────┘
        │
        │ 1
        │
        │ N
        ▼
┌──────────────────┐
│  BANK_BRANCH     │
├──────────────────┤
│ Branch_no (PK)   │
│ Addr             │
│ Code (FK)        │
└──────────────────┘
        │
        ├──────────────┬──────────────┐
        │ 1            │ 1            │
        │ N            │ N            │
        ▼              ▼              │
┌──────────────┐ ┌──────────────┐    │
│   ACCOUNT    │ │     LOAN     │    │
├──────────────┤ ├──────────────┤    │
│ Accd_no (PK) │ │ Loan_no (PK) │    │
│ Balance      │ │ Amount       │    │
│ Type         │ │ Type         │    │
│ Branch_no(FK)│ │ Branch_no(FK)│    │
└──────────────┘ └──────────────┘    │
        │                │            │
        │ M              │ M          │
        │                │            │
        │ N              │ N          │
        ▼                ▼            │
┌────────────────┐ ┌────────────────┐│
│ ACCOUNT_       │ │ LOAN_          ││
│ CUSTOMER       │ │ CUSTOMER       ││
├────────────────┤ ├────────────────┤│
│ Accd_no(PK,FK) │ │ Loan_no(PK,FK) ││
│ Ssn (PK,FK)    │ │ Ssn (PK,FK)    ││
└────────────────┘ └────────────────┘│
        │                │            │
        └────────┬───────┘            │
                 │                    │
                 ▼                    │
        ┌──────────────────┐          │
        │    CUSTOMER      │          │
        ├──────────────────┤          │
        │ Ssn (PK)         │          │
        │ Name             │          │
        │ Phone            │          │
        │ Addr             │          │
        └──────────────────┘          │
```

---

### Foreign Key Constraints Summary

| Relation | Foreign Key | References | On Delete |
|----------|-------------|------------|-----------|
| BANK_BRANCH | Code | BANK(Code) | CASCADE |
| ACCOUNT | Branch_no | BANK_BRANCH(Branch_no) | CASCADE |
| LOAN | Branch_no | BANK_BRANCH(Branch_no) | CASCADE |
| ACCOUNT_CUSTOMER | Accd_no | ACCOUNT(Accd_no) | CASCADE |
| ACCOUNT_CUSTOMER | Ssn | CUSTOMER(Ssn) | CASCADE |
| LOAN_CUSTOMER | Loan_no | LOAN(Loan_no) | CASCADE |
| LOAN_CUSTOMER | Ssn | CUSTOMER(Ssn) | CASCADE |

---

### Complete SQL DDL Script

```sql
-- Create BANK table (strong entity)
CREATE TABLE BANK (
    Code VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Addr VARCHAR(200)
);

-- Create CUSTOMER table (strong entity)
CREATE TABLE CUSTOMER (
    Ssn VARCHAR(11) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    Addr VARCHAR(200)
);

-- Create BANK_BRANCH table (weak entity)
CREATE TABLE BANK_BRANCH (
    Branch_no VARCHAR(20) PRIMARY KEY,
    Addr VARCHAR(200),
    Code VARCHAR(20) NOT NULL,
    FOREIGN KEY (Code) REFERENCES BANK(Code)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create ACCOUNT table (weak entity)
CREATE TABLE ACCOUNT (
    Accd_no VARCHAR(20) PRIMARY KEY,
    Balance DECIMAL(15, 2) DEFAULT 0.00,
    Type VARCHAR(20),
    Branch_no VARCHAR(20) NOT NULL,
    FOREIGN KEY (Branch_no) REFERENCES BANK_BRANCH(Branch_no)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create LOAN table (weak entity)
CREATE TABLE LOAN (
    Loan_no VARCHAR(20) PRIMARY KEY,
    Amount DECIMAL(15, 2) NOT NULL,
    Type VARCHAR(20),
    Branch_no VARCHAR(20) NOT NULL,
    FOREIGN KEY (Branch_no) REFERENCES BANK_BRANCH(Branch_no)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create ACCOUNT_CUSTOMER table (M:N relationship)
CREATE TABLE ACCOUNT_CUSTOMER (
    Accd_no VARCHAR(20),
    Ssn VARCHAR(11),
    PRIMARY KEY (Accd_no, Ssn),
    FOREIGN KEY (Accd_no) REFERENCES ACCOUNT(Accd_no)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Ssn) REFERENCES CUSTOMER(Ssn)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create LOAN_CUSTOMER table (M:N relationship)
CREATE TABLE LOAN_CUSTOMER (
    Loan_no VARCHAR(20),
    Ssn VARCHAR(11),
    PRIMARY KEY (Loan_no, Ssn),
    FOREIGN KEY (Loan_no) REFERENCES LOAN(Loan_no)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Ssn) REFERENCES CUSTOMER(Ssn)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

---

## Sample Data and Verification

### Sample Data Insertion

```sql
-- Insert Banks
INSERT INTO BANK VALUES ('B001', 'First National Bank', '123 Main St');
INSERT INTO BANK VALUES ('B002', 'City Bank', '456 Oak Ave');

-- Insert Customers
INSERT INTO CUSTOMER VALUES ('123-45-6789', 'John Doe', '555-1234', '789 Elm St');
INSERT INTO CUSTOMER VALUES ('987-65-4321', 'Jane Smith', '555-5678', '321 Pine Rd');

-- Insert Bank Branches
INSERT INTO BANK_BRANCH VALUES ('BR001', '100 Downtown Blvd', 'B001');
INSERT INTO BANK_BRANCH VALUES ('BR002', '200 Uptown Ave', 'B001');
INSERT INTO BANK_BRANCH VALUES ('BR003', '300 City Center', 'B002');

-- Insert Accounts
INSERT INTO ACCOUNT VALUES ('A001', 5000.00, 'Savings', 'BR001');
INSERT INTO ACCOUNT VALUES ('A002', 10000.00, 'Checking', 'BR001');
INSERT INTO ACCOUNT VALUES ('A003', 15000.00, 'Savings', 'BR003');

-- Insert Loans
INSERT INTO LOAN VALUES ('L001', 50000.00, 'Home', 'BR001');
INSERT INTO LOAN VALUES ('L002', 20000.00, 'Car', 'BR002');

-- Insert Account-Customer relationships (joint accounts possible)
INSERT INTO ACCOUNT_CUSTOMER VALUES ('A001', '123-45-6789');
INSERT INTO ACCOUNT_CUSTOMER VALUES ('A002', '123-45-6789');
INSERT INTO ACCOUNT_CUSTOMER VALUES ('A002', '987-65-4321'); -- Joint account
INSERT INTO ACCOUNT_CUSTOMER VALUES ('A003', '987-65-4321');

-- Insert Loan-Customer relationships (co-borrowers possible)
INSERT INTO LOAN_CUSTOMER VALUES ('L001', '123-45-6789');
INSERT INTO LOAN_CUSTOMER VALUES ('L001', '987-65-4321'); -- Co-borrowers
INSERT INTO LOAN_CUSTOMER VALUES ('L002', '123-45-6789');
```

### Verification Queries

**1. List all branches of a specific bank:**
```sql
SELECT bb.Branch_no, bb.Addr
FROM BANK_BRANCH bb
JOIN BANK b ON bb.Code = b.Code
WHERE b.Name = 'First National Bank';
```

**2. Find all accounts of a customer:**
```sql
SELECT a.Accd_no, a.Type, a.Balance, bb.Addr AS Branch_Address
FROM ACCOUNT a
JOIN ACCOUNT_CUSTOMER ac ON a.Accd_no = ac.Accd_no
JOIN CUSTOMER c ON ac.Ssn = c.Ssn
JOIN BANK_BRANCH bb ON a.Branch_no = bb.Branch_no
WHERE c.Name = 'John Doe';
```

**3. Find all customers of a loan (co-borrowers):**
```sql
SELECT c.Name, c.Ssn
FROM CUSTOMER c
JOIN LOAN_CUSTOMER lc ON c.Ssn = lc.Ssn
JOIN LOAN l ON lc.Loan_no = l.Loan_no
WHERE l.Loan_no = 'L001';
```

---

## Key Takeaways

### 1. Entity Classification
- **Strong entities** exist independently: BANK, CUSTOMER
- **Weak entities** depend on owners: BANK_BRANCH, ACCOUNT, LOAN
- Total participation indicates dependency

### 2. Participation Constraints
- **Total (double line)**: Mandatory, min = 1
- **Partial (single line)**: Optional, min = 0
- Affects foreign key NULL constraints

### 3. Cardinality Mapping
- **1:N relationships**: Foreign key in N-side table
- **M:N relationships**: New junction table with composite key
- Weak entities: Include owner's key

### 4. Referential Integrity
- Foreign keys ensure valid references
- CASCADE options maintain consistency
- NOT NULL enforces total participation

### 5. Normalization
- Relations are in at least 3NF
- No redundancy in design
- Efficient storage and retrieval

---

**End of Question 1**
