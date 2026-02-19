# Airport Management System - Scenario (IST603)

## Story

Metro International Airport wants a lightweight airport management system used for training new software engineers. The system should model common airport operations while clearly showcasing object-oriented programming concepts.

The airport manages:

**Airports and terminals**
- Each airport has a unique code (e.g., “MIA”), a name, and a city.
- Each airport contains multiple terminals.
- Each terminal contains multiple gates (e.g., A1, A2, B4).

**Aircraft**
- Each aircraft has a unique tail number, a model name, and a seating capacity.
- Different aircraft types may have different operational rules (e.g., max baggage weight).

**People**
- Every person has a unique ID, full name, and contact info.
- **Passengers** can book seats on flights and may have loyalty status.
- **Employees** work for the airport and have employee IDs and roles:
  - **Pilots** (flight crew)
  - **Flight attendants** (flight crew)
  - **Ground staff** (gate agents / baggage / operations)

**Flights**
- Each flight has a flight number, an origin airport, a destination airport, and scheduled departure/arrival times.
- A flight is assigned an aircraft and a gate for departure.
- Flights can be scheduled, delayed, boarding, departed, landed, or cancelled.

**Bookings**
- A booking represents a passenger reserving a seat on a flight.
- Bookings include seat assignment, fare class (Economy/Business), and optional baggage count.

## Notes for Design (important for the exercise)

- The scenario intentionally describes **entities and attributes**, but does not fully define the relationships.
- Your job is to **discover and formalize relationships** during class design and UML work (e.g., “What needs to reference what to satisfy the requirements?”).

