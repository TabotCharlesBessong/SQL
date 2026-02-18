# Hospital Management System - Scenario

## Story

City General Hospital needs a comprehensive database system to manage patients, medical staff, departments, appointments, admissions, treatments, and medications.

**Patients:**
- Each patient has a unique Patient ID, full name, date of birth, gender, phone number, email, address (street, city, postal code), emergency contact name and phone, and insurance provider.

**Doctors:**
- Each doctor has a unique Doctor ID, full name, specialization (Cardiology, Pediatrics, Surgery, etc.), phone number, email, and license number.

**Nurses:**
- Each nurse has a unique Nurse ID, full name, certification level (RN, LPN, etc.), phone number, email, and license number.

**Departments:**
- Each department has a unique Department Code, department name (Cardiology, Emergency, Pediatrics, etc.), location (building and floor), and information about which doctor heads the department.

**Appointments:**
- The system needs to track appointment information including: appointment date and time, appointment type (Consultation, Follow-up, Check-up), status (Scheduled, Completed, Cancelled), and notes.

**Admissions:**
- The system needs to track patient admissions including: room number, admission date, discharge date (NULL if still admitted), and diagnosis.

**Treatments:**
- The system needs to track treatment information including: treatment date, treatment type (Surgery, Medication, Therapy, etc.), description, and cost.

**Medications:**
- Each medication has a unique Medication Code, medication name, manufacturer, dosage form (Tablet, Injection, etc.), and unit price.

**Prescriptions:**
- The system needs to track prescription information including: prescription date, dosage, frequency, and duration (days).
