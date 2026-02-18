-- ============================================
-- INSERT DATA - Library Management
-- ============================================

-- 1. MEMBERS
INSERT INTO Member VALUES
('M001', 'Alice Johnson', 'alice.j@email.com', '555-1001', '1990-03-15', '123 Oak St', 'Springfield', '12345', 'Premium', '2023-01-10'),
('M002', 'Bob Smith', 'bob.s@email.com', '555-1002', '1985-07-22', '456 Elm Ave', 'Springfield', '12346', 'Standard', '2024-02-01'),
('M003', 'Carol Davis', 'carol.d@email.com', '555-1003', '2000-11-08', '789 Pine Rd', 'Riverside', '23456', 'Student', '2024-08-15'),
('M004', 'David Wilson', 'david.w@email.com', '555-1004', '1978-05-30', '321 Maple Dr', 'Springfield', '12347', 'Standard', '2022-06-20'),
('M005', 'Eve Martinez', 'eve.m@email.com', '555-1005', '1995-09-12', '654 Cedar Ln', 'Riverside', '23457', 'Premium', '2023-11-01'),
('M006', 'Frank Brown', 'frank.b@email.com', '555-1006', '1988-12-03', '987 Birch Blvd', 'Springfield', '12348', 'Student', '2024-09-01');

-- 2. BOOKS
INSERT INTO Book VALUES
('978-0132350884', 'Clean Code', 'Robert Martin', 'Prentice Hall', 2008, 'Technology', 'A-101', 3),
('978-0201633610', 'Design Patterns', 'Gang of Four', 'Addison-Wesley', 1994, 'Technology', 'A-102', 2),
('978-0596517748', 'JavaScript: The Good Parts', 'Douglas Crockford', 'O''Reilly', 2008, 'Technology', 'A-103', 4),
('978-0141439518', 'Pride and Prejudice', 'Jane Austen', 'Penguin', 1813, 'Fiction', 'B-201', 5),
('978-0061120084', 'To Kill a Mockingbird', 'Harper Lee', 'HarperCollins', 1960, 'Fiction', 'B-202', 3),
('978-0385333481', 'The Firm', 'John Grisham', 'Doubleday', 1991, 'Fiction', 'B-203', 2),
('978-0307887436', 'Zero to One', 'Peter Thiel', 'Crown', 2014, 'Business', 'C-301', 4);

-- 3. STAFF
INSERT INTO Staff VALUES
('S001', 'Grace Lee', 'grace.l@library.gov', '555-2001', 'Circulation', 'Librarian', '2020-01-15'),
('S002', 'Henry Clark', 'henry.c@library.gov', '555-2002', 'Circulation', 'Assistant', '2022-06-01'),
('S003', 'Ivy Turner', 'ivy.t@library.gov', '555-2003', 'Reference', 'Librarian', '2019-03-10');

-- 4. LOANS (LoanID auto-generated via SERIAL)
INSERT INTO Loan (MemberID, ISBN, StaffID, LoanDate, DueDate, ReturnDate, FineAmount) VALUES
('M001', '978-0132350884', 'S001', '2024-10-01', '2024-10-15', '2024-10-14', 0),
('M001', '978-0201633610', 'S001', '2024-10-02', '2024-10-16', NULL, 0),
('M001', '978-0596517748', 'S001', '2024-10-05', '2024-10-19', '2024-10-18', 0),
('M002', '978-0141439518', 'S002', '2024-10-03', '2024-10-17', '2024-10-20', 1.50),
('M002', '978-0061120084', 'S002', '2024-10-08', '2024-10-22', NULL, 0),
('M003', '978-0132350884', 'S002', '2024-10-10', '2024-10-24', '2024-10-23', 0),
('M003', '978-0385333481', 'S001', '2024-10-12', '2024-10-26', NULL, 0),
('M004', '978-0307887436', 'S001', '2024-10-01', '2024-10-15', '2024-10-15', 0),
('M004', '978-0201633610', 'S002', '2024-10-15', '2024-10-29', NULL, 0),
('M005', '978-0141439518', 'S003', '2024-10-04', '2024-10-18', '2024-10-17', 0),
('M005', '978-0596517748', 'S003', '2024-10-06', '2024-10-20', '2024-10-19', 0),
('M005', '978-0061120084', 'S001', '2024-10-14', '2024-10-28', NULL, 0),
('M006', '978-0132350884', 'S002', '2024-10-16', '2024-10-30', NULL, 0);

-- Verify
SELECT 'Members' AS tbl, COUNT(*) AS cnt FROM Member
UNION ALL SELECT 'Books', COUNT(*) FROM Book
UNION ALL SELECT 'Staff', COUNT(*) FROM Staff
UNION ALL SELECT 'Loans', COUNT(*) FROM Loan;
