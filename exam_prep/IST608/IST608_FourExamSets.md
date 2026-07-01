# IST608 Advanced Topics in Database Management — Four Practice Examination Sets

**Source materials:** PhysicalDatabaseDesignI.pdf · PhysicalDatabaseDesignII.pdf · Topic36.md · DataCenterEnvironment.md

**Format per set:** 20 MCQs (20 marks) · Structural Questions (50 marks)  
**Total per set:** 70 marks | **Suggested time per set:** 3 hours

---

# EXAM SET 1 — Disk Technology, File Organizations, and RAID

**Coverage in this set:** Secondary storage devices and disk performance · File record placement and buffering · Heap files and sorted files · Hashing techniques · RAID levels and parity · File access operations and allocation strategies

---

## Section A: Multiple Choice Questions (20 Marks)

*Choose the best answer for each question. 1 mark each.*

**1.** (Medium) [PBD-I] When a disk block size (B) is larger than the record size (R), and records are not allowed to cross block boundaries, the placement method is called:

A. Spanned record allocation  
B. Unspanned record allocation  
C. Linked record allocation  
D. Indexed allocation

**2.** (Hard) [PBD-I] In a disk pack where all tracks have the same number of sectors, the result is:

A. Higher data density on outer tracks  
B. Lower data density on outer tracks  
C. Constant data density across all tracks  
D. Variable rotational latency across tracks

**3.** (Medium) [PBD-I] A hash function that maps a search key value to a bucket address is the defining characteristic of:

A. A B+tree index  
B. A dynamic multilevel index  
C. External hashing  
D. A primary index

**4.** (Hard) [PBD-I] Which of the following statements about a concatenated metaLUN is FALSE?

A. Component LUNs need not have the same capacity as the base LUN  
B. A RAID 0 LUN can be concatenated with a RAID 5 LUN  
C. It provides additional capacity but no performance improvement  
D. All LUNs must reside on the same disk-drive type

**5.** (Medium) [PBD-I] The primary disadvantage of a heap (unordered) file organization is:

A. Slow insertion speed  
B. Slow sequential access  
C. Slow retrieval of specific records without an index  
D. Inability to handle variable-length records

**6.** (Hard) [PBD-I] In extendible hashing, what causes the global depth of the directory to increase?

A. A bucket split when the local depth equals the global depth  
B. A bucket overflow due to too many records  
C. A deletion of a record from a full bucket  
D. A compaction of the directory

**7.** (Medium) [PBD-I] The average rotational latency for a 10,000 RPM disk drive is approximately:

A. 3.0 ms  
B. 6.0 ms  
C. 0.3 ms  
D. 12.0 ms

**8.** (Hard) [PBD-I] Which RAID level provides striping with distributed parity across all disks, supporting concurrent reads without single-parity bottlenecks?

A. RAID 0  
B. RAID 1  
C. RAID 5  
D. RAID 6

**9.** (Medium) [DCE] According to the utilization-versus-response-time curve, the "knee of the curve" — beyond which response time rises exponentially — occurs at approximately what disk controller utilization?

A. 30 percent  
B. 50 percent  
C. 70 percent  
D. 90 percent

**10.** (Hard) [PBD-I] In a sorted file, the main reason insertion is expensive is that:

A. The file must be reindexed from scratch  
B. Records must be moved to maintain physical order  
C. An overflow file is always required  
D. Binary search cannot locate the insertion point

**11.** (Medium) [PBD-I] Linear hashing differs from extendible hashing in that it:

A. Requires a directory to map keys to buckets  
B. Does not require a directory structure  
C. Cannot split buckets dynamically  
D. Only supports static files

**12.** (Hard) [PBD-I] What happens when a non-root node in a B-tree is full and a new entry is inserted?

A. The new entry is rejected  
B. The node splits into two, and the middle entry moves to the parent  
C. The entire tree is rebuilt from scratch  
D. The node is marked as overflow

**13.** (Medium) [Topic36] The smallest unit of cache allocation in an intelligent storage system is called a:

A. Bucket  
B. Page  
C. Sector  
D. Block

**14.** (Hard) [DCE] For a disk drive with an average seek time of 8 ms, 15,000 RPM spindle speed, and an internal transfer rate of 80 MB/s, what is the approximate maximum IOPS when the block size is 32 KB?

A. 100 IOPS  
B. 125 IOPS  
C. 150 IOPS  
D. 200 IOPS

**15.** (Medium) [PBD-I] In internal hashing, collision resolution by chaining means:

A. Searching successive buckets until an empty slot is found  
B. Storing colliding records in a linked list attached to the hash table entry  
C. Recomputing the hash with a second function  
D. Splitting the bucket into two

**16.** (Hard) [PBD-I] A striped metaLUN expansion requires all component LUNs to be:

A. Unprotected (RAID 0) with different capacities  
B. Identical in capacity and RAID level  
C. A mix of RAID 5 and RAID 6  
D. Concatenated rather than striped

**17.** (Medium) [Topic36] Write-aside (bypass) cache is typically triggered when a write I/O exceeds which threshold?

A. The LUN size  
B. The write-back size  
C. The predefined write-aside size  
D. The cache page size

**18.** (Hard) [DCE] If a database block is 8 KB and the disk internal transfer rate is 40 MB/s, the internal transfer component of disk service time (X) is:

A. 0.1 ms  
B. 0.2 ms  
C. 0.4 ms  
D. 0.8 ms

**19.** (Medium) [PBD-I] In a dense secondary index built on a non-ordering key field, why must an index entry exist for every record?

A. The data file is small  
B. Because the data file is not physically ordered by the indexed field, individual record pointers are needed to locate each record anywhere in the file  
C. The index file must be larger than the data file  
D. Sparse indexes are deprecated in modern DBMSs

**20.** (Hard) [PBD-I] Which of the following correctly describes the relationship between a search tree of order p and a B-tree of order p?

A. A search tree allows at most p-1 keys per node; a B-tree is the same but balanced  
B. Both are always balanced  
C. A B-tree node cannot split  
D. A search tree uses linked leaves while a B-tree does not

---

## Section A — Answer Key

| Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|
| 1 | B | 6 | A | 11 | B | 16 | B |
| 2 | B | 7 | A | 12 | B | 17 | C |
| 3 | C | 8 | C | 13 | B | 18 | B |
| 4 | B | 9 | C | 14 | B | 19 | B |
| 5 | C | 10 | B | 15 | B | 20 | A |

---

## Section B: Structural Questions (50 Marks)

*Answer ALL questions in this section.*

---

### Question 1 (12 Marks)

An enterprise application is deployed on a disk drive with the following specifications:
- Average seek time T_seek = 8 ms
- Spindle speed = 10,000 RPM
- Internal transfer rate = 60 MB/s
- The application issues 32 KB I/O blocks.

**(a)** Calculate the average rotational latency L in milliseconds. **(2 marks)**

**(b)** Calculate the internal transfer time X for a 32 KB block. **(2 marks)**

**(c)** Calculate the total disk service time Ts for one I/O request. **(2 marks)**

**(d)** Calculate the maximum theoretical IOPS this disk can perform at near-full utilization. **(2 marks)**

**(e)** Using the formula R = Ts / (1 – U), compute the response time R when the disk controller utilization U is: (i) 60%, (ii) 80%, and (iii) 95%. Comment on the trend as utilization approaches 100%. **(4 marks)**

#### Model Answer — Question 1

**(a)**
- Rotational speed = 10,000 RPM = 10,000 / 60 = 166.67 revolutions per second (rps)
- Average rotational latency = 0.5 / 166.67 = **3.0 ms**

**(b)**
- Transfer rate = 60 MB/s = 60 × 1024 × 1024 bytes/s = 62,914,560 bytes/s
- Internal transfer time X = (32 × 1024) / 62,914,560 = 32,768 / 62,914,560 ≈ **0.000521 s = 0.521 ms**

**(c)**
- Ts = T_seek + L + X = 8 + 3.0 + 0.521 ≈ **11.52 ms** (accept 11.5 ms)

**(d)**
- IOPS = 1 / Ts(s) = 1 / 0.01152 ≈ **86.8 ≈ 87 IOPS**

**(e)**
- (i) U = 60%: R = 11.52 / (1 – 0.60) = 11.52 / 0.40 = **28.8 ms**
- (ii) U = 80%: R = 11.52 / (1 – 0.80) = 11.52 / 0.20 = **57.6 ms**
- (iii) U = 95%: R = 11.52 / (1 – 0.95) = 11.52 / 0.05 = **230.4 ms**

**Trend:** As utilization approaches 100%, the denominator (1 – U) approaches zero, so response time increases nonlinearly and explodes toward infinity. This confirms that for response-time-sensitive applications, disks should be kept below approximately 70% utilization to avoid exponential degradation.

---

### Question 2 (12 Marks)

A file contains fixed-length records with record size R = 180 bytes. The disk block size is B = 4,096 bytes. The file has r = 27,000 records.

**(a)** Calculate the blocking factor (bfr) and the number of file blocks (b) under **unspanned** record allocation. **(4 marks)**

**(b)** If the same file used **spanned** record allocation, would the number of file blocks increase, decrease, or stay the same? Explain why, and state a scenario in which spanned allocation is necessary. **(4 marks)**

**(c)** Explain the three methods of allocating file blocks on disk: contiguous allocation, linked allocation, and indexed allocation. For each, state one advantage and one disadvantage. **(4 marks)**

#### Model Answer — Question 2

**(a)**
- bfr = ⌊B / R⌋ = ⌊4,096 / 180⌋ = **22 records per block**
- b = ⌈r / bfr⌉ = ⌈27,000 / 22⌉ = **1,228 blocks**

**(b)**
- For **spanned** records where R < B but records are not restricted to one block, the number of blocks could **decrease slightly** in some cases because the last block of each multi-block record can be partially filled by the next record. However, with R = 180 and B = 4,096, the block is not full (22 × 180 = 3,960 bytes used, 136 bytes free). If records were larger (e.g., R = 5,000 bytes), spanning would be **necessary** because the record cannot fit in a single block. Spanned allocation uses a pointer at the end of the first block to link to the continuation block. It is required for variable-length records or records larger than the block size.

**(c)**

| Method | Description | Advantage | Disadvantage |
|--------|-------------|-----------|--------------|
| Contiguous allocation | File blocks allocated to consecutive disk blocks | Fast sequential access; minimal seek time | File growth is difficult; external fragmentation |
| Linked allocation | Each file block contains a pointer to the next file block | Only the head pointer must be kept in one place; easy file growth | Slow random access; pointer overhead |
| Indexed allocation | Index blocks contain pointers to file blocks | Supports both sequential and random access efficiently | Index block overhead; additional I/O for index lookup |

---

### Question 3 (13 Marks)

Consider a storage system with five physical disks, each of capacity 2 TB.

**(a)** For **RAID 0** (striping), calculate the total logical capacity presented to the host. **(2 marks)**

**(b)** For **RAID 1** (mirroring), calculate: (i) the total usable capacity, and (ii) the read and write performance characteristics compared to a single disk. **(4 marks)**

**(c)** For **RAID 5** (block-level striping with distributed parity) using the same five disks, calculate: (i) the total usable capacity, and (ii) the write penalty for a small random write operation. **(4 marks)**

**(d)** For **RAID 6** (P+Q redundancy), calculate the usable capacity and compare its fault tolerance and write penalty to RAID 5. **(3 marks)**

#### Model Answer — Question 3

**(a)** RAID 0 uses all disks for data with no redundancy.
- Capacity = 5 × 2 TB = **10 TB**

**(b)**
- (i) RAID 1 mirrors data across disk pairs. Usable capacity = (number of mirrors) × drive capacity = (5 / 2) × 2 TB = **5 TB** (one drive's worth is consumed by mirroring overhead, or more precisely: floor(5/2) = 2 pairs = 4 drives of usable data = 4 TB, plus the 5th drive typically unused or as hot spare. The standard calculation for an odd number of disks in mirroring is (n/2) × disk_size if a spare is used, or simply that capacity is halved. With 5 drives: usable = floor(5/2) × 2 TB = 2 × 2 TB = **4 TB** if the 5th is spare, or 2.5 × 2 TB = 5 TB if the 5th is also mirrored partially. The standard textbook formula is n/2 × disk_size for even n. For clarity: **4 TB usable** (2 mirrors × 2 TB), with the 5th drive typically as a hot spare or unused.)
  - *Simpler accepted answer:* RAID 1 gives **4–5 TB usable** (capacity is approximately halved); a commonly accepted textbook answer is **(n/2) × disk_size**.

- (ii) Read performance: improved, because reads can be serviced from either side of the mirror simultaneously. Write performance: no improvement over a single disk, because every write must update both mirrored copies.

**(c)**
- (i) RAID 5 uses one disk's worth of parity. Usable capacity = (n – 1) × disk_size = (5 – 1) × 2 TB = **8 TB**
- (ii) Write penalty = **4** (read old data + read old parity + write new data + write new parity = 4 disk I/Os for every host write)

**(d)**
- Usable capacity = (n – 2) × disk_size = (5 – 2) × 2 TB = **6 TB**
- Fault tolerance: RAID 6 survives up to **two simultaneous disk failures** vs. RAID 5's one.
- Write penalty: RAID 6 = **6** (higher than RAID 5 due to two parity calculations), but provides superior protection.

---

### Question 4 (13 Marks)

Compare and contrast **heap (unordered) files** with **sorted (ordered) files** as primary file organizations. Your answer must address:

**(a)** Record insertion efficiency, including the role of overflow files. **(4 marks)**

**(b)** Record deletion efficiency, including deletion markers versus physical rewrite. **(4 marks)**

**(c)** Search efficiency for a record based on the ordering key. **(3 marks)**

**(d)** Modification efficiency when the modification involves the ordering key field versus a non-ordering field. **(2 marks)**

#### Model Answer — Question 4

**(a) Insertion:** Heap files allow insertion at the end or in any available slot with **O(1)** efficiency; the new record is simply placed in the next available block. Sorted files require finding the correct physical position (typically via binary search) and then shifting approximately half the records on average to make space — **O(n/2)** block transfers. Overflow files ameliorate this by appending new records to an unordered overflow area instead, at the cost of a more complex search algorithm that must check both the main file and overflow.

**(b) Deletion:** Heap files can mark a record as deleted using a deletion marker (1 bit/byte) in **O(1)** or rewrite the block in **O(1)** if the record is in a buffer. Sorted files with a deletion marker also achieve O(1) per record, but physical compaction is deferred to periodic reorganization. Without markers, both file types must rewrite the affected block.

**(c) Search:** Sorted files support efficient **binary search** on the ordering key (log₂b block accesses), while heap files require linear search in the worst case (b/2 on average). Non-ordering field searches are equally inefficient in both organizations.

**(d) Modification:** Modifying a **non-ordering field** in a sorted file is a simple rewrite of the same physical location. Modifying the **ordering key** requires deleting the old record and inserting a new one, because the record's value change alters its correct physical position in the sorted sequence.

---

### Question 5 (10 Marks)

**(a)** Define hashing in the context of external file organizations, and distinguish between **static hashing** and **dynamic hashing** techniques. **(6 marks)**

**(b)** Explain the specific problem with static hashing as a file grows, and describe how **extendible hashing** addresses this problem using a directory and global/local depth. **(4 marks)**

#### Model Answer — Question 5

**(a)** Hashing maps a search key value to a disk block address (bucket) using a hash function. **Static hashing** allocates a fixed number of buckets at file creation time; performance degrades as the file grows because overflow chains lengthen. **Dynamic hashing** (including extendible and linear hashing) allows the file to grow and shrink buckets dynamically without catastrophic performance loss.

**(b)** In static hashing, once buckets overflow, long overflow chains develop, degrading searches to near-linear time. Extendible hashing maintains a **directory** of 2^d entries (where d is the global depth). When a bucket splits, if its local depth i < global depth d, only a single directory entry is pointed to the new bucket, and the original entry's pointer is redirected. If i = d, the directory doubles in size (global depth increases by 1), and all entries are re-linked. This ensures that searches remain efficient even as the file grows.

---

*End of Exam Set 1*

---

# EXAM SET 2 — Indexing Structures and Physical Database Design

**Coverage in this set:** Single-level ordered indexes (primary, clustering, secondary) · Multilevel indexes and fan-out · B-trees and B+trees · Indexes on multiple keys (composite, partitioned hashing, grid files) · Physical database design factors

---

## Section A: Multiple Choice Questions (20 Marks)

*Choose the best answer for each question. 1 mark each.*

**1.** (Medium) [PBD-II] A primary index is built on the:
A. Any foreign key field of an unordered file
B. Ordering key field of an ordered data file
C. Any non-ordering field of an unordered file
D. Nonkey clustering field of a sorted file

**2.** (Hard) [PBD-II] Which type of single-level index is built on a nonkey field of an ordered data file and has one entry per distinct value of that field?
A. Primary index
B. Clustering index
C. Secondary index
D. Dense index

**3.** (Medium) [PBD-II] In a multilevel index, the blocking factor of the index file (bfri) is also called the:
A. Search radius
B. Fan-out (fo)
C. Occupancy ratio
D. Anchor factor

**4.** (Hard) [PBD-II] A multilevel index with fan-out 80 and 1,024 first-level blocks requires approximately how many block accesses to locate a data block (excluding the final data block access)?
A. log2(1,024) = 10
B. 1,024 / 80 = 12.8
C. log80(1,024) ≈ 1.7
D. 80 × 1,024 = 81,920

**5.** (Medium) [PBD-II] In a B+-tree of order p, every internal node (except the root) must have at least how many children?
A. p
B. ⌈p/2⌉
C. p – 1
D. 2p

**6.** (Hard) [PBD-II] What is the fundamental structural difference between a B-tree and a B+-tree?
A. B-trees are unbalanced; B+-trees are balanced
B. In a B-tree, data pointers appear at every level; in a B+-tree, data pointers appear only at leaf nodes
C. B+-trees cannot support deletions
D. B-trees do not use linked leaves

**7.** (Medium) [PBD-II] After prolonged random insertions and deletions, B-tree and B+-tree nodes typically stabilize at approximately what occupancy?
A. 50%
B. 69%
C. 85%
D. 100%

**8.** (Hard) [PBD-II] A search tree of order p allows at most how many search values per node?
A. p
B. p – 1
C. p + 1
D. 2p

**9.** (Medium) [PBD-II] Partitioned hashing is most suitable for which type of query condition?
A. Range queries on a single attribute
B. Equality comparisons on multiple attributes
C. Wildcard pattern matching
D. Join operations only

**10.** (Hard) [PBD-II] In a grid file built on attributes (Dno, Age), each cell of the grid array points to:
A. A B+-tree root node
B. A bucket address where matching records are stored
C. A hash function definition
D. Another grid array

**11.** (Medium) [PBD-II] A bitmap index is most efficiently applied to columns that have:
A. A very large number of distinct values, all unique
B. A small number of distinct values relative to the number of rows
C. Only numeric data types
D. Only foreign key columns

**12.** (Hard) [PBD-II] Given a column where a particular value occurs very frequently, what storage optimization is preferred in a B+-tree leaf node over storing many individual record pointers?
A. A grid file
B. A bitmap (bitvector)
C. Partitioned hashing
D. A logical index

**13.** (Medium) [PBD-II] The main advantage of a logical index <K, Kp> over a physical index <K, P> is that it:
A. Requires less storage space
B. Avoids updating pointers when record physical addresses change
C. Eliminates the need for a primary file organization
D. Only works with hash indexes

**14.** (Hard) [PBD-II] Function-based indexing is primarily useful because it:
A. Removes the need for WHERE clauses in SQL
B. Allows the DBMS to use an index even when a function is applied to a column in a search predicate
C. Converts a B+-tree into a hash index automatically
D. Only accelerates DELETE operations

**15.** (Medium) [PBD-II] According to physical database design guidelines, which attributes are the best candidates to be excluded from indexing?
A. Candidate key attributes
B. Attributes frequently updated by transaction processing
C. Attributes used in join conditions
D. Attributes used in range queries

**16.** (Hard) [PBD-II] In a B+-tree leaf node, the extra pointer (not found in internal nodes) points to:
A. The parent node
B. The next leaf node
C. The root node
D. A data block pointer

**17.** (Medium) [PBD-II] In a primary index on an ordered file with b = 2,000 data blocks and an index entry size of 16 bytes on a 1 KB block, the number of first-level index blocks is approximately:
A. 125
B. 200
C. 250
D. 500

**18.** (Hard) [PBD-II] Which statement about a secondary index on a nonkey field is FALSE?
A. It is dense because the data file is not ordered by the indexed field
B. An entry must exist for every record
C. Block anchors can be used because the file is physically ordered
D. It usually requires more storage and longer search time than a primary index

**19.** (Medium) [PBD-II] In a grid file with two search keys of relatively uniform distribution, the array is typically indexed along each key using a:
A. B+-tree
B. Hash function with a fixed number of buckets
C. Linear scale that groups key values to achieve uniform distribution across cells
D. Bitmap index

**20.** (Hard) [PBD-II] Why are B+-trees generally preferred for index implementation in commercial RDBMSs over B-trees?
A. B+-trees are always shorter because internal nodes contain only keys and tree pointers, allowing more entries per node and higher fan-out
B. B+-trees do not require splitting on insertion
C. B-trees have a higher branching factor by definition
D. B+-trees are easier to implement in hardware

---

## Section A — Answer Key

| Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|
| 1 | B | 6 | B | 11 | B | 16 | B |
| 2 | B | 7 | B | 12 | B | 17 | A |
| 3 | B | 8 | B | 13 | B | 18 | C |
| 4 | C | 9 | B | 14 | B | 19 | C |
| 5 | B | 10 | B | 15 | B | 20 | A |

---

## Section B: Structural Questions (50 Marks)

*Answer ALL questions in this section.*

---

### Question 1 (12 Marks)

An EMPLOYEE file is ordered by Ssn. The file has:
- r = 40,000 records
- Block size B = 1,024 bytes
- Record size R = 120 bytes (unspanned)
- Ssn key size = 9 bytes
- Block pointer size = 6 bytes

**(a)** Calculate the blocking factor (bfr) and the number of data blocks (b) for the file. **(3 marks)**

**(b)** Calculate the index entry size, the index blocking factor (bfri), and the number of first-level index blocks (bi). **(3 marks)**

**(c)** Calculate the number of block accesses required to retrieve a record using: (i) binary search directly on the data file, and (ii) binary search on the primary index followed by one data block access. State which is more efficient and explain in one sentence. **(4 marks)**

**(d)** Explain why the primary index is classified as sparse (nondense) rather than dense. **(2 marks)**

#### Model Answer — Question 1

**(a)**
bfr = floor(1,024 / 120) = 8 records per block.
b = ceil(40,000 / 8) = 5,000 blocks.

**(b)**
Index entry size Ri = 9 + 6 = 15 bytes.
bfri = floor(1,024 / 15) = 68 entries per block.
bi = ceil(5,000 / 68) = 74 index blocks.

**(c)**
(i) Binary search on data file: ceil(log2 5,000) = 13 block accesses.
(ii) Binary search on primary index: ceil(log2 74) = 7 block accesses, plus 1 data block access = 8 total block accesses.
The primary index search is more efficient (8 vs 13 accesses) because the index file is smaller, enabling a faster binary search over fewer blocks, with only one additional access to fetch the actual data.

**(d)** A primary index is sparse because there is one index entry per block anchor (the first record in each data block), not one per record. Since the data file is physically ordered by the key, all records with key values between two consecutive anchors reside in the same block, so intermediate records do not need separate index entries.

---

### Question 2 (13 Marks)

**(a)** Define the following terms precisely, in the context of indexing: (i) indexing field, (ii) block anchor, (iii) dense index, (iv) sparse (nondense) index. **(8 marks — 2 marks each)**

**(b)** For each of the following index types, state whether it is dense or sparse and justify briefly: (i) primary index, (ii) secondary index on a key field, (iii) clustering index. **(5 marks)**

#### Model Answer — Question 2

**(a)**
- Indexing field: The attribute (field) of a file on which an index access structure is defined; it is the search key used to construct index entries.
- Block anchor: The first record physically stored in each data block; its key value is used as the K(i) value in a primary index entry for that block.
- Dense index: An index containing an entry for every search key value — and hence every record — in the data file.
- Sparse (nondense) index: An index containing entries for only a subset of search key values, typically one per block or one per distinct value.

**(b)**
- Primary index — Sparse: One entry per data block (the block anchor), not one per record, because the data file is physically ordered by the key.
- Secondary index on a key field — Dense: The data file is NOT ordered by this field, so a separate pointer is needed for every record to locate each record individually regardless of physical position.
- Clustering index — Sparse: One entry per distinct value of the (nonkey) clustering field, because all records sharing the same value are physically grouped together starting at a known block.

---

### Question 3 (12 Marks)

Consider a B+-tree with order p = 5 for internal nodes and p_leaf = 4 for leaf nodes.

**(a)** Describe the structure of an internal node: what does it contain, and how many tree pointers and search values can it hold at most? **(4 marks)**

**(b)** Describe the structure of a leaf node and state how it differs from an internal node. **(3 marks)**

**(c)** In your own words, explain why leaf nodes in a B+-tree are linked together with next pointers, and state one query pattern that benefits most from this design. **(3 marks)**

**(d)** If the data file has r = 60,000 records, key size V = 10 bytes, block pointer P = 6 bytes, record pointer Pr = 8 bytes, and block size B = 1,024 bytes, estimate the number of levels and the approximate search cost at 69% occupancy. **(2 marks)**

#### Model Answer — Question 3

**(a)** An internal node stores entries of the form <P1, K1, P2, K2, ..., Kq-1, Pq> where q <= p. Each Pi is a tree pointer to a child node. With p = 5, an internal node holds at most 5 tree pointers and 4 search key values. There are no data pointers in internal nodes.

**(b)** A leaf node stores entries of the form <Ki, Pri>, where Pri is a data pointer (to the record or to a block of records). With p_leaf = 4, a leaf holds at most 3 key-data-pointer pairs plus a next-leaf pointer. Unlike internal nodes, leaf node entries point to actual data, not to tree nodes.

**(c)** Linked leaves allow retrieval of records in ordered sequence without traversing back up the internal levels. Range queries (e.g., BETWEEN, ORDER BY) benefit most because the DBMS can begin at the first matching leaf and then follow next pointers to read all qualifying records sequentially.

**(d)**
Internal order p: largest integer s.t. p*P + (p-1)*V <= B. With P=6, V=10, B=1024: 6p + 10(p-1) <= 1024 -> p approx 64.
Leaf order p_leaf: largest integer s.t. p_leaf*(V+Pr) + P <= B. With V+Pr=18, P=6: 18*p_leaf + 6 <= 1024 -> p_leaf approx 56.
At 69% occupancy: fan-out approx 0.69 * 64 approx 44. Leaf entries approx 0.69 * 56 approx 38.
Leaf blocks approx 60,000 / 38 approx 1,579.
Next level approx 1,579 / 44 approx 36.
Root approx 36 / 44 approx 1 block.
Levels approx 3 (root, intermediate, leaves). Search cost approx 3-4 block accesses.

---

### Question 4 (13 Marks)

**(a)** What is a composite index, and when should it be used instead of separate single-attribute indexes? **(3 marks)**

**(b)** Describe partitioned hashing as an extension of static external hashing. Explain how the hash address is formed and why it can only answer equality conditions on the component attributes. **(5 marks)**

**(c)** Explain how a grid file supports range queries on multiple keys, and contrast this with partitioned hashing in terms of range-query support. **(5 marks)**

#### Model Answer — Question 4

**(a)** A composite index is an index built on a key formed by combining two or more attributes (e.g., (Dno, Age)). It should be used when a query predicate specifies conditions on both attributes simultaneously, allowing the DBMS to locate records via a single index structure. Separate single-attribute indexes would require intersecting two postings lists.

**(b)** Partitioned hashing extends static external hashing to n attributes by computing a separate hash address for each attribute and concatenating them to form the bucket address. For example, hash(Dno) = 2 and hash(Age) = 5 yields bucket 25. It answers equality conditions (e.g., Dno=4 AND Age=59) because the exact concatenated bucket can be computed. It cannot support range queries because hash functions scatter keys pseudo-randomly; there is no contiguous set of bucket addresses corresponding to a range (e.g., Age 30-40), since hash(31) bears no predictable relationship to hash(32).

**(c)** A grid file defines a linear scale for each search attribute (e.g., Dno -> [0,1,2,...], Age -> [0,1,2,...]) forming an n-dimensional array. Each cell points to a data bucket. A range query (e.g., Dno <= 5 AND Age > 40) maps to a rectangular subregion of the array, and all cells in that subregion are retrieved. Unlike hashing, the ordered scales preserve adjacency, so contiguous ranges of key values map to contiguous sets of cells. The trade-off is space overhead for the grid array and reorganization cost as data grows.

---

*End of Exam Set 2*

---

# EXAM SET 3 — Intelligent Storage Systems and Data Center Environment

**Coverage in this set:** Intelligent storage system components · Cache structure and operations · Cache management (LRU, MRU, watermarks) · Cache data protection (mirroring, vaulting) · LUN provisioning (traditional vs virtual, thick vs thin, metaLUN) · LUN masking · High-end vs midrange storage · Disk drive performance and flash drives · Application and compute virtualization

---

## Section A: Multiple Choice Questions (20 Marks)

*Choose the best answer for each question. 1 mark each.*

**1.** (Medium) [Topic36] In the structure of cache, which component contains the dirty bit flag indicating whether cached data has been committed to disk?
A. Data store
B. Tag RAM
C. Vault drive
D. Front-end buffer

**2.** (Hard) [Topic36] A storage system prefetches data in an amount that is a multiple of the host's read request size. This strategy is called:
A. Fixed prefetch
B. Maximum prefetch
C. Variable prefetch
D. Sequential-only prefetch

**3.** (Medium) [Topic36] Which Fibre Channel port type forms the connection between two FC switches via an Interswitch Link (ISL)?
A. N_Port
B. F_Port
C. E_Port
D. G_Port

**4.** (Hard) [Topic36] What is the maximum theoretical number of node ports addressable in an FC switched fabric, based on the 24-bit FC address structure?
A. 126
B. 256
C. 15,663,104
D. 2,112

**5.** (Medium) [Topic36] In iSCSI, what is the role of the initiator?
A. It is the storage device that responds to SCSI commands
B. It is the host that originates the SCSI command request over IP
C. It is the gateway that converts FC frames to IP packets
D. It is the switch that routes Ethernet traffic

**6.** (Hard) [DCE] Which iSCSI host connectivity option offloads the entire iSCSI and TCP/IP processing from the host processor, providing the best performance?
A. Standard NIC with software initiator
B. TCP Offload Engine (TOE) NIC
C. iSCSI HBA
D. FCoE CNA

**7.** (Medium) [DCE] What are the two key components of a NAS device?
A. Front end and back end
B. NAS head and storage
C. CNA and FCF
D. Initiator and target

**8.** (Hard) [Topic36] Which NFS version is based on a stateful protocol design, uses TCP, and introduced features such as the session model and parallel NFS (pNFS)?
A. NFSv2
B. NFSv3
C. NFSv4 (specifically NFSv4.1)
D. NFSv1

**9.** (Medium) [Topic36] What is the term for a LUN created via virtual provisioning, distinguishing it from a traditionally provisioned LUN?
A. MetaLUN
B. Thick LUN
C. Thin LUN
D. Virtual RAID set

**10.** (Hard) [Topic36] In FC zoning, which type uses World Wide Names to define zone membership, allowing devices to be moved to different switch ports without modifying the zone configuration?
A. Port zoning
B. WWN zoning
C. Mixed zoning
D. Domain zoning

**11.** (Medium) [DCE] What is the purpose of LUN masking, and at what level is it implemented?
A. It is implemented at the fabric level to define which ports can communicate
B. It is implemented at the array level to define which hosts can access specific LUNs
C. It is implemented at the host level to mask disk drivers
D. It is implemented at the switch level to control VLAN membership

**12.** (Hard) [Topic36] Which FCoE enabling technology creates eight separate virtual links on a single physical Ethernet link, allowing any one of them to be paused independently without affecting the others?
A. Enhanced Transmission Selection (ETS)
B. Priority-based Flow Control (PFC)
C. Congestion Notification (CN)
D. Data Center Bridging Exchange Protocol (DCBX)

**13.** (Medium) [DCE] Which file-sharing protocol is described as a stateful protocol because the server maintains connection information for every connected client?
A. NFSv3
B. FTP
C. CIFS
D. NFSv2

**14.** (Hard) [Topic36] Which type of metaLUN expansion requires all participating LUNs to be the same capacity and RAID level, and provides a genuine performance improvement by redistributing data across more drives?
A. Concatenated expansion
B. Striped expansion
C. Mirrored expansion
D. Sequential expansion

**15.** (Medium) [Topic36] In FC-AL (Fibre Channel Arbitrated Loop), what is the maximum number of nodes that can be connected on the loop, given that one address is reserved for connecting to an FC switch port?
A. 127
B. 126
C. 256
D. 15 million

**16.** (Hard) [Topic36] What is the role of a pNFS metadata server in the pNFS architecture?
A. It handles all data read/write traffic directly between client and storage
B. It processes only metadata (file name, location, ACLs, attributes), while clients access storage devices directly via parallel data paths
C. It replaces the need for a storage network protocol such as iSCSI or FC
D. It functions as the FCoE Forwarder for the NAS cluster

**17.** (Medium) [Topic36] Which cache write implementation has a HIGHER risk of data loss but provides FASTER write response time, because acknowledgment is sent to the host before data is committed to disk?
A. Write-through cache
B. Write-back cache
C. Direct write cache
D. Mirrored write cache

**18.** (Hard) [DCE] Which type of flushing occurs when cache utilization hits the high watermark, dedicating additional resources and impacting I/O processing?
A. Idle flushing
B. High watermark flushing
C. Forced flushing
D. Background flushing

**19.** (Medium) [Topic36] The EMC Symmetrix VMAX series supports up to how many engines in a single system?
A. 2
B. 4
C. 8
D. 16

**20.** (Hard) [DCE] A database uses a block size of 4 KB and records average 200 bytes unspanned. If the file is ordered by a 12-byte key field and a block pointer is 8 bytes, what is the primary index blocking factor (bfri) on a 2 KB index block?
A. 85
B. 102
C. 128
D. 170

---

## Section A — Answer Key

| Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|
| 1 | B | 6 | C | 11 | B | 16 | B |
| 2 | C | 7 | B | 12 | B | 17 | B |
| 3 | C | 8 | C | 13 | C | 18 | B |
| 4 | C | 9 | C | 14 | B | 19 | C |
| 5 | B | 10 | B | 15 | B | 20 | B |

---

## Section B: Structural Questions (50 Marks)

*Answer ALL questions in this section.*

---

### Question 1 (12 Marks)

**(a)** Explain the four key components of an intelligent storage system (front end, cache, back end, physical disks) and the primary role of each in servicing an I/O request. **(6 marks)**

**(b)** Differentiate between a read hit and a read miss. Then explain how prefetch (read-ahead) improves performance for sequential workloads, and distinguish between fixed prefetch and variable prefetch. **(6 marks)**

#### Model Answer — Question 1

**(a)**
1. Front end — Interfaces between host and storage. Contains front-end ports and controllers that execute transport protocols (FC, iSCSI, FICON, FCoE) and route data to/from cache via the internal data bus.
2. Cache — Semiconductor memory that temporarily holds data, isolating the host from mechanical disk delays. A write is acknowledged from cache, and reads are served from cache when possible (~1 ms).
3. Back end — Interfaces between cache and physical disks. Controls data transfers, performs error detection/correction, and executes RAID functionality.
4. Physical disks — Provide persistent storage. For reads, the back end retrieves data from the appropriate disk when a cache miss occurs.

**(b)**
- A read hit occurs when requested data is found in cache; it is sent directly to the host without disk access (~1 ms).
- A read miss occurs when data is not in cache; the back end must retrieve it from disk, increasing response time.
- Prefetch (read-ahead) improves sequential workload performance by speculatively reading additional contiguous blocks from disk into cache before the host requests them, converting future misses into hits.
- Fixed prefetch reads a constant amount irrespective of request size. Variable prefetch reads an amount that is a multiple of the host's request size, adapting to workload patterns.

---

### Question 2 (12 Marks)

**(a)** Explain the three types of flushing in cache management (idle flushing, high watermark flushing, and forced flushing), and describe the role of the high watermark (HWM) and low watermark (LWM). **(6 marks)**

**(b)** Compare and contrast cache mirroring and cache vaulting as cache data protection mechanisms. For each, state the specific failure scenario it addresses and one limitation. **(6 marks)**

#### Model Answer — Question 2

**(a)**
- Idle flushing: Occurs continuously at a modest rate when cache utilization is between HWM and LWM. It keeps some free pages available without heavy I/O impact.
- High watermark flushing: Activated when cache utilization hits HWM. The storage system dedicates additional resources for flushing, which has some impact on I/O processing.
- Forced flushing: Occurs when cache reaches 100% capacity (typically during a large I/O burst). The system flushes cache on priority by allocating more resources, significantly affecting I/O response time.
- HWM is the cache utilization level that triggers high-speed flushing. LWM is the level at which flushing stops.

**(b)**
- Cache mirroring addresses cache memory card/module failure. Every write is held in two independent memory locations; if one fails, data survives in the mirrored location. It does not protect against extended power failure. It also introduces cache coherency requirements (the two copies must remain identical).
- Cache vaulting addresses extended power failure. Because batteries cannot sustain power long enough to flush large caches to disk, the entire cache content is dumped onto dedicated vault drives. When power is restored, data is written back to cache and then to intended disks. It requires dedicated vault drive capacity.

---

### Question 3 (13 Marks)

**(a)** Explain the difference between traditional (thick) LUNs and thin LUNs in terms of allocation strategy, capacity utilization, and oversubscription. **(4 marks)**

**(b)** Explain concatenated metaLUN and striped metaLUN expansion. For each, state whether component LUNs must match the base LUN in capacity and RAID level, and whether performance improves. **(4 marks)**

**(c)** A storage administrator creates a RAID set from five 1 TB drives but mixes 10,000 RPM drives with 15,000 RPM drives. Explain the negative consequences for the RAID set's performance and reliability, and state the best practice regarding drive homogeneity. **(5 marks)**

#### Model Answer — Question 3

**(a)**
- Traditional (thick) LUNs: Physical storage is fully pre-allocated at creation time from a RAID set. Capacity is reserved even if unused, leading to over-provisioning and lower utilization.
- Thin LUNs: Physical storage is allocated on-demand from a shared pool. Only written data consumes capacity, improving utilization and enabling oversubscription (presenting more capacity than physically exists).
- Oversubscription is possible only with thin LUNs because unused capacity is not reserved.

**(b)**
- Concatenated metaLUN: Appends component LUNs to increase capacity. Component LUNs need not match the base LUN in capacity. RAID types can be mixed (except RAID 0 can only concatenate with RAID 0). No performance improvement.
- Striped metaLUN: Restripes data across the base and component LUNs. All LUNs must be identical in capacity and RAID level. Performance improves because data is distributed across more drives.

**(c)** Mixing drive speeds causes the RAID set to operate at the speed of the slowest drive, lowering overall throughput. Mixing capacities causes the smallest drive's capacity to be used from each disk, wasting the extra capacity on larger drives. Best practice: RAID sets should be created from drives of the same type, speed, and capacity.

---

### Question 4 (13 Marks)

**(a)** Describe the structure and components of a disk drive (platter, spindle, read/write head, actuator arm assembly, controller board). For each component, state one function relevant to I/O performance. **(6 marks)**

**(b)** Define seek time, rotational latency, and data transfer rate as components of disk service time. Using the formula Ts = T_seek + L + X, calculate the service time for a disk with average seek time 6 ms, 15,000 RPM spindle, and 80 MB/s internal transfer rate for a 16 KB block. **(4 marks)**

**(c)** For a 7200 RPM drive with an average seek time of 9 ms and a 40 MB/s transfer rate, calculate: (i) average rotational latency, (ii) internal transfer time for an 8 KB block, (iii) maximum IOPS at near-full utilization, and (iv) the number of disks required to meet an application requirement of 6,000 IOPS assuming 70% utilization limit. **(3 marks)**

#### Model Answer — Question 4

**(a)**
- Platter: Rigid disk coated with magnetic material; stores data as magnetic polarization. More platters increase capacity but add mass, slightly affecting rotational latency.
- Spindle: Connects platters and rotates them at constant speed (e.g., 15,000 RPM). Higher RPM reduces rotational latency but increases power and heat.
- Read/write head: Reads and writes data by detecting/changing magnetic polarization. Flying height affects reliability; head crash causes data loss.
- Actuator arm assembly: Positions the R/W heads over the correct track. Seek time is determined by actuator speed.
- Controller board: Contains firmware controlling spindle motor speed, R/W head movement, and communication with the host.

**(b)**
- Seek time (T_seek): Time to position the R/W head over the correct track.
- Rotational latency (L): Time for the platter to rotate the requested sector under the head.
- Data transfer rate (X): Time to transfer the data between disk and host.
- Ts = 6 ms + (0.5 / 250 rps) + (16 KB / 80 MB/s) = 6 + 2 + 0.2 = 8.2 ms.

**(c)**
(i) L = 0.5 / (7200/60) = 0.5 / 120 = 4.17 ms.
(ii) X = 8192 / (40 x 1024 x 1024) = 8192 / 41,943,040 = 0.195 ms.
(iii) Ts = 9 + 4.17 + 0.195 = 13.365 ms. IOPS = 1 / 0.013365 = 74.8 IOPS.
(iv) At 70% utilization: 74.8 x 0.7 = 52.4 IOPS per disk. Disks required = ceil(6000 / 52.4) = 115 disks.

---

*End of Exam Set 3*

---

# EXAM SET 4 — Storage Networking, Modern Storage Architectures, and Integration

**Coverage in this set:** Fibre Channel SAN components and topologies · FC addressing, ports, and classes of service · Zoning and LUN masking · IP SAN (iSCSI) and FCoE · NAS architectures and protocols · Flash drives and SSDs · Object-based and unified storage · Integration of physical database design with storage infrastructure

---

## Section A: Multiple Choice Questions (20 Marks)

*Choose the best answer for each question. 1 mark each.*

**1.** (Medium) [Topic36] What is the primary function of the front-end controller in an intelligent storage system?
A. It manages cache flushing between HWM and LWM
B. It executes the transport protocol (FC, iSCSI, FICON, FCoE) and routes data to/from cache
C. It performs RAID parity calculations
D. It controls spindle motor speed

**2.** (Hard) [Topic36] In a B+-tree internal node of order p, what is the minimum number of children (tree pointers) that a non-root node must have?
A. 1
B. ⌈p/2⌉
C. p – 1
D. p

**3.** (Medium) [Topic36] Which Fibre Channel port type is a generic port that can function as either an E_Port or an F_Port depending on what it connects to?
A. N_Port
B. F_Port
C. E_Port
D. G_Port

**4.** (Hard) [Topic36] In a 24-bit FC address (Domain ID, Area ID, Port ID), how many usable domains are there in a switched fabric?
A. 256
B. 239
C. 255
D. 126

**5.** (Medium) [DCE] Which interface protocol provides serial transmission over copper or fiber and is widely used for high-speed host-to-storage communication?
A. IDE/ATA
B. SCSI
C. Fibre Channel
D. USB

**6.** (Hard) [DCE] A disk drive advertises 500 GB capacity. What is the approximate user-data capacity available after formatting?
A. 500 GB
B. 465.7 GB
C. 512 GB
D. 488 GB

**7.** (Medium) [PBD-I] In a heap file, what is the time complexity of searching for a record using linear search?
A. O(1)
B. O(log n)
C. O(n)
D. O(n log n)

**8.** (Hard) [PBD-I] For a sorted file with b = 4,000 blocks, what is the approximate number of block accesses required for binary search?
A. 4
B. 8
C. 12
D. 16

**9.** (Medium) [PBD-II] What is the blocking factor (bfr) for a file with block size B = 2,048 bytes and record size R = 256 bytes under unspanned allocation?
A. 4
B. 8
C. 16
D. 32

**10.** (Hard) [PBD-I] In a disk service time formula Ts = T_seek + L + X, if the spindle speed is doubled while all other parameters remain constant, which component is directly affected and how?
A. Seek time is halved
B. Rotational latency is halved
C. Transfer rate is halved
D. Transfer time is halved

**11.** (Medium) [Topic36] Which intelligent storage system type uses active-active configuration, allowing a host to perform I/O to its LUNs through any available controller?
A. Midrange storage system
B. High-end storage system
C. DAS array
D. JBOD enclosure

**12.** (Hard) [DCE] Which command is used on DOS, OS/2, and Microsoft Windows to check file system consistency?
A. fsck
B. chkdsk
C. fdisk
D. format

**13.** (Medium) [PBD-I] Which RAID level uses block-level striping with distributed parity across all disks?
A. RAID 0
B. RAID 1
C. RAID 3
D. RAID 5

**14.** (Hard) [Topic36] In iSCSI, what ensures that every command is delivered to the SCSI layer in the same order in which it was transmitted, regardless of which TCP connection carries it?
A. Session ID (SSID)
B. Command Sequence Number (CmdSN)
C. Data Sequence Number (DataSN)
D. Target Port Group Tag (TPGT)

**15.** (Medium) [DCE] In a virtualized host environment, to what does the hypervisor assign a LUN?
A. A raw disk visible directly to guest VMs
B. The hypervisor file system, where virtual disks are created
C. A physical partition on the host boot drive
D. A dedicated iSCSI target

**16.** (Hard) [PBD-II] In a multilevel index with fan-out 64 and 4,096 first-level blocks, how many block accesses are required to locate a data block (excluding the final data access)?
A. 1
B. 2
C. 3
D. 4

**17.** (Medium) [DCE] Which storage device uses magnetic media and supports rapid random access, making it suitable for online transaction processing?
A. Tape drive
B. Optical disc
C. Disk drive
D. Flash drive

**18.** (Hard) [Topic36] What does the dirty bit flag in tag RAM indicate?
A. Whether the cache page is currently being written to disk
B. Whether the cached data has been modified but not yet committed to disk
C. Whether the cache page is reserved for reads only
D. Whether the cache page is full

**19.** (Medium) [PBD-I] Which of the following is NOT a dynamic hashing technique?
A. Extendible hashing
B. Linear hashing
C. Static hashing
D. All of the above are dynamic

**20.** (Hard) [DCE] According to the utilization-versus-response-time curve, what happens to response time when utilization exceeds approximately 70%?
A. It increases linearly
B. It increases exponentially
C. It remains constant
D. It decreases slightly

---

## Section A — Answer Key

| Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|
| 1 | B | 6 | B | 11 | B | 16 | B |
| 2 | B | 7 | C | 12 | B | 17 | C |
| 3 | D | 8 | C | 13 | D | 18 | B |
| 4 | B | 9 | B | 14 | B | 19 | C |
| 5 | C | 10 | B | 15 | B | 20 | B |

---

## Section B: Structural Questions (50 Marks)

*Answer ALL questions in this section.*

---

### Question 1 (12 Marks)

**(a)** Describe the five layers of the iSCSI protocol stack and explain how SCSI commands are encapsulated for transmission over an IP network. **(6 marks)**

**(b)** What is the role of the Fibre Channel Forwarder (FCF) in an FCoE switch, and why is jumbo frame support important for FCoE performance? **(6 marks)**

#### Model Answer — Question 1

**(a)** The iSCSI protocol stack maps to the OSI model as follows:
- Layer 7 (Application): SCSI — commands and data exchanged between initiator and target.
- Layer 5 (Session): iSCSI — handles login, authentication, target discovery, and session management.
- Layer 4 (Transport): TCP — provides reliable transmission, flow control, error recovery, and retransmission.
- Layer 3 (Network): IP — provides global addressing and packet routing.
- Layer 2 (Data Link): Ethernet — enables node-to-node communication through frames.

SCSI commands and data are encapsulated into iSCSI Protocol Data Units (PDUs), which are encapsulated into TCP segments, then into IP packets, and finally into Ethernet frames for transmission.

**(b)** The Fibre Channel Forwarder (FCF) resides within an FCoE switch and performs two functions: (1) encapsulating native FC frames received from the FC port into FCoE frames for transmission over Ethernet, and (2) de-encapsulating FCoE frames back into native FC frames for delivery to FC end-devices. Jumbo frames are important because a standard Ethernet frame payload is 1,500 bytes, while a typical FC frame payload is up to 2,112 bytes; without jumbo frames, an FC frame would be fragmented across multiple Ethernet frames, harming performance.

---

### Question 2 (12 Marks)

**(a)** What is a journaling file system, and how does it maintain file system consistency after a crash? **(4 marks)**

**(b)** Differentiate between NFSv3 and NFSv4 in terms of statefulness, transport protocol, and key features. **(4 marks)**

**(c)** Explain the concept of pNFS and the role of the metadata server versus the data server. **(4 marks)**

#### Model Answer — Question 2

**(a)** A journaling file system uses a separate area called a log or journal to record pending metadata (and optionally data) changes before they are committed to the file system. If the system crashes during an operation, the journal contains enough information to replay the incomplete transaction and restore consistency, avoiding the lengthy fsck/chkdsk scan required by non-journaling file systems.

**(b)**
- NFSv3 is stateless (no open-file information retained between calls), supports both UDP and TCP, and uses 64-bit file sizes with asynchronous writes. NFSv4 is stateful, uses TCP only, and introduces enhanced security, locking, and delegation.
- NFSv4.1 adds the session model and parallel NFS (pNFS).

**(c)** pNFS (parallel NFS) separates metadata processing from data processing. The metadata server handles file name resolution, location, ACLs, and attributes. Clients access storage devices directly via parallel data paths using a protocol like iSCSI or FC, bypassing the metadata server for actual data transfer. This improves client performance by eliminating the metadata server as a bottleneck for large data transfers.

---

### Question 3 (13 Marks)

**(a)** Using the disk service time formula, calculate the maximum IOPS for a 5,400 RPM drive with an average seek time of 5 ms and an internal transfer rate of 40 MB/s for a 4 KB block. Show all steps. **(5 marks)**

**(b)** An application requires 500 GB of storage and 3,500 IOPS at peak. Available disks are 146 GB, 15,000 RPM drives rated at 180 max IOPS. The application is response-time-sensitive, so utilization must not exceed 70%. Calculate the minimum number of disks required to meet both capacity and IOPS requirements. **(4 marks)**

**(c)** Explain why the IOPS requirement typically drives the disk count in performance-sensitive applications, even when capacity requirements are modest. **(4 marks)**

#### Model Answer — Question 3

**(a)**
- Rotational speed = 5,400 RPM = 90 rps.
- Average rotational latency L = 0.5 / 90 = 5.56 ms.
- Transfer rate = 40 MB/s = 41,943,040 bytes/s.
- Block size = 4 KB = 4,096 bytes.
- Internal transfer time X = 4096 / 41,943,040 = 0.0977 ms.
- Ts = 5 + 5.56 + 0.0977 = 10.6577 ms.
- Max IOPS = 1 / 0.0106577 = 93.8 IOPS.

**(b)**
- Capacity disks: D_C = ceil(500 / 146) = 4 disks.
- IOPS at 70% utilization per disk = 180 x 0.7 = 126 IOPS.
- IOPS disks: D_I = ceil(3,500 / 126) = ceil(27.78) = 28 disks.
- Total disks D_R = Max(4, 28) = 28 disks.

**(c)** A single disk may provide ample capacity (e.g., 146 GB is more than enough for 500 GB requirement when considering 4 disks), but its IOPS capability is limited by mechanical latency. High IOPS applications (e.g., databases with many small random writes) require many spindles to parallelize I/O. Thus, the IOPS requirement dominates the disk count, often requiring far more disks than capacity alone would suggest.

---

### Question 4 (13 Marks)

**(a)** Define the five factors that influence physical database design according to the lecture notes. For each factor, state its practical implication in one sentence. **(5 marks)**

**(b)** Apply three of the five factors to the design of a primary index on the ORDER table of an e-commerce database. Assume the table is ordered by OrderDate and contains 10 million rows. **(4 marks)**

**(c)** Explain why a clustering index on a nonkey attribute (e.g., CustomerId on the ORDER table) is generally preferred over a secondary index for queries that retrieve all orders for a specific customer. **(4 marks)**

#### Model Answer — Question 4

**(a)**
1. Query/transaction analysis — Identify which files, selection conditions, and join attributes are used, so indexing effort targets actual access paths.
2. Frequency of invocation — Focus indexing on the 20% of queries that consume 80% of the workload.
3. Time constraints — Prioritize indexing for transactions with strict response-time requirements.
4. Frequency of updates — Limit indexes on heavily updated files to avoid excessive insert/delete overhead.
5. Uniqueness constraints — Create indexes on candidate keys to enable efficient uniqueness enforcement.

**(b)**
- Query analysis: Range queries on OrderDate (e.g., orders between two dates) benefit from a clustered order.
- Frequency: If 70% of queries filter by date, the index is high-value.
- Uniqueness: If OrderId is unique, it should be the primary key with a primary index.

**(c)** A clustering index on CustomerId physically groups all rows with the same CustomerId together. Retrieving all orders for a customer requires reading a contiguous range of blocks. A secondary index on CustomerId would require following pointers scattered across the file, causing many random I/Os.

---

*End of Exam Set 4*

