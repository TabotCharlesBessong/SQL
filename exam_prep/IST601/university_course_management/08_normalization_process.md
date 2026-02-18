# Database Normalization Process: 1NF to BCNF

## Overview

This document analyzes the four tables from the relational schema (STUDENT, INSTRUCTOR, COURSE, ENROLLMENT) and verifies that each satisfies 1NF, 2NF, 3NF, and BCNF.

**Tables under analysis:**
- STUDENT (StudentID, StudentName, Email, Phone, DateOfBirth, Major)
- INSTRUCTOR (InstructorID, InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom)
- COURSE (CourseCode, CourseTitle, CreditHours, Department, Description)
- ENROLLMENT (EnrollmentID, StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade)

---

## FIRST NORMAL FORM (1NF)

### Definition

A relation is in **1NF** if:
1. All attributes contain **atomic (indivisible)** values
2. Each attribute has a **unique name**
3. All rows are **unique**
4. Order of rows and columns does not matter

### Analysis of Each Table

| Table | Atomic values | Unique attributes | Unique rows | Order independence | Result |
|-------|---------------|-------------------|-------------|--------------------|--------|
| STUDENT | ✅ All atomic | ✅ | ✅ (StudentID PK) | ✅ | 1NF |
| INSTRUCTOR | ✅ All atomic | ✅ | ✅ (InstructorID PK) | ✅ | 1NF |
| COURSE | ✅ All atomic | ✅ | ✅ (CourseCode PK) | ✅ | 1NF |
| ENROLLMENT | ✅ All atomic | ✅ | ✅ (EnrollmentID PK) | ✅ | 1NF |

**Conclusion:** All four tables satisfy 1NF.

---

## SECOND NORMAL FORM (2NF)

### Definition

A relation is in **2NF** if:
1. It is in 1NF
2. All non-key attributes are **fully functionally dependent** on the primary key  
   - No **partial dependencies**: a non-key attribute must not depend on only part of a composite key

### Analysis of Each Table

**STUDENT**
- PK: StudentID (simple key)
- All attributes depend on StudentID
- No composite key, so no partial dependencies possible
- ✅ 2NF

**INSTRUCTOR**
- PK: InstructorID (simple key)
- All attributes depend on InstructorID
- No composite key
- ✅ 2NF

**COURSE**
- PK: CourseCode (simple key)
- All attributes depend on CourseCode
- No composite key
- ✅ 2NF

**ENROLLMENT**
- PK: EnrollmentID (simple key)
- CK: (StudentID, CourseCode, Semester, Year)
- All non-key attributes depend on EnrollmentID (or the full candidate key)
- No partial dependencies: no attribute depends on only part of the composite key
- ✅ 2NF

**Conclusion:** All four tables satisfy 2NF.

---

## THIRD NORMAL FORM (3NF)

### Definition

A relation is in **3NF** if:
1. It is in 2NF
2. No **transitive dependencies**: no non-key attribute depends on another non-key attribute

### Analysis of Each Table

**STUDENT**
- FD: StudentID → StudentName, Email, Phone, DateOfBirth, Major
- No non-key attribute determines another non-key attribute
- ✅ 3NF

**INSTRUCTOR**
- FD: InstructorID → InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom
- No transitive dependencies
- ✅ 3NF

**COURSE**
- FD: CourseCode → CourseTitle, CreditHours, Department, Description
- No transitive dependencies
- ✅ 3NF

**ENROLLMENT**
- FD: EnrollmentID → StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade
- All non-key attributes depend directly on EnrollmentID (or the candidate key)
- No transitive dependencies within ENROLLMENT
- ✅ 3NF

**Conclusion:** All four tables satisfy 3NF.

---

## BOYCE-CODD NORMAL FORM (BCNF)

### Definition

A relation is in **BCNF** if:
1. It is in 3NF
2. For every non-trivial functional dependency X → Y, **X is a superkey**

### Analysis of Each Table

**STUDENT**
- FD: StudentID → StudentName, Email, Phone, DateOfBirth, Major  
- Determinant: StudentID (superkey)  
- ✅ BCNF

**INSTRUCTOR**
- FD: InstructorID → InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom  
- Determinant: InstructorID (superkey)  
- ✅ BCNF

**COURSE**
- FD: CourseCode → CourseTitle, CreditHours, Department, Description  
- Determinant: CourseCode (superkey)  
- ✅ BCNF

**ENROLLMENT**

| FD | Determinant | Superkey? |
|----|-------------|-----------|
| EnrollmentID → StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade | EnrollmentID | ✅ Yes (PK) |
| (StudentID, CourseCode, Semester, Year) → EnrollmentID, InstructorID, EnrollmentDate, Grade | (StudentID, CourseCode, Semester, Year) | ✅ Yes (candidate key) |

**Note on (CourseCode, Semester, Year) → InstructorID:**  
We allow multiple sections: the same course in the same semester can have different instructors. So (CourseCode, Semester, Year) does **not** functionally determine InstructorID, and there is no BCNF violation.

**Conclusion:** All four tables satisfy BCNF.

---

## Normalization Summary

| Normal Form | Requirement | STUDENT | INSTRUCTOR | COURSE | ENROLLMENT |
|-------------|-------------|---------|------------|--------|------------|
| **1NF** | Atomic values, unique rows | ✅ | ✅ | ✅ | ✅ |
| **2NF** | No partial dependencies | ✅ | ✅ | ✅ | ✅ |
| **3NF** | No transitive dependencies | ✅ | ✅ | ✅ | ✅ |
| **BCNF** | Every determinant is a superkey | ✅ | ✅ | ✅ | ✅ |

---

## Final Schema (from Relational Schema)

```
STUDENT (StudentID, StudentName, Email, Phone, DateOfBirth, Major)
PK: StudentID

INSTRUCTOR (InstructorID, InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom)
PK: InstructorID

COURSE (CourseCode, CourseTitle, CreditHours, Department, Description)
PK: CourseCode

ENROLLMENT (EnrollmentID, StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade)
PK: EnrollmentID
CK: (StudentID, CourseCode, Semester, Year)
FK: StudentID → STUDENT, CourseCode → COURSE, InstructorID → INSTRUCTOR
```

---

## Functional Dependency Summary

| Table | Functional Dependencies |
|-------|-------------------------|
| STUDENT | StudentID → StudentName, Email, Phone, DateOfBirth, Major |
| INSTRUCTOR | InstructorID → InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom |
| COURSE | CourseCode → CourseTitle, CreditHours, Department, Description |
| ENROLLMENT | EnrollmentID → StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade |
| ENROLLMENT | (StudentID, CourseCode, Semester, Year) → EnrollmentID, InstructorID, EnrollmentDate, Grade |

---

## Benefits of This Schema

1. **No insertion anomalies** — Students, courses, and instructors can be added without enrollments.
2. **No deletion anomalies** — Deleting enrollments does not remove student, course, or instructor data.
3. **No update anomalies** — Each fact is stored once; updates happen in one place.
4. **Reduced redundancy** — No repeated student, course, or instructor attributes.
5. **Referential integrity** — Foreign keys maintain consistent relationships.
