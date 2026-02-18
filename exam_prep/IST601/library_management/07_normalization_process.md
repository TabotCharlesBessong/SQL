# Normalization Process: Library Management (1NF to BCNF)

## Overview

This document analyzes the four tables from the relational schema (MEMBER, BOOK, STAFF, LOAN) and verifies each satisfies 1NF, 2NF, 3NF, and BCNF.

**Tables under analysis:**
- MEMBER (MemberID, MemberName, Email, Phone, DateOfBirth, Street, City, PostalCode, MembershipType, MembershipStartDate)
- BOOK (ISBN, Title, Author, Publisher, PublicationYear, Category, ShelfLocation, CopiesAvailable)
- STAFF (StaffID, StaffName, Email, Phone, Department, Position, HireDate)
- LOAN (LoanID, MemberID, ISBN, StaffID, LoanDate, DueDate, ReturnDate, FineAmount)

---

## FIRST NORMAL FORM (1NF)

**Definition:** Atomic values, unique attribute names, unique rows, order independence.

| Table   | Atomic | Unique attrs | Unique rows | Order indep | Result |
|---------|--------|--------------|-------------|-------------|--------|
| MEMBER  | ✅     | ✅           | ✅ (MemberID) | ✅          | 1NF   |
| BOOK    | ✅     | ✅           | ✅ (ISBN)     | ✅          | 1NF   |
| STAFF   | ✅     | ✅           | ✅ (StaffID)  | ✅          | 1NF   |
| LOAN    | ✅     | ✅           | ✅ (LoanID)   | ✅          | 1NF   |

**Conclusion:** All tables satisfy 1NF.

---

## SECOND NORMAL FORM (2NF)

**Definition:** In 1NF and no partial dependencies (non-key attributes fully depend on the primary key).

| Table   | PK            | Partial dependencies? | Result |
|---------|---------------|------------------------|--------|
| MEMBER  | MemberID      | None (simple key)      | ✅ 2NF |
| BOOK    | ISBN          | None (simple key)      | ✅ 2NF |
| STAFF   | StaffID       | None (simple key)      | ✅ 2NF |
| LOAN    | LoanID        | None; CK (MemberID, ISBN, LoanDate) has no partial deps | ✅ 2NF |

**Conclusion:** All tables satisfy 2NF.

---

## THIRD NORMAL FORM (3NF)

**Definition:** In 2NF and no transitive dependencies (no non-key attribute depends on another non-key attribute).

| Table   | Transitive dependencies? | Result |
|---------|---------------------------|--------|
| MEMBER  | None                      | ✅ 3NF |
| BOOK    | None                      | ✅ 3NF |
| STAFF   | None                      | ✅ 3NF |
| LOAN    | None                      | ✅ 3NF |

**Conclusion:** All tables satisfy 3NF.

---

## BOYCE-CODD NORMAL FORM (BCNF)

**Definition:** In 3NF and every determinant is a superkey.

| Table   | Determinants      | Superkeys? | Result |
|---------|-------------------|------------|--------|
| MEMBER  | MemberID          | ✅         | ✅ BCNF |
| BOOK    | ISBN              | ✅         | ✅ BCNF |
| STAFF   | StaffID           | ✅         | ✅ BCNF |
| LOAN    | LoanID; (MemberID, ISBN, LoanDate) | ✅ | ✅ BCNF |

**Conclusion:** All tables satisfy BCNF.

---

## Final Schema (BCNF)

```
MEMBER (MemberID, MemberName, Email, Phone, DateOfBirth, Street, City, PostalCode, MembershipType, MembershipStartDate)
PK: MemberID

BOOK (ISBN, Title, Author, Publisher, PublicationYear, Category, ShelfLocation, CopiesAvailable)
PK: ISBN

STAFF (StaffID, StaffName, Email, Phone, Department, Position, HireDate)
PK: StaffID

LOAN (LoanID, MemberID, ISBN, StaffID, LoanDate, DueDate, ReturnDate, FineAmount)
PK: LoanID
CK: (MemberID, ISBN, LoanDate)
FK: MemberID → MEMBER, ISBN → BOOK, StaffID → STAFF
```
