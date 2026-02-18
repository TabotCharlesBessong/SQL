# Entity-Relationship Diagram - Library Management

## Textual ER Diagram

```
MEMBER                    BOOK                      STAFF
┌──────────────┐        ┌──────────────┐          ┌──────────────┐
│ MemberID PK  │        │ ISBN PK      │          │ StaffID PK   │
│ MemberName   │        │ Title        │          │ StaffName    │
│ Email        │        │ Author       │          │ Email        │
│ Phone        │        │ Publisher    │          │ Phone        │
│ DateOfBirth  │        │ PubYear      │          │ Department   │
│ Street       │        │ Category     │          │ Position     │
│ City         │        │ ShelfLocation│          │ HireDate     │
│ PostalCode   │        │ CopiesAvail  │          └──────┬───────┘
│ MemberType   │        └──────┬───────┘                 │
│ MemberStart  │               │                         │
└──────┬───────┘               │                         │
       │                       │                         │
       │ (1)                   │ (M)                     │ (1)
       │                       │                         │
       │    borrows            │         processes       │
       └───────────────────────┼─────────────────────────┘
                               │
                               ▼
                    ┌──────────────────┐
                    │      LOAN        │
                    ├──────────────────┤
                    │ LoanID PK        │
                    │ MemberID FK      │
                    │ ISBN FK          │
                    │ StaffID FK       │
                    │ LoanDate         │
                    │ DueDate          │
                    │ ReturnDate       │
                    │ FineAmount       │
                    └──────────────────┘
```

## Mermaid ER Diagram

```mermaid
erDiagram
    MEMBER ||--o{ LOAN : "borrows"
    BOOK ||--o{ LOAN : "has loans"
    STAFF ||--o{ LOAN : "processes"
    
    MEMBER {
        string MemberID PK
        string MemberName
        string Email
        string Phone
        date DateOfBirth
        string Street
        string City
        string PostalCode
        string MembershipType
        date MembershipStartDate
    }
    
    BOOK {
        string ISBN PK
        string Title
        string Author
        string Publisher
        int PublicationYear
        string Category
        string ShelfLocation
        int CopiesAvailable
    }
    
    STAFF {
        string StaffID PK
        string StaffName
        string Email
        string Phone
        string Department
        string Position
        date HireDate
    }
    
    LOAN {
        int LoanID PK
        string MemberID FK
        string ISBN FK
        string StaffID FK
        date LoanDate
        date DueDate
        date ReturnDate
        decimal FineAmount
    }
```

## PlantUML ER Diagram

```plantuml
@startuml Library Management ER Diagram

skinparam linetype ortho
skinparam roundcorner 10
skinparam shadowing false

entity "MEMBER" as member {
  * **MemberID** <<PK>> : VARCHAR(10)
  --
  MemberName : VARCHAR(100)
  Email : VARCHAR(100)
  Phone : VARCHAR(20)
  DateOfBirth : DATE
  Street : VARCHAR(100)
  City : VARCHAR(50)
  PostalCode : VARCHAR(20)
  MembershipType : VARCHAR(20)
  MembershipStartDate : DATE
}

entity "LOAN" as loan {
  * **LoanID** <<PK>> : INT
  --
  * MemberID <<FK>> : VARCHAR(10)
  * ISBN <<FK>> : VARCHAR(20)
  * StaffID <<FK>> : VARCHAR(10)
  LoanDate : DATE
  DueDate : DATE
  ReturnDate : DATE
  FineAmount : DECIMAL
}

entity "BOOK" as book {
  * **ISBN** <<PK>> : VARCHAR(20)
  --
  Title : VARCHAR(200)
  Author : VARCHAR(100)
  Publisher : VARCHAR(100)
  PublicationYear : INT
  Category : VARCHAR(50)
  ShelfLocation : VARCHAR(50)
  CopiesAvailable : INT
}

entity "STAFF" as staff {
  * **StaffID** <<PK>> : VARCHAR(10)
  --
  StaffName : VARCHAR(100)
  Email : VARCHAR(100)
  Phone : VARCHAR(20)
  Department : VARCHAR(50)
  Position : VARCHAR(50)
  HireDate : DATE
}

member ||--o{ loan : "borrows"
book ||--o{ loan : "has loans"
staff ||--o{ loan : "processes"

@enduml
```
