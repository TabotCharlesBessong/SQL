-- ============================================
-- HOSPITAL MANAGEMENT - NORMALIZED DATABASE (BCNF)
-- PostgreSQL compatible
-- ============================================

DROP TABLE IF EXISTS Prescription;
DROP TABLE IF EXISTS Treatment;
DROP TABLE IF EXISTS Admission;
DROP TABLE IF EXISTS Appointment;
DROP TABLE IF EXISTS Medication;
DROP TABLE IF EXISTS Nurse;
DROP TABLE IF EXISTS Doctor;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Patient;

-- ============================================
-- 1. PATIENT TABLE
-- ============================================
CREATE TABLE Patient (
    PatientID VARCHAR(10) PRIMARY KEY,
    PatientName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender VARCHAR(10),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Street VARCHAR(100),
    City VARCHAR(50),
    PostalCode VARCHAR(20),
    EmergencyContactName VARCHAR(100),
    EmergencyContactPhone VARCHAR(20),
    InsuranceProvider VARCHAR(50)
);

-- ============================================
-- 2. DEPARTMENT TABLE
-- ============================================
-- Note: HeadDoctorID FK added after Doctor table is created (circular dependency)
CREATE TABLE Department (
    DepartmentCode VARCHAR(10) PRIMARY KEY,
    DepartmentName VARCHAR(50) NOT NULL,
    Building VARCHAR(50),
    Floor INT,
    HeadDoctorID VARCHAR(10)
);

-- ============================================
-- 3. DOCTOR TABLE
-- ============================================
CREATE TABLE Doctor (
    DoctorID VARCHAR(10) PRIMARY KEY,
    DoctorName VARCHAR(100) NOT NULL,
    Specialization VARCHAR(50) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100),
    LicenseNumber VARCHAR(20) UNIQUE NOT NULL,
    DepartmentCode VARCHAR(10) NOT NULL,
    CONSTRAINT fk_doctor_dept FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Add foreign key constraint for Department.HeadDoctorID after Doctor table exists
ALTER TABLE Department ADD CONSTRAINT fk_dept_head_doctor FOREIGN KEY (HeadDoctorID) REFERENCES Doctor(DoctorID) ON DELETE SET NULL ON UPDATE CASCADE;

-- ============================================
-- 4. NURSE TABLE
-- ============================================
CREATE TABLE Nurse (
    NurseID VARCHAR(10) PRIMARY KEY,
    NurseName VARCHAR(100) NOT NULL,
    CertificationLevel VARCHAR(20) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100),
    LicenseNumber VARCHAR(20) UNIQUE NOT NULL,
    DepartmentCode VARCHAR(10) NOT NULL,
    CONSTRAINT fk_nurse_dept FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- ============================================
-- 5. MEDICATION TABLE
-- ============================================
CREATE TABLE Medication (
    MedicationCode VARCHAR(20) PRIMARY KEY,
    MedicationName VARCHAR(100) NOT NULL,
    Manufacturer VARCHAR(100),
    DosageForm VARCHAR(50),
    UnitPrice DECIMAL(10,2) CHECK (UnitPrice >= 0)
);

-- ============================================
-- 6. APPOINTMENT TABLE
-- ============================================
CREATE TABLE Appointment (
    AppointmentID SERIAL PRIMARY KEY,
    PatientID VARCHAR(10) NOT NULL,
    DoctorID VARCHAR(10) NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    AppointmentType VARCHAR(50),
    Status VARCHAR(20) DEFAULT 'Scheduled',
    Notes TEXT,
    CONSTRAINT fk_appt_patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_appt_doctor FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT uk_appt_unique UNIQUE (PatientID, DoctorID, AppointmentDate, AppointmentTime),
    CONSTRAINT chk_appt_status CHECK (Status IN ('Scheduled', 'Completed', 'Cancelled'))
);

-- ============================================
-- 7. ADMISSION TABLE
-- ============================================
CREATE TABLE Admission (
    AdmissionID SERIAL PRIMARY KEY,
    PatientID VARCHAR(10) NOT NULL,
    DoctorID VARCHAR(10) NOT NULL,
    DepartmentCode VARCHAR(10) NOT NULL,
    RoomNumber VARCHAR(20) NOT NULL,
    AdmissionDate DATE NOT NULL,
    DischargeDate DATE,
    Diagnosis TEXT,
    CONSTRAINT fk_adm_patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_adm_doctor FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_adm_dept FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT uk_adm_unique UNIQUE (PatientID, RoomNumber, AdmissionDate),
    CONSTRAINT chk_discharge CHECK (DischargeDate IS NULL OR DischargeDate >= AdmissionDate)
);

-- ============================================
-- 8. TREATMENT TABLE
-- ============================================
CREATE TABLE Treatment (
    TreatmentID SERIAL PRIMARY KEY,
    PatientID VARCHAR(10) NOT NULL,
    DoctorID VARCHAR(10) NOT NULL,
    TreatmentDate DATE NOT NULL,
    TreatmentType VARCHAR(50),
    Description TEXT,
    Cost DECIMAL(10,2) CHECK (Cost >= 0),
    CONSTRAINT fk_treat_patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_treat_doctor FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- ============================================
-- 9. PRESCRIPTION TABLE
-- ============================================
CREATE TABLE Prescription (
    PrescriptionID SERIAL PRIMARY KEY,
    PatientID VARCHAR(10) NOT NULL,
    DoctorID VARCHAR(10) NOT NULL,
    MedicationCode VARCHAR(20) NOT NULL,
    PrescriptionDate DATE NOT NULL,
    Dosage VARCHAR(50),
    Frequency VARCHAR(50),
    Duration INT CHECK (Duration > 0),
    CONSTRAINT fk_pres_patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_pres_doctor FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_pres_medication FOREIGN KEY (MedicationCode) REFERENCES Medication(MedicationCode) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT uk_pres_unique UNIQUE (PatientID, DoctorID, MedicationCode, PrescriptionDate)
);

-- ============================================
-- CREATE INDEXES
-- ============================================
CREATE INDEX idx_doctor_dept ON Doctor(DepartmentCode);
CREATE INDEX idx_nurse_dept ON Nurse(DepartmentCode);
CREATE INDEX idx_appt_patient ON Appointment(PatientID);
CREATE INDEX idx_appt_doctor ON Appointment(DoctorID);
CREATE INDEX idx_adm_patient ON Admission(PatientID);
CREATE INDEX idx_adm_doctor ON Admission(DoctorID);
CREATE INDEX idx_adm_dept ON Admission(DepartmentCode);
CREATE INDEX idx_treat_patient ON Treatment(PatientID);
CREATE INDEX idx_treat_doctor ON Treatment(DoctorID);
CREATE INDEX idx_pres_patient ON Prescription(PatientID);
CREATE INDEX idx_pres_doctor ON Prescription(DoctorID);
CREATE INDEX idx_pres_medication ON Prescription(MedicationCode);
