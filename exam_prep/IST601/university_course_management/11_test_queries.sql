-- ============================================
-- TEST QUERIES TO VERIFY NORMALIZATION BENEFITS
-- ============================================

-- ============================================
-- 1. TEST INSERTION - Can add entities independently
-- ============================================

-- Add a new student without enrollment (WORKS in normalized design)
INSERT INTO Student (StudentID, StudentName, Email, Phone, DateOfBirth, Major)
VALUES ('S009', 'New Student', 'new.student@university.edu', '555-0109', '2002-01-01', 'Computer Science');

-- Add a new course without enrollment (WORKS in normalized design)
INSERT INTO Course (CourseCode, CourseTitle, CreditHours, Department, Description)
VALUES ('CS401', 'Advanced Algorithms', 3, 'CS Department', 'Advanced algorithm design and analysis');

-- Add a new instructor without course assignment (WORKS in normalized design)
-- Note: Instructor assignment is per enrollment (per semester), not per course permanently,
-- so instructors can be added without immediate course assignments
INSERT INTO Instructor (InstructorID, InstructorName, Email, Phone, Department, OfficeBuilding, OfficeRoom)
VALUES ('I005', 'Dr. New Instructor', 'new.instructor@university.edu', '555-1005', 'Math Department', 'Math Building', 'MB-310');

-- ============================================
-- 2. TEST UPDATE - Update in one place
-- ============================================

-- Update student email (only one place to update)
UPDATE Student 
SET Email = 'john.smith.new@university.edu'
WHERE StudentID = 'S001';

-- Verify update propagated correctly
SELECT e.EnrollmentID, s.StudentID, s.StudentName, s.Email
FROM Enrollment e
JOIN Student s ON e.StudentID = s.StudentID
WHERE s.StudentID = 'S001';

-- Update course credit hours (only one place to update)
UPDATE Course 
SET CreditHours = 4
WHERE CourseCode = 'CS101';

-- Verify update
SELECT CourseCode, CourseTitle, CreditHours FROM Course WHERE CourseCode = 'CS101';

-- Update instructor department (only one place to update)
UPDATE Instructor 
SET Department = 'Computer Engineering Department'
WHERE InstructorID = 'I001';

-- Verify update
SELECT InstructorID, InstructorName, Department FROM Instructor WHERE InstructorID = 'I001';

-- ============================================
-- 3. TEST DELETION - No loss of related data
-- ============================================

-- Delete a student's enrollment (student info preserved)
DELETE FROM Enrollment WHERE StudentID = 'S008' AND CourseCode = 'CS101';

-- Verify student still exists
SELECT * FROM Student WHERE StudentID = 'S008';

-- Verify course still exists
SELECT * FROM Course WHERE CourseCode = 'CS101';

-- Verify instructor still exists
SELECT * FROM Instructor WHERE InstructorID = 'I001';

-- ============================================
-- 4. USEFUL QUERIES
-- ============================================

-- List all students with their enrollments
SELECT 
    s.StudentID,
    s.StudentName,
    s.Major,
    c.CourseCode,
    c.CourseTitle,
    e.Semester,
    e.Year,
    e.Grade
FROM Student s
LEFT JOIN Enrollment e ON s.StudentID = e.StudentID
LEFT JOIN Course c ON e.CourseCode = c.CourseCode
ORDER BY s.StudentID, e.Year, e.Semester;

-- List all courses with enrollment counts
SELECT 
    c.CourseCode,
    c.CourseTitle,
    c.CreditHours,
    COUNT(e.EnrollmentID) AS EnrollmentCount
FROM Course c
LEFT JOIN Enrollment e ON c.CourseCode = e.CourseCode
GROUP BY c.CourseCode, c.CourseTitle, c.CreditHours
ORDER BY EnrollmentCount DESC;

-- List instructors with their courses (through enrollments)
-- Note: Shows courses taught per semester, as instructor assignment is per enrollment
SELECT 
    i.InstructorID,
    i.InstructorName,
    i.Department,
    c.CourseCode,
    c.CourseTitle,
    e.Semester,
    e.Year,
    COUNT(DISTINCT e.StudentID) AS StudentCount
FROM Instructor i
LEFT JOIN Enrollment e ON i.InstructorID = e.InstructorID
LEFT JOIN Course c ON e.CourseCode = c.CourseCode
GROUP BY i.InstructorID, i.InstructorName, i.Department, c.CourseCode, c.CourseTitle, e.Semester, e.Year
ORDER BY i.InstructorID, e.Year, e.Semester, c.CourseCode;

-- Find students enrolled in multiple courses
SELECT 
    s.StudentID,
    s.StudentName,
    COUNT(e.EnrollmentID) AS CourseCount
FROM Student s
JOIN Enrollment e ON s.StudentID = e.StudentID
GROUP BY s.StudentID, s.StudentName
HAVING COUNT(e.EnrollmentID) > 1
ORDER BY CourseCount DESC;

-- Calculate GPA for each student
SELECT 
    s.StudentID,
    s.StudentName,
    AVG(CASE e.Grade
        WHEN 'A' THEN 4.0
        WHEN 'B' THEN 3.0
        WHEN 'C' THEN 2.0
        WHEN 'D' THEN 1.0
        WHEN 'F' THEN 0.0
        ELSE NULL
    END) AS GPA,
    COUNT(e.Grade) AS CoursesCompleted
FROM Student s
LEFT JOIN Enrollment e ON s.StudentID = e.StudentID AND e.Grade IS NOT NULL
GROUP BY s.StudentID, s.StudentName
HAVING COUNT(e.Grade) > 0
ORDER BY GPA DESC;
