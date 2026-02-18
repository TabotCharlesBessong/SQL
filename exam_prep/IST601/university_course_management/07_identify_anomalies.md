# Database Anomalies Identification

## Overview
This document identifies the three main types of anomalies present in the unnormalized database design: Insertion Anomalies, Deletion Anomalies, and Update Anomalies.

---

## 1. INSERTION ANOMALIES

**Definition:** Problems that occur when trying to insert new data into the database.

### Example 1: Cannot Add a New Course Without a Student Enrollment
**Problem:** If we want to add a new course "CS401 - Advanced Algorithms" that hasn't been enrolled in yet, we cannot do so because all course information is stored only within enrollment records.

**SQL Attempt:**
```sql
-- This won't work - we need StudentID, InstructorID, Semester, Year, etc.
INSERT INTO UnnormalizedEnrollment (CourseCode, CourseTitle, CourseCreditHours, CourseDepartment, CourseDescription)
VALUES ('CS401', 'Advanced Algorithms', 3, 'CS Department', 'Advanced algorithm design and analysis');
-- ERROR: Cannot insert NULL values for required enrollment fields
```

**Why it fails:** The table requires enrollment-specific fields (StudentID, Semester, Year, etc.) even when we only want to add course information.

### Example 2: Cannot Add a New Student Without Enrollment
**Problem:** If a new student registers but hasn't enrolled in any courses yet, we cannot add their information to the database.

**SQL Attempt:**
```sql
-- This won't work - we need CourseCode, InstructorID, Semester, Year, etc.
INSERT INTO UnnormalizedEnrollment (StudentID, StudentName, StudentEmail, StudentPhone, StudentDOB, StudentMajor)
VALUES ('S009', 'New Student', 'new.student@university.edu', '555-0109', '2002-01-01', 'Computer Science');
-- ERROR: Cannot insert NULL values for required enrollment fields
```

**Why it fails:** The table requires course and enrollment information even when we only want to add student information.

### Example 3: Cannot Add a New Instructor Without Course Assignment
**Problem:** If a new instructor is hired but hasn't been assigned to teach any courses yet, we cannot add their information.

**SQL Attempt:**
```sql
-- This won't work - we need StudentID, CourseCode, Semester, Year, etc.
INSERT INTO UnnormalizedEnrollment (InstructorID, InstructorName, InstructorEmail, InstructorDepartment)
VALUES ('I005', 'Dr. New Instructor', 'new.instructor@university.edu', 'Math Department');
-- ERROR: Cannot insert NULL values for required enrollment fields
```

**Why it fails:** The table requires student and course information even when we only want to add instructor information.

**Note:** In the normalized design, instructors can be added independently. Also note that instructor assignment is per enrollment (per semester), not per course permanently, so instructors don't need to be assigned to courses immediately.

---

## 2. DELETION ANOMALIES

**Definition:** Problems that occur when deleting data causes unintended loss of information.

### Example 1: Deleting Last Enrollment Loses Student Information
**Problem:** If a student drops their last (or only) course, deleting that enrollment record will also delete all the student's information.

**SQL Demonstration:**
```sql
-- Check student S008's enrollments
SELECT * FROM UnnormalizedEnrollment WHERE StudentID = 'S008';
-- Shows 2 enrollments

-- Delete both enrollments (student drops all courses)
DELETE FROM UnnormalizedEnrollment WHERE StudentID = 'S008';

-- Now try to find student S008's information
SELECT * FROM UnnormalizedEnrollment WHERE StudentID = 'S008';
-- Returns no rows - student information is lost!
```

**Impact:** The student's personal information (name, email, phone, DOB, major) is permanently lost even though the student still exists at the university.

### Example 2: Deleting Last Enrollment Loses Course Information
**Problem:** If all students drop a course, deleting those enrollment records will also delete the course information.

**SQL Demonstration:**
```sql
-- Check enrollments for CS301
SELECT * FROM UnnormalizedEnrollment WHERE CourseCode = 'CS301';
-- Shows 2 enrollments

-- Delete all enrollments (all students drop the course)
DELETE FROM UnnormalizedEnrollment WHERE CourseCode = 'CS301';

-- Now try to find CS301 course information
SELECT * FROM UnnormalizedEnrollment WHERE CourseCode = 'CS301';
-- Returns no rows - course information is lost!
```

**Impact:** The course information (title, credit hours, department, description) is permanently lost even though the course may be offered again in the future.

### Example 3: Deleting Enrollment Loses Instructor Information
**Problem:** If an instructor's only course enrollment is deleted, the instructor's information is lost.

**SQL Demonstration:**
```sql
-- Check enrollments for I004 (Dr. David Lee)
SELECT * FROM UnnormalizedEnrollment WHERE InstructorID = 'I004';
-- Shows 2 enrollments

-- Delete all enrollments for this instructor
DELETE FROM UnnormalizedEnrollment WHERE InstructorID = 'I004';

-- Now try to find instructor I004's information
SELECT * FROM UnnormalizedEnrollment WHERE InstructorID = 'I004';
-- Returns no rows - instructor information is lost!
```

**Impact:** The instructor's information (name, email, phone, department, office location) is permanently lost even though the instructor still works at the university.

---

## 3. UPDATE ANOMALIES

**Definition:** Problems that occur when updating data requires changes in multiple places, leading to inconsistency.

### Example 1: Updating Student Email Requires Multiple Updates
**Problem:** If a student changes their email address, we must update it in every enrollment record, and it's easy to miss some.

**SQL Demonstration:**
```sql
-- Student S001 (John Smith) has 3 enrollments
-- If his email changes from 'john.smith@university.edu' to 'john.smith.new@university.edu'

-- We must update ALL enrollment records
UPDATE UnnormalizedEnrollment 
SET StudentEmail = 'john.smith.new@university.edu'
WHERE StudentID = 'S001';

-- But what if we miss one? Or update incorrectly?
-- Risk of data inconsistency!
```

**Impact:** 
- Must update multiple rows (3 rows for S001)
- Risk of missing some updates (data inconsistency)
- If one record isn't updated, queries will show different email addresses for the same student

### Example 2: Updating Course Credit Hours Requires Multiple Updates
**Problem:** If a course's credit hours change, we must update it in every enrollment record.

**SQL Demonstration:**
```sql
-- CS101 has 6 enrollments
-- If credit hours change from 3 to 4

-- We must update ALL enrollment records
UPDATE UnnormalizedEnrollment 
SET CourseCreditHours = 4
WHERE CourseCode = 'CS101';

-- But what if we miss one?
-- Risk of showing incorrect credit hours!
```

**Impact:**
- Must update multiple rows (6 rows for CS101)
- Risk of data inconsistency
- If one record shows 3 credits and others show 4, which is correct?

### Example 3: Updating Instructor Department Requires Multiple Updates
**Problem:** If an instructor changes departments, we must update it in every enrollment record.

**SQL Demonstration:**
```sql
-- Dr. Alice Johnson (I001) has 8 enrollments
-- If she moves from 'CS Department' to 'Computer Engineering Department'

-- We must update ALL enrollment records
UPDATE UnnormalizedEnrollment 
SET InstructorDepartment = 'Computer Engineering Department'
WHERE InstructorID = 'I001';

-- But what if we miss some?
-- Risk of showing instructor in wrong department!
```

**Impact:**
- Must update multiple rows (8 rows for I001)
- Risk of data inconsistency
- Reports might show the instructor in different departments

**Note:** In the normalized design, instructor department is stored once in the Instructor table. Also, instructor assignment is per enrollment (per semester), so historical enrollments preserve which department the instructor was in at that time.

### Example 4: Updating Instructor Office Location
**Problem:** If an instructor moves to a new office, we must update it in every enrollment record.

**SQL Demonstration:**
```sql
-- Dr. Bob Williams (I002) moves from MB-305 to MB-310

-- We must update ALL enrollment records
UPDATE UnnormalizedEnrollment 
SET InstructorOfficeRoom = 'MB-310'
WHERE InstructorID = 'I002';

-- Risk of inconsistency if we miss some records
```

**Impact:**
- Must update multiple rows
- Risk of showing incorrect office location
- Students might go to the wrong office

---

## Summary of Problems

| Anomaly Type | Count of Issues | Severity |
|-------------|----------------|----------|
| **Insertion** | 3 major issues | High - Cannot add independent entities |
| **Deletion** | 3 major issues | High - Loss of important information |
| **Update** | 4+ major issues | High - Data inconsistency risk |

## Root Cause

**All anomalies stem from the same problem:** Data redundancy caused by storing information about multiple entities (Student, Course, Instructor) in a single table (Enrollment).

## Solution

**Normalization:** Split the unnormalized table into separate tables:
1. **STUDENT** table - stores student information once
2. **COURSE** table - stores course information once
3. **INSTRUCTOR** table - stores instructor information once
4. **ENROLLMENT** table - stores only enrollment-specific information and foreign keys

This eliminates redundancy and prevents all three types of anomalies.
