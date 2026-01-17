# Bus Station Management System (Case Study)
## Entity Relationship Diagram (ERD)

---

## 1. ERD Overview

The Entity Relationship Diagram (ERD) represents the data model of the Bus Station Management System, showing entities, their attributes, and relationships between them.

---

## 2. Entities and Attributes

### 2.1 Passenger Entity

**Entity:** Passenger

**Attributes:**
- PassengerID (PK) - Unique identifier for passenger
- FullName - Passenger's full name
- Email - Email address (unique)
- PhoneNumber - Contact phone number
- Address - Physical address
- City - City of residence
- State - State/Province
- Country - Country
- DateOfBirth - Date of birth
- IDNumber - Government ID number
- PasswordHash - Encrypted password
- EmailVerified - Boolean flag for email verification
- AccountStatus - Status (Active, Suspended, Inactive)
- CreatedDate - Account creation date
- LastLoginDate - Last login timestamp
- ProfilePicture - URL to profile picture (optional)

**Relationships:**
- Makes multiple Bookings (One-to-Many)
- Has multiple Tickets (One-to-Many)
- Receives multiple Payments (One-to-Many)

---

### 2.2 Staff Entity

**Entity:** Staff

**Attributes:**
- StaffID (PK) - Unique identifier for staff
- FullName - Staff member's full name
- Email - Email address (unique)
- PhoneNumber - Contact phone number
- Address - Physical address
- DateOfBirth - Date of birth
- EmploymentDate - Date of employment
- RoleID (FK) - Reference to Role entity
- DepartmentID (FK) - Reference to Department entity
- PasswordHash - Encrypted password
- AccountStatus - Status (Active, Suspended, Terminated)
- LicenseNumber - Driver's license number (for drivers)
- LicenseExpiryDate - License expiration date (for drivers)
- CreatedDate - Account creation date
- LastLoginDate - Last login timestamp

**Relationships:**
- Assigned to Role (Many-to-One)
- Belongs to Department (Many-to-One)
- Assigned to multiple Trips as Driver (One-to-Many)
- Creates multiple Bookings (One-to-Many)

---

### 2.3 Role Entity

**Entity:** Role

**Attributes:**
- RoleID (PK) - Unique identifier for role
- RoleName - Name of role (e.g., Admin, Manager, Driver, Ticketing Staff)
- Description - Role description
- Permissions - JSON or text field for permissions
- CreatedDate - Role creation date

**Relationships:**
- Assigned to multiple Staff members (One-to-Many)

---

### 2.4 Department Entity

**Entity:** Department

**Attributes:**
- DepartmentID (PK) - Unique identifier for department
- DepartmentName - Name of department (e.g., Operations, Maintenance, Administration)
- Description - Department description
- ManagerID (FK) - Reference to Staff (manager)
- CreatedDate - Department creation date

**Relationships:**
- Has multiple Staff members (One-to-Many)
- Managed by Staff (Many-to-One)

---

### 2.5 Bus Entity

**Entity:** Bus

**Attributes:**
- BusID (PK) - Unique identifier for bus
- LicensePlate - License plate number (unique)
- Model - Bus model
- Manufacturer - Bus manufacturer
- YearOfManufacture - Year of manufacture
- Capacity - Seating capacity
- BusTypeID (FK) - Reference to BusType entity
- Status - Current status (Active, Maintenance, Retired, Out of Service)
- RegistrationDate - Registration date
- InsuranceNumber - Insurance policy number
- InsuranceExpiryDate - Insurance expiration date
- LastMaintenanceDate - Date of last maintenance
- NextMaintenanceDate - Scheduled next maintenance date
- GPSDeviceID - GPS tracking device identifier
- CreatedDate - Bus registration date

**Relationships:**
- Belongs to BusType (Many-to-One)
- Assigned to multiple Trips (One-to-Many)
- Has multiple Maintenance records (One-to-Many)

---

### 2.6 BusType Entity

**Entity:** BusType

**Attributes:**
- BusTypeID (PK) - Unique identifier for bus type
- TypeName - Type name (Standard, Luxury, Express, Mini-bus)
- Description - Type description
- BaseFareMultiplier - Fare multiplier for pricing
- Amenities - List of amenities (JSON or text)
- CreatedDate - Type creation date

**Relationships:**
- Has multiple Buses (One-to-Many)

---

### 2.7 Route Entity

**Entity:** Route

**Attributes:**
- RouteID (PK) - Unique identifier for route
- RouteName - Name of route
- RouteCode - Route code (unique)
- OriginStationID (FK) - Reference to Station (origin)
- DestinationStationID (FK) - Reference to Station (destination)
- Distance - Total distance in kilometers
- EstimatedTravelTime - Estimated travel time in minutes
- RouteClassification - Classification (Local, Intercity, Interstate, International)
- Status - Route status (Active, Inactive, Suspended)
- BaseFare - Base fare for the route
- CreatedDate - Route creation date

**Relationships:**
- Has Origin Station (Many-to-One)
- Has Destination Station (Many-to-One)
- Has multiple RouteStops (One-to-Many)
- Has multiple Trips (One-to-Many)
- Has multiple Schedules (One-to-Many)

---

### 2.8 Station Entity

**Entity:** Station

**Attributes:**
- StationID (PK) - Unique identifier for station
- StationName - Name of station
- StationCode - Station code (unique)
- Address - Physical address
- City - City location
- State - State/Province
- Country - Country
- Latitude - GPS latitude coordinate
- Longitude - GPS longitude coordinate
- ContactNumber - Station contact number
- Facilities - Available facilities (JSON or text)
- Status - Station status (Active, Inactive)
- CreatedDate - Station creation date

**Relationships:**
- Serves as Origin for multiple Routes (One-to-Many)
- Serves as Destination for multiple Routes (One-to-Many)
- Included in multiple RouteStops (One-to-Many)

---

### 2.9 RouteStop Entity

**Entity:** RouteStop

**Attributes:**
- RouteStopID (PK) - Unique identifier for route stop
- RouteID (FK) - Reference to Route
- StationID (FK) - Reference to Station
- StopOrder - Order of stop in route (1, 2, 3, ...)
- DistanceFromOrigin - Distance from origin in kilometers
- EstimatedTimeFromOrigin - Estimated time from origin in minutes
- StopFare - Additional fare for this stop (if applicable)
- CreatedDate - Stop creation date

**Relationships:**
- Belongs to Route (Many-to-One)
- Located at Station (Many-to-One)

---

### 2.10 Trip Entity

**Entity:** Trip

**Attributes:**
- TripID (PK) - Unique identifier for trip
- TripNumber - Trip number (unique)
- RouteID (FK) - Reference to Route
- BusID (FK) - Reference to Bus
- DriverID (FK) - Reference to Staff (driver)
- DepartureDate - Departure date
- DepartureTime - Scheduled departure time
- ExpectedArrivalTime - Expected arrival time
- ActualDepartureTime - Actual departure time
- ActualArrivalTime - Actual arrival time
- Status - Trip status (Scheduled, In Progress, Completed, Cancelled, Delayed)
- TotalSeats - Total available seats
- BookedSeats - Number of booked seats
- AvailableSeats - Calculated available seats
- CurrentLocation - Current GPS location (latitude, longitude)
- ETA - Estimated time of arrival (calculated)
- DelayMinutes - Delay in minutes
- CreatedDate - Trip creation date
- UpdatedDate - Last update timestamp

**Relationships:**
- Follows Route (Many-to-One)
- Uses Bus (Many-to-One)
- Driven by Staff (Many-to-One)
- Has multiple Bookings (One-to-Many)

---

### 2.11 Schedule Entity

**Entity:** Schedule

**Attributes:**
- ScheduleID (PK) - Unique identifier for schedule
- RouteID (FK) - Reference to Route
- DepartureTime - Scheduled departure time
- Frequency - Frequency (Daily, Weekly, Specific Days)
- DaysOfWeek - Days of week (JSON or text)
- EffectiveDate - Schedule effective start date
- ExpiryDate - Schedule expiry date
- Status - Schedule status (Active, Inactive)
- CreatedDate - Schedule creation date

**Relationships:**
- Belongs to Route (Many-to-One)

---

### 2.12 Booking Entity

**Entity:** Booking

**Attributes:**
- BookingID (PK) - Unique identifier for booking
- BookingReference - Unique booking reference number
- PassengerID (FK) - Reference to Passenger
- TripID (FK) - Reference to Trip
- StaffID (FK) - Reference to Staff (who created booking, nullable)
- BookingDate - Date of booking
- BookingTime - Time of booking
- NumberOfPassengers - Number of passengers
- TotalFare - Total fare amount
- DiscountAmount - Discount applied
- FinalAmount - Final amount after discount
- PaymentStatus - Payment status (Pending, Paid, Refunded, Failed)
- BookingStatus - Booking status (Confirmed, Cancelled, Completed)
- CancellationDate - Date of cancellation (if cancelled)
- CancellationReason - Reason for cancellation
- SpecialRequests - Special requests or notes
- CreatedDate - Booking creation date
- UpdatedDate - Last update timestamp

**Relationships:**
- Made by Passenger (Many-to-One)
- For Trip (Many-to-One)
- Created by Staff (Many-to-One, optional)
- Has multiple Tickets (One-to-Many)
- Has Payment (One-to-One or One-to-Many)

---

### 2.13 Ticket Entity

**Entity:** Ticket

**Attributes:**
- TicketID (PK) - Unique identifier for ticket
- TicketNumber - Unique ticket number
- BookingID (FK) - Reference to Booking
- PassengerID (FK) - Reference to Passenger
- TripID (FK) - Reference to Trip
- SeatNumber - Assigned seat number (if applicable)
- QRCode - QR code data or image URL
- Barcode - Barcode data
- Status - Ticket status (Issued, Used, Cancelled, Expired)
- CheckInTime - Check-in timestamp
- BoardingTime - Boarding timestamp
- IssuedDate - Ticket issue date
- ExpiryDate - Ticket expiry date

**Relationships:**
- Belongs to Booking (Many-to-One)
- For Passenger (Many-to-One)
- For Trip (Many-to-One)

---

### 2.14 Payment Entity

**Entity:** Payment

**Attributes:**
- PaymentID (PK) - Unique identifier for payment
- BookingID (FK) - Reference to Booking
- PaymentMethod - Payment method (Cash, Card, Mobile Payment, Online)
- Amount - Payment amount
- TransactionID - External transaction ID from payment gateway
- PaymentGateway - Payment gateway used
- PaymentDate - Payment date and time
- PaymentStatus - Payment status (Pending, Completed, Failed, Refunded)
- PaymentGatewayResponse - Response from payment gateway (JSON)
- ReceiptNumber - Receipt number
- CreatedDate - Payment creation date

**Relationships:**
- For Booking (Many-to-One)
- Has Refund (One-to-Many, optional)

---

### 2.15 Refund Entity

**Entity:** Refund

**Attributes:**
- RefundID (PK) - Unique identifier for refund
- BookingID (FK) - Reference to Booking
- PaymentID (FK) - Reference to Payment
- RefundAmount - Refund amount
- RefundReason - Reason for refund
- RefundMethod - Refund method (Original Payment Method, Cash, Bank Transfer)
- RefundDate - Refund processing date
- RefundStatus - Refund status (Pending, Processed, Failed)
- TransactionID - Refund transaction ID
- ProcessedBy - Staff ID who processed refund (FK to Staff)
- CreatedDate - Refund request date
- ProcessedDate - Refund processing date

**Relationships:**
- For Booking (Many-to-One)
- For Payment (Many-to-One)
- Processed by Staff (Many-to-One)

---

### 2.16 Maintenance Entity

**Entity:** Maintenance

**Attributes:**
- MaintenanceID (PK) - Unique identifier for maintenance
- BusID (FK) - Reference to Bus
- MaintenanceType - Type of maintenance (Regular, Repair, Inspection, Emergency)
- ScheduledDate - Scheduled maintenance date
- CompletedDate - Actual completion date
- Cost - Maintenance cost
- Description - Maintenance description
- PartsReplaced - List of parts replaced (JSON or text)
- MaintenanceProvider - Service provider name
- ProviderContact - Service provider contact
- Status - Maintenance status (Scheduled, In Progress, Completed, Cancelled)
- NextMaintenanceDate - Next scheduled maintenance date
- MileageAtMaintenance - Bus mileage at maintenance
- CreatedDate - Maintenance record creation date
- UpdatedDate - Last update timestamp

**Relationships:**
- For Bus (Many-to-One)

---

## 3. Relationships

### 3.1 Relationship Types

#### One-to-Many (1:N) Relationships

1. **Passenger → Booking** (1:N)
   - One passenger can make multiple bookings
   - Foreign Key: Booking.PassengerID

2. **Passenger → Ticket** (1:N)
   - One passenger can have multiple tickets
   - Foreign Key: Ticket.PassengerID

3. **Staff → Trip** (1:N) [as Driver]
   - One driver can be assigned to multiple trips
   - Foreign Key: Trip.DriverID

4. **Staff → Booking** (1:N) [as Creator]
   - One staff member can create multiple bookings
   - Foreign Key: Booking.StaffID

5. **Role → Staff** (1:N)
   - One role can be assigned to multiple staff members
   - Foreign Key: Staff.RoleID

6. **Department → Staff** (1:N)
   - One department can have multiple staff members
   - Foreign Key: Staff.DepartmentID

7. **BusType → Bus** (1:N)
   - One bus type can have multiple buses
   - Foreign Key: Bus.BusTypeID

8. **Bus → Trip** (1:N)
   - One bus can be assigned to multiple trips
   - Foreign Key: Trip.BusID

9. **Bus → Maintenance** (1:N)
   - One bus can have multiple maintenance records
   - Foreign Key: Maintenance.BusID

10. **Route → Trip** (1:N)
    - One route can have multiple trips
    - Foreign Key: Trip.RouteID

11. **Route → Schedule** (1:N)
    - One route can have multiple schedules
    - Foreign Key: Schedule.RouteID

12. **Route → RouteStop** (1:N)
    - One route can have multiple stops
    - Foreign Key: RouteStop.RouteID

13. **Station → Route** (1:N) [as Origin]
    - One station can be origin for multiple routes
    - Foreign Key: Route.OriginStationID

14. **Station → Route** (1:N) [as Destination]
    - One station can be destination for multiple routes
    - Foreign Key: Route.DestinationStationID

15. **Station → RouteStop** (1:N)
    - One station can be included in multiple route stops
    - Foreign Key: RouteStop.StationID

16. **Booking → Ticket** (1:N)
    - One booking can have multiple tickets
    - Foreign Key: Ticket.BookingID

17. **Booking → Payment** (1:N)
    - One booking can have multiple payments (partial payments, refunds)
    - Foreign Key: Payment.BookingID

18. **Payment → Refund** (1:N)
    - One payment can have multiple refunds (partial refunds)
    - Foreign Key: Refund.PaymentID

19. **Trip → Booking** (1:N)
    - One trip can have multiple bookings
    - Foreign Key: Booking.TripID

20. **Trip → Ticket** (1:N)
    - One trip can have multiple tickets
    - Foreign Key: Ticket.TripID

#### Many-to-One (N:1) Relationships

All relationships listed above are bidirectional, so the reverse is Many-to-One.

#### One-to-One (1:1) Relationships

- **Booking ↔ Payment** (can be 1:1 if one payment per booking)
- **Department → Staff** (Manager relationship) - One department has one manager

---

## 4. ERD Diagram Description

### 4.1 Key Features

1. **Normalization**: All entities are normalized to at least 3NF
2. **Primary Keys**: All entities have unique primary keys
3. **Foreign Keys**: Relationships are properly defined with foreign keys
4. **Attributes**: All necessary attributes are included
5. **Cardinality**: Relationships show proper cardinality (1:1, 1:N, N:M)

### 4.2 Entity Groups

#### User Management Group
- Passenger
- Staff
- Role
- Department

#### Transportation Group
- Bus
- BusType
- Route
- Station
- RouteStop
- Trip
- Schedule

#### Booking and Payment Group
- Booking
- Ticket
- Payment
- Refund

#### Maintenance Group
- Maintenance
- Bus (linked)

---

## 5. Database Constraints

### 5.1 Primary Key Constraints

- All entities have a unique primary key
- Primary keys are auto-incrementing or generated

### 5.2 Foreign Key Constraints

- All foreign keys reference valid primary keys
- Cascade rules defined for deletions:
  - **CASCADE**: When parent is deleted, children are deleted
  - **SET NULL**: When parent is deleted, foreign key is set to NULL
  - **RESTRICT**: Prevent deletion if children exist

### 5.3 Unique Constraints

- Email addresses (Passenger, Staff)
- Phone numbers (where applicable)
- License plates (Bus)
- Booking references (Booking)
- Ticket numbers (Ticket)
- Station codes (Station)
- Route codes (Route)

### 5.4 Check Constraints

- Status fields have valid values
- Dates are valid (e.g., ExpiryDate > EffectiveDate)
- Amounts are non-negative
- Capacities are positive integers

---

## 6. Indexes

### 6.1 Primary Indexes

- All primary keys are automatically indexed

### 6.2 Foreign Key Indexes

- All foreign keys should be indexed for join performance

### 6.3 Additional Indexes

- Email addresses (for login lookups)
- Booking references (for quick lookups)
- Ticket numbers (for validation)
- Dates (for range queries)
- Status fields (for filtering)

---

## 7. ERD Implementation Notes

### 7.1 Database Design Considerations

1. **Data Types**: Choose appropriate data types for each attribute
2. **Nullability**: Define which fields can be NULL
3. **Defaults**: Set default values where appropriate
4. **Timestamps**: Include created/updated timestamps for audit trails

### 7.2 Performance Considerations

1. **Indexing**: Index frequently queried columns
2. **Partitioning**: Consider partitioning large tables (e.g., by date)
3. **Archiving**: Plan for archiving old data

### 7.3 Security Considerations

1. **Sensitive Data**: Encrypt sensitive fields (passwords, payment info)
2. **Access Control**: Implement row-level security if needed
3. **Audit Trails**: Maintain audit logs for critical operations

---

## 8. PlantUML ERD Code (Optional)

For visual representation, the ERD can be created using PlantUML, draw.io, or similar tools. The structure above provides all necessary information for creating the visual diagram.
