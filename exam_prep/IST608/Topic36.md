Chapter 4
Intelligent Storage Systems
Business-critical applications require high lev- KEY CONCEPTS
els of performance, availability, security, and
Intelligent Storage Systems
scalability. A disk drive is a core element of
storage that governs the performance of any storage
Cache Mirroring and Vaulting
system. Some of the older disk-array technologies
could not overcome performance constraints due to Logical Unit Number
the limitations of disk drives and their mechanical
LUN Masking
components. RAID technology made an important
contribution to enhancing storage performance Meta LUN
and reliability, but disk drives, even with a RAID
Virtual Storage Provisioning
implementation, could not meet the performance
requirements of today’s applications. High-End Storage Systems
With advancements in technology, a new breed
of storage solutions, known as intelligent storage Midrange Storage Systems
systems, has evolved. These intelligent storage
systems are feature-rich RAID arrays that provide highly optimized I/O process-
ing capabilities. These storage systems are confi gured with a large amount of
memory (called cache) and multiple I/O paths and use sophisticated algorithms
to meet the requirements of performance-sensitive applications. These arrays
have an operating environment that intelligently and optimally handles the
management, allocation, and utilization of storage resources. Support for fl ash
drives and other modern-day technologies, such as virtual storage provisioning
and automated storage tiering, has added a new dimension to storage system
performance, scalability, and availability.
This chapter covers components of intelligent storage systems along with
storage provisioning to applications.
71
cc0044..iinndddd 7711 44//1199//22001122 1122::0066::5566 PPMM

72 Section I n Storage System
4.1 Components of an Intelligent Storage System
An intelligent storage system consists of four key components: front end, cache,
back end, and physical disks. Figure 4-1 illustrates these components and their
interconnections. An I/O request received from the host at the front-end port is
processed through cache and back end, to enable storage and retrieval of data
from the physical disk. A read request can be serviced directly from cache if the
requested data is found in the cache. In modern intelligent storage systems, front
end, cache, and back end are typically integrated on a single board (referred to
as a storage processor or storage controller).
Intelligent Storage System
Front End Back End Physical Disks
Host
Connectivity Cache
Storage
Network
Ports Ports
Front-End Back-End
Controllers Controllers
Figure 4-1: Components of an intelligent storage system
4.1.1 Front End
The front end provides the interface between the storage system and the host. It
consists of two components: front-end ports and front-end controllers. Typically,
a front end has redundant controllers for high availability, and each control-
ler contains multiple ports that enable large numbers of hosts to connect to
the intelligent storage system. Each front-end controller has processing logic
that executes the appropriate transport protocol, such as Fibre Channel, iSCSI,
FICON, or FCoE for storage connections.
Front-end controllers route data to and from cache via the internal data bus.
When the cache receives the write data, the controller sends an acknowledg-
ment message back to the host.
4.1.2 Cache
Cache is semiconductor memory where data is placed temporarily to reduce the
time required to service I/O requests from the host.
cc0044..iinndddd 7722 44//1199//22001122 1122::0066::5566 PPMM

Chapter 4 n Intelligent Storage Systems 73
Cache improves storage system performance by isolating hosts from the mechani-
cal delays associated with rotating disks or hard disk drives (HDD). Rotating disks
are the slowest component of an intelligent storage system. Data access on rotating
disks usually takes several millisecond because of seek time and rotational latency.
Accessing data from cache is fast and typically takes less than a millisecond. On
intelligent arrays, write data is fi rst placed in cache and then written to disk.
Structure of Cache
Cache is organized into pages, which is the smallest unit of cache allocation. The
size of a cache page is confi gured according to the application I/O size. Cache
consists of the data store and tag RAM. The data store holds the data whereas
the tag RAM tracks the location of the data in the data store (see Figure 4-2)
and in the disk.
Page
Cache
Disk
Data Store
Tag RAM
Figure 4-2: Structure of cache
Entries in tag RAM indicate where data is found in cache and where the data
belongs on the disk. Tag RAM includes a dirty bit fl ag, which indicates whether
the data in cache has been committed to the disk. It also contains time-based
information, such as the time of last access, which is used to identify cached
information that has not been accessed for a long period and may be freed up.
Read Operation with Cache
When a host issues a read request, the storage controller reads the tag RAM
to determine whether the required data is available in cache. If the requested
data is found in the cache, it is called a read cache hit or read hit and data is sent
directly to the host, without any disk operation (see Figure 4-3 [a]). This provides
cc0044..iinndddd 7733 44//1199//22001122 1122::0066::5566 PPMM

74 Section I n Storage System
a fast response time to the host (about a millisecond). If the requested data is not
found in cache, it is called a cache miss and the data must be read from the disk
(see Figure 4-3 [b]). The back end accesses the appropriate disk and retrieves the
requested data. Data is then placed in cache and fi nally sent to the host through
the front end. Cache misses increase the I/O response time.
Data found in cache = Read Hit
1 Physical Disks
Host
Read
Cache
Request
Send Data
2
(a)
Data not found in cache = Read Miss
1 2 Physical Disks
Host Read Read
Cache
Request Request
Send Data Read from
the Disk
4 3
(b)
Figure 4-3: Read hit and read miss
A prefetch or read-ahead algorithm is used when read requests are sequential.
In a sequential read request, a contiguous set of associated blocks is retrieved.
Several other blocks that have not yet been requested by the host can be read from
the disk and placed into cache in advance. When the host subsequently requests
these blocks, the read operations will be read hits. This process signifi cantly
improves the response time experienced by the host. The intelligent storage
system offers fi xed and variable prefetch sizes. In fi xed prefetch, the intelligent
storage system prefetches a fi xed amount of data. It is most suitable when host
I/O sizes are uniform. In variable prefetch, the storage system prefetches an amount
of data in multiples of the size of the host request. Maximum prefetch limits the
number of data blocks that can be prefetched to prevent the disks from being
rendered busy with prefetch at the expense of other I/Os.
cc0044..iinndddd 7744 44//1199//22001122 1122::0066::5566 PPMM

Chapter 4 n Intelligent Storage Systems 75
Read performance is measured in terms of the read hit ratio, or the hit rate,
usually expressed as a percentage. This ratio is the number of read hits with
respect to the total number of read requests. A higher read hit ratio improves
the read performance.
Write Operation with Cache
Write operations with cache provide performance advantages over writing
directly to disks. When an I/O is written to cache and acknowledged, it is
completed in far less time (from the host’s perspective) than it would take to
write directly to disk. Sequential writes also offer opportunities for optimiza-
tion because many smaller writes can be coalesced for larger transfers to disk
drives with the use of cache.
A write operation with cache is implemented in the following ways:
n Write-back cache: Data is placed in cache and an acknowledgment
is sent to the host immediately. Later, data from several writes are
committed (de-staged) to the disk. Write response times are much
faster because the write operations are isolated from the mechanical
delays of the disk. However, uncommitted data is at risk of loss if cache
failures occur.
n Write-through cache: Data is placed in the cache and immediately writ-
ten to the disk, and an acknowledgment is sent to the host. Because data
is committed to disk as it arrives, the risks of data loss are low, but the
write-response time is longer because of the disk operations.
Cache can be bypassed under certain conditions, such as large size write I/O.
In this implementation, if the size of an I/O request exceeds the predefi ned size,
called write aside size, writes are sent to the disk directly to reduce the impact
of large writes consuming a large cache space. This is particularly useful in an
environment where cache resources are constrained and cache is required for
small random I/Os.
Cache Implementation
Cache can be implemented as either dedicated cache or global cache.
With dedicated cache, separate sets of memory locations are reserved for
reads and writes. In global cache, both reads and writes can use any of the
available memory addresses. Cache management is more effi cient in a global
cache implementation because only one global set of addresses has to be
managed.
Global cache allows users to specify the percentages of cache available for
reads and writes for cache management. Typically, the read cache is small, but
cc0044..iinndddd 7755 44//1199//22001122 1122::0066::5577 PPMM

76 Section I n Storage System
it should be increased if the application being used is read-intensive. In other
global cache implementations, the ratio of cache available for reads versus writes
is dynamically adjusted based on the workloads.
Cache Management
Cache is a fi nite and expensive resource that needs proper management. Even
though modern intelligent storage systems come with a large amount of cache,
when all cache pages are fi lled, some pages have to be freed up to accommodate
new data and avoid performance degradation. Various cache management algo-
rithms are implemented in intelligent storage systems to proactively maintain
a set of free pages and a list of pages that can be potentially freed up whenever
required. The most commonly used algorithms are discussed in the following list:
n Least Recently Used (LRU): An algorithm that continuously monitors
data access in cache and identifi es the cache pages that have not been
accessed for a long time. LRU either frees up these pages or marks them
for reuse. This algorithm is based on the assumption that data that has
not been accessed for a while will not be requested by the host. However,
if a page contains write data that has not yet been committed to disk, the
data is fi rst written to disk before the page is reused.
n Most Recently Used (MRU): This algorithm is the opposite of LRU, where
the pages that have been accessed most recently are freed up or marked for
reuse. This algorithm is based on the assumption that recently accessed
data may not be required for a while.
As cache fi lls, the storage system must take action to fl ush dirty pages (data written
into the cache but not yet written to the disk) to manage space availability. Flushing is
the process that commits data from cache to the disk. On the basis of the I/O access
rate and pattern, high and low levels called watermarks are set in cache to manage
the fl ushing process. High watermark (HWM) is the cache utilization level at which
the storage system starts high-speed fl ushing of cache data. Low watermark (LWM)
is the point at which the storage system stops fl ushing data to the disks. The cache
utilization level, as shown in Figure 4-4, drives the mode of fl ushing to be used:
n Idle fl ushing: Occurs continuously, at a modest rate, when the cache
utilization level is between the high and low watermark.
n High watermark fl ushing: Activated when cache utilization hits the high
watermark. The storage system dedicates some additional resources for
fl ushing. This type of fl ushing has some impact on I/O processing.
n Forced fl ushing: Occurs in the event of a large I/O burst when cache
reaches 100 percent of its capacity, which signifi cantly affects the I/O
response time. In forced fl ushing, system fl ushes the cache on priority
by allocating more resources.
cc0044..iinndddd 7766 44//1199//22001122 1122::0066::5577 PPMM

Chapter 4 n Intelligent Storage Systems 77
100% 100% 100%
HWM HWM HWM
LWM LWM LWM
Idle Flushing High Watermark Forced Flushing
Flushing
LWM = Low Watermark
HWM = High Watermark
Figure 4-4: Types of flushing
Cache Data Protection
Cache is volatile memory, so a power failure or any kind of cache failure will
cause loss of the data that is not yet committed to the disk. This risk of losing
uncommitted data held in cache can be mitigated using cache mirroring and
cache vaulting:
n Cache mirroring: Each write to cache is held in two different memory
locations on two independent memory cards. If a cache failure occurs, the
write data will still be safe in the mirrored location and can be committed
to the disk. Reads are staged from the disk to the cache; therefore, if a
cache failure occurs, the data can still be accessed from the disk. Because
only writes are mirrored, this method results in better utilization of the
available cache.
In cache mirroring approaches, the problem of maintaining cache coherency
is introduced. Cache coherency means that data in two different cache
locations must be identical at all times. It is the responsibility of the array
operating environment to ensure coherency.
n Cache vaulting: The risk of data loss due to power failure can be addressed
in various ways: powering the memory with a battery until the AC
power is restored or using battery power to write the cache content to the
disk. If an extended power failure occurs, using batteries is not a viable
option. This is because in intelligent storage systems, large amounts of
data might need to be committed to numerous disks, and batteries might
not provide power for suffi cient time to write each piece of data to its
intended disk. Therefore, storage vendors use a set of physical disks to
dump the contents of cache during power failure. This is called cache
vaulting and the disks are called vault drives. When power is restored,
data from these disks is written back to write cache and then written
to the intended disks.
cc0044..iinndddd 7777 44//1199//22001122 1122::0066::5577 PPMM

78 Section I n Storage System
SERVER FLASH-CACHING TECHNOLOGY
Server fl ash-caching technology uses intelligent c aching
software and a PCI Express (PCIe) fl ash card on the host.
This dramatically improves application performance by
reducing latency, and accelerates throughput. Server fl ash-
caching technology works in both physical and virtual
environments and provides performance acceleration for
read-intensive workloads. This technology uses minimal CPU and memory
resources from the server by offl oading fl ash management onto the
PCIe card.
It intelligently determines which data would benefi t by sitting in the server
on PCIe fl ash and closer to the application. This avoids the latencies associ-
ated with I/O access over the network to the storage array. With this, the
processing power required for an application’s most frequently referenced
data is offl oaded from the back-end storage to the PCIe card. Therefore, the
storage array can allocate greater processing power to other applications.
4.1.3 Back End
The back end provides an interface between cache and the physical disks.
It consists of two components: back-end ports and back-end controllers. The
back-end controls data transfers between cache and the physical disks. From
cache, data is sent to the back end and then routed to the destination disk.
Physical disks are connected to ports on the back end. The back-end con-
troller communicates with the disks when performing reads and writes and
also provides additional, but limited, temporary data storage. The algorithms
implemented on back-end controllers provide error detection and correction,
along with RAID functionality.
For high data protection and high availability, storage systems are confi g-
ured with dual controllers with multiple ports. Such confi gurations provide
an alternative path to physical disks if a controller or port failure occurs. This
reliability is further enhanced if the disks are also dual-ported. In that case,
each disk port can connect to a separate controller. Multiple controllers also
facilitate load balancing.
4.1.4 Physical Disk
Physical disks are connected to the back-end storage controller and provide
persistent data storage. Modern intelligent storage systems provide support
to a variety of disk drives with different speeds and types, such as FC, SATA,
SAS, and fl ash drives. They also support the use of a mix of fl ash, FC, or SATA
within the same array.
cc0044..iinndddd 7788 44//1199//22001122 1122::0066::5577 PPMM

Chapter 4 n Intelligent Storage Systems 79
4.2 Storage Provisioning
Storage provisioning is the process of assigning storage resources to hosts based
on capacity, availability, and performance requirements of applications running
on the hosts. Storage provisioning can be performed in two ways: traditional
and virtual. Virtual provisioning leverages virtualization technology for provi-
sioning storage for applications. This section details both traditional and virtual
storage provisioning.
4.2.1 Traditional Storage Provisioning
In traditional storage provisioning, physical disks are logically grouped together
and a required RAID level is applied to form a set, called a RAID set. The number
of drives in the RAID set and the RAID level determine the availability, capacity,
and performance of the RAID set. It is highly recommend that the RAID set be
created from drives of the same type, speed, and capacity to ensure maximum
usable capacity, reliability, and consistency in performance. For example, if drives
of different capacities are mixed in a RAID set, the capacity of the smallest drive
is used from each disk in the set to make up the RAID set’s overall capacity.
The remaining capacity of the larger drives remains unused. Likewise, mixing
higher revolutions per minute (RPM) drives with lower RPM drives lowers the
overall performance of the RAID set.
RAID sets usually have a large capacity because they combine the total capac-
ity of individual drives in the set. Logical units are created from the RAID sets by
partitioning (seen as slices of the RAID set) the available capacity into smaller units.
These units are then assigned to the host based on their storage requirements.
Logical units are spread across all the physical disks that belong to that set.
Each logical unit created from the RAID set is assigned a unique ID, called a
logical unit number (LUN). LUNs hide the organization and composition of the
RAID set from the hosts. LUNs created by traditional storage provisioning
methods are also referred to as thick LUNs to distinguish them from the LUNs
created by virtual provisioning methods.
Figure 4-5 shows a RAID set consisting of fi ve disks that have been sliced, or
partitioned, into two LUNs: LUN 0 and LUN 1. These LUNs are then assigned
to Host1 and Host 2 for their storage requirements.
When a LUN is confi gured and assigned to a non-virtualized host, a bus
scan is required to identify the LUN. This LUN appears as a raw disk to the
operating system. To make this disk usable, it is formatted with a fi le system
and then the fi le system is mounted.
In a virtualized host environment, the LUN is assigned to the hypervisor, which
recognizes it as a raw disk. This disk is confi gured with the hypervisor fi le system,
and then virtual disks are created on it. Virtual disks are fi les on the hypervisor
cc0044..iinndddd 7799 44//1199//22001122 1122::0066::5577 PPMM

80 Section I n Storage System
fi le system. The virtual disks are then assigned to virtual machines and appear
as raw disks to them. To make the virtual disk usable to the v irtual machine,
similar steps are followed as in a non-virtualized environment. Here, the LUN
space may be shared and accessed simultaneously by multiple virtual machines.
Host 1
Intelligent Storage System
Physical Disks
Front End Back End (RAID Set)
Cache LUN 0
LLUUNN 00
Storage
Network
LUN 1
LLUUNN 11
Host 2
Figure 4-5: RAID set and LUNs
Virtual machines can also access a LUN directly on the storage system. In this
method the entire LUN is allocated to a single virtual machine. Storing data in
this way is recommended when the applications running on the virtual machine
are response-time sensitive, and sharing storage with other virtual machines may
impact their response time. The direct access method is also used when a virtual
machine is clustered with a physical machine. In this case, the virtual machine
is required to access the LUN that is being accessed by the physical machine.
LUN Expansion: MetaLUN
MetaLUN is a method to expand LUNs that require additional capacity or
performance. A metaLUN can be created by combining two or more LUNs. A
metaLUN consists of a base LUN and one or more component LUNs. MetaLUNs
can be either concatenated or striped.
Concatenated expansion simply adds additional capacity to the base LUN. In
this expansion, the component LUNs are not required to be of the same capacity
as the base LUN. All LUNs in a concatenated metaLUN must be either protected
(parity or mirrored) or unprotected (RAID 0). RAID types within a metaLUN can
be mixed. For example, a RAID 1/0 LUN can be concatenated with a RAID 5 LUN.
However, a RAID 0 LUN can be concatenated only with another RAID 0 LUN.
Concatenated expansion is quick but does not provide any performance
benefi t. (See Figure 4-6.)
cc0044..iinndddd 8800 44//1199//22001122 1122::0066::5577 PPMM

|     |     |     | Chapter 4 n Intelligent Storage Systems  |     |           | 81  |
| --- | --- | --- | ---------------------------------------- | --- | --------- | --- |
| 1   |     |     | 1                                        |     |           |     |
| 2   |     |     | 2                                        |     |           |     |
|     |     |     | 3                                        |     | Increased |     |
3
|          | +          | =   |          |            | Capacity |     |
| -------- | ---------- | --- | -------- | ---------- | -------- | --- |
| 4        |            |     | 4        |            |          |     |
| 5        |            |     | 5        |            |          |     |
| 6        |            |     | 6        |            |          |     |
| Base LUN | Component  |     | Base LUN | Component  |          |     |
|          | LUN        |     |          | LUN        |          |     |
MetaLUN
Figure 4-6: Concatenated metaLUN
Striped expansion restripes the base LUN’s data across the base LUN and
component LUNs. In striped expansion, all LUNs must be of the same capacity
and RAID level. Striped expansion provides improved performance due to the
increased number of drives being striped (see Figure 4-7).
| 1   |     |     | 1   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| 2   |     |     | 3   | 4   |     |     |
| 3   |     |     | 5   | 6   |     |     |
|     | +   | =   |     |     |     |     |
4
Increased
| 5   |     |     |     |     | Capacity |     |
| --- | --- | --- | --- | --- | -------- | --- |
6
| Base LUN | Component |     | Base LUN | Component  |     |     |
| -------- | --------- | --- | -------- | ---------- | --- | --- |
|          | LUN       |     |          | LUN        |     |     |
MetaLUN
Figure 4-7: Striped metaLUN
cc0044..iinndddd      8811 44//1199//22001122      1122::0066::5588  PPMM

82 Section I n Storage System
All LUNs in both concatenated and striped expansion must reside on the
same disk-drive type: either all Fibre Channel or all ATA.
4.2.2 Virtual Storage Provisioning
Virtual provisioning enables creating and presenting a LUN with more capac-
ity than is physically allocated to it on the storage array. The LUN created
using virtual provisioning is called a thin LUN to distinguish it from the
traditional LUN.
Thin LUNs do not require physical storage to be completely allocated to
them at the time they are created and presented to a host. Physical storage is
allocated to the host “on-demand” from a shared pool of physical capacity.
Ashared pool consists of physical disks. A shared pool in virtual provisioning
is analogous to a RAID group, which is a collection of drives on which LUNs
are created. Similar to a RAID group, a shared pool supports a single RAID
protection level. However, unlike a RAID group, a shared pool might contain
large numbers of drives. Shared pools can be homogeneous (containing a single
drive type) or heterogeneous (containing mixed drive types, such as fl ash, FC,
SAS, and SATA drives).
Virtual provisioning enables more effi cient allocation of storage to hosts.
Virtual provisioning also enables oversubscription, where more capacity is
presented to the hosts than is actually available on the storage array. Both
shared pool and thin LUN can be expanded nondisruptively as the storage
requirements of the hosts grow. Multiple shared pools can be created within
a storage array, and a shared pool may be shared by multiple thin LUNs.
Figure 4-8 illustrates the provisioning of thin LUNs.
Comparison between Virtual and Traditional Storage
Provisioning
Administrators typically allocate storage capacity based on anticipated storage
requirements. This generally results in the over provisioning of storage capacity,
which then leads to higher costs and lower capacity utilization. Administrators
often over-provision storage to an application for various reasons, such as, to
avoid frequent provisioning of storage if the LUN capacity is exhausted, and
to reduce disruption to application availability. Over provisioning of storage
often leads to additional storage acquisition and operational costs.
Virtual provisioning addresses these challenges. Virtual provisioning improves
storage capacity utilization and simplifi es storage management. Figure 4-9
shows an example, comparing virtual provisioning with traditional storage
provisioning.
cc0044..iinndddd 8822 44//1199//22001122 1122::0066::5588 PPMM

|     |     |     |     | Chapter 4 n Intelligent Storage Systems  |     |     |     |     | 83  |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |                                          |     | APP | APP |     |     |
|     |     |     |     |                                          |     | OS  | OS  |     |     |
Compute Systems
|     |     |     |     |     |     | VM  | VM  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hypervisor
|     |     |     | Thin  | Thin  |       | Thin  |       |     |     |
| --- | --- | --- | ----- | ----- | ----- | ----- | ----- | --- | --- |
|     |     |     | LUN   | LUN   |       | LUN   |       |     |     |
|     |     |     | 10 TB |       | 10 TB |       | 10 TB |     |     |
|     |     |     |       | 4TB   |       | 3TB   |       |     |     |
3 TB
|     |     | Allocated |     | Allocated |     | Allocated |     |     |     |
| --- | --- | --------- | --- | --------- | --- | --------- | --- | --- | --- |
Disk Drives
Shared Storage Pool (Thin Pool)
Figure 4-8: Virtual provisioning
150 GB
Available
|            |                              | 800 GB        | Capacity        |     |          |                          | 800 GB          |                   |     |
| ---------- | ---------------------------- | ------------- | --------------- | --- | -------- | ------------------------ | --------------- | ----------------- | --- |
|            | 550 GB                       |               |                 |     |          | 550 GB                   |                 | 1.65 TB           |     |
|            |                              |               |  1.5 TB         |     |          |                          |                 | A v a i la b l e  |     |
| 500 GB     |                              | 6 0 0   G B   |   A ll o ca te  | d   | 500 GB   |                          |                 |                   |     |
|            |                              | A ll o c a te | d               |     |          |                          |                 | C a p a c it y    |     |
|            |                              | Unused        | U n u se        | d   |          |                          |                 |                   |     |
| 400 GB     | 500 GB                       |               | Capacity        |     |          |                          |                 |                   |     |
| Allocated  | Allocated                    | Capacity      |                 |     |          |                          |                 |                   |     |
| Unused     | Unused                       |               |                 |     |          |                          |                 |                   |     |
| Capacity   | Capacity                     |               |                 |     |          |                          |                 |                   |     |
|            |                              | 20 0   G B    | 350 GB          |     |          |                          | 2 0 0   G B     |                   |     |
|            |                              | D a t a       |                 |     |          |                          | A ll o c a te d | 350 GB            |     |
| 10 0       |   G B                        |               | Actual Data     |     | 1 0 0    |   G B                    |                 | Actual Data       |     |
| D a        | t a 50 GB                    |               |                 |     | A ll o c | a te d 50 GB             |                 |                   |     |
|            | Data                         |               |                 |     |          | Allocated                |                 |                   |     |
| LUN 1      | LUN 2                        | LUN 3         | Storage System  |     | Thin     | Thin                     | Thin            | Storage System    |     |
|            |                              |               | (2 TB)          |     | LUN 1    | LUN 2                    | LUN 3           | (2 TB)            |     |
|            | (a) Traditional Provisioning |               |                 |     |          | (b) Virtual Provisioning |                 |                   |     |
Figure 4-9: Traditional versus virtual provisioning
cc0044..iinndddd      8833 44//1199//22001122      1122::0066::5588  PPMM

84 Section I n Storage System
With traditional provisioning, three LUNs are created and presented to one
or more hosts (see Figure 4-9 [a]). The total storage capacity of the storage sys-
tem is 2 TB. The allocated capacity of LUN 1 is 500 GB, of which only 100 GB is
consumed, and the remaining 400 GB is unused. The size of LUN 2 is 550 GB,
of which 50 GB is consumed, and 500 GB is unused. The size of LUN 3 is 800
GB, of which 200 GB is consumed, and 600 GB is unused. In total, the storage
system has 350 GB of data, 1.5 TB of allocated but unused capacity, and only
150 GB of remaining capacity available for other applications.
Now consider the same 2 TB storage system with virtual provisioning (see
Figure 4-9 [b]). Here, three thin LUNs of the same sizes are created. However, there
is no allocated unused capacity. In total, the storage system with virtual provi-
sioning has the same 350 GB of data, but 1.65 TB of capacity is available for other
applications, whereas only 150 GB is available in traditional storage provisioning.
Use Cases for Thin and Traditional LUNs
Virtual provisioning and thin LUN offer many benefi ts, although in some cases
traditional LUN is better suited for an application. Thin LUNs are appropriate for
applications that can tolerate performance variations. In some cases, performance
improvement is perceived when using a thin LUN, due to striping across a large
number of drives in the pool. However, when multiple thin LUNs contend for
shared storage resources in a given pool, and when utilization reaches higher
levels, the performance can degrade. Thin LUNs provide the best storage space
effi ciency and are suitable for applications where space consumption is diffi cult
to forecast. Using thin LUNs benefi ts organizations in reducing power and
acquisition costs and in simplifying their storage management.
Traditional LUNs are suited for applications that require predictable perfor-
mance. Traditional LUNs provide full control for precise data placement and
allow an administrator to create LUNs on different RAID groups if there is any
workload contention. Organizations that are not highly concerned about storage
space effi ciency may still use traditional LUNs.
Both traditional and thin LUNs can coexist in the same storage array. Based
on the requirement, an administrator may migrate data between thin and
traditional LUNs.
4.2.3 LUN Masking
LUN masking is a process that provides data access control by defi ning which
LUNs a host can access. The LUN masking function is implemented on the stor-
age array. This ensures that volume access by hosts is controlled appropriately,
preventing unauthorized or accidental use in a shared environment.
For example, consider a storage array with two LUNs that store data of the
sales and fi nance departments. Without LUN masking, both departments
cc0044..iinndddd 8844 44//1199//22001122 1122::0066::5588 PPMM

Chapter 4 n Intelligent Storage Systems 85
can easily see and modify each other’s data, posing a high risk to data
integrity and security. With LUN masking, LUNs are accessible only to the
designated hosts.
4.3 Types of Intelligent Storage Systems
Intelligent storage systems generally fall into one of the following two categories:
n High-end storage systems
n Midrange storage systems
Traditionally, high-end storage systems have been implemented with active-
active confi guration, whereas midrange storage systems have been implemented
with active-passive confi guration. The distinctions between these two implemen-
tations are becoming increasingly insignifi cant.
4.3.1 High-End Storage Systems
High-end storage systems, referred to as active-active arrays, are generally aimed
at large enterprise applications. These systems are designed with a large number
of controllers and cache memory. An active-active array implies that the host can
perform I/Os to its LUNs through any of the available controllers (see Figure 4-10).
Active
LUN
Active
Host
Storage Array
Figure 4-10: Active-active configuration
To address enterprise storage needs, these arrays provide the following
capabilities:
n Large storage capacity
n Large amounts of cache to service host I/Os optimally
cc0044..iinndddd 8855 44//1199//22001122 1122::0066::5599 PPMM

86 Section I n Storage System
n Fault tolerance architecture to improve data availability
n Connectivity to mainframe computers and open systems hosts
n Availability of multiple front-end ports and interface protocols to serve
a large number of hosts
n Availability of multiple back-end controllers to manage disk processing
n Scalability to support increased connectivity, performance, and storage
capacity requirements
n Ability to handle large amounts of concurrent I/Os from a number of
hosts and applications
n Support for array-based local and remote data replication
In addition to these features, high-end systems possess some unique features
that are required for mission-critical applications.
4.3.2 Midrange Storage Systems
Midrange storage systems are also referred to as active-passive arrays and are
best suited for small- and medium-sized enterprise applications. They also
provide optimal storage solutions at a lower cost. In an active-passive array,
a host can perform I/Os to a LUN only through the controller that owns the
LUN. As shown in Figure 4-11, the host can perform reads or writes to the
LUN only through the path to controller A because controller A is the owner
of that LUN. The path to controller B remains passive and no I/O activity is
performed through this path.
Midrange storage systems are typically designed with two controllers,
each of which contains host interfaces, cache, RAID controllers, and interface
to disk drives.
Active
LUN
Passive
Host
Storage Array
Figure 4-11: Active-passive configuration
cc0044..iinndddd 8866 44//1199//22001122 1122::0066::5599 PPMM

Chapter 4 n Intelligent Storage Systems 87
Midrange arrays are designed to meet the requirements of small and medium
enterprise applications; therefore, they host less storage capacity and cache than
high-end storage arrays. There are also fewer front-end ports for connection to hosts.
However, they ensure high redundancy and high performance for applications with
predictable workloads. They also support array-based local and remote replication.
4.4 Concepts in Practice: EMC Symmetrix and VNX
To illustrate the concepts discussed in this chapter, this section covers the EMC
implementation of intelligent storage arrays.
The EMC Symmetrix storage array is an active-active array implementation.
Symmetrix is a solution for customers who require an uncompromising level
of service, performance, and the most advanced business continuity solution
to support large and unpredictable application workloads. Symmetrix also
provides built-in, advanced-level security features and offers the most effi cient
use of power and cooling to support enterprise-level data storage requirements.
The EMC VNX storage array is an active-passive array implementation. It is
EMC’s midrange storage offering that delivers enterprise-quality features and
functionalities. EMC VNX is a unifi ed storage platform that offers storage for
block, fi le, and object-based data within the same array. It is ideally suited for
applications with predictable workloads that require moderate-to-high through-
put. Details of unifi ed storage and EMC VNX are covered in Chapter 8.
For the latest information on Symmetrix and VNX, visit www.emc.com.
4.4.1 EMC Symmetrix Storage Array
EMC Symmetrix establishes the highest standards for performance and
capacity for an enterprise information storage solution and is recognized as
the industry’s most trusted storage platform. Symmetrix offers the highest
level of scalability and performance to meet even unpredictable I/O workload
requirements. The EMC Symmetrix offering includes the Symmetrix Virtual
Matrix (VMAX) series.
The EMC Symmetrix VMAX series is an innovative platform built around
a scalable Virtual Matrix architecture to support the future storage growth
demands of virtual IT environments. Figure 4-12 shows the Symmetrix VMAX
storage array. The key features supported by Symmetrix VMAX follows:
n Incrementally scalable to 2,400 disks
n Supports up to 8 VMAX engines (Each VMAX engine contains a pair of
directors.)
n Supports fl ash drives, fully automated storage tiering (FAST), virtual
provisioning, and Cloud computing
cc0044..iinndddd 8877 44//1199//22001122 1122::0066::5599 PPMM

88 Section I n Storage System
n Supports up to 1 TB of global cache memory
n Supports FC, iSCSI, GigE, and FICON for host connectivity
n Supports RAID levels 1, 1+0, 5, and 6
n Supports storage-based replication through EMC TimeFinder and
EMC SRDF
n Highly fault-tolerant design that allows nondisruptive upgrades and full
component-level redundancy with hot-swappable replacements
76.66
inch
41.88 30.21
inch inch
Figure 4-12: EMC Symmetrix VMAX
4.4.2 EMC Symmetrix VMAX Component
EMC Symmetrix VMAX contains one system bay and up to ten storage bays.
A storage bay supports up to 16 drive array enclosures (DAEs), and each drive
enclosure can house up to 15 drives. The system bay houses the system compo-
nents, which include VMAX Engines, Matrix Interface Board Enclosure (MIBE),
standby power supply (SPS) modules, and service processor:
n VMAX Engine: Consists of a pair of directors that contains four quad-core
Intel processors, up to 128 GB of memory, and up to16 front-end ports
for host access or SRDF channels.
cc0044..iinndddd 8888 44//1199//22001122 1122::0066::5599 PPMM

Chapter 4 n Intelligent Storage Systems 89
n Matrix Interface Board Enclosure (MIBE): Contains two independent
matrix switches that provide point-to point communication between
directors. Each director has two connections to the V-Max Matrix Interface
Board Enclosure. Because every director has two separate physical paths
to every other director via the Virtual Matrix, this is a highly available
interconnect with no single point of failure. This design eliminates
the need for separate interconnects for data, control, messaging, and
environmental and system tests. A single highly available interconnect
suffi ces for all communications between the directors, which reduces
complexity.
n Service Processor: Used for system confi guration and the management
console. It also provides notifi cation and support capabilities to allow access
to the system locally or remotely. The Service Processor automatically
notifi es the vendor’s Customer Support Center whenever a component
failure or environmental violation is detected.
n Symmetrix Enginuity: The operating environment for EMC Symmetrix.
Enginuity manages and ensures the optimal fl ow and integrity of informa-
tion through the various hardware components of the Symmetrix system.
It manages all Symmetrix operations and system resources to optimize
performance intelligently. Enginuity ensures system availability through
advanced fault monitoring, detection, and correction capabilities and
provides concurrent maintenance and serviceability features. It also offers
a foundation for specifi c software features for disaster recovery, business
continuance, and storage management.
4.4.3 Symmetrix VMAX Architecture
Each VMAX engine contains a portion of global memory and two directors
capable of managing front-end, back-end, and remote connections simul-
taneously. The VMAX engine is connected to Virtual Matrix and allows
all system resources, including CPU, memory, drives, and host ports, to be
dynamically accessed and shared by any host. Additional VMAX engines
can be added nondisruptively to efficiently scale system resources. The
Virtual Matrix supports up to eight VMAX engines in a system, as shown
in Figure 4-13.
cc0044..iinndddd 8899 44//1199//22001122 1122::0077::0000 PPMM

ecafretnI xirtaM lautriV
| dnE kcaB eroC       | eroC  labolG  yromeM |     |
| ------------------- | -------------------- | --- |
| stroP ksiD dna tsoH |                      | B   |
eroC eroC
| dnE tnorF eroC | eroC  xelpmoC |     |
| -------------- | ------------- | --- |
 UPC
| eroC | eroC | A   |
| ---- | ---- | --- |
ecafretnI xirtaM lautriV
| dnE kcaB eroC       | eroC  xelpmoC |     |
| ------------------- | ------------- | --- |
| stroP ksiD dna tsoH |  UPC          | B   |
eroC eroC
| dnE tnorF eroC | eroC  yromeM |     |
| -------------- | ------------ | --- |
 labolG
| eroC | eroC | A   |
| ---- | ---- | --- |
stroP ksiD dna tsoH eroCeroC eroCeroC  y lraobmoleGM ecafretnI xirtaM lautriV
B
eroCeroC eroCeroC  xe UlpPmCoC
A
eroCeroC eroCeroC  xe UlpPmCoC ecafretnI xirtaM lautriV
stroP ksiD dna tsoH B  lautriV
xirtaM
eroCeroC eroCeroC  y lraobmoleGM
A
eroCeroC eroCeroC  y lraobmoleGM ecafretnI xirtaM lautriV
stroP ksiD dna tsoH B
erutcetihcra XAMV :31-4 erugiF
eroCeroC eroCeroC  xe UlpPmCoC
A
 xe UlpPmCoC ecafretnI xirtaM lautriV
stroP ksiD dna tsoH eroCeroC eroCeroC B
eroCeroC eroCeroC  y lraobmoleGM
A
cc0044..iinndddd      9900 44//1199//22001122      1122::0077::0000  PPMM

Chapter 4 n Intelligent Storage Systems 91
Summary
This chapter detailed the features and key components of modern intelligent
storage systems. The different types of storage systems, high-end and midrange,
and their characteristics were also explained. An intelligent storage system
provides the following benefi ts to an organization:
n Increased storage capacity
n Improved I/O performance
n Easier storage management
n Improved data availability
n Improved scalability and fl exibility
n Improved business continuity
n Improved security and access control
An intelligent storage system is an integral part of every data center. The
large capacity and high performance supported by the intelligent storage system
makes it necessary to share it among multiple hosts. Intelligent storage systems
enable enterprises to share data easily and securely.
Storage networking is a fl exible information-centric strategy that extends
the reach of intelligent storage systems throughout an enterprise. It provides
a common way to manage, share, and protect enterprise-information assets.
Storage networking is detailed in the next part of this book.
EXERCISES
1. Research Cache Coherency mechanisms, and explain how they address
the environment with multiple shared caches.
2. Which type of application benefits the most by bypassing write cache?
Justify your answer.
3. Research various cache parameters: cache page size, read versus write
cache allocation, cache prefetch size, and write aside size.
4 An Oracle database uses a block size of 4 KB for its I/O operation. The
application that uses this database primarily performs a sequential read
operation. Suggest and explain the appropriate values for the following
cache parameters: cache page size, cache allocation (read versus write),
prefetch type, and write aside size.
5. Research and prepare a presentation on EMC VMAX architecture.
cc0044..iinndddd 9911 44//1199//22001122 1122::0077::0022 PPMM

cc0044..iinndddd 9922 44//1199//22001122 1122::0077::0022 PPMM

Section
II
Storage Networking
Technologies
In This Section
Chapter 5: Fibre Channel Storage Area Networks
Chapter 6: IP SAN and FCoE
Chapter 7: Network-Attached Storage
Chapter 8: Object-Based and Unifi ed Storage
cc0055..iinndddd 9933 44//1199//22001122 1122::0055::5588 PPMM

cc0055..iinndddd 9944 44//1199//22001122 1122::0055::5588 PPMM

Chapter 5
Fibre Channel Storage Area
Networks
Organizations are experiencing an explosive KEY CONCEPTS
growth in information. This information
needs to be stored, protected, optimized, Fibre Channel (FC) Architecture
and managed effi ciently. Data center managers
Fibre Channel Protocol Stack
are burdened with the challenging task of pro-
viding low-cost, high-performance information Ports in Fibre Channel SAN
management solutions. An effective information
Fibre Channel Addressing
management solution must provide the following:
World Wide Names
n Just-in-time information to business
users: Information must be available to
Zoning
business users when they need it. 24 x 7
data availability is becoming one of the Fibre Channel SAN Topologies
key requirements of today’s storage infra-
Block-level Storage
structure. The explosive growth in storage,
Virtualization
proliferation of new servers and applica-
tions, and the spread of mission-critical Virtual SAN
data throughout enterprises are some of
the challenges that need to be addressed to provide information avail-
ability in real time.
n Integration of information infrastructure with business processes: The
storage infrastructure should be integrated with various business processes
without compromising its security and integrity.
n Flexible and resilient storage infrastructure: The storage infrastructure
must provide fl exibility and resilience that aligns with changing business
requirements. Storage should scale without compromising the performance
95
cc0055..iinndddd 9955 44//1199//22001122 1122::0055::5588 PPMM

96 Section II n Storage Networking Technologies
requirements of applications and, at the same time, the total cost of man-
aging information must be low.
Direct-attached storage (DAS) is often referred to as a stovepiped storage environ-
ment. Hosts “own” the storage, and it is diffi cult to manage and share resources
on these isolated storage devices. Efforts to organize this dispersed data led
to the emergence of the storage area network (SAN). SAN is a high-speed, dedi-
cated network of servers and shared storage devices. A SAN provides storage
consolidation and facilitates centralized data management. It meets the storage
demands effi ciently with better economies of scale and also provides effective
maintenance and protection of data. Virtualized SAN and block storage virtual-
ization provide enhanced utilization and collaboration among dispersed storage
resources. The implementation of virtualization in SAN provides improved
productivity, resource utilization, and manageability.
Common SAN deployments are Fibre Channel (FC) SAN and IP SAN. Fibre
Channel SAN uses Fibre Channel protocol for the transport of data, commands,
and status information between servers (or hosts) and storage devices. IP SAN
uses IP-based protocols for communication.
This chapter provides detailed insight into the FC technology on which an
FC SAN is deployed. It also covers FC SAN components, topologies, and block
storage virtualization.
5.1 Fibre Channel: Overview
The FC architecture forms the fundamental construct of the FC SAN infrastructure.
Fibre Channel is a high-speed network technology that runs on high-speed optical
fi ber cables and serial copper cables. The FC technology was developed to meet the
demand for increased speeds of data transfer between servers and mass storage
systems. Although FC networking was introduced in 1988, the FC standardization
process began when the American National Standards Institute (ANSI) chartered
the Fibre Channel Working Group (FCWG). By 1994, the new high-speed computer
interconnection standard was developed and the Fibre Channel Association (FCA)
was founded with 70 charter member companies. Technical Committee T11, which
is the committee within International Committee for Information Technology
Standards (INCITS), is responsible for Fibre Channel interface standards.
High data transmission speed is an important feature of the FC network-
ing technology. The initial implementation offered a throughput of 200 MB/s
(equivalent to a raw bit rate of 1Gb/s), which was greater than the speeds of
Ultra SCSI (20 MB/s), commonly used in DAS environments. In comparison
with Ultra SCSI, FC is a signifi cant leap in storage networking technology. The
latest FC implementations of 16 GFC (Fibre Channel) offer a throughput of
3200 MB/s (raw bit rates of 16 Gb/s), whereas Ultra640 SCSI is available with a
throughput of 640 MB/s. The FC architecture is highly scalable, and theoreti-
cally, a single FC network can accommodate approximately 15 million devices.
cc0055..iinndddd 9966 44//1199//22001122 1122::0055::5588 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 97
5.2 The SAN and Its Evolution
A SAN carries data between servers (or hosts) and storage devices through
Fibre Channel network (see Figure 5-1). A SAN enables storage consolidation
and enables storage to be shared across multiple servers. This improves the
utilization of storage resources compared to direct-attached storage architecture
and reduces the total amount of storage an organization needs to purchase
and manage. With consolidation, storage management becomes centralized
and less complex, which further reduces the cost of managing information.
SAN also enables organizations to connect geographically dispersed servers
and storage.
Servers
APP APP
OS OS
VM VM
Hypervisor
Server Server
FC SAN
Storage Array Storage Array
Figure 5-1: FC SAN implementation
In its earliest implementation, the FC SAN was a simple grouping of hosts
and storage devices connected to a network using an FC hub as a connectivity
device. This confi guration of an FC SAN is known as a Fibre Channel Arbitrated
cc0055..iinndddd 9977 44//1199//22001122 1122::0055::5588 PPMM

98  Section II n Storage Networking Technologies
Loop (FC-AL). Use of hubs resulted in isolated FC-AL SAN islands because hubs
provide limited connectivity and bandwidth.
The inherent limitations associated with hubs gave way to high-performance
FC switches. Use of switches in SAN improved connectivity and performance and
enabled FC SANs to be highly scalable. This enhanced data accessibility to applica-
tions across the enterprise. Now, FC-AL has been almost abandoned for FC SANs
due to its limitations but still survives as a back-end connectivity option to disk
drives. Figure 5-2 illustrates the FC SAN evolution from FC-AL to enterprise SANs.
|        | Servers Servers       |               |        |
| ------ | --------------------- | ------------- | ------ |
|        | APP APP APP           | APP           |        |
|        | OS OS OS              | OS            |        |
|        | VM VM VM              | VM            |        |
|        | Hypervisor Hypervisor |               |        |
| Server | Server Server         | Server Server | Server |
FC Switch
FC Hub
FC Switch
|     | FC Switch |     | FC Switch |
| --- | --------- | --- | --------- |
FC Hub FC Switch
|                    | FC Switch           |                    | FC Switch |
| ------------------ | ------------------- | ------------------ | --------- |
| Storage Array      | Storage Arrays      | Storage Arrays     |           |
| SAN Islands        | Interconnected SANs | Enterprise SANs    |           |
| FC Arbitrated Loop | FC Switched Fabric  | FC Switched Fabric |           |
Fibre Channel SAN Evolution
Figure 5-2: FC SAN evolution
5.3 Components of FC SAN
FC SAN is a network of servers and shared storage devices. Servers and storage
are the end points or devices in the SAN (called nodes). FC SAN infrastructure
consists of node ports, cables, connectors, and interconnecting devices (such as
FC switches or hubs), along with SAN management software.
cc0055..iinndddd      9988 44//1199//22001122      1122::0055::5599  PPMM

Chapter 5 n Fibre Channel Storage Area Networks 99
5.3.1 Node Ports
In a Fibre Channel network, the end devices, such as hosts, storage arrays, and
tape libraries, are all referred to as nodes. Each node is a source or destination of
information. Each node requires one or more ports to provide a physical interface
for communicating with other nodes. These ports are integral components of
host adapters, such as HBA, and storage front-end controllers or adapters. In an
FC environment a port operates in full-duplex data transmission mode with a
transmit (Tx) link and a receive (Rx) link (see Figure 5-3).
Port 0 Tx
Port 0
Port 1 Rx
Link
Port n
Node
Figure 5-3: Nodes, ports, and links
5.3.2 Cables and Connectors
SAN implementations use optical fi ber cabling. Copper can be used for shorter
distances for back-end connectivity because it provides an acceptable signal-to-
noise ratio for distances up to 30 meters. Optical fi ber cables carry data in the
form of light. There are two types of optical cables: multimode and single-mode.
Multimode fi ber (MMF) cable carries multiple beams of light projected at differ-
ent angles simultaneously onto the core of the cable (see Figure 5-4 [a]). Based
on the bandwidth, multimode fi bers are classifi ed as OM1 (62.5μm core), OM2
(50μm core), and laser-optimized OM3 (50μm core). In an MMF transmission,
multiple light beams traveling inside the cable tend to disperse and collide.
This collision weakens the signal strength after it travels a certain distance — a
process known as modal dispersion. An MMF cable is typically used for short
distances because of signal degradation (attenuation) due to modal dispersion.
Single-mode fi ber (SMF) carries a single ray of light projected at the center of the core
(see Figure 5-4 [b]). These cables are available in core diameters of 7 to 11 microns;
cc0055..iinndddd 9999 44//1199//22001122 1122::0055::5599 PPMM

100 Section II n Storage Networking Technologies
the most common size is 9 microns. In an SMF transmission, a single light beam
travels in a straight line through the core of the fi ber. The small core and the single
light wave help to limit modal dispersion. Among all types of fi ber cables, single-
mode provides minimum signal attenuation over maximum distance (up to 10
km). A single-mode cable is used for long-distance cable runs, and distance usually
depends on the power of the laser at the transmitter and sensitivity of the receiver.
Cladding Core Cladding Core
Light In Light In
(a) Multimode Fiber (b) Single-mode Fiber
Figure 5-4: Multimode fiber and single-mode fiber
MMFs are generally used within data centers for shorter distance runs, whereas
SMFs are used for longer distances.
A connector is attached at the end of a cable to enable swift connection and
disconnection of the cable to and from a port. A Standard connector (SC) (see
Figure 5-5 [a]) and a Lucent connector (LC) (see Figure 5-5 [b]) are two commonly
used connectors for fi ber optic cables. Straight Tip (ST) is another fi ber-optic con-
nector, which is often used with fi ber patch panels (see Figure 5.5 [c]).
(a) Standard Connector (SC) (b) Lucent Connector (LC)
(c) Straight Tip Connector (ST)
Figure 5-5: SC, LC, and ST connectors
5.3.3 Interconnect Devices
FC hubs, switches, and directors are the interconnect devices commonly used
in FC SAN.
Hubs are used as communication devices in FC-AL implementations. Hubs
physically connect nodes in a logical loop or a physical star topology. All the
nodes must share the loop because data travels through all the connection
points. Because of the availability of low-cost and high-performance switches,
hubs are no longer used in FC SANs.
cc0055..iinndddd 110000 44//1199//22001122 1122::0066::0000 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 101
Switches are more intelligent than hubs and directly route data from one
physical port to another. Therefore, nodes do not share the bandwidth. Instead,
each node has a dedicated communication path.
Directors are high-end switches with a higher port count and better fault-
tolerance capabilities.
Switches are available with a fi xed port count or with modular design. In a
modular switch, the port count is increased by installing additional port cards
to open slots. The architecture of a director is always modular, and its port
count is increased by inserting additional line cards or blades to the director’s
chassis. High-end switches and directors contain redundant components to
provide high availability. Both switches and directors have management ports
(Ethernet or serial) for connectivity to SAN management servers.
A port card or blade has multiple ports for connecting nodes and
other FC switches. Typically, a Fibre Channel transceiver is installed at each
port slot that houses the transmit (Tx) and receive (Rx) link. In a transceiver,
the Tx and Rx links share common circuitry. Transceivers inside a port card are
connected to an application specifi c integrated circuit, also called port ASIC.
Blades in a director usually have more than one ASIC for higher throughput.
5.3.4 SAN Management Software
SAN management software manages the interfaces between hosts, intercon-
nect devices, and storage arrays. The software provides a view of the SAN
environment and enables management of various resources from one central
console.
It provides key management functions, including mapping of storage devices,
switches, and servers, monitoring and generating alerts for discovered devices,
and zoning (discussed in section 5.9 “Zoning” later in this chapter).
FC SWITCH VERSUS FC HUB
Scalability and performance are the primary differences
between switches and hubs. Addressing in a switched
fabric supports more than 15 million nodes within the fab-
ric, whereas the FC-AL implemented in hubs supports only a
maximum of 126 nodes.
Fabric switches provide full bandwidth between multiple
pairs of ports in a fabric, resulting in a scalable architecture that supports
multiple simultaneous communications.
Hubs support only one communication at a time. They provide a low-cost
connectivity expansion solution. Switches, conversely, can be used to build
dynamic, high-performance fabrics through which multiple communications
can take place simultaneously. Switches are more expensive than hubs.
cc0055..iinndddd 110011 44//1199//22001122 1122::0066::0000 PPMM

102 Section II n Storage Networking Technologies
5.4 FC Connectivity
The FC architecture supports three basic interconnectivity options: point-to-
point, arbitrated loop, and Fibre Channel switched fabric.
5.4.1 Point-to-Point
Point-to-point is the simplest FC confi guration — two devices are connected directly
to each other, as shown in Figure 5-6. This confi guration provides a dedicated
connection for data transmission between nodes. However, the point-to-point con-
fi guration offers limited connectivity, because only two devices can communicate
with each other at a given time. Moreover, it cannot be scaled to accommodate a
large number of nodes. Standard DAS uses point-to-point connectivity.
Servers
APP APP
OS OS
VM VM
Hypervisor
SSeerrvveerr
Server
Storage Array
Figure 5-6: Point-to-point connectivity
5.4.2 Fibre Channel Arbitrated Loop
In the FC-AL confi guration, devices are attached to a shared loop. FC-AL has the
characteristics of a token ring topology and a physical star topology. In FC-AL,
each device contends with other devices to perform I/O operations. Devices on
the loop must “arbitrate” to gain control of the loop. At any given time, only one
device can perform I/O operations on the loop (see Figure 5-7).
cc0055..iinndddd 110022 44//1199//22001122 1122::0066::0000 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 103
Servers
APP APP
OS OS
VM VM
Hypervisor
Server
FC Hub
Server
Storage Array
Figure 5-7: Fibre Channel Arbitrated Loop
As a loop confi guration, FC-AL can be implemented without any intercon-
necting devices by directly connecting one device to another two devices in a
ring through cables.
However, FC-AL implementations may also use hubs whereby the arbitrated
loop is physically connected in a star topology.
The FC-AL confi guration has the following limitations in terms of scalability:
n FC-AL shares the loop and only one device can perform I/O operations
at a time. Because each device in a loop must wait for its turn to process
an I/O request, the overall performance in FC-AL environments is low.
n FC-AL uses only 8-bits of 24-bit Fibre Channel addressing (the remaining
16-bits are masked) and enables the assignment of 127 valid addresses to
the ports. Hence, it can support up to 127 devices on a loop. One address is
reserved for optionally connecting the loop to an FC switch port. Therefore,
up to 126 nodes can be connected to the loop.
n Adding or removing a device results in loop re-initialization, which can
cause a momentary pause in loop traffi c.
5.4.3 Fibre Channel Switched Fabric
Unlike a loop confi guration, a Fibre Channel switched fabric (FC-SW) network
provides dedicated data path and scalability. The addition or removal of a device
cc0055..iinndddd 110033 44//1199//22001122 1122::0066::0000 PPMM

104 Section II n Storage Networking Technologies
in a switched fabric is minimally disruptive; it does not affect the ongoing traf-
fi c between other devices.
FC-SW is also referred to as fabric connect. A fabric is a logical space in which
all nodes communicate with one another in a network. This virtual space can be
created with a switch or a network of switches. Each switch in a fabric contains
a unique domain identifi er, which is part of the fabric’s addressing scheme. In
FC-SW, nodes do not share a loop; instead, data is transferred through a dedicated
path between the nodes. Each port in a fabric has a unique 24-bit Fibre Channel
address for communication. Figure 5-8 shows an example of the FC-SW fabric.
In a switched fabric, the link between any two switches is called an Interswitch
link (ISL). ISLs enable switches to be connected together to form a single, larger
fabric. ISLs are used to transfer host-to-storage data and fabric management traffi c
from one switch to another. By using ISLs, a switched fabric can be expanded
to connect a large number of nodes.
Servers
APP APP
OS OS
VM VM
Hypervisor
Server
FC Switch FC Switch
Storage Array
Interswitch Links
Server
Storage Array
Figure 5-8: Fibre Channel switched fabric
A fabric can be described by the number of tiers it contains. The number of
tiers in a fabric is based on the number of switches traversed between two points
that are farthest from each other. This number is based on the infrastructure
cc0055..iinndddd 110044 44//1199//22001122 1122::0066::0011 PPMM

|     | Chapter 5 n Fibre Channel Storage Area Networks  |     |     |     | 105 |
| --- | ------------------------------------------------ | --- | --- | --- | --- |
constructed by the fabric instead of how the storage and server are connected
across the switches.
When the number of tiers in a fabric increases, the distance that the fabric
management traffi c must travel to reach each switch also increases. This increase
in the distance also increases the time taken to propagate and complete a fabric
reconfi guration event, such as the addition of a new switch or a zone set propa-
gation event. Figure 5-9 illustrates two-tier and three-tier fabric architecture.
|           |           | FC Switch | FC Switch |           |     |
| --------- | --------- | --------- | --------- | --------- | --- |
| FC Switch | FC Switch |           |           | FC Switch |     |
Tier 1
Tier 2
|     | FC Director | FC Director |     |     |     |
| --- | ----------- | ----------- | --- | --- | --- |
FC Director
Tier 3
|           |     | FC Switch | FC Switch   | FC Switch |     |
| --------- | --- | --------- | ----------- | --------- | --- |
| Two-tier  |     |           | Three-tier  |           |     |
Figure 5-9: Tiered structure of Fibre Channel switched fabric
FC-SW Transmission
FC-SW uses switches that can switch data traffi c between nodes directly through
switch ports. Frames are routed between source and destination by the fabric.
As shown in Figure 5-10, if node B wants to communicate with node D, the
nodes should individually login fi rst and then transmit data via the FC-SW. This
link is considered a dedicated connection between the initiator and the target.
| Node A  |          |           |          | Node D  |     |
| ------- | -------- | --------- | -------- | ------- | --- |
|         | Transmit |           | Receive  |         |     |
| Port #1 |          | Port Port |          | Port #2 |     |
|         | Receive  |           | Transmit |         |     |
Node C
Node B
|         | Transmit |           | Receive  |         |     |
| ------- | -------- | --------- | -------- | ------- | --- |
| Port #4 |          | Port Port |          | Port #3 |     |
|         | Receive  |           | Transmit |         |     |
FC Switch
Figure 5-10: Data transmission in Fibre Channel switched fabric
cc0055..iinndddd      110055 44//1199//22001122      1122::0066::0011  PPMM

106 Section II n Storage Networking Technologies
5.5 Switched Fabric Ports
Ports in a switched fabric can be one of the following types:
n N_Port: An end point in the fabric. This port is also known as the node
port. Typically, it is a host port (HBA) or a storage array port connected
to a switch in a switched fabric.
n E_Port: A port that forms the connection between two FC switches. This
port is also known as the expansion port. The E_Port on an FC switch con-
nects to the E_Port of another FC switch in the fabric through ISLs.
n F_Port: A port on a switch that connects an N_Port. It is also known as
a fabric port.
n G_Port: A generic port on a switch that can operate as an E_Port or an
F_Port and determines its functionality automatically during initialization.
Figure 5-11 shows various FC ports located in a switched fabric.
Server
N_Port
F_Port
FC Switch FC Switch
F_Port E_Port E_Port F_Port
ISL
N_Port N_Port
Storage Array Storage Array
Figure 5-11: Switched fabric ports
5.6 Fibre Channel Architecture
Traditionally, host computer operating systems have communicated with periph-
eral devices over channel connections, such as ESCON and SCSI. Channel tech-
nologies provide high levels of performance with low protocol overheads. Such
performance is achievable due to the static nature of channels and the high level
of hardware and software integration provided by the channel technologies.
cc0055..iinndddd 110066 44//1199//22001122 1122::0066::0011 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 107
However, these technologies suffer from inherent limitations in terms of the
number of devices that can be connected and the distance between these devices.
In contrast to channel technology, network technologies are more fl exible and
provide greater distance capabilities. Network connectivity provides greater
scalability and uses shared bandwidth for communication. This fl exibility results
in greater protocol overhead and reduced performance.
The FC architecture represents true channel/network integration and captures
some of the benefi ts of both channel and network technology. FC SAN uses the
Fibre Channel Protocol (FCP) that provides both channel speed for data transfer
with low protocol overhead and scalability of network technology.
FCP forms the fundamental construct of the FC SAN infrastructure. Fibre Channel
provides a serial data transfer interface that operates over copper wire and optical
fi ber. FCP is the implementation of serial SCSI over an FC network. In FCP archi-
tecture, all external and remote storage devices attached to the SAN appear as local
devices to the host operating system. The key advantages of FCP are as follows:
n Sustained transmission bandwidth over long distances.
n Support for a larger number of addressable devices over a network.
Theoretically, FC can support more than 15 million device addresses on
a network.
n Support speeds up to 16 Gbps (16 GFC).
5.6.1 Fibre Channel Protocol Stack
It is easier to understand a communication protocol by viewing it as a structure
of independent layers. FCP defi nes the communication protocol in fi ve layers:
FC-0 through FC-4 (except FC-3 layer, which is not implemented). In a layered
communication model, the peer layers on each node talk to each other through
defi ned protocols. Figure 5-12 illustrates the Fibre Channel protocol stack.
Upper Layer Protocol
Example: SCSI, HIPPI, ESCON, ATM, IP
FC-4 Upper Layer Protocol Mapping
FC-2 Framing/Flow Control
FC-1 Encode/Decode
FC-0 1 Gb/s 2 Gb/s 4 Gb/s 8 Gb/s 16 Gb/s
Figure 5-12: Fibre Channel protocol stack
cc0055..iinndddd 110077 44//1199//22001122 1122::0066::0022 PPMM

108 Section II n Storage Networking Technologies
FC-4 Layer
FC-4 is the uppermost layer in the FCP stack. This layer defi nes the application
interfaces and the way Upper Layer Protocols (ULPs) are mapped to the lower FC
layers. The FC standard defi nes several protocols that can operate on the FC-4
layer (see Figure 5-12). Some of the protocols include SCSI, High Performance
Parallel Interface (HIPPI) Framing Protocol, Enterprise Storage Connectivity
(ESCON), Asynchronous Transfer Mode (ATM), and IP.
FC-2 Layer
The FC-2 layer provides Fibre Channel addressing, structure, and organization
of data (frames, sequences, and exchanges). It also defi nes fabric services, classes
of service, fl ow control, and routing.
FC-1 Layer
The FC-1 layer defi nes how data is encoded prior to transmission and decoded
upon receipt. At the transmitter node, an 8-bit character is encoded into a 10-bit
transmissions character. This character is then transmitted to the receiver node.
At the receiver node, the 10-bit character is passed to the FC-1 layer, which
decodes the 10-bit character into the original 8-bit character. FC links with
speeds of 10 Gbps and above use 64-bit to 66-bit encoding algorithms. The
FC-1 layer also defi nes the transmission words, such as FC frame delimiters,
which identify the start and end of a frame and primitive signals that indicate
events at a transmitting port. In addition to these, the FC-1 layer performs link
initialization and error recovery.
FC-0 Layer
FC-0 is the lowest layer in the FCP stack. This layer defi nes the physical interface,
media, and transmission of bits. The FC-0 specifi cation includes cables, connec-
tors, and optical and electrical parameters for a variety of data rates. The FC
transmission can use both electrical and optical media.
Mainframe SANs use Fibre Connectivity (FICON) for a
low-latency, high-bandwidth connection to the stor-
age controller. FICON was designed as a replacement for
EnterpriseSystemConnection (ESCON) to support main-
frame-attached storage systems.
cc0055..iinndddd 110088 44//1199//22001122 1122::0066::0022 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 109
5.6.2 Fibre Channel Addressing
An FC address is dynamically assigned when a node port logs on to the fabric.
The FC address has a distinct format, as shown in Figure 5-13. The address-
ing mechanism provided here corresponds to the fabric with the switch as an
interconnecting device.
23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Domain ID Area ID Port ID
Figure 5-13: 24-bit FC address of N_Port
The fi rst fi eld of the FC address contains the domain ID of the switch. A domain
ID is a unique number provided to each switch in the fabric. Although this is an
8-bit fi eld, there are only 239 available addresses for domain ID because some
addresses are deemed special and reserved for fabric management services. For
example, FFFFFC is reserved for the name server, and FFFFFE is reserved for the
fabric login service. The area ID is used to identify a group of switch ports used for
connecting nodes. An example of a group of ports with a common area ID is a port
card on the switch. The last fi eld, the port ID, identifi es the port within the group.
Therefore, the maximum possible number of node ports in a switched fabric
is calculated as:
239 domains ¥ 256 areas ¥ 256 ports = 15,663,104
N_PORT ID VIRTUALIZATION (NPIV)
NPIV is a Fibre Channel confi guration that enables multiple
N_Port IDs to share a single physical N_Port. A typical use
of NPIV would be for SAN storage p rovisioning to virtual
machines in a virtualized server environment. With NPIV, sev-
eral virtual machines on a host may share a common physical
N_Port in the host, with each virtual machine using its own
N_Port_ID for that physical node port. For this to work, the FC switch must be
NPIV-enabled.
5.6.3 World Wide Names
Each device in the FC environment is assigned a 64-bit unique identifi er called
the World Wide Name (WWN). The Fibre Channel environment uses two types
of WWNs: World Wide Node Name (WWNN) and World Wide Port Name (WWPN).
Unlike an FC address, which is assigned dynamically, a WWN is a static name
cc0055..iinndddd 110099 44//1199//22001122 1122::0066::0022 PPMM

110  Section II n Storage Networking Technologies
for each node on an FC network. WWNs are similar to the Media Access Control
(MAC) addresses used in IP networking. WWNs are burned into the hardware
or assigned through software. Several confi guration defi nitions in a SAN use
WWN for identifying storage devices and HBAs. The name server in an FC
environment keeps the association of WWNs to the dynamically created FC
addresses for nodes. Figure 5-14 illustrates the WWN structure examples for
an array and an HBA.
World Wide Name - Array
| 5   | 0   | 0 6 0 | 1   | 6 0 0 | 0   | 6   | 0 0 1 B | 2   |
| --- | --- | ----- | --- | ----- | --- | --- | ------- | --- |
0101 0000 0000 0110 0000 0001 0110 0000 0000 0000 0110 0000 0000 0001 1011 0010
|     |     | Company ID |     | Port |     | Model Seed |     |     |
| --- | --- | ---------- | --- | ---- | --- | ---------- | --- | --- |
Format
| Type |     | 24 bits |     |     |     | 32 bits |     |     |
| ---- | --- | ------- | --- | --- | --- | ------- | --- | --- |
World Wide Name - HBA
| 1   | 0        | 0 0 0 | 0          | 0 0 c | 9   | 2   | 0 d c 4          | 0   |
| --- | -------- | ----- | ---------- | ----- | --- | --- | ---------------- | --- |
|     | Reserved |       | Company ID |       |     |     | Company Specific |     |
Format
| Type | 12 bits |     |     | 24 bits |     |     | 24 bits |     |
| ---- | ------- | --- | --- | ------- | --- | --- | ------- | --- |
Figure 5-14: World Wide Names
5.6.4 FC Frame
An FC frame (Figure 5-15) consists of fi ve parts: start of frame (SOF), frame header,
data fi eld, cyclic redundancy check (CRC), and end of frame (EOF).
| SOF     |     | Frame Header |        | Data Field     |       |                | CRC EOF         |     |
| ------- | --- | ------------ | ------ | -------------- | ----- | -------------- | --------------- | --- |
| 4 Bytes |     | 24 Bytes     |        | 0 – 2112 Bytes |       |                | 4 Bytes 4 Bytes |     |
|         |     | R_CTL        |        | Destination ID |       |                |                 |     |
|         |     | CS_CTL       |        | Source ID      |       |                |                 |     |
|         |     | TYPE         |        |                | F_CTL |                |                 |     |
|         |     | SEQ_ID       | DF_CTL |                |       | Sequence Count |                 |     |
|         |     |              | OX_ID  |                |       | RX_ID          |                 |     |
Offset
Figure 5-15: FC frame
cc0055..iinndddd      111100 44//1199//22001122      1122::0066::0022  PPMM

Chapter 5 n Fibre Channel Storage Area Networks 111
The SOF and EOF act as delimiters. In addition to this role, the SOF also
indicates whether the frame is the fi rst frame in a sequence of frames.
The frame header is 24 bytes long and contains addressing information for
the frame. It includes the following information: Source ID (S_ID), Destination
ID (D_ID), Sequence ID (SEQ_ID), Sequence Count (SEQ_CNT), Originating
Exchange ID (OX_ID), and Responder Exchange ID (RX_ID), in addition to
some control fi elds.
The S_ID and D_ID are FC addresses for the source port and the destination
port, respectively. The SEQ_ID and OX_ID identify the frame as a component
of a specifi c sequence and exchange, respectively.
The frame header also defi nes the following fi elds:
n Routing Control (R_CTL): This fi eld denotes whether the frame is a link
control frame or a data frame. Link control frames are frames that do not
carry any user data. These frames are used for setup and messaging. In
contrast, data frames carry the user data.
n Class Specifi c Control (CS_CTL): This fi eld specifi es link speeds for class
1 and class 4 data transmission. (Class of service is discussed in section
5.6.7 “Classes of Service” later in the chapter.)
n TYPE: This fi eld describes the upper layer protocol (ULP) to be carried
on the frame if it is a data frame. However, if it is a link control frame,
this fi eld is used to signal an event such as “fabric busy.” For example, if
the TYPE is 08, and the frame is a data frame, it means that the SCSI will
be carried on an FC.
n Data Field Control (DF_CTL): A 1-byte fi eld that indicates the existence
of any optional headers at the beginning of the data payload. It is a mecha-
nism to extend header information into the payload.
n Frame Control (F_CTL): A 3-byte fi eld that contains control information
related to frame content. For example, one of the bits in this fi eld indicates
whether this is the fi rst sequence of the exchange.
The data fi eld in an FC frame contains the data payload, up to 2,112 bytes of
actual data with 36 bytes of fi xed overhead.
The CRC checksum facilitates error detection for the content of the frame.
This checksum verifi es data integrity by checking whether the content of the
frames are received correctly. The CRC checksum is calculated by the sender
before encoding at the FC-1 layer. Similarly, it is calculated by the receiver after
decoding at the FC-1 layer.
cc0055..iinndddd 111111 44//1199//22001122 1122::0066::0022 PPMM

112 Section II n Storage Networking Technologies
5.6.5. Structure and Organization of FC Data
In an FC network, data transport is analogous to a conversation between two
people, whereby a frame represents a word, a sequence represents a sentence,
and an exchange represents a conversation.
n Exchange: An exchange operation enables two node ports to identify
and manage a set of information units. Each upper layer protocol has its
protocol-specifi c information that must be sent to another port to perform
certain operations. This protocol-specifi c information is called an informa-
tion unit. The structure of these information units is defi ned in the FC-4
layer. This unit maps to a sequence. An exchange is composed of one or
more sequences.
n Sequence: A sequence refers to a contiguous set of frames that are sent
from one port to another. A sequence corresponds to an information unit,
as defi ned by the ULP.
n Frame: A frame is the fundamental unit of data transfer at Layer 2. Each
frame can contain up to 2,112 bytes of payload.
5.6.6 Flow Control
Flow control defi nes the pace of the fl ow of data frames during data transmis-
sion. FC technology uses two fl ow-control mechanisms: buffer-to-buffer credit
(BB_Credit) and end-to-end credit (EE_Credit).
BB_Credit
FC uses the BB_Credit mechanism for fl ow control. BB_Credit controls the maxi-
mum number of frames that can be present over the link at any given point
in time. In a switched fabric, BB_Credit management may take place between
any two FC ports. The transmitting port maintains a count of free receiver buf-
fers and continues to send frames if the count is greater than 0. The BB_Credit
mechanism uses Receiver Ready (R_RDY) primitive that indicates a buffer has
been freed on the port that transmitted the R_RDY.
EE_Credit
The function of end-to-end credit, known as EE_Credit, is similar to that
of BB_Credit. When an initiator and a target establish themselves as nodes
communicating with each other, they exchange the EE_Credit parameters (part
of Port login). The EE_Credit mechanism provides the fl ow control for class 1
and class 2 traffi c only.
cc0055..iinndddd 111122 44//1199//22001122 1122::0066::0033 PPMM

|     | Chapter 5 n Fibre Channel Storage Area Networks  |     |     | 113 |
| --- | ------------------------------------------------ | --- | --- | --- |
5.6.7 Classes of Service
The FC standards defi ne different classes of service to meet the requirements
of a wide range of applications. Table 5-1 shows three classes of services and
their features.
Table 5-1: FC Class of Services
|                    | CLASS 1     | CLASS 2       | CLASS 3       |     |
| ------------------ | ----------- | ------------- | ------------- | --- |
| Communication type | Dedicated   | Nondedicated  | Nondedicated  |     |
|                    | connection  | connection    | connection    |     |
| Flow control       | End-to-end  | End-to-end    | B-to-B credit |     |
|                    | credit      | credit        |               |     |
B-to-B credit
| Frame delivery | In order delivery | Order not    | Order not        |     |
| -------------- | ----------------- | ------------ | ---------------- | --- |
|                |                   | guaranteed   | guaranteed       |     |
| Frame          | Acknowledged      | Acknowledged | Not acknowledged |     |
acknowledgment
| Multiplexing          | No   | Yes      | Yes  |     |
| --------------------- | ---- | -------- | ---- | --- |
| Bandwidth utilization | Poor | Moderate | High |     |
Another class of service is class F, which is used for fabric management. Class
F is similar to Class 2 and provides notifi cation of nondelivery of frames.
5.7 Fabric Services
All FC switches, regardless of the manufacturer, provide a common set of ser-
vices as defi ned in the Fibre Channel standards. These services are available at
certain predefi ned addresses. Some of these services are Fabric Login Server,
Fabric Controller, Name Server, and Management Server (see Figure 5-16).
The Fabric Login Server is located at the predefi ned address of FFFFFE and is
used during the initial part of the node’s fabric login process.
The Name Server (formally known as Distributed Name Server) is located at
the predefi ned address FFFFFC and is responsible for name registration and
management of node ports. Each switch exchanges its Name Server informa-
tion with other switches in the fabric to maintain a synchronized, distributed
name service.
Each switch has a Fabric Controller located at the predefi ned address FFFFFD.
The Fabric Controller provides services to both node ports and other switches.
The Fabric Controller is responsible for managing and distributing Registered
State Change Notifi cations (RSCNs) to the node ports registered with the
cc0055..iinndddd   111133 44//1199//22001122   1122::0066::0033 PPMM

114 Section II n Storage Networking Technologies
Fabric Controller. If there is a change in the fabric, RSCNs are sent out by a
switch to the attached node ports. The Fabric Controller also generates Switch
Registered State Change Notifi cations (SW-RSCNs) to every other domain
(switch) in the fabric. These RSCNs keep the name server up-to-date on all
switches in the fabric.
Fabric Login Management
Fabric Controller Name Server
Server Server
FFFFFD FFFFFC
FFFFFE FFFFFA
Switch Port Switch Port Switch Port Switch Port
I/O I/O I/O I/O
Figure 5-16: Fabric services provided by FC switches
FFFFFA is the Fibre Channel address for the Management Server. The Management
Server is distributed to every switch within the fabric. The Management Server
enables the FC SAN management software to retrieve information and admin-
ister the fabric.
5.8 Switched Fabric Login Types
Fabric services defi ne three login types:
n Fabric login (FLOGI): Performed between an N_Port and an F_Port. To
log on to the fabric, a node sends a FLOGI frame with the WWNN and
WWPN parameters to the login service at the predefi ned FC address
FFFFFE (Fabric Login Server). In turn, the switch accepts the login and
returns an Accept (ACC) frame with the assigned FC address for the node.
Immediately after the FLOGI, the N_Port registers itself with the local
Name Server on the switch, indicating its WWNN, WWPN, port type,
class of service, assigned FC address and so on. After the N_Port has
logged in, it can query the name server database for information about
all other logged in ports.
cc0055..iinndddd 111144 44//1199//22001122 1122::0066::0033 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 115
n Port login (PLOGI): Performed between two N_Ports to establish a session.
The initiator N_Port sends a PLOGI request frame to the target N_Port,
which accepts it. The target N_Port returns an ACC to the initiator N_Port.
Next, the N_Ports exchange service parameters relevant to the session.
n Process login (PRLI): Also performed between two N_Ports. This login
relates to the FC-4 ULPs, such as SCSI. If the ULP is SCSI, N_Ports exchange
SCSI-related service parameters.
5.9 Zoning
Zoning is an FC switch function that enables node ports within the fabric to be
logically segmented into groups and to communicate with each other within
the group (see Figure 5-17).
Servers
APP APP
OS OS
VM VM
Hypervisor
Server
FC SAN
Server
Storage Array
Figure 5-17: Zoning
Whenever a change takes place in the name server database, the fabric
controller sends a Registered State Change Notifi cation (RSCN) to all the
nodes impacted by the change. If zoning is not confi gured, the fabric control-
ler sends an RSCN to all the nodes in the fabric. Involving the nodes that are
not impacted by the change results in increased fabric-management traffi c. For
cc0055..iinndddd 111155 44//1199//22001122 1122::0066::0033 PPMM

116 Section II n Storage Networking Technologies
a large fabric, the amount of FC traffi c generated due to this process can be
signifi cant and might impact the host-to-storage data traffi c. Zoning helps
to limit the number of RSCNs in a fabric. In the presence of zoning, a fabric
sends the RSCN to only those nodes in a zone where the change has occurred.
Zone members, zones, and zone sets form the hierarchy defi ned in the zoning
process (see Figure 5-18). A zone set is composed of a group of zones that can
be activated or deactivated as a single entity in a fabric. Multiple zone sets may
be defi ned in a fabric, but only one zone set can be active at a time. Members
are nodes within the SAN that can be included in a zone. Switch ports, HBA
ports, and storage device ports can be members of a zone. A port or node can
be a member of multiple zones. Nodes distributed across multiple switches in
a switched fabric may also be grouped into the same zone. Zone sets are also
referred to as zone confi gurations.
Zone set
Zone Zone Zone
Member Member Member Member Member Member
Figure 5-18: Members, zones, and zone sets
Zoning provides control by allowing only the members in the same zone
to establish communication with each other.
5.9.1 Types of Zoning
Zoning can be categorized into three types:
n Port zoning: Uses the physical address of switch ports to defi ne zones.
In port zoning, access to node is determined by the physical switch port
to which a node is connected. The zone members are the port identifi er
(switch domain ID and port number) to which HBA and its targets (storage
devices) are connected. If a node is moved to another switch port in the
cc0055..iinndddd 111166 44//1199//22001122 1122::0066::0033 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 117
fabric, then zoning must be modifi ed to allow the node, in its new port,
to participate in its original zone. However, if an HBA or storage device
port fails, an administrator just has to replace the failed device without
changing the zoning confi guration.
n WWN zoning: Uses World Wide Names to defi ne zones. The zone mem-
bers are the unique WWN addresses of the HBA and its targets (storage
devices). A major advantage of WWN zoning is its fl exibility. WWN zoning
allows nodes to be moved to another switch port in the fabric and main-
tain connectivity to its zone partners without having to modify the zone
confi guration. This is possible because the WWN is static to the node port.
n Mixed zoning: Combines the qualities of both WWN zoning and port
zoning. Using mixed zoning enables a specifi c node port to be tied to the
WWN of another node.
Figure 5-19 shows the three types of zoning on an FC network.
Switch Domain ID = 15
Port 5
Server Zone 2
Port 12
Port 1
WWN 10:00:00:00:C9:20:DC:40 Storage Array
FC Switch
Server
Zone 3 Port 9
WWN 10:00:00:00:C9:20:DC:56
WWN 50:06:04:82:E8:91:2B:9E
Server Zone 1
WWN 10:00:00:00:C9:20:DC:82
Zone 1 (WWN Zone) = 10:00:00:00:C9:20:DC:82 ; 50:06:04:82:E8:91:2B:9E
Zone 2 (Port Zone) = 15,5 ; 15,12
Zone 3 (Mixed Zone) = 10:00:00:00:C9:20:DC:56 ; 15,12
Figure 5-19: Types of zoning
Zoning is used with LUN masking to control server access to storage. However,
these are two different activities. Zoning takes place at the fabric level and LUN
masking is performed at the array level.
cc0055..iinndddd 111177 44//1199//22001122 1122::0066::0033 PPMM

118 Section II n Storage Networking Technologies
SINGLE HBA ZONING
Single HBA zoning is considered as an industry best practice
to confi gure a zone set. A single HBA zone consists of one
HBA port and one or more storage device ports. Single HBA
zoning eliminates unnecessary host-to-host interaction and
minimizes RSCNs. Single HBA zoning in a large fabric leads to
confi guring a large number of zones and more administrative
actions. However, this practice improves the FC SAN performance and reduces
the time to troubleshoot FC SAN-related problems.
5.10 FC SAN Topologies
Fabric design follows standard topologies to connect devices. Core-edge fabric
is one of the popular topologies for fabric designs. Variations of core-edge fabric
and mesh topologies are most commonly deployed in FC SAN implementations.
5.10.1 Mesh Topology
A mesh topology may be one of the two types: full mesh or partial mesh. In
afull mesh, every switch is connected to every other switch in the topology. A
full mesh topology may be appropriate when the number of switches involved
is small. A typical deployment would involve up to four switches or directors,
with each of them servicing highly localized host-to-storage traffi c. In a full
mesh topology, a maximum of one ISL or hop is required for host-to-storage
traffi c. However, with the increase in the number of switches, the number of
switch ports used for ISL also increases. This reduces the available switch ports
for node connectivity.
In a partial mesh topology, several hops or ISLs may be required for the traf-
fi c to reach its destination. Partial mesh offers more scalability than full mesh
topology. However, without proper placement of host and storage devices, traf-
fi c management in a partial mesh fabric might be complicated and ISLs could
become overloaded due to excessive traffi c aggregation. Figure 5-20 depicts both
partial mesh and full mesh topologies.
A SINGLE-SWITCH TOPOLOGY
A single-switch fabric consists of only a single switch or
single director. This topology is becoming popular, especially
in large data centers, due to their inherent simplicity. Larger
port count and modular and scalable architecture of switches
and directors allow SAN design to start small and grow as
needed by adding port cards/blades in the switch rather than
adding new switches.
cc0055..iinndddd 111188 44//1199//22001122 1122::0066::0044 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 119
Partial Mesh Full Mesh
FC Switches FC Switches
Server Server
Storage Array Storage Array
Figure 5-20: Partial mesh and full mesh topologies
5.10.2 Core-Edge Fabric
The core-edge fabric topology has two types of switch tiers. The edge tier is usu-
ally composed of switches and offers an inexpensive approach to adding more
hosts in a fabric. Each switch at the edge tier is attached to a switch at the core
tier through ISLs.
The core tier is usually composed of enterprise directors that ensure high fabric
availability. In addition, typically all traffi c must either traverse this tier or termi-
nate at this tier. In this confi guration, all storage devices are connected to the core
tier, enabling host-to-storage traffi c to traverse only one ISL. Hosts that require
high performance may be connected directly to the core tier and consequently
avoid ISL delays.
In core-edge topology, the edge-tier switches are not connected to each other.
The core-edge fabric topology increases connectivity within the SAN while
conserving the overall port utilization. If fabric expansion is required, additional
edge switches are connected to the core. The core of the fabric is also extended
by adding more switches or directors at the core tier. Based on the number of
core-tier switches, this topology has different variations, such as, single-core
topology (see Figure 5-21) and dual-core topology (see Figure 5-22). To transform
a single-core topology to dual-core, new ISLs are created to connect each edge
switch to the new core switch in the fabric.
Benefi ts and Limitations of Core-Edge Fabric
The core-edge fabric provides maximum one-hop storage access to all storage
devices in the system. Because traffi c travels in a deterministic pattern (from
the edge to the core and vice versa), a core-edge provides easier calculation of
the ISL load and traffi c patterns. In this topology, because each tier’s switch port
cc0055..iinndddd 111199 44//1199//22001122 1122::0066::0055 PPMM

120 Section II n Storage Networking Technologies
is used for either storage or hosts, it’s easy to identify which network resources
are approaching their capacity, making it easier to develop a set of rules for
scaling and apportioning.
Edge Tier
FC Switch FC Switch FC Switch
Server Storage Array
FC Director
Core Tier
Figure 5-21: Single-core topology
Edge Tier
FC Switch FC Switch FC Switch
FC Director FC Director
Server Storage Array
Core Tier
Figure 5-22: Dual-core topology
Core-edge fabrics are scaled to larger environments by adding more core
switches and linking them, or adding more edge switches. This method enables
extending the existing simple core-edge model or expanding the fabric into a
compound or complex core-edge model.
However, the core-edge fabric might lead to some performance-related prob-
lems because scaling a core-edge topology involves increasing the number of
hop counts in the fabric. Hop count represents the total number of ISLs traversed
by a packet between its source and destination. A common best practice is to
keep the number of host-to-storage hops unchanged, at one hop, in a core-edge.
Generally, a large hop count means a high data transmission delay between the
source and destination.
cc0055..iinndddd 112200 44//1199//22001122 1122::0066::0055 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 121
As the number of cores increases, it is prohibitive to continue to maintain
ISLs from each core to each edge switch. When this happens, the fabric design
is changed to a compound or complex core-edge design (see Figure 5-23).
Servers
APP APP
OS OS
VM VM
Hypervisor
Edge Tier
Storage Array
Core Tier
Storage Array
Edge Tier
Server
Figure 5-23: Compound core-edge topology
FAN-OUT AND FAN-IN
Fan-out enables multiple server ports to communicate to
a single storage port. A four-server connection to a single-
storage port results in a fan-out ratio of 4. The fan-out ratio of
a storage port is dependent on the capabilities of the storage
system. The key parameter that governs the fan-out ratio of a
storage port is the front-end processing capability of the stor-
age system. Typically, the product vendor specifi es the fan-out ratio of a storage
system.
Fan-in refers to the number of storage ports that a single server port uses.
Similar to fan-out, the restriction on fan-in is based on the capability of the
host-bus adapter.
cc0055..iinndddd 112211 44//1199//22001122 1122::0066::0055 PPMM

122 Section II n Storage Networking Technologies
5.11 Virtualization in SAN
This section details two network-based virtualization techniques in a SAN
environment: block-level storage virtualization and virtual SAN (VSAN).
5.11.1 Block-level Storage Virtualization
Block-level storage virtualization aggregates block storage devices (LUNs) and
enables provisioning of virtual storage volumes, independent of the underlying
physical storage. A virtualization layer, which exists at the SAN, abstracts the
identity of physical storage devices and creates a storage pool from heteroge-
neous storage devices. Virtual volumes are created from the storage pool and
assigned to the hosts. Instead of being directed to the LUNs on the individual
storage arrays, the hosts are directed to the virtual volumes provided by the
virtualization layer. For hosts and storage arrays, the virtualization layer appears
as the target and initiator devices, respectively. The virtualization layer maps
the virtual volumes to the LUNs on the individual arrays. The hosts remain
unaware of the mapping operation and access the virtual volumes as if they
were accessing the physical storage attached to them. Typically, the virtualiza-
tion layer is managed via a dedicated virtualization appliance to which the
hosts and the storage arrays are connected.
Figure 5-24 illustrates a virtualized environment. It shows two physical servers,
each of which has one virtual volume assigned. These virtual volumes are used
by the servers. These virtual volumes are mapped to the LUNs in the storage
arrays. When an I/O is sent to a virtual volume, it is redirected through the
virtualization layer at the storage network to the mapped LUNs. Depending on
the capabilities of the virtualization appliance, the architecture may allow for
more complex mapping between array LUNs and virtual volumes.
Block-level storage virtualization enables extending the storage volumes
online to meet application growth requirements. It consolidates heterogeneous
storage arrays and enables transparent volume access.
Block-level storage virtualization also provides the advantage of nondisrup-
tive data migration. In a traditional SAN environment, LUN migration from
one array to another is an offl ine event because the hosts needed to be updated
to refl ect the new array confi guration. In other instances, host CPU cycles were
required to migrate data from one array to the other, especially in a multivendor
environment. With a block-level virtualization solution in place, the virtual-
ization layer handles the back-end migration of data, which enables LUNs to
remain online and accessible while data is migrating. No physical changes
are required because the host still points to the same virtual targets on the
virtualization layer. However, the mappings information on the virtualization
cc0055..iinndddd 112222 44//1199//22001122 1122::0066::0066 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 123
layer should be changed. These changes can be executed dynamically and are
transparent to the end user.
Servers
APP APP
OS OS
VM VM
Hypervisor
Server
FC SAN
Virtual Volume Virtual Volume
Virtualization
Appliance
Storage Pool
LUN LUN
LUN LUN
Storage Array Storage Array
Figure 5-24: Block-level storage virtualization
Previously, block-level storage virtualization provided nondisruptive data
migration only within a data center. The new generation of block-level storage
virtualization enables nondisruptive data migration both within and between
data centers. It provides the capability to connect the virtualization layers at
multiple data centers. The connected virtualization layers are managed cen-
trally and work as a single virtualization layer stretched across data centers (see
Figure 5-25). This enables the federation of block-storage resources both within
and across data centers. The virtual volumes are created from the federated
storage resources.
cc0055..iinndddd 112233 44//1199//22001122 1122::0066::0066 PPMM

124 Section II n Storage Networking Technologies
Data Center 1 Data Center 2
Servers Servers
APP APP APP APP
OS OS OS OS
VM VM VM VM
Hypervisor Hypervisor
Server Server
Virtual Virtual
Volumes Virtualization Appliance Volumes
FC or IP
FC SAN FC SAN
Virtualization Layer
Storage Arrays Storage Arrays
Figure 5-25: Federation of block storage across data centers
5.11.2 Virtual SAN (VSAN)
Virtual SAN (also called virtual fabric) is a logical fabric on an FC SAN, which
enables communication among a group of nodes regardless of their physical
location in the fabric. In a VSAN, a group of hosts or storage ports communicate
with each other using a virtual topology defi ned on the physical SAN. Multiple
VSANs may be created on a single physical SAN. Each VSAN acts as an indepen-
dent fabric with its own set of fabric services, such as name server, and zoning.
Fabric-related confi gurations in one VSAN do not affect the traffi c in another.
VSANs improve SAN security, scalability, availability, and manageability.
VSANs provide enhanced security by isolating the sensitive data in a VSAN and
by restricting access to the resources located within that VSAN. The same Fibre
Channel address can be assigned to nodes in different VSANs, thus increasing the
fabric scalability. Events causing traffi c disruptions in one VSAN are contained
cc0055..iinndddd 112244 44//1199//22001122 1122::0066::0066 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 125
within that VSAN and are not propagated to other VSANs. VSANs facilitate
an easy, fl exible, and less expensive way to manage networks. Confi guring
VSANs is easier and quicker compared to building separate physical FC SANs
for various node groups. To regroup nodes, an administrator simply changes
the VSAN confi gurations without moving nodes and recabling. VSAN is further
discussed in Chapter 14.
5.12 Concepts in Practice: EMC Connectrix and
EMC VPLEX
The EMC Connectrix family represents the industry’s most extensive selection
of networked storage connectivity products. Connectrix integrates high-speed
Fibre Channel connectivity, highly resilient switching technology, options for
intelligent IP storage networking, and I/O consolidation with products that
support Fibre Channel over Ethernet.
EMC VPLEX is the next-generation solution for block-level virtualization and
data mobility within, across, and between data centers. EMC VPLEX provides
storage federation by aggregating storage arrays that can be located either in
a single data center or multiple data centers. VPLEX is also used as the data
mobility solution for environments like cloud computing.
For the latest information on Connectrix connectivity products and VPLEX,
visit www.emc.com.
5.12.1 EMC Connectrix
EMC offers the following connectivity products under the Connectrix brand
(see Figure 5-26):
n Enterprise directors
n Departmental switches
n Multi-purpose switches
Enterprise directors are ideal for large enterprise connectivity. They offer
high port density and high component redundancy. Enterprise directors are
deployed in high-availability or large-scale environments. Connectrix direc-
tors offer several hundred ports per domain. Departmental switches are best
suited for workgroup, mid-tier environments. Multi-purpose switches support
various protocols such as iSCSI, FCIP, FCoE, FICON, in addition to FC proto-
col. In addition to FC ports, Connectrix switches and directors have Ethernet
ports and serial ports for communication and switch management functions.
The Connectrix management software enables confi guration, monitoring, and
management of Connectrix switches.
cc0055..iinndddd 112255 44//1199//22001122 1122::0066::0077 PPMM

126 Section II n Storage Networking Technologies
Departmental Switch
Enterprise Director Multi-purpose Switch
Figure 5-26: EMC Connectrix
Connectrix Switches
B-series and MDS-series make up the Connectrix family of switches offered
by EMC. These switches are designed to meet workgroup, department-level,
and enterprise-level requirements. They are designed with a nonblocking
architecture and can operate in heterogeneous environments. Nonblocking
architecture refers to the capability of a switch to handle independent packets
simultaneously because the switch has suffi cient internal resources to handle
maximum transfer rates from all ports. The features of these switches that ensure
their high availability are their nondisruptive software and port upgrade, and
redundant and hot-swappable components. These switches can be managed
through CLI, HTTP, and standalone GUI applications.
Connectrix Directors
EMC offers the high-end Connectrix family of directors. Their modular archi-
tectural design offers high scalability by providing over 500 ports. They are
suitable for server and storage consolidation across enterprises. These directors
have redundant components for high availability and provide multiprotocol
connectivity for both mainframe and open system environments. Connectrix
directors offer high speeds (up to 16 Gb/s) and support ISL aggregation. Similar
to switches, directors can also be managed through CLI or with other GUI tools.
Connectrix Multi-purpose Switches
Multi-purpose switches provide support for multiple protocols, such as FC,
FCIP, iSCSI, FCoE, and FICON. They perform protocol translation and route
frames between two dissimilar networks, such as FC and IP. These multiprotocol
cc0055..iinndddd 112266 44//1199//22001122 1122::0066::0077 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 127
capabilities offer many benefi ts, including long-distance SAN extension, greater
resource sharing, and simplifi ed management. Connectrix multi-purpose switches
include FCoE switches, FCIP routers, iSCSI gateways, and so on.
Connectrix Management Tools
There are several ways to monitor and manage FC switches in a fabric. Individual
switch management is accomplished through the CLI or browser-based tools.
Command-line utilities such as Telnet and Secure Shell (SSH) are used to log
on to the switch over IP and issue CLI commands. The primary purpose of the
CLI is to automate the management of a large number of switches or directors
with the use of scripts. The browser-based tools provide GUIs. These tools also
display the topology map.
Fabric-wide management and monitoring is accomplished by using vendor-
specifi c tools and Simple Network Management Protocol (SNMP)-based, third-
party software.
EMC ControlCenter SAN Manager provides a single interface for managing
a Storage Area Network. With SAN Manager, an administrator can discover,
monitor, manage, and confi gure complex heterogeneous SAN environments.
It streamlines and centralizes SAN management operations across multiven-
dor storage networks and storage devices. It enables storage administrators to
manage SAN zones and LUN masking consistently across multivendor SAN
arrays and switches. EMC ControlCenter SAN Manager also supports virtual
environments, including VMware, and virtual SANs.
EMC ProSphere is a newly launched tool with additional features specifi cally
for the cloud computing environment. A future release of EMC ProSphere will
include all the functionalities of EMC ControlCenter.
5.12.2 EMC VPLEX
EMC VPLEX provides a virtual storage infrastructure that enables federation of
heterogeneous storage resources both within and across datacenters. The VPLEX
appliance resides between the servers and heterogeneous storage devices. It
forms a pool of distributed block storage resources and enables creating virtual
storage volumes from the pool. These virtual volumes are then allocated to the
servers. The virtual-to-physical-storage mapping remains hidden to the servers.
VPLEX provides nondisruptive data mobility among physical storage devices
to balance the application workload and to enable both local and remote data
access. The mapping of virtual volumes to physical volumes can be changed
dynamically by the administrator. This allows for a virtual volume to be moved
across storage arrays while still in production.
cc0055..iinndddd 112277 44//1199//22001122 1122::0066::1100 PPMM

128 Section II n Storage Networking Technologies
VPLEX uses a unique clustering architecture and distributed cache coherency
that enable multiple hosts located across two locations to access a single copy of
data. This eliminates the operational overhead and time required to copy and
distribute data across locations VPLEX also provides the capability to mirror
data of a virtual volume both within and across locations. This enables hosts at
different data centers to access cache-coherent copies of the same virtual volume.
Practical applications of this capability include mobility, load-balancing, and
high availability across data centers.
To avoid application downtime due to outage at a data center, the workload
can be moved quickly to another data center. Applications continue accessing
the same virtual volume and remain uninterrupted by the data mobility.
VPLEX Family of Products
The VPLEX family consists of three products: VPLEX Local, VPLEX Metro, and
VPLEX Geo.
EMC VPLEX Local delivers local federation, which provides simplifi ed man-
agement and nondisruptive data mobility across heterogeneous arrays within a
data center. EMC VPLEX Metro delivers distributed federation, which provides
data access and mobility between two VPEX clusters within synchronous dis-
tances that support round-trip latency up to 5 ms. EMC VPLEX Geo delivers
data access and mobility between two VPLEX clusters within asynchronous
distances (that support round-trip latency up to 50 ms).
Summary
The FC SAN has enabled the consolidation of storage and benefi ted organiza-
tions by lowering the cost of storage infrastructure. FC SAN reduces overall
operational cost and downtime. Virtualization of storage and storage networks
further minimizes resource management complexity and cost. The adoption of
FC SANs has increased with the decline of hardware prices and has enhanced
to the maturity of storage network standards.
This chapter detailed the components of an FC SAN, its topologies, and the
FC technology that forms its backbone. FC meets today’s demands for reliable,
and high-performance applications. The chapter also covered virtualization in
a SAN environment.
The interoperability between FC switches from different vendors has enhanced
signifi cantly compared to early SAN deployments. The standards published by
a dedicated study group within T11 on FC SAN routing, and the new product
offerings from vendors, are now revolutionizing the way FC SANs are deployed
and operated.
cc0055..iinndddd 112288 44//1199//22001122 1122::0066::1111 PPMM

Chapter 5 n Fibre Channel Storage Area Networks 129
Although FC SANs have eliminated islands of storage, their implementation
requires additional equipment and infrastructure in an enterprise. The emer-
gence of the iSCSI and FCIP technologies, detailed in Chapter 6, has pushed the
convergence of FC SAN with IP technology, providing a cost-effective method
to leverage existing IP based infrastructure for storage networking.
EXERCISES
1. What is zoning? Discuss a scenario:
a. Where WWN zoning is preferred over port zoning.
b. Where port zoning is preferred over WWN zoning.
2. Describe the process of assigning an FC address to a node when logging
on to the network for the first time.
3. Seventeen switches, with 16 ports each, are connected in a full mesh
topology. How many ports are available for host and storage connectivity?
4. Discuss the roles of the name server and fabric controller in an
FC-switched fabric.
5. How does flow control work in an FC network?
6. Explain storage migration using block-level storage virtualization.
Compare this migration with traditional migration methods.
7. How do VSANs improve the manageability of an FC SAN?
cc0055..iinndddd 112299 44//1199//22001122 1122::0066::1111 PPMM

cc0055..iinndddd 113300 44//1199//22001122 1122::0066::1111 PPMM

Chapter 6
IP SAN and FCoE
Traditional SAN enables the transfer of block KEY CONCEPTS
I/O over Fibre Channel and provides high
performance and scalability. These advan- iSCSI Protocol
tages of FC SAN come with the additional cost
Native and Bridged iSCSI
of buying FC components, such as FC HBA and
switches. Organizations typically have an exist- FCIP Protocol
ing Internet Protocol (IP)-based infrastructure,
FCoE Protocol
which could be leveraged for storage networking.
Advancements in technology have enabled IP to be
used for transporting block I/O over the IP network. This technology of trans-
porting block I/Os over an IP is referred to as IP SAN. IP is a mature technology,
and using IP as a storage networking option provides several advantages. When
block I/O is run over IP, the existing network infrastructure can be leveraged,
which is more economical than investing in a new SAN infrastructure. In addi-
tion, many robust and mature security options are now available for IP networks.
Many long-distance, disaster recovery (DR) solutions are already leveraging
IP-based networks. With IP SAN, organizations can extend the geographical
reach of their storage infrastructure.
Two primary protocols that leverage IP as the transport mechanism are Internet
SCSI (iSCSI) and Fibre Channel over IP (FCIP). iSCSI is encapsulation of SCSI I/O
over IP. FCIP is a protocol in which an FCIP entity such as an FCIP gateway is used
to tunnel FC fabrics through an IP network. In FCIP, FC frames are encapsulated
onto the IP payload. An FCIP implementation is capable of merging interconnected
fabrics into a single fabric. Frequently, only a small subset of nodes at either end
require connectivity across fabrics. Thus, the majority of FCIP implementations
today use switch-specifi c features such as IVR (Inter-VSAN Routing) or FCRS
131
cc0066..iinndddd 113311 44//1199//22001122 1122::0099::1133 PPMM

132 Section II n Storage Networking Technologies
(Fibre Channel Routing Services) to create a tunnel. In this manner, traffi c may
be routed between specifi c nodes without actually merging the fabrics.
This chapter describes both iSCSI and FCIP protocols, components, and topolo-
gies in detail. This chapter also covers an emerging protocol, Fibre Channel over
Ethernet (FCoE). FCoE converges Ethernet and FC traffi c over a single physical
link. Therefore, it eliminates the complexity of managing two separate networks
in the data center.
6.1 iSCSI
iSCSI is an IP based protocol that establishes and manages connections between
host and storage over IP, as shown in Figure 6-1. iSCSI encapsulates SCSI commands
and data into an IP packet and transports them using TCP/IP. iSCSI is widely
adopted for connecting servers to storage because it is relatively inexpensive and
easy to implement, especially in environments in which an FC SAN does not exist.
Storage Array
iSCSI Gateway
FC Port
IP
Server
iSCSI HBA
iSCSI Port
Storage Array
Figure 6-1: iSCSI implementation
6.1.1 Components of iSCSI
An initiator (host), target (storage or iSCSI gateway), and an IP-based network
are the key iSCSI components. If an iSCSI-capable storage array is deployed, then
a host with the iSCSI initiator can directly communicate with the storage array
over an IP network. However, in an implementation that uses an existing FC
array for iSCSI communication, an iSCSI gateway is used. These devices perform
cc0066..iinndddd 113322 44//1199//22001122 1122::0099::1133 PPMM

Chapter 6 n IP SAN and FCoE 133
the translation of IP packets to FC frames and vice versa, thereby bridging the
connectivity between the IP and FC environments.
6.1.2 iSCSI Host Connectivity
A standard NIC with software iSCSI initiator, a TCP offl oad engine (TOE)
NIC with software iSCSI initiator, and an iSCSI HBA are the three iSCSI host
connectivity options. The function of the iSCSI initiator is to route the SCSI
commands over an IP network.
A standard NIC with a software iSCSI initiator is the simplest and least expensive
connectivity option. It is easy to implement because most servers come with at least
one, and in many cases two, embedded NICs. It requires only a software initiator
for iSCSI functionality. Because NICs provide standard IP function, encapsulation
of SCSI into IP packets and decapsulation are carried out by the host CPU. This
places additional overhead on the host CPU. If a standard NIC is used in heavy I/O
load situations, the host CPU might become a bottleneck. TOE NIC helps allevi-
ate this burden. A TOE NIC offl oads TCP management functions from the host
and leaves only the iSCSI functionality to the host processor. The host passes the
iSCSI information to the TOE card, and the TOE card sends the information to the
destination using TCP/IP. Although this solution improves performance, the iSCSI
functionality is still handled by a software initiator that requires host CPU cycles.
An iSCSI HBA is capable of providing performance benefi ts because it offl oads
the entire iSCSI and TCP/IP processing from the host processor. The use of an
iSCSI HBA is also the simplest way to boot hosts from a SAN environment via
iSCSI. If there is no iSCSI HBA, modifi cations must be made to the basic oper-
ating system to boot a host from the storage devices because the NIC needs to
obtain an IP address before the operating system loads. The functionality of an
iSCSI HBA is similar to the functionality of an FC HBA.
6.1.3 iSCSI Topologies
Two topologies of iSCSI implementations are native and bridged. Native topology
does not have FC components. The initiators may be either directly attached
to targets or connected through the IP network. Bridged topology enables the
coexistence of FC with IP by providing iSCSI-to-FC bridging functionality. For
example, the initiators can exist in an IP environment while the storage remains
in an FC environment.
Native iSCSI Connectivity
FC components are not required for iSCSI connectivity if an iSCSI-enabled
array is deployed. In Figure 6-2 (a), the array has one or more iSCSI ports
confi gured with an IP address and is connected to a standard Ethernet switch.
cc0066..iinndddd 113333 44//1199//22001122 1122::0099::1144 PPMM

134 Section II n Storage Networking Technologies
After an initiator is logged on to the network, it can access the available
LUNs on the storage array. A single array port can service multiple hosts or
initiators as long as the array port can handle the amount of storage traffi c
that the hosts generate.
Storage Array
IP
Server
iSCSI HBA iSCSI Port
(a) Native iSCSI Connectivity
iSCSI Gateway Storage Array
IP
Servers
iSCSI HBA FC SAN
FC Port
FC HBA
(b) Bridged iSCSI Connectivity
iSCSI Port
Storage Array
IP
Servers
iSCSI HBA
FC SAN
FC Port
FC HBA
(c) Combining FC and Native iSCSI Connectivity
Figure 6-2: iSCSI Topologies
cc0066..iinndddd 113344 44//1199//22001122 1122::0099::1144 PPMM

Chapter 6 n IP SAN and FCoE 135
Bridged iSCSI Connectivity
A bridged iSCSI implementation includes FC components in its confi guration.
Figure 6-2 (b) illustrates iSCSI host connectivity to an FC storage array.
In this case, the array does not have any iSCSI ports. Therefore, an external
device, called a gateway or a multiprotocol router, must be used to facilitate
the communication between the iSCSI host and FC storage. The gateway con-
verts IP packets to FC frames and vice versa. The bridge devices contain both
FC and Ethernet ports to facilitate the communication between the FC and
IP environments.
In a bridged iSCSI implementation, the iSCSI initiator is confi gured with the
gateway’s IP address as its target destination. On the other side, the gateway is
confi gured as an FC initiator to the storage array.
Combining FC and Native iSCSI Connectivity
The most common topology is a combination of FC and native iSCSI. Typically,
a storage array comes with both FC and iSCSI ports that enable iSCSI and FC
connectivity in the same environment, as shown in Figure 6-2 (c).
6.1.4 iSCSI Protocol Stack
Figure 6-3 displays a model of the iSCSI protocol layers and depicts the
encapsulation order of the SCSI commands for their delivery through a physi-
cal carrier.
SCSI is the command protocol that works at the application layer of
the Open System Interconnection (OSI) model. The initiators and tar-
gets use SCSI commands and responses to talk to each other. The SCSI
command descriptor blocks, data, and status messages are encapsulated
into TCP/IP and transmitted across the network between the initiators and
targets.
iSCSI is the session-layer protocol that initiates a reliable session between
devices that recognize SCSI commands and TCP/IP. The iSCSI session-layer
interface is responsible for handling login, authentication, target discovery, and
session management. TCP is used with iSCSI at the transport layer to provide
reliable transmission.
TCP controls message fl ow, windowing, error recovery, and retransmission.
It relies upon the network layer of the OSI model to provide global addressing
and connectivity. The Layer 2 protocols at the data link layer of this model
enable node-to-node communication through a physical network.
cc0066..iinndddd 113355 44//1199//22001122 1122::0099::1144 PPMM

136  Section II n Storage Networking Technologies
| OSI Model           | iSCSI Initiator |                      |     | iSCSI Target |
| ------------------- | --------------- | -------------------- | --- | ------------ |
| Layer 7 Application | SCSI            | Commands and Data    |     | SCSI         |
| Layer 5 Session     | iSCSI           | Login and Discovery  |     | iSCSI        |
| Layer 4 Transport   | TCP             | Windows and Segments |     | TCP          |
| Layer 3 Network     | IP              | Packets              |     | IP           |
| Layer 2 Data Link   | Ethernet        | Frames               |     | Ethernet     |
Interconnect
| Ethernet | IP TCP | iSCSI | SCSI | Data |
| -------- | ------ | ----- | ---- | ---- |
Figure 6-3: iSCSI protocol stack
6.1.5 iSCSI PDU
A protocol data unit (PDU) is the basic “information unit” in the iSCSI environ-
ment. The iSCSI initiators and targets communicate with each other using iSCSI
PDUs. This communication includes establishing iSCSI connections and iSCSI
sessions, performing iSCSI discovery, sending SCSI commands and data, and
receiving SCSI status. All iSCSI PDUs contain one or more header segments
followed by zero or more data segments. The PDU is then encapsulated into an
IP packet to facilitate the transport.
A PDU includes the components shown in Figure 6-4. The IP header provides
packet-routing information to move the packet across a network. The TCP
header contains the information required to guarantee the packet delivery to
the target. The iSCSI header (basic header segment) describes how to extract
SCSI commands and data for the target. iSCSI adds an optional CRC, known
as the digest, to ensure datagram integrity. This is in addition to TCP checksum
and Ethernet CRC. The header and the data digests are optionally used in the
PDU to validate integrity and data placement.
As shown in Figure 6-5, each iSCSI PDU does not correspond in a 1:1 rela-
tionship with an IP packet. Depending on its size, an iSCSI PDU can span an
IP packet or even coexist with another PDU in the same packet.
cc0066..iinndddd      113366 44//1199//22001122      1122::0099::1144  PPMM

|     |                  |     | Chapter 6 n IP SAN and FCoE  |     |        | 137 |
| --- | ---------------- | --- | ---------------------------- | --- | ------ | --- |
|     | Basic Additional |     |                              |     | Header |     |
Header
| IP Header TCP Header | Header Header |     |     | Data | Data |     |
| -------------------- | ------------- | --- | --- | ---- | ---- | --- |
Digest
|     | Segment Segment |     |     |     | Digest |     |
| --- | --------------- | --- | --- | --- | ------ | --- |
iSCSI PDU
TCP Segment
IP Packet
Figure 6-4: iSCSI PDU encapsulated in an IP packet
A message transmitted on a network is divided into
a number of packets. If necessary, each packet can be
sent by a different route across the network. Packets can
arrive in a different order than the order in which they
were sent. IP only delivers them; it is up to TCP to organize
them in the right sequence. The target extracts the SCSI commands and data
on the basis of the information in the iSCSI header.
SCSI Command and Data
| iSCSI PDU     | iSCSI PDU     |        | iSCSI PDU | iSCSI PDU |        |     |
| ------------- | ------------- | ------ | --------- | --------- | ------ | --- |
| Header Data   | Header Data   | Header | Data      | Header    | Data   |     |
| IP  IP        | IP  IP        |        | IP        | IP  IP    | IP     |     |
| Packet Packet | Packet Packet | Packet | Packet    | Packet    | Packet |     |
Varying iSCSI PDU alignment
with IP packets
Figure 6-5: Alignment of iSCSI PDUs with IP packets
To achieve the 1:1 relationship between the IP packet and the iSCSI PDU,
the maximum transmission unit (MTU) size of the IP packet is modifi ed.
This eliminates fragmentation of the IP packet, which improves the trans-
mission effi ciency.
cc0066..iinndddd      113377 44//1199//22001122      1122::0099::1155  PPMM

138 Section II n Storage Networking Technologies
6.1.6 iSCSI Discovery
An initiator must discover the location of its targets on the network and the
names of the targets available to it before it can establish a session. This discov-
ery can take place in two ways: SendTargetsdiscovery or internetStorageName
Service (iSNS).
In SendTargets discovery, the initiator is manually confi gured with the tar-
get’s network portal to establish a discovery session. The initiator issues the
SendTargets command, and the target network portal responds with the names
and addresses of the targets available to the host.
iSNS (see Figure 6-6) enables automatic discovery of iSCSI devices on an
IP network. The initiators and targets can be confi gured to automatically
register themselves with the iSNS server. Whenever an initiator wants to
know the targets that it can access, it can query the iSNS server for a list of
available targets.
The discovery can also take place by using service location protocol
(SLP). However, this is less commonly used than SendTargets discovery
and iSNS.
6.1.7 iSCSI Names
A unique worldwide iSCSI identifi er, known as an iSCSI name, is used to identify
the initiators and targets within an iSCSI network to facilitate communication.
The unique identifi er can be a combination of the names of the department,
application, or manufacturer, serial number, asset number, or any tag that can
be used to recognize and manage the devices. Following are two types of iSCSI
names commonly used:
n iSCSI Qualifi ed Name (IQN): An organization must own a registered
domain name to generate iSCSI Qualifi ed Names. This domain name does
not need to be active or resolve to an address. It just needs to be reserved
to prevent other organizations from using the same domain name to
generate iSCSI names. A date is included in the name to avoid potential
confl icts caused by the transfer of domain names. An example of an IQN
isiqn.2008-02.com.example:optional_string.
Theoptional_string provides a serial number, an asset number, or any other
device identifi ers. An iSCSI Qualifi ed Name enables storage administra-
tors to assign meaningful names to iSCSI devices, and therefore, manage
those devices more easily.
cc0066..iinndddd 113388 44//1199//22001122 1122::0099::1155 PPMM

Chapter 6 n IP SAN and FCoE 139
n Extended Unique Identifi er (EUI): An EUI is a globally unique identi-
fi er based on the IEEE EUI-64 naming standard. An EUI is composed
of the eui prefi x followed by a 16-character hexadecimal name, such as
eui.0300732A32598D26.
In either format, the allowed special characters are dots, dashes, and
blank spaces.
Application iSCSI Initiator
Server
IP
iSNS Server iSCSI Target
APP APP
OS OS Storage Array
VM VM
Hypervisor
Application
iSCSI Initiator
Server
Figure 6-6: Discovery using iSNS
cc0066..iinndddd 113399 44//1199//22001122 1122::0099::1155 PPMM

140 Section II n Storage Networking Technologies
NETWORK ADDRESS AUTHORITY
Network Address Authority (NAA) is an additional iSCSI node
name type to enable a worldwide naming format as defi ned
by the InterNational Committee for Information Technology
Standards (INCITS) T11. This format enables the SCSI stor-
age devices that contain both iSCSI ports and SAS ports to
use the same NAA-based SCSI device name. This format is
defi ned by RFC 3980, “T11 Network Address Authority (NAA) Naming Format
for iSCSI Node Names.”
6.1.8 iSCSI Session
An iSCSI session is established between an initiator and a target, as shown in
Figure 6-7. A session is identifi ed by a session ID (SSID), which includes part of an
initiator ID and a target ID. The session can be intended for one of the following:
n The discovery of the available targets by the initiators and the location of
a specifi c target on a network
n The normal operation of iSCSI (transferring data between initiators and targets)
There might be one or more TCP connections within each session. Each TCP
connection within the session has a unique connection ID (CID).
iSCSI Session
iSCSI Host iSCSI Device
TCP Connection
iSCSI Target
iSCSI TCP Connection
Initiator
TCP Connection
iSCSI Target
iSCSI Session
Figure 6-7: iSCSI session
An iSCSI session is established via the iSCSI login process. The login process
is started when the initiator establishes a TCP connection with the required
target either via the well-known port 3260 or a specifi ed target port. During the
login phase, the initiator and the target authenticate each other and negotiate
on various parameters.
cc0066..iinndddd 114400 44//1199//22001122 1122::0099::1166 PPMM

Chapter 6 n IP SAN and FCoE 141
After the login phase is successfully completed, the iSCSI session enters the
full-feature phase for normal SCSI transactions. In this phase, the initiator may
send SCSI commands and data to the various LUNs on the target by encap-
sulating them in iSCSI PDUs that travel over the established TCP connection.
The fi nal phase of the iSCSI session is the connection termination phase,
which is referred to as the logout procedure. The initiator is responsible for
commencing the logout procedure; however, the target may also prompt ter-
mination by sending an iSCSI message, indicating the occurrence of an internal
error condition. After the logout request is sent from the initiator and accepted
by the target, no further request and response can be sent on that connection.
6.1.9 iSCSI Command Sequencing
The iSCSI communication between the initiators and targets is based on the
request-response command sequences. A command sequence may generate
multiple PDUs. A command sequence number (CmdSN) within an iSCSI session
is used for numbering all initiator-to-target command PDUs belonging to the
session. This number ensures that every command is delivered in the same
order in which it is transmitted, regardless of the TCP connection that carries
the command in the session.
Command sequencing begins with the fi rst login command, and the CmdSN
is incremented by one for each subsequent command. The iSCSI target layer is
responsible for delivering the commands to the SCSI layer in the order of their
CmdSN. This ensures the correct order of data and commands at a target even
when there are multiple TCP connections between an initiator and the target
that use portal groups.
Similar to command numbering, a status sequence number (StatSN) is used to
sequentially number status responses, as shown in Figure 6-8. These unique
numbers are established at the level of the TCP connection.
CmdSN1 CmdSN2
StatSN1 StatSN1 StatSN2
PDU#1 PDU#1 PDU#1
PDU#2 PDU#2
PDU#3 PDU#3
PDU#4
Figure 6-8: Command and status sequence number
cc0066..iinndddd 114411 44//1199//22001122 1122::0099::1166 PPMM

142 Section II n Storage Networking Technologies
A target sends request-to-transfer (R2T) PDUs to the initiator when it is ready
to accept data. A data sequence number (DataSN) is used to ensure in-order deliv-
ery of data within the same command. The DataSN and R2TSN are used to
sequence data PDUs and R2Ts, respectively. Each of these sequence numbers
is stored locally as an unsigned 32-bit integer counter defi ned by iSCSI. These
numbers are communicated between the initiator and target in the appropriate
iSCSI PDU fi elds during command, status, and data exchanges.
For read operations, the DataSN begins at zero and is incremented by one for
each subsequent data PDU in that command sequence. For a write operation,
the fi rst unsolicited data PDU or the fi rst data PDU in response to an R2T begins
with a DataSN of zero and increments by one for each subsequent data PDU.
R2TSN is set to zero at the initiation of the command and incremented by one
for each subsequent R2T sent by the target for that command.
6.2 FCIP
FC SAN provides a high-performance infrastructure for localized data movement.
Organizations are now looking for ways to transport data over a long distance
between their disparate SANs at multiple geographic locations. One of the best
ways to achieve this goal is to interconnect geographically dispersed SANs through
reliable, high-speed links. This approach involves transporting the FC block data
over the IP infrastructure. FCIP is a tunneling protocol that enables distributed
FC SAN islands to be interconnected over the existing IP-based networks.
The FCIP standard has rapidly gained acceptance as a manageable, cost-
effective way to blend the best of the two worlds: FC SAN and the proven,
widely deployed IP infrastructure. As a result, organizations now have a
better way to store, protect and move their data by leveraging investments
in their existing IP infrastructure. FCIP is extensively used in disaster recov-
ery implementations in which data is duplicated to the storage located at a
remote site.
FCIP might require high network bandwidth when replicat-
ing or backing up data. FCIP does not handle data traffi c
throttling or fl ow control; these are controlled by the com-
municating FC switches and devices within the fabric.
6.2.1 FCIP Protocol Stack
The FCIP protocol stack is shown in Figure: 6-9. Applications generate SCSI
commands and data, which are processed by various layers of the protocol stack.
cc0066..iinndddd 114422 44//1199//22001122 1122::0099::1166 PPMM

Chapter 6 n IP SAN and FCoE 143
Application
SCSI Commands, Data, and Status FC Frame
FCP (SCSI over FC)
FCIP
TCP FC to IP Encapsulation
IP
Physical Media
Figure 6-9: FCIP protocol stack
The upper layer protocol SCSI includes the SCSI driver program that executes
the read-and-write commands. Below the SCSI layer is the Fibre Channel Protocol
(FCP) layer, which is simply a Fibre Channel frame whose payload is SCSI. The
FCP layer rides on top of the Fibre Channel transport layer. This enables the
FC frames to run natively within a SAN fabric environment. In addition, the
FC frames can be encapsulated into the IP packet and sent to a remote SAN
over the IP. The FCIP layer encapsulates the Fibre Channel frames onto the IP
payload and passes them to the TCP layer (see Figure 6-10). TCP and IP are
used for transporting the encapsulated information across Ethernet, wireless,
or other media that support the TCP/IP traffi c.
FC
FC Frame SOF SCSI Data CRC EOF
Header
FCIP Encapsulation
IP TCP FCIP
IP Packet IP Payload
Header Header Header
Figure 6-10: FCIP encapsulation
Encapsulation of FC frame into an IP packet could cause the IP packet to be
fragmented when the data link cannot support the maximum transmission unit
cc0066..iinndddd 114433 44//1199//22001122 1122::0099::1166 PPMM

144 Section II n Storage Networking Technologies
(MTU) size of an IP packet. When an IP packet is fragmented, the required parts
of the header must be copied by all fragments. When a TCP packet is segmented,
normal TCP operations are responsible for receiving and re-sequencing the data
prior to passing it on to the FC processing portion of the device.
6.2.2 FCIP Topology
In an FCIP environment, an FCIP gateway is connected to each fabric via a standard
FC connection (see Figure 6-11). The FCIP gateway at one end of the IP network
encapsulates the FC frames into IP packets. The gateway at the other end removes
the IP wrapper and sends the FC data to the layer 2 fabric. The fabric treats these
gateways as layer 2 fabric switches. An IP address is assigned to the port on the
gateway, which is connected to an IP network. After the IP connectivity is estab-
lished, the nodes in the two independent fabrics can communicate with each other.
Servers Servers
APP APP APP APP
OS OS OS OS
VM VM VM VM
Hypervisor Hypervisor
Server Server
FCIP Gateway FCIP Gateway
FC SAN FC SAN
IP
Storage Array Storage Array
Figure 6-11: FCIP topology
6.2.3 FCIP Performance and Security
Performance, reliability, and security should always be taken into consideration
when implementing storage solutions. The implementation of FCIP is also subject
to the same considerations.
cc0066..iinndddd 114444 44//1199//22001122 1122::0099::1177 PPMM

Chapter 6 n IP SAN and FCoE 145
From the perspective of performance, confi guring multiple paths between FCIP
gateways eliminates single points of failure and provides increased bandwidth.
In a scenario of extended distance, the IP network might be a bottleneck if
suffi cient bandwidth is not available. In addition, because FCIP creates a unifi ed
fabric, disruption in the underlying IP network can cause instabilities in the
SAN environment. These instabilities include a segmented fabric, excessive
RSCNs, and host timeouts.
The vendors of FC switches have recognized some of the drawbacks related to
FCIP and have implemented features to enhance stability, such as the capability
to segregate the FCIP traffi c into a separate virtual fabric.
Security is also a consideration in an FCIP solution because the data is trans-
mitted over public IP channels. Various security options are available to protect
the data based on the router’s support. IPSec is one such security measure that
can be implemented in the FCIP environment.
6.3 FCoE
Data centers typically have multiple networks to handle various types of I/O
traffi c — for example, an Ethernet network for TCP/IP communication and an
FC network for FC communication. TCP/IP is typically used for client-server
communication, data backup, infrastructure management communication, and
so on. FC is typically used for moving block-level data between storage and
servers. To support multiple networks, servers in a data center are equipped
with multiple redundant physical network interfaces — for example, multiple
Ethernet and FC cards/adapters. In addition, to enable the communication,
different types of networking switches and physical cabling infrastructure
are implemented in data centers. The need for two different kinds of physi-
cal network infrastructure increases the overall cost and complexity of data
center operation.
Fibre Channel over Ethernet (FCoE) protocol provides consolidation of LAN
and SAN traffi c over a single physical interface infrastructure. FCoE helps
organizations address the challenges of having multiple discrete network infra-
structures. FCoE uses the Converged Enhanced Ethernet (CEE) link (10 Gigabit
Ethernet) to send FC frames over Ethernet.
6.3.1 I/O Consolidation Using FCoE
The key benefi t of FCoE is I/O consolidation. Figure 6-12 represents the infra-
structure before FCoE deployment. Here, the storage resources are accessed
using HBAs, and the IP network resources are accessed using NICs by the
servers. Typically, in a data center, a server is confi gured with 2 to 4 NIC cards
and redundant HBA cards. If the data center has hundreds of servers, it would
cc0066..iinndddd 114455 44//1199//22001122 1122::0099::1177 PPMM

146  Section II n Storage Networking Technologies
require a large number of adapters, cables, and switches. This leads to a complex
environment, which is diffi cult to manage and scale. The cost of power, cooling,
and fl oor space further adds to the challenge.
|        | Servers    |        | Servers    |
| ------ | ---------- | ------ | ---------- |
|        | APP APP    |        | APP APP    |
|        | OS OS      |        | OS OS      |
|        | VM VM      |        | VM VM      |
| Server | Hypervisor | Server | Hypervisor |
IP
FC Switches
Switches
FC
Switches
LAN
| Storage Array | Storage Array |     |     |
| ------------- | ------------- | --- | --- |
Figure 6-12: Infrastructure before using FCoE
Figure 6-13 shows the I/O consolidation with FCoE using FCoE switches
and Converged Network Adapters (CNAs). A CNA (discussed in the section
“Converged Network Adapter”) replaces both HBAs and NICs in the server and
consolidates both the IP and FC traffi c. This reduces the requirement of multiple
network adapters at the server to connect to different networks. Overall, this
reduces the requirement of adapters, cables, and switches. This also consider-
ably reduces the cost and management overhead.
cc0066..iinndddd      114466 44//1199//22001122      1122::0099::1177  PPMM

Chapter 6 n IP SAN and FCoE 147
Servers Servers
APP APP APP APP
OS OS OS OS
VM VM VM VM
Hypervisor Hypervisor
Server Server
FCoE
Switches
FC
Switches
LAN
Storage Array Storage Array
Figure 6-13: Infrastructure after using FCoE
6.3.2 Components of an FCoE Network
This section describes the key physical components required to implement FCoE
in a data center. The key FCoE components are:
n Converged Network Adapter (CNA)
n Cables
n FCoE switches
cc0066..iinndddd 114477 44//1199//22001122 1122::0099::1188 PPMM

148 Section II n Storage Networking Technologies
Converged Network Adapter
A CNA provides the functionality of both a standard NIC and an FC HBA in a
single adapter and consolidates both types of traffi c. CNA eliminates the need
to deploy separate adapters and cables for FC and Ethernet communications,
thereby reducing the required number of server slots and switch ports. CNA
offl oads the FCoE protocol processing task from the server, thereby freeing the
server CPU resources for application processing. As shown in Figure 6-14, a CNA
contains separate modules for 10 Gigabit Ethernet, Fibre Channel, and FCoE
Application Specifi c Integrated Circuits (ASICs). The FCoE ASIC encapsulates
FC frames into Ethernet frames. One end of this ASIC is connected to 10GbE
and FC ASICs for server connectivity, while the other end provides a 10GbE
interface to connect to an FCoE switch.
10GbE
FCoE
ASIC
10GbE FC
ASIC ASIC
PCIe Bus
Figure 6-14: Converged Network Adapter
Cables
Currently two options are available for FCoE cabling: Copper based Twinax and
standard fi ber optical cables. A Twinax cable is composed of two pairs of copper
cables covered with a shielded casing. The Twinax cable can transmit data at the
speed of 10 Gbps over shorter distances up to 10 meters. Twinax cables require
less power and are less expensive than fi ber optic cables. The Small Form Factor
Pluggable Plus (SFP+) connector is the primary connector used for FCoE links
and can be used with both optical and copper cables.
cc0066..iinndddd 114488 44//1199//22001122 1122::0099::1188 PPMM

Chapter 6 n IP SAN and FCoE 149
A typical strategy for FCoE deployment is the top of
rack implementation. Here, a pair of redundant FCoE
switches is installed at the top of each rack of servers.
Both FC and IP connectivity to each server is accom-
plished using inexpensive Twinax cabling from the server
to the top of rack FCoE switches. This short distance is well supported with
Twinax. Connectivity from the top of rack switches to existing backbone
LAN and SAN infrastructures, that is connections across racks, is typically
done with optical links, which can support the longer cable runs that may
be required.
FCoE Switches
An FCoE switch has both Ethernet switch and Fibre Channel switch function-
alities. The FCoE switch has a Fibre Channel Forwarder (FCF), Ethernet Bridge,
and set of Ethernet ports and optional FC ports, as shown in Figure 6-15. The
function of the FCF is to encapsulate the FC frames, received from the FC port,
into the FCoE frames and also to de-encapsulate the FCoE frames, received from
the Ethernet Bridge, to the FC frames.
FC Port FC Port FC Port FC Port
Fibre Channel Forwarder
Ethernet Bridge
Ethernet Ethernet Ethernet Ethernet
Port Port Port Port
Figure 6-15: FCoE switch generic architecture
cc0066..iinndddd 114499 44//1199//22001122 1122::0099::1199 PPMM

150 Section II n Storage Networking Technologies
Upon receiving the incoming traffi c, the FCoE switch inspects the Ethertype
(used to indicate which protocol is encapsulated in the payload of an Ethernet
frame) of the incoming frames and uses that to determine the destination. If the
Ethertype of the frame is FCoE, the switch recognizes that the frame contains
an FC payload and forwards it to the FCF. From there, the FC is extracted from
the FCoE frame and transmitted to FC SAN over the FC ports. If the Ethertype
is not FCoE, the switch handles the traffi c as usual Ethernet traffi c and forwards
it over the Ethernet ports.
6.3.3 FCoE Frame Structure
An FCoE frame is an Ethernet frame that contains an FCoE Protocol Data Unit.
Figure 6-16 shows the FCoE frame structure. The fi rst 48-bits in the frame are
used to specify the destination MAC address, and the next 48-bits specify the
source MAC address. The 32-bit IEEE 802.1Q tag supports the creation of multiple
virtual networks (VLANs) across a single physical infrastructure. FCoE has its
own Ethertype, as designated by the next 16 bits, followed by the 4-bit version
fi eld. The next 100-bits are reserved and are followed by the 8-bit Start of Frame
and then the actual FC frame. The 8-bit End of Frame delimiter is followed by 24
reserved bits. The frame ends with the fi nal 32-bits dedicated to the Frame Check
Sequence (FCS) function that provides error detection for the Ethernet frame.
Destination MAC Address
Source MAC Address
(IEEE 802.1Q Tag)
Ether Type = FCoE Ver Reserved
Reserved
Reserved
Reserved SOF
Encapsulated FC Frame
(including FC-CRC)
EOF Reserved
Ethernet FCS
Figure 6-16: FCoE frame structure
cc0066..iinndddd 115500 44//1199//22001122 1122::0099::1199 PPMM

|     |     |     | Chapter 6 n IP SAN and FCoE  |     | 151 |
| --- | --- | --- | ---------------------------- | --- | --- |
The encapsulated Fibre Channel frame consists of the original 24-byte FC
header and the data being transported (including the Fibre Channel CRC).
The FC frame structure is maintained such that when a traditional FC SAN is
connected to an FCoE capable switch, the FC frame is de-encapsulated from
the FCoE frame and transported to FC SAN seamlessly. This capability enables
FCoE to integrate with the existing FC SANs without the need for a gateway.
Frame size is also an important factor in FCoE. A typical Fibre Channel
data frame has a 2,112-byte payload, a 24-byte header, and an FCS. A standard
Ethernet frame has a default payload capacity of 1,500 bytes. To maintain good
performance, FCoE must use jumbo frames to prevent a Fibre Channel frame
from being split into two Ethernet frames. The next chapter discusses jumbo
frames in detail. FCoE requires Converged Enhanced Ethernet, which provides
lossless Ethernet and jumbo frame support.
FCoE Frame Mapping
The encapsulation of the Fibre Channel frame occurs through the mapping of the
FC frames onto Ethernet, as shown in Figure 6-17. Fibre Channel and traditional
networks have stacks of layers where each layer in the stack represents a set of
functionalities. The FC stack consists of fi ve layers: FC-0 through FC-4. Ethernet
is typically considered as a set of protocols that operates at the physical and
data link layers in the seven layer OSI stack. The FCoE protocol specifi cation
replaces the FC-0 and FC-1 layers of the FC stack with Ethernet. This provides
the capability to carry the FC-2 to the FC-4 layer over the Ethernet layer.
OSI Stack
7 - Application
|                  |           | FCoE Protocol Stack |     | FC Protocol Stack   |     |
| ---------------- | --------- | ------------------- | --- | ------------------- | --- |
| 6 - Presentation |           | FC - 4              |     | FC - 4 Protocol map |     |
| 5 - Session      | FC Layers | FC - 3              |     | FC - 3 Services     |     |
| 4 - Transport    |           | FC - 2              |     | FC - 2 Framing      |     |
| 3 - Network      |           | FCoE Mapping        |     | FC - 1 Data enc/dec |     |
| 2 - Data Link    |           | 2 - MAC             |     | FC - 0 Physical     |     |
IEEE 802.1q
Layers
| 1 - Physical |     | 1 - Physical |     |     |     |
| ------------ | --- | ------------ | --- | --- | --- |
Ethernet
Figure 6-17: FCoE frame mapping
cc0066..iinndddd      115511 44//1199//22001122      1122::0099::1199  PPMM

152 Section II n Storage Networking Technologies
FCoE PORTS
To transport FC frames, the FCoE ports need to emulate the
behavior of FC ports and become virtual FC ports. FCoE uses
similar terminology as FC to defi ne various ports in the net-
work. FCoE has the following ports (See the fi gure following
this list):
n VN_Port (Virtual N_Port): Port in an Enhanced Ethernet node (or Enode).
Enodes are end points, such as a server, with CNA.
n VF_Port (Virtual F_Port): Virtual Fabric Port in an FCoE Switch
n VE_Port (Virtual E_Port): Virtual Extension Port in an FCoE Switch for ISLs
Enode
FCoE Node Port FCoE Switch Port
VN_Port FCoE LEP FCoE LEP VF_Port
VN_Port FCoE LEP FCoE LEP VF_Port
Lossless
Ethernet
Enode Network
FCoE Node Port FCoE Switch Port
VN_Port FCoE LEP FCoE LEP VF_Port
VN_Port FCoE LEP FCoE LEP VF_Port
FCoE Link End Points (LEP) are located between the MAC and the virtual
ports. LEPs are responsible for FC frame encapsulation/de-capsulation and for
transmitting and receiving the encapsulated frames through a virtual port.
6.3.4 FCoE Enabling Technologies
Conventional Ethernet is lossy in nature, which means that frames might be
dropped or lost during transmission. Converged Enhanced Ethernet (CEE), or
lossless Ethernet, provides a new specifi cation to the existing Ethernet standard
that eliminates the lossy nature of Ethernet. This makes 10 Gb Ethernet a viable
storage networking option, similar to FC. Lossless Ethernet requires certain
functionalities. These functionalities are defi ned and maintained by the data
center bridging (DCB) task group, which is a part of the IEEE 802.1 working
group, and they are:
n Priority-based fl ow control
n Enhanced transmission selection
cc0066..iinndddd 115522 44//1199//22001122 1122::0099::1199 PPMM

Chapter 6 n IP SAN and FCoE 153
n Congestion Notifi cation
n Data center bridging exchange protocol
Priority-Based Flow Control (PFC)
Traditional FC manages congestion through the use of a link-level, credit-based
fl ow control that guarantees no loss of frames. Typical Ethernet, coupled with
TCP/IP, uses a packet drop fl ow control mechanism. The packet drop fl ow control
is not lossless. This challenge is eliminated by using an IEEE 802.3x Ethernet
PAUSE control frame to create a lossless Ethernet. A receiver can send a PAUSE
request to a sender when the receiver’s buffer is fi lling up. Upon receiving a
PAUSE frame, the sender stops transmitting frames, which guarantees no loss
of frames. The downside of using the Ethernet PAUSE frame is that it operates
on the entire link, which might be carrying multiple traffi c fl ows.
PFC provides a link level fl ow control mechanism. PFC creates eight separate
virtual links on a single physical link and allows any of these links to be paused
and restarted independently. PFC enables the pause mechanism based on user
priorities or classes of service. Enabling the pause based on priority allows cre-
ating lossless links for traffi c, such as FCoE traffi c. This PAUSE mechanism is
typically implemented for FCoE while regular TCP/IP traffi c continues to drop
frames. Figure 6-18 illustrates how a physical Ethernet link is divided into eight
virtual links and allows a PAUSE for a single virtual link without affecting the
traffi c for the others.
Transmit Queues Receive Buffers
Ethernet Link
One One
Two Two
Three STOP PAUSE Three
Four Four
Eight
Virtual Lanes
Five Five
Six Six
Seven Seven
Eight Eight
Figure 6-18: Priority-based flow control
cc0066..iinndddd 115533 44//1199//22001122 1122::0099::2200 PPMM

154 Section II n Storage Networking Technologies
Enhanced Transmission Selection (ETS)
Enhanced transmission selection provides a common management framework
for the assignment of bandwidth to different traffi c classes, such as LAN, SAN,
and Inter Process Communication (IPC). When a particular class of traffi c does
not use its allocated bandwidth, ETS enables other traffi c classes to use the
available bandwidth.
Congestion Notifi cation (CN)
Congestion notifi cation provides end-to-end congestion management for
protocols, such as FCoE, that do not have built-in congestion control mecha-
nisms. Link level congestion notifi cation provides a mechanism for detecting
congestion and notifying the source to move the traffi c fl ow away from the
congested links. Link level congestion notifi cation enables a switch to send
a signal to other ports that need to stop or slow down their transmissions.
The process of congestion notifi cation and its management is shown in Figure
6-19, which represents the communication between the nodes A (sender) and
B (receiver). If congestion at the receiving end occurs, the algorithm running
on the switch generates a congestion notifi cation message to the sending
node (Node A). In response to the CN message, the sending end limits the
rate of data transfer.
Rate limiting to avoid
packet loss
FCoE
Switch
FCoE
Switch
FCoE
Switch
Host
(Node A)
Congestion
Notification Message
Congestion
Storage Array
(Node B)
Fi gure 6-19: Congestion Notification
Data Center Bridging Exchange Protocol (DCBX)
DCBX protocol is a discovery and capability exchange protocol, which helps
Converged Enhanced Ethernet devices to convey and confi gure their features
with the other CEE devices in the network. DCBX is used to negotiate capabilities
cc0066..iinndddd 115544 44//1199//22001122 1122::0099::2200 PPMM

Chapter 6 n IP SAN and FCoE 155
between the switches and the adapters, and it allows the switch to distribute the
confi guration values to all the attached adapters. This helps to ensure consistent
confi guration across the entire network.
Summary
IP SAN has enabled IT organizations to adopt storage networking infrastructure
at reasonable costs. Storage networks can now be geographically distributed with
the help of the IP SAN technology, which enhances storage utilization across
enterprises. FCIP has emerged as a solution for implementing viable business
continuity across data centers.
Because IP SANs are based on standard IP protocols, the concepts, security
mechanisms, and management tools are familiar to network administrators.
This has enabled the rapid adoption of IP SAN in organizations. This chapter
detailed the two IP SAN technologies: iSCSI and FCIP. This chapter also detailed
the emerging FCoE technology that enables transportation of both the LAN and
SAN traffi c on a single physical network infrastructure.
SAN offers a high-performance storage networking solution; however, SAN
does not enable sharing of data among multiple hosts. Organizations might
require sharing of data or fi les among multiple heterogeneous clients for col-
laboration purposes.
The next chapter details network-attached storage (NAS), a solution that
provides a fi le-sharing environment to heterogeneous clients. Because NAS
is dedicated for fi le sharing, it provides better performance than traditional
fi le servers.
cc0066..iinndddd 115555 44//1199//22001122 1122::0099::2200 PPMM

156 Section II n Storage Networking Technologies
EXERCISES
1. How does iSCSI handle the process of authentication? Research the
available options.
2. Compared to a standard IP packet, what percentage of reduction can be
realized in protocol overhead in an iSCSI, configured to use jumbo frames
with an MTU value of 9,000 bytes?
3. Why should an MTU value of at least 2,500 bytes be configured in
a bridged iSCSI environment?
4. Why does the lossy nature of standard Ethernet make it unsuitable for a
layered FCoE implementation? How does Converged Enhanced Ethernet
(CEE) address this problem?
5. Compare various data center protocols that use Ethernet as the physical
medium for transporting storage traffic.
cc0066..iinndddd 115566 44//1199//22001122 1122::0099::2200 PPMM

Chapter 7
Network-Attached Storage
File sharing, as the name implies, enables KEY CONCEPTS
users to share files with other users.
Traditional methods of fi le sharing involve NAS Devices
copying fi les to portable media such as fl oppy
Network File Sharing
diskette, CD, DVD, or USB drives and deliver-
ing them to other users with whom it is being Unified, Gateway, and
shared. However, this approach is not suitable Scale-Out NAS
in an enterprise environment in which a large
NAS Connectivity and Protocols
number of users at different locations need access
to common fi les. NAS Performance
Network-based fi le sharing provides the fl ex-
MTU and Jumbo Frames
ibility to share fi les over long distances among
a large number of users. File servers use client- TCP Window and Link
server technology to enable fi le sharing over a Aggregation
network. To address the tremendous growth of
File-Level Virtualization
fi le data in enterprise environments, organiza-
tions have been deploying large numbers of fi le
servers. These servers are either connected to direct-attached storage (DAS) or
storage area network (SAN)-attached storage. This has resulted in the prolifera-
tion of islands of over-utilized and under-utilized fi le servers and storage. In
157
cc0077..iinndddd 115577 44//1199//22001122 1122::0099::5577 PPMM

158 Section II n Storage Networking Technologies
addition, such environments have poor scalability, higher management cost,
and greater complexity. Network-attached storage (NAS) emerged as a solution
to these challenges.
NAS is a dedicated, high-performance fi le sharing and storage device. NAS
enables its clients to share fi les over an IP network. NAS provides the advan-
tages of server consolidation by eliminating the need for multiple fi le servers.
It also consolidates the storage used by the clients onto a single system, making
it easier to manage the storage. NAS uses network and fi le-sharing protocols to
provide access to the fi le data. These protocols include TCP/IP for data transfer,
and Common Internet File System (CIFS) and Network File System (NFS) for
network fi le service. NAS enables both UNIX and Microsoft Windows users to
share the same data seamlessly.
A NAS device uses its own operating system and integrated hardware and
software components to meet specifi c fi le-service needs. Its operating system is
optimized for fi le I/O and, therefore, performs fi le I/O better than a general-purpose
server. As a result, a NAS device can serve more clients than general-purpose
servers and provide the benefi t of server consolidation.
A network-based fi le sharing environment is composed of multiple fi le servers
or NAS devices. It might be required to move the fi les from one device to another
due to reasons such as cost or performance. File-level virtualization, implemented
in the fi le sharing environment, provides a simple, nondisruptive fi le-mobility
solution. It enables the movement of fi les across NAS devices, even if the fi les
are being accessed.
This chapter describes the components of NAS, different types of NAS
implementations, and the fi le-sharing protocols used in NAS implementations.
The chapter also explains factors that affect NAS performance, and fi le-level
virtualization.
7.1 General-Purpose Servers versus NAS Devices
A NAS device is optimized for file-serving functions such as storing,
retrieving, and accessing fi les for applications and clients. As shown in
Figure 7-1, a general-purpose server can be used to host any application
because it runs a general-purpose operating system. Unlike a general-purpose
server, a NAS device is dedicated to fi le-serving. It has specialized operat-
ing system dedicated to fi le serving by using industry-standard protocols.
Some NAS vendors support features, such as native clustering for high
availability.
cc0077..iinndddd 115588 44//1199//22001122 1122::0099::5577 PPMM

Chapter 7 n Network-Attached Storage 159
Applications File System
Print Drivers Operating System
File System Network Interface
Operating System
Network Interface
Single Purpose
NAS Device
General Purpose Servers
(Windows or UNIX)
Figure 7-1: General purpose server versus NAS device
7.2 Benefi ts of NAS
NAS offers the following benefi ts:
n Comprehensive access to information: Enables effi cient fi le sharing and
supports many-to-one and one-to-many confi gurations. The many-to-one
confi guration enables a NAS device to serve many clients simultaneously.
The one-to-many confi guration enables one client to connect with many
NAS devices simultaneously.
n Improved effi ciency: NAS delivers better performance compared to a
general-purpose fi le server because NAS uses an operating system spe-
cialized for fi le serving.
n Improved fl exibility: Compatible with clients on both UNIX and Windows
platforms using industry-standard protocols. NAS is fl exible and can serve
requests from different types of clients from the same source.
n Centralized storage: Centralizes data storage to minimize data duplication
on client workstations, and ensure greater data protection
n Simplifi ed management: Provides a centralized console that makes it
possible to manage fi le systems effi ciently
cc0077..iinndddd 115599 44//1199//22001122 1122::0099::5577 PPMM

160 Section II n Storage Networking Technologies
n Scalability: Scales well with different utilization profi les and types of
business applications because of the high-performance and low-latency
design
n High availability: Offers effi cient replication and recovery options, enabling
high data availability. NAS uses redundant components that provide
maximum connectivity options. A NAS device supports clustering tech-
nology for failover.
n Security: Ensures security, user authentication, and fi le locking with
industry-standard security schemas
n Low cost: NAS uses commonly available and inexpensive Ethernet
components.
n Ease of deployment: Confi guration at the client is minimal, because the
clients have required NAS connection software built in.
7.3 File Systems and Network File Sharing
A fi le system is a structured way to store and organize data fi les. Many fi le
systems maintain a fi le access table to simplify the process of searching and
accessing fi les.
7.3.1 Accessing a File System
A fi le system must be mounted before it can be used. In most cases, the oper-
ating system mounts a local fi le system during the boot process. The mount
process creates a link between the fi le system on the NAS and the operating
system on the client. When mounting a fi le system, the operating system
organizes fi les and directories in a tree-like structure and grants the privi-
lege to the user to access this structure. The tree is rooted at a mount point.
The mount point is named using operating system conventions. Users and
applications can traverse the entire tree from the root to the leaf nodes as fi le
system permissions allow. Files are located at leaf nodes, and directories and
subdirectories are located at intermediate roots. The access to the fi le system
terminates when the fi le system is unmounted. Figure 7-2 shows an example
of a UNIX directory structure.
7.3.2 Network File Sharing
Network fi le sharing refers to storing and accessing fi les over a network. In a
fi le-sharing environment, the user who creates a fi le (the creator or owner of
a fi le) determines the type of access (such as read, write, execute, append, and
cc0077..iinndddd 116600 44//1199//22001122 1122::0099::5577 PPMM

Chapter 7 n Network-Attached Storage 161
delete) to be given to other users and controls changes to the fi le. When multiple
users try to access a shared fi le at the same time, a locking scheme is required
to maintain data integrity and, at the same time, make this sharing possible.
/(root)
...
etc bin usr tmp dev
... ...
ls csh ucb lib
Figure 7-2: UNIX directory structure
Some examples of fi le-sharing methods are fi le transfer protocol (FTP),
Distributed File System (DFS), client-server models that use fi le-sharing protocols
such as NFS and CIFS, and the peer-to-peer (P2P) model
FTP is a client-server protocol that enables data transfer over a network. An
FTP server and an FTP client communicate with each other using TCP as the
transport protocol. FTP, as defi ned by the standard, is not a secure method of
data transfer because it uses unencrypted data transfer over a network. FTP
over Secure Shell (SSH) adds security to the original FTP specifi cation. When
FTP is used over SSH, it is referred to as Secure FTP (SFTP).
A distributed fi le system (DFS) is a fi le system that is distributed across several
hosts. A DFS can provide hosts with direct access to the entire fi le system, while
ensuring effi cient management and data security. Standard client-server fi le-
sharing protocols, such as NFS and CIFS, enable the owner of a fi le to set the
required type of access, such as read-only or read-write, for a particular user or
group of users. Using this protocol, the clients mount remote fi le systems that
are available on dedicated fi le servers.
A name service, such as Domain Name System (DNS), and directory services
such as Microsoft Active Directory, and Network Information Services (NIS),
helps users identify and access a unique resource over the network. A name
service protocol such as the Lightweight Directory Access Protocol (LDAP) creates
a namespace, which holds the unique name of every network resource and helps
recognize resources on the network.
A peer-to-peer (P2P) file sharing model uses a peer-to-peer network.
P2P enables client machines to directly share fi les with each other over a
cc0077..iinndddd 116611 44//1199//22001122 1122::0099::5577 PPMM

162 Section II n Storage Networking Technologies
network. Clients use a fi le sharing software that searches for other peer cli-
ents. This differs from the client-server model that uses fi le servers to store
fi les for sharing.
7.4 Components of NAS
A NAS device has two key components: NAS head and storage (see Figure 7-3).
In some NAS implementations, the storage could be external to the NAS device
and shared with other hosts. The NAS head includes the following components:
n CPU and memory
n One or more network interface cards (NICs), which provide connectivity
to the client network. Examples of network protocols supported by NIC
include Gigabit Ethernet, Fast Ethernet, ATM, and Fiber Distributed Data
Interface (FDDI).
n An optimized operating system for managing the NAS functionality.
It translates fi le-level requests into block-storage requests and further
converts the data supplied at the block level to fi le data.
n NFS, CIFS, and other protocols for fi le sharing
n Industry-standard storage protocols and ports to connect and manage
physical disk resources
The NAS environment includes clients accessing a NAS device over an IP
network using fi le-sharing protocols.
NFS Network Interface
UNIX NAS Head
NFS CIFS
IP
NAS Device OS
Storage Interface
CIFS
Windows
Storage Array
Figure 7-3: Components of NAS
cc0077..iinndddd 116622 44//1199//22001122 1122::0099::5588 PPMM

Chapter 7 n Network-Attached Storage 163
7.5 NAS I/O Operation
NAS provides fi le-level data access to its clients. File I/O is a high-level request
that specifi es the fi le to be accessed. For example, a client may request a fi le by
specifying its name, location, or other attributes. The NAS operating system
keeps track of the location of fi les on the disk volume and converts client fi le
I/O into block-level I/O to retrieve data. The process of handling I/Os in a NAS
environment is as follows:
1. The requestor (client) packages an I/O request into TCP/IP and forwards
it through the network stack. The NAS device receives this request from
the network.
2. The NAS device converts the I/O request into an appropriate physical
storage request, which is a block-level I/O, and then performs the operation
on the physical storage.
3. When the NAS device receives data from the storage, it processes and
repackages the data into an appropriate fi le protocol response.
4. The NAS device packages this response into TCP/IP again and forwards
it to the client through the network.
Figure 7-4 illustrates this process.
2
Application Storage Interface
3
Operating System NAS Operating System
Block I/O
NFS or CIFS NFS and CIFS
TCP/IP Stack TCP/IP Stack Storage Array
1
Network Interface Network Interface
4
Client File I/O NAS Head
Figure 7-4: NAS I/O operation
7.6 NAS Implementations
Three common NAS implementations are unifi ed, gateway, and scale-out. The
unifi ed NAS consolidates NAS-based and SAN-based data access within a unifi ed
storage platform and provides a unifi ed management interface for managing
both the environments.
cc0077..iinndddd 116633 44//1199//22001122 1122::0099::5588 PPMM

164 Section II n Storage Networking Technologies
In a gateway implementation, the NAS device uses external storage to store
and retrieve data, and unlike unifi ed storage, there are separate administrative
tasks for the NAS device and storage.
The scale-out NAS implementation pools multiple nodes together in a cluster.
A node may consist of either the NAS head or storage or both. The cluster
performs the NAS operation as a single entity.
7.6.1 Unifi ed NAS
Unifi ed NAS performs fi le serving and storing of fi le data, along with providing
access to block-level data. It supports both CIFS and NFS protocols for fi le
access and iSCSI and FC protocols for block level access. Due to consolidation
of NAS-based and SAN-based access on a single storage platform, unifi ed NAS
reduces an organization’s infrastructure and management costs.
A unifi ed NAS contains one or more NAS heads and storage in a single system.
NAS heads are connected to the storage controllers (SCs), which provide access
to the storage. These storage controllers also provide connectivity to iSCSI and
FC hosts. The storage may consist of different drive types, such as SAS, ATA,
FC, and fl ash drives, to meet different workload requirements.
7.6.2 Unifi ed NAS Connectivity
Each NAS head in a unifi ed NAS has front-end Ethernet ports, which connect
to the IP network. The front-end ports provide connectivity to the clients and
service the fi le I/O requests. Each NAS head has back-end ports, to provide
connectivity to the storage controllers.
iSCSI and FC ports on a storage controller enable hosts to access the storage
directly or through a storage network at the block level. Figure 7-5 illustrates
an example of unifi ed NAS connectivity.
7.6.3 Gateway NAS
A gateway NAS device consists of one or more NAS heads and uses external
and independently managed storage. Similar to unifi ed NAS, the storage is
shared with other applications that use block-level I/O. Management func-
tions in this type of solution are more complex than those in a unifi ed NAS
environment because there are separate administrative tasks for the NAS
head and the storage. A gateway solution can use the FC infrastructure, such
as switches and directors for accessing SAN-attached storage arrays or direct-
attached storage arrays.
The gateway NAS is more scalable compared to unifi ed NAS because NAS
heads and storage arrays can be independently scaled up when required.
cc0077..iinndddd 116644 44//1199//22001122 1122::0099::5588 PPMM

Chapter 7 n Network-Attached Storage 165
For example, NAS heads can be added to scale up the NAS device perfor-
mance. When the storage limit is reached, it can scale up, adding capacity
on the SAN, independent of NAS heads. Similar to a unifi ed NAS, a gateway
NAS also enables high utilization of storage capacity by sharing it with the
SAN environment.
APP APP
OS OS
VM VM
Hypervisor
Block Data Access
FC SAN
FC Hosts
APP APP
OS OS
VM VM
Hypervisor
FC Port
Block Data Access
iSCSI SAN
iSCSI Port
Unified NAS
iSCSI Hosts
Ethernet Port
File Access
Ethernet
NAS Clients
Figure 7-5: Unified NAS connectivity
7.6.4 Gateway NAS Connectivity
In a gateway solution, the front-end connectivity is similar to that in a unifi ed
storage solution. Communication between the NAS gateway and the storage
system in a gateway solution is achieved through a traditional FC SAN. To deploy
a gateway NAS solution, factors, such as multiple paths for data, redundant
cc0077..iinndddd 116655 44//1199//22001122 1122::0099::5588 PPMM

166 Section II n Storage Networking Technologies
fabrics, and load distribution, must be considered. Figure 7-6 illustrates an
example of gateway NAS connectivity.
Application Servers
APP APP
OS OS
VM VM
Hypervisor
Client
IP FC SAN
Client
Application Server
Storage Array
Gateway NAS
Client
Figure 7-6: Gateway NAS connectivity
Implementation of both unifi ed and gateway solutions requires analysis
of the SAN environment. This analysis is required to determine the feasibil-
ity of combining the NAS workload with the SAN workload. Analyze the
SAN to determine whether the workload is primarily read or write, and if
it is random or sequential. Also determine the predominant I/O size in use.
Typically, NAS workloads are random with small I/O sizes. Introducing
sequential workload with random workloads can be disruptive to the sequen-
tial workload. Therefore, it is recommended to separate the NAS and SAN
disks. Also, determine whether the NAS workload performs adequately with
the confi gured cache in the storage system.
7.6.5 Scale-Out NAS
Both unifi ed and gateway NAS implementations provide the capability to scale-
up their resources based on data growth and rise in performance requirements.
Scaling up these NAS devices involves adding CPUs, memory, and storage to
cc0077..iinndddd 116666 44//1199//22001122 1122::0099::5588 PPMM

Chapter 7 n Network-Attached Storage 167
the NAS device. Scalability is limited by the capacity of the NAS device to house
and use additional NAS heads and storage.
Scale-out NAS enables grouping multiple nodes together to construct
a clustered NAS system. A scale-out NAS provides the capability to scale
its resources by simply adding nodes to a clustered NAS architecture.
The cluster works as a single NAS device and is managed centrally. Nodes
can be added to the cluster, when more performance or more capacity
is needed, without causing any downtime. Scale-out NAS provides the fl ex-
ibility to use many nodes of moderate performance and availability char-
acteristics to produce a total system that has better aggregate performance
and availability. It also provides ease of use, low cost, and theoretically unlim-
ited scalability.
Scale-out NAS creates a single fi le system that runs on all nodes in the
cluster. All information is shared among nodes, so the entire fi le system is
accessible by clients connecting to any node in the cluster. Scale-out NAS
stripes data across all nodes in a cluster along with mirror or parity pro-
tection. As data is sent from clients to the cluster, the data is divided and
allocated to different nodes in parallel. When a client sends a request to
read a fi le, the scale-out NAS retrieves the appropriate blocks from mul-
tiple nodes, recombines the blocks into a fi le, and presents the fi le to the
client. As nodes are added, the fi le system grows dynamically and data is
evenly distributed to every node. Each node added to the cluster increases
the aggregate storage, memory, CPU, and network capacity. Hence, cluster
performance also increases.
Scale-out NAS is suitable to solve the “Big Data” challenges that enterprises
and customers face today. It provides the capability to manage and store large,
high-growth data in a single place with the fl exibility to meet a broad range of
performance requirements.
7.6.6 Scale-Out NAS Connectivity
Scale-out NAS clusters use separate internal and external networks for back-end
and front-end connectivity, respectively. An internal network provides con-
nections for intracluster communication, and an external network connection
enables clients to access and share fi le data. Each node in the cluster connects
to the internal network. The internal network offers high throughput and low
latency and uses high-speed networking technology, such as Infi niBand or
Gigabit Ethernet. To enable clients to access a node, the node must be connected
to the external Ethernet network. Redundant internal or external networks
may be used for high availability. Figure 7-7 illustrates an example of scale-out
NAS connectivity.
cc0077..iinndddd 116677 44//1199//22001122 1122::0099::5599 PPMM

168 Section II n Storage Networking Technologies
External Switch
Node 1 Node 2 Node 3
Internal Switch 1 Internal Switch 2
InfiniBand Switches
Figure 7-7: Scale-out NAS with dual internal and single external networks
INFINIBAND
Infi niBand is a networking technology that provides a
low-latency, high-bandwidth communication link between
hosts and peripherals. It provides serial connection and
is often used for inter-server communications in high-
performance computing environments. Infi niBand enables
remote direct memory access (RDMA) that enables a device
(host or peripheral) to access data directly from the memory of a remote
device. Infi niBand also enables a single physical link to carry multiple chan-
nels of data simultaneously using a multiplexing technique. The Infi niBand
networking infrastructure consists of host channel adapters (HCAs), tar-
get channel adapters (TCAs), and Infi niBand switches. HCAs are located
within hosts. HCAs provide the mechanism to connect CPUs and memory
of the hosts to the Infi niBand network. Similarly, TCAs enable storage and
other peripheral devices to connect to the Infi niBand network. Infi niBand
switches provide connectivity among HCAs and TCAs.
7.7 NAS File-Sharing Protocols
Most NAS devices support multiple fi le-service protocols to handle fi le I/O
requests to a remote fi le system. As discussed earlier, NFS and CIFS are the
common protocols for fi le sharing. NAS devices enable users to share fi le data
across different operating environments and provide a means for users to
migrate transparently from one operating system to another.
cc0077..iinndddd 116688 44//1199//22001122 1122::0099::5599 PPMM

Chapter 7 n Network-Attached Storage 169
7.7.1 NFS
NFS is a client-server protocol for fi le sharing that is commonly used on UNIX
systems. NFS was originally based on the connectionless User Datagram Protocol
(UDP). It uses a machine-independent model to represent user data. It also uses
Remote Procedure Call (RPC) as a method of inter-process communication
between two computers. The NFS protocol provides a set of RPCs to access a
remote fi le system for the following operations:
n Searching fi les and directories
n Opening, reading, writing to, and closing a fi le
n Changing fi le attributes
n Modifying fi le links and directories
NFS creates a connection between the client and the remote system to transfer
data. NFS (NFSv3 and earlier) is a stateless protocol, which means that it does not
maintain any kind of table to store information about open fi les and associated
pointers. Therefore, each call provides a full set of arguments to access fi les on
the server. These arguments include a fi le handle reference to the fi le, a particular
position to read or write, and the versions of NFS.
Currently, three versions of NFS are in use:
n NFS version 2 (NFSv2): Uses UDP to provide a stateless network connec-
tion between a client and a server. Features, such as locking, are handled
outside the protocol.
n NFS version 3 (NFSv3): The most commonly used version, which uses
UDP or TCP, and is based on the stateless protocol design. It includes
some new features, such as a 64-bit fi le size, asynchronous writes, and
additional fi le attributes to reduce refetching.
n NFS version 4 (NFSv4): Uses TCP and is based on a stateful protocol design.
It offers enhanced security. The latest NFS version 4.1 is the enhancement
of NFSv4 and includes some new features, such as session model, parallel
NFS (pNFS), and data retention.
PNFS AND MPFS
pNFS, as part of NFSv4.1, separates the fi le system protocol
processing into two parts: metadata processing and data pro-
cessing. The metadata includes information about a fi le sys-
tem object, such as its name, location within the namespace,
owner, access control list (ACL), and other attributes. The
pNFS server, also called a metadata server,
(Continued)
cc0077..iinndddd 116699 44//1199//22001122 1122::0099::5599 PPMM

170 Section II n Storage Networking Technologies
PNFS AND MPFS (continued)
does the metadata processing and is kept out of the data path. pNFS clients
send the metadata information to the pNFS server. The pNFS clients access
storage devices directly using multiple parallel data paths. The pNFS client
uses a storage network protocol, such as iSCSI or FC, to perform I/O to storage
devices. The pNFS clients get information about the storage devices from the
metadata server. Because the pNFS server is relieved of data processing and
pNFS clients can access the storage devices directly using parallel paths, the
pNFS mechanism signifi cantly improves the pNFS client performance.
The EMC-patented Multi-Path File System (MPFS) protocol works similar to
pNFS. The MPFS driver software, installed at the NAS clients, sends the fi le’s
metadata to the NAS device (MPFS server) via the IP network. The MPFS driver
obtains information about the location of the data from the NAS device over
the IP network. After knowing the data location, the MPFS driver communi-
cates directly to the storage devices and enables the NAS clients to access
the data over SAN. The following Figure shows the MPFS architecture that
provides different paths for transferring a fi le’s metadata and data.
File Metadata over
IP via CIFS/NFS
MPFS MPFS
Driver Server
NAS Head
Server Read/Write Data over SAN
Storage Array
(NAS Client)
7.7.2 CIFS
CIFS is a client-server application protocol that enables client programs to make
requests for fi les and services on remote computers over TCP/IP. It is a public,
or open, variation of Server Message Block (SMB) protocol.
The CIFS protocol enables remote clients to gain access to fi les on a server.
CIFS enables fi le sharing with other clients by using special locks. Filenames
in CIFS are encoded using unicode characters. CIFS provides the following
features to ensure data integrity:
n It uses fi le and record locking to prevent users from overwriting the work
of another user on a fi le or a record.
n It supports fault tolerance and can automatically restore connections and
reopen fi les that were open prior to an interruption. The fault tolerance
features of CIFS depend on whether an application is written to take advan-
tage of these features. Moreover, CIFS is a stateful protocol because the
CIFS server maintains connection information regarding every connected
cc0077..iinndddd 117700 44//1199//22001122 1122::0099::5599 PPMM

Chapter 7 n Network-Attached Storage 171
client. If a network failure or CIFS server failure occurs, the client receives a
disconnection notifi cation. User disruption is minimized if the application
has the embedded intelligence to restore the connection. However, if the
embedded intelligence is missing, the user must take steps to reestablish
the CIFS connection.
Users refer to remote fi le systems with an easy-to-use fi le-naming scheme:
\\server\share or \\servername.domain.suffix\share.
The fi le naming scheme in an NFS environment is:
Server:/export or Server.domain.suffix:/export.
7.8 Factors Affecting NAS Performance
NAS uses IP network; therefore, bandwidth and latency issues associated with
IP affect NAS performance. Network congestion is one of the most signifi cant
sources of latency (Figure 7-8) in a NAS environment. Other factors that affect
NAS performance at different levels follow:
1. Number of hops: A large number of hops can increase latency because
IP processing is required at each hop, adding to the delay caused at the
router.
2. Authentication with a directory service such as Active Directory or NIS:
The authentication service must be available on the network with enough
resources to accommodate the authentication load. Otherwise, a large
number of authentication requests can increase latency.
3. Retransmission: Link errors and buffer overfl ows can result in retransmis-
sion. This causes packets that have not reached the specifi ed destination
to be re-sent. Care must be taken to match both speed and duplex settings
on the network devices and the NAS heads. Improper confi guration might
result in errors and retransmission, adding to latency.
4. Overutilized routers and switches: The amount of time that an over-
utilized device in a network takes to respond is always more than the
response time of an optimally utilized or underutilized device. Network
administrators can view utilization statistics to determine the optimum
utilization of switches and routers in a network. Additional devices should
be added if the current devices are overutilized.
cc0077..iinndddd 117711 44//1199//22001122 1122::1100::0000 PPMM

172 Section II n Storage Networking Technologies
5. File system lookup and metadata requests: NAS clients access fi les on
NAS devices. The processing required to reach the appropriate fi le or
directory can cause delays. Sometimes a delay is caused by deep direc-
tory structures and can be resolved by fl attening the directory structure.
Poor fi le system layout and an overutilized disk system can also degrade
performance.
6. Over utilized NAS devices: Clients accessing multiple fi les can cause high
utilization levels on a NAS device, which can be determined by viewing
utilization statistics. High memory, CPU, or disk subsystem utilization
levels can be caused by a poor fi le system structure or insuffi cient resources
in a storage subsystem.
7. Over utilized clients: The client accessing CIFS or NFS data might also
be over utilized. An overutilized client requires a longer time to process
the requests and responses. Specifi c performance-monitoring tools are
available for various operating systems to help determine the utilization
of client resources.
IP Network
7 5
1
3
Client
3 6
4 4 4 NAS Device
7 3
3 2
Client
Authentication
Request
Directory Services Server
Figure 7-8: Causes of latency
Confi guring virtual LANs (VLANs), setting proper Maximum Transmission
Unit (MTU) and TCP window sizes, and link aggregation can improve NAS
performance. Link aggregation and redundant network confi gurations also
ensure high availability.
cc0077..iinndddd 117722 44//1199//22001122 1122::1100::0000 PPMM

Chapter 7 n Network-Attached Storage 173
A VLAN is a logical segment of a switched network or logical grouping
of end devices connected to different physical networks. An end device
could be a client or a NAS device. The segmentation or grouping can be
done based on business functions, project teams, or applications. VLAN is
a Layer 2 (data link layer) construct and works similar to a physical LAN. A
network switch can be logically divided among multiple VLANs, enabling
better utilization of the switch and reducing the overall cost of deploying a
network infrastructure.
The broadcast traffi c on one VLAN is not transmitted outside that VLAN,
which substantially reduces the broadcast overhead, makes bandwidth
available for applications, and reduces the network’s vulnerability to broad-
cast storms.
VLANs also provide enhanced security by restricting user access, fl agging
network intrusions, and controlling the size and composition of the broadcast
domain. The MTU setting determines the size of the largest packet that can
be transmitted without data fragmentation. Path maximum transmission unit
discovery is the process of discovering the maximum size of a packet that can
be sent across a network without fragmentation. The default MTU setting for
an Ethernet interface card is 1,500 bytes. A feature called jumbo frames sends,
receives, or transports Ethernet frames with an MTU of more than 1,500 bytes.
The most common deployments of jumbo frames have an MTU of 9,000 bytes.
However not all vendors use the same MTU size for jumbo frames. Servers send
and receive larger frames more effi ciently than smaller ones in heavy network
traffi c conditions. Jumbo frames ensure increased effi ciency because it takes
fewer, larger frames to transfer the same amount of data. Larger packets also
reduce the amount of raw network bandwidth being consumed for the same
amount of payload. Larger frames also help to smooth sudden I/O bursts.
The TCP window size is the maximum amount of data that can be sent
at any time for a connection. For example, if a pair of hosts is talking
over a TCP connection that has a TCP window size of 64 KB, the sender
can send only 64 KB of data and must then wait for an acknowledgment
from the receiver. If the receiver acknowledges that all the data has been
received, then the sender is free to send another 64 KB of data. If the sender
receives an acknowledgment from the receiver that only the fi rst 32 KB of
data has been received, which can happen only if another 32 KB of data is in
transit or was lost, the sender can send only another 32 KB of data because
the transmission cannot have more than 64 KB of unacknowledged data
outstanding.
In theory, the TCP window size should be set to the product of the available
bandwidth of the network and the round-trip time of data sent over the network.
cc0077..iinndddd 117733 44//1199//22001122 1122::1100::0000 PPMM

174 Section II n Storage Networking Technologies
For example, if a network has a bandwidth of 100 Mbps and the round-trip time
is 5 milliseconds, the TCP window should be as follows:
100 Mb/s × .005 seconds = 524,288 bits or 65,536 bytes
The size of the TCP window fi eld that controls the fl ow of data is between
2 bytes and 65,535 bytes.
Link aggregation is the process of combining two or more network interfaces
into a logical network interface, enabling higher throughput, load sharing or load
balancing, transparent path failover, and scalability. Due to link aggregation,
multiple active Ethernet connections to the same switch appear as one link. If
a connection or a port in the aggregation is lost, then all the network traffi c on
that link is redistributed across the remaining active connections.
7.9 File-Level Virtualization
File-level virtualization eliminates the dependencies between the data accessed at
the fi le level and the location where the fi les are physically stored. Implementation
of fi le-level virtualization is common in NAS or fi le-server environments. It
provides non-disruptive fi le mobility to optimize storage utilization.
Before virtualization, each host knows exactly where its fi le resources
are located. This environment leads to underutilized storage resources
and capacity problems because fi les are bound to a specifi c NAS device
or file server. It may be required to move the files from one server to
another because of performance reasons or when the fi le server fi lls up.
Moving fi les across the environment is not easy and may make fi les inac-
cessible during fi le movement. Moreover, hosts and applications need to be
reconfi gured to access the fi le at the new location. This makes it diffi cult for
storage administrators to improve storage effi ciency while maintaining the
required service level.
File-level virtualization simplifi es fi le mobility. It provides user or appli-
cation independence from the location where the fi les are stored. File-level
virtualization creates a logical pool of storage, enabling users to use a logi-
cal path, rather than a physical path, to access fi les. File-level virtualization
facilitates the movement of fi les across the online fi le servers or NAS devices.
This means that while the fi les are being moved, clients can access their fi les
nondisruptively. Clients can also read their fi les from the old location and
write them back to the new location without realizing that the physical loca-
tion has changed. A global namespace is used to map the logical path of a fi le
to the physical path names.
Figure 7-9 illustrates a fi le-serving environment before and after the imple-
mentation of fi le-level virtualization.
cc0077..iinndddd 117744 44//1199//22001122 1122::1100::0000 PPMM

Chapter 7 n Network-Attached Storage 175
Clients Clients Clients Clients
Virtualization Appliance
NAS Head NAS Head NAS Head NAS Head
Storage Array Storage Array
File Sharing Environment File Sharing Environment
(a) Before File-Level Virtualization (b) After File-Level Virtualization
F igure 7-9: File-serving environment before and after file-level virtualization
7.10 Concepts in Practice: EMC Isilon and
EMC VNX Gateway
EMC Isilon is the scale-out NAS solution. Isilon offers high scalability of both
performance and storage capacity. It provides the capability to address big-data
challenges.
The VNX Gateway, a member of the EMC VNX family, provides a gateway
NAS solution. It provides multiprotocol fi le access, dynamic expansion of fi le
systems, high availability, and high performance.
For more information on EMC Isilon and VNX Gateway, visit www.emc.com.
7.10.1 EMC Isilon
Isilon has a specialized operating system called OneFS that enables the scale-
out NAS architecture. OneFS combines the three layers of traditional storage
architectures — fi le system, volume manager, and RAID — into one unifi ed
software layer, creating a single fi le system that spans across all nodes in an
Isilon cluster. OneFS enables data protection and automated data balancing.
It provides the ability to seamlessly add storage and other resources without
system downtime. With OneFS, throughput scales linearly with the number
of nodes in a cluster.
cc0077..iinndddd 117755 44//1199//22001122 1122::1100::0000 PPMM

176 Section II n Storage Networking Technologies
OneFS enables different node types to be mixed in a single cluster through the
addition of the SmartPools application software. SmartPools enables deploying
a single fi le system to span multiple nodes that have different performance
characteristics and capacities. Isilon offers different types of nodes, such as the
X-Series, S-Series, NL-Series, and Accelerator. These nodes have different prices,
performance levels, and storage capabilities. Each type of node is optimized for
handling a specifi c type of workload.
OneFS enables the storage system administrator to specify the access pattern
(random, concurrent, or sequential) on a per-fi le or per-directory basis. This
unique capability enables OneFS to tailor data layout decisions, cache-retention
policies, and data prefetch policies to maximize performance of individual
workfl ows.
OneFS constantly monitors the health of all fi les and disks within a cluster,
and if components are at risk, the fi le system automatically fl ags the problem
components for replacement and transparently relocates those fi les to healthy
components. OneFS also ensures data integrity if the fi le system has an unexpected
failure during a write operation.
When a new storage node is added, the Autobalance feature of OneFS
automatically moves data onto this new node via the Infi niband based inter-
nal network. This automatic rebalancing ensures that the new node does not
become a hot spot for new data. The Autobalance feature is transparent to
the clients and can be adjusted to minimize the impact on high-performance
workloads.
OneFS includes a core technology, called FlexProtect, to provide data pro-
tection. FlexProtect provides protection for up to four simultaneous failures of
either nodes or individual drives per stripe. FlexProtect ensures minimal data
reconstruction time if a failure occurs. FlexProtect provides fi le-specifi c protec-
tion capabilities. Different protection levels can be assigned to individual fi les,
directories, or to portions of a fi le system. These protection levels are aligned
based on the importance of data and workfl ow.
7.10.2 EMC VNX Gateway
The VNX Series Gateway contains one or more NAS heads, called X-Blades,
that access external storage arrays, such as Symmetrix, block-based VNX, or
CLARiiON storage array, via SAN. X-Blades run the VNX operating environment
that is optimized for high-performance and multiprotocol network fi le system
access. Each X-Blade consists of processors, redundant data paths, power sup-
plies, Gigabit Ethernet, and 10-Gigabit Ethernet optical ports. All the X-Blades
in a VNX gateway system are managed by Control Station, which provides a
single point for confi guring VNX Gateway. The VNX Gateway supports both
pNFS and EMC patented Multi-Path File System (MPFS) protocols, which further
improves the VNX Gateway performance.
cc0077..iinndddd 117766 44//1199//22001122 1122::1100::0011 PPMM

Chapter 7 n Network-Attached Storage 177
VNX Series Gateway offers two models: VG2 and VG8. VG8 supports up to
eight X-Blades, whereas VG2 supports up to two. X-Blades may be confi gured
as either primary or standby. A primary X-Blade is the operating NAS head,
whereas a standby X-Blade becomes operational if the primary X-Blade fails. The
Control Station handles an X-Blade failover. The Control Station also provides
other high-availability features, such as fault monitoring, fault reporting, call
home, and remote diagnostics.
Summary
Decisions for choosing an appropriate storage infrastructure are based on main-
taining the balance between cost and performance. Organizations look for the
performance and scalability of SAN combined with the ease of use and lower
total cost of ownership of NAS solutions. Both SAN and NAS have enjoyed
unique advantages in enterprises, and advances in IP technology have scaled
NAS solutions to meet the demands of performance-sensitive applications.
With the advancement of storage networking technology, both SAN-based and
NAS-based accesses have converged to a single platform.
Although NAS invariably imposes higher protocol overhead, it tends to be
the most effi cient for fi le-sharing tasks. NAS performance has signifi cantly
improved with the emergence of MPFS and pNFS protocols. These protocols
use SAN speed to provide access to fi le data. They also offl oad the fi le-data
processing load from the NAS device. NAS can also provide fi le-level access
control to its clients. Organizations can also deploy NAS solutions for their
database applications. Scale-out NAS fulfi lls the need for big-data performance
and big-data capacity. Applications generating big data are optimized and
more easily managed by using a single-expandable fi le system. File-level vir-
tualization provides the fl exibility to move fi les across NAS devices without
disrupting the access to the fi les.
NAS devices impose additional latency to the client traffi c while convert-
ing fi le I/O to block I/Os and vice versa. Also, nested directory structure and
management of permission for individual fi les and directories add overhead to
NAS. The overhead increases as the NAS fi le system grows. Hence, NAS clients
are limited by the performance of the NAS device. Although the use of pNFS
and MPFS protocols has considerably improved the NAS performance, these
protocols might pose some security challenges. Object-based storage, detailed
in the following chapter, addresses the performance and security challenges
in the fi le-serving environment. Unifi ed storage, also detailed in the following
chapter, provides a single-storage platform for accessing fi les, blocks, and objects
simultaneously. Unifi ed storage brings ease of management and eliminates the
additional cost of deploying separate storage systems for storing fi le-, block-,
and object-based data.
cc0077..iinndddd 117777 44//1199//22001122 1122::1100::0011 PPMM

178 Section II n Storage Networking Technologies
EXERCISES
1. SAN is configured for a backup–to-disk environment, and the storage con-
figuration has additional capacity available. Can you have a NAS gateway
configuration use this SAN-attached storage? Discuss the implications of
sharing the backup-to-disk SAN environment with NAS.
2. Explain how the performance of NAS can be affected if the TCP window
size at the sender and receiver are not synchronized.
3. How does the use of jumbo frames affect the NAS performance?
4. Research the file access and sharing features of pNFS.
5. A NAS implementation configured jumbo frames on the NAS head with
9,000 as its MTU. However, the implementers did not see any perfor-
mance improvement and actually experienced performance degradation.
What could be the cause? Research the end-to-end jumbo frame support
requirements in a network.
6. How does file-level virtualization ensure nondisruptive file mobility?
cc0077..iinndddd 117788 44//1199//22001122 1122::1100::0011 PPMM

Chapter 8
Object-Based and
Unifi ed Storage
Recent studies have shown that more than KEY CONCEPTS
90 percent of data generated is unstructured.
This growth of unstructured data has posed Object-Based Storage
new challenges to IT administrators and storage
Content Addressed Storage
managers. With this growth, traditional NAS, which
is a dominant solution for storing unstructured Unified Storage
data, has become ineffi cient. Data growth adds high
overhead to the network-attached storage (NAS) in terms of managing a large
number of permissions and nested directories. In an enterprise environment, NAS
also manages large amounts of metadata generated by hosts, storage systems, and
individual applications. Typically this metadata is stored as part of the fi le and
distributed throughout the environment. This adds to the complexity and latency
in searching and retrieving fi les. These challenges demand a smarter approach
to manage unstructured data based on its content rather than metadata about its
name, location, and so on. Object-based storage is a way to store fi le data in the form of
objects based on its content and other attributes rather than the name and location.
Due to varied application requirements, organizations have been deploying stor-
age area networks (SANs), NAS, and object-based storage devices (OSDs) in their
data centers. Deploying these disparate storage solutions adds management
complexity, cost and environmental overhead. An ideal solution would be to
have an integrated storage solution that supports block, fi le, and object access.
Unifi ed storage has emerged as a solution that consolidates block, fi le, and
object-based access within one unifi ed platform. It supports multiple protocols
for data access and can be managed using a single management interface.
This chapter details object-based storage, its components, and operation. It also
details content addressed storage (CAS), a special type of OSD. Further, this chapter
covers the components and data access method in unifi ed storage.
179
cc0088..iinndddd 117799 44//1199//22001122 1122::0088::4466 PPMM