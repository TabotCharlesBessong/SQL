# Airport Management System - Class Design Notes (IST603)

This is the “answer key” style design guide used to implement both Java and Python versions consistently.

## Core classes

### `Airport` (aggregate root)
- **State**: `code`, `name`, `city`, list/map of terminals
- **Behavior**: add terminal, find gate by code (`A1`, `B4`)
- **Nested classes**
  - `Terminal` (static nested)
    - state: terminal id/name, gates
    - behavior: add/find gate
    - `Gate` (inner class)
      - state: gate code, allowed aircraft size/category (optional)

### `Aircraft` (abstraction)
- **Abstract**: tail number, model, capacity
- **Polymorphism**: subclasses implement `maxBaggageKgPerPassenger()` or `category()`
  - `NarrowBodyAircraft`
  - `WideBodyAircraft`

### `Person` (abstraction)
- **Abstract**: id, name, contact info
- **Polymorphism**: `role()` / `describe()`
  - `Passenger`
  - `Employee` (abstract)
    - `Pilot`
    - `FlightAttendant`
    - `GroundStaff`

### `Flight`
- **State**: flight number, origin, destination, times, status, aircraft, departure gate
- **Behavior**: assign aircraft, assign gate, cancel, board, add booking
- **Nested helper**: `Manifest` (static nested) responsible for seat uniqueness + capacity rules

### `Booking`
- **State**: booking id, passenger, flight, seat, fare class, bags
- **Behavior**: compute total fees (interface-driven)

## Interfaces (Java) / ABC “interfaces” (Python)

- `Identifiable`: `getId()`
- `Chargeable`: `calculateFees()`
- `AssignableToFlight`: `assignTo(Flight flight)` for crew members

## Exceptions

- `DomainException` (base)
  - `BookingException` (invalid booking operations)
  - `GateAssignmentException` (bad gate / gate unavailable)
  - `FlightStateException` (invalid status transitions)

## Status modeling

- Use an enum (Java) / Enum (Python) for `FlightStatus`:
  - `SCHEDULED`, `DELAYED`, `BOARDING`, `DEPARTED`, `LANDED`, `CANCELLED`

