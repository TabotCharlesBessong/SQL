# MIST Master's Examination — Practice Set
## Data Center Environment: Intelligent Storage Systems & Fibre Channel SAN

**Coverage:** Chapter 4 (Intelligent Storage Systems — Front End, Cache, Back End, LUN/MetaLUN, Virtual Provisioning, LUN Masking, High-End vs Midrange arrays, EMC Symmetrix/VNX) and Chapter 5 (Fibre Channel SAN — FC overview, SAN evolution, FC SAN components: nodes/ports, cables/connectors, interconnect devices, FC connectivity options)

**Format:** 20 MCQs (Medium–Hard) · Structural Questions (30 Marks) · Essay Questions (50 Marks)

---

# SECTION A: Multiple Choice Questions (20 Questions)

*Each question has one correct answer. Difficulty is indicated. Answers and explanations follow at the end of this section.*

---

**1.** (Medium) In an intelligent storage system, which component is responsible for executing the transport protocol (such as Fibre Channel, iSCSI, FICON, or FCoE) used to communicate with the host?

A. Back-end controller
B. Front-end controller
C. Cache controller
D. Physical disk controller

---

**2.** (Medium) What is the smallest unit of cache allocation in an intelligent storage system?

A. Block
B. Sector
C. Page
D. Segment

---

**3.** (Hard) In the structure of cache, which component tracks the location of data in the data store and on the disk, and contains the dirty bit flag?

A. Data store
B. Tag RAM
C. Front-end buffer
D. Vault drive

---

**4.** (Medium) A host requests data and the storage controller finds it already in cache, delivering it without any disk operation. What is this event called?

A. Cache miss
B. Read hit
C. Write-through
D. Forced flush

---

**5.** (Hard) A storage system prefetches an amount of data that is a multiple of the size of the host's read request. Which prefetching strategy is being used?

A. Fixed prefetch
B. Maximum prefetch
C. Variable prefetch
D. Adaptive prefetch

---

**6.** (Medium) Which cache write implementation sends an acknowledgment to the host immediately after data is placed in cache, deferring the actual disk write to a later time?

A. Write-through cache
B. Write-around cache
C. Write-back cache
D. Direct write cache

---

**7.** (Hard) Which write cache implementation provides a lower risk of data loss, but at the cost of a longer write-response time, because data is committed to disk immediately upon arrival in cache?

A. Write-back cache
B. Write-through cache
C. Cache vaulting
D. Cache mirroring

---

**8.** (Medium) Which cache management algorithm frees up cache pages that have NOT been accessed for the longest period of time, based on the assumption that such data is unlikely to be requested soon?

A. Most Recently Used (MRU)
B. First In First Out (FIFO)
C. Least Recently Used (LRU)
D. Round Robin

---

**9.** (Hard) At which cache utilization point does an intelligent storage system activate "idle flushing"?

A. When cache reaches 100% utilization
B. When cache utilization is between the Low Watermark (LWM) and High Watermark (HWM)
C. Only when a forced flush is triggered
D. When cache utilization falls below the Low Watermark

---

**10.** (Hard) Which technique protects cache data against a cache memory card failure by storing every write in two independent memory locations?

A. Cache vaulting
B. Cache mirroring
C. Write-through caching
D. RAID striping

---

**11.** (Medium) During an extended power failure, what mechanism is used to preserve uncommitted cache data when battery power alone is insufficient to write all the data to its intended disks?

A. Cache mirroring
B. Cache vaulting (using vault drives)
C. Write-back caching
D. LUN masking

---

**12.** (Medium) What is the term used for a unique identifier assigned to a logical unit created by partitioning a RAID set, which hides the underlying RAID composition from the host?

A. World Wide Name (WWN)
B. Logical Unit Number (LUN)
C. MetaLUN
D. VSAN ID

---

**13.** (Hard) Which type of metaLUN expansion restripes the base LUN's data across the base LUN and component LUNs, requiring all LUNs to be the same capacity and RAID level, and offering improved performance?

A. Concatenated expansion
B. Striped expansion
C. Mirrored expansion
D. Virtual expansion

---

**14.** (Medium) What is a LUN created using virtual provisioning called, to distinguish it from a traditional LUN?

A. Thick LUN
B. MetaLUN
C. Thin LUN
D. Virtual LUN

---

**15.** (Hard) In virtual storage provisioning, what is the term for presenting hosts with more total LUN capacity than is physically available in the storage array?

A. RAID expansion
B. Oversubscription
C. LUN masking
D. Cache vaulting

---

**16.** (Medium) What is the primary purpose of LUN masking in a shared storage environment?

A. To increase the speed of read operations
B. To control which hosts can access specific LUNs, preventing unauthorized access
C. To compress data before writing to disk
D. To balance load between front-end and back-end controllers

---

**17.** (Medium) Which type of intelligent storage system architecture allows a host to perform I/O to a LUN through ANY of the available controllers?

A. Active-passive (midrange storage systems)
B. Active-active (high-end storage systems)
C. Passive-passive
D. Direct-attached storage

---

**18.** (Hard) In an FC network, what describes the data transmission capability of a node port that has both a transmit (Tx) link and a receive (Rx) link operating simultaneously?

A. Half-duplex
B. Simplex
C. Full-duplex
D. Multiplex

---

**19.** (Hard) Which optical fiber type carries a single ray of light projected at the center of the core, provides minimum signal attenuation, and is suited for long-distance cable runs of up to 10 km?

A. Multimode fiber (MMF)
B. Single-mode fiber (SMF)
C. Coaxial cable
D. Twisted pair cable

---

**20.** (Hard) What is the key architectural difference between an FC switch and an FC hub that allows switches to support significantly more nodes (over 15 million) compared to hubs (a maximum of 126 nodes)?

A. Switches use copper cabling while hubs use fiber optic cabling
B. Switches provide dedicated bandwidth per port (full bandwidth between port pairs) while hubs require all nodes to share the loop bandwidth
C. Switches only support FC-AL while hubs support switched fabric
D. Hubs have more processing power than switches

---

## Answer Key & Explanations — Section A

| Q | Answer | Explanation |
|---|---|---|
| 1 | **B** | The front-end controller contains the processing logic that executes the transport protocol (FC, iSCSI, FICON, FCoE) for host connectivity. |
| 2 | **C** | A cache page is the smallest unit of cache allocation; its size is configured according to application I/O size. |
| 3 | **B** | Tag RAM tracks data location in the data store and on disk, and holds the dirty bit flag and time-based access information; the data store holds the actual data. |
| 4 | **B** | A read hit occurs when requested data is found in cache and sent directly to the host without disk access. |
| 5 | **C** | Variable prefetch reads an amount of data that is a multiple of the host's request size, adapting to the request pattern (unlike fixed prefetch, which always reads a constant amount). |
| 6 | **C** | Write-back cache acknowledges the host immediately upon placing data in cache; the actual disk write (de-staging) happens later, improving response time but creating a data-loss risk if cache fails before de-staging. |
| 7 | **B** | Write-through cache writes to disk immediately as data arrives, so risk of data loss is low, but the host wait time is longer because the write-response time includes disk latency. |
| 8 | **C** | LRU identifies and frees cache pages that have not been accessed for the longest time, assuming such data is unlikely to be needed again soon. MRU does the opposite. |
| 9 | **B** | Idle flushing occurs continuously at a modest rate when cache utilization sits between the LWM and HWM — this is the "normal operating" flushing mode. |
| 10 | **B** | Cache mirroring stores each write in two independent memory locations/cards so that a single card failure does not lose data; only writes are mirrored (reads can be re-staged from disk). |
| 11 | **B** | Cache vaulting dumps the entire cache content onto a dedicated set of physical disks (vault drives) during an extended power failure, since batteries alone cannot sustain writing all data to its final disk destinations. |
| 12 | **B** | The Logical Unit Number (LUN) is the unique ID assigned to a logical unit carved from a RAID set; it hides the underlying RAID set organization from the host. |
| 13 | **B** | Striped expansion restripes data across base + component LUNs (all same capacity/RAID level) for improved performance, unlike concatenated expansion which only adds capacity with no performance benefit. |
| 14 | **C** | A "thin LUN" is the term for a LUN created via virtual provisioning, distinguishing it from a traditional ("thick") LUN that has all its capacity physically allocated upfront. |
| 15 | **B** | Oversubscription is presenting more total capacity to hosts than is physically available on the array, enabled by virtual provisioning's on-demand allocation model. |
| 16 | **B** | LUN masking is an access-control mechanism implemented on the storage array that defines and restricts which hosts can access which LUNs, preventing unauthorized or accidental access. |
| 17 | **B** | Active-active configuration (characteristic of high-end storage systems) allows a host to perform I/O to a LUN through any available controller, unlike active-passive (midrange) systems, where only the owning controller's path is active. |
| 18 | **C** | Full-duplex mode means a port can transmit (Tx) and receive (Rx) data simultaneously over separate links — this is standard for FC node ports. |
| 19 | **B** | Single-mode fiber (SMF) carries a single light ray through a small core, minimizing modal dispersion and signal attenuation, making it ideal for long-distance runs (up to 10 km), unlike multimode fiber (MMF) which is for short distances. |
| 20 | **B** | FC switches provide full, dedicated bandwidth between each pair of communicating ports (no sharing), enabling massive scalability (15+ million node addressing), while FC-AL hubs force all nodes to share the same loop bandwidth, limiting them to 126 nodes and one communication at a time. |

---

# SECTION B: Structural Questions (30 Marks)

*Answer all questions. Marks are indicated in brackets.*

---

### Question 1 (10 Marks)

**(a)** Name and briefly describe the four key components of an intelligent storage system. **[8 marks]**

**(b)** Explain why, in modern intelligent storage systems, the front end, cache, and back end are typically integrated onto a single board. **[2 marks]**

#### Model Answer

**(a) The four key components [8 marks — 2 marks each]:**

1. **Front End** — Provides the interface between the storage system and the host. It consists of front-end ports and front-end controllers. Controllers execute the transport protocol (FC, iSCSI, FICON, FCoE) and route data to/from cache via the internal data bus; they also send write acknowledgments back to the host.

2. **Cache** — Semiconductor memory used to temporarily hold data, reducing the time required to service host I/O requests by isolating the host from the mechanical delays of rotating disks.

3. **Back End** — Provides the interface between cache and the physical disks; it consists of back-end ports and controllers that manage the physical disk drives and the transfer of data between them and cache.

4. **Physical Disks** — Store data persistently. They are the slowest component of the system (seek time and rotational latency cause multi-millisecond access), which is why cache exists to mitigate this bottleneck.

**(b) Reason for integration [2 marks]:**

Integrating front end, cache, and back end onto a single board (the storage processor/controller) reduces internal data transfer latency between components, simplifies the physical design and manufacturing, lowers cost, and improves reliability by reducing the number of separate interconnects and points of potential failure.

---

### Question 2 (10 Marks)

**(a)** Differentiate between write-back cache and write-through cache in terms of mechanism, performance, and data-loss risk. **[6 marks]**

**(b)** Explain what is meant by "write aside size" and describe the circumstance under which cache is bypassed for a write operation. **[4 marks]**

#### Model Answer

**(a) Write-back vs Write-through [6 marks]:**

| Aspect | Write-back Cache | Write-through Cache |
|---|---|---|
| **Mechanism** | Data is placed in cache; acknowledgment sent to host immediately; data is de-staged (committed) to disk later, often as a batch | Data is placed in cache and immediately written to disk; acknowledgment is sent to host only after the disk write completes |
| **Performance** | Faster write response time (host is isolated from disk mechanical delays) | Slower write response time (host must wait for the disk operation to complete) |
| **Data-loss risk** | Higher — uncommitted data in cache is lost if a cache failure occurs before de-staging | Lower — data is committed to disk as it arrives, so there is minimal data at risk |

**(b) Write aside size [4 marks]:**

The write aside size is a predefined I/O size threshold. If an incoming write I/O request exceeds this size, the storage system bypasses cache entirely and writes the data directly to disk. This is done to prevent large write I/Os from consuming a disproportionate amount of cache space, preserving cache capacity for the small, random I/Os that benefit most from caching. This is particularly useful in cache-constrained environments.

---

### Question 3 (10 Marks)

**(a)** Distinguish between a traditional ("thick") LUN and a thin LUN created through virtual provisioning, in terms of how physical storage is allocated. **[4 marks]**

**(b)** A 2 TB storage array uses traditional provisioning to create three LUNs of sizes 500 GB, 550 GB, and 800 GB. Only 100 GB, 50 GB, and 200 GB of actual data are stored in each LUN respectively. Calculate:
  - (i) The total allocated capacity. **[2 marks]**
  - (ii) The total unused (allocated but not consumed) capacity. **[2 marks]**
  - (iii) The remaining capacity available for other applications. **[2 marks]**

#### Model Answer

**(a) Thick LUN vs Thin LUN [4 marks]:**

A **traditional (thick) LUN** has its entire capacity physically allocated from the RAID set at the time it is created, regardless of how much data is actually stored — unused allocated space cannot be used by any other LUN.

A **thin LUN** (virtual provisioning) is presented to the host with a specified logical capacity, but physical storage is allocated "on-demand" from a shared pool only as data is actually written. Unused logical capacity does not consume physical disk space, allowing more efficient utilization and oversubscription.

**(b) Calculations [6 marks total]:**

(i) **Total allocated capacity** = 500 + 550 + 800 = **1,850 GB (1.85 TB)** [2 marks]

(ii) **Total unused (allocated but unconsumed) capacity:**
- LUN 1: 500 − 100 = 400 GB
- LUN 2: 550 − 50 = 500 GB
- LUN 3: 800 − 200 = 600 GB
- Total unused = 400 + 500 + 600 = **1,500 GB (1.5 TB)** [2 marks]

(iii) **Remaining capacity available for other applications:**
Total array capacity (2,048 GB ≈ 2 TB) − Total allocated (1,850 GB) = **≈ 150–198 GB** (using the textbook's approximation of 2 TB = 2,000 GB: 2,000 − 1,850 = **150 GB**) [2 marks]

*(Accept either the exact 2,048 GB-based calculation or the textbook's rounded 2,000 GB figure, provided the method is shown correctly.)*

---

# SECTION C: Essay Questions (50 Marks)

*Answer all questions. Marks are indicated in brackets.*

---

### Essay Question 1 (25 Marks)

**Critically discuss the role of cache in an intelligent storage system. Your answer should address: the structure of cache, how read and write operations are handled, the algorithms used to manage finite cache resources, and the mechanisms used to protect cache data against failure.**

#### Model Answer

**Introduction [2 marks]**

Cache is semiconductor memory in an intelligent storage system used to temporarily hold data in order to reduce the time required to service host I/O requests. It is a critical performance enabler because it isolates the host from the mechanical delays inherent to rotating disk drives — disk access typically takes several milliseconds due to seek time and rotational latency, whereas cache access takes less than a millisecond. However, cache is a finite, volatile, and expensive resource, which means it must be carefully structured, managed, and protected.

**Structure of Cache [4 marks]**

Cache is organized into pages, the smallest unit of cache allocation, with page size configured according to the application's I/O size. Cache consists of two logical parts:
- The **data store**, which holds the actual cached data.
- The **tag RAM**, which tracks where each piece of data is located within the data store and where it belongs on disk.

Tag RAM also contains a **dirty bit flag** indicating whether cached data has been committed to disk, and time-based information (such as last access time) that supports cache management decisions about which pages can be safely freed.

**Read Operations with Cache [4 marks]**

When a host issues a read request, the storage controller consults the tag RAM to determine if the requested data resides in cache:
- A **read hit** occurs when the data is found in cache; it is sent directly to the host with no disk operation, yielding response times of about one millisecond.
- A **read miss** occurs when the data is not in cache; the back end must retrieve it from the physical disk, place it in cache, and then forward it to the host — significantly increasing response time.

To improve hit rates for sequential workloads, storage systems use **prefetching (read-ahead)**: additional, not-yet-requested blocks are speculatively read from disk into cache. **Fixed prefetch** reads a constant amount of data (best for uniform host I/O sizes), while **variable prefetch** reads an amount proportional to the size of the host's request. A **maximum prefetch limit** caps how much data can be prefetched, preventing prefetch operations from monopolizing disk resources at the expense of other I/Os. Read performance is commonly measured using the **read hit ratio** — the percentage of read requests serviced as hits.

**Write Operations with Cache [4 marks]**

Two implementations govern how writes interact with cache:
- **Write-back cache**: data is placed in cache and the host receives an immediate acknowledgment; the data is later de-staged to disk, often coalescing multiple smaller writes into larger, more efficient disk transfers. This delivers superior write response time but exposes uncommitted data to loss if a cache failure occurs before de-staging.
- **Write-through cache**: data is written to cache and immediately to disk before acknowledgment; this lowers data-loss risk but increases write latency because the host must wait on the (slower) disk operation.

Storage systems can also **bypass cache** for very large writes that exceed a configured **write aside size**, sending such I/Os directly to disk to preserve cache capacity for smaller, random I/Os that benefit more from caching.

Cache can be implemented as **dedicated cache** (separate memory regions reserved for reads and writes) or **global cache** (a single pool shared dynamically between reads and writes, configurable by percentage and often dynamically adjusted based on workload). Global cache is generally more efficient to manage because only one set of addresses needs administration.

**Cache Management Algorithms [4 marks]**

Because cache is finite, the storage system must continuously identify pages that can be freed to make room for new data:
- **Least Recently Used (LRU)** frees pages that have not been accessed for the longest time, on the assumption that such data is unlikely to be requested again soon. If a page contains uncommitted ("dirty") write data, it must first be flushed to disk before reuse.
- **Most Recently Used (MRU)** does the opposite — it frees the most recently accessed pages, assuming that data just used is unlikely to be needed again immediately.

Cache space management is also governed by **watermarks**, which determine the urgency of flushing dirty pages to disk:
- **Idle flushing** occurs continuously at a modest rate when utilization sits between the Low Watermark (LWM) and High Watermark (HWM).
- **High watermark flushing** activates when utilization reaches the HWM; additional system resources are dedicated to flushing, with some I/O performance impact.
- **Forced flushing** occurs when cache hits 100% capacity (typically during large I/O bursts); the system prioritizes flushing aggressively, significantly affecting response time.

**Cache Data Protection [5 marks]**

Because cache is volatile memory, any power or hardware failure threatens uncommitted data. Two complementary mechanisms address this risk:

- **Cache mirroring**: every write is stored simultaneously in two independent memory locations on separate memory cards. If one card fails, the mirrored copy is still safe and can be committed to disk. Only writes are mirrored (since reads can always be re-staged from disk), which conserves cache capacity. This introduces the challenge of **cache coherency** — ensuring both mirrored copies remain identical at all times — which is managed by the array's operating environment.

- **Cache vaulting**: addresses power failure risk. Short outages can be bridged with battery power (either powering memory directly or using battery power to flush cache to disk), but extended outages exceed what batteries can sustain, especially given the volume of data that may need to be committed across numerous disks. In such cases, the entire cache content is dumped to a dedicated set of physical disks called **vault drives**. When power is restored, the vaulted data is read back into write cache and subsequently written to its intended disk locations.

**Conclusion [2 marks]**

Cache is the linchpin of intelligent storage system performance: it transforms the storage system's effective response time from the millisecond-plus realm of mechanical disks to sub-millisecond electronic speeds. However, its volatility and finite size necessitate carefully engineered algorithms (LRU/MRU, watermark-based flushing) for capacity management and dedicated resilience mechanisms (mirroring, vaulting) to guarantee that the performance benefits of caching do not come at the cost of data integrity.

---

### Essay Question 2 (25 Marks)

**Discuss the concept of LUNs in intelligent storage systems. Your answer should cover: how LUNs are created from RAID sets, the purpose and methods of LUN expansion (MetaLUN), the comparison between traditional and virtual storage provisioning, and the role of LUN masking in storage security.**

#### Model Answer

**Introduction [2 marks]**

A Logical Unit Number (LUN) is a fundamental abstraction in intelligent storage systems that allows the physical capacity of a RAID set to be divided, allocated, and presented to hosts in a controlled and secure manner. Understanding how LUNs are created, expanded, and provisioned — and how access to them is controlled — is essential to managing storage resources efficiently and securely in a shared, multi-host data center environment.

**LUN Creation from RAID Sets [4 marks]**

A RAID set combines the capacity of multiple physical disks into one large pool, governed by a chosen RAID level for performance and protection. Because RAID sets are typically large, they are partitioned into smaller, more manageable units called **logical units**, each of which is spread across all the physical disks belonging to that RAID set and assigned a unique identifier — the LUN. LUNs hide the underlying RAID set organization and composition from the host, presenting what appears to the operating system as a single raw disk. Traditionally provisioned LUNs (with capacity fully allocated up-front) are also called **thick LUNs**, a term used to distinguish them from virtually provisioned thin LUNs.

For a LUN to become usable: in a non-virtualized host, a bus scan identifies the LUN as a raw disk, which is then formatted with a file system and mounted. In a virtualized host environment, the LUN is assigned to the hypervisor, formatted with the hypervisor's file system, and virtual disks are created on top of it; these virtual disks are then assigned to individual virtual machines, which can also directly access an entire LUN when response-time sensitivity or clustering with a physical machine requires it.

**LUN Expansion: MetaLUN [5 marks]**

As application storage or performance requirements grow, a **metaLUN** allows expansion of an existing LUN by combining a base LUN with one or more component LUNs. Two expansion methods exist:

- **Concatenated expansion** simply appends additional capacity from component LUNs to the base LUN. Component LUNs need not match the base LUN's capacity. All LUNs must be either protected (parity/mirrored) or unprotected (RAID 0) consistently, though RAID types can otherwise be mixed (e.g., a RAID 1/0 LUN concatenated with a RAID 5 LUN) — except RAID 0, which can only concatenate with other RAID 0 LUNs. This method is fast to implement but provides no performance benefit, since data is simply appended rather than redistributed.

- **Striped expansion** restripes the base LUN's existing data across both the base and component LUNs. This requires all LUNs to share the same capacity and RAID level. Because data is now spread across a greater number of physical drives, striped expansion delivers a genuine performance improvement, unlike the concatenated approach.

In both expansion types, all participating LUNs must reside on the same disk-drive type (e.g., all Fibre Channel or all ATA), ensuring consistent performance characteristics across the metaLUN.

**Traditional vs Virtual Storage Provisioning [7 marks]**

**Traditional provisioning** allocates a LUN's entire declared capacity from physical disks immediately at creation time, regardless of actual data usage. Administrators frequently over-provision to avoid the operational disruption of expanding a LUN later or running out of space — but this leads to large amounts of "allocated but unused" capacity, increasing acquisition and operational costs while reducing overall utilization efficiency.

**Virtual provisioning** addresses this inefficiency by creating **thin LUNs**: a LUN is presented to the host with a specified logical capacity, but physical storage is drawn "on-demand" from a **shared pool** of physical disks only as data is actually written. A shared pool is conceptually similar to a RAID group (supporting a single RAID protection level) but can be much larger and may be homogeneous (single drive type) or heterogeneous (mixed drive types such as flash, FC, SAS, SATA). This enables **oversubscription** — presenting hosts with more total capacity than physically exists in the array — alongside non-disruptive expansion of both the thin LUN and the shared pool.

*Illustrative comparison (textbook example):* A 2 TB array with three traditionally provisioned LUNs (500 GB, 550 GB, 800 GB) consuming only 350 GB of actual data leaves 1.5 TB allocated-but-unused and just 150 GB available for other applications. The same array using thin LUNs of identical declared sizes, storing the same 350 GB of actual data, leaves 1.65 TB genuinely available — a dramatic utilization improvement.

**Use case distinction:** Thin LUNs suit applications that can tolerate some performance variability and whose space requirements are difficult to forecast, offering excellent space efficiency and reduced power/acquisition costs. Traditional (thick) LUNs suit applications requiring predictable performance and precise data placement control — useful when an administrator must isolate workloads across different RAID groups to avoid contention. Both LUN types can coexist within the same array, and administrators may migrate data between them as requirements evolve.

**LUN Masking and Storage Security [5 marks]**

**LUN masking** is an access-control function implemented at the storage array that explicitly defines which hosts are permitted to access which LUNs. Without LUN masking, any host connected to the storage network could potentially see and modify the data on any LUN, creating serious data-integrity and security risks in a shared, multi-tenant storage environment — for example, allowing a sales department host to inadvertently access and corrupt a finance department's LUN. By enforcing LUN masking, the storage array ensures that each host can only discover and operate on the LUNs explicitly designated for it, preventing both unauthorized access and accidental cross-department data exposure.

**Conclusion [2 marks]**

LUNs, their expansion via metaLUN, their provisioning model (traditional vs. virtual), and their access control via LUN masking collectively form the foundation of modern storage resource management. Together, these mechanisms allow data center administrators to balance performance predictability, capacity efficiency, scalability, and security — core requirements of any enterprise storage strategy.

---

*End of Practice Examination Set — Data Center Environment: Intelligent Storage Systems & Fibre Channel SAN*
