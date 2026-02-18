# University Course Management System - Scenario

## Story

The University of Technology wants to implement a database system to manage its courses, students, instructors, and enrollments. Here's how the system currently works:

**Students:**
- Each student has a unique Student ID, full name, email address, phone number, date of birth, and major (e.g., Computer Science, Mathematics, Physics).
- Students can enroll in multiple courses each semester.

**Instructors:**
- Each instructor has a unique Instructor ID, full name, email address, phone number, department they belong to (e.g., CS Department, Math Department), and their office location (building and room number).
- Instructors can teach multiple courses.

**Courses:**
- Each course has a unique Course Code (e.g., CS101, MATH201), course title, number of credit hours, department offering the course, and a description.
- Each course is assigned to one instructor who teaches it.
- Courses are offered in different semesters (Fall, Spring, Summer) and years (e.g., 2024, 2025).

**Enrollments:**
- When a student enrolls in a course, the system records:
  - The student's information
  - The course information
  - The instructor teaching that course
  - The semester and year
  - The enrollment date
  - The final grade received (A, B, C, D, F, or NULL if not yet completed)
  - The number of credit hours for that course

**Current Issues:**
The university has been storing all this information in a single table, which has led to several problems:
- When updating a course's credit hours, they have to update multiple rows
- If a student drops all courses, their information might be lost
- If an instructor changes departments, multiple records need updating
- Course information is repeated for every student enrollment

## Business Rules

1. A student can enroll in multiple courses
2. A course can have multiple students enrolled
3. Each course enrollment is taught by exactly one instructor (instructor assignment is per enrollment/semester, not per course permanently)
4. An instructor can teach multiple courses
5. Each enrollment is for a specific semester and year
6. A student can enroll in the same course multiple times (retaking a course)
7. Grades are assigned per enrollment (student + course + semester combination)
8. Course credit hours are fixed per course, not per enrollment
9. The same course can be taught by different instructors in different semesters (e.g., CS101 by Dr. Johnson in Fall 2024, Dr. Lee in Spring 2025)

## Sample Data Requirements

We need to track:
- At least 5-10 students
- At least 3-5 instructors
- At least 5-8 different courses
- At least 15-20 enrollment records across different semesters
- Some students should have multiple enrollments
- Some courses should have multiple students
- Include some completed courses (with grades) and some in-progress courses (no grades yet)
