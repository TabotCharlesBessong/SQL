-- ============================================
-- LIBRARY MANAGEMENT - NORMALIZED DATABASE (BCNF)
-- PostgreSQL compatible (SERIAL for auto-increment)
-- ============================================

DROP TABLE IF EXISTS Loan;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Staff;

-- ============================================
-- 1. MEMBER TABLE
-- ============================================
CREATE TABLE Member (
    MemberID VARCHAR(10) PRIMARY KEY,
    MemberName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    DateOfBirth DATE,
    Street VARCHAR(100),
    City VARCHAR(50),
    PostalCode VARCHAR(20),
    MembershipType VARCHAR(20) NOT NULL,
    MembershipStartDate DATE NOT NULL,
    CONSTRAINT chk_member_type CHECK (MembershipType IN ('Standard', 'Premium', 'Student'))
);

-- ============================================
-- 2. BOOK TABLE
-- ============================================
CREATE TABLE Book (
    ISBN VARCHAR(20) PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    Author VARCHAR(100) NOT NULL,
    Publisher VARCHAR(100),
    PublicationYear INT,
    Category VARCHAR(50),
    ShelfLocation VARCHAR(50),
    CopiesAvailable INT NOT NULL DEFAULT 0,
    CONSTRAINT chk_pub_year CHECK (PublicationYear IS NULL OR PublicationYear > 1800),
    CONSTRAINT chk_copies CHECK (CopiesAvailable >= 0)
);

-- ============================================
-- 3. STAFF TABLE
-- ============================================
CREATE TABLE Staff (
    StaffID VARCHAR(10) PRIMARY KEY,
    StaffName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Department VARCHAR(50) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    HireDate DATE NOT NULL
);

-- ============================================
-- 4. LOAN TABLE
-- ============================================
CREATE TABLE Loan (
    LoanID SERIAL PRIMARY KEY,
    MemberID VARCHAR(10) NOT NULL,
    ISBN VARCHAR(20) NOT NULL,
    StaffID VARCHAR(10) NOT NULL,
    LoanDate DATE NOT NULL,
    DueDate DATE NOT NULL,
    ReturnDate DATE,
    FineAmount DECIMAL(10,2) DEFAULT 0 CHECK (FineAmount >= 0),
    
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT uk_loan_unique UNIQUE (MemberID, ISBN, LoanDate)
);

CREATE INDEX idx_loan_member ON Loan(MemberID);
CREATE INDEX idx_loan_book ON Loan(ISBN);
CREATE INDEX idx_loan_staff ON Loan(StaffID);
CREATE INDEX idx_loan_dates ON Loan(LoanDate, ReturnDate);
