# Bus Station Management System (Case Study)
## Data Flow Diagrams (DFD)

---

## 1. Context Diagram (Level 0 DFD)

### 1.1 Overview

The Context Diagram represents the entire Bus Station Management System as a single process, showing all external entities that interact with the system and the data flows between them.

### 1.2 External Entities

1. **Passenger**
   - Individual travelers who book tickets and travel
   
2. **Staff**
   - Station employees including ticketing staff, drivers, and administrators
   
3. **Payment Gateway**
   - External payment processing service
   
4. **GPS Service**
   - External GPS tracking service for bus location
   
5. **Communication Service**
   - External SMS and email service providers
   
6. **Management**
   - Station managers and administrators
   
7. **Maintenance Provider**
   - External maintenance service providers

### 1.3 Data Flows

#### Passenger ↔ System
- **Input to System:**
  - Registration Information
  - Login Credentials
  - Booking Request
  - Payment Information
  - Cancellation Request
  - Profile Update Request

- **Output from System:**
  - Booking Confirmation
  - Ticket
  - Payment Receipt
  - Booking Status
  - Trip Information
  - Notifications

#### Staff ↔ System
- **Input to System:**
  - Staff Login Credentials
  - Booking Creation Request
  - Trip Management Request
  - Bus Management Request
  - Report Request
  - System Configuration

- **Output from System:**
  - Booking Information
  - Trip Details
  - Bus Status
  - Reports
  - System Status
  - Notifications

#### Payment Gateway ↔ System
- **Input to System:**
  - Payment Confirmation
  - Payment Status
  - Refund Confirmation

- **Output from System:**
  - Payment Request
  - Refund Request
  - Payment Verification

#### GPS Service ↔ System
- **Input to System:**
  - Bus Location Data
  - Route Information

- **Output from System:**
  - Location Request
  - Tracking Request

#### Communication Service ↔ System
- **Input to System:**
  - Delivery Status
  - Service Status

- **Output from System:**
  - SMS Request
  - Email Request
  - Notification Request

#### Management ↔ System
- **Input to System:**
  - Report Request
  - Configuration Changes
  - Policy Updates

- **Output from System:**
  - Management Reports
  - Analytics
  - System Status
  - Performance Metrics

#### Maintenance Provider ↔ System
- **Input to System:**
  - Maintenance Completion Report
  - Maintenance Cost Information

- **Output from System:**
  - Maintenance Schedule
  - Maintenance Request
  - Bus Information

---

## 2. Level 1 DFD

### 2.1 Major Processes

The Level 1 DFD decomposes the system into major processes:

1. **1.0 User Management**
   - Handles passenger and staff registration, authentication, and profile management

2. **2.0 Booking Management**
   - Manages ticket booking, modification, and cancellation processes

3. **3.0 Payment Processing**
   - Handles payment transactions and refund processing

4. **4.0 Trip Management**
   - Manages trip creation, scheduling, tracking, and completion

5. **5.0 Bus and Route Management**
   - Manages bus registration, route management, and maintenance

6. **6.0 Reporting and Analytics**
   - Generates operational, financial, and analytical reports

### 2.2 Data Stores

1. **D1: Passenger Database**
   - Stores passenger information, accounts, and profiles

2. **D2: Staff Database**
   - Stores staff information, roles, and permissions

3. **D3: Booking Database**
   - Stores booking records and ticket information

4. **D4: Payment Database**
   - Stores payment and refund transaction records

5. **D5: Trip Database**
   - Stores trip information, schedules, and status

6. **D6: Bus Database**
   - Stores bus information, status, and maintenance records

7. **D7: Route Database**
   - Stores route information, stations, and schedules

8. **D8: Report Database**
   - Stores generated reports and analytics data

### 2.3 Process Details

#### Process 1.0: User Management

**Inputs:**
- Registration Information (from Passenger)
- Login Credentials (from Passenger, Staff)
- Profile Update Request (from Passenger, Staff)

**Outputs:**
- Account Confirmation (to Passenger, Staff)
- Authentication Result (to Passenger, Staff)
- Profile Information (to Passenger, Staff)

**Data Stores:**
- D1: Passenger Database (read/write)
- D2: Staff Database (read/write)

**Sub-processes:**
- 1.1: Passenger Registration
- 1.2: Staff Registration
- 1.3: User Authentication
- 1.4: Profile Management

#### Process 2.0: Booking Management

**Inputs:**
- Booking Request (from Passenger, Staff)
- Booking Modification Request (from Passenger, Staff)
- Cancellation Request (from Passenger, Staff)

**Outputs:**
- Booking Confirmation (to Passenger, Staff)
- Ticket (to Passenger)
- Booking Status (to Passenger, Staff)

**Data Stores:**
- D3: Booking Database (read/write)
- D5: Trip Database (read)
- D1: Passenger Database (read)

**Sub-processes:**
- 2.1: Booking Creation
- 2.2: Booking Modification
- 2.3: Booking Cancellation
- 2.4: Ticket Generation

#### Process 3.0: Payment Processing

**Inputs:**
- Payment Request (from Process 2.0)
- Refund Request (from Process 2.0)
- Payment Confirmation (from Payment Gateway)

**Outputs:**
- Payment Receipt (to Passenger)
- Refund Confirmation (to Passenger)
- Payment Status (to Process 2.0)

**Data Stores:**
- D4: Payment Database (read/write)
- D3: Booking Database (read/write)

**Sub-processes:**
- 3.1: Payment Transaction
- 3.2: Refund Processing
- 3.3: Payment Verification

#### Process 4.0: Trip Management

**Inputs:**
- Trip Creation Request (from Staff)
- GPS Location Data (from GPS Service)
- Trip Status Update (from Staff)

**Outputs:**
- Trip Schedule (to Staff, Passenger)
- Trip Status (to Staff, Passenger)
- Location Updates (to Passenger)
- Notifications (to Communication Service)

**Data Stores:**
- D5: Trip Database (read/write)
- D6: Bus Database (read)
- D7: Route Database (read)
- D2: Staff Database (read)

**Sub-processes:**
- 4.1: Trip Creation
- 4.2: Trip Scheduling
- 4.3: Trip Tracking
- 4.4: Trip Completion

#### Process 5.0: Bus and Route Management

**Inputs:**
- Bus Registration Request (from Staff)
- Route Creation Request (from Staff)
- Maintenance Request (from Staff)
- Maintenance Completion (from Maintenance Provider)

**Outputs:**
- Bus Information (to Staff)
- Route Information (to Staff, Passenger)
- Maintenance Schedule (to Staff, Maintenance Provider)
- Bus Status (to Staff)

**Data Stores:**
- D6: Bus Database (read/write)
- D7: Route Database (read/write)

**Sub-processes:**
- 5.1: Bus Registration
- 5.2: Route Management
- 5.3: Maintenance Scheduling
- 5.4: Maintenance Tracking

#### Process 6.0: Reporting and Analytics

**Inputs:**
- Report Request (from Staff, Management)
- Data from various databases

**Outputs:**
- Operational Reports (to Staff, Management)
- Financial Reports (to Management)
- Analytics Reports (to Management)

**Data Stores:**
- D8: Report Database (read/write)
- D3: Booking Database (read)
- D4: Payment Database (read)
- D5: Trip Database (read)
- D6: Bus Database (read)

**Sub-processes:**
- 6.1: Data Aggregation
- 6.2: Report Generation
- 6.3: Analytics Processing

---

## 3. Level 2 DFD - Booking Management (Detailed)

### 3.1 Process 2.0 Decomposition

#### Process 2.1: Booking Creation

**Inputs:**
- Route Selection (from Passenger)
- Date and Time Selection (from Passenger)
- Passenger Information (from Passenger)
- Seat Selection (from Passenger)

**Outputs:**
- Booking Details (to Process 2.4)
- Payment Request (to Process 3.0)
- Availability Check Result (to Passenger)

**Data Stores:**
- D3: Booking Database (write)
- D5: Trip Database (read)
- D7: Route Database (read)

**Steps:**
1. Validate route and date selection
2. Check trip availability
3. Check seat availability
4. Calculate fare
5. Create booking record
6. Generate booking reference
7. Request payment

#### Process 2.2: Booking Modification

**Inputs:**
- Booking Reference (from Passenger)
- Modification Request (from Passenger)
- New Date/Time (from Passenger)

**Outputs:**
- Updated Booking (to Passenger)
- Fare Difference (to Process 3.0)
- Modification Confirmation (to Passenger)

**Data Stores:**
- D3: Booking Database (read/write)
- D5: Trip Database (read)

**Steps:**
1. Retrieve booking record
2. Verify modification eligibility
3. Check new trip availability
4. Calculate fare difference
5. Update booking record
6. Process payment adjustment

#### Process 2.3: Booking Cancellation

**Inputs:**
- Booking Reference (from Passenger)
- Cancellation Request (from Passenger)

**Outputs:**
- Cancellation Confirmation (to Passenger)
- Refund Request (to Process 3.0)
- Seat Release (to D5)

**Data Stores:**
- D3: Booking Database (read/write)
- D5: Trip Database (read/write)

**Steps:**
1. Retrieve booking record
2. Verify cancellation eligibility
3. Calculate refund amount
4. Update booking status
5. Release seats
6. Request refund

#### Process 2.4: Ticket Generation

**Inputs:**
- Booking Confirmation (from Process 2.1)
- Payment Confirmation (from Process 3.0)

**Outputs:**
- Ticket (to Passenger)
- Ticket Information (to D3)

**Data Stores:**
- D3: Booking Database (read/write)

**Steps:**
1. Verify payment completion
2. Generate ticket number
3. Generate QR code
4. Create ticket record
5. Send ticket to passenger

---

## 4. Level 2 DFD - Payment Processing (Detailed)

### 4.1 Process 3.0 Decomposition

#### Process 3.1: Payment Transaction

**Inputs:**
- Payment Request (from Process 2.0)
- Payment Method (from Passenger)
- Payment Amount (from Process 2.0)

**Outputs:**
- Payment Request (to Payment Gateway)
- Payment Status (to Process 2.0)
- Payment Receipt (to Passenger)

**Data Stores:**
- D4: Payment Database (write)

**Steps:**
1. Validate payment information
2. Process payment through gateway
3. Record payment transaction
4. Update booking payment status
5. Generate payment receipt

#### Process 3.2: Refund Processing

**Inputs:**
- Refund Request (from Process 2.0)
- Refund Amount (from Process 2.0)
- Original Payment Information (from D4)

**Outputs:**
- Refund Request (to Payment Gateway)
- Refund Confirmation (to Passenger)
- Refund Status (to Process 2.0)

**Data Stores:**
- D4: Payment Database (read/write)

**Steps:**
1. Retrieve original payment record
2. Verify refund eligibility
3. Process refund through gateway
4. Record refund transaction
5. Update booking status
6. Generate refund receipt

#### Process 3.3: Payment Verification

**Inputs:**
- Payment Confirmation (from Payment Gateway)
- Transaction ID (from Payment Gateway)

**Outputs:**
- Payment Verification Result (to Process 2.0)
- Payment Status Update (to D4)

**Data Stores:**
- D4: Payment Database (read/write)

**Steps:**
1. Receive payment gateway callback
2. Verify transaction
3. Update payment status
4. Confirm booking
5. Trigger ticket generation

---

## 5. Data Flow Diagram Notations

### 5.1 Symbols Used

- **Process (Circle/Bubble)**: Represents a process that transforms data
  - Labeled with verb phrases (e.g., "Create Booking", "Process Payment")
  - Numbered hierarchically (1.0, 2.0, 2.1, 2.2, etc.)

- **Data Store (Open Rectangle)**: Represents data storage
  - Labeled with noun phrases (e.g., "Passenger Database", "Booking Database")
  - Numbered (D1, D2, D3, etc.)

- **External Entity (Square/Rectangle)**: Represents external entities
  - Labeled with noun phrases (e.g., "Passenger", "Staff", "Payment Gateway")

- **Data Flow (Arrow)**: Represents data movement
  - Labeled with noun phrases describing the data (e.g., "Booking Request", "Payment Confirmation")
  - Shows direction of data flow

### 5.2 Data Flow Rules

1. **Data flows must have names** describing the data being transferred
2. **Processes must have inputs and outputs** - data cannot be created or destroyed
3. **Data stores must be accessed** through processes, not directly by external entities
4. **External entities** cannot communicate directly with each other
5. **Data flows** are unidirectional

---

## 6. Additional DFD Levels (If Needed)

### 6.1 Level 3 DFD

For complex processes, further decomposition can be done:
- **Process 2.1.1**: Route Validation
- **Process 2.1.2**: Availability Checking
- **Process 2.1.3**: Fare Calculation
- **Process 2.1.4**: Booking Record Creation

### 6.2 Process Decomposition Guidelines

- Decompose processes that are too complex
- Maintain data flow consistency across levels
- Ensure all inputs and outputs are accounted for
- Keep decomposition to 3-4 levels maximum for clarity

---

## 7. DFD Validation

### 7.1 Consistency Checks

- **Balancing**: All data flows at one level must appear at the next level
- **Naming**: Consistent naming conventions throughout
- **Completeness**: All processes have inputs and outputs
- **Clarity**: Diagrams are readable and not overcrowded

### 7.2 Common Errors to Avoid

- Data flows without names
- Processes without outputs
- External entities communicating directly
- Missing data stores
- Unbalanced data flows between levels
