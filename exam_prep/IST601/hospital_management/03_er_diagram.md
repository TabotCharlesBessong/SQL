# Entity-Relationship Diagram - Hospital Management

## Textual ER Diagram

```
PATIENT                    DOCTOR                    DEPARTMENT
┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│ PatientID PK │          │ DoctorID PK  │          │ DeptCode PK  │
│ PatientName  │          │ DoctorName   │          │ DeptName     │
│ DOB          │          │ Specialization│         │ Building     │
│ Gender       │          │ Phone         │          │ Floor        │
│ Phone        │          │ Email         │          │ HeadDocID FK │
│ Email        │          │ LicenseNum    │          └──────┬───────┘
│ Address...   │          │ DeptCode FK  │                 │
│ Emergency... │          └──────┬───────┘                 │
│ Insurance    │                 │                          │
└──────┬───────┘                 │                          │
       │                         │                          │
       │ (M)                     │ (M)                     │ (1)
       │                         │                          │
       │    has                  │ belongs to               │ has head
       │                         │                          │
       ▼                         ▼                          │
┌──────────────────┐    ┌──────────────────┐               │
│   APPOINTMENT    │    │   ADMISSION      │◄──────────────┘
├──────────────────┤    ├──────────────────┤
│ AppointmentID PK │    │ AdmissionID PK   │
│ PatientID FK     │    │ PatientID FK     │
│ DoctorID FK      │    │ DoctorID FK      │
│ ApptDate         │    │ DeptCode FK      │
│ ApptTime         │    │ RoomNumber       │
│ ApptType         │    │ AdmissionDate    │
│ Status           │    │ DischargeDate    │
│ Notes            │    │ Diagnosis        │
└──────────────────┘    └──────────────────┘

NURSE                    TREATMENT                  PRESCRIPTION
┌──────────────┐        ┌──────────────────┐      ┌──────────────────┐
│ NurseID PK   │        │ TreatmentID PK   │      │ PrescriptionID PK│
│ NurseName    │        │ PatientID FK     │      │ PatientID FK     │
│ CertLevel    │        │ DoctorID FK      │      │ DoctorID FK      │
│ Phone        │        │ TreatmentDate    │      │ MedicationCode FK│
│ Email        │        │ TreatmentType    │      │ PrescriptionDate  │
│ LicenseNum   │        │ Description      │      │ Dosage           │
│ DeptCode FK  │        │ Cost             │      │ Frequency        │
└──────┬───────┘        └──────────────────┘      │ Duration         │
       │                                            └──────────────────┘
       │ (M)
       │ assigned to
       │
       ▼
   DEPARTMENT

MEDICATION
┌──────────────┐
│ MedCode PK   │
│ MedName      │
│ Manufacturer │
│ DosageForm   │
│ UnitPrice    │
└──────┬───────┘
       │
       │ (M)
       │ prescribed in
       │
       ▼
   PRESCRIPTION
```

## Mermaid ER Diagram

```mermaid
erDiagram
    PATIENT ||--o{ APPOINTMENT : "has"
    DOCTOR ||--o{ APPOINTMENT : "sees"
    PATIENT ||--o{ ADMISSION : "has"
    DOCTOR ||--o{ ADMISSION : "admits"
    DEPARTMENT ||--o{ ADMISSION : "admits to"
    PATIENT ||--o{ TREATMENT : "receives"
    DOCTOR ||--o{ TREATMENT : "provides"
    PATIENT ||--o{ PRESCRIPTION : "receives"
    DOCTOR ||--o{ PRESCRIPTION : "prescribes"
    MEDICATION ||--o{ PRESCRIPTION : "prescribed in"
    DOCTOR }o--|| DEPARTMENT : "belongs to"
    NURSE }o--|| DEPARTMENT : "assigned to"
    DEPARTMENT ||--|| DOCTOR : "headed by"
    
    PATIENT {
        string PatientID PK
        string PatientName
        date DateOfBirth
        string Gender
        string Phone
        string Email
        string Street
        string City
        string PostalCode
        string EmergencyContactName
        string EmergencyContactPhone
        string InsuranceProvider
    }
    
    DOCTOR {
        string DoctorID PK
        string DoctorName
        string Specialization
        string Phone
        string Email
        string LicenseNumber
        string DepartmentCode FK
    }
    
    NURSE {
        string NurseID PK
        string NurseName
        string CertificationLevel
        string Phone
        string Email
        string LicenseNumber
        string DepartmentCode FK
    }
    
    DEPARTMENT {
        string DepartmentCode PK
        string DepartmentName
        string Building
        int Floor
        string HeadDoctorID FK
    }
    
    APPOINTMENT {
        int AppointmentID PK
        string PatientID FK
        string DoctorID FK
        date AppointmentDate
        time AppointmentTime
        string AppointmentType
        string Status
        text Notes
    }
    
    ADMISSION {
        int AdmissionID PK
        string PatientID FK
        string DoctorID FK
        string DepartmentCode FK
        string RoomNumber
        date AdmissionDate
        date DischargeDate
        text Diagnosis
    }
    
    TREATMENT {
        int TreatmentID PK
        string PatientID FK
        string DoctorID FK
        date TreatmentDate
        string TreatmentType
        text Description
        decimal Cost
    }
    
    MEDICATION {
        string MedicationCode PK
        string MedicationName
        string Manufacturer
        string DosageForm
        decimal UnitPrice
    }
    
    PRESCRIPTION {
        int PrescriptionID PK
        string PatientID FK
        string DoctorID FK
        string MedicationCode FK
        date PrescriptionDate
        string Dosage
        string Frequency
        int Duration
    }
```

## PlantUML ER Diagram

```plantuml
@startuml Hospital Management ER Diagram

skinparam linetype ortho
skinparam roundcorner 10
skinparam shadowing false

entity "PATIENT" as patient {
  * **PatientID** <<PK>> : VARCHAR(10)
  --
  PatientName : VARCHAR(100)
  DateOfBirth : DATE
  Gender : VARCHAR(10)
  Phone : VARCHAR(20)
  Email : VARCHAR(100)
  Street : VARCHAR(100)
  City : VARCHAR(50)
  PostalCode : VARCHAR(20)
  EmergencyContactName : VARCHAR(100)
  EmergencyContactPhone : VARCHAR(20)
  InsuranceProvider : VARCHAR(50)
}

entity "DOCTOR" as doctor {
  * **DoctorID** <<PK>> : VARCHAR(10)
  --
  DoctorName : VARCHAR(100)
  Specialization : VARCHAR(50)
  Phone : VARCHAR(20)
  Email : VARCHAR(100)
  LicenseNumber : VARCHAR(20)
  * DepartmentCode <<FK>> : VARCHAR(10)
}

entity "NURSE" as nurse {
  * **NurseID** <<PK>> : VARCHAR(10)
  --
  NurseName : VARCHAR(100)
  CertificationLevel : VARCHAR(20)
  Phone : VARCHAR(20)
  Email : VARCHAR(100)
  LicenseNumber : VARCHAR(20)
  * DepartmentCode <<FK>> : VARCHAR(10)
}

entity "DEPARTMENT" as dept {
  * **DepartmentCode** <<PK>> : VARCHAR(10)
  --
  DepartmentName : VARCHAR(50)
  Building : VARCHAR(50)
  Floor : INT
  * HeadDoctorID <<FK>> : VARCHAR(10)
}

entity "APPOINTMENT" as appointment {
  * **AppointmentID** <<PK>> : INT
  --
  * PatientID <<FK>> : VARCHAR(10)
  * DoctorID <<FK>> : VARCHAR(10)
  AppointmentDate : DATE
  AppointmentTime : TIME
  AppointmentType : VARCHAR(50)
  Status : VARCHAR(20)
  Notes : TEXT
}

entity "ADMISSION" as admission {
  * **AdmissionID** <<PK>> : INT
  --
  * PatientID <<FK>> : VARCHAR(10)
  * DoctorID <<FK>> : VARCHAR(10)
  * DepartmentCode <<FK>> : VARCHAR(10)
  RoomNumber : VARCHAR(20)
  AdmissionDate : DATE
  DischargeDate : DATE
  Diagnosis : TEXT
}

entity "TREATMENT" as treatment {
  * **TreatmentID** <<PK>> : INT
  --
  * PatientID <<FK>> : VARCHAR(10)
  * DoctorID <<FK>> : VARCHAR(10)
  TreatmentDate : DATE
  TreatmentType : VARCHAR(50)
  Description : TEXT
  Cost : DECIMAL
}

entity "MEDICATION" as medication {
  * **MedicationCode** <<PK>> : VARCHAR(20)
  --
  MedicationName : VARCHAR(100)
  Manufacturer : VARCHAR(100)
  DosageForm : VARCHAR(50)
  UnitPrice : DECIMAL
}

entity "PRESCRIPTION" as prescription {
  * **PrescriptionID** <<PK>> : INT
  --
  * PatientID <<FK>> : VARCHAR(10)
  * DoctorID <<FK>> : VARCHAR(10)
  * MedicationCode <<FK>> : VARCHAR(20)
  PrescriptionDate : DATE
  Dosage : VARCHAR(50)
  Frequency : VARCHAR(50)
  Duration : INT
}

patient ||--o{ appointment : "has"
doctor ||--o{ appointment : "sees"
patient ||--o{ admission : "has"
doctor ||--o{ admission : "admits"
dept ||--o{ admission : "admits to"
patient ||--o{ treatment : "receives"
doctor ||--o{ treatment : "provides"
patient ||--o{ prescription : "receives"
doctor ||--o{ prescription : "prescribes"
medication ||--o{ prescription : "prescribed in"
doctor }o--|| dept : "belongs to"
nurse }o--|| dept : "assigned to"
dept ||--|| doctor : "headed by"

@enduml
```
