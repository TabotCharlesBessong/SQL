# MIST Master's Examination — Practice Set 3 of 4
## Data Center Environment: Mixed Topics
### Intelligent Storage Systems · Fibre Channel SAN · IP SAN & FCoE · Network-Attached Storage

**Format:** 20 MCQs (Medium–Hard) · Structural Questions (30 Marks) · Essay Questions (50 Marks)

**Coverage in this set:** LUN/MetaLUN and virtual provisioning numerical scenarios (Ch.4) · FC fabric login process and fabric services (Ch.5) · iSCSI sessions and command sequencing (Ch.6) · File-level virtualization and NAS file systems (Ch.7)

---

# SECTION A: Multiple Choice Questions (20 Questions)

---

**1.** (Medium) [Ch.4] What happens to the remaining capacity of larger drives when disks of different capacities are mixed within the same RAID set?

A. It is automatically reallocated to a separate RAID set
B. It remains unused, since the capacity of the smallest drive is used from each disk
C. It is converted into cache
D. It causes the RAID set to fail validation

---

**2.** (Hard) [Ch.4] In a concatenated metaLUN expansion, which statement about RAID type mixing is correct?

A. Any RAID type can be concatenated with any other RAID type without restriction
B. RAID 0 LUNs can only be concatenated with other RAID 0 LUNs; otherwise, all LUNs must be either protected or unprotected consistently
C. Concatenation is not possible if RAID types differ at all
D. Only RAID 5 LUNs can be concatenated

---

**3.** (Medium) [Ch.5] During Fabric Login (FLOGI), which two parameters does the node send to the Fabric Login Server (at address FFFFFE)?

A. IP address and MAC address
B. WWNN and WWPN
C. LUN number and zone ID
D. CmdSN and StatSN

---

**4.** (Hard) [Ch.5] What is the correct order of FC switched fabric login types, and which login relates specifically to FC-4 upper layer protocols such as SCSI?

A. PRLI, then PLOGI, then FLOGI — FLOGI relates to SCSI
B. FLOGI, then PLOGI, then PRLI — PRLI relates to SCSI
C. PLOGI, then FLOGI, then PRLI — PLOGI relates to SCSI
D. FLOGI only — it handles all ULP negotiation

---

**5.** (Medium) [Ch.6] In an iSCSI session, what is used to ensure that every command is delivered to the SCSI layer in the same order in which it was transmitted, regardless of which TCP connection carries it?

A. Session ID (SSID)
B. Connection ID (CID)
C. Command Sequence Number (CmdSN)
D. R2T PDU

---

**6.** (Hard) [Ch.6] During an iSCSI write operation, how does the DataSN behave for the first unsolicited data PDU or the first data PDU sent in response to an R2T?

A. It starts at a random value
B. It starts at zero and increments by one for each subsequent data PDU
C. It matches the CmdSN exactly
D. It is not used for write operations, only read operations

---

**7.** (Medium) [Ch.7] What does file-level virtualization eliminate, in terms of the relationship between data and its physical storage location?

A. The need for any file-sharing protocol
B. The dependency between data accessed at the file level and the physical location where the files are stored
C. The need for a NAS head
D. The need for an IP network

---

**8.** (Hard) [Ch.7] What does a "global namespace" do in a file-level virtualization implementation?

A. It maps the logical path of a file to its physical path names, enabling non-disruptive file movement
B. It assigns IP addresses to NAS devices
C. It replaces the need for NFS or CIFS protocols
D. It functions identically to LUN masking

---

**9.** (Medium) [Ch.4] A 2 TB storage array creates three thin LUNs with the same declared sizes as a traditional provisioning example (500 GB, 550 GB, 800 GB), but only 350 GB of data is actually written. Approximately how much capacity remains available for other applications?

A. 150 GB
B. 350 GB
C. 1.65 TB
D. 1.5 TB

---

**10.** (Hard) [Ch.5] What is N_Port ID Virtualization (NPIV), and what must be true of the FC switch for it to function?

A. NPIV allows multiple N_Port IDs to share a single physical N_Port; the FC switch must be NPIV-enabled
B. NPIV eliminates the need for WWNs; no special switch requirement exists
C. NPIV is used only for zoning; any switch supports it by default
D. NPIV assigns a single N_Port ID to multiple physical ports; requires an NPIV-disabled switch

---

**11.** (Medium) [Ch.6] What two discovery methods can an iSCSI initiator use to find available targets on the network?

A. Zoning and LUN masking
B. SendTargets discovery and iSNS (Internet Storage Name Service)
C. FLOGI and PLOGI
D. PFC and ETS

---

**12.** (Hard) [Ch.6] What is the purpose of the StatSN in an iSCSI session, and at what level is it established?

A. It numbers status responses sequentially; established at the level of the TCP connection
B. It numbers SCSI commands; established at the level of the session
C. It identifies the initiator's IQN; established at the array level
D. It replaces the need for CmdSN

---

**13.** (Medium) [Ch.7] In file-level virtualization, what problem existed BEFORE its implementation, when files needed to move between file servers due to performance or capacity constraints?

A. Files could move freely with no host reconfiguration ever needed
B. Hosts and applications needed to be reconfigured to access files at their new location, and files could become inaccessible during the move
C. File movement was impossible under any circumstances
D. Only CIFS clients were affected; NFS clients were unaffected

---

**14.** (Hard) [Ch.4] Which statement correctly distinguishes traditional (thick) LUN use cases from thin LUN use cases?

A. Thick LUNs are best for unpredictable space needs; thin LUNs are best for predictable performance
B. Thick LUNs are best for predictable performance and precise data placement; thin LUNs are best for space efficiency where consumption is hard to forecast
C. Both LUN types are functionally identical with no use-case difference
D. Thin LUNs cannot coexist with thick LUNs in the same array

---

**15.** (Medium) [Ch.5] Which predefined FC address corresponds to the Name Server, and what is its primary responsibility?

A. FFFFFE; fabric login processing
B. FFFFFD; Fabric Controller services
C. FFFFFC; name registration and management of node ports
D. FFFFFA; Management Server functions

---

**16.** (Hard) [Ch.6] What happens during the "full-feature phase" of an iSCSI session, following successful login?

A. The session is terminated immediately
B. The initiator sends SCSI commands and data to LUNs on the target, encapsulated in iSCSI PDUs over the established TCP connection
C. Only discovery operations are permitted
D. Authentication parameters are renegotiated continuously

---

**17.** (Medium) [Ch.7] Why is a file system "mounted" before it can be used, and what structure results from the mount process?

A. Mounting deletes the file system; no structure results
B. Mounting creates a link between the file system on the NAS and the operating system on the client, organizing files/directories into a tree-like structure rooted at a mount point
C. Mounting is only relevant to CIFS, not NFS
D. Mounting converts files into objects automatically

---

**18.** (Hard) [Ch.4] If an Oracle database with sequential read-heavy I/O patterns is being configured on an intelligent storage array, which prefetch type and cache allocation strategy would generally be most appropriate, and why?

A. Maximum prefetch disabled, large write cache allocation — because writes dominate
B. Variable or fixed prefetch enabled with read-ahead, and a larger read cache allocation — because sequential reads benefit significantly from prefetching into cache
C. No prefetching at all — sequential reads gain nothing from prefetching
D. Write aside size set to zero — to force all I/O through cache regardless of size

---

**19.** (Medium) [Ch.5] What distinguishes a "tier" in a Fibre Channel switched fabric, and what is the consequence of increasing the number of tiers?

A. A tier is the number of disks per RAID set; more tiers means more capacity
B. A tier reflects the number of switches traversed between the two points farthest apart in the fabric infrastructure; more tiers increases the time for fabric management traffic (e.g., zone propagation) to reach all switches
C. A tier is irrelevant to fabric management traffic
D. A tier only applies to NAS clusters, not FC fabrics

---

**20.** (Hard) [Ch.7] In the pNFS/MPFS model, why does separating metadata processing from data processing improve client performance compared to traditional NFS?

A. Because metadata servers handle all I/O directly, eliminating the need for clients
B. Because the metadata server is relieved of data processing, and clients access storage devices directly via multiple parallel data paths using a protocol like iSCSI or FC — avoiding the single-server bottleneck of traditional file serving
C. Because metadata is no longer needed at all
D. Because it eliminates the requirement for a storage network protocol

---

## Answer Key & Explanations — Section A

| Q | Answer | Explanation |
|---|---|---|
| 1 | **B** | When drives of different capacities are mixed in a RAID set, only the capacity of the smallest drive is used from each disk; the remaining capacity of larger drives goes unused. |
| 2 | **B** | In concatenated expansion, all LUNs must be consistently either protected (parity/mirrored) or unprotected (RAID 0); RAID 0 LUNs can only concatenate with other RAID 0 LUNs, though otherwise RAID types can be mixed (e.g., RAID 1/0 with RAID 5). |
| 3 | **B** | During FLOGI, the node sends a FLOGI frame containing its WWNN and WWPN parameters to the Fabric Login Server at FFFFFE. |
| 4 | **B** | The order is FLOGI (N_Port to F_Port, fabric login) → PLOGI (N_Port to N_Port, session establishment) → PRLI (N_Port to N_Port, FC-4 ULP-specific, e.g., SCSI service parameters). |
| 5 | **C** | The Command Sequence Number (CmdSN) numbers all initiator-to-target command PDUs in a session, ensuring delivery order to the SCSI layer regardless of which TCP connection carried each command. |
| 6 | **B** | For write operations, the first unsolicited data PDU (or first PDU in response to an R2T) starts DataSN at zero and increments by one for each subsequent data PDU in that command sequence. |
| 7 | **B** | File-level virtualization eliminates the dependency between data accessed at the file level and the physical location where files are stored, enabling location-independent access. |
| 8 | **A** | A global namespace maps the logical path of a file to its actual physical path names, which is what enables files to be moved between NAS devices/file servers without disrupting client access. |
| 9 | **C** | Using the textbook's virtual provisioning example: with thin LUNs, the same 350 GB of actual data leaves 1.65 TB of capacity available for other applications (versus only 150 GB with traditional provisioning). |
| 10 | **A** | NPIV enables multiple N_Port IDs to share one physical N_Port (useful for VM storage provisioning); this requires the FC switch itself to be NPIV-enabled to function. |
| 11 | **B** | iSCSI initiators discover targets via SendTargets discovery (manual configuration of target's network portal) or iSNS (automatic registration/discovery via an iSNS server); SLP is a less common third option. |
| 12 | **A** | StatSN sequentially numbers status responses and is established at the level of the TCP connection (unlike CmdSN, which is session-level). |
| 13 | **B** | Before file-level virtualization, moving files between servers required host/application reconfiguration to point to the new location, and files could become inaccessible during the move — problems that file-level virtualization with a global namespace solves. |
| 14 | **B** | Thick (traditional) LUNs suit applications needing predictable performance and precise data placement control; thin LUNs suit applications with hard-to-forecast space needs, prioritizing space efficiency. |
| 15 | **C** | FFFFFC is the predefined address of the Name Server, responsible for name registration and management of node ports (synchronized across switches in the fabric). |
| 16 | **B** | In the full-feature phase (after successful login), the initiator sends SCSI commands/data to LUNs on the target, encapsulated as iSCSI PDUs over the established TCP connection, for normal SCSI transactions. |
| 17 | **B** | Mounting links the NAS file system to the client OS and organizes files/directories in a tree structure rooted at a mount point, with files at leaf nodes and directories at intermediate nodes. |
| 18 | **B** | Sequential read-heavy workloads benefit strongly from read-ahead/prefetching (fixed or variable) and a larger read cache allocation, since prefetched blocks become read hits, significantly improving response time. |
| 19 | **B** | A tier reflects how many switches are traversed between the two farthest points in the fabric's infrastructure (not how storage/server connect); more tiers increase the distance/time for fabric management traffic (e.g., new switch addition, zone set propagation) to reach every switch. |
| 20 | **B** | In pNFS/MPFS, the metadata server is relieved of data processing duties, and clients use multiple parallel data paths (via iSCSI or FC) to access storage devices directly, removing the bottleneck of a single server handling all data traffic. |

---

# SECTION B: Structural Questions (30 Marks)

---

### Question 1 (10 Marks)

**(a)** A RAID set consisting of 5 disks is sliced into two LUNs: LUN 0 (assigned to Host 1) and LUN 1 (assigned to Host 2). Explain what happens when each LUN is configured and assigned to a non-virtualized host versus a virtualized host (hypervisor) environment. **[6 marks]**

**(b)** Explain the difference between concatenated and striped metaLUN expansion in terms of performance impact and capacity requirements of component LUNs. **[4 marks]**

#### Model Answer

**(a) Non-virtualized vs Virtualized LUN assignment [6 marks]:**

In a **non-virtualized host** environment: when a LUN is configured and assigned, a bus scan is required to identify the LUN, which then appears as a raw disk to the operating system. To make this disk usable, it must be formatted with a file system, and the file system is then mounted. **[3 marks]**

In a **virtualized host** environment: the LUN is assigned to the hypervisor, which recognizes it as a raw disk. This disk is configured with the hypervisor's file system, and virtual disks (files on the hypervisor file system) are created on top of it. These virtual disks are then assigned to virtual machines and appear as raw disks to them; similar formatting steps follow within the VM. Notably, the LUN space may be shared and accessed simultaneously by multiple virtual machines. **[3 marks]**

**(b) Concatenated vs Striped metaLUN [4 marks]:**

**Concatenated expansion** simply appends additional capacity from component LUNs to the base LUN; component LUNs need not match the base LUN's capacity. This is quick to implement but provides **no performance benefit** since data is not redistributed.

**Striped expansion** restripes the base LUN's existing data across the base and component LUNs, requiring **all LUNs to be the same capacity and RAID level**. Because data is spread across more physical drives, this method provides a genuine **performance improvement**.

---

### Question 2 (10 Marks)

**(a)** Describe the three FC switched fabric login types (FLOGI, PLOGI, PRLI), specifying which ports are involved in each and what each accomplishes. **[6 marks]**

**(b)** Explain the role of the Fabric Controller (located at FFFFFD) in managing RSCNs within a fabric. **[4 marks]**

#### Model Answer

**(a) FLOGI, PLOGI, PRLI [6 marks — 2 marks each]:**

- **FLOGI (Fabric Login)**: Performed between an N_Port and an F_Port. The node sends a FLOGI frame with its WWNN and WWPN to the Fabric Login Server (FFFFFE); the switch returns an Accept (ACC) frame with the assigned FC address. The N_Port then registers itself with the local Name Server.
- **PLOGI (Port Login)**: Performed between two N_Ports to establish a session. The initiator N_Port sends a PLOGI request to the target N_Port, which accepts it and returns an ACC; the N_Ports then exchange session-relevant service parameters.
- **PRLI (Process Login)**: Also performed between two N_Ports; relates specifically to FC-4 Upper Layer Protocols (e.g., SCSI). If the ULP is SCSI, the N_Ports exchange SCSI-related service parameters.

**(b) Fabric Controller and RSCNs [4 marks]:**

The Fabric Controller, located at the predefined address FFFFFD, is responsible for managing and distributing Registered State Change Notifications (RSCNs) to node ports registered with it. Whenever a change occurs in the fabric, RSCNs are sent to attached node ports to notify them. The Fabric Controller also generates Switch RSCNs (SW-RSCNs) to every other switch (domain) in the fabric, keeping the name server synchronized and up to date across all switches.

---

### Question 3 (10 Marks)

**(a)** Describe the iSCSI session establishment process, from TCP connection initiation through the full-feature phase to logout. **[6 marks]**

**(b)** Explain what file-level virtualization is and how it provides non-disruptive file mobility. **[4 marks]**

#### Model Answer

**(a) iSCSI Session Lifecycle [6 marks]:**

1. **Login phase**: The initiator establishes a TCP connection with the target via the well-known port 3260 (or a specified target port). During login, the initiator and target authenticate each other and negotiate various session parameters. **[2 marks]**
2. **Full-feature phase**: Following successful login, the session enters this phase for normal SCSI transactions. The initiator sends SCSI commands and data to LUNs on the target, encapsulated in iSCSI PDUs traveling over the established TCP connection. **[2 marks]**
3. **Connection termination (logout) phase**: The initiator typically commences the logout procedure, though the target may also prompt termination (e.g., due to an internal error). After the logout request is sent and accepted, no further requests/responses can be sent on that connection. **[2 marks]**

**(b) File-level virtualization and non-disruptive mobility [4 marks]:**

File-level virtualization eliminates the dependency between data accessed at the file level and the physical location where files are stored. It creates a logical pool of storage, allowing users/applications to access files via a **logical path** rather than a physical path. A **global namespace** maps this logical path to the actual physical path names. Because of this abstraction, files can be moved between NAS devices/file servers while clients continue to access them — reading from the old location and writing to the new location — without realizing the physical location has changed, and without requiring host/application reconfiguration.

---

# SECTION C: Essay Questions (50 Marks)

---

### Essay Question 1 (25 Marks)

**Discuss how identity and addressing are managed across the storage lifecycle, from the storage array's internal LUN structures to the FC fabric's login and naming services. Your answer should address: how LUNs are created and identified within RAID sets, how MetaLUN and virtual provisioning alter this identity model, and how FC fabric services (name server, fabric controller, login types) manage device identity dynamically within the fabric.**

#### Model Answer

**Introduction [2 marks]**

Effective storage management depends on consistent, well-understood identity and addressing schemes at every layer — from how a slice of physical disk capacity becomes a host-visible LUN, to how that host's HBA port is dynamically and statically identified within an FC fabric. This essay traces that identity model from the storage array outward to the fabric.

**LUN Identity within RAID Sets [5 marks]**

A RAID set combines multiple physical disks under a chosen RAID level. Because RAID sets are large, they are partitioned ("sliced") into smaller logical units, each assigned a unique **Logical Unit Number (LUN)**. The LUN abstraction is critical: it hides the underlying RAID set's organization and disk composition entirely from the host, presenting what appears to be a single raw disk. Each logical unit is spread across all physical disks belonging to its RAID set, distributing both capacity and I/O load. Traditionally provisioned LUNs (fully allocated at creation) are termed "thick" LUNs, establishing a baseline identity model: one LUN ID, fully backed by dedicated physical capacity, with no ambiguity about where its data physically resides.

**MetaLUN and Virtual Provisioning: Altering the Identity Model [7 marks]**

**MetaLUN** complicates this simple one-to-one identity slightly: a metaLUN combines a base LUN with one or more component LUNs, but is still presented and addressed as a single logical entity to the host. In **concatenated expansion**, the component LUNs are simply appended — different capacities are allowed, but all LUNs must consistently be protected or unprotected (RAID 0 may only concatenate with RAID 0). In **striped expansion**, the base LUN's data is restriped across base and component LUNs of identical capacity and RAID level, improving performance. Despite this internal complexity, the host still addresses a single metaLUN identity — the underlying expansion mechanics remain transparent.

**Virtual provisioning** represents a more fundamental shift: a **thin LUN** is presented to the host with a declared logical capacity, but its physical backing is drawn on-demand from a **shared pool** rather than dedicated, pre-allocated disks. The LUN's logical identity (its declared size, its LUN ID) becomes decoupled from any fixed physical disk mapping — multiple thin LUNs can draw from the same shared pool, and that pool's total physical capacity can be smaller than the sum of all thin LUNs' declared capacities (oversubscription). This is a profound shift from the thick-LUN model: the *identity* (LUN number, declared capacity) remains stable and host-visible, but the *physical referent* behind that identity becomes dynamic and pool-managed.

**FC Fabric Identity: Dynamic Addressing and Static Naming [7 marks]**

Once a host's HBA port needs to reach these LUNs across an FC SAN, a second identity layer comes into play — one defined not by the storage array but by the fabric. Each N_Port has a **dynamically assigned 24-bit FC address** (Domain ID + Area ID + Port ID), reassigned at every fabric login, alongside a **statically assigned 64-bit WWN** (WWNN/WWPN) burned into hardware or configured in software — directly paralleling the LUN-identity-vs-physical-backing duality seen above: the WWN is the stable "identity," while the FC address is the dynamic "physical-network-position" equivalent.

This duality is actively managed through three login types. **FLOGI** (N_Port–F_Port) establishes the node's presence on the fabric: the node presents its WWNN/WWPN to the Fabric Login Server (FFFFFE), receiving back a freshly assigned FC address, and then registers this WWN-to-address mapping with the **Name Server** (FFFFFC) — the fabric's authoritative directory mapping static identity to current dynamic address. **PLOGI** (N_Port–N_Port) then establishes a session between two already-logged-in nodes, exchanging session parameters. Finally, **PRLI** (N_Port–N_Port) negotiates FC-4 upper-layer-protocol-specific parameters (e.g., SCSI). The **Fabric Controller** (FFFFFD) complements the Name Server by distributing RSCNs whenever this identity mapping changes anywhere in the fabric, ensuring all relevant nodes stay synchronized.

**Conclusion [4 marks]**

A consistent pattern emerges across every layer examined: storage identity management consistently separates a **stable, host/application-visible identifier** (LUN number, WWN) from a **dynamic, infrastructure-managed physical backing or network position** (physical disk allocation, FC address). Virtual provisioning decouples LUN identity from fixed physical allocation; FC fabric login decouples WWN identity from a fixed network address. This separation is precisely what enables modern storage infrastructure's defining capabilities — non-disruptive LUN expansion, oversubscription, device mobility, and fabric resilience — without ever requiring the host or application layer to be aware of, or disrupted by, the underlying physical reality.

---

### Essay Question 2 (25 Marks)

**Critically discuss the mechanisms that allow storage networking protocols to maintain reliable, ordered, and location-independent data access in the presence of network unreliability and infrastructure change. Your answer should address: iSCSI's command/data sequencing over potentially unordered IP delivery, file-level virtualization's handling of file mobility, and NAS performance-affecting factors with their corresponding mitigation techniques.**

#### Model Answer

**Introduction [2 marks]**

A defining engineering challenge in storage networking is reconciling the strict ordering and reliability that storage I/O demands with the inherently unordered, sometimes unreliable nature of the underlying network — particularly when that network is general-purpose IP rather than a purpose-built, lossless fabric. This essay examines how iSCSI, file-level virtualization, and NAS performance management each solve a facet of this challenge.

**iSCSI Sequencing Over Unordered IP Delivery [9 marks]**

IP networks do not guarantee in-order packet delivery — a message may be split into multiple packets that travel different routes and arrive out of sequence; IP only delivers packets, while TCP is responsible for reassembling them in the correct order. iSCSI must therefore impose its own ordering guarantees at a higher level, since SCSI commands and data absolutely require correct sequencing to maintain data integrity.

iSCSI accomplishes this through several sequence number mechanisms operating at different scopes. The **Command Sequence Number (CmdSN)** numbers every initiator-to-target command PDU within a session, beginning with the first login command and incrementing by one per subsequent command; critically, the iSCSI target layer delivers commands to the SCSI layer strictly in CmdSN order — this guarantee holds even when **multiple TCP connections** exist within a single session (each with its own unique **Connection ID, CID**), since CmdSN ordering operates at the session level, above any individual connection. The **Status Sequence Number (StatSN)** similarly numbers status responses but is established at the **TCP connection level**, not the session level. For data transfer, the **DataSN** ensures in-order delivery of data PDUs within a single command — starting at zero and incrementing per subsequent data PDU (for reads, or for the first unsolicited/R2T-triggered write PDU) — while the **R2TSN** sequences Request-to-Transfer PDUs, which a target sends to an initiator to signal readiness to receive write data.

This layered sequencing model — session-level CmdSN, connection-level StatSN, command-level DataSN/R2TSN — allows iSCSI to multiplex multiple TCP connections (for performance or redundancy) within one logical session while still presenting the SCSI layer with a single, strictly ordered command stream, exactly as if the unreliable, potentially out-of-order IP substrate beneath it did not exist.

**File-Level Virtualization: Location Independence Under Infrastructure Change [8 marks]**

A related but distinct reliability problem arises when the underlying storage infrastructure itself changes — specifically, when files must be relocated from one NAS device or file server to another due to capacity exhaustion or performance rebalancing needs. Without abstraction, hosts and applications hard-code the physical location of their file resources; moving files requires reconfiguring every client and risks making files inaccessible during the transition — directly undermining the "location-independent, always-available" promise storage networking aims to provide.

**File-level virtualization** solves this by introducing a logical abstraction layer: clients address files via a **logical path**, and a **global namespace** maintains the mapping from this logical path to the file's actual, current physical path. Because this mapping is centrally managed and can be updated independently of client configuration, files can be migrated between NAS devices while remaining continuously accessible — clients may even read from the old location and write to the new one during the transition window without being aware that any physical relocation occurred. This is conceptually analogous to how an FC fabric's Name Server maps a stable WWN identity to a dynamically reassignable FC address: in both cases, a layer of indirection absorbs infrastructure change so that the consuming layer above never needs to be aware of, or disrupted by, it.

**NAS Performance: Identifying and Mitigating Network-Induced Unreliability [4 marks]**

Even where data remains correctly ordered and locatable, the IP network's variable latency and loss characteristics directly threaten NAS performance. Key degradation sources include: excessive hop counts (cumulative per-hop IP processing delay); authentication bottlenecks under heavy directory-service load; retransmissions from link errors, buffer overflows, or speed/duplex mismatches; and overutilization at any point in the chain — routers, switches, the NAS device itself, or clients. Mitigations directly target these mechanisms: **VLANs** reduce broadcast overhead and improve security/isolation; **jumbo frames** (MTU up to 9,000 bytes) reduce the number of frames (and thus per-frame overhead) needed to move a given volume of data; correctly sized **TCP window** settings (ideally bandwidth × round-trip-time) avoid needless throughput throttling from premature send-stalling; and **link aggregation** combines multiple physical NICs into one logical, higher-throughput, failover-resilient interface.

**Conclusion [2 marks]**

Across all three mechanisms — iSCSI's layered sequence numbering, file-level virtualization's logical-to-physical namespace mapping, and NAS's network-tuning toolkit — the underlying engineering principle is the same: introduce a layer of structured indirection or compensation precisely at the point where an unreliable or changeable substrate would otherwise leak its unpredictability into the layer above. This principle, repeated at multiple scales throughout storage networking, is what allows applications to treat networked storage as if it were as simple, ordered, and stable as a local disk — even though, underneath, it manifestly is not.

---

*End of Practice Examination Set 3 of 4*
