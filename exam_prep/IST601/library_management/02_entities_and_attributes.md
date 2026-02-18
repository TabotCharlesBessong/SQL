# Entity Identification and Attributes

## Entities Identified

### 1. MEMBER
**Attributes:**
- MemberID (PK)
- MemberName
- Email
- Phone
- DateOfBirth
- Street
- City
- PostalCode
- MembershipType (Standard, Premium, Student)
- MembershipStartDate

### 2. BOOK
**Attributes:**
- ISBN (PK)
- Title
- Author
- Publisher
- PublicationYear
- Category
- ShelfLocation
- CopiesAvailable

### 3. STAFF
**Attributes:**
- StaffID (PK)
- StaffName
- Email
- Phone
- Department
- Position
- HireDate

### 4. LOAN
**Attributes:**
- LoanID (PK)
- MemberID (FK)
- ISBN (FK)
- StaffID (FK)
- LoanDate
- DueDate
- ReturnDate
- FineAmount

## Relationships

1. **MEMBER - LOAN:** 1:M (one member, many loans)
2. **BOOK - LOAN:** 1:M (one book, many loan records)
3. **STAFF - LOAN:** 1:M (one staff processes many loans)

**Note:** Loan is a junction/associative entity. Staff assignment is per loan (who processed each transaction), not per book or member permanently.
