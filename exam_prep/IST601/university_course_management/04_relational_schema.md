# Relational Schema

## Normalized Schema (Final Design)

### STUDENT (StudentID, StudentName, Email, Phone, DateOfBirth, Major)
- **Primary Key:** StudentID
- **Constraints:**
  - StudentID is unique
  - Email should be unique
  - Major cannot be NULL

### INSTRUCTOR (InstructorID, InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom)
- **Primary Key:** InstructorID
- **Constraints:**
  - InstructorID is unique
  - Email should be unique
  - Department cannot be NULL

### COURSE (CourseCode, CourseTitle, CreditHours, Department, Description)
- **Primary Key:** CourseCode
- **Constraints:**
  - CourseCode is unique
  - CreditHours must be > 0
  - Department cannot be NULL

### ENROLLMENT (EnrollmentID, StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade)
- **Primary Key:** EnrollmentID
- **Foreign Keys:**
  - StudentID → STUDENT(StudentID)
  - CourseCode → COURSE(CourseCode)
  - InstructorID → INSTRUCTOR(InstructorID)
- **Constraints:**
  - EnrollmentID is unique
  - (StudentID, CourseCode, Semester, Year) should be unique (composite unique constraint)
  - Semester must be one of: Fall, Spring, Summer
  - Grade must be one of: A, B, C, D, F, or NULL
  - Year must be > 2000

---

## Normalization Reference

The schema above is in **BCNF**. See `08_normalization_process.md` for the normalization analysis verifying each table satisfies 1NF, 2NF, 3NF, and BCNF.

---

## Schema Notation

**Format:** RELATION_NAME (Attribute1, Attribute2, Attribute3, ...)
- **Underlined attributes:** Primary Key
- **Italicized attributes:** Foreign Keys
- **Bold attributes:** Required (NOT NULL)

## Functional Dependencies (For Normalization)

### STUDENT
- StudentID → StudentName, Email, Phone, DateOfBirth, Major

### INSTRUCTOR
- InstructorID → InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom

### COURSE
- CourseCode → CourseTitle, CreditHours, Department, Description
- **Note:** CourseCode does NOT determine InstructorID (same course can have different instructors)

### ENROLLMENT
- EnrollmentID → StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade
- StudentID → (from STUDENT: StudentName, Email, Phone, DateOfBirth, Major)
- CourseCode → (from COURSE: CourseTitle, CreditHours, Department, Description)
- InstructorID → (from INSTRUCTOR: InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom)
- (StudentID, CourseCode, Semester, Year) → EnrollmentID, InstructorID, EnrollmentDate, Grade
- **Important:** (CourseCode, Semester, Year) → InstructorID (instructor assignment is per course offering, not per course permanently)

## Design Rationale: Why InstructorID is in ENROLLMENT, not COURSE

**Key Point:** The instructor assignment is **contextual to the enrollment** (specific semester/year), not a permanent property of the course.

**Why this design:**
1. **Semester-specific assignments:** CS101 might be taught by Dr. Johnson in Fall 2024 but Dr. Lee in Spring 2025
2. **Multiple sections:** The same course can have multiple sections with different instructors in the same semester
3. **Historical tracking:** We can track which instructor taught which course in which semester
4. **Flexibility:** Courses can be reassigned without changing the course definition

**If we put InstructorID in COURSE instead:**
- Would imply each course has ONE permanent instructor
- Cannot change instructors per semester
- Cannot have multiple sections
- Less flexible and less realistic

**Our design correctly models:** Course offerings (enrollments) have instructors, not courses themselves.

## Referential Integrity Rules

1. **ON DELETE CASCADE:** If a student is deleted, all their enrollments should be deleted
2. **ON DELETE RESTRICT:** If a course is deleted, check if there are enrollments (prevent deletion if enrollments exist)
3. **ON UPDATE CASCADE:** If a StudentID is updated, update all related enrollments
