# Relational Schema - Hospital Management

## Overview

The relational schema formalizes the relationships discovered in the ER diagram phase. Foreign keys are added to junction tables and related entities to establish referential integrity.

## Normalized Schema (BCNF)

### PATIENT (PatientID, PatientName, DateOfBirth, Gender, Phone, Email, Street, City, PostalCode, EmergencyContactName, EmergencyContactPhone, InsuranceProvider)
- **Primary Key:** PatientID

### DOCTOR (DoctorID, DoctorName, Specialization, Phone, Email, LicenseNumber, DepartmentCode)
- **Primary Key:** DoctorID
- **Foreign Key:** DepartmentCode → DEPARTMENT(DepartmentCode)

### NURSE (NurseID, NurseName, CertificationLevel, Phone, Email, LicenseNumber, DepartmentCode)
- **Primary Key:** NurseID
- **Foreign Key:** DepartmentCode → DEPARTMENT(DepartmentCode)

### DEPARTMENT (DepartmentCode, DepartmentName, Building, Floor, HeadDoctorID)
- **Primary Key:** DepartmentCode
- **Foreign Key:** HeadDoctorID → DOCTOR(DoctorID)

### APPOINTMENT (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentType, Status, Notes)
- **Primary Key:** AppointmentID
- **Foreign Keys:** PatientID → PATIENT, DoctorID → DOCTOR
- **Unique:** (PatientID, DoctorID, AppointmentDate, AppointmentTime)

### ADMISSION (AdmissionID, PatientID, DoctorID, DepartmentCode, RoomNumber, AdmissionDate, DischargeDate, Diagnosis)
- **Primary Key:** AdmissionID
- **Foreign Keys:** PatientID → PATIENT, DoctorID → DOCTOR, DepartmentCode → DEPARTMENT
- **Unique:** (PatientID, RoomNumber, AdmissionDate) - assuming one patient per room at a time

### TREATMENT (TreatmentID, PatientID, DoctorID, MedicationCode, TreatmentDate, TreatmentType, Description, Cost)
- **Primary Key:** TreatmentID
- **Foreign Keys:** PatientID → PATIENT, DoctorID → DOCTOR, MedicationCode → MEDICATION (optional - for treatments involving medication)
- **Note:** MedicationCode is optional - not all treatments involve medication (e.g., surgery, therapy)

### MEDICATION (MedicationCode, MedicationName, Manufacturer, DosageForm, UnitPrice)
- **Primary Key:** MedicationCode

### PRESCRIPTION (PrescriptionID, PatientID, DoctorID, MedicationCode, TreatmentID, PrescriptionDate, Dosage, Frequency, Duration)
- **Primary Key:** PrescriptionID
- **Foreign Keys:** PatientID → PATIENT, DoctorID → DOCTOR, MedicationCode → MEDICATION, TreatmentID → TREATMENT (optional - prescription may result from a treatment)
- **Unique:** (PatientID, DoctorID, MedicationCode, PrescriptionDate)
- **Note:** TreatmentID is optional - prescriptions can be standalone or result from a treatment

## Functional Dependencies

| Table | Functional Dependencies |
|-------|-------------------------|
| PATIENT | PatientID → All attributes |
| DOCTOR | DoctorID → DoctorName, Specialization, Phone, Email, LicenseNumber, DepartmentCode |
| NURSE | NurseID → NurseName, CertificationLevel, Phone, Email, LicenseNumber, DepartmentCode |
| DEPARTMENT | DepartmentCode → DepartmentName, Building, Floor, HeadDoctorID |
| APPOINTMENT | AppointmentID → PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentType, Status, Notes |
| ADMISSION | AdmissionID → PatientID, DoctorID, DepartmentCode, RoomNumber, AdmissionDate, DischargeDate, Diagnosis |
| TREATMENT | TreatmentID → PatientID, DoctorID, MedicationCode, TreatmentDate, TreatmentType, Description, Cost |
| MEDICATION | MedicationCode → MedicationName, Manufacturer, DosageForm, UnitPrice |
| PRESCRIPTION | PrescriptionID → PatientID, DoctorID, MedicationCode, TreatmentID, PrescriptionDate, Dosage, Frequency, Duration |

## Relationship Summary

**Direct Relationships:**
- DOCTOR → DEPARTMENT (many-to-one)
- NURSE → DEPARTMENT (many-to-one)
- DEPARTMENT → DOCTOR (one-to-one, head doctor)

**Junction Tables (Many-to-Many):**
- APPOINTMENT: PATIENT ↔ DOCTOR
- ADMISSION: PATIENT ↔ DOCTOR ↔ DEPARTMENT
- TREATMENT: PATIENT ↔ DOCTOR (optionally involves MEDICATION)
- PRESCRIPTION: PATIENT ↔ DOCTOR ↔ MEDICATION (optionally results from TREATMENT)

**Additional Relationships:**
- TREATMENT ↔ MEDICATION (optional): A treatment may involve medication administration
- TREATMENT ↔ PRESCRIPTION (optional): A treatment may result in a prescription
