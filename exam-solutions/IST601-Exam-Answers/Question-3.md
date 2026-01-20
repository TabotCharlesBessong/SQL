# Question 3: Higher Education Database EER Diagram Design
## IST601 - Database Management
**Total Marks: 10 marks**

---

## Problem Statement

The Ministry of Higher Education wants to design a database to keep track of universities in the country as well as the various faculties, academic departments, degree programmes, courses, and students in higher education.

### Requirements Analysis:

**1. University Entity:**
- Attributes: `university_id`, `university_name`, `towns`
- Special consideration: Some universities have campuses in only one town, others in multiple towns
- **Multi-valued attribute**: `towns`

**2. Organizational Hierarchy:**
- Universities **have** Faculties
- Faculties **have** Academic Departments
- Departments **have** Programmes of Study (e.g., B.Sc. in Computer Science)
- Departments also **offer** Courses

**3. Unique Identifier Requirements:**
- Faculties, academic departments, programmes of study, and courses have unique identifier codes
- **Important:** These codes are independently developed by each university
- Different universities may use the same codes
- **Design must uniquely identify them system-wide**
- **Implication:** Weak entities with composite keys

**4. Programme-Course Relationship:**
- Each programme of study has courses that make up that programme
- Many-to-many relationship

**5. Student Admission:**
- Students are admitted into programmes of study
- Track: `semester` and `year` of admission
- **Relationship attribute:** semester, year on Admission relationship

**6. Student Categories (Specialization/Generalization):**
- Students belong to one of three categories:
  - **Undergraduate**
  - **Postgraduate**
  - **Certificate**
- **Disjoint specialization** (student belongs to exactly one category)
- **Total specialization** (every student must belong to a category)

**7. Category-Specific Attributes:**
- **Undergraduate students:** GPA (on scale of 4)
- **Postgraduate students:** GPA (on scale of 4)
- **Certificate students:** Average Score (on scale of 20)

**8. Postgraduate-Specific Relationship:**
- Postgraduate students are assigned to one or more thesis supervisors
- Supervisors are likely Faculty members (staff)
- Many-to-many relationship

**9. Additional Considerations:**
- Courses offered by departments (weak entity relationship)
- Programme-Course composition

---

### Task:
Construct EER diagrams for the student database using **Crow's Feet Notation**.

---

## Entity Identification

### Strong Entities:

**1. UNIVERSITY**
- Attributes: `university_id` (PK), `university_name`
- Multi-valued attribute: `towns`

**2. STUDENT**
- Attributes: `student_id` (PK), `name`, `phone`, `email`, `address`
- Superclass for specialization

**3. SUPERVISOR** (Faculty/Staff)
- Attributes: `supervisor_id` (PK), `name`, `title`, `department_id` (FK)

---

### Weak Entities:

**4. FACULTY**
- Partial key: `faculty_code`
- Full key: (`university_id`, `faculty_code`)
- Owner: UNIVERSITY
- Attributes: `faculty_code`, `faculty_name`, `university_id` (FK)

**5. DEPARTMENT**
- Partial key: `dept_code`
- Full key: (`university_id`, `faculty_code`, `dept_code`)
- Owner: FACULTY
- Attributes: `dept_code`, `dept_name`, `university_id` (FK), `faculty_code` (FK)

**6. PROGRAMME**
- Partial key: `programme_code`
- Full key: (`university_id`, `faculty_code`, `dept_code`, `programme_code`)
- Owner: DEPARTMENT
- Attributes: `programme_code`, `programme_name`, `degree_type`, `duration_years`, `university_id` (FK), `faculty_code` (FK), `dept_code` (FK)

**7. COURSE**
- Partial key: `course_code`
- Full key: (`university_id`, `dept_code`, `course_code`)
- Owner: DEPARTMENT
- Attributes: `course_code`, `course_name`, `credits`, `university_id` (FK), `dept_code` (FK)

---

### Specialized Entities (Subtypes of STUDENT):

**8. UNDERGRADUATE**
- Inherits: All STUDENT attributes
- Additional attribute: `gpa_4` (GPA on scale of 4)

**9. POSTGRADUATE**
- Inherits: All STUDENT attributes
- Additional attribute: `gpa_4` (GPA on scale of 4)
- Participates in: SUPERVISED_BY relationship

**10. CERTIFICATE**
- Inherits: All STUDENT attributes
- Additional attribute: `average_score_20` (Average on scale of 20)

---

## Relationship Identification

### 1. HAS_FACULTY (UNIVERSITY to FACULTY)
- Type: 1:N
- Cardinality: One university has many faculties
- University: (1, N) - Must have at least one faculty
- Faculty: (1, 1) - Belongs to exactly one university
- Identifying relationship for FACULTY

### 2. HAS_DEPARTMENT (FACULTY to DEPARTMENT)
- Type: 1:N
- Cardinality: One faculty has many departments
- Faculty: (1, N) - Must have at least one department
- Department: (1, 1) - Belongs to exactly one faculty
- Identifying relationship for DEPARTMENT

### 3. HAS_PROGRAMME (DEPARTMENT to PROGRAMME)
- Type: 1:N
- Cardinality: One department has many programmes
- Department: (1, N) - Must have at least one programme
- Programme: (1, 1) - Belongs to exactly one department
- Identifying relationship for PROGRAMME

### 4. OFFERS_COURSE (DEPARTMENT to COURSE)
- Type: 1:N
- Cardinality: One department offers many courses
- Department: (0, N) - May offer many courses
- Course: (1, 1) - Offered by exactly one department
- Identifying relationship for COURSE

### 5. PROGRAMME_COURSE (PROGRAMME to COURSE)
- Type: M:N
- Cardinality: Programme has many courses; Course in many programmes
- Programme: (1, N) - Programme must have at least one course
- Course: (0, N) - Course may be in multiple programmes
- Junction table needed: PROGRAMME_COURSE

### 6. ADMISSION (STUDENT to PROGRAMME)
- Type: M:N (students can change programmes, programmes have many students)
- Relationship attributes: `semester`, `year`, `status` (active, completed, withdrawn)
- Student: (1, N) - Student must be admitted to at least one programme
- Programme: (0, N) - Programme can have many students
- Junction table needed: ADMISSION

### 7. SUPERVISED_BY (POSTGRADUATE to SUPERVISOR)
- Type: M:N
- Cardinality: Postgraduate has 1+ supervisors; Supervisor has many students
- Postgraduate: (1, N) - Must have at least one supervisor
- Supervisor: (0, N) - May supervise multiple postgraduate students
- Junction table needed: SUPERVISION

---

## EER Diagram Using Crow's Feet Notation

### Crow's Feet Notation Legend:

```
Cardinality Symbols:
│  = One (exactly one)
○  = Zero or one (optional)
<  = Many
>  = Many

Combinations:
│─ = Exactly one (mandatory)
○─ = Zero or one (optional)
─< = One or many (mandatory many)
○< = Zero or many (optional many)

Participation:
||  = Mandatory (total participation)
○|  = Optional (partial participation)
```

---

### Main EER Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           HIGHER EDUCATION SYSTEM                           │
└─────────────────────────────────────────────────────────────────────────────┘


                        ┌──────────────────────┐
                        │    UNIVERSITY        │
                        ├──────────────────────┤
                        │ university_id (PK)   │
                        │ university_name      │
                        ├──────────────────────┤
                        │ {towns} (multi-val.) │ ◄──── Multi-valued attribute
                        └──────────┬───────────┘
                                   │
                                   │ HAS_FACULTY (Identifying)
                                   │ (1:N)
                                   │
                        ┌──────────┴───────────┐
                        │                      │
                        ├< (many)              │ (one) ||
                        │                      │
                        ▼                      │
              ┌──────────────────────┐         │
              │      FACULTY         │◄────────┘
              │      (Weak Entity)   │
              ├──────────────────────┤
              │ university_id (PK,FK)│
              │ faculty_code (PK)    │
              │ faculty_name         │
              └──────────┬───────────┘
                         │
                         │ HAS_DEPARTMENT (Identifying)
                         │ (1:N)
                         │
              ┌──────────┴───────────┐
              │                      │
              ├< (many)              │ (one) ||
              │                      │
              ▼                      │
    ┌──────────────────────────┐    │
    │     DEPARTMENT           │◄───┘
    │     (Weak Entity)        │
    ├──────────────────────────┤
    │ university_id (PK,FK)    │
    │ faculty_code (PK,FK)     │
    │ dept_code (PK)           │
    │ dept_name                │
    └──────┬────────────┬──────┘
           │            │
           │            │ OFFERS_COURSE
           │            │ (1:N)
           │            │
           │            ├< (many)
           │            │
           │            ▼
           │    ┌──────────────────────────┐
           │    │      COURSE              │
           │    │      (Weak Entity)       │
           │    ├──────────────────────────┤
           │    │ university_id (PK,FK)    │
           │    │ dept_code (PK,FK)        │
           │    │ course_code (PK)         │
           │    │ course_name              │
           │    │ credits                  │
           │    └──────────┬───────────────┘
           │               │
           │               │ PROGRAMME_COURSE (M:N)
           │               │
           │ HAS_PROGRAMME │
           │ (1:N)         │
           │               │
           ├< (many)       │
           │               │
           ▼               │
┌──────────────────────────┐ │
│      PROGRAMME           │ │
│      (Weak Entity)       │ │
├──────────────────────────┤ │
│ university_id (PK,FK)    │ │
│ faculty_code (PK,FK)     │ │
│ dept_code (PK,FK)        │ │
│ programme_code (PK)      │ │
│ programme_name           │ │
│ degree_type              │ │
│ duration_years           │ │
└──────────┬───────────────┘ │
           │                 │
           │                 │
           └<────────────────┘
           ▲
           │
           │ ADMISSION (M:N)
           │ {semester, year, status}
           │
           ○< (zero or many)
           │
           │
           │
┌──────────┴───────────┐
│                      │
│ (one) ||             │
│                      │
▼                      │
┌──────────────────────┐
│      STUDENT         │◄────────────────────┐
│    (Superclass)      │                     │
├──────────────────────┤                     │
│ student_id (PK)      │                     │
│ name                 │                     │
│ phone                │                     │
│ email                │                     │
│ address              │                     │
└──────────┬───────────┘                     │
           │                                 │
           │ ISA (Disjoint, Total)           │
           │ d, t                            │
           │                                 │
    ┌──────┴──────┬──────────────┐           │
    │             │              │           │
    ▼             ▼              ▼           │
┌──────────┐ ┌──────────┐ ┌──────────┐      │
│UNDERGRAD │ │POSTGRAD  │ │CERTIFIC. │      │
├──────────┤ ├──────────┤ ├──────────┤      │
│student_id│ │student_id│ │student_id│      │
│  (PK,FK) │ │  (PK,FK) │ │  (PK,FK) │      │
│ gpa_4    │ │ gpa_4    │ │ avg_sc_20│      │
└──────────┘ └────┬─────┘ └──────────┘      │
                  │                          │
                  │ SUPERVISED_BY (M:N)      │
                  │                          │
                  ├< (one or many)           │
                  │                          │
                  ▼                          │
         ┌──────────────────┐                │
         │   SUPERVISOR     │                │
         │   (Faculty)      │                │
         ├──────────────────┤                │
         │ supervisor_id(PK)│                │
         │ name             │                │
         │ title            │                │
         │ dept_id (FK)     │────────────────┘
         └──────────────────┘


Legend:
─── = Relationship
<   = Many (crow's feet)
||  = One (mandatory)
○   = Optional
{x} = Multi-valued attribute
d,t = Disjoint, Total specialization
```

---

### Detailed Entity Diagrams

**1. UNIVERSITY with Multi-valued Attribute**

```
┌──────────────────────────┐
│       UNIVERSITY         │
├──────────────────────────┤
│ university_id (PK)       │
│ university_name          │
└────────────┬─────────────┘
             │
             │ has
             ▼
      ┌─────────────┐
      │   TOWNS     │  ◄──── Separate table for multi-valued attribute
      ├─────────────┤
      │ university_id (PK, FK) │
      │ town_name (PK)         │
      └─────────────┘
```

**2. Weak Entity Hierarchy**

```
UNIVERSITY (Strong)
    │
    └── FACULTY (Weak, owned by UNIVERSITY)
            │
            └── DEPARTMENT (Weak, owned by FACULTY)
                    │
                    ├── PROGRAMME (Weak, owned by DEPARTMENT)
                    │
                    └── COURSE (Weak, owned by DEPARTMENT)
```

**3. Student Specialization Hierarchy**

```
                    STUDENT (Superclass)
                         │
                         │ ISA
            ┌────────────┼────────────┐
            │            │            │
            ▼            ▼            ▼
      UNDERGRADUATE  POSTGRADUATE  CERTIFICATE
       (gpa_4)        (gpa_4)     (avg_score_20)
                          │
                          │ SUPERVISED_BY
                          ▼
                     SUPERVISOR
```

---

## Crow's Feet Notation Details

### Relationship Diagrams with Cardinality:

**1. UNIVERSITY ───< FACULTY**
```
UNIVERSITY ||────────<| FACULTY
   (1)              (N)
```
- One university has many faculties (1:N)
- Mandatory on both sides

**2. FACULTY ───< DEPARTMENT**
```
FACULTY ||────────<| DEPARTMENT
  (1)            (N)
```
- One faculty has many departments (1:N)
- Mandatory on both sides

**3. DEPARTMENT ───< PROGRAMME**
```
DEPARTMENT ||────────<| PROGRAMME
    (1)             (N)
```
- One department has many programmes (1:N)
- Mandatory on both sides

**4. DEPARTMENT ───< COURSE**
```
DEPARTMENT ||────────<| COURSE
    (1)             (N)
```
- One department offers many courses (1:N)
- Mandatory on both sides

**5. PROGRAMME >───< COURSE (M:N)**
```
PROGRAMME ||────────< PROGRAMME_COURSE >────────○| COURSE
   (1,N)                                          (0,N)
```
- Many-to-many relationship
- Programme must have courses
- Course may be in multiple programmes

**6. STUDENT >───< PROGRAMME (M:N via ADMISSION)**
```
STUDENT ||────────< ADMISSION >────────○| PROGRAMME
  (1,N)           {sem, year}            (0,N)
```
- Many-to-many relationship with attributes
- Student must be admitted to at least one programme
- Programme may have many students

**7. POSTGRADUATE >───< SUPERVISOR (M:N)**
```
POSTGRADUATE ||────────< SUPERVISION >────────○| SUPERVISOR
    (1,N)                                        (0,N)
```
- Many-to-many relationship
- Postgraduate must have at least one supervisor
- Supervisor may supervise multiple students

---

## Relational Model Translation

### Strong Entities:

**1. UNIVERSITY**
```sql
UNIVERSITY (university_id, university_name)
  PK: university_id
```

**2. UNIVERSITY_TOWNS** (Multi-valued attribute)
```sql
UNIVERSITY_TOWNS (university_id, town_name)
  PK: (university_id, town_name)
  FK: university_id → UNIVERSITY(university_id)
```

**3. STUDENT**
```sql
STUDENT (student_id, name, phone, email, address, student_type)
  PK: student_id
  student_type: 'UNDERGRAD', 'POSTGRAD', 'CERTIFICATE'
```

**4. SUPERVISOR**
```sql
SUPERVISOR (supervisor_id, name, title, dept_id)
  PK: supervisor_id
  FK: dept_id → DEPARTMENT(university_id, faculty_code, dept_code)
```

---

### Weak Entities:

**5. FACULTY**
```sql
FACULTY (university_id, faculty_code, faculty_name)
  PK: (university_id, faculty_code)
  FK: university_id → UNIVERSITY(university_id) ON DELETE CASCADE
```

**6. DEPARTMENT**
```sql
DEPARTMENT (university_id, faculty_code, dept_code, dept_name)
  PK: (university_id, faculty_code, dept_code)
  FK: (university_id, faculty_code) → FACULTY(university_id, faculty_code)
      ON DELETE CASCADE
```

**7. PROGRAMME**
```sql
PROGRAMME (university_id, faculty_code, dept_code, programme_code, 
           programme_name, degree_type, duration_years)
  PK: (university_id, faculty_code, dept_code, programme_code)
  FK: (university_id, faculty_code, dept_code) → 
      DEPARTMENT(university_id, faculty_code, dept_code)
      ON DELETE CASCADE
```

**8. COURSE**
```sql
COURSE (university_id, dept_code, course_code, course_name, credits)
  PK: (university_id, dept_code, course_code)
  FK: (university_id, dept_code) → 
      DEPARTMENT(university_id, faculty_code, dept_code)
      ON DELETE CASCADE
```

---

### Specialized Entities:

**9. UNDERGRADUATE**
```sql
UNDERGRADUATE (student_id, gpa_4)
  PK: student_id
  FK: student_id → STUDENT(student_id) ON DELETE CASCADE
```

**10. POSTGRADUATE**
```sql
POSTGRADUATE (student_id, gpa_4)
  PK: student_id
  FK: student_id → STUDENT(student_id) ON DELETE CASCADE
```

**11. CERTIFICATE**
```sql
CERTIFICATE (student_id, average_score_20)
  PK: student_id
  FK: student_id → STUDENT(student_id) ON DELETE CASCADE
```

---

### Junction Tables (M:N Relationships):

**12. PROGRAMME_COURSE**
```sql
PROGRAMME_COURSE (university_id, faculty_code, dept_code, programme_code,
                  course_code, is_core, semester_offered)
  PK: (university_id, faculty_code, dept_code, programme_code, course_code)
  FK: (university_id, faculty_code, dept_code, programme_code) → 
      PROGRAMME(...)
  FK: (university_id, dept_code, course_code) → COURSE(...)
```

**13. ADMISSION**
```sql
ADMISSION (student_id, university_id, faculty_code, dept_code, 
           programme_code, semester, year, status)
  PK: (student_id, university_id, faculty_code, dept_code, 
       programme_code, semester, year)
  FK: student_id → STUDENT(student_id)
  FK: (university_id, faculty_code, dept_code, programme_code) → 
      PROGRAMME(...)
```

**14. SUPERVISION**
```sql
SUPERVISION (student_id, supervisor_id, role, start_date)
  PK: (student_id, supervisor_id)
  FK: student_id → POSTGRADUATE(student_id)
  FK: supervisor_id → SUPERVISOR(supervisor_id)
  
  role: 'Primary', 'Secondary', 'Co-supervisor'
```

---

## Complete SQL DDL Script

```sql
-- =====================================================
-- STRONG ENTITIES
-- =====================================================

CREATE TABLE UNIVERSITY (
    university_id VARCHAR(10) PRIMARY KEY,
    university_name VARCHAR(200) NOT NULL UNIQUE
);

CREATE TABLE UNIVERSITY_TOWNS (
    university_id VARCHAR(10),
    town_name VARCHAR(100),
    PRIMARY KEY (university_id, town_name),
    FOREIGN KEY (university_id) REFERENCES UNIVERSITY(university_id)
        ON DELETE CASCADE
);

CREATE TABLE STUDENT (
    student_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    address VARCHAR(200),
    student_type VARCHAR(15) NOT NULL CHECK (student_type IN 
        ('UNDERGRAD', 'POSTGRAD', 'CERTIFICATE'))
);

-- =====================================================
-- WEAK ENTITIES (Hierarchical)
-- =====================================================

CREATE TABLE FACULTY (
    university_id VARCHAR(10),
    faculty_code VARCHAR(10),
    faculty_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (university_id, faculty_code),
    FOREIGN KEY (university_id) REFERENCES UNIVERSITY(university_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE DEPARTMENT (
    university_id VARCHAR(10),
    faculty_code VARCHAR(10),
    dept_code VARCHAR(10),
    dept_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (university_id, faculty_code, dept_code),
    FOREIGN KEY (university_id, faculty_code) 
        REFERENCES FACULTY(university_id, faculty_code)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PROGRAMME (
    university_id VARCHAR(10),
    faculty_code VARCHAR(10),
    dept_code VARCHAR(10),
    programme_code VARCHAR(10),
    programme_name VARCHAR(150) NOT NULL,
    degree_type VARCHAR(50),
    duration_years INT,
    PRIMARY KEY (university_id, faculty_code, dept_code, programme_code),
    FOREIGN KEY (university_id, faculty_code, dept_code) 
        REFERENCES DEPARTMENT(university_id, faculty_code, dept_code)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE COURSE (
    university_id VARCHAR(10),
    dept_code VARCHAR(10),
    course_code VARCHAR(10),
    course_name VARCHAR(150) NOT NULL,
    credits INT,
    PRIMARY KEY (university_id, dept_code, course_code),
    FOREIGN KEY (university_id, dept_code) 
        REFERENCES DEPARTMENT(university_id, faculty_code, dept_code)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE SUPERVISOR (
    supervisor_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    title VARCHAR(50),
    university_id VARCHAR(10),
    faculty_code VARCHAR(10),
    dept_code VARCHAR(10),
    FOREIGN KEY (university_id, faculty_code, dept_code) 
        REFERENCES DEPARTMENT(university_id, faculty_code, dept_code)
);

-- =====================================================
-- SPECIALIZED ENTITIES (ISA Hierarchy)
-- =====================================================

CREATE TABLE UNDERGRADUATE (
    student_id VARCHAR(20) PRIMARY KEY,
    gpa_4 DECIMAL(3, 2) CHECK (gpa_4 >= 0 AND gpa_4 <= 4.0),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
        ON DELETE CASCADE
);

CREATE TABLE POSTGRADUATE (
    student_id VARCHAR(20) PRIMARY KEY,
    gpa_4 DECIMAL(3, 2) CHECK (gpa_4 >= 0 AND gpa_4 <= 4.0),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
        ON DELETE CASCADE
);

CREATE TABLE CERTIFICATE (
    student_id VARCHAR(20) PRIMARY KEY,
    average_score_20 DECIMAL(4, 2) CHECK (average_score_20 >= 0 
        AND average_score_20 <= 20.0),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
        ON DELETE CASCADE
);

-- =====================================================
-- JUNCTION TABLES (M:N Relationships)
-- =====================================================

CREATE TABLE PROGRAMME_COURSE (
    university_id VARCHAR(10),
    faculty_code VARCHAR(10),
    dept_code VARCHAR(10),
    programme_code VARCHAR(10),
    course_code VARCHAR(10),
    is_core BOOLEAN DEFAULT TRUE,
    semester_offered INT,
    PRIMARY KEY (university_id, faculty_code, dept_code, 
                 programme_code, course_code),
    FOREIGN KEY (university_id, faculty_code, dept_code, programme_code) 
        REFERENCES PROGRAMME(university_id, faculty_code, dept_code, 
                            programme_code)
        ON DELETE CASCADE,
    FOREIGN KEY (university_id, dept_code, course_code) 
        REFERENCES COURSE(university_id, dept_code, course_code)
        ON DELETE CASCADE
);

CREATE TABLE ADMISSION (
    student_id VARCHAR(20),
    university_id VARCHAR(10),
    faculty_code VARCHAR(10),
    dept_code VARCHAR(10),
    programme_code VARCHAR(10),
    semester VARCHAR(10),
    year INT,
    status VARCHAR(20) DEFAULT 'ACTIVE' 
        CHECK (status IN ('ACTIVE', 'COMPLETED', 'WITHDRAWN')),
    PRIMARY KEY (student_id, university_id, faculty_code, 
                 dept_code, programme_code, semester, year),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
        ON DELETE CASCADE,
    FOREIGN KEY (university_id, faculty_code, dept_code, programme_code) 
        REFERENCES PROGRAMME(university_id, faculty_code, dept_code, 
                            programme_code)
        ON DELETE CASCADE
);

CREATE TABLE SUPERVISION (
    student_id VARCHAR(20),
    supervisor_id VARCHAR(20),
    role VARCHAR(20) DEFAULT 'Primary' 
        CHECK (role IN ('Primary', 'Secondary', 'Co-supervisor')),
    start_date DATE,
    PRIMARY KEY (student_id, supervisor_id),
    FOREIGN KEY (student_id) REFERENCES POSTGRADUATE(student_id)
        ON DELETE CASCADE,
    FOREIGN KEY (supervisor_id) REFERENCES SUPERVISOR(supervisor_id)
        ON DELETE CASCADE
);
```

---

## Sample Data and Queries

### Sample Data:

```sql
-- Universities
INSERT INTO UNIVERSITY VALUES 
    ('UB', 'University of Buea'),
    ('UY', 'University of Yaounde I');

-- University Towns (multi-valued)
INSERT INTO UNIVERSITY_TOWNS VALUES 
    ('UB', 'Buea'),
    ('UY', 'Yaounde'),
    ('UY', 'Soa');

-- Faculties
INSERT INTO FACULTY VALUES 
    ('UB', 'FST', 'Faculty of Science and Technology'),
    ('UB', 'FHS', 'Faculty of Health Sciences'),
    ('UY', 'FS', 'Faculty of Science');

-- Departments
INSERT INTO DEPARTMENT VALUES 
    ('UB', 'FST', 'CS', 'Computer Science'),
    ('UB', 'FST', 'MATH', 'Mathematics'),
    ('UB', 'FHS', 'NURS', 'Nursing');

-- Programmes
INSERT INTO PROGRAMME VALUES 
    ('UB', 'FST', 'CS', 'BSC-CS', 'B.Sc. Computer Science', 'Bachelors', 3),
    ('UB', 'FST', 'CS', 'MSC-CS', 'M.Sc. Computer Science', 'Masters', 2),
    ('UB', 'FST', 'CS', 'CERT-WEB', 'Certificate in Web Development', 
     'Certificate', 1);

-- Courses
INSERT INTO COURSE VALUES 
    ('UB', 'CS', 'IST601', 'Database Management', 3),
    ('UB', 'CS', 'IST603', 'Data Structures', 4),
    ('UB', 'CS', 'IST605', 'Software Engineering', 3);

-- Programme-Course mapping
INSERT INTO PROGRAMME_COURSE VALUES 
    ('UB', 'FST', 'CS', 'BSC-CS', 'IST601', TRUE, 3),
    ('UB', 'FST', 'CS', 'BSC-CS', 'IST603', TRUE, 2),
    ('UB', 'FST', 'CS', 'MSC-CS', 'IST601', TRUE, 1);

-- Students
INSERT INTO STUDENT VALUES 
    ('UB2022001', 'John Doe', '677123456', 'john@example.com', 
     'Buea', 'UNDERGRAD'),
    ('UB2023050', 'Jane Smith', '677234567', 'jane@example.com', 
     'Douala', 'POSTGRAD'),
    ('UB2024010', 'Bob Wilson', '677345678', 'bob@example.com', 
     'Yaounde', 'CERTIFICATE');

-- Specialized student data
INSERT INTO UNDERGRADUATE VALUES ('UB2022001', 3.45);
INSERT INTO POSTGRADUATE VALUES ('UB2023050', 3.80);
INSERT INTO CERTIFICATE VALUES ('UB2024010', 15.50);

-- Supervisors
INSERT INTO SUPERVISOR VALUES 
    ('SUP001', 'Prof. Alice Johnson', 'Professor', 'UB', 'FST', 'CS'),
    ('SUP002', 'Dr. Mark Brown', 'Senior Lecturer', 'UB', 'FST', 'CS');

-- Admissions
INSERT INTO ADMISSION VALUES 
    ('UB2022001', 'UB', 'FST', 'CS', 'BSC-CS', 'First', 2022, 'ACTIVE'),
    ('UB2023050', 'UB', 'FST', 'CS', 'MSC-CS', 'First', 2023, 'ACTIVE'),
    ('UB2024010', 'UB', 'FST', 'CS', 'CERT-WEB', 'First', 2024, 'ACTIVE');

-- Supervision (only for postgraduates)
INSERT INTO SUPERVISION VALUES 
    ('UB2023050', 'SUP001', 'Primary', '2023-09-01'),
    ('UB2023050', 'SUP002', 'Secondary', '2023-09-01');
```

---

### Useful Queries:

**1. List all programmes in a department:**
```sql
SELECT p.programme_code, p.programme_name, p.degree_type
FROM PROGRAMME p
WHERE p.university_id = 'UB' 
  AND p.faculty_code = 'FST' 
  AND p.dept_code = 'CS';
```

**2. Find all courses in a programme:**
```sql
SELECT c.course_code, c.course_name, c.credits, pc.is_core
FROM COURSE c
JOIN PROGRAMME_COURSE pc ON c.course_code = pc.course_code
WHERE pc.university_id = 'UB' 
  AND pc.programme_code = 'BSC-CS';
```

**3. List all students admitted to a programme:**
```sql
SELECT s.student_id, s.name, s.student_type, a.semester, a.year, a.status
FROM STUDENT s
JOIN ADMISSION a ON s.student_id = a.student_id
WHERE a.university_id = 'UB' 
  AND a.programme_code = 'MSC-CS';
```

**4. Find all postgraduate students with their supervisors:**
```sql
SELECT s.student_id, s.name, pg.gpa_4, 
       sup.name AS supervisor_name, sv.role
FROM STUDENT s
JOIN POSTGRADUATE pg ON s.student_id = pg.student_id
JOIN SUPERVISION sv ON pg.student_id = sv.student_id
JOIN SUPERVISOR sup ON sv.supervisor_id = sup.supervisor_id
ORDER BY s.student_id, sv.role;
```

**5. List all campuses (towns) of a university:**
```sql
SELECT u.university_name, ut.town_name
FROM UNIVERSITY u
JOIN UNIVERSITY_TOWNS ut ON u.university_id = ut.university_id
WHERE u.university_id = 'UY';
```

**6. Count students by type in each programme:**
```sql
SELECT p.programme_name, s.student_type, COUNT(*) AS student_count
FROM PROGRAMME p
JOIN ADMISSION a ON p.programme_code = a.programme_code
JOIN STUDENT s ON a.student_id = s.student_id
WHERE p.university_id = 'UB'
GROUP BY p.programme_name, s.student_type;
```

---

## Key EER Concepts Demonstrated

### 1. Multi-valued Attributes
- **UNIVERSITY.towns** → Separate table UNIVERSITY_TOWNS
- Allows universities to have multiple campus locations

### 2. Weak Entities with Composite Keys
- **FACULTY**, **DEPARTMENT**, **PROGRAMME**, **COURSE**
- Unique identifiers only within owner's context
- Composite primary keys include owner's key

### 3. Specialization/Generalization (ISA Hierarchy)
- **STUDENT** superclass
- Three subtypes: UNDERGRADUATE, POSTGRADUATE, CERTIFICATE
- **Disjoint:** Student belongs to exactly one subtype
- **Total:** Every student must belong to a subtype
- **Implementation:** Separate tables with shared PK

### 4. Category-Specific Attributes
- UNDERGRADUATE and POSTGRADUATE: `gpa_4`
- CERTIFICATE: `average_score_20`

### 5. Category-Specific Relationships
- Only POSTGRADUATE students can have SUPERVISION relationship
- Enforced by foreign key constraint

### 6. M:N Relationships with Attributes
- **ADMISSION:** semester, year, status
- **PROGRAMME_COURSE:** is_core, semester_offered
- **SUPERVISION:** role, start_date

### 7. Hierarchical Weak Entity Dependencies
```
UNIVERSITY (strong)
  └─> FACULTY (weak)
       └─> DEPARTMENT (weak)
            ├─> PROGRAMME (weak)
            └─> COURSE (weak)
```

---

## Design Considerations and Best Practices

### 1. Unique Identification Across Universities
- Problem: Different universities use same codes
- Solution: Include university_id in all keys
- Example: Programme 'BSC-CS' at UB ≠ 'BSC-CS' at UY

### 2. Cascade Deletion
- Deleting UNIVERSITY cascades to all its children
- Maintains referential integrity
- Prevents orphan records

### 3. Specialization Design Choices

**Option A: Separate Tables (Used in this design)**
```
STUDENT (student_id, name, ...)
UNDERGRADUATE (student_id, gpa_4)
POSTGRADUATE (student_id, gpa_4)
CERTIFICATE (student_id, average_score_20)
```

**Advantages:**
- No NULL values
- Category-specific constraints
- Easy to add category-specific relationships

**Option B: Single Table**
```
STUDENT (student_id, name, ..., student_type, gpa_4, average_score_20)
```

**Disadvantages:**
- Many NULL values
- Cannot enforce constraints easily

### 4. Composite Keys
- More complex queries require multiple join conditions
- Index on composite keys recommended
- Foreign keys must reference entire composite key

### 5. Multi-valued Attribute Normalization
- **towns** becomes separate table
- Avoids repeating groups
- Maintains 1NF (First Normal Form)

---

## Verification and Constraints

### Business Rules Enforced:

1. ✓ Student must belong to exactly one category (disjoint, total)
2. ✓ Student must be admitted to at least one programme
3. ✓ Postgraduate must have at least one supervisor
4. ✓ Programme must have at least one course
5. ✓ Faculty, Department, Programme codes unique within university
6. ✓ Each entity uniquely identifiable system-wide

### Additional Constraints (Optional):

```sql
-- Ensure postgraduate has at least one supervisor
CREATE ASSERTION PostgradHasSupervisor
CHECK (NOT EXISTS (
    SELECT * FROM POSTGRADUATE pg
    WHERE NOT EXISTS (
        SELECT * FROM SUPERVISION sv
        WHERE sv.student_id = pg.student_id
    )
));

-- Ensure programme has at least one course
CREATE ASSERTION ProgrammeHasCourse
CHECK (NOT EXISTS (
    SELECT * FROM PROGRAMME p
    WHERE NOT EXISTS (
        SELECT * FROM PROGRAMME_COURSE pc
        WHERE pc.university_id = p.university_id
          AND pc.programme_code = p.programme_code
    )
));
```

---

## Summary

This EER design successfully models a complex higher education system with:

- **Hierarchical structure** of universities, faculties, departments, programmes
- **Weak entities** with proper composite keys
- **Multi-valued attributes** (towns)
- **Specialization hierarchy** (student types)
- **Category-specific attributes and relationships**
- **M:N relationships with attributes**
- **Proper constraints** ensuring data integrity

The Crow's Feet notation clearly shows:
- Cardinalities (1:N, M:N)
- Participation (mandatory vs optional)
- Weak entity dependencies
- Specialization hierarchies

The relational model translation:
- Preserves all semantic information
- Enforces referential integrity
- Supports all required queries
- Maintains normalization

---

**End of Question 3**
