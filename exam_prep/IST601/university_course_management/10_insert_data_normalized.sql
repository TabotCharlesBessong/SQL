-- ============================================
-- INSERT DATA INTO NORMALIZED TABLES
-- Insert in order: Student, Instructor, Course, then Enrollment
-- ============================================

-- ============================================
-- 1. INSERT STUDENTS
-- ============================================
INSERT INTO Student (StudentID, StudentName, Email, Phone, DateOfBirth, Major) VALUES
('S001', 'John Smith', 'john.smith@university.edu', '555-0101', '2000-05-15', 'Computer Science'),
('S002', 'Emily Davis', 'emily.davis@university.edu', '555-0102', '2001-03-22', 'Mathematics'),
('S003', 'Michael Brown', 'michael.brown@university.edu', '555-0103', '1999-11-08', 'Physics'),
('S004', 'Sarah Wilson', 'sarah.wilson@university.edu', '555-0104', '2000-07-30', 'Computer Science'),
('S005', 'James Taylor', 'james.taylor@university.edu', '555-0105', '2001-01-12', 'Mathematics'),
('S006', 'Lisa Anderson', 'lisa.anderson@university.edu', '555-0106', '2000-09-05', 'Computer Science'),
('S007', 'Robert Thomas', 'robert.thomas@university.edu', '555-0107', '1999-12-18', 'Physics'),
('S008', 'Jennifer White', 'jennifer.white@university.edu', '555-0108', '2001-04-25', 'Computer Science');

-- ============================================
-- 2. INSERT INSTRUCTORS
-- ============================================
INSERT INTO Instructor (InstructorID, InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom) VALUES
('I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201'),
('I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305'),
('I003', 'Dr. Carol Martinez', 'carol.martinez@university.edu', '555-1003', 'Physics Department', 'Science Hall', 'SH-150'),
('I004', 'Dr. David Lee', 'david.lee@university.edu', '555-1004', 'CS Department', 'Science Hall', 'SH-205');

-- ============================================
-- 3. INSERT COURSES
-- ============================================
INSERT INTO Course (CourseCode, CourseTitle, CreditHours, Department, Description) VALUES
('CS101', 'Introduction to Programming', 3, 'CS Department', 'Basic programming concepts and syntax'),
('CS201', 'Data Structures', 3, 'CS Department', 'Arrays, linked lists, trees, and graphs'),
('CS301', 'Database Systems', 3, 'CS Department', 'Relational databases, SQL, and normalization'),
('MATH101', 'Calculus I', 4, 'Math Department', 'Differential and integral calculus'),
('MATH201', 'Linear Algebra', 3, 'Math Department', 'Vector spaces, matrices, and linear transformations'),
('PHYS101', 'Physics I', 4, 'Physics Department', 'Mechanics, waves, and thermodynamics');

-- ============================================
-- 4. INSERT ENROLLMENTS
-- ============================================
-- Note: EnrollmentID is auto-generated (SERIAL), so we don't include it in INSERT
INSERT INTO Enrollment (StudentID, CourseCode, InstructorID, Semester, Year, EnrollmentDate, Grade) VALUES
-- Student S001 enrollments
('S001', 'CS101', 'I001', 'Fall', 2024, '2024-08-15', 'A'),
('S001', 'MATH101', 'I002', 'Fall', 2024, '2024-08-16', 'B'),
('S001', 'CS201', 'I001', 'Spring', 2025, '2025-01-10', NULL),
('S001', 'PHYS101', 'I003', 'Spring', 2025, '2025-01-11', NULL),

-- Student S002 enrollments
('S002', 'MATH101', 'I002', 'Fall', 2024, '2024-08-20', 'A'),
('S002', 'MATH201', 'I002', 'Fall', 2024, '2024-08-20', 'A'),
('S002', 'CS101', 'I001', 'Spring', 2025, '2025-01-12', NULL),
('S002', 'CS201', 'I001', 'Spring', 2025, '2025-01-13', NULL),

-- Student S003 enrollments
('S003', 'PHYS101', 'I003', 'Fall', 2024, '2024-08-18', 'B'),
('S003', 'MATH101', 'I002', 'Fall', 2024, '2024-08-18', 'C'),
('S003', 'CS101', 'I001', 'Spring', 2025, '2025-01-15', NULL),
('S003', 'MATH201', 'I002', 'Spring', 2025, '2025-01-16', NULL),

-- Student S004 enrollments
('S004', 'CS101', 'I001', 'Fall', 2024, '2024-08-22', 'A'),
('S004', 'CS301', 'I004', 'Spring', 2025, '2025-01-18', NULL),
('S004', 'CS201', 'I001', 'Spring', 2025, '2025-01-19', NULL),
('S004', 'MATH101', 'I002', 'Spring', 2025, '2025-01-20', NULL),

-- Student S005 enrollments
('S005', 'MATH101', 'I002', 'Fall', 2024, '2024-08-25', 'B'),
('S005', 'MATH201', 'I002', 'Spring', 2025, '2025-01-20', NULL),
('S005', 'CS101', 'I001', 'Spring', 2025, '2025-01-21', NULL),

-- Student S006 enrollments
('S006', 'CS101', 'I001', 'Fall', 2024, '2024-08-28', 'A'),
('S006', 'CS201', 'I001', 'Spring', 2025, '2025-01-22', NULL),
('S006', 'CS301', 'I004', 'Spring', 2025, '2025-01-23', NULL),
('S006', 'MATH101', 'I002', 'Spring', 2025, '2025-01-24', NULL),

-- Student S007 enrollments
('S007', 'PHYS101', 'I003', 'Fall', 2024, '2024-09-01', 'A'),
('S007', 'MATH101', 'I002', 'Fall', 2024, '2024-09-01', 'B'),
('S007', 'CS101', 'I001', 'Spring', 2025, '2025-01-25', NULL),
('S007', 'PHYS101', 'I003', 'Spring', 2025, '2025-01-26', NULL),

-- Student S008 enrollments
('S008', 'CS101', 'I001', 'Spring', 2025, '2025-01-25', NULL),
('S008', 'CS301', 'I004', 'Spring', 2025, '2025-01-25', NULL),
('S008', 'MATH101', 'I002', 'Spring', 2025, '2025-01-26', NULL);

-- ============================================
-- VERIFY DATA INSERTION
-- ============================================
SELECT 'Students' AS TableName, COUNT(*) AS RecordCount FROM Student
UNION ALL
SELECT 'Instructors', COUNT(*) FROM Instructor
UNION ALL
SELECT 'Courses', COUNT(*) FROM Course
UNION ALL
SELECT 'Enrollments', COUNT(*) FROM Enrollment;

-- Display sample data
SELECT '=== STUDENTS ===' AS Info;
SELECT * FROM Student ORDER BY StudentID LIMIT 5;

SELECT '=== INSTRUCTORS ===' AS Info;
SELECT * FROM Instructor ORDER BY InstructorID;

SELECT '=== COURSES ===' AS Info;
SELECT * FROM Course ORDER BY CourseCode;

SELECT '=== ENROLLMENTS ===' AS Info;
SELECT * FROM Enrollment ORDER BY EnrollmentID LIMIT 15;

-- Show enrollment statistics
SELECT 
    '=== ENROLLMENT STATISTICS ===' AS Info,
    COUNT(*) AS TotalEnrollments,
    COUNT(DISTINCT StudentID) AS UniqueStudents,
    COUNT(DISTINCT CourseCode) AS UniqueCourses,
    COUNT(DISTINCT InstructorID) AS UniqueInstructors,
    COUNT(CASE WHEN Grade IS NOT NULL THEN 1 END) AS CompletedCourses,
    COUNT(CASE WHEN Grade IS NULL THEN 1 END) AS InProgressCourses
FROM Enrollment;
