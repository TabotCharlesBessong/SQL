"""
Demonstration of inheritance in Python.

This example shows:
- Single inheritance (Person -> Student)
- Multilevel inheritance (Person -> Student -> GraduateStudent)
- Method overriding
- Calling the parent implementation with super()
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def describe(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def greet(self) -> None:
        print(f"Hello, I am {self.name}.")


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str) -> None:
        # Call the parent constructor
        super().__init__(name, age)
        self.student_id = student_id

    # Override describe() to include student-specific info
    def describe(self) -> str:
        base_description = super().describe()
        return f"{base_description}, Student(id={self.student_id})"

    # Override greet() with more specific behavior
    def greet(self) -> None:
        print(f"Hi, I'm student {self.name} with ID {self.student_id}.")


class GraduateStudent(Student):
    def __init__(self, name: str, age: int, student_id: str, thesis_title: str) -> None:
        # Multilevel inheritance: calls Student, which calls Person
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    # Further override describe()
    def describe(self) -> str:
        base_description = super().describe()
        return f"{base_description}, GraduateStudent(thesis='{self.thesis_title}')"


def main() -> None:
    # Base class instance
    person = Person("Alice", 40)
    print(person.describe())
    person.greet()
    print()

    # Single inheritance: Student is a Person
    student = Student("Bob", 20, "S12345")
    print(student.describe())  # uses overridden method
    student.greet()  # uses overridden greet()
    print()

    # Multilevel inheritance: GraduateStudent -> Student -> Person
    grad = GraduateStudent("Carol", 25, "G98765", "Machine Learning in Healthcare")
    print(grad.describe())
    grad.greet()  # inherits Student.greet()
    print()

    # isinstance / issubclass checks
    print("isinstance checks:")
    print("grad is Person:", isinstance(grad, Person))
    print("grad is Student:", isinstance(grad, Student))
    print("grad is GraduateStudent:", isinstance(grad, GraduateStudent))


if __name__ == "__main__":
    main()

