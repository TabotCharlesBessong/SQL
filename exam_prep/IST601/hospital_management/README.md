# Hospital Management System - Database Exercise

Complete database design exercise demonstrating complex inter-entity relationships.

## Design Process Flow

1. **Scenario** → Describes entities and their attributes (no relationships defined)
2. **Entity Identification** → Lists all entities and attributes
3. **ER Diagram** → **Relationships are discovered here** by analyzing what information needs to be linked
4. **Relational Schema** → Relationships are formalized with foreign keys
5. **SQL Implementation** → Tables created with proper constraints
6. **Normalization** → Verify schema is in BCNF

## Key Features

- **9 entities** with multiple relationship types
- **Direct relationships:** DOCTOR→DEPARTMENT, NURSE→DEPARTMENT, DEPARTMENT→DOCTOR (head)
- **Multiple junction tables:** APPOINTMENT, ADMISSION, TREATMENT, PRESCRIPTION
- **Complex network:** Entities relate to multiple other entities through different paths

## Files

| File | Description |
|------|-------------|
| `01_scenario.md` | Hospital management scenario |
| `02_entities_and_attributes.md` | 9 entities identified |
| `03_er_diagram.md` | ER diagram (text, Mermaid, PlantUML) |
| `03_er_diagram.puml` | Standalone PlantUML file |
| `04_relational_schema.md` | Relational schema and FDs |
| `05_create_tables.sql` | CREATE TABLE statements |
| `06_insert_data.sql` | Sample data (5 patients, 5 doctors, 5 nurses, 4 departments, etc.) |
| `07_normalization_process.md` | 1NF → BCNF normalization analysis |
| `README.md` | This file |

## Relationship Types

1. **Many-to-One:** DOCTOR→DEPARTMENT, NURSE→DEPARTMENT
2. **One-to-One:** DEPARTMENT→DOCTOR (head doctor)
3. **Many-to-Many (via junction):**
   - PATIENT ↔ DOCTOR (via APPOINTMENT, ADMISSION, TREATMENT, PRESCRIPTION)
   - PATIENT ↔ DEPARTMENT (via ADMISSION)
   - PATIENT ↔ MEDICATION (via PRESCRIPTION)
   - DOCTOR ↔ MEDICATION (via PRESCRIPTION)

## Usage

1. **Read scenario** (`01_scenario.md`) - Describes entities and attributes only (no relationships)
2. **Identify entities** (`02_entities_and_attributes.md`) - Lists entities and their attributes
3. **Design ER diagram** (`03_er_diagram.md`) - **This is where relationships are discovered and defined** based on what information needs to be linked
4. **Create relational schema** (`04_relational_schema.md`) - Formalizes relationships with foreign keys
5. **Execute SQL** (`05_create_tables.sql`) - Note: Department references Doctor, so order matters
6. **Insert data** (`06_insert_data.sql`)
7. **Study normalization** (`07_normalization_process.md`) - Verify 1NF → BCNF
