"""
University class with:
- Static nested class Policy: store and display university rules (accessed without University instance).
- Non-static inner class Student: store name and department; accesses private members of University.
"""


class University:
    def __init__(self):
        self.__uni_name = "Tech Institute"  # Private member (name mangling)

    # Static nested class: accessed via University.Policy without a University instance
    class Policy:
        def __init__(self):
            self._rules = []

        def add_rule(self, rule: str) -> None:
            self._rules.append(rule)

        def display_rules(self) -> None:
            print("University rules:")
            for r in self._rules:
                print(f"  - {r}")

    # Non-static inner class: holds reference to outer University, accesses its private member
    class Student:
        def __init__(self, university: "University", name: str, department: str) -> None:
            self._university = university  # Reference to outer class instance
            self.name = name
            self.department = department

        def display_info(self) -> None:
            # Access private member of outer class (via stored reference and name-mangled attribute)
            uni_name = self._university._University__uni_name
            print(f"Student: {self.name} | Dept: {self.department} | Uni: {uni_name}")


def main() -> None:
    # Access Policy WITHOUT creating a University object (static nested class)
    policy = University.Policy()
    policy.add_rule("Attendance must be above 75%.")
    policy.add_rule("Academic integrity is mandatory.")
    policy.display_rules()

    # Inner class requires a University instance; Student accesses outer's private __uni_name
    my_uni = University()
    s1 = University.Student(my_uni, "Alice", "Engineering")
    s2 = University.Student(my_uni, "Bob", "Computer Science")
    s1.display_info()
    s2.display_info()


if __name__ == "__main__":
    main()
