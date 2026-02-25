## IST601 – Extra Practice: Normalization & Relational Algebra

Use these questions to drill the same concepts that appear in the airline/hotel exam question.

---

### Part 1 – Functional Dependencies & Normalization

#### Question 1 – Course Registration (2NF / 3NF)

A university stores student registrations in a single relation:

`Registration(StudentID, StudentName, CourseID, CourseTitle, LecturerID, LecturerName, Semester, Grade)`

Assume the following functional dependencies hold:

1. `StudentID → StudentName`
2. `CourseID → CourseTitle, LecturerID`
3. `LecturerID → LecturerName`
4. `{StudentID, CourseID, Semester} → Grade`

Tasks:

1. **Identify all candidate keys** for `Registration` (show attribute closures).
2. Classify **each FD as full or partial** functional dependency with respect to any composite keys.
3. State whether `Registration` is in **1NF, 2NF, 3NF**. Justify carefully.
4. **Normalize to 3NF**, giving the resulting relation schemas and keys.

---

#### Question 2 – Online Orders (Transitive dependencies)

Consider the unnormalized relation:

`OrderLine(OrderID, OrderDate, CustomerID, CustomerName, CustomerCity, ProductID, ProductName, UnitPrice, Quantity)`

Assume:

1. `OrderID → OrderDate, CustomerID`
2. `CustomerID → CustomerName, CustomerCity`
3. `ProductID → ProductName, UnitPrice`
4. `{OrderID, ProductID} → Quantity`

Tasks:

1. Find all **candidate keys** of `OrderLine`.
2. Identify any **partial** and **transitive** dependencies.
3. Explain why the table is **not in 3NF**.
4. Produce a **3NF (or BCNF) decomposition**, listing each relation and its key.

---

#### Question 3 – Airline Re‑visit (Key analysis)

Re‑use the airline attributes from the solved question:

`FlightNumber, DepAirport, ArrAirport, FlightDate, PassportNumber, SeatNo, Price`

Add the additional (hypothetical) dependency:

5. `{FlightNumber, FlightDate, SeatNo} → PassportNumber`

Tasks:

1. With this *extra* FD, recompute all **candidate keys** of the relation.
2. Which attributes are **prime** now? Which are **non‑prime**?
3. List **all FDs that violate 3NF** under this new set.
4. Give a **3NF decomposition** that preserves dependencies and is lossless.

---

#### Question 4 – Supplier–Part Database

Relation:

`Supply(SupplierID, SupplierName, City, PartID, PartName, UnitCost, Category)`

Functional dependencies:

1. `SupplierID → SupplierName, City`
2. `PartID → PartName, Category`
3. `{SupplierID, PartID} → UnitCost`

Tasks:

1. Determine the **candidate key(s)** of `Supply`.
2. Is `Supply` in **2NF**? in **3NF**? Explain.
3. Carry out a **step‑by‑step normalization** to obtain a 3NF design.

---

### Part 2 – Relational Algebra Practice

Use the same hotel schema from the exam:

- `Hotel(hotelNo, hotelName, city)`  
- `Room(roomNo, hotelNo, type, price)`  
- `Booking(hotelNo, guestNo, dateFrom, dateTo, roomNo)`  
- `Guest(guestNo, guestName, guestAddress)`

Assume “Buea” is a city appearing in `Hotel.city` and in `guestAddress`.

#### Question 5 – Hotels and Rooms (Selections & Projections)

1. Write a relational algebra expression to return the **hotel numbers and names of all hotels in Buea**.  
2. Write an expression to return the **room numbers and prices of all rooms costing more than 25,000**, sorted by price is *not* part of relational algebra, so just focus on the relation content.  
3. Describe in words the result of:  
   \( \pi_{\text{roomNo}}(\sigma_{\text{type} = 'Single' \land \text{price} < 15000}(\text{Room})) \).

---

#### Question 6 – Joins Across Hotel / Room / Booking

1. Give a relational algebra expression that returns:  
   **hotelName, roomNo, type, price** for all rooms (in any city).  
2. Extend your expression so that it returns only rooms in **hotels located in Buea**.  
3. Write an expression that returns **guestName, hotelName, roomNo, dateFrom, dateTo** for all bookings (join across all four tables).

---

#### Question 7 – August Bookings

1. Using relational algebra, select all **bookings whose `dateFrom` is in August 2007**. Assume you can use conditions such as `dateFrom >= '2007-08-01' ∧ dateFrom < '2007-09-01'`.  
2. From those bookings, write an expression that returns only the **distinct guest numbers**.  
3. Combine your result with `Guest` to obtain **guest names** for all guests who have bookings in August 2007.

---

#### Question 8 – Set Operations

Assume we define two relations using selections:

- \( R_1 = \sigma_{\text{city} = 'Buea'}(\text{Hotel}) \)  
- \( R_2 = \sigma_{\text{city} = 'Douala'}(\text{Hotel}) \)

1. What does \( R_1 \cup R_2 \) represent?  
2. What does \( R_1 \cap R_2 \) represent? Under what circumstances could this intersection be non‑empty?  
3. What does \( R_1 - R_2 \) represent?

---

#### Question 9 – RA → SQL Translation

For each of the following relational algebra expressions, **write an equivalent SQL query**:

1. \( \pi_{\text{hotelName}}(\sigma_{\text{city} = 'Buea'}(\text{Hotel})) \)  
2. \( \pi_{\text{guestName}}(\sigma_{\text{guestAddress LIKE '%Buea%'}(\text{Guest})) \)  
3. \( \pi_{\text{hotelName}, \text{roomNo}}\big(\sigma_{\text{type} = 'Double'}(\text{Hotel} \bowtie \text{Room})\big) \)  
4. \( \pi_{\text{guestName}}\big(\sigma_{\text{dateFrom} \ge '2007-08-01' \land \text{dateFrom} < '2007-09-01'}(\text{Guest} \bowtie \text{Booking})\big) \)

---

### How to Use These Practice Questions

- **Step 1**: Do the functional‑dependency and normalization questions on paper *before* looking back at your worked example.  
- **Step 2**: For each relational algebra expression, sketch the pipeline: starting relation → selections → joins → projections.  
- **Step 3**: Try to convert your own RA expressions into SQL; then compare with the exam‑style SQL from `01_exam_question_3_solutions.md`.  
- **Step 4**: Time yourself (e.g., 25–30 minutes) per full problem set to simulate exam conditions.

