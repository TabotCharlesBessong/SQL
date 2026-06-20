# MIST Master's Examination — Practice Set
## Data Center Environment & Introduction to RAID

**Coverage:** Chapter 2 (Data Center Environment — Application, DBMS, Host/Compute, Operating System, Volume Manager, File System, Compute/Memory/Desktop Virtualization, Connectivity, Storage Media, Disk Drive Components, Zoned Bit Recording, Logical Block Addressing, Disk Drive Performance, Host Access to Data, Direct-Attached Storage, Storage Design Based on Application Requirements, Disk Native Command Queuing, Flash Drives, VMware ESXi) and the introductory portion of Chapter 3 (RAID Implementation Methods — Software and Hardware RAID)

**Format:** 20 MCQs (Medium–Hard) · Structural Questions (30 Marks) · Essay Questions (50 Marks)

---

# SECTION A: Multiple Choice Questions (20 Questions)

*Each question has one correct answer. Difficulty is indicated. Answers and explanations follow at the end of this section.*

---

**1.** (Medium) What is the role of the Logical Volume Manager (LVM) in a host system?

A. It executes application-level business logic
B. It serves as an intermediate layer between the file system and the physical disk, managing logical and physical storage
C. It replaces the operating system entirely
D. It performs RAID parity calculations exclusively

---

**2.** (Medium) In LVM terminology, what is a "physical extent"?

A. A unique identifier assigned to a volume group
B. An equal-sized data block into which each physical volume is partitioned when a volume group is created
C. The total capacity of a logical volume
D. A backup copy of the volume group metadata

---

**3.** (Hard) Why can a logical volume be made up of "noncontiguous physical extents" and potentially span multiple physical volumes?

A. Because the LVM converts physical storage into a logical abstraction, decoupling the logical volume's contiguous appearance to the OS from its actual underlying physical layout
B. Because logical volumes are always smaller than a single physical extent
C. Because file systems require fragmented storage to function correctly
D. Because physical volumes cannot be grouped into volume groups

---

**4.** (Medium) What is the primary disadvantage of a nonjournaling file system compared to a journaling file system?

A. Nonjournaling file systems are always faster but use more disk space
B. Nonjournaling file systems risk losing or corrupting data/metadata if the system crashes during a write, and require a lengthy consistency check on reboot
C. Nonjournaling file systems cannot support directories
D. Nonjournaling file systems do not support permissions

---

**5.** (Hard) A journaling file system writes changes to a separate log area before applying them to the file system. What specific benefit does this provide during crash recovery, and what is the principal trade-off?

A. Benefit: no trade-off exists. The journal is purely beneficial with no downside
B. Benefit: only the active/recently-accessed parts of the file system need checking after a crash (fast recovery using the log to replay operations); trade-off: extra write operations to the journal slow down normal file system operations
C. Benefit: eliminates the need for metadata entirely; trade-off: requires twice the storage capacity
D. Benefit: prevents all possible data loss; trade-off: only works with FAT32

---

**6.** (Medium) What is the function of compute virtualization, and what component implements it?

A. It eliminates the need for an operating system; implemented by the BIOS
B. It abstracts/masks physical hardware from the operating system, enabling multiple OS instances to run concurrently; implemented by a virtualization layer called the hypervisor
C. It only virtualizes storage, not compute resources; implemented by the LVM
D. It is implemented exclusively at the application layer

---

**7.** (Hard) In the context of memory virtualization, what is "swap space," and why is access to it slower than access to physical memory?

A. Swap space is a region of RAM reserved for the OS kernel; it is slower because the kernel has lower priority
B. Swap space is a portion of the disk drive that appears as physical memory to the OS; it is slower because disk access is inherently slower than RAM access
C. Swap space is a cache within the CPU; it is slower due to cache coherency overhead
D. Swap space does not exist in modern virtual memory implementations

---

**8.** (Medium) Which host interface protocol is described as supporting single-bit serial transmission, has largely replaced its parallel predecessor in newer systems, and (in revision 3.0) supports a data transfer rate up to 6 Gb/s?

A. SCSI
B. Fibre Channel
C. SATA (Serial ATA)
D. iSCSI

---

**9.** (Hard) Why does an advertised 500 GB disk drive provide only 465.7 GB of actual usable capacity?

A. Because 34.3 GB is reserved exclusively for the file system journal
B. Because drive manufacturers calculate capacity using a base of 10 (1 KB = 1,000 bytes), while operating systems typically calculate using a base of 2 (1 KB = 1,024 bytes), making the OS-reported usable capacity appear smaller than the advertised figure
C. Because RAID always consumes 7% of capacity for parity
D. Because flash memory wear-leveling reserves that space permanently

---

**10.** (Medium) What does Zoned Bit Recording (ZBR) achieve, and why is it more efficient than the older fixed-sector-per-track approach?

A. It assigns the same number of sectors to every track regardless of position, simplifying the controller
B. It groups tracks into zones based on distance from the center, assigning more sectors per track to outer zones (which are physically longer), making more efficient use of available disk surface area
C. It eliminates the need for tracks entirely, replacing them with a single spiral
D. It only applies to flash drives, not mechanical disks

---

**11.** (Hard) Why does Logical Block Addressing (LBA) simplify host-to-disk communication compared to the older Cylinder-Head-Sector (CHS) addressing scheme?

A. LBA requires the host OS to know the exact physical geometry (cylinders, heads, sectors) of every disk
B. LBA allows the host to reference a linear block number, while the disk controller internally translates this to the actual CHS address — the host only needs to know the total number of blocks, not the physical geometry
C. LBA and CHS are functionally identical with no practical difference
D. LBA is only used in flash drives, never in mechanical disks

---

**12.** (Medium) What are the three components that make up total disk service time (T_S)?

A. Cache hit time, cache miss time, and flush time
B. Seek time, rotational latency, and internal data transfer time
C. Queue time, controller time, and network latency
D. Read time, write time, and erase time

---

**13.** (Hard) According to the fundamental relationship between disk I/O controller utilization and response time, what happens to average response time as utilization approaches 100%, and what is the generally recommended utilization threshold for performance-sensitive applications?

A. Response time decreases linearly; recommended threshold is 100%
B. Response time approaches infinity as utilization nears 100% (since Response Time = Service Time / (1 − Utilization)); recommended threshold is to keep utilization below 70%
C. Response time remains constant regardless of utilization; no threshold is necessary
D. Response time only matters for write operations, not reads

---

**14.** (Medium) In Direct-Attached Storage (DAS), what distinguishes "internal DAS" from "external DAS"?

A. Internal DAS uses only flash drives; external DAS uses only mechanical disks
B. Internal DAS connects the storage device inside the host via a serial/parallel bus (with distance and device-count limitations); external DAS connects the host directly to an external storage device, typically via SCSI or FC, overcoming those limitations
C. Internal DAS requires a storage network; external DAS does not
D. There is no meaningful difference between internal and external DAS

---

**15.** (Hard) Why does DAS "not scale well" according to its limitations, even though it offers low initial investment and simple deployment?

A. DAS arrays have unlimited ports, making scaling trivial but expensive
B. A storage array has a limited number of ports, restricting the number of hosts that can directly connect; this also limits optimal resource sharing, leading to islands of over-utilized and under-utilized storage
C. DAS cannot be used with any file system
D. DAS requires a dedicated storage network switch for every host

---

**16.** (Medium) What is the formula for computing the total number of disks required (D_R) for an application, given the number of disks required for capacity (D_C) and the number of disks required for IOPS (D_I)?

A. D_R = D_C + D_I
B. D_R = D_C × D_I
C. D_R = Max(D_C, D_I)
D. D_R = Min(D_C, D_I)

---

**17.** (Hard) An application requires 1.46 TB of capacity and generates 9,000 IOPS at peak. A 146 GB, 15,000-rpm drive can perform a maximum of 180 IOPS, but the application is response-time sensitive (requiring utilization to stay at or below 70%). Using 180 × 0.7 = 126 IOPS per disk at 70% utilization, how many disks are required to meet the IOPS requirement, and what is the final number of disks required overall?

A. 50 disks for IOPS; final requirement is 50 disks
B. 72 disks for IOPS (9,000/126 ≈ 72); final requirement is Max(10, 72) = 72 disks
C. 10 disks for IOPS; final requirement is 10 disks
D. 100 disks for IOPS; final requirement is 100 disks

---

**18.** (Medium) What is the primary advantage of disk native command queuing (e.g., seek time optimization), and what does it actually change about command execution?

A. It guarantees commands execute in the exact order they are received, with no exceptions
B. It reorders the execution sequence of received I/O commands based on data organization on disk (e.g., minimizing head movement), rather than strictly the order in which commands arrived, to reduce unnecessary drive-head movement and improve performance
C. It only works on flash drives, not mechanical disks
D. It eliminates the need for an I/O queue entirely

---

**19.** (Medium) Compared to conventional mechanical disk drives, what performance and efficiency advantages do enterprise flash drives (EFDs) offer?

A. EFDs are slower but cheaper per GB, with no power savings
B. EFDs offer no seek/rotational latency (since they have no moving parts), up to 30 times the throughput, response times under 1 ms (versus 6-10 ms), and significantly lower power consumption per I/O
C. EFDs are only useful for sequential, large-block workloads
D. EFDs require more drives than mechanical disks to meet the same IOPS requirement

---

**20.** (Hard) In flash drive architecture, what is the distinction between a "page" and a "block," and what operational rule governs read versus write/erase operations at each level?

A. A page and a block are identical terms for the same unit; reads and writes both occur at the page level
B. A page is the smallest readable/writable unit, and pages are grouped into blocks (e.g., 32, 64, or 128 pages per block); a read operation can occur at the page level, but a write or erase operation can only occur at the block level
C. A block is smaller than a page, and only blocks can be read
D. Pages and blocks both refer to 512-byte mechanical disk sectors

---

## Answer Key & Explanations — Section A

| Q | Answer | Explanation |
|---|---|---|
| 1 | **B** | The LVM sits between the file system and physical disk, managing both logical and physical storage; it can partition large disks into smaller virtual volumes or aggregate smaller disks into one larger virtual volume. |
| 2 | **B** | When a volume group is created, each physical volume within it is partitioned into equal-sized data blocks called physical extents — the basic allocation unit for building logical volumes. |
| 3 | **A** | The LVM provides a logical abstraction over physical storage; this decoupling allows a logical volume to be composed of noncontiguous physical extents, potentially drawn from multiple physical volumes, while still appearing as a single contiguous device to the OS. |
| 4 | **B** | Nonjournaling file systems use separate writes for data and metadata; a crash during this process can corrupt or lose data, and recovery requires a lengthy full-filesystem consistency check (e.g., via fsck/CHKDSK). |
| 5 | **B** | Journaling writes pending changes to a log first; on crash, only the log's active/recent entries need replaying (fast recovery), but the extra journal writes during normal operation introduce a performance overhead. |
| 6 | **B** | Compute virtualization masks/abstracts physical hardware from the OS, enabling multiple OS instances to run concurrently on one or clustered machines; this is implemented by the hypervisor, a virtualization layer between hardware and VMs. |
| 7 | **B** | Swap space (page file) is disk-drive space that the OS treats as an extension of physical memory; because disk access is fundamentally slower than RAM access, accessing swapped-out pages is slower than accessing pages still resident in physical memory. |
| 8 | **C** | SATA (Serial ATA) uses single-bit serial transmission and has largely replaced Parallel ATA (PATA); SATA revision 3.0 supports up to 6 Gb/s data transfer rate. |
| 9 | **B** | Manufacturers use a base-10 definition of capacity (1 KB = 1,000 bytes) for advertised capacity, while actual usable capacity calculations (often base-2, 1 KB = 1,024 bytes) yield a smaller number — hence 500 GB advertised becomes 465.7 GB of actual usable capacity. |
| 10 | **B** | ZBR groups tracks into zones based on distance from the disk center, assigning more sectors per track to outer (physically longer) zones and fewer to inner zones — making more efficient use of the larger surface area available on outer tracks, unlike the old approach where all tracks had equal sectors regardless of length. |
| 11 | **B** | LBA lets the host reference data using a simple linear block number; the disk controller handles the internal translation to the physical CHS address, so the host only needs to know the disk's total block count, not its detailed physical geometry. |
| 12 | **B** | Disk service time (T_S) = seek time + rotational latency + internal data transfer time — the three electromechanical/data-movement components that determine how long a disk takes to service one I/O request. |
| 13 | **B** | Using Response Time = Service Time / (1 − Utilization), as utilization approaches 100%, the denominator approaches zero, driving response time toward infinity; because of this nonlinear blow-up (acute beyond ~70%), performance-sensitive applications should keep disk utilization below 70%. |
| 14 | **B** | Internal DAS connects storage inside the host chassis via a serial/parallel bus, limited by distance and device count; external DAS connects the host directly to an external array (typically via SCSI or FC), removing those internal limitations while still being block-level, host-direct access. |
| 15 | **B** | A storage array's limited port count restricts how many hosts can directly attach; this also limits the ability to share/reallocate front-end ports flexibly, leading to "islands" — some storage pools overutilized, others underutilized, with no easy reallocation. |
| 16 | **C** | D_R = Max(D_C, D_I) — the total disks required must satisfy whichever requirement (capacity or IOPS) demands more disks, since both constraints must be met simultaneously. |
| 17 | **B** | Capacity needs 1.46 TB / 146 GB = 10 disks. At 70% utilization, each disk delivers 180 × 0.7 = 126 IOPS, so IOPS needs 9,000 / 126 ≈ 72 disks. Final requirement = Max(10, 72) = 72 disks — illustrating that performance (IOPS), not capacity, is often the binding constraint. |
| 18 | **B** | Command queuing (e.g., seek time optimization) reorders queued I/O commands based on their physical location on disk to minimize head movement, rather than executing them strictly in arrival order — this reduces unnecessary radial movement and improves overall throughput. |
| 19 | **B** | EFDs have no moving parts, so they eliminate seek/rotational latency, delivering up to 30× the throughput of mechanical disks, sub-millisecond response times (versus 6-10 ms), and substantially lower power consumption per I/O and per TB. |
| 20 | **B** | A page is the smallest readable/writable unit on a flash drive; pages are grouped into blocks (32/64/128 pages each). Reads can happen at the page level, but writes and erases can only happen at the block level — a key architectural distinction from mechanical disk sectors. |

---

# SECTION B: Structural Questions (30 Marks)

*Answer all questions. Marks are indicated in brackets.*

---

### Question 1 (10 Marks)

**(a)** Describe the basic components of the Logical Volume Manager (LVM): physical volume, volume group, and logical volume, explaining the relationship between them. **[6 marks]**

**(b)** Explain two specific benefits that the LVM provides to storage administrators, beyond simply presenting storage to the host. **[4 marks]**

#### Model Answer

**(a) LVM Components [6 marks — 2 marks each]:**

1. **Physical Volume (PV)**: Each physical disk connected to the host system is treated by the LVM as a physical volume. A unique Physical Volume Identifier (PVID) is assigned to each PV when it is initialized for LVM use.

2. **Volume Group (VG)**: Created by grouping together one or more physical volumes. Physical volumes can be dynamically added to or removed from a volume group, but a single physical volume cannot be shared between different volume groups — once assigned, the entire PV becomes part of that VG. Each PV in a VG is partitioned into equal-sized physical extents.

3. **Logical Volume (LV)**: Created within a given volume group; conceptually analogous to a disk partition (while the volume group itself is analogous to a disk). A VG can contain multiple LVs. An LV's size is based on a multiple of physical extents, may be made up of noncontiguous extents, and may span multiple physical volumes — yet it appears to the OS as a single physical device. A file system is created on top of the logical volume.

**(b) Two Benefits of LVM [4 marks — 2 marks each]:**

1. **Optimized storage access and simplified management**: The LVM hides the details of the physical disk and the location of data on disk from the file system/application layer, abstracting away physical complexity.

2. **Dynamic storage reallocation**: The LVM enables administrators to change storage allocation (e.g., extend a logical volume) even while the application using it continues running — avoiding the downtime that direct physical-disk allocation would otherwise require.

---

### Question 2 (10 Marks)

**(a)** Explain the three components of disk service time and describe how each impacts the I/O response time experienced by an application. **[6 marks]**

**(b)** A disk has an average seek time of 5 ms, rotates at 15,000 rpm (250 rps), and has an internal data transfer rate of 40 MB/s. Calculate the disk service time (T_S) for an I/O with a block size of 16 KB, and determine the maximum IOPS this disk could perform at that block size. **[4 marks]**

#### Model Answer

**(a) Three Components of Disk Service Time [6 marks — 2 marks each]:**

1. **Seek time**: The time taken to position the R/W head over the correct track via radial movement. Lower seek time means faster I/O. It has greater impact on random-track access than on adjacent-track access. Disk vendors specify full-stroke, average, and track-to-track seek times.

2. **Rotational latency**: The time taken for the platter to rotate so the requested sector arrives under the R/W head. This depends on spindle speed; average rotational latency is half the time for one full rotation. Like seek time, it impacts random sector access more than adjacent sector access.

3. **Internal (data) transfer time**: The time for data to move from the platter surface to the disk's internal buffer/cache, which depends on the block size of the I/O and the drive's internal transfer rate.

Together, T_S = Seek time + Rotational latency + Internal transfer time, and a higher T_S directly translates into a higher I/O response time (especially as utilization rises, per the response-time formula).

**(b) Calculation [4 marks]:**

```
T (seek) = 5 ms
L (rotational latency) = 0.5 / 250 rps = 0.002 s = 2 ms
X (internal transfer time) = 16 KB / 40 MB/s = 16/40,000 s ≈ 0.4 ms

T_S = 5 + 2 + 0.4 = 7.4 ms

IOPS = 1 / T_S = 1 / (7.4 × 10⁻³) ≈ 135 IOPS
```

**Disk service time ≈ 7.4 ms; Maximum IOPS ≈ 135** *(matching the textbook's Table 2-1 value for a 16 KB block size)*.

---

### Question 3 (10 Marks)

**(a)** Explain the difference between block-level access and file-level access when a host retrieves data over a network. **[4 marks]**

**(b)** An application requires 500 GB of capacity and generates 6,000 IOPS at peak workload. The available disks provide 100 GB of usable capacity each and the manufacturer specifies a maximum of 150 IOPS per disk. The application is response-time sensitive, requiring disk utilization to remain at or below 70%. Calculate the minimum number of disks required to meet both the capacity and performance requirements. **[6 marks]**

#### Model Answer

**(a) Block-Level vs File-Level Access [4 marks]:**

In **block-level access**, the file system is created on the host itself, and raw disks or logical volumes are assigned to the host; data is accessed over the network at the block level — the host's file system directly manages block addressing.

In **file-level access**, the file system is created on a separate file server or at the storage side; the host sends file-level requests (e.g., "open this file") over the network rather than raw block requests. Because of this additional layer of abstraction and protocol overhead, file-level access generally incurs higher overhead compared to block-level access.

**(b) Disk Count Calculation [6 marks]:**

**Step 1 — Capacity requirement (D_C):**
```
D_C = 500 GB / 100 GB per disk = 5 disks
```
**[2 marks]**

**Step 2 — IOPS requirement at 70% utilization (D_I):**
```
IOPS per disk at 70% utilization = 150 × 0.7 = 105 IOPS
D_I = 6,000 / 105 ≈ 57.1 → round up to 58 disks
```
**[3 marks]**

**Step 3 — Final disk requirement:**
```
D_R = Max(D_C, D_I) = Max(5, 58) = 58 disks
```
**[1 mark]**

**Minimum number of disks required: 58** — illustrating that the IOPS (performance) requirement, not the capacity requirement, is the binding constraint in this scenario.

---

# SECTION C: Essay Questions (50 Marks)

*Answer all questions. Marks are indicated in brackets.*

---

### Essay Question 1 (25 Marks)

**Discuss the host (compute) component of a data center environment. Your answer should address: the core software components of a host (operating system, device drivers, volume manager, file system), the concept of compute virtualization and its relationship to memory and desktop virtualization, and the benefits this virtualization brings to data center operations.**

#### Model Answer

**Introduction [2 marks]**

The host, or compute system, is one of the five core elements of a data center environment (alongside application, DBMS, connectivity, and storage). A host consists of physical hardware (CPU, memory, I/O devices) and a software stack that enables it to perform computing operations and manage data access. Understanding this software stack — and how virtualization reshapes it — is foundational to understanding modern data center design.

**Operating System [3 marks]**

In a traditional (non-virtualized) computing environment, the operating system controls all aspects of computing: it sits between the application and the physical components, providing data access services, monitoring and responding to user actions, organizing and controlling hardware, allocating hardware resources, and providing basic security for resource access. It also performs basic storage management tasks while managing the file system, volume manager, and device drivers that operate beneath it.

**Device Drivers [2 marks]**

A device driver is specialized, hardware-dependent and OS-specific software that permits the operating system to recognize, access, and control a specific device (e.g., printer, mouse, disk drive) — acting as the translation layer between generic OS calls and device-specific hardware behavior.

**Volume Manager [4 marks]**

The Logical Volume Manager (LVM) addresses the inflexibility of early disk allocation, where an entire disk drive was allocated to a single file system with no easy way to extend it or use unused capacity. The LVM sits between the file system and the physical disk, managing both logical and physical storage. It can **partition** a larger disk into smaller virtual volumes, or **concatenate** several smaller disks into one larger virtual volume. Its core components — physical volumes (PVs), volume groups (VGs), and logical volumes (LVs) — together allow administrators to dynamically reallocate storage even while applications continue running, while hiding the physical disk's details entirely from the file system layer above.

**File System [4 marks]**

A file system is a hierarchical structure of files, consisting of logical structures and software routines controlling file access, creation, modification, and deletion. It organizes data via directories and maintains metadata (e.g., in UNIX: the superblock, inodes, and free/used block lists) that must remain consistent for the file system to be healthy. File systems are categorized as **nonjournaling** (risk of data/metadata loss/corruption on crash, requiring lengthy consistency checks via tools like fsck or CHKDSK) or **journaling** (writes pending changes to a separate log first, enabling fast crash recovery by replaying only the log's active entries, at the cost of extra write overhead during normal operation). Nearly all modern file system implementations use journaling because the integrity and recovery-speed benefits outweigh this overhead.

**Compute, Memory, and Desktop Virtualization [8 marks]**

**Compute virtualization** is a technique for masking/abstracting physical hardware from the operating system, enabling multiple operating systems to run concurrently on a single or clustered physical machine. This is achieved through a virtualization layer called the **hypervisor**, positioned between the hardware and the virtual machines (VMs) it hosts. Each VM appears to its guest OS as a complete physical host — with its own CPU, memory, network controller, and disks — even though all VMs actually share the same underlying physical hardware in an isolated manner. From the hypervisor's perspective, a VM is simply a discrete set of files (configuration file, data files, etc.).

**Memory virtualization** complements this at the OS level: it virtualizes physical RAM, creating a virtual address space larger than the actual physical memory by combining physical RAM with a portion of disk storage (swap space, managed by the Virtual Memory Manager, VMM). Through **paging**, inactive memory pages are moved to the swap file and brought back when needed, allowing the aggregate memory demand of multiple applications/processes to exceed physical RAM without those applications interfering with one another.

**Desktop virtualization** extends the same philosophy to the end-user environment: it breaks the traditional dependency between hardware and the OS/applications/user profile/settings, hosting desktops as VMs centrally in the data center while users access them remotely from thin client devices. This centralizes both application execution and data storage, mitigating data leakage/theft risk and simplifying patching, backup, and compliance.

**Benefits of Virtualization to Data Center Operations [2 marks]**

Collectively, these virtualization technologies eliminate the historical problem of resource-conflict-driven server sprawl (where organizations had to dedicate one physical server per application to avoid conflicting requirements), enabling **server consolidation**: fewer physical servers, reduced acquisition and operational cost, reduced floor/rack space, faster provisioning, and the ability to move or restart individual VMs without disrupting others on the same physical host.

**Conclusion**

The host's software stack — OS, device drivers, volume manager, and file system — together with the virtualization layer that increasingly sits beneath (or alongside) the traditional OS, exemplifies the data center's broader trend: abstracting physical complexity to deliver greater flexibility, utilization, and manageability.

---

### Essay Question 2 (25 Marks)

**Critically discuss disk drive performance in intelligent storage environments. Your answer should address: the physical components and geometry of a disk drive, the three components of disk service time, the relationship between I/O controller utilization and response time, and how these performance characteristics are used to determine the number of disks required to meet an application's storage requirements.**

#### Model Answer

**Introduction [2 marks]**

The disk drive is an electromechanical device whose physical characteristics fundamentally govern the performance of any storage system built upon it. Understanding disk geometry, the components of service time, and the mathematical relationship between utilization and response time is essential not only for diagnosing performance problems but for proactively designing storage systems that meet an application's combined capacity and performance requirements.

**Physical Components and Geometry of a Disk Drive [6 marks]**

A hard disk drive (HDD) consists of several key components: the **platter** (one or more flat, rigid circular disks coated with magnetic material on both surfaces, on which data is recorded as polarized magnetic domains), the **spindle** (connects all platters to a motor that rotates them at a constant speed — commonly 5,400, 7,200, 10,000, or 15,000 rpm), the **read/write (R/W) head** (one per platter surface, which senses or changes magnetic polarization without physically touching the platter — maintaining a microscopic "head flying height" air gap during operation, and resting in a lubricated "landing zone" when the spindle stops; accidental contact outside this zone causes a "head crash" and likely data loss), the **actuator arm assembly** (positions all R/W heads simultaneously across the platters), and the **drive controller board** (a microprocessor-driven circuit board managing spindle motor power/speed, host communication, and R/W operation optimization).

Data is physically organized into **tracks** (concentric rings, numbered from the outer edge), which are divided into **sectors** (the smallest individually addressable unit, typically 512 bytes of user data plus location metadata), and a **cylinder** is the set of identical tracks across all platter surfaces at a given radial position. **Zoned Bit Recording (ZBR)** improves on the historically inefficient approach of giving every track the same sector count regardless of length: ZBR groups tracks into zones by distance from center, assigning more sectors to the physically longer outer-zone tracks — though data transfer rate correspondingly drops when accessing inner zones, meaning performance-critical data should be placed in outer zones. **Logical Block Addressing (LBA)** further simplifies host-disk interaction by letting the host reference a simple linear block number rather than the disk's actual cylinder-head-sector geometry, with the disk controller handling the CHS translation internally.

**Components of Disk Service Time [6 marks]**

Disk service time (T_S) — the time to complete one I/O request — is the sum of three components: **seek time** (the time to radially position the R/W head over the correct track; vendors specify full-stroke, average, and track-to-track variants, typically 3–15 ms for modern disks; impacts random access far more than sequential/adjacent-track access), **rotational latency** (the time for the platter to rotate the target sector under the head, averaging half a full rotation's time — e.g., ≈2 ms for a 15,000-rpm/250-rps drive), and **internal data transfer time** (the time to move data from the platter to the disk's internal buffer, dependent on the I/O's block size and the drive's internal transfer rate). For example, with a 5 ms seek time, a 15,000-rpm drive (2 ms rotational latency), and a 40 MB/s internal transfer rate, a 32 KB I/O yields T_S = 5 + 2 + 0.8 = 7.8 ms, translating to a maximum of 1/0.0078 ≈ 128 IOPS at that block size.

**Utilization and Response Time [5 marks]**

The relationship between I/O controller utilization (U) and average response time (T_R) is given by:

```
T_R = T_S / (1 − U)
```

This relationship is markedly **nonlinear**: at low-to-moderate utilization, response time stays low and increases gradually, but beyond approximately 70% utilization, response time begins increasing exponentially, approaching infinity as utilization nears 100% (since the denominator approaches zero). This occurs because a saturated controller forces serialization of I/O requests — each new request must wait for all queued requests ahead of it. Consequently, the well-established best practice for performance-sensitive applications is to keep disk utilization at or below 70%, even though this means each disk delivers fewer maximum IOPS than its theoretical 100%-utilization ceiling.

**Applying These Concepts: Determining Required Disk Count [4 marks]**

These performance characteristics directly inform storage system design. An application's disk requirement must satisfy **both** capacity and IOPS demands simultaneously: D_C (disks needed for capacity) = required capacity ÷ usable capacity per disk; D_I (disks needed for IOPS) = required IOPS ÷ IOPS deliverable per disk **at the chosen utilization threshold** (e.g., manufacturer-rated IOPS × 0.7, if response-time sensitivity demands 70% utilization). The final required disk count is D_R = Max(D_C, D_I). In the textbook's worked example (1.46 TB capacity, 9,000 IOPS, 146 GB/180 IOPS drives, 70% utilization cap), D_C = 10 disks but D_I = 72 disks — meaning the *performance* requirement, not capacity, dictates the actual number of disks needed; provisioning for capacity alone would leave the application severely under-resourced for its true I/O demand.

**Conclusion [2 marks]**

Disk drive performance is not a single number but an interplay of mechanical geometry (seek, rotation), workload characteristics (block size, IOPS demand), and an explicitly nonlinear utilization-response relationship. Properly sizing a storage system, therefore, requires moving beyond simple capacity arithmetic to jointly account for IOPS demand and the response-time consequences of disk utilization — a discipline that remains foundational even as flash drives and RAID/caching technologies (covered in later chapters) provide alternative ways to meet these same performance demands with fewer mechanical drives.

---

*End of Practice Examination Set — Data Center Environment & Introduction to RAID*
