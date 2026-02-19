from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import re
from typing import Dict, List, Optional, Set


# =========================
# Interfaces (Python-style)
# =========================


class Identifiable(ABC):
    @abstractmethod
    def get_id(self) -> str: ...


class Chargeable(ABC):
    @abstractmethod
    def calculate_fees(self) -> float: ...


class AssignableToFlight(ABC):
    @abstractmethod
    def assign_to(self, flight: "Flight") -> None: ...


# =========================
# Exceptions
# =========================


class DomainError(RuntimeError):
    pass


class BookingError(DomainError):
    pass


class GateAssignmentError(DomainError):
    pass


class FlightStateError(DomainError):
    pass


# =========================
# Enums
# =========================


class FlightStatus(Enum):
    SCHEDULED = "SCHEDULED"
    DELAYED = "DELAYED"
    BOARDING = "BOARDING"
    DEPARTED = "DEPARTED"
    LANDED = "LANDED"
    CANCELLED = "CANCELLED"


class FareClass(Enum):
    ECONOMY = "ECONOMY"
    BUSINESS = "BUSINESS"


class LoyaltyStatus(Enum):
    NONE = "NONE"
    SILVER = "SILVER"
    GOLD = "GOLD"


# =========================
# Abstractions + Inheritance
# =========================


class Person(Identifiable, ABC):
    def __init__(self, person_id: str, full_name: str, email: str) -> None:
        self._id = _require_non_blank(person_id, "person_id")
        self.full_name = full_name
        self.email = email

    def get_id(self) -> str:
        return self._id

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        self._full_name = _require_non_blank(value, "full_name")

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = _require_non_blank(value, "email")

    @abstractmethod
    def role(self) -> str: ...

    def describe(self) -> str:
        # Polymorphic behavior: calls subclass role()
        return f"{self.role()}: {self.full_name} ({self.get_id()})"


class Passenger(Person):
    def __init__(self, person_id: str, full_name: str, email: str, loyalty_status: LoyaltyStatus) -> None:
        super().__init__(person_id, full_name, email)
        self.loyalty_status = loyalty_status or LoyaltyStatus.NONE

    def role(self) -> str:
        return f"Passenger({self.loyalty_status.value})"


class Employee(Person, AssignableToFlight, ABC):
    def __init__(self, person_id: str, full_name: str, email: str, employee_number: str) -> None:
        super().__init__(person_id, full_name, email)
        self._employee_number = _require_non_blank(employee_number, "employee_number")

    @property
    def employee_number(self) -> str:
        return self._employee_number


class Pilot(Employee):
    def __init__(self, person_id: str, full_name: str, email: str, employee_number: str, license_type: str) -> None:
        super().__init__(person_id, full_name, email, employee_number)
        self.license_type = _require_non_blank(license_type, "license_type")

    def role(self) -> str:
        return f"Pilot({self.license_type})"

    def assign_to(self, flight: "Flight") -> None:
        flight.assign_crew(self)


class FlightAttendant(Employee):
    def __init__(self, person_id: str, full_name: str, email: str, employee_number: str, level: str) -> None:
        super().__init__(person_id, full_name, email, employee_number)
        self.level = _require_non_blank(level, "level")

    def role(self) -> str:
        return f"FlightAttendant({self.level})"

    def assign_to(self, flight: "Flight") -> None:
        flight.assign_crew(self)


class GroundStaff(Employee):
    def __init__(self, person_id: str, full_name: str, email: str, employee_number: str, job_title: str) -> None:
        super().__init__(person_id, full_name, email, employee_number)
        self.job_title = _require_non_blank(job_title, "job_title")

    def role(self) -> str:
        return f"GroundStaff({self.job_title})"

    def assign_to(self, flight: "Flight") -> None:
        flight.assign_crew(self)


class Aircraft(ABC):
    def __init__(self, tail_number: str, model: str, capacity: int) -> None:
        self._tail_number = _require_non_blank(tail_number, "tail_number")
        self._model = _require_non_blank(model, "model")
        if capacity <= 0:
            raise DomainError("capacity must be > 0")
        self._capacity = capacity

    @property
    def tail_number(self) -> str:
        return self._tail_number

    @property
    def model(self) -> str:
        return self._model

    @property
    def capacity(self) -> int:
        return self._capacity

    @abstractmethod
    def max_baggage_kg_per_passenger(self) -> int: ...


class NarrowBodyAircraft(Aircraft):
    def max_baggage_kg_per_passenger(self) -> int:
        return 20


class WideBodyAircraft(Aircraft):
    def max_baggage_kg_per_passenger(self) -> int:
        return 30


# =========================
# Nested classes + Domain
# =========================


class Airport:
    class Terminal:
        def __init__(self, terminal_id: str) -> None:
            self.terminal_id = _require_non_blank(terminal_id, "terminal_id").upper()
            self._gates: Dict[str, "Airport.Terminal.Gate"] = {}

        class Gate:
            def __init__(self, terminal_id: str, code: str) -> None:
                self._terminal_id = terminal_id
                self._code = code

            @property
            def code(self) -> str:
                return self._code

            def __str__(self) -> str:
                return f"{self._terminal_id}-{self._code}"

        def add_gate(self, gate_code: str) -> None:
            code = _require_non_blank(gate_code, "gate_code").upper()
            self._gates[code] = Airport.Terminal.Gate(self.terminal_id, code)

        def find_gate(self, gate_code: str) -> Optional["Airport.Terminal.Gate"]:
            return self._gates.get(gate_code)

    def __init__(self, code: str, name: str, city: str) -> None:
        self.code = _require_non_blank(code, "code").upper()
        self.name = _require_non_blank(name, "name")
        self.city = _require_non_blank(city, "city")
        self._terminals: Dict[str, Airport.Terminal] = {}

    def add_terminal(self, terminal: "Airport.Terminal") -> None:
        self._terminals[terminal.terminal_id] = terminal

    def find_gate(self, gate_code: str) -> "Airport.Terminal.Gate":
        code = _require_non_blank(gate_code, "gate_code").upper()
        for terminal in self._terminals.values():
            found = terminal.find_gate(code)
            if found is not None:
                return found
        raise GateAssignmentError(f"Gate not found: {code} at airport {self.code}")

    def __str__(self) -> str:
        return f"{self.code} ({self.city})"


class Flight:
    class Manifest:
        _seat_re = re.compile(r"^[1-9][0-9]*[A-F]$")

        def __init__(self) -> None:
            self._seats: Set[str] = set()

        def validate_seat(self, seat: str) -> str:
            s = _require_non_blank(seat, "seat").upper()
            if not self._seat_re.match(s):
                raise BookingError(f"Invalid seat format: {seat} (expected like 12A)")
            return s

        def add_booking(self, capacity: int, booking: "Booking") -> None:
            seat = self.validate_seat(booking.seat)
            if len(self._seats) >= capacity:
                raise BookingError(f"Overbooking not allowed (capacity {capacity})")
            if seat in self._seats:
                raise BookingError(f"Seat already taken: {seat}")
            self._seats.add(seat)

    def __init__(
        self,
        flight_number: str,
        origin: Airport,
        destination: Airport,
        scheduled_departure: datetime,
        scheduled_arrival: datetime,
    ) -> None:
        self.flight_number = _require_non_blank(flight_number, "flight_number").upper()
        self.origin = origin
        self.destination = destination
        self.scheduled_departure = scheduled_departure
        self.scheduled_arrival = scheduled_arrival
        if scheduled_arrival < scheduled_departure:
            raise DomainError("scheduled_arrival must be after scheduled_departure")

        self.status = FlightStatus.SCHEDULED
        self.aircraft: Optional[Aircraft] = None
        self.departure_gate: Optional[Airport.Terminal.Gate] = None
        self.manifest = Flight.Manifest()
        self.crew: List[Employee] = []
        self.bookings: List["Booking"] = []

    def assign_aircraft(self, aircraft: Aircraft) -> None:
        self.aircraft = aircraft

    def assign_departure_gate(self, gate: Airport.Terminal.Gate) -> None:
        self.departure_gate = gate

    def cancel(self, reason: str) -> None:
        if self.status in (FlightStatus.DEPARTED, FlightStatus.LANDED):
            raise FlightStateError("Cannot cancel after departure/landing")
        self.status = FlightStatus.CANCELLED

    def assign_crew(self, employee: Employee) -> None:
        self.crew.append(employee)

    def add_booking(self, booking: "Booking") -> None:
        if self.status == FlightStatus.CANCELLED:
            raise BookingError(f"Cannot book a cancelled flight: {self.flight_number}")
        if self.aircraft is None:
            raise BookingError(f"Cannot book flight without assigned aircraft: {self.flight_number}")
        self.manifest.add_booking(self.aircraft.capacity, booking)
        self.bookings.append(booking)


@dataclass(frozen=True)
class Booking(Chargeable):
    booking_id: str
    passenger: Passenger
    flight: Flight
    seat: str
    fare_class: FareClass
    bags: int

    def __post_init__(self) -> None:
        if not self.booking_id or not self.booking_id.strip():
            raise BookingError("booking_id must not be blank")
        if self.bags < 0:
            raise BookingError("bags must be >= 0")

    def calculate_fees(self) -> float:
        base = 250.0 if self.fare_class == FareClass.BUSINESS else 120.0
        bag_fee = max(0, self.bags - 1) * 35.0
        discount = {
            LoyaltyStatus.GOLD: 0.15,
            LoyaltyStatus.SILVER: 0.05,
            LoyaltyStatus.NONE: 0.0,
        }[self.passenger.loyalty_status]
        subtotal = base + bag_fee
        return round(subtotal * (1.0 - discount), 2)


def _require_non_blank(value: str, field_name: str) -> str:
    if value is None or not str(value).strip():
        raise DomainError(f"{field_name} must not be blank")
    return str(value).strip()


def main() -> None:
    mia = Airport("MIA", "Metro International Airport", "Metro City")
    lax = Airport("LAX", "Pacific International Airport", "Coast City")

    terminal_a = Airport.Terminal("A")
    terminal_a.add_gate("A1")
    terminal_a.add_gate("A2")
    mia.add_terminal(terminal_a)

    terminal_b = Airport.Terminal("B")
    terminal_b.add_gate("B4")
    mia.add_terminal(terminal_b)

    a1 = NarrowBodyAircraft("N123NB", "Boeing 737", 2)
    a2 = WideBodyAircraft("N999WB", "Boeing 787", 250)

    p1 = Passenger("P001", "Alex Rivera", "alex@email.com", LoyaltyStatus.SILVER)
    p2 = Passenger("P002", "Jamie Chen", "jamie@email.com", LoyaltyStatus.NONE)
    p3 = Passenger("P003", "Taylor Singh", "taylor@email.com", LoyaltyStatus.GOLD)

    pilot = Pilot("E100", "Morgan Reed", "morgan@airport.gov", "EMP-100", "ATP")
    fa = FlightAttendant("E200", "Sam Patel", "sam@airport.gov", "EMP-200", "Senior")
    gs = GroundStaff("E300", "Riley Jones", "riley@airport.gov", "EMP-300", "Gate Agent")

    flight = Flight(
        "MI603",
        mia,
        lax,
        datetime(2026, 3, 1, 9, 30),
        datetime(2026, 3, 1, 12, 10),
    )
    flight.assign_aircraft(a1)
    flight.assign_departure_gate(mia.find_gate("A1"))

    for employee in (pilot, fa, gs):
        employee.assign_to(flight)

    # Polymorphism demo: treat as base type
    people: List[Person] = [p1, p2, p3, pilot, fa, gs]
    for person in people:
        print(person.describe())

    print()

    try:
        b1 = Booking("B001", p1, flight, "1A", FareClass.ECONOMY, 1)
        b2 = Booking("B002", p2, flight, "1B", FareClass.BUSINESS, 2)
        flight.add_booking(b1)
        flight.add_booking(b2)

        print("Fees:")
        print(f"{b1.booking_id} -> ${b1.calculate_fees()}")
        print(f"{b2.booking_id} -> ${b2.calculate_fees()}")

        # Overbooking exception (capacity is 2)
        b3 = Booking("B003", p3, flight, "2A", FareClass.ECONOMY, 0)
        flight.add_booking(b3)
    except DomainError as ex:
        print(f"Handled domain error: {ex}")

    print()

    try:
        flight.cancel("Weather")
        invalid = Booking("B004", p3, flight, "2A", FareClass.ECONOMY, 0)
        flight.add_booking(invalid)
    except DomainError as ex:
        print(f"Handled domain error: {ex}")

    try:
        _ = mia.find_gate("Z9")
    except DomainError as ex:
        print(f"Handled domain error: {ex}")

    print()
    print("Aircraft baggage rules:")
    for aircraft in (a1, a2):
        print(f"{aircraft.tail_number} ({aircraft.model}) -> {aircraft.max_baggage_kg_per_passenger()}kg per passenger")


if __name__ == "__main__":
    main()

