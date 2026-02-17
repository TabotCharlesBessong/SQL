# Entity Identification and Attributes

## Entities Identified

### 1. STUDENT
**Description:** Represents a student enrolled at the university

**Attributes:**
- StudentID (Primary Key) - Unique identifier for each student
- StudentName - Full name of the student
- Email - Student's email address
- Phone - Student's phone number
- DateOfBirth - Student's date of birth
- Major - Student's academic major (e.g., Computer Science, Mathematics)

**Sample Values:**
- StudentID: S001, S002, S003, etc.
- Major: Computer Science, Mathematics, Physics, Engineering

---

### 2. INSTRUCTOR
**Description:** Represents an instructor/faculty member teaching courses

**Attributes:**
- InstructorID (Primary Key) - Unique identifier for each instructor
- InstructorName - Full name of the instructor
- Email - Instructor's email address
- Phone - Instructor's phone number
- Department - Department the instructor belongs to
- OfficeBuilding - Building where instructor's office is located
- OfficeRoom - Room number of instructor's office

**Sample Values:**
- InstructorID: I001, I002, I003, etc.
- Department: CS Department, Math Department, Physics Department
- OfficeBuilding: Science Hall, Math Building, Engineering Building

---

### 3. COURSE
**Description:** Represents a course offered by the university

**Attributes:**
- CourseCode (Primary Key) - Unique course identifier (e.g., CS101, MATH201)
- CourseTitle - Name/title of the course
- CreditHours - Number of credit hours for the course
- Department - Department offering the course
- Description - Brief description of the course content

**Sample Values:**
- CourseCode: CS101, CS201, MATH101, MATH201, PHYS101
- CreditHours: 3, 4, 1
- Department: CS Department, Math Department, Physics Department

---

### 4. ENROLLMENT
**Description:** Represents a student's enrollment in a course for a specific semester

**Attributes:**
- EnrollmentID (Primary Key) - Unique identifier for each enrollment
- StudentID (Foreign Key) - References STUDENT
- CourseCode (Foreign Key) - References COURSE
- InstructorID (Foreign Key) - References INSTRUCTOR
- Semester - Semester when course is taken (Fall, Spring, Summer)
- Year - Year when course is taken (e.g., 2024, 2025)
- EnrollmentDate - Date when student enrolled
- Grade - Final grade received (A, B, C, D, F, or NULL if not completed)

**Sample Values:**
- Semester: Fall, Spring, Summer
- Year: 2024, 2025
- Grade: A, B, C, D, F, NULL

**Note:** The combination of (StudentID, CourseCode, Semester, Year) should be unique to prevent duplicate enrollments.

---

## Relationships

1. **STUDENT - ENROLLMENT:** One-to-Many
   - One student can have many enrollments
   - Each enrollment belongs to exactly one student

2. **COURSE - ENROLLMENT:** One-to-Many
   - One course can have many enrollments
   - Each enrollment is for exactly one course

3. **INSTRUCTOR - ENROLLMENT:** One-to-Many
   - One instructor can have many enrollments (teaches multiple courses/semesters)
   - Each enrollment is taught by exactly one instructor

4. **INSTRUCTOR - COURSE:** One-to-Many (implicit through enrollment)
   - One instructor can teach multiple courses
   - Each course is taught by exactly one instructor (per semester)

## Initial Unnormalized Design (What NOT to do)

If we put everything in one table, we would have:
- All student attributes repeated for each enrollment
- All course attributes repeated for each enrollment
- All instructor attributes repeated for each enrollment
- This leads to data redundancy and anomalies
