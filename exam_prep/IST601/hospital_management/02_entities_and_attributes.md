# Entity Identification and Attributes

## Entities Identified

### 1. PATIENT
**Attributes:**
- PatientID (PK)
- PatientName
- DateOfBirth
- Gender
- Phone
- Email
- Street
- City
- PostalCode
- EmergencyContactName
- EmergencyContactPhone
- InsuranceProvider

### 2. DOCTOR
**Attributes:**
- DoctorID (PK)
- DoctorName
- Specialization
- Phone
- Email
- LicenseNumber
- DepartmentCode (FK) - Department doctor belongs to

### 3. NURSE
**Attributes:**
- NurseID (PK)
- NurseName
- CertificationLevel
- Phone
- Email
- LicenseNumber
- DepartmentCode (FK) - Department nurse is assigned to

### 4. DEPARTMENT
**Attributes:**
- DepartmentCode (PK)
- DepartmentName
- Building
- Floor
- HeadDoctorID (FK) - Doctor who heads the department

### 5. APPOINTMENT
**Attributes:**
- AppointmentID (PK)
- PatientID (FK)
- DoctorID (FK)
- AppointmentDate
- AppointmentTime
- AppointmentType
- Status
- Notes

### 6. ADMISSION
**Attributes:**
- AdmissionID (PK)
- PatientID (FK)
- DoctorID (FK) - Admitting doctor
- DepartmentCode (FK)
- RoomNumber
- AdmissionDate
- DischargeDate
- Diagnosis

### 7. TREATMENT
**Attributes:**
- TreatmentID (PK)
- PatientID (FK)
- DoctorID (FK)
- TreatmentDate
- TreatmentType
- Description
- Cost

### 8. MEDICATION
**Attributes:**
- MedicationCode (PK)
- MedicationName
- Manufacturer
- DosageForm
- UnitPrice

### 9. PRESCRIPTION
**Attributes:**
- PrescriptionID (PK)
- PatientID (FK)
- DoctorID (FK)
- MedicationCode (FK)
- PrescriptionDate
- Dosage
- Frequency
- Duration

## Relationships

1. **DOCTOR ↔ DEPARTMENT:** Many-to-One (many doctors, one department)
2. **NURSE ↔ DEPARTMENT:** Many-to-One (many nurses, one department)
3. **DEPARTMENT ↔ DOCTOR:** One-to-One (one head doctor per department)
4. **PATIENT ↔ DOCTOR:** Many-to-Many through APPOINTMENT
5. **PATIENT ↔ DOCTOR:** Many-to-Many through ADMISSION
6. **PATIENT ↔ DOCTOR:** Many-to-Many through TREATMENT
7. **PATIENT ↔ DOCTOR:** Many-to-Many through PRESCRIPTION
8. **PATIENT ↔ MEDICATION:** Many-to-Many through PRESCRIPTION
9. **DOCTOR ↔ MEDICATION:** Many-to-Many through PRESCRIPTION
10. **PATIENT ↔ DEPARTMENT:** Many-to-Many through ADMISSION

**Key Design Points:**
- Multiple junction tables (APPOINTMENT, ADMISSION, TREATMENT, PRESCRIPTION)
- Direct relationships: DOCTOR→DEPARTMENT, NURSE→DEPARTMENT, DEPARTMENT→DOCTOR (head)
- Complex network of relationships showing real-world hospital operations
