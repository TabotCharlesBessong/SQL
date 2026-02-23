package exam_prep.IST603.assignment.part1;
// Create a class University that contains:
//  A static nested class Policy
//  A non-static inner class Student
// Requirements:
//  Policy should store and display university rules.
//  Student should store student name and department.
//  Demonstrate how:
// o The static nested class is accessed without creating a University object.
// o The inner class accesses private members of the outer class.

import java.util.*;

// Write a main() method to test all functionalities.


class University {
    private String uniName = "Tech Institute"; // Private member [cite: 11]

    // Static nested class: store and display university rules
    static class Policy {
        private final List<String> rules = new ArrayList<>();

        void addRule(String rule) {
            rules.add(rule);
        }

        void displayRules() {
            System.out.println("University rules:");
            for (String r : rules) System.out.println("  - " + r);
        }
    }

    // Non-static inner class [cite: 5]
    class Student {
        String name;
        String department;

        Student(String name, String department) {
            this.name = name; 
            this.department = department; 
        }

        void displayInfo() {
            // Accesses private member 'uniName' of the outer class [cite: 11]
            System.out.println("Student: " + name + " | Dept: " + department + " | Uni: " + uniName);
        }
    }

    public static void main(String[] args) {
        // Access Policy WITHOUT creating a University object (static nested class)
        University.Policy policy = new University.Policy();
        policy.addRule("Attendance must be above 75%.");
        policy.addRule("Academic integrity is mandatory.");
        policy.displayRules();

        // Inner class requires a University instance; Student accesses outer's private uniName
        University myUni = new University();
        University.Student s1 = myUni.new Student("Alice", "Engineering");
        University.Student s2 = myUni.new Student("Bob", "Computer Science");
        s1.displayInfo();
        s2.displayInfo();
    }
}