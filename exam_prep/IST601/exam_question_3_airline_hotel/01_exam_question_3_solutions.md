## IST601 – Exam Question 3 (Airline & Hotel Schema) – Worked Solutions

This file contains detailed, step‑by‑step solutions for the exam question in your photo.

---

### a) Functional dependency concepts

Let \(R\) be a relation with attributes \(A\) and \(B\).

1. **Functional dependency \(A \rightarrow B\)**  
   In any valid instance of \(R\), if two tuples have the same value for attribute(s) \(A\), then they must also have the same value for attribute(s) \(B\).  
   Equivalently: **\(A\) functionally determines \(B\)**; the value of \(A\) uniquely identifies the value of \(B\).

2. **Full functional dependency**  
   \(A \rightarrow B\) is a *full* functional dependency if:
   - \(B\) is functionally dependent on all of \(A\), **and**
   - \(B\) is **not** functionally dependent on any *proper subset* of \(A\).  
   This mainly matters when \(A\) is a composite (multi‑attribute) determinant – every attribute in \(A\) is needed to determine \(B\).

3. **Partial functional dependency**  
   \(A \rightarrow B\) is a *partial* functional dependency if:
   - \(B\) is functionally dependent on \(A\), **but**
   - \(B\) is also functionally dependent on some *proper subset* of \(A\).  
   Partial dependencies typically occur when a non‑key attribute depends on only part of a composite key (violates 2NF).

---

### b) Airline flights schema – keys, 3NF check, and 3NF decomposition

Attributes in relation \(U\):  
`FlightNumber`, `DepAirport`, `ArrAirport`, `FlightDate`, `PassportNumber`, `SeatNo`, `Price`

Given functional dependencies (FDs):

1. \( \{\text{FlightNumber}, \text{FlightDate}\} \rightarrow \{\text{DepAirport}, \text{ArrAirport}\} \)
2. \( \{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}\} \rightarrow \{\text{SeatNo}\} \)
3. \( \{\text{FlightNumber}, \text{SeatNo}\} \rightarrow \{\text{Price}\} \)

#### b.i) Find all keys for \(U\)

Let \(K = \{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}\}\).

Compute \(K^+\) (attribute closure using the given FDs):

- Start: \(K^+ = \{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}\}\)
- Using FD (1): add `DepAirport`, `ArrAirport`  
  \(K^+ = \{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}, \text{DepAirport}, \text{ArrAirport}\}\)
- Using FD (2): from `FlightNumber`, `FlightDate`, `PassportNumber` add `SeatNo`  
  \(K^+ = \{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}, \text{DepAirport}, \text{ArrAirport}, \text{SeatNo}\}\)
- Using FD (3): from `FlightNumber`, `SeatNo` add `Price`  
  \(K^+ = \{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}, \text{DepAirport}, \text{ArrAirport}, \text{SeatNo}, \text{Price}\}\)

Thus \(K^+\) contains **all seven attributes**, so \(K\) is a **superkey**.

Check minimality (is any proper subset of \(K\) a key?):

- \(\{\text{FlightNumber}, \text{FlightDate}\}^+\) gives `DepAirport`, `ArrAirport` only → **not** a key.
- \(\{\text{FlightNumber}, \text{PassportNumber}\}^+\) gives just those two → **not** a key.
- \(\{\text{FlightDate}, \text{PassportNumber}\}^+\) gives just those two → **not** a key.

No proper subset of \(K\) is a superkey, so \(K\) is a **candidate key**.

**All keys of \(U\):**

- **Candidate key:** \(\{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}\}\)

No other candidate keys are implied by the given FDs (for example, \(\{\text{FlightNumber}, \text{FlightDate}, \text{SeatNo}\}\) does *not* determine `PassportNumber`, so it is not a key).

Prime attributes (appear in some candidate key):  
`FlightNumber`, `FlightDate`, `PassportNumber`  
Non‑prime attributes: `DepAirport`, `ArrAirport`, `SeatNo`, `Price`

#### b.ii) 3NF check for each FD in \(U\)

Recall 3NF condition for each FD \(X \rightarrow A\) in a relation schema \(R\):  
For every such FD, at least one of the following must hold:

1. \(A \in X\) (trivial FD), or  
2. \(X\) is a superkey of \(R\), or  
3. Every attribute in \(A\) is a **prime** attribute (part of some candidate key).

Check each FD:

1. **FD (1):** \(\{\text{FlightNumber}, \text{FlightDate}\} \rightarrow \{\text{DepAirport}, \text{ArrAirport}\}\)
   - LHS is **not** a superkey (its closure does not contain all attributes).
   - RHS attributes `DepAirport`, `ArrAirport` are **non‑prime**.
   - FD is non‑trivial.  
   ⇒ **Violates 3NF**.

2. **FD (2):** \(\{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}\} \rightarrow \{\text{SeatNo}\}\)
   - LHS is the **candidate key** of \(U\), so it is a superkey.  
   ⇒ **Satisfies 3NF**.

3. **FD (3):** \(\{\text{FlightNumber}, \text{SeatNo}\} \rightarrow \{\text{Price}\}\)
   - LHS is **not** a superkey (its closure does not include all attributes).
   - RHS attribute `Price` is **non‑prime**.  
   ⇒ **Violates 3NF**.

Since some FDs violate the 3NF conditions, **schema \(U\) is not in 3NF**.

#### b.iii) 3NF decomposition of \(U\)

Use the standard 3NF synthesis (one relation per FD, then ensure a key is present):

- From FD (1): \(R_1(\text{FlightNumber}, \text{FlightDate}, \text{DepAirport}, \text{ArrAirport})\)
- From FD (2): \(R_2(\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}, \text{SeatNo})\)
- From FD (3): \(R_3(\text{FlightNumber}, \text{SeatNo}, \text{Price})\)

Check:

- The union of attributes of \(R_1, R_2, R_3\) is exactly the set of attributes in \(U\).
- `FlightNumber`, `FlightDate`, `PassportNumber` (a key for \(U\)) is contained in relation \(R_2\), so a key for \(U\) appears in the decomposition.
- Each relation is in 3NF:
  - In \(R_1\), key is \(\{\text{FlightNumber}, \text{FlightDate}\}\); non‑key attributes depend fully on the key.
  - In \(R_2\), key is \(\{\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}\}\); `SeatNo` depends on that key.
  - In \(R_3\), key is \(\{\text{FlightNumber}, \text{SeatNo}\}\); `Price` depends on that key.

**A valid 3NF decomposition:**

- \(R_1(\text{FlightNumber}, \text{FlightDate}, \text{DepAirport}, \text{ArrAirport})\)
- \(R_2(\text{FlightNumber}, \text{FlightDate}, \text{PassportNumber}, \text{SeatNo})\)
- \(R_3(\text{FlightNumber}, \text{SeatNo}, \text{Price})\)

---

### c) Relational algebra – describing the resulting relations

Schema:

- `Hotel(hotelNo, hotelName, city)` – hotel details  
- `Room(roomNo, hotelNo, type, price)` – room details  
- `Booking(hotelNo, guestNo, dateFrom, dateTo, roomNo)` – booking details  
- `Guest(guestNo, guestName, guestAddress)` – guest details

The exact symbols on your paper are a bit hard to read, but the following interpretations match the usual style of this question and the later SQL parts.

1. **\( \pi_{\text{roomNo}}(\sigma_{\text{price} \ge 80}(\text{Room})) \)**  
   - Start from `Room`, keep only rows where `price >= 80`.  
   - Then project just the `roomNo` column.  
   - **Result:** *A relation containing a single attribute `roomNo`, listing the room numbers of all rooms that cost at least 80 per night.*

2. **\( \pi_{\text{hotelName}, \text{roomNo}, \text{type}, \text{price}}\big(\sigma_{\text{city}='Buea'}(\text{Hotel} \bowtie \text{Room})\big) \)**  
   - Perform a natural join of `Hotel` and `Room` on `hotelNo`.  
   - Select only the tuples where `city = 'Buea'`.  
   - Project the attributes `hotelName`, `roomNo`, `type`, `price`.  
   - **Result:** *A relation listing hotel name, room number, room type, and price for every room in hotels located in Buea.*

3. **\( \text{Guest} \bowtie_{\text{Guest.guestNo}=\text{Booking.guestNo}} \text{Booking} \)**  
   - Join `Guest` and `Booking` on matching `guestNo`.  
   - **Result:** *A relation that combines each guest with all of their bookings (each tuple contains both guest and booking attributes).*

4. **\( \text{Guest} \bowtie_{\substack{\text{Guest.guestNo}=\text{Booking.guestNo}\\ \land\ \text{dateFrom in August}}} \text{Booking} \)**  
   - Same join as (3) but restricted to bookings whose `dateFrom` lies in August (e.g., between `1-Aug-2007` and `31-Aug-2007`).  
   - **Result:** *A relation giving guest and booking details for bookings made for the month of August only.*

> Even if the exact selection predicates in your printout differ slightly, the description technique above is what the examiner looks for: **start relation → selection conditions → join conditions → projection (final attributes).**

---

### d) SQL queries

Use the same schemas as in part (c).

#### d.i) Simple queries

1. **List full details of all hotels in Buea**

```sql
SELECT *
FROM Hotel
WHERE city = 'Buea';
```

2. **List the names and addresses of all guests living in Buea, alphabetically ordered by name**

(Assuming `guestAddress` contains the city name.)

```sql
SELECT guestName, guestAddress
FROM Guest
WHERE guestAddress LIKE '%Buea%'
ORDER BY guestName ASC;
```

3. **List all double or family rooms with a price below 20,000 per night, in descending order of price**

```sql
SELECT roomNo, hotelNo, type, price
FROM Room
WHERE type IN ('Double', 'Family')
  AND price < 20000
ORDER BY price DESC;
```

#### d.ii) Aggregate functions

1. **How many hotels are there?**

```sql
SELECT COUNT(*) AS numHotels
FROM Hotel;
```

2. **What is the total revenue per night from all double rooms?**

Interpretation: sum of the per‑night price of every double room.

```sql
SELECT SUM(price) AS totalRevenuePerNight
FROM Room
WHERE type = 'Double';
```

3. **How many different guests have made bookings for August?**

(Assuming “August 2007”; adjust dates as needed for your exam.)

```sql
SELECT COUNT(DISTINCT guestNo) AS numGuestsForAugust
FROM Booking
WHERE dateFrom >= DATE '2007-08-01'
  AND dateFrom <  DATE '2007-09-01';
```

#### d.iii) Grouping

1. **List the number of rooms in each hotel**

```sql
SELECT h.hotelNo,
       h.hotelName,
       COUNT(r.roomNo) AS numRooms
FROM Hotel AS h
JOIN Room  AS r ON h.hotelNo = r.hotelNo
GROUP BY h.hotelNo, h.hotelName;
```

2. **List the number of rooms in each hotel in Buea**

```sql
SELECT h.hotelNo,
       h.hotelName,
       COUNT(r.roomNo) AS numRooms
FROM Hotel AS h
JOIN Room  AS r ON h.hotelNo = r.hotelNo
WHERE h.city = 'Buea'
GROUP BY h.hotelNo, h.hotelName;
```

3. **What is the total number of bookings for each hotel?**

```sql
SELECT h.hotelNo,
       h.hotelName,
       COUNT(b.roomNo) AS numBookings
FROM Hotel   AS h
JOIN Booking AS b ON h.hotelNo = b.hotelNo
GROUP BY h.hotelNo, h.hotelName;
```

These solutions give you both the **theory steps** (closures, 3NF criteria, decomposition) and the **practical SQL/RA interpretations** that are typically examined in IST601.

