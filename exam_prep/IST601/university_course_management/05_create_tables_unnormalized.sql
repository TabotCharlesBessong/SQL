-- ============================================
-- UNNORMALIZED DATABASE DESIGN
-- This file demonstrates what NOT to do
-- Used to identify anomalies before normalization
-- ============================================

-- Drop table if exists (for testing)
DROP TABLE IF EXISTS UnnormalizedEnrollment;

-- Create unnormalized table with all attributes combined
CREATE TABLE UnnormalizedEnrollment (
    EnrollmentID INT PRIMARY KEY,
    
    -- Student Information (repeated for each enrollment)
    StudentID VARCHAR(10),
    StudentName VARCHAR(100),
    StudentEmail VARCHAR(100),
    StudentPhone VARCHAR(20),
    StudentDOB DATE,
    StudentMajor VARCHAR(50),
    
    -- Course Information (repeated for each enrollment)
    CourseCode VARCHAR(10),
    CourseTitle VARCHAR(200),
    CourseCreditHours INT,
    CourseDepartment VARCHAR(50),
    CourseDescription TEXT,
    
    -- Instructor Information (repeated for each enrollment)
    InstructorID VARCHAR(10),
    InstructorName VARCHAR(100),
    InstructorEmail VARCHAR(100),
    InstructorPhone VARCHAR(20),
    InstructorDepartment VARCHAR(50),
    InstructorOfficeBuilding VARCHAR(50),
    InstructorOfficeRoom VARCHAR(20),
    
    -- Enrollment-specific Information
    Semester VARCHAR(20),
    Year INT,
    EnrollmentDate DATE,
    Grade VARCHAR(2) CHECK (Grade IN ('A', 'B', 'C', 'D', 'F') OR Grade IS NULL)
);

-- Create indexes for better query performance
CREATE INDEX idx_student_id ON UnnormalizedEnrollment(StudentID);
CREATE INDEX idx_course_code ON UnnormalizedEnrollment(CourseCode);
CREATE INDEX idx_instructor_id ON UnnormalizedEnrollment(InstructorID);
CREATE INDEX idx_semester_year ON UnnormalizedEnrollment(Semester, Year);

-- Display table structure
-- SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'UnnormalizedEnrollment';
