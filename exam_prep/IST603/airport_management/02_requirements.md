# Airport Management System - Requirements (IST603)

## Functional requirements

1. **Create airport structure**
   - Create an `Airport` with one or more `Terminal`s.
   - Each terminal has one or more `Gate`s.

2. **Register aircraft**
   - Add aircraft to the system (tail number, model, capacity).
   - Support at least two aircraft types with different behavior (for polymorphism).

3. **Manage people**
   - Create passengers and employees (pilot, flight attendant, ground staff).
   - Enforce basic validation (e.g., IDs not blank, capacity positive).

4. **Schedule flights**
   - Create flights with origin/destination airports and scheduled times.
   - Assign an aircraft to a flight.
   - Assign a departure gate to a flight (must exist in a terminal).

5. **Book seats**
   - A passenger can create a booking for a flight with a seat code (e.g., 12A).
   - Prevent overbooking (cannot exceed aircraft capacity).
   - Validate seat codes (simple rule is fine: row number + letter).

6. **Handle operational exceptions**
   - Throw/raise domain-specific exceptions for invalid operations:
     - booking a cancelled flight
     - assigning a non-existent gate
     - overbooking

7. **Demonstrate nested classes**
   - Use at least one nested class to model airport structure (Terminal/Gate) or flight structure (Manifest/Segment).

## Non-functional constraints

- Provide implementations in **both Java and Python**.
- Keep the project runnable from the command line without external dependencies.
- Code should clearly demonstrate:
  - inheritance, polymorphism, encapsulation, abstraction
  - interfaces (Java) / ABC “interface-like” constructs (Python)
  - exception handling
  - nested classes

