# Library Management System - Scenario

## Story

City Public Library needs a database system to manage its collection, members, loans, and staff.

**Members:**
- Each member has a unique Member ID, full name, email address, phone number, date of birth, address (street, city, postal code), membership type (Standard, Premium, Student), and membership start date.
- Members can borrow multiple books.

**Books:**
- Each book has a unique ISBN, title, author(s), publisher, publication year, category (Fiction, Non-Fiction, Reference, etc.), shelf location, and number of copies available.
- Books can be borrowed by multiple members over time.

**Staff:**
- Each staff member has a unique Staff ID, full name, email address, phone number, department (Circulation, Reference, Technical Services), position (Librarian, Assistant, Technician), and hire date.
- Staff process loan and return transactions.

**Loans:**
- When a member borrows a book, the system records:
  - The member's information
  - The book information
  - The staff member who processed the loan
  - Loan date
  - Due date
  - Return date (NULL if not yet returned)
  - Fine amount (if late, 0 otherwise)

**Business rules:**
- A member can have multiple active and past loans
- A book can be loaned to multiple members over time (one at a time per copy)
- Each loan is processed by exactly one staff member
- Standard members can borrow up to 5 books; Premium up to 10; Student up to 3
