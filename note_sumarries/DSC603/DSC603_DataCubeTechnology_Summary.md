# Summary: DSC603 Data Cube Technology and Computation

## Document Outline
- Data Cube Computation: Preliminary Concepts
- Data Cube Computation Methods
- Processing Advanced Queries by Exploring Data Cube Technology
- Multidimensional Data Analysis in Cube Space
- Summary

---

## 1. Data Cube Computation: Preliminary Concepts

### Data Cube: A Lattice of Cuboids
- The data cube is modeled as a **lattice of cuboids**.
- **0-D (apex) cuboid:** one cell (all dimensions aggregated).
- **1-D cuboids:** time; item; location; supplier.
- **2-D cuboids:** time,item; time,location; time,supplier; item,location; item,supplier; location,supplier.
- **3-D cuboids:** time,item,location; time,item,supplier; time,location,supplier; item,location,supplier.
- **4-D (base) cuboid:** time, item, location, supplier.

### Base vs. Aggregate; Ancestor vs. Descendant; Parent vs. Child
- **Base cells** are in the base cuboid; **aggregate cells** are in higher-level cuboids.
- **Ancestor vs. descendant:** ancestor = more *’s (more aggregation); descendant = fewer *’s (more specific).
- **Parent vs. child:** one dimension difference in aggregation level.

**Example (from document):**  
Cells listed in order (ancestor/descendant relationship):
1. (9/15, milk, Urbana, Dairy_land) — base
2. (9/15, milk, Urbana, *)
3. (*, milk, Urbana, *)
4. (*, milk, Urbana, *) — same as 3
5. (*, milk, Chicago, *)
6. (*, milk, *, *)

Lattice diagram shows apex → 1-D → 2-D → 3-D → 4-D (base).

---

### Cube Materialization: Full Cube vs. Iceberg Cube
- **Full cube:** materialize all cuboid cells.
- **Iceberg cube:** materialize only cells whose measure satisfies an **iceberg condition** (e.g., `HAVING count(*) >= min_support`).
- **DMQL example:**
  ```text
  compute cube sales iceberg as
  select month, city, customer_group, count(*)
  from salesInfo
  cube by month, city, customer_group
  having count(*) >= min_support
  ```
- Motivation: in sparse, high-dimensional cubes only a small portion of cells may be “above the water.”

**Example / exercise (from document):**  
- Cube with **100 dimensions**, **2 base cells:** (a1, a2, …, a100), (b1, b2, …, b100).

**Q1: How many aggregate cells if “having count >= 1”?**  
**Answer:** **2^100.** Each subset of dimensions defines one aggregate cell; each of the two base cells contributes to every such cell, so every aggregate cell has count ≥ 1. There are 2^100 such cells (one per subset of the 100 dimensions).

**Q2: What about “having count >= 2”?**  
**Answer:** **1 aggregate cell.** Both base cells aggregate to the same cell only when we use * on every dimension where they differ. They differ in dimensions 3 through 100 (a3 vs b3, …, a100 vs b100). So the only cell with count 2 is (*, *, …, *) — the apex cuboid. Hence one cell.

---

### Iceberg Cube, Closed Cube, and Cube Shell
- **Closed cell c:** no descendant of c has the same measure value as c.
- **Closed cube:** cube consisting only of closed cells (lossless compression for many measures).
- **Cube shell:** precompute only cuboids that involve a **small number** of dimensions (e.g., 3); other combinations are computed on the fly.

**Example (from document):**  
- **2 base cells:** {(a1, a2, a3, …, a100): 10, (a1, a2, b3, …, b100): 10}.

**Q: How many cells will the iceberg cube have if `having count(*) >= 10`?**  
**Answer:** **4 cells.** The only cells with count ≥ 10 are those that aggregate both base cells. Both base cells agree on dimensions 1 and 2 (a1, a2) and differ on 3..100. So we get one cell per subset of {dim1, dim2}: (a1, a2, *, …, *) : 20, (a1, *, *, …, *) : 20, (*, a2, *, …, *) : 20, (*, *, *, …, *) : 20. So 4 cells.

**Q: What is the closed cube of the above base cuboid? Hint: only 3 cells.**  
**Answer:** **3 cells.**  
- The two **base cells** (a1, a2, a3, …, a100): 10 and (a1, a2, b3, …, b100): 10 are closed (no descendant has the same measure; their descendants would be more specific and have the same or smaller count).  
- The cell (a1, a2, *, …, *): 20 is closed: its “descendants” in the lattice (e.g. (a1, a2, a3, *, …), (a1, a2, b3, *, …)) have measure 10 each, not 20.  
- Cells (*, *, *, …): 20, (a1, *, *, …): 20, (*, a2, *, …): 20 are **not** closed because they have a descendant (a1, a2, *, …, *): 20 with the same measure.  
So the closed cube has **3 cells:** the two base cells and (a1, a2, *, …, *): 20.

**Q: For (A1, A2, … A10), how many combinations to compute? (Cube shell with 3 dimensions.)**  
**Answer:** **C(10, 3) = 120** combinations. We compute all 3-dimensional cuboids over the 10 dimensions.

---

### Roadmap for Efficient Computation
- **General heuristics** for cube computation.
- **Full/iceberg cube methods:**
  - **Bottom-up:** Multi-Way Array Aggregation (Zhao et al., SIGMOD’97).
  - **Top-down:** BUC (Beyer et al., SIGMOD’99), H-cubing.
  - **Integrated:** Star-Cubing (Xin et al., VLDB’03).
- **High-dimensional OLAP:** minimal cubing (e.g., shell fragments).
- **Other:** partial cube, closed cube, approximate cube, etc.

---

### General Heuristics
- **Sorting, hashing, grouping** on dimension attributes to reorder and cluster tuples.
- Compute aggregates **from previously computed aggregates** when possible (not only from base fact table).
- **Smallest-child:** compute a cuboid from the smallest previously computed cuboid.
- **Cache-results:** cache a cuboid used to compute others to reduce disk I/O.
- **Amortize-scans:** compute many cuboids in the same pass to amortize reads.
- **Share-sorts:** reuse sorting across cuboids (sort-based methods).
- **Share-partitions:** reuse partitioning across cuboids (hash-based methods).

---

## 2. Data Cube Computation Methods

### Multi-Way Array Aggregation
- **Array-based, bottom-up** algorithm.
- Uses **multi-dimensional chunks** (subcubes that fit in memory).
- **No direct tuple comparisons**; simultaneous aggregation on multiple dimensions.
- **Intermediate aggregates** are reused for ancestor cuboids.
- **Limitation:** cannot do Apriori pruning; **no iceberg** optimization.

**Best traversing order (exercise in document):**  
**Answer:** Sort and compute **planes in ascending order of size**. Keep the **smallest plane** in main memory and fetch/compute **one chunk at a time** for the largest plane. This minimizes memory use and I/O.

**3-D to 2-D aggregation:**  
- Diagram shows lattice: all → A, B, AB, C, AC, BC, ABC.  
- Planes are sorted by size; smallest plane is kept in memory.

**2-D to 1-D:**  
- Same idea: aggregate from smaller to larger dimensions.

**Method summary:**  
- Sort planes by size (ascending); compute in that order.  
- **Limitation:** works well only for a **small number of dimensions**; for many dimensions, top-down and iceberg methods are more suitable.

---

### Bottom-Up Computation (BUC)
- **BUC** (Beyer & Ramakrishnan, SIGMOD’99): “bottom-up” cube computation (top-down in the lattice view).
- Partitions dimensions and supports **iceberg pruning**: if a partition does not meet min_sup, its descendants can be pruned.
- If min_sup = 1 ⇒ computes **full cube**.
- **No simultaneous aggregation** (unlike Multi-Way).

**Partitioning:**  
- Data often does not fit in memory.  
- Sort distinct values; partition into blocks that fit.  
- **Optimizations:** partitioning (external sort, hashing, counting sort); dimension ordering (cardinality, skew, correlation) to encourage pruning; **collapsing duplicates** (then holistic aggregates are no longer possible).

**Lattice numbering (from slide):**  
1=all, 2=A, 10=B, 14=C, 7=AC, 11=BC, 4=ABC, 6=ABD, 8=ACD, 12=BCD, 9=AD, 13=BD, 15=CD, 16=D, 5=ABCD, 3=AB.

---

### Star-Cubing: Integrating Top-Down and Bottom-Up
- **Star-Cubing** (Xin, Han, Li, Wah, VLDB’03): top-down aggregation with a bottom-up sub-layer for **Apriori pruning**.
- **Shared dimensions:** e.g., A is shared by ACD and AD; ABD/AB means cuboid ABD shares dimensions AB. Enables **shared computation** (e.g., AB computed while computing ABD).

**Iceberg pruning in shared dimensions:**  
- **Anti-monotonic** measure: if the aggregate on a shared dimension does not satisfy the iceberg condition, all cells extended from that shared dimension can be pruned.  
- **Idea:** compute shared dimensions before the full cuboid and use them for pruning.  
- **Challenge:** prune while still aggregating on multiple dimensions.

**Cell trees:**  
- Tree (e.g. H-tree style) represents cuboids; **common prefixes** collapsed to save space; **count** stored at nodes; traverse to get a tuple.

**Star attributes and star nodes:**  
- If a **single-dimensional aggregate** on an attribute value does not satisfy the iceberg condition, that value is not needed for the iceberg result.  
- **Solution:** replace such values by **\*** (star attribute); corresponding nodes are **star nodes**.  
- **Example table:** A B C D Count — e.g. a1 b1 c1 d1 1, …; values like b2, b3, b4, c1, c2, c4, d1, d2, d3 may become * if their 1-D count &lt; min_sup.

**Example: Star reduction (from document):**  
- **min_sup = 2.**  
- One-dimensional aggregation: replace attribute values with count &lt; 2 by *. Collapse *’s.  
- **Before:** rows like (a1,b1,c1,d1,1), (a1,b1,c4,d3,1), (a1,b2,c2,d2,1), (a2,b3,c3,d4,1), (a2,b4,c3,d4,1).  
- **After (compressed):** (a1, b1, *, *, 2), (a1, *, *, *, 1), (a2, *, c3, d4, 2).  
- This is a **lossless compression** for the iceberg computation.

**Star tree:**  
- Built from the compressed table; **star table** on the side for lookup.  
- Star tree is a lossless compression of the original cell tree.

**Star-Cubing algorithm:**  
- **DFS on the lattice tree** (e.g. all → A, B/B, C/C → AC/AC, BC/BC, ABC/ABC, ABD/AB, ACD/A, BCD, AD/A, BD/B, CD, D/D → ABCD).  
- **DFS on star-tree:** at each node, create descendant star trees following the integrated traversal; carry counts from base tree; at leaf (e.g. d*), backtrack; on backtrack, output counts, destroy trees/nodes.  
- **Example:** from d* back to c*: output and destroy a1b*c*/a1b*c* tree; from c* back to b*: output and destroy a1b*D/a1b* tree; then move to b1 and repeat.

---

### High-Dimensional OLAP
- **Curse of dimensionality:** previous cubing methods do not scale to very high dimensions.
- **Example setting:** 600K tuples, each dimension cardinality 100, Zipf 2.
- **Iceberg/compressed cubes** only delay the explosion; **full materialization** still has high overhead.
- **Applications:** science/engineering, bio-data (e.g. thousands of genes), statistical surveys (hundreds of variables).

**Fast high-D OLAP with minimal cubing:**  
- **Idea:** OLAP typically touches only a **small subset of dimensions** at a time.  
- **Semi-online model:**  
  1. Partition dimensions into **shell fragments**.  
  2. Compute **data cubes for each fragment**, keeping **inverted indices** (or value-list indices).  
  3. **Online:** from precomputed fragment cubes, compute cells of the full high-D cube on demand.

**Properties:**  
- **Vertical partitioning** of data; high-D cube reduced to **lower-dimensional** cubes; **online** reconstruction of the full space; **lossless**; tradeoff between preprocessing and online cost.

**Example computation (from document):**  
- **Aggregation:** count.  
- **5 dimensions** split into **2 shell fragments:** (A, B, C) and (D, E).  
- **Base table (tid, A, B, C, D, E):**  
  (1, a1, b1, c1, d1, e1), (2, a1, b2, c1, d2, e1), (3, a1, b2, c1, d1, e2), (4, a2, b1, c1, d1, e2), (5, a2, b1, c1, d1, e3).

**1-D inverted indices (example):**  
- Attribute value → TID list and list size.  
- E.g. a1 → {1,2,3}, size 3; a2 → {4,5}, size 2; b1 → {1,4,5}, size 3; b2 → {2,3}, size 2; c1 → {1,2,3,4,5}, size 5; d1 → {1,3,4,5}, size 4; d2 → {2}, size 1; e1 → {1,2}, size 2; e2 → {3,4}, size 2; e3 → {5}, size 1.

**Shell fragment cubes:**  
- **Fragment (A,B,C):** compute all cuboids A, B, C, AB, AC, BC, ABC with **inverted (TID) lists**.  
- **Fragment (D,E):** similarly DE, D, E.  
- **Idea:** generalize 1-D inverted indices to multi-D in the cube sense; compute cuboids by **intersecting TID lists** (e.g. cell a1∧b1 → intersection of a1’s and b1’s TID lists).  
- **Offline:** build these fragment cubes.

**Size and design:**  
- **Space** for fragment cubes: **O(T · ⌈D/F⌉ · (2^F − 1))** (T tuples, D dimensions, F fragment size). For F &lt; 5, growth is sub-linear.  
- Fragments need not be disjoint; grouping can be chosen for performance (e.g. put &lt;city, state&gt; together). Fragment size can be tuned for offline vs. online balance.

**ID_measure table:**  
- If measures other than count exist (e.g. sum), store **(tid, measure)** in a separate **ID_measure** table.  
- **Example:** tid, count, sum — (1,5,70), (2,3,10), (3,8,20), (4,5,40), (5,2,30).

**Frag-Shells algorithm (sketch):**  
1. Partition dimensions (A1,…,An) into k fragments (P1,…,Pk).  
2. Scan base table once: insert &lt;tid, measure&gt; into ID_measure; for each attribute value build inverted index &lt;ai, tidlist&gt;.  
3. For each fragment Pi: build **local fragment cube** Si by intersecting TID lists in bottom-up fashion.

**Online query:**  
- **Form:** ⟨a1, a2, …, an⟩ : M.  
- Each ai can be: **instantiated value**, **\*** (aggregate), or **?** (inquire).  
- **Example:** ⟨3, ?, ?, *, 1⟩ : count — returns a 2-D data cube (dimensions 2 and 3; 1 and 5 instantiated; 4 aggregated).

**Online method:**  
1. Split query by fragment (same as shell).  
2. Fetch **TID lists** for each fragment from fragment cubes.  
3. **Intersect** TID lists to get the **instantiated base table**.  
4. Run any cubing algorithm on this table to get the requested cube.

**Experiments (from document):**  
- **Synthetic:** (50-C) 10^6 tuples, 0 skew, cardinality 50, fragment size 3; (100-C) 10^6 tuples, skew 2, cardinality 100, fragment size 2.  
- **UCI Forest CoverType:** 54 dimensions, 581K tuples; shell fragments of size 2 → 33 s, 325 MB; 3-D subquery with 1 instantiated dimension: 85 ms–1.4 s.  
- **Longitudinal Study of Vocational Rehab.:** 24 dimensions, 8818 tuples; fragments of size 3 → 0.9 s, 60 MB; 5-D query with 0 instantiated dimensions: 227 ms–2.6 s.

---

## 3. Summary (From the Document)

- **Preliminary concepts:** Lattice of cuboids; base vs. aggregate; full vs. iceberg vs. closed vs. cube shell; roadmap and heuristics.
- **Computation methods:**  
  - Multi-Way Array Aggregation (bottom-up, chunks, best order = smallest plane first).  
  - BUC (top-down, partitioning, iceberg pruning).  
  - Star-Cubing (top-down + bottom-up, shared dimensions, star tree, iceberg pruning).  
  - High-dimensional OLAP (shell fragments, inverted indices, semi-online, Frag-Shells).

**Left for SPW (Student Personal Work):**  
- **Processing advanced queries:** Sampling Cubes, Ranking Cubes.  
- **Multidimensional analysis in cube space:** Discovery-Driven Exploration, Multi-feature Cubes, Prediction Cubes.

---

## 4. Answers to In-Document Exercises and Questions

| Slide / Topic | Question | Answer |
|---------------|----------|--------|
| Full vs. iceberg (2 base cells, 100 dims) | How many aggregate cells if count ≥ 1? | **2^100** |
| Same | How many if count ≥ 2? | **1** (apex only) |
| Iceberg, closed, shell (2 cells, count 10 each) | How many cells if count ≥ 10? | **4** cells |
| Same | Closed cube of that cuboid? | **3** cells (two base + (a1,a2,*,…,*):20) |
| Cube shell | (A1..A10), 3-D shell: how many combinations? | **C(10,3) = 120** |
| Multi-Way Array | Best traversing order? | **Ascending order of plane size**; smallest plane in memory, one chunk at a time for largest |

---

## Note on Exercises and Assignments

This PDF is a **49-slide lecture** on Data Cube Technology. It contains the **exercises and answers** listed in the table above; there are no separate assignment sheets. Topics marked as **SPW** (Sampling Cubes, Ranking Cubes, Discovery-Driven Exploration, Multi-feature Cubes, Prediction Cubes) are for self-study. If you have a separate problem set, share it for answer drafting.
