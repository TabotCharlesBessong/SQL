# MIST Master's Examination — Practice Set 1 of 4
## Data Center Environment: Mixed Topics
### Intelligent Storage Systems · Fibre Channel SAN · IP SAN & FCoE · Network-Attached Storage

**Format:** 20 MCQs (Medium–Hard) · Structural Questions (30 Marks) · Essay Questions (50 Marks)

**Coverage in this set:** Cache internals & LUN provisioning (Ch.4) · FC ports, addressing, zoning (Ch.5) · iSCSI architecture (Ch.6) · NAS components & file-sharing protocols (Ch.7)

---

# SECTION A: Multiple Choice Questions (20 Questions)

---

**1.** (Medium) [Ch.4] In the structure of cache, which component contains the dirty bit flag indicating whether cached data has been committed to disk?

A. Data store
B. Tag RAM
C. Vault drive
D. Front-end buffer

---

**2.** (Hard) [Ch.4] A storage system prefetches an amount of data proportional to the size of the host's read request. Which prefetch strategy is this?

A. Fixed prefetch
B. Maximum prefetch
C. Variable prefetch
D. Sequential-only prefetch

---

**3.** (Medium) [Ch.5] Which Fibre Channel port type forms the connection between two FC switches via an Interswitch Link (ISL)?

A. N_Port
B. F_Port
C. E_Port
D. G_Port

---

**4.** (Hard) [Ch.5] What is the maximum theoretical number of node ports addressable in an FC switched fabric, based on the 24-bit FC address structure (Domain ID, Area ID, Port ID)?

A. 126
B. 256
C. 15,663,104
D. 2,112

---

**5.** (Medium) [Ch.6] In iSCSI, what is the role of the "initiator"?

A. It is the storage device that responds to SCSI commands
B. It is the host that originates the SCSI command request over IP
C. It is the gateway that converts FC frames to IP packets
D. It is the switch that routes Ethernet traffic

---

**6.** (Hard) [Ch.6] Which iSCSI host connectivity option offloads the entire iSCSI and TCP/IP processing from the host processor, providing the best performance?

A. Standard NIC with software initiator
B. TCP Offload Engine (TOE) NIC
C. iSCSI HBA
D. FCoE CNA

---

**7.** (Medium) [Ch.7] What are the two key components of a NAS device?

A. Front end and back end
B. NAS head and storage
C. CNA and FCF
D. Initiator and target

---

**8.** (Hard) [Ch.7] Which NFS version is based on a stateful protocol design, uses TCP, and introduced features such as the session model and parallel NFS (pNFS)?

A. NFSv2
B. NFSv3
C. NFSv4 (specifically NFSv4.1)
D. NFSv1

---

**9.** (Medium) [Ch.4] What is the term for a LUN created via virtual provisioning, distinguishing it from a traditionally provisioned LUN?

A. MetaLUN
B. Thick LUN
C. Thin LUN
D. Virtual RAID set

---

**10.** (Hard) [Ch.5] In FC zoning, which type uses World Wide Names to define zone membership, allowing devices to be moved to different switch ports without modifying the zone configuration?

A. Port zoning
B. WWN zoning
C. Mixed zoning
D. Domain zoning

---

**11.** (Medium) [Ch.6] What does FCIP do?

A. It encapsulates Ethernet frames into FC frames
B. It tunnels/encapsulates FC frames over an IP network to interconnect distributed FC SAN islands
C. It converts NFS requests into CIFS requests
D. It replaces TCP with a lossless protocol

---

**12.** (Hard) [Ch.6] In FCoE, which virtual port type resides in an Enhanced Ethernet node (Enode), such as a server equipped with a CNA?

A. VF_Port
B. VE_Port
C. VN_Port
D. VG_Port

---

**13.** (Medium) [Ch.7] Which NAS implementation consolidates NAS-based (file) and SAN-based (block) data access within a single unified storage platform, sharing the same storage controllers?

A. Gateway NAS
B. Scale-out NAS
C. Unified NAS
D. Native NAS

---

**14.** (Hard) [Ch.4] Which cache write implementation has a HIGHER risk of data loss but provides FASTER write response time, because acknowledgment is sent to the host before data is committed to disk?

A. Write-through cache
B. Write-back cache
C. Direct write cache
D. Mirrored write cache

---

**15.** (Medium) [Ch.5] What is the purpose of LUN masking, and at what level is it implemented?

A. It is implemented at the fabric level to define which ports can communicate
B. It is implemented at the array level to define which hosts can access specific LUNs
C. It is implemented at the host level to mask disk drivers
D. It is implemented at the switch level to control VLAN membership

---

**16.** (Hard) [Ch.6] Which FCoE enabling technology creates eight separate virtual links on a single physical Ethernet link, allowing any one of them to be paused independently without affecting the others?

A. Enhanced Transmission Selection (ETS)
B. Priority-based Flow Control (PFC)
C. Congestion Notification (CN)
D. Data Center Bridging Exchange Protocol (DCBX)

---

**17.** (Medium) [Ch.7] Which file-sharing protocol is described as a stateful protocol because the server maintains connection information for every connected client?

A. NFSv3
B. FTP
C. CIFS
D. NFSv2

---

**18.** (Hard) [Ch.4] Which type of metaLUN expansion requires all participating LUNs to be the same capacity and RAID level, and provides a genuine performance improvement by redistributing data across more drives?

A. Concatenated expansion
B. Striped expansion
C. Mirrored expansion
D. Sequential expansion

---

**19.** (Medium) [Ch.5] In FC-AL (Fibre Channel Arbitrated Loop), what is the maximum number of nodes that can be connected on the loop, given that one address is reserved for connecting to an FC switch port?

A. 127
B. 126
C. 256
D. 15 million

---

**20.** (Hard) [Ch.7] What is the role of a pNFS metadata server in the pNFS (parallel NFS) architecture?

A. It handles all data read/write traffic directly between client and storage
B. It processes only metadata (file name, location, ACLs, attributes), while clients access storage devices directly via parallel data paths
C. It replaces the need for a storage network protocol such as iSCSI or FC
D. It functions as the FCoE Forwarder for the NAS cluster

---

## Answer Key & Explanations — Section A

| Q | Answer | Explanation |
|---|---|---|
| 1 | **B** | Tag RAM tracks data location and contains the dirty bit flag plus time-based access information; the data store holds the actual cached data. |
| 2 | **C** | Variable prefetch reads an amount of data that is a multiple of the host's request size, adapting to the size of the request (unlike fixed prefetch, which always reads a constant amount). |
| 3 | **C** | The E_Port (expansion port) connects two FC switches together via an ISL, enabling fabric expansion; N_Port is an end-point device port, F_Port connects an N_Port to a switch, and G_Port is generic (can act as E or F). |
| 4 | **C** | 239 domains × 256 areas × 256 ports = 15,663,104 — the theoretical maximum addressable node ports in a switched fabric. |
| 5 | **B** | The initiator is the host that originates SCSI command requests encapsulated in IP; the target is the storage device or gateway that responds. |
| 6 | **C** | An iSCSI HBA offloads the entire iSCSI and TCP/IP processing stack from the host CPU, unlike a standard NIC (host CPU does everything) or TOE NIC (offloads only TCP, not iSCSI). |
| 7 | **B** | A NAS device consists of a NAS head (CPU, memory, NICs, optimized OS, file-sharing protocols) and storage (which may be internal or external/shared). |
| 8 | **C** | NFSv4 (and its enhancement NFSv4.1) uses TCP and is stateful, unlike NFSv2/v3 which are stateless; NFSv4.1 specifically introduced the session model and pNFS. |
| 9 | **C** | A "thin LUN" is created via virtual provisioning, with physical storage allocated on-demand from a shared pool, unlike a thick (traditional) LUN with capacity fully pre-allocated. |
| 10 | **B** | WWN zoning uses the static World Wide Name of devices, so connectivity persists even if a device is moved to a different physical switch port — unlike port zoning, which is tied to the physical port. |
| 11 | **B** | FCIP (Fibre Channel over IP) is a tunneling protocol that encapsulates FC frames onto IP packets to interconnect geographically dispersed FC SAN islands over existing IP infrastructure. |
| 12 | **C** | VN_Port (Virtual N_Port) resides in an Enode (e.g., a server with a CNA); VF_Port and VE_Port reside in the FCoE switch (as fabric port and extension/ISL port respectively). |
| 13 | **C** | Unified NAS consolidates file (NAS) and block (SAN) access on one platform with shared storage controllers, reducing infrastructure and management costs, unlike gateway NAS (separate storage management). |
| 14 | **B** | Write-back cache acknowledges the host immediately on cache write (fast response), but uncommitted data is at risk if a cache failure occurs before de-staging to disk. |
| 15 | **B** | LUN masking is implemented at the storage array level and controls which hosts are permitted to discover/access which specific LUNs — distinct from zoning, which operates at the fabric level. |
| 16 | **B** | Priority-based Flow Control (PFC) creates 8 virtual lanes on one physical Ethernet link, each independently pausable, enabling lossless behavior for FCoE traffic without pausing the entire link (unlike standard Ethernet PAUSE). |
| 17 | **C** | CIFS is stateful — the server tracks connection state for every client, enabling automatic reconnection/file reopening after interruption; NFS (v3 and earlier) is stateless. |
| 18 | **B** | Striped expansion restripes data across base + component LUNs of identical capacity/RAID level, improving performance through more drives; concatenated expansion only appends capacity with no performance gain. |
| 19 | **B** | FC-AL uses 8 of the 24 address bits, allowing 127 valid port addresses, but one is reserved for an optional connection to an FC switch port, leaving 126 nodes that can be connected to the loop. |
| 20 | **B** | The pNFS metadata server processes only metadata (name, location, ACLs) and is kept out of the data path; pNFS clients use the metadata to access storage directly via parallel paths using a protocol like iSCSI or FC, improving performance. |

---

# SECTION B: Structural Questions (30 Marks)

---

### Question 1 (10 Marks)

**(a)** List and briefly explain the four key components of an intelligent storage system. **[6 marks]**

**(b)** Differentiate between a read hit and a read miss, and explain how prefetching improves read performance for sequential workloads. **[4 marks]**

#### Model Answer

**(a) Four key components [6 marks — 1.5 marks each]:**
1. **Front End** — interfaces between host and storage system; consists of front-end ports and controllers that execute the transport protocol (FC, iSCSI, FICON, FCoE) and route data to/from cache.
2. **Cache** — semiconductor memory that temporarily holds data, isolating the host from the mechanical delays of disk drives.
3. **Back End** — interfaces between cache and physical disks; consists of back-end ports and controllers that manage disk reads/writes, error detection/correction, and RAID functionality.
4. **Physical Disks** — provide persistent storage; the slowest component due to seek time and rotational latency.

**(b) Read hit/miss and prefetching [4 marks]:**

A **read hit** occurs when requested data is found in cache and sent directly to the host without disk access (fast, ~1ms response). A **read miss** occurs when data is not in cache, requiring the back end to retrieve it from disk before forwarding it to the host (slower response, increased I/O latency).

**Prefetching (read-ahead)** improves performance for sequential workloads by speculatively reading additional, not-yet-requested contiguous blocks from disk into cache in advance. When the host subsequently requests these blocks, the operations become read hits rather than read misses, significantly improving response time.

---

### Question 2 (10 Marks)

**(a)** Explain the function of the FC-2, FC-1, and FC-0 layers in the Fibre Channel Protocol stack. **[6 marks]**

**(b)** Describe the structure of a 24-bit FC address and explain why FC-AL is limited to a maximum of 126 connectable nodes. **[4 marks]**

#### Model Answer

**(a) FCP Layers [6 marks — 2 marks each]:**

- **FC-2 Layer**: Provides FC addressing, defines the structure and organization of data (frames, sequences, exchanges), and handles fabric services, classes of service, flow control, and routing.
- **FC-1 Layer**: Defines how data is encoded before transmission and decoded upon receipt (8-bit to 10-bit encoding, or 64b/66b for links ≥10 Gbps); also defines transmission words (frame delimiters, primitive signals) and performs link initialization and error recovery.
- **FC-0 Layer**: The lowest layer; defines the physical interface, media, and transmission of bits — cables, connectors, and optical/electrical parameters for various data rates.

**(b) FC Address structure and FC-AL limitation [4 marks]:**

The 24-bit FC address is divided into three fields: **Domain ID** (8 bits, identifies the switch), **Area ID** (identifies a group of switch ports, e.g., a port card), and **Port ID** (identifies the specific port within the group).

FC-AL uses only 8 bits of this 24-bit address (the remaining 16 bits are masked), enabling 127 valid port addresses. However, one address is reserved for optionally connecting the loop to an FC switch port, leaving a maximum of **126 nodes** that can actually be connected to the loop.

---

### Question 3 (10 Marks)

**(a)** Explain the iSCSI protocol stack, describing how SCSI commands are encapsulated for transmission over an IP network. **[6 marks]**

**(b)** Describe the NAS I/O operation process — how a NAS device handles a client's file I/O request, from request to response. **[4 marks]**

#### Model Answer

**(a) iSCSI Protocol Stack [6 marks]:**

The iSCSI protocol stack maps to the OSI model as follows:
- **Application Layer (Layer 7)**: SCSI — commands and data exchanged between initiator and target.
- **Session Layer (Layer 5)**: iSCSI — handles login, authentication, target discovery, and session management.
- **Transport Layer (Layer 4)**: TCP — provides reliable transmission, message flow control, windowing, error recovery, and retransmission.
- **Network Layer (Layer 3)**: IP — provides global addressing and connectivity (packets).
- **Data Link Layer (Layer 2)**: Ethernet — enables node-to-node communication through the physical network (frames).

SCSI commands and data are encapsulated into iSCSI PDUs, which are encapsulated into TCP segments, which are further encapsulated into IP packets and finally Ethernet frames for transmission.

**(b) NAS I/O Operation [4 marks — 1 mark per step]:**

1. The client packages a file I/O request into TCP/IP and forwards it to the NAS device over the network.
2. The NAS device converts the file-level I/O request into an appropriate block-level I/O request and performs the operation on the physical storage.
3. When the NAS device receives data from storage, it processes and repackages the data into the appropriate file protocol (NFS/CIFS) response.
4. The NAS device packages this response into TCP/IP and forwards it back to the client over the network.

---

# SECTION C: Essay Questions (50 Marks)

---

### Essay Question 1 (25 Marks)

**Discuss how data is logically structured and addressed for transmission in both Fibre Channel SAN and iSCSI environments. Your answer should cover: the FC frame structure and addressing scheme, World Wide Names, the iSCSI PDU and naming scheme, and a comparison of how each technology achieves device identification and communication.**

#### Model Answer

**Introduction [2 marks]**

Both Fibre Channel SAN and iSCSI require robust mechanisms to identify devices, structure data for transmission, and ensure reliable delivery across their respective networks. Although FC and iSCSI rely on fundamentally different transport mechanisms (a dedicated channel-network hybrid versus standard IP), both technologies define explicit conventions for addressing, naming, and data unit structure.

**FC Frame Structure [5 marks]**

An FC frame consists of five parts: **Start of Frame (SOF)**, **frame header** (24 bytes), **data field** (0–2,112 bytes payload), **CRC** (cyclic redundancy check for error detection), and **End of Frame (EOF)**. The frame header contains addressing information including the Source ID (S_ID) and Destination ID (D_ID) — both FC addresses — along with Sequence ID (SEQ_ID), Sequence Count (SEQ_CNT), Originating Exchange ID (OX_ID), and Responder Exchange ID (RX_ID). Control fields such as R_CTL (denotes link control vs. data frame), CS_CTL (link speed for certain classes of service), TYPE (identifies the upper layer protocol), DF_CTL, and F_CTL round out the header. Data transport in FC is hierarchically organized: a **frame** is the basic Layer 2 transfer unit, a **sequence** is a contiguous set of frames forming one information unit, and an **exchange** is composed of one or more sequences representing a complete operation between two ports — analogous to a word, sentence, and conversation, respectively.

**FC Addressing Scheme [5 marks]**

An FC address is dynamically assigned (not static) when a node port logs onto the fabric. It is a 24-bit value structured into three fields: **Domain ID** (8 bits — unique per switch, with 239 of 256 possible values actually usable since several are reserved for fabric services such as FFFFFC for the name server and FFFFFE for fabric login), **Area ID** (identifies a logical group of ports, such as a port card), and **Port ID** (identifies the specific port). This yields a theoretical maximum of 239 × 256 × 256 = 15,663,104 addressable node ports — illustrating FC's enormous scalability compared to the 126-node limit of FC-AL.

Because the FC address is dynamic (it changes if a device is unplugged and replugged, or moved), FC also defines a separate, **static** identifier: the **World Wide Name (WWN)** — a 64-bit unique identifier analogous to a MAC address in IP networking. Two types exist: World Wide Node Name (WWNN) and World Wide Port Name (WWPN). WWNs are burned into hardware or assigned via software and are used by zoning configurations and the name server to maintain a persistent association between a physical device and its (changeable) FC address.

**iSCSI PDU and Naming Scheme [6 marks]**

iSCSI structures data into **Protocol Data Units (PDUs)** — the basic information unit for iSCSI communication, used for establishing sessions/connections, discovery, sending SCSI commands/data, and receiving status. A PDU contains one or more header segments (basic header + optional additional header) followed by zero or more data segments, with optional CRC digests (header digest and data digest) added for integrity beyond the standard TCP checksum and Ethernet CRC. The PDU is then encapsulated within a TCP segment, which is encapsulated within an IP packet. Notably, there is no strict 1:1 relationship between an iSCSI PDU and an IP packet — a PDU may span multiple packets or coexist with another PDU in the same packet, depending on size; adjusting the IP MTU can help achieve a cleaner 1:1 alignment and reduce fragmentation overhead.

For naming, every iSCSI device requires a unique worldwide identifier — an **iSCSI name**. Two formats exist: the **iSCSI Qualified Name (IQN)**, which requires the organization to own a registered domain name (e.g., `iqn.2008-02.com.example:optional_string`, with the date included to avoid conflicts from domain transfers), and the **Extended Unique Identifier (EUI)**, based on the IEEE EUI-64 standard (e.g., `eui.0300732A32598D26`). A third format, **Network Address Authority (NAA)**, enables devices with both iSCSI and SAS ports to share the same naming scheme.

**Comparative Discussion [5 marks]**

| Aspect | Fibre Channel | iSCSI |
|---|---|---|
| Dynamic address | FC address (24-bit), assigned at fabric login | None — relies entirely on IP addressing at lower layers |
| Static identity | WWN (64-bit), burned into hardware/software | iSCSI name (IQN/EUI/NAA), software-configured |
| Basic transfer unit | FC Frame (up to 2,112 bytes payload) | iSCSI PDU (variable, encapsulated in TCP/IP) |
| Device discovery | Name Server (FFFFFC), Fabric Login Server (FFFFFE) | SendTargets discovery or iSNS server |
| Transport reliability | BB_Credit / EE_Credit flow control (link-level, lossless) | TCP (windowing, retransmission, congestion control) |

Both technologies separate a *dynamic, network-position-dependent address* from a *static, hardware-bound identity* — FC's FC-address/WWN pairing closely parallels how iSCSI conceptually separates the IP-layer addressing from the persistent iSCSI name. However, FC achieves guaranteed, lossless delivery through credit-based flow control intrinsic to the fabric, whereas iSCSI relies on TCP's well-established but comparatively higher-overhead reliability mechanisms running over a potentially lossy IP network.

**Conclusion [2 marks]**

The structured addressing and framing mechanisms of FC and iSCSI reflect their differing design philosophies: FC was purpose-built as a dedicated storage channel-network hybrid with deterministic, low-overhead addressing and frame delivery, while iSCSI was designed to leverage ubiquitous, general-purpose IP infrastructure, trading some of FC's native efficiency for broad compatibility and lower deployment cost.

---

### Essay Question 2 (25 Marks)

**Critically discuss the role of Network-Attached Storage (NAS) in modern data centers. Your answer should cover: the components of a NAS device, the three common NAS implementations (unified, gateway, scale-out), the key file-sharing protocols (NFS and CIFS), and the major factors affecting NAS performance.**

#### Model Answer

**Introduction [2 marks]**

Network-Attached Storage (NAS) emerged as a dedicated, high-performance file-sharing solution to address the proliferation of underutilized and overutilized general-purpose file servers in enterprise environments. By using an operating system specifically optimized for file I/O rather than general-purpose computing, NAS devices serve more clients more efficiently while enabling centralized storage consolidation across heterogeneous (UNIX and Windows) client environments.

**Components of NAS [4 marks]**

A NAS device consists of two key components: the **NAS head** and **storage** (which may be internal or external/shared with other hosts). The NAS head includes: CPU and memory; one or more NICs providing client network connectivity (Gigabit Ethernet, Fast Ethernet, etc.); an operating system optimized for file-serving that translates file-level requests into block-storage requests (and vice versa for responses); and software implementing NFS, CIFS, and other file-sharing protocols, plus industry-standard storage protocols for connecting to physical disk resources.

**Three NAS Implementations [9 marks — 3 marks each]**

**Unified NAS** consolidates both NAS-based (file) and SAN-based (block) data access within a single storage platform. It contains one or more NAS heads connected to shared storage controllers, which also provide iSCSI and FC connectivity for block-level hosts. Because both access types share the same physical storage platform and management interface, unified NAS reduces infrastructure and management costs — but at the cost of some operational entanglement between file and block workloads.

**Gateway NAS** consists of one or more NAS heads using *external and independently managed* storage. Unlike unified NAS, the storage and NAS head have *separate* administrative domains, making management more complex. However, this separation grants superior scalability: NAS heads and storage arrays can each be scaled independently — for example, adding NAS heads to boost performance without necessarily adding storage capacity, or vice versa.

**Scale-out NAS** pools multiple nodes (each consisting of a NAS head, storage, or both) into a clustered system that operates and is managed as a single logical NAS device. A single file system spans all nodes in the cluster; data is striped across all nodes with mirror or parity protection, so any client connecting to any node can access the entire file system. As nodes are added, the file system grows dynamically with data automatically rebalanced, and aggregate storage, memory, CPU, and network capacity — and therefore performance — all increase. This architecture is specifically suited to "Big Data" workloads requiring both massive capacity and flexible, near-unlimited scalability.

**File-Sharing Protocols: NFS and CIFS [6 marks]**

**NFS** (Network File System) is the dominant client-server file-sharing protocol on UNIX systems, using Remote Procedure Calls (RPC) for inter-process communication. NFSv2 and NFSv3 are **stateless** — no information about open files is retained between calls, so each call carries the full set of arguments needed (file handle, position, etc.). NFSv3 (the most widely used version) supports both UDP and TCP and added 64-bit file sizes and asynchronous writes. NFSv4 switched to TCP and a **stateful** design with enhanced security; NFSv4.1 introduced the session model and parallel NFS (pNFS), which separates metadata processing (handled by a dedicated metadata server) from data processing (handled directly between clients and storage via parallel paths), significantly improving client performance.

**CIFS** (Common Internet File System), a public variant of SMB, is the standard for Windows file sharing. Unlike NFS, CIFS is **stateful** — the server tracks connection information for every connected client, enabling it to automatically restore connections and reopen previously open files after a network interruption (provided the client application has the embedded intelligence to take advantage of this). CIFS uses file and record locking to prevent concurrent overwrite conflicts and Unicode encoding for filenames.

**Factors Affecting NAS Performance [4 marks]**

Because NAS relies on an IP network, performance is sensitive to several factors: the **number of hops** (each adds IP processing delay); **authentication latency** with directory services (Active Directory, NIS) under heavy load; **retransmission** caused by link errors, buffer overflows, or speed/duplex mismatches; **overutilized routers/switches/NAS devices/clients**, each adding response delay under load; and **file system lookup and metadata request overhead**, worsened by deep directory structures or poor file-system layout. Mitigations include configuring VLANs, tuning MTU size (jumbo frames, typically 9,000 bytes, reduce per-frame overhead), correctly sizing the TCP window (ideally the product of available bandwidth and round-trip time), and using link aggregation to combine multiple NICs into one logical, higher-throughput, fault-tolerant interface.

**Conclusion [2 marks]**

NAS has evolved from a simple file-server replacement into a flexible, scalable storage architecture capable of meeting the most demanding modern enterprise and Big Data workloads. The choice between unified, gateway, and scale-out implementations — and careful tuning of the underlying IP network — determines whether an organization realizes the full performance and cost benefits that the NAS architecture promises.

---

*End of Practice Examination Set 1 of 4*
