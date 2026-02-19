# Airport Management System - OOP Exercise (IST603)

Exam preparation project designed to explicitly demonstrate core OOP concepts in **Java** and **Python** using the same domain model.

## OOP Concepts Covered (and where to look)

- **Inheritance**: `Person → Passenger`, `Person → Employee → (Pilot, FlightAttendant, GroundStaff)`
- **Polymorphism**: common `describe()` / `role()` behavior overridden in subclasses; collections of base types calling overridden methods
- **Encapsulation**: private/protected state with validation via setters/constructors (Java) and properties (Python)
- **Abstraction**: abstract base classes (e.g., `Person`, `Employee`) define shared behavior + required overrides
- **Interfaces**: `Identifiable`, `Chargeable`, `AssignableToFlight` (Java interfaces; Python ABC “interface-like” base)
- **Exception handling**: custom domain exceptions (e.g., `BookingException`, `GateAssignmentException`) + try/catch/raise
- **Nested classes**: `Airport.Terminal` and `Terminal.Gate` (nested + inner), plus a nested `Flight.Manifest` helper

## Files

| File | Description |
|------|-------------|
| `01_scenario.md` | Story + domain entities (no code) |
| `02_requirements.md` | Functional requirements + constraints |
| `03_class_design.md` | Class list, responsibilities, and relationships |
| `04_uml_diagram.puml` | PlantUML class diagram |
| `05_java/` | Java implementation + runnable demo |
| `06_python/` | Python implementation + runnable demo |
| `07_practice_questions.md` | Exam-style prompts (design + code tracing + debugging) |

## How to run

### Java

From `exam_prep/IST603/airport_management/05_java`:

```bash
javac --release 21 -d out src/ist603/airport/Demo.java
java -cp out ist603.airport.Demo
```

### Python

From `exam_prep/IST603/airport_management/06_python`:

```bash
python demo.py
```

