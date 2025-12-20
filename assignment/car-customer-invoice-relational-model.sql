-- ============================================
-- RELATIONAL MODEL FOR CAR-CUSTOMER-EMPLOYEE-INVOICE SYSTEM
-- ============================================
-- Converted from ER Diagram with M:N relationships
-- ============================================

-- Entity: CAR
CREATE TABLE CAR (
    Car_ID VARCHAR(50) PRIMARY KEY,
    Serial_Number VARCHAR(100) UNIQUE,
    Model_No VARCHAR(100),
    Model VARCHAR(100),
    Color VARCHAR(50),
    Year INTEGER
);

-- Entity: CUSTOMER
CREATE TABLE CUSTOMER (
    CustomerID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(50),
    Address VARCHAR(255),
    Country VARCHAR(100),
    City VARCHAR(100)
);

-- Entity: EMPLOYEE
CREATE TABLE EMPLOYEE (
    EmpID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Qualification VARCHAR(100)
);

-- Entity: INVOICE
CREATE TABLE INVOICE (
    InvoiceID VARCHAR(50) PRIMARY KEY,
    Date DATE NOT NULL
);

-- ============================================
-- INTERSECTION TABLES FOR M:N RELATIONSHIPS
-- ============================================

-- M:N Relationship: CAR has CUSTOMER
-- A car can be associated with zero or more customers
-- A customer can be associated with one or more cars
CREATE TABLE CAR_CUSTOMER (
    Car_ID VARCHAR(50),
    CustomerID VARCHAR(50),
    PRIMARY KEY (Car_ID, CustomerID),
    
    CONSTRAINT fk_car_customer_car 
        FOREIGN KEY (Car_ID) 
        REFERENCES CAR(Car_ID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_car_customer_customer 
        FOREIGN KEY (CustomerID) 
        REFERENCES CUSTOMER(CustomerID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- M:N Relationship: CAR Sell EMPLOYEE
-- Many cars can be sold by many employees
CREATE TABLE CAR_EMPLOYEE (
    Car_ID VARCHAR(50),
    EmpID VARCHAR(50),
    SaleDate DATE,  -- Optional: additional attribute for the relationship
    PRIMARY KEY (Car_ID, EmpID),
    
    CONSTRAINT fk_car_employee_car 
        FOREIGN KEY (Car_ID) 
        REFERENCES CAR(Car_ID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_car_employee_employee 
        FOREIGN KEY (EmpID) 
        REFERENCES EMPLOYEE(EmpID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- M:N Relationship: CUSTOMER has INVOICE
-- Many customers can have many invoices
-- Many invoices can belong to many customers
CREATE TABLE CUSTOMER_INVOICE (
    CustomerID VARCHAR(50),
    InvoiceID VARCHAR(50),
    PRIMARY KEY (CustomerID, InvoiceID),
    
    CONSTRAINT fk_customer_invoice_customer 
        FOREIGN KEY (CustomerID) 
        REFERENCES CUSTOMER(CustomerID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_customer_invoice_invoice 
        FOREIGN KEY (InvoiceID) 
        REFERENCES INVOICE(InvoiceID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- M:N Relationship: EMPLOYEE has INVOICE
-- Many employees can be associated with many invoices
-- Many invoices can be associated with many employees
CREATE TABLE EMPLOYEE_INVOICE (
    EmpID VARCHAR(50),
    InvoiceID VARCHAR(50),
    PRIMARY KEY (EmpID, InvoiceID),
    
    CONSTRAINT fk_employee_invoice_employee 
        FOREIGN KEY (EmpID) 
        REFERENCES EMPLOYEE(EmpID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_employee_invoice_invoice 
        FOREIGN KEY (InvoiceID) 
        REFERENCES INVOICE(InvoiceID) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- ============================================
-- INDEXES FOR PERFORMANCE
-- ============================================
CREATE INDEX idx_car_serial ON CAR(Serial_Number);
CREATE INDEX idx_customer_name ON CUSTOMER(Name);
CREATE INDEX idx_employee_name ON EMPLOYEE(Name);
CREATE INDEX idx_invoice_date ON INVOICE(Date);

CREATE INDEX idx_car_customer_car ON CAR_CUSTOMER(Car_ID);
CREATE INDEX idx_car_customer_customer ON CAR_CUSTOMER(CustomerID);
CREATE INDEX idx_car_employee_car ON CAR_EMPLOYEE(Car_ID);
CREATE INDEX idx_car_employee_employee ON CAR_EMPLOYEE(EmpID);
CREATE INDEX idx_customer_invoice_customer ON CUSTOMER_INVOICE(CustomerID);
CREATE INDEX idx_customer_invoice_invoice ON CUSTOMER_INVOICE(InvoiceID);
CREATE INDEX idx_employee_invoice_employee ON EMPLOYEE_INVOICE(EmpID);
CREATE INDEX idx_employee_invoice_invoice ON EMPLOYEE_INVOICE(InvoiceID);

-- ============================================
-- NOTES ON RELATIONAL MODEL:
-- ============================================
-- 1. All M:N relationships have been converted to intersection tables:
--    - CAR_CUSTOMER: Links cars to customers (M:N)
--    - CAR_EMPLOYEE: Links cars to employees who sold them (M:N)
--    - CUSTOMER_INVOICE: Links customers to invoices (M:N)
--    - EMPLOYEE_INVOICE: Links employees to invoices (M:N)
--
-- 2. Primary keys in intersection tables are composite keys
--    consisting of the foreign keys from both related entities.
--
-- 3. All foreign keys have CASCADE options for DELETE and UPDATE
--    to maintain referential integrity.
--
-- 4. Additional attributes can be added to intersection tables
--    if needed (e.g., SaleDate in CAR_EMPLOYEE).

