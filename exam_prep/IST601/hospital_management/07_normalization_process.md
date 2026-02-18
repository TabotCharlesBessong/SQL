# Normalization Process: Hospital Management (1NF to BCNF)

## Overview

This document analyzes all nine tables from the relational schema and verifies each satisfies 1NF, 2NF, 3NF, and BCNF.

**Tables under analysis:**
- PATIENT (PatientID, PatientName, DateOfBirth, Gender, Phone, Email, Street, City, PostalCode, EmergencyContactName, EmergencyContactPhone, InsuranceProvider)
- DOCTOR (DoctorID, DoctorName, Specialization, Phone, Email, LicenseNumber, DepartmentCode)
- NURSE (NurseID, NurseName, CertificationLevel, Phone, Email, LicenseNumber, DepartmentCode)
- DEPARTMENT (DepartmentCode, DepartmentName, Building, Floor, HeadDoctorID)
- APPOINTMENT (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentType, Status, Notes)
- ADMISSION (AdmissionID, PatientID, DoctorID, DepartmentCode, RoomNumber, AdmissionDate, DischargeDate, Diagnosis)
- TREATMENT (TreatmentID, PatientID, DoctorID, MedicationCode, TreatmentDate, TreatmentType, Description, Cost)
- MEDICATION (MedicationCode, MedicationName, Manufacturer, DosageForm, UnitPrice)
- PRESCRIPTION (PrescriptionID, PatientID, DoctorID, MedicationCode, TreatmentID, PrescriptionDate, Dosage, Frequency, Duration)

---

## FIRST NORMAL FORM (1NF)

**Definition:** Atomic values, unique attribute names, unique rows, order independence.

| Table       | Atomic | Unique attrs | Unique rows | Order indep | Result |
|-------------|--------|--------------|-------------|-------------|--------|
| PATIENT     | ✅     | ✅           | ✅ (PatientID) | ✅          | 1NF    |
| DOCTOR      | ✅     | ✅           | ✅ (DoctorID) | ✅          | 1NF    |
| NURSE       | ✅     | ✅           | ✅ (NurseID)  | ✅          | 1NF    |
| DEPARTMENT  | ✅     | ✅           | ✅ (DeptCode) | ✅          | 1NF    |
| APPOINTMENT | ✅     | ✅           | ✅ (ApptID)   | ✅          | 1NF    |
| ADMISSION   | ✅     | ✅           | ✅ (AdmID)    | ✅          | 1NF    |
| TREATMENT   | ✅     | ✅           | ✅ (TreatID)  | ✅          | 1NF    |
| MEDICATION  | ✅     | ✅           | ✅ (MedCode)  | ✅          | 1NF    |
| PRESCRIPTION| ✅     | ✅           | ✅ (PrescID)  | ✅          | 1NF    |

**Conclusion:** All tables satisfy 1NF.

---

## SECOND NORMAL FORM (2NF)

**Definition:** In 1NF and no partial dependencies.

| Table       | PK            | Partial dependencies? | Result |
|-------------|---------------|----------------------|--------|
| PATIENT     | PatientID     | None (simple key)     | ✅ 2NF |
| DOCTOR      | DoctorID      | None (simple key)     | ✅ 2NF |
| NURSE       | NurseID       | None (simple key)     | ✅ 2NF |
| DEPARTMENT  | DepartmentCode| None (simple key)     | ✅ 2NF |
| APPOINTMENT | AppointmentID | None; CK (PatientID, DoctorID, ApptDate, ApptTime) has no partial deps | ✅ 2NF |
| ADMISSION   | AdmissionID   | None; CK (PatientID, RoomNumber, AdmissionDate) has no partial deps | ✅ 2NF |
| TREATMENT   | TreatmentID   | None (simple key)     | ✅ 2NF |
| MEDICATION  | MedicationCode| None (simple key)     | ✅ 2NF |
| PRESCRIPTION| PrescriptionID| None; CK (PatientID, DoctorID, MedCode, PrescDate) has no partial deps | ✅ 2NF |

**Conclusion:** All tables satisfy 2NF.

---

## THIRD NORMAL FORM (3NF)

**Definition:** In 2NF and no transitive dependencies.

| Table       | Transitive dependencies? | Result |
|-------------|--------------------------|--------|
| PATIENT     | None                     | ✅ 3NF |
| DOCTOR      | None                     | ✅ 3NF |
| NURSE       | None                     | ✅ 3NF |
| DEPARTMENT  | None                     | ✅ 3NF |
| APPOINTMENT | None                     | ✅ 3NF |
| ADMISSION   | None                     | ✅ 3NF |
| TREATMENT   | None                     | ✅ 3NF |
| MEDICATION  | None                     | ✅ 3NF |
| PRESCRIPTION| None                     | ✅ 3NF |

**Conclusion:** All tables satisfy 3NF.

---

## BOYCE-CODD NORMAL FORM (BCNF)

**Definition:** In 3NF and every determinant is a superkey.

| Table       | Determinants | Superkeys? | Result |
|-------------|--------------|------------|--------|
| PATIENT     | PatientID    | ✅         | ✅ BCNF |
| DOCTOR      | DoctorID     | ✅         | ✅ BCNF |
| NURSE       | NurseID      | ✅         | ✅ BCNF |
| DEPARTMENT  | DepartmentCode| ✅        | ✅ BCNF |
| APPOINTMENT | AppointmentID; (PatientID, DoctorID, ApptDate, ApptTime) | ✅ | ✅ BCNF |
| ADMISSION   | AdmissionID; (PatientID, RoomNumber, AdmissionDate) | ✅ | ✅ BCNF |
| TREATMENT   | TreatmentID  | ✅         | ✅ BCNF |
| MEDICATION  | MedicationCode| ✅       | ✅ BCNF |
| PRESCRIPTION| PrescriptionID; (PatientID, DoctorID, MedCode, PrescDate) | ✅ | ✅ BCNF |
|             | Note: TreatmentID FK is optional, doesn't affect normalization |       |       |

**Conclusion:** All tables satisfy BCNF.

---

## Normalization Summary

| Normal Form | PATIENT | DOCTOR | NURSE | DEPT | APPT | ADM | TREAT | MED | PRESC |
|-------------|---------|--------|-------|------|------|-----|-------|-----|-------|
| **1NF**     | ✅      | ✅     | ✅    | ✅   | ✅   | ✅  | ✅    | ✅  | ✅    |
| **2NF**     | ✅      | ✅     | ✅    | ✅   | ✅   | ✅  | ✅    | ✅  | ✅    |
| **3NF**     | ✅      | ✅     | ✅    | ✅   | ✅   | ✅  | ✅    | ✅  | ✅    |
| **BCNF**    | ✅      | ✅     | ✅    | ✅   | ✅   | ✅  | ✅    | ✅  | ✅    |

---

## Final Schema (BCNF)

```
PATIENT (PatientID, PatientName, DateOfBirth, Gender, Phone, Email, Street, City, PostalCode, EmergencyContactName, EmergencyContactPhone, InsuranceProvider)
PK: PatientID

DOCTOR (DoctorID, DoctorName, Specialization, Phone, Email, LicenseNumber, DepartmentCode)
PK: DoctorID
FK: DepartmentCode → DEPARTMENT

NURSE (NurseID, NurseName, CertificationLevel, Phone, Email, LicenseNumber, DepartmentCode)
PK: NurseID
FK: DepartmentCode → DEPARTMENT

DEPARTMENT (DepartmentCode, DepartmentName, Building, Floor, HeadDoctorID)
PK: DepartmentCode
FK: HeadDoctorID → DOCTOR

APPOINTMENT (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentType, Status, Notes)
PK: AppointmentID
FK: PatientID → PATIENT, DoctorID → DOCTOR

ADMISSION (AdmissionID, PatientID, DoctorID, DepartmentCode, RoomNumber, AdmissionDate, DischargeDate, Diagnosis)
PK: AdmissionID
FK: PatientID → PATIENT, DoctorID → DOCTOR, DepartmentCode → DEPARTMENT

TREATMENT (TreatmentID, PatientID, DoctorID, MedicationCode, TreatmentDate, TreatmentType, Description, Cost)
PK: TreatmentID
FK: PatientID → PATIENT, DoctorID → DOCTOR, MedicationCode → MEDICATION (optional)

MEDICATION (MedicationCode, MedicationName, Manufacturer, DosageForm, UnitPrice)
PK: MedicationCode

PRESCRIPTION (PrescriptionID, PatientID, DoctorID, MedicationCode, TreatmentID, PrescriptionDate, Dosage, Frequency, Duration)
PK: PrescriptionID
FK: PatientID → PATIENT, DoctorID → DOCTOR, MedicationCode → MEDICATION, TreatmentID → TREATMENT (optional)
```
