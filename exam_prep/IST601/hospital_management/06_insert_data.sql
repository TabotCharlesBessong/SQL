-- ============================================
-- INSERT DATA - Hospital Management
-- ============================================
-- 
-- This file inserts sample data into the normalized tables.
-- Foreign key relationships (discovered during ER diagram/relational schema phases)
-- determine the insertion order.
-- 
-- Note: Department must be created first, but HeadDoctorID references Doctor
-- So we'll insert Departments without HeadDoctorID first, then update after Doctors are inserted

-- 1. DEPARTMENTS (without HeadDoctorID initially)
INSERT INTO Department (DepartmentCode, DepartmentName, Building, Floor) VALUES
('CARD', 'Cardiology', 'Main Building', 3),
('PEDS', 'Pediatrics', 'Main Building', 2),
('SURG', 'Surgery', 'Main Building', 4),
('EMER', 'Emergency', 'Main Building', 1);

-- 2. DOCTORS
INSERT INTO Doctor VALUES
('D001', 'Dr. Sarah Johnson', 'Cardiology', '555-3001', 'sarah.j@hospital.gov', 'LIC-CARD-001', 'CARD'),
('D002', 'Dr. Michael Chen', 'Cardiology', '555-3002', 'michael.c@hospital.gov', 'LIC-CARD-002', 'CARD'),
('D003', 'Dr. Emily Davis', 'Pediatrics', '555-3003', 'emily.d@hospital.gov', 'LIC-PEDS-001', 'PEDS'),
('D004', 'Dr. Robert Wilson', 'Surgery', '555-3004', 'robert.w@hospital.gov', 'LIC-SURG-001', 'SURG'),
('D005', 'Dr. Lisa Martinez', 'Emergency', '555-3005', 'lisa.m@hospital.gov', 'LIC-EMER-001', 'EMER');

-- 3. UPDATE DEPARTMENTS with Head Doctors
UPDATE Department SET HeadDoctorID = 'D001' WHERE DepartmentCode = 'CARD';
UPDATE Department SET HeadDoctorID = 'D003' WHERE DepartmentCode = 'PEDS';
UPDATE Department SET HeadDoctorID = 'D004' WHERE DepartmentCode = 'SURG';
UPDATE Department SET HeadDoctorID = 'D005' WHERE DepartmentCode = 'EMER';

-- 4. NURSES
INSERT INTO Nurse VALUES
('N001', 'Jennifer Brown', 'RN', '555-4001', 'jennifer.b@hospital.gov', 'NUR-RN-001', 'CARD'),
('N002', 'David Lee', 'RN', '555-4002', 'david.l@hospital.gov', 'NUR-RN-002', 'PEDS'),
('N003', 'Amanda White', 'LPN', '555-4003', 'amanda.w@hospital.gov', 'NUR-LPN-001', 'SURG'),
('N004', 'James Taylor', 'RN', '555-4004', 'james.t@hospital.gov', 'NUR-RN-003', 'EMER'),
('N005', 'Maria Garcia', 'RN', '555-4005', 'maria.g@hospital.gov', 'NUR-RN-004', 'CARD');

-- 5. PATIENTS
INSERT INTO Patient (
    PatientID, PatientName, DateOfBirth, Gender, Phone, Email,
    Street, City, PostalCode,
    EmergencyContactName, EmergencyContactPhone,
    InsuranceProvider
) VALUES
('P001', 'John Smith', '1980-05-15', 'M', '555-1001', 'john.s@email.com', '123 Main St', 'Springfield', '12345', 'Jane Smith', '555-1002', 'BlueCross'),
('P002', 'Mary Johnson', '1995-08-22', 'F', '555-2001', 'mary.j@email.com', '456 Oak Ave', 'Springfield', '12346', 'Tom Johnson', '555-2002', 'Aetna'),
('P003', 'Robert Brown', '1975-11-10', 'M', '555-3001', 'robert.b@email.com', '789 Pine Rd', 'Riverside', '23456', 'Susan Brown', '555-3002', 'Medicare'),
('P004', 'Linda Davis', '2005-03-08', 'F', '555-4001', 'linda.d@email.com', '321 Elm St', 'Springfield', '12347', 'Mark Davis', '555-4002', 'BlueCross'),
('P005', 'William Wilson', '1990-07-25', 'M', '555-5001', 'william.w@email.com', '654 Maple Dr', 'Riverside', '23457', 'Patricia Wilson', '555-5002', 'Aetna');

-- 6. MEDICATIONS
INSERT INTO Medication VALUES
('MED001', 'Aspirin', 'PharmaCorp', 'Tablet', 0.50),
('MED002', 'Ibuprofen', 'MediPharm', 'Tablet', 0.75),
('MED003', 'Amoxicillin', 'DrugCo', 'Capsule', 2.00),
('MED004', 'Insulin', 'BioMed', 'Injection', 15.00),
('MED005', 'Metformin', 'PharmaCorp', 'Tablet', 1.25);

-- 7. APPOINTMENTS
INSERT INTO Appointment (PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentType, Status, Notes) VALUES
('P001', 'D001', '2024-10-15', '09:00:00', 'Consultation', 'Completed', 'Routine checkup'),
('P001', 'D001', '2024-11-15', '09:00:00', 'Follow-up', 'Scheduled', NULL),
('P002', 'D003', '2024-10-16', '10:30:00', 'Consultation', 'Completed', 'Child wellness visit'),
('P003', 'D004', '2024-10-17', '14:00:00', 'Consultation', 'Completed', 'Pre-surgery consultation'),
('P004', 'D003', '2024-10-18', '11:00:00', 'Check-up', 'Scheduled', NULL),
('P005', 'D002', '2024-10-19', '15:30:00', 'Follow-up', 'Scheduled', NULL);

-- 8. ADMISSIONS
INSERT INTO Admission (PatientID, DoctorID, DepartmentCode, RoomNumber, AdmissionDate, DischargeDate, Diagnosis) VALUES
('P001', 'D001', 'CARD', '301', '2024-10-01', '2024-10-05', 'Hypertension monitoring'),
('P003', 'D004', 'SURG', '401', '2024-10-10', '2024-10-15', 'Appendectomy'),
('P002', 'D003', 'PEDS', '201', '2024-10-12', NULL, 'Pneumonia treatment'),
('P005', 'D002', 'CARD', '302', '2024-10-20', NULL, 'Cardiac observation');

-- 9. TREATMENTS
-- Note: Some treatments involve medication (MedicationCode), others don't (surgery, therapy)
INSERT INTO Treatment (PatientID, DoctorID, MedicationCode, TreatmentDate, TreatmentType, Description, Cost) VALUES
('P001', 'D001', NULL, '2024-10-02', 'Medication', 'Blood pressure medication adjustment', 150.00),
('P003', 'D004', NULL, '2024-10-11', 'Surgery', 'Appendectomy procedure', 5000.00),
('P002', 'D003', 'MED003', '2024-10-13', 'Medication', 'Antibiotic treatment', 200.00),
('P001', 'D001', NULL, '2024-10-03', 'Therapy', 'Cardiac rehabilitation session', 300.00),
('P005', 'D002', NULL, '2024-10-21', 'Diagnostic', 'EKG and stress test', 450.00);

-- 10. PRESCRIPTIONS
-- Note: Some prescriptions result from treatments (TreatmentID), others are standalone
INSERT INTO Prescription (PatientID, DoctorID, MedicationCode, TreatmentID, PrescriptionDate, Dosage, Frequency, Duration) VALUES
('P001', 'D001', 'MED001', 1, '2024-10-02', '81mg', 'Once daily', 30),  -- Results from treatment 1
('P001', 'D001', 'MED004', NULL, '2024-10-02', '10 units', 'Twice daily', 30),  -- Standalone prescription
('P002', 'D003', 'MED003', 3, '2024-10-13', '500mg', 'Three times daily', 7),  -- Results from treatment 3
('P003', 'D004', 'MED002', 2, '2024-10-11', '400mg', 'Every 6 hours', 5),  -- Results from treatment 2 (surgery follow-up)
('P005', 'D002', 'MED001', NULL, '2024-10-21', '81mg', 'Once daily', 30),  -- Standalone prescription
('P002', 'D003', 'MED002', NULL, '2024-10-13', '200mg', 'Every 8 hours', 7);  -- Standalone prescription

-- Verify
SELECT 'Patients' AS tbl, COUNT(*) AS cnt FROM Patient
UNION ALL SELECT 'Doctors', COUNT(*) FROM Doctor
UNION ALL SELECT 'Nurses', COUNT(*) FROM Nurse
UNION ALL SELECT 'Departments', COUNT(*) FROM Department
UNION ALL SELECT 'Medications', COUNT(*) FROM Medication
UNION ALL SELECT 'Appointments', COUNT(*) FROM Appointment
UNION ALL SELECT 'Admissions', COUNT(*) FROM Admission
UNION ALL SELECT 'Treatments', COUNT(*) FROM Treatment
UNION ALL SELECT 'Prescriptions', COUNT(*) FROM Prescription;
