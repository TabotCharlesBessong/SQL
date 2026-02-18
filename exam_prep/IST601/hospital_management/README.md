# Hospital Management System - Database Exercise

Complete database design exercise demonstrating complex inter-entity relationships.

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

1. Read scenario and entities
2. Review ER diagram (shows complex relationships)
3. Execute `05_create_tables.sql` (note: Department references Doctor, so order matters)
4. Execute `06_insert_data.sql`
5. Study normalization analysis
