-- ============================================
-- INSERT DATA INTO UNNORMALIZED TABLE
-- This data will demonstrate normalization anomalies
-- ============================================

-- Insert enrollment records
-- Notice the redundancy: student, course, and instructor info repeated

INSERT INTO UnnormalizedEnrollment VALUES
-- Student S001 (John Smith) enrollments
(1, 'S001', 'John Smith', 'john.smith@university.edu', '555-0101', '2000-05-15', 'Computer Science',
 'CS101', 'Introduction to Programming', 3, 'CS Department', 'Basic programming concepts and syntax',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Fall', 2024, '2024-08-15', 'A'),

(2, 'S001', 'John Smith', 'john.smith@university.edu', '555-0101', '2000-05-15', 'Computer Science',
 'MATH101', 'Calculus I', 4, 'Math Department', 'Differential and integral calculus',
 'I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305',
 'Fall', 2024, '2024-08-16', 'B'),

(3, 'S001', 'John Smith', 'john.smith@university.edu', '555-0101', '2000-05-15', 'Computer Science',
 'CS201', 'Data Structures', 3, 'CS Department', 'Arrays, linked lists, trees, and graphs',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Spring', 2025, '2025-01-10', NULL),

-- Student S002 (Emily Davis) enrollments
(4, 'S002', 'Emily Davis', 'emily.davis@university.edu', '555-0102', '2001-03-22', 'Mathematics',
 'MATH101', 'Calculus I', 4, 'Math Department', 'Differential and integral calculus',
 'I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305',
 'Fall', 2024, '2024-08-20', 'A'),

(5, 'S002', 'Emily Davis', 'emily.davis@university.edu', '555-0102', '2001-03-22', 'Mathematics',
 'MATH201', 'Linear Algebra', 3, 'Math Department', 'Vector spaces, matrices, and linear transformations',
 'I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305',
 'Fall', 2024, '2024-08-20', 'A'),

(6, 'S002', 'Emily Davis', 'emily.davis@university.edu', '555-0102', '2001-03-22', 'Mathematics',
 'CS101', 'Introduction to Programming', 3, 'CS Department', 'Basic programming concepts and syntax',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Spring', 2025, '2025-01-12', NULL),

-- Student S003 (Michael Brown) enrollments
(7, 'S003', 'Michael Brown', 'michael.brown@university.edu', '555-0103', '1999-11-08', 'Physics',
 'PHYS101', 'Physics I', 4, 'Physics Department', 'Mechanics, waves, and thermodynamics',
 'I003', 'Dr. Carol Martinez', 'carol.martinez@university.edu', '555-1003', 'Physics Department', 'Science Hall', 'SH-150',
 'Fall', 2024, '2024-08-18', 'B'),

(8, 'S003', 'Michael Brown', 'michael.brown@university.edu', '555-0103', '1999-11-08', 'Physics',
 'MATH101', 'Calculus I', 4, 'Math Department', 'Differential and integral calculus',
 'I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305',
 'Fall', 2024, '2024-08-18', 'C'),

(9, 'S003', 'Michael Brown', 'michael.brown@university.edu', '555-0103', '1999-11-08', 'Physics',
 'CS101', 'Introduction to Programming', 3, 'CS Department', 'Basic programming concepts and syntax',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Spring', 2025, '2025-01-15', NULL),

-- Student S004 (Sarah Wilson) enrollments
(10, 'S004', 'Sarah Wilson', 'sarah.wilson@university.edu', '555-0104', '2000-07-30', 'Computer Science',
 'CS101', 'Introduction to Programming', 3, 'CS Department', 'Basic programming concepts and syntax',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Fall', 2024, '2024-08-22', 'A'),

(11, 'S004', 'Sarah Wilson', 'sarah.wilson@university.edu', '555-0104', '2000-07-30', 'Computer Science',
 'CS301', 'Database Systems', 3, 'CS Department', 'Relational databases, SQL, and normalization',
 'I004', 'Dr. David Lee', 'david.lee@university.edu', '555-1004', 'CS Department', 'Science Hall', 'SH-205',
 'Spring', 2025, '2025-01-18', NULL),

-- Student S005 (James Taylor) enrollments
(12, 'S005', 'James Taylor', 'james.taylor@university.edu', '555-0105', '2001-01-12', 'Mathematics',
 'MATH101', 'Calculus I', 4, 'Math Department', 'Differential and integral calculus',
 'I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305',
 'Fall', 2024, '2024-08-25', 'B'),

(13, 'S005', 'James Taylor', 'james.taylor@university.edu', '555-0105', '2001-01-12', 'Mathematics',
 'MATH201', 'Linear Algebra', 3, 'Math Department', 'Vector spaces, matrices, and linear transformations',
 'I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305',
 'Spring', 2025, '2025-01-20', NULL),

-- Student S006 (Lisa Anderson) enrollments
(14, 'S006', 'Lisa Anderson', 'lisa.anderson@university.edu', '555-0106', '2000-09-05', 'Computer Science',
 'CS101', 'Introduction to Programming', 3, 'CS Department', 'Basic programming concepts and syntax',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Fall', 2024, '2024-08-28', 'A'),

(15, 'S006', 'Lisa Anderson', 'lisa.anderson@university.edu', '555-0106', '2000-09-05', 'Computer Science',
 'CS201', 'Data Structures', 3, 'CS Department', 'Arrays, linked lists, trees, and graphs',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Spring', 2025, '2025-01-22', NULL),

-- Student S007 (Robert Thomas) enrollments
(16, 'S007', 'Robert Thomas', 'robert.thomas@university.edu', '555-0107', '1999-12-18', 'Physics',
 'PHYS101', 'Physics I', 4, 'Physics Department', 'Mechanics, waves, and thermodynamics',
 'I003', 'Dr. Carol Martinez', 'carol.martinez@university.edu', '555-1003', 'Physics Department', 'Science Hall', 'SH-150',
 'Fall', 2024, '2024-09-01', 'A'),

(17, 'S007', 'Robert Thomas', 'robert.thomas@university.edu', '555-0107', '1999-12-18', 'Physics',
 'MATH101', 'Calculus I', 4, 'Math Department', 'Differential and integral calculus',
 'I002', 'Dr. Bob Williams', 'bob.williams@university.edu', '555-1002', 'Math Department', 'Math Building', 'MB-305',
 'Fall', 2024, '2024-09-01', 'B'),

-- Student S008 (Jennifer White) enrollments
(18, 'S008', 'Jennifer White', 'jennifer.white@university.edu', '555-0108', '2001-04-25', 'Computer Science',
 'CS101', 'Introduction to Programming', 3, 'CS Department', 'Basic programming concepts and syntax',
 'I001', 'Dr. Alice Johnson', 'alice.johnson@university.edu', '555-1001', 'CS Department', 'Science Hall', 'SH-201',
 'Spring', 2025, '2025-01-25', NULL),

(19, 'S008', 'Jennifer White', 'jennifer.white@university.edu', '555-0108', '2001-04-25', 'Computer Science',
 'CS301', 'Database Systems', 3, 'CS Department', 'Relational databases, SQL, and normalization',
 'I004', 'Dr. David Lee', 'david.lee@university.edu', '555-1004', 'CS Department', 'Science Hall', 'SH-205',
 'Spring', 2025, '2025-01-25', NULL);

-- Verify data insertion
SELECT COUNT(*) AS TotalRecords FROM UnnormalizedEnrollment;
SELECT DISTINCT StudentID, StudentName FROM UnnormalizedEnrollment ORDER BY StudentID;
SELECT DISTINCT CourseCode, CourseTitle FROM UnnormalizedEnrollment ORDER BY CourseCode;
SELECT DISTINCT InstructorID, InstructorName FROM UnnormalizedEnrollment ORDER BY InstructorID;
