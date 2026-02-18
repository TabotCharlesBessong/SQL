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

### 3. NURSE
**Attributes:**
- NurseID (PK)
- NurseName
- CertificationLevel
- Phone
- Email
- LicenseNumber

### 4. DEPARTMENT
**Attributes:**
- DepartmentCode (PK)
- DepartmentName
- Building
- Floor
- HeadDoctorID (information about which doctor heads the department)

### 5. APPOINTMENT
**Attributes:**
- AppointmentID (PK)
- AppointmentDate
- AppointmentTime
- AppointmentType
- Status
- Notes

### 6. ADMISSION
**Attributes:**
- AdmissionID (PK)
- RoomNumber
- AdmissionDate
- DischargeDate
- Diagnosis

### 7. TREATMENT
**Attributes:**
- TreatmentID (PK)
- TreatmentDate
- TreatmentType
- Description
- Cost
- MedicationCode (optional - for treatments involving medication administration)

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
- PrescriptionDate
- Dosage
- Frequency
- Duration
- TreatmentID (optional - if prescription results from a treatment)

**Note:** Foreign keys and relationships will be determined during the relational schema design phase based on what information needs to be linked together. The optional attributes (MedicationCode in TREATMENT, TreatmentID in PRESCRIPTION) represent relationships that may or may not exist for every record.
