## IST601 – 2024/2025 Resit Exam – Question 1 & 2 Solutions

These solutions assume the standard COMPANY database instance from the course notes/textbook (same as in the script on the last page of the exam).

---

### Question 1 – COMPANY Schema, Constraints, and Queries

#### 1(a) Integrity constraint violations

Schemas (keys and FKs as in the script):

- `EMPLOYEE(Fname, Minit, Lname, Ssn PK, Bdate, Address, Sex, Salary, Super_ssn FK→EMPLOYEE(Ssn), Dno FK→DEPARTMENT(Dnumber))`
- `DEPARTMENT(Dname UNIQUE, Dnumber PK, Mgr_ssn FK→EMPLOYEE(Ssn), Mgr_start_date)`
- `DEPT_LOCATIONS(Dnumber FK→DEPARTMENT(Dnumber), Dlocation, PK(Dnumber, Dlocation))`
- `PROJECT(Pname UNIQUE, Pnumber PK, Plocation, Dnum FK→DEPARTMENT(Dnumber))`
- `WORKS_ON(Essn FK→EMPLOYEE(Ssn), Pno FK→PROJECT(Pnumber), Hours, PK(Essn, Pno))`
- `DEPENDENT(Essn FK→EMPLOYEE(Ssn), Dependent_name, Sex, Bdate, Relationship, PK(Essn, Dependent_name))`

For each operation, we say **VIOLATION** or **NO VIOLATION**, and if there is a violation we state which constraint(s) are broken.  
**Important:** In the actual exam you are told to answer the questions under each exercise *chronologically*, so we treat the operations **sequentially**: if an operation succeeds (NO VIOLATION) its effect is visible to later operations; if it violates a constraint, the operation is rejected and makes **no change**.

i. **Insert**  
`INSERT INTO EMPLOYEE VALUES ('Robert','F','Scott','943775543','1972-06-21','2365 Newcastle Rd, Bellaire, TX','M',58000,'888665555',1);`

- `Ssn = '943775543'` is new (no duplicate primary key).  
- `Super_ssn = '888665555'` exists (James Borg).  
- `Dno = 1` exists (Headquarters).  
- **Result:** **NO VIOLATION.**

ii. **Insert**  
`INSERT INTO PROJECT VALUES ('ProductX', 4, 'Bellaire', 2);` *(actual values: pname = 'ProductA' in the exam, pnumber = 4, plocation = 'Bellaire', dnum = 2)*  

- `Pnumber = 4` is new → no PK violation.  
- `Pname` is new → no unique-name violation.  
- `Dnum = 2` **does not exist** in `DEPARTMENT` (only 1, 4, 5 exist).  
- **Result:** **VIOLATION – foreign key on `PROJECT.Dnum` referencing `DEPARTMENT(Dnumber)`.**

iii. **Insert**  
`INSERT INTO DEPARTMENT VALUES ('ProductA', 4, '943775543', '2007-10-01');`

- We first apply (i), which successfully inserts employee `('Robert','F','Scott','943775543', ...)`, so `Mgr_ssn = '943775543'` **does exist** as an employee at this point.  
- However, `Dnumber = 4` already exists (Administration) → **primary key violation on `Dnumber`**.  
- **Result:** **VIOLATION – PK(Dnumber)** (but **no** FK violation on `Mgr_ssn` because the manager now exists).

iv. **Insert**  
`INSERT INTO WORKS_ON VALUES ('677678989', NULL, 40.0);`

- `Essn = '677678989'` is not an existing employee → **FK violation** on `Essn`.  
- `Pno = NULL` – attribute `Pno` is part of the primary key `(Essn, Pno)`, so it **cannot be NULL** → **entity integrity / PK violation**.  
- (NULL `Pno` would also not satisfy the FK referencing `PROJECT(Pnumber)`.)  
- **Result:** **VIOLATION – PK(Essn, Pno) and FK `Essn`→`EMPLOYEE(Ssn)` (and `Pno`→`PROJECT(Pnumber)`).**

v. **Insert**  
`INSERT INTO DEPENDENT VALUES ('453453453','John','M','1990-12-12','spouse');`

- `Essn = '453453453'` exists (`Joyce English`).  
- Pair `(Essn, Dependent_name) = ('453453453','John')` does not already occur in `DEPENDENT`.  
- All attribute domains are respected.  
- **Result:** **NO VIOLATION.**

vi. **Delete** the `WORKS_ON` tuple with `Essn = '333445555'` and `Pno = 10`.

- That tuple exists in `WORKS_ON`.  
- No other table has a foreign key **pointing to** `WORKS_ON` (it is only the referencing side).  
- Deleting it does not break any PK or FK constraint in other tables.  
- **Result:** **NO VIOLATION.**

vii. **Delete** the `EMPLOYEE` tuple with `Ssn = '987654321'` (Jennifer Wallace).

This employee is referenced by several foreign keys:

- As **manager** of department 4 (`DEPARTMENT.Mgr_ssn = '987654321'`).  
- As **supervisor** of employees `999887777` and `987987987` (`EMPLOYEE.Super_ssn`).  
- In `DEPENDENT` (`Essn = '987654321'` for dependent Abner).  
- In `WORKS_ON` (`Essn = '987654321'` for some project assignments).

Deleting her would leave all of these referencing tuples with dangling foreign keys.

- **Result:** **VIOLATION – multiple FKs referencing `EMPLOYEE(Ssn)` from `DEPARTMENT`, `EMPLOYEE.Super_ssn`, `DEPENDENT`, and `WORKS_ON`.**

viii. **Delete** the `PROJECT` tuple with `Pnumber = 10` (Computerization).

- There are `WORKS_ON` tuples with `Pno = 10` (several employees work on project 10).  
- Deleting project 10 would leave those `WORKS_ON` rows’ foreign key `Pno` without a matching `PROJECT(Pnumber)`.  
- **Result:** **VIOLATION – FK `WORKS_ON.Pno`→`PROJECT(Pnumber)`.**

ix. **Delete** the `DEPARTMENT` tuple with `Dnumber = 5` (Research).

Department 5 is referenced by:

- `EMPLOYEE.Dno` (several employees belong to department 5).  
- `PROJECT.Dnum` (`ProductX`, `ProductY`, `ProductZ` are in department 5).  
- `DEPT_LOCATIONS.Dnumber` (there are locations for department 5).

Deleting department 5 would break all of these foreign keys.

- **Result:** **VIOLATION – FKs `EMPLOYEE.Dno`, `PROJECT.Dnum`, `DEPT_LOCATIONS.Dnumber` referencing `DEPARTMENT(Dnumber)`.**

x. **Modify** the `Super_ssn` attribute of the `EMPLOYEE` tuple with `Ssn = '999887777'` (Alicia Zelaya) to `'943775543'`.

- From operation (i), employee with `Ssn = '943775543'` **does exist** in `EMPLOYEE`.  
- Changing `Super_ssn` from `'987654321'` to `'943775543'` therefore still points to a valid supervisor and does not affect any primary key.  
- **Result:** **NO VIOLATION.**

xi. **Modify** the `Hours` attribute of the `WORKS_ON` tuple with `Essn = '999887777'` and `Pno = 10` to `5.0`.

- This tuple exists in `WORKS_ON`.  
- Only the non-key, non-FK attribute `Hours` is changed from `10.0` to `5.0`.  
- Value `5.0` is within the domain of `Hours`.  
- **Result:** **NO VIOLATION.**

---

#### 1(b) MySQL queries on COMPANY

Let the schemas be exactly as above.

**i. Names of all employees in department 5 who work more than 10 hours per week on the ‘ProductX’ project**

```sql
SELECT DISTINCT e.Fname, e.Minit, e.Lname
FROM EMPLOYEE AS e
JOIN WORKS_ON AS w  ON e.Ssn = w.Essn
JOIN PROJECT  AS p  ON w.Pno = p.Pnumber
WHERE e.Dno = 5
  AND p.Pname = 'ProductX'
  AND w.Hours > 10;
```

**ii. Names of all employees who have a dependent with the same first name as themselves**

```sql
SELECT DISTINCT e.Fname, e.Minit, e.Lname
FROM EMPLOYEE  AS e
JOIN DEPENDENT AS d ON e.Ssn = d.Essn
WHERE d.Dependent_name = e.Fname;
```

**iii. Names of all employees who are directly supervised by ‘Franklin Wong’**

```sql
SELECT e.Fname, e.Minit, e.Lname
FROM EMPLOYEE AS e
JOIN EMPLOYEE AS s
  ON e.Super_ssn = s.Ssn
WHERE s.Fname = 'Franklin'
  AND s.Lname = 'Wong';
```

---

### Question 2 – ER to Relational, SQL Semantics, and Joins

#### 2(a) ER → Relational mapping

From the ER diagram on the exam sheet:

- `Patients(sin PK, name, address, age, doctor_sin FK→P_Doctor.sin)`  
  (each patient **has** exactly one primary doctor, so we store the doctor’s `sin` as a foreign key in `Patients`.)

- `P_Doctor(sin PK, name, specialty)`  

- `prescribe(doctor_sin FK→P_Doctor.sin, drug_name FK→Drug.name, quantity, p_date, PK(doctor_sin, drug_name, p_date))`  
  (many‑to‑many relationship between `P_Doctor` and `Drug` with attributes `quantity` and `p_date`.)

- `Pharmacy(name PK, address, phone)`  

- `sells(pharmacy_name FK→Pharmacy.name, drug_name FK→Drug.name, price, PK(pharmacy_name, drug_name))`  
  (many‑to‑many between `Pharmacy` and `Drug` with attribute `price`.)

- `Drug(name PK, formula)`  
  (each drug has a unique name and formula.)

- `makes` – 1‑to‑many relationship from `PharmaceuticalCompany` to `Drug`, with **no attributes of its own**.  
  Instead of a separate relation, we store a foreign key in `Drug`:

  - `Drug` becomes `Drug(name PK, formula, company_name FK→PharmaceuticalCompany.name)`  
  - Therefore, the separate `makes` relation is **not needed** → its row in the table should be filled with **NONE**.

- `PharmaceuticalCompany(name PK, phone)`  

If you must fill the column labeled “Relation / Attributes” exactly:

- **Patients**: `sin (PK), name, address, age, doctor_sin (FK)`  
- **P_Doctor**: `sin (PK), name, specialty`  
- **prescribe**: `doctor_sin (PK, FK), drug_name (PK, FK), quantity, p_date (PK)`  
- **Pharmacy**: `name (PK), address, phone`  
- **sells**: `pharmacy_name (PK, FK), drug_name (PK, FK), price`  
- **Drug**: `name (PK), formula, company_name (FK)`  
- **makes**: `NONE` (implemented via FK from `Drug` instead)  
- **PharmaceuticalCompany**: `name (PK), phone`

*(If your instructor chose a slightly different key structure for the relationship tables, e.g. omitting `p_date` from the primary key of `prescribe`, that is also acceptable as long as the foreign keys and relationship cardinalities are correctly represented.)*

---

#### 2(b) SQL with `EXCEPT`

Given relation schemas:

- `person(id, name)` – people’s id and name  
- `taken(person, course)` – which person (by id) has taken which course id  
- `course(id, cse)` – course id and title

SQL query:

```sql
SELECT id
FROM person
EXCEPT
(SELECT person AS id FROM taken);
```

**i. Why is `id` required in the above query?**

In a set operation such as `EXCEPT`, the **two subqueries must be union‑compatible** – same number of columns and compatible data types.  
The first query returns column `id`; the second originally returns column `person`, so it is **renamed to `id`** to match in both **name and type** for the `EXCEPT` to be valid.

**ii. What is the query asking for (which people are returned)?**

It returns the **ids of all people who have never taken any course** – i.e. all `person.id` values that do **not** appear as `taken.person` in the `taken` table.

**iii. MySQL alternatives (MySQL has no `EXCEPT`)**

Two equivalent MySQL queries:

**Using `NOT IN`:**

```sql
SELECT id
FROM person
WHERE id NOT IN (SELECT person FROM taken);
```

**Using `NOT EXISTS`:**

```sql
SELECT p.id
FROM person AS p
WHERE NOT EXISTS (
  SELECT 1
  FROM taken AS t
  WHERE t.person = p.id
);
```

Both queries return the ids of persons who are **not present** in the `taken` relation.

---

#### 2(c) Row counts for joins

Assume:

- `person` has **N** rows.  
- `taken` has **M** rows.  
- `taken.person` is a foreign key referencing `person.id`.

**i. `person JOIN taken ON id = person` (inner join)**

- Every row in `taken` **must** match exactly one row in `person` (because of the FK).  
- A person can appear many times in `taken` (one row per course taken).  
- Hence, each of the **M** rows in `taken` appears exactly once in the join result.  
- **Number of rows:** **M**.

**ii. `person LEFT JOIN taken ON id = person`**

- All N rows from `person` appear at least once.  
- For persons who have taken at least one course, they appear once per matching row in `taken`.  
- For persons with no courses, they appear **once** with `NULL` values on the `taken` side.

Let `K` be the number of distinct persons that appear in `taken`. Then:

- Rows contributed by those K persons: **M** (one per `taken` row).  
- Rows contributed by the remaining `N − K` persons (no matching taken rows): **N − K**.

So total rows = `M + (N − K)` which is:

- **At least** `max(N, M)` and  
- **At most** `N + M` (when only one person accounts for all M taken rows).

Since `K` is not given, the **exact number of rows cannot be determined** from N and M alone; you just know it lies between `max(N, M)` and `N + M` inclusive.

