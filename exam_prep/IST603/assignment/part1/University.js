/**
 * University class with:
 * - Static nested class Policy: store and display university rules (accessed without University instance).
 * - Non-static inner class Student: store name and department; accesses private members of University.
 */

class University {
  #uniName = "Tech Institute"; // Private field (outer class)

  // Static nested class: attached to class, no outer instance needed
  static Policy = class Policy {
    constructor() {
      this.rules = [];
    }

    addRule(rule) {
      this.rules.push(rule);
    }

    displayRules() {
      console.log("University rules:");
      this.rules.forEach((r) => console.log("  - " + r));
    }
  };

  // Non-static inner class: receives outer University instance to access its private member
  constructor() {}

  createStudent(name, department) {
    const outer = this;
    return new (class Student {
      constructor(name, department) {
        this.name = name;
        this.department = department;
        this._university = outer; // Reference to outer University instance
      }

      displayInfo() {
        // Access private member of outer class via reference (outer stores #uniName)
        const uniName = outer.#uniName;
        console.log(
          `Student: ${this.name} | Dept: ${this.department} | Uni: ${uniName}`
        );
      }
    })(name, department);
  }
}

function main() {
  // Access Policy WITHOUT creating a University object (static nested class)
  const Policy = University.Policy;
  const policy = new Policy();
  policy.addRule("Attendance must be above 75%.");
  policy.addRule("Academic integrity is mandatory.");
  policy.displayRules();

  // Inner class requires a University instance; Student accesses outer's private #uniName
  const myUni = new University();
  const s1 = myUni.createStudent("Alice", "Engineering");
  const s2 = myUni.createStudent("Bob", "Computer Science");
  s1.displayInfo();
  s2.displayInfo();
}

main();
