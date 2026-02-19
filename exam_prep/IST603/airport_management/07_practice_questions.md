# IST603 Exam Prep - Airport Management (Practice Questions)

## Design / UML-to-code

1. **Inheritance**: Draw a small hierarchy for `Person → (Passenger, Employee)` and `Employee → (Pilot, FlightAttendant, GroundStaff)`. Which fields belong in `Person` vs `Employee` and why?
2. **Abstraction**: Why should `Aircraft` be abstract? Name two methods/properties that should be common to all aircraft and one that should vary by subclass.
3. **Interfaces**: Create an interface for “can be charged fees”. Which classes should implement it in this system and why?
4. **Encapsulation**: List three fields that must not be publicly mutable. Show how you would validate them in Java and Python.

## Polymorphism (explain output)

5. You have `List<Person> people` containing `Passenger`, `Pilot`, and `GroundStaff`. If you call `describe()` on each, which implementation runs? Explain dynamic dispatch.
6. You store `Aircraft` references to both `NarrowBodyAircraft` and `WideBodyAircraft`. You call `maxBaggageKgPerPassenger()`. Why does the return value differ?

## Exception handling

7. In what situations should the system throw/raise:
   - `BookingException/BookingError`
   - `GateAssignmentException/GateAssignmentError`
   - `FlightStateException/FlightStateError`
8. Show a try/catch (Java) or try/except (Python) around “create booking → add booking”, and explain what the program should do when capacity is exceeded.

## Nested classes

9. Why might `Terminal` and `Gate` be modeled as nested classes inside `Airport`? Give two benefits and one downside.
10. In Java, what’s the difference between a **static nested** class and an **inner** class? Which one is `Airport.Terminal` vs `Terminal.Gate` and why?

## Debugging / code tracing

11. A student reports: “I can add two bookings but the third booking throws an error even though there are 200 seats.” List two likely causes in the code.
12. Seat format validation rejects `01A`. Is that correct according to your validation rule? How would you change the rule to allow it?
13. A booking for seat `12A` is added twice without error. Where is the bug? What structure should track seat uniqueness?

## Small coding prompts

14. Add a new employee subtype `SecurityOfficer` and ensure it works with polymorphic `describe()` and `assignTo/assign_to`.
15. Add a new fare class `PREMIUM_ECONOMY` with a different base price and show how fees are computed for it.
16. Add a method `delay(minutes)` on `Flight` that changes the status and logs a reason; enforce invalid transitions with exceptions.

