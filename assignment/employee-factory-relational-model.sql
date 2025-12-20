-- ============================================
-- RELATIONAL MODEL FOR EMPLOYEE-FACTORY SYSTEM
-- ============================================
-- Derived from ER Diagram using Crow's Feet Notation
-- ============================================

-- Entity: employee
CREATE TABLE employee (
    ID VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(100),
    pay_rate DECIMAL(10,2),
    pay_type VARCHAR(50),
    supervisor_ID VARCHAR(50),  -- Foreign key for recursive relationship
    factory_city VARCHAR(100),  -- Foreign key for works_at relationship
    manager_ID VARCHAR(50),     -- Foreign key for manages relationship (1:1)
    
    -- Foreign key constraints
    CONSTRAINT fk_employee_supervisor 
        FOREIGN KEY (supervisor_ID) 
        REFERENCES employee(ID) 
        ON DELETE SET NULL 
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_employee_factory 
        FOREIGN KEY (factory_city) 
        REFERENCES factory(city) 
        ON DELETE RESTRICT 
        ON UPDATE CASCADE,
    
    CONSTRAINT fk_employee_manager 
        FOREIGN KEY (manager_ID) 
        REFERENCES employee(ID) 
        ON DELETE SET NULL 
        ON UPDATE CASCADE,
    
    -- Unique constraint for 1:1 manages relationship
    CONSTRAINT uk_employee_manager 
        UNIQUE (manager_ID)
);

-- Entity: factory
CREATE TABLE factory (
    city VARCHAR(100) PRIMARY KEY,
    -- throughput is derived, not stored
    -- Can be calculated as needed
);

-- Indexes for performance
CREATE INDEX idx_employee_supervisor ON employee(supervisor_ID);
CREATE INDEX idx_employee_factory ON employee(factory_city);
CREATE INDEX idx_employee_manager ON employee(manager_ID);

-- ============================================
-- NOTES ON RELATIONAL MODEL:
-- ============================================
-- 1. Recursive Relationship (supervises):
--    - Implemented via supervisor_ID foreign key
--    - Self-referencing: employee.ID -> employee.supervisor_ID
--    - Cardinality: 1:N (one supervisor can supervise many employees)
--
-- 2. Works At Relationship (N:1):
--    - Implemented via factory_city foreign key in employee table
--    - Many employees can work at one factory
--    - Participation: Total for employee (every employee works at a factory)
--
-- 3. Manages Relationship (1:1):
--    - Implemented via manager_ID foreign key in employee table
--    - Unique constraint ensures one employee manages one factory
--    - One factory is managed by one employee
--    - manager_ID can be NULL if factory has no manager assigned
--
-- 4. Derived Attribute:
--    - throughput in factory is not stored
--    - Should be calculated as needed (e.g., via views or computed columns)

