# Relational Schema - Library Management

## Normalized Schema (BCNF)

### MEMBER (MemberID, MemberName, Email, Phone, DateOfBirth, Street, City, PostalCode, MembershipType, MembershipStartDate)
- **Primary Key:** MemberID
- **Constraints:** Email unique, MembershipType IN (Standard, Premium, Student)

### BOOK (ISBN, Title, Author, Publisher, PublicationYear, Category, ShelfLocation, CopiesAvailable)
- **Primary Key:** ISBN
- **Constraints:** PublicationYear > 0, CopiesAvailable >= 0

### STAFF (StaffID, StaffName, Email, Phone, Department, Position, HireDate)
- **Primary Key:** StaffID
- **Constraints:** Email unique

### LOAN (LoanID, MemberID, ISBN, StaffID, LoanDate, DueDate, ReturnDate, FineAmount)
- **Primary Key:** LoanID
- **Foreign Keys:** MemberID → MEMBER, ISBN → BOOK, StaffID → STAFF
- **Constraints:** (MemberID, ISBN, LoanDate) unique, FineAmount >= 0

## Functional Dependencies

| Table | FDs |
|-------|-----|
| MEMBER | MemberID → MemberName, Email, Phone, DateOfBirth, Street, City, PostalCode, MembershipType, MembershipStartDate |
| BOOK | ISBN → Title, Author, Publisher, PublicationYear, Category, ShelfLocation, CopiesAvailable |
| STAFF | StaffID → StaffName, Email, Phone, Department, Position, HireDate |
| LOAN | LoanID → MemberID, ISBN, StaffID, LoanDate, DueDate, ReturnDate, FineAmount |
| LOAN | (MemberID, ISBN, LoanDate) → LoanID, StaffID, DueDate, ReturnDate, FineAmount |
