# Hospital Management System - Scenario

## Story

City General Hospital needs a comprehensive database system to manage patients, medical staff, departments, appointments, admissions, treatments, and medications.

**Patients:**
- Each patient has a unique Patient ID, full name, date of birth, gender, phone number, email, address (street, city, postal code), emergency contact name and phone, and insurance provider.
- Patients can have multiple appointments, admissions, and treatments over time.

**Doctors:**
- Each doctor has a unique Doctor ID, full name, specialization (Cardiology, Pediatrics, Surgery, etc.), phone number, email, and license number.
- Doctors belong to departments and can see multiple patients.

**Nurses:**
- Each nurse has a unique Nurse ID, full name, certification level (RN, LPN, etc.), phone number, email, and license number.
- Nurses are assigned to departments and can care for multiple patients.

**Departments:**
- Each department has a unique Department Code, department name (Cardiology, Emergency, Pediatrics, etc.), location (building and floor), and head doctor (who manages the department).
- Departments have multiple doctors and nurses assigned to them.

**Appointments:**
- When a patient schedules an appointment, the system records:
  - Patient ID
  - Doctor ID (which doctor they're seeing)
  - Appointment date and time
  - Appointment type (Consultation, Follow-up, Check-up)
  - Status (Scheduled, Completed, Cancelled)
  - Notes

**Admissions:**
- When a patient is admitted to the hospital, the system records:
  - Patient ID
  - Doctor ID (admitting doctor)
  - Department Code (which department)
  - Room number
  - Admission date
  - Discharge date (NULL if still admitted)
  - Diagnosis

**Treatments:**
- When a patient receives treatment, the system records:
  - Patient ID
  - Doctor ID (treating doctor)
  - Treatment date
  - Treatment type (Surgery, Medication, Therapy, etc.)
  - Description
  - Cost

**Medications:**
- Each medication has a unique Medication Code, medication name, manufacturer, dosage form (Tablet, Injection, etc.), and unit price.
- Medications can be prescribed to multiple patients.

**Prescriptions:**
- When a doctor prescribes medication to a patient, the system records:
  - Patient ID
  - Doctor ID (prescribing doctor)
  - Medication Code
  - Prescription date
  - Dosage
  - Frequency
  - Duration (days)

## Business Rules

1. A patient can have multiple appointments with different doctors
2. A doctor can see multiple patients
3. A doctor belongs to exactly one department
4. A department has one head doctor (who is also a doctor in that department)
5. A nurse is assigned to exactly one department
6. A patient can have multiple admissions over time
7. Each admission is to one department and supervised by one doctor
8. A patient can receive multiple treatments from different doctors
9. A doctor can prescribe multiple medications to multiple patients
10. A medication can be prescribed to multiple patients by different doctors
