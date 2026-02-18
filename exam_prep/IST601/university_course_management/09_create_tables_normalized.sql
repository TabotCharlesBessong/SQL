-- ============================================
-- NORMALIZED DATABASE DESIGN (BCNF)
-- This is the correct, normalized design
-- Compatible with PostgreSQL (uses SERIAL for auto-increment)
-- For MySQL/MariaDB, change SERIAL to AUTO_INCREMENT
-- For SQL Server, use IDENTITY(1,1)
-- ============================================

-- Drop tables if they exist (in reverse order of dependencies)
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Instructor;

-- ============================================
-- 1. STUDENT TABLE
-- ============================================
CREATE TABLE Student (
    StudentID VARCHAR(10) PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    DateOfBirth DATE,
    Major VARCHAR(50) NOT NULL,
    
    -- Constraints
    CONSTRAINT chk_student_email CHECK (Email LIKE '%@%.%'),
    CONSTRAINT chk_student_dob CHECK (DateOfBirth < CURRENT_DATE)
);

-- ============================================
-- 2. INSTRUCTOR TABLE
-- ============================================
CREATE TABLE Instructor (
    InstructorID VARCHAR(10) PRIMARY KEY,
    InstructorName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Department VARCHAR(50) NOT NULL,
    OfficeBuilding VARCHAR(50),
    OfficeRoom VARCHAR(20),
    
    -- Constraints
    CONSTRAINT chk_instructor_email CHECK (Email LIKE '%@%.%')
);

-- ============================================
-- 3. COURSE TABLE
-- ============================================
-- Note: Course does NOT have InstructorID foreign key.
-- Instructor assignment is per enrollment (per semester),
-- not per course permanently. This allows the same course
-- to be taught by different instructors in different semesters.
CREATE TABLE Course (
    CourseCode VARCHAR(10) PRIMARY KEY,
    CourseTitle VARCHAR(200) NOT NULL,
    CreditHours INT NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Description TEXT,
    
    -- Constraints
    CONSTRAINT chk_credit_hours CHECK (CreditHours > 0 AND CreditHours <= 6)
);

-- ============================================
-- 4. ENROLLMENT TABLE
-- ============================================
-- Note: InstructorID is included here (not in Course table) because:
-- - Instructor assignment is per enrollment (per semester), not per course permanently
-- - The same course can be taught by different instructors in different semesters
-- - Example: CS101 taught by Dr. Johnson in Fall 2024, Dr. Lee in Spring 2025
CREATE TABLE Enrollment (
    EnrollmentID SERIAL PRIMARY KEY,
    StudentID VARCHAR(10) NOT NULL,
    CourseCode VARCHAR(10) NOT NULL,
    InstructorID VARCHAR(10) NOT NULL,  -- Instructor assigned per enrollment/semester
    Semester VARCHAR(20) NOT NULL,
    Year INT NOT NULL,
    EnrollmentDate DATE NOT NULL,
    Grade VARCHAR(2) CHECK (Grade IN ('A', 'B', 'C', 'D', 'F') OR Grade IS NULL),
    
    -- Foreign Keys
    CONSTRAINT fk_enrollment_student 
        FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_enrollment_course 
        FOREIGN KEY (CourseCode) REFERENCES Course(CourseCode)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_enrollment_instructor 
        FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    
    -- Constraints
    CONSTRAINT chk_semester CHECK (Semester IN ('Fall', 'Spring', 'Summer')),
    CONSTRAINT chk_year CHECK (Year >= 2000 AND Year <= 2100),
    
    -- Unique constraint: prevent duplicate enrollments
    CONSTRAINT uk_enrollment_unique 
        UNIQUE (StudentID, CourseCode, Semester, Year)
);

-- ============================================
-- CREATE INDEXES FOR BETTER PERFORMANCE
-- ============================================
CREATE INDEX idx_enrollment_student ON Enrollment(StudentID);
CREATE INDEX idx_enrollment_course ON Enrollment(CourseCode);
CREATE INDEX idx_enrollment_instructor ON Enrollment(InstructorID);
CREATE INDEX idx_enrollment_semester_year ON Enrollment(Semester, Year);
CREATE INDEX idx_student_major ON Student(Major);
CREATE INDEX idx_course_department ON Course(Department);
CREATE INDEX idx_instructor_department ON Instructor(Department);

-- ============================================
-- VERIFY TABLE CREATION
-- ============================================
-- Uncomment to verify:
-- SHOW TABLES;
-- DESCRIBE Student;
-- DESCRIBE Instructor;
-- DESCRIBE Course;
-- DESCRIBE Enrollment;
