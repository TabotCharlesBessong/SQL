

package ist603.airport;

import java.time.LocalDateTime;
import java.util.*;
import java.util.regex.Pattern;

public class Air {
    public static void main(String[] args) {
        Airport mia = new Airport("MIA", "Metro International Airport", "Metro City");
        Airport lax = new Airport("LAX", "Pacific International Airport", "Coast City");

        Airport.Terminal terminalA = new Airport.Terminal("A");
        terminalA.addGate("A1");
        terminalA.addGate("A2");
        mia.addTerminal(terminalA);

        Airport.Terminal terminalB = new Airport.Terminal("B");
        terminalB.addGate("B4");
        mia.addTerminal(terminalB);

        Aircraft a1 = new NarrowBodyAircraft("N123NB", "Boeing 737", 2);
        Aircraft a2 = new WideBodyAircraft("N999WB", "Boeing 787", 250);

        Passenger p1 = new Passenger("P001", "Alex Rivera", "alex@email.com", LoyaltyStatus.SILVER);
        Passenger p2 = new Passenger("P002", "Jamie Chen", "jamie@email.com", LoyaltyStatus.NONE);
        Passenger p3 = new Passenger("P003", "Taylor Singh", "taylor@email.com", LoyaltyStatus.GOLD);

        Pilot pilot = new Pilot("E100", "Morgan Reed", "morgan@airport.gov", "EMP-100", "ATP");
        FlightAttendant fa = new FlightAttendant("E200", "Sam Patel", "sam@airport.gov", "EMP-200", "Senior");
        GroundStaff gs = new GroundStaff("E300", "Riley Jones", "riley@airport.gov", "EMP-300", "Gate Agent");

        Flight flight = new Flight("MI603", mia, lax,
                LocalDateTime.of(2026, 3, 1, 9, 30),
                LocalDateTime.of(2026, 3, 1, 12, 10));

        flight.assignAircraft(a1);
        flight.assignDepartureGate(mia.findGate("A1"));

        pilot.assignTo(flight);
        fa.assignTo(flight);
        gs.assignTo(flight);

        // Polymorphism demo: treat as base type
        List<Person> people = List.of(p1, p2, p3, pilot, fa, gs);
        for (Person person : people) {
            System.out.println(person.describe());
        }

        System.out.println();

        try {
            Booking b1 = Booking.create("B001", p1, flight, "1A", FareClass.ECONOMY, 1);
            Booking b2 = Booking.create("B002", p2, flight, "1B", FareClass.BUSINESS, 2);
            flight.addBooking(b1);
            flight.addBooking(b2);

            System.out.println("Fees:");
            System.out.println(b1.getBookingId() + " -> $" + b1.calculateFees());
            System.out.println(b2.getBookingId() + " -> $" + b2.calculateFees());

            // Overbooking exception (capacity is 2)
            Booking b3 = Booking.create("B003", p3, flight, "2A", FareClass.ECONOMY, 0);
            flight.addBooking(b3);
        } catch (DomainException ex) {
            System.out.println("Handled domain error: " + ex.getMessage());
        }

        System.out.println();

        // Flight state exception demo
        try {
            flight.cancel("Weather");
            Booking invalid = Booking.create("B004", p3, flight, "2A", FareClass.ECONOMY, 0);
            flight.addBooking(invalid);
        } catch (DomainException ex) {
            System.out.println("Handled domain error: " + ex.getMessage());
        }

        // Gate assignment exception demo
        try {
            flight.assignDepartureGate(mia.findGate("Z9"));
        } catch (DomainException ex) {
            System.out.println("Handled domain error: " + ex.getMessage());
        }

        // Extra polymorphism: different aircraft behavior
        System.out.println();
        System.out.println("Aircraft baggage rules:");
        for (Aircraft aircraft : List.of(a1, a2)) {
            System.out.println(aircraft.getTailNumber() + " (" + aircraft.getModel() + ") -> " +
                    aircraft.maxBaggageKgPerPassenger() + "kg per passenger");
        }
    }
}

// =========================
// Interfaces
// =========================

interface Identifiable {
    String getId();
}

interface Chargeable {
    double calculateFees();
}

interface AssignableToFlight {
    void assignTo(Flight flight);
}

// =========================
// Exceptions
// =========================

class DomainException extends RuntimeException {
    public DomainException(String message) {
        super(message);
    }
}

class BookingException extends DomainException {
    public BookingException(String message) {
        super(message);
    }
}

class GateAssignmentException extends DomainException {
    public GateAssignmentException(String message) {
        super(message);
    }
}

class FlightStateException extends DomainException {
    public FlightStateException(String message) {
        super(message);
    }
}

// =========================
// Enums
// =========================

enum FlightStatus {
    SCHEDULED, DELAYED, BOARDING, DEPARTED, LANDED, CANCELLED
}

enum FareClass {
    ECONOMY, BUSINESS
}

enum LoyaltyStatus {
    NONE, SILVER, GOLD
}

// =========================
// Abstractions + Inheritance
// =========================

abstract class Person implements Identifiable {
    private final String id;
    private String fullName;
    private String email;

    protected Person(String id, String fullName, String email) {
        this.id = requireNonBlank(id, "id");
        this.fullName = requireNonBlank(fullName, "fullName");
        this.email = requireNonBlank(email, "email");
    }

    @Override
    public String getId() {
        return id;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = requireNonBlank(fullName, "fullName");
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = requireNonBlank(email, "email");
    }

    public abstract String role();

    // Polymorphic behavior: subclasses can override, but this calls role()
    public String describe() {
        return role() + ": " + fullName + " (" + id + ")";
    }

    protected static String requireNonBlank(String value, String fieldName) {
        if (value == null || value.trim().isEmpty()) {
            throw new DomainException(fieldName + " must not be blank");
        }
        return value.trim();
    }
}

class Passenger extends Person {
    private LoyaltyStatus loyaltyStatus;

    public Passenger(String id, String fullName, String email, LoyaltyStatus loyaltyStatus) {
        super(id, fullName, email);
        this.loyaltyStatus = Objects.requireNonNullElse(loyaltyStatus, LoyaltyStatus.NONE);
    }

    public LoyaltyStatus getLoyaltyStatus() {
        return loyaltyStatus;
    }

    public void setLoyaltyStatus(LoyaltyStatus loyaltyStatus) {
        this.loyaltyStatus = Objects.requireNonNullElse(loyaltyStatus, LoyaltyStatus.NONE);
    }

    @Override
    public String role() {
        return "Passenger(" + loyaltyStatus + ")";
    }
}

abstract class Employee extends Person implements AssignableToFlight {
    private final String employeeNumber;

    protected Employee(String id, String fullName, String email, String employeeNumber) {
        super(id, fullName, email);
        this.employeeNumber = requireNonBlank(employeeNumber, "employeeNumber");
    }

    public String getEmployeeNumber() {
        return employeeNumber;
    }
}

class Pilot extends Employee {
    private final String licenseType;

    public Pilot(String id, String fullName, String email, String employeeNumber, String licenseType) {
        super(id, fullName, email, employeeNumber);
        this.licenseType = requireNonBlank(licenseType, "licenseType");
    }

    @Override
    public String role() {
        return "Pilot(" + licenseType + ")";
    }

    @Override
    public void assignTo(Flight flight) {
        Objects.requireNonNull(flight, "flight");
        flight.assignCrew(this);
    }
}

class FlightAttendant extends Employee {
    private final String level;

    public FlightAttendant(String id, String fullName, String email, String employeeNumber, String level) {
        super(id, fullName, email, employeeNumber);
        this.level = requireNonBlank(level, "level");
    }

    @Override
    public String role() {
        return "FlightAttendant(" + level + ")";
    }

    @Override
    public void assignTo(Flight flight) {
        Objects.requireNonNull(flight, "flight");
        flight.assignCrew(this);
    }
}

class GroundStaff extends Employee {
    private final String jobTitle;

    public GroundStaff(String id, String fullName, String email, String employeeNumber, String jobTitle) {
        super(id, fullName, email, employeeNumber);
        this.jobTitle = requireNonBlank(jobTitle, "jobTitle");
    }

    @Override
    public String role() {
        return "GroundStaff(" + jobTitle + ")";
    }

    @Override
    public void assignTo(Flight flight) {
        Objects.requireNonNull(flight, "flight");
        flight.assignCrew(this);
    }
}

abstract class Aircraft {
    private final String tailNumber;
    private final String model;
    private final int capacity;

    protected Aircraft(String tailNumber, String model, int capacity) {
        this.tailNumber = Person.requireNonBlank(tailNumber, "tailNumber");
        this.model = Person.requireNonBlank(model, "model");
        if (capacity <= 0) {
            throw new DomainException("capacity must be > 0");
        }
        this.capacity = capacity;
    }

    public String getTailNumber() {
        return tailNumber;
    }

    public String getModel() {
        return model;
    }

    public int getCapacity() {
        return capacity;
    }

    public abstract int maxBaggageKgPerPassenger();
}

class NarrowBodyAircraft extends Aircraft {
    public NarrowBodyAircraft(String tailNumber, String model, int capacity) {
        super(tailNumber, model, capacity);
    }

    @Override
    public int maxBaggageKgPerPassenger() {
        return 20;
    }
}

class WideBodyAircraft extends Aircraft {
    public WideBodyAircraft(String tailNumber, String model, int capacity) {
        super(tailNumber, model, capacity);
    }

    @Override
    public int maxBaggageKgPerPassenger() {
        return 30;
    }
}

// =========================
// Nested classes + Domain
// =========================

class Airport {
    private final String code;
    private final String name;
    private final String city;
    private final Map<String, Terminal> terminals = new LinkedHashMap<>();

    public Airport(String code, String name, String city) {
        this.code = Person.requireNonBlank(code, "code").toUpperCase(Locale.ROOT);
        this.name = Person.requireNonBlank(name, "name");
        this.city = Person.requireNonBlank(city, "city");
    }

    public String getCode() {
        return code;
    }

    public void addTerminal(Terminal terminal) {
        Objects.requireNonNull(terminal, "terminal");
        terminals.put(terminal.getTerminalId(), terminal);
    }

    public Terminal.Gate findGate(String gateCode) {
        String normalized = Person.requireNonBlank(gateCode, "gateCode").toUpperCase(Locale.ROOT);
        for (Terminal terminal : terminals.values()) {
            Terminal.Gate found = terminal.findGate(normalized);
            if (found != null) return found;
        }
        throw new GateAssignmentException("Gate not found: " + normalized + " at airport " + code);
    }

    public static class Terminal {
        private final String terminalId;
        private final Map<String, Gate> gates = new LinkedHashMap<>();

        public Terminal(String terminalId) {
            this.terminalId = Person.requireNonBlank(terminalId, "terminalId").toUpperCase(Locale.ROOT);
        }

        public String getTerminalId() {
            return terminalId;
        }

        public void addGate(String gateCode) {
            Gate gate = new Gate(Person.requireNonBlank(gateCode, "gateCode").toUpperCase(Locale.ROOT));
            gates.put(gate.getCode(), gate);
        }

        public Gate findGate(String gateCode) {
            return gates.get(gateCode);
        }

        public class Gate {
            private final String code;

            private Gate(String code) {
                this.code = code;
            }

            public String getCode() {
                return code;
            }

            @Override
            public String toString() {
                return terminalId + "-" + code;
            }
        }
    }

    @Override
    public String toString() {
        return code + " (" + city + ")";
    }
}

class Flight {
    private final String flightNumber;
    private final Airport origin;
    private final Airport destination;
    private final LocalDateTime scheduledDeparture;
    private final LocalDateTime scheduledArrival;

    private FlightStatus status = FlightStatus.SCHEDULED;
    private Aircraft aircraft;
    private Airport.Terminal.Gate departureGate;
    private final Manifest manifest = new Manifest();
    private final List<Employee> crew = new ArrayList<>();

    public Flight(String flightNumber, Airport origin, Airport destination,
                  LocalDateTime scheduledDeparture, LocalDateTime scheduledArrival) {
        this.flightNumber = Person.requireNonBlank(flightNumber, "flightNumber").toUpperCase(Locale.ROOT);
        this.origin = Objects.requireNonNull(origin, "origin");
        this.destination = Objects.requireNonNull(destination, "destination");
        this.scheduledDeparture = Objects.requireNonNull(scheduledDeparture, "scheduledDeparture");
        this.scheduledArrival = Objects.requireNonNull(scheduledArrival, "scheduledArrival");
        if (scheduledArrival.isBefore(scheduledDeparture)) {
            throw new DomainException("scheduledArrival must be after scheduledDeparture");
        }
    }

    public String getFlightNumber() {
        return flightNumber;
    }

    public FlightStatus getStatus() {
        return status;
    }

    public void assignAircraft(Aircraft aircraft) {
        this.aircraft = Objects.requireNonNull(aircraft, "aircraft");
    }

    public void assignDepartureGate(Airport.Terminal.Gate gate) {
        this.departureGate = Objects.requireNonNull(gate, "gate");
    }

    public void cancel(String reason) {
        if (status == FlightStatus.DEPARTED || status == FlightStatus.LANDED) {
            throw new FlightStateException("Cannot cancel after departure/landing");
        }
        status = FlightStatus.CANCELLED;
    }

    public void assignCrew(Employee employee) {
        Objects.requireNonNull(employee, "employee");
        crew.add(employee);
    }

    public void addBooking(Booking booking) {
        Objects.requireNonNull(booking, "booking");
        if (status == FlightStatus.CANCELLED) {
            throw new BookingException("Cannot book a cancelled flight: " + flightNumber);
        }
        if (aircraft == null) {
            throw new BookingException("Cannot book flight without assigned aircraft: " + flightNumber);
        }
        manifest.addBooking(aircraft.getCapacity(), booking);
    }

    public static class Manifest {
        private static final Pattern SEAT_PATTERN = Pattern.compile("^[1-9][0-9]*[A-F]$");
        private final Set<String> seats = new HashSet<>();

        public void addBooking(int capacity, Booking booking) {
            validateSeat(booking.getSeat());
            if (seats.size() >= capacity) {
                throw new BookingException("Overbooking not allowed (capacity " + capacity + ")");
            }
            if (!seats.add(booking.getSeat())) {
                throw new BookingException("Seat already taken: " + booking.getSeat());
            }
        }

        public void validateSeat(String seat) {
            String normalized = Person.requireNonBlank(seat, "seat").toUpperCase(Locale.ROOT);
            if (!SEAT_PATTERN.matcher(normalized).matches()) {
                throw new BookingException("Invalid seat format: " + seat + " (expected like 12A)");
            }
        }
    }
}

class Booking implements Chargeable {
    private final String bookingId;
    private final Passenger passenger;
    private final Flight flight;
    private final String seat;
    private final FareClass fareClass;
    private final int bags;

    private Booking(String bookingId, Passenger passenger, Flight flight, String seat, FareClass fareClass, int bags) {
        this.bookingId = Person.requireNonBlank(bookingId, "bookingId");
        this.passenger = Objects.requireNonNull(passenger, "passenger");
        this.flight = Objects.requireNonNull(flight, "flight");
        this.seat = Person.requireNonBlank(seat, "seat").toUpperCase(Locale.ROOT);
        this.fareClass = Objects.requireNonNull(fareClass, "fareClass");
        if (bags < 0) {
            throw new BookingException("bags must be >= 0");
        }
        this.bags = bags;
    }

    public static Booking create(String bookingId, Passenger passenger, Flight flight, String seat, FareClass fareClass, int bags) {
        return new Booking(bookingId, passenger, flight, seat, fareClass, bags);
    }

    public String getBookingId() {
        return bookingId;
    }

    public String getSeat() {
        return seat;
    }

    @Override
    public double calculateFees() {
        double base = (fareClass == FareClass.BUSINESS) ? 250.0 : 120.0;
        double bagFee = Math.max(0, bags - 1) * 35.0;
        double loyaltyDiscount = switch (passenger.getLoyaltyStatus()) {
            case GOLD -> 0.15;
            case SILVER -> 0.05;
            default -> 0.0;
        };
        double subtotal = base + bagFee;
        return Math.round((subtotal * (1.0 - loyaltyDiscount)) * 100.0) / 100.0;
    }
}
