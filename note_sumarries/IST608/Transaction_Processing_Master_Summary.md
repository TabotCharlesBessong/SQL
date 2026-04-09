# Transaction Processing I - Master-Level Summary

## 1. Core Idea of Transaction Processing

1. A transaction is the smallest logical unit of database work that must be treated as all-or-nothing.
2. Transaction processing exists because real DBMSs are multiuser, high-throughput systems where many operations interleave.
3. Two system goals must be achieved at the same time:
   1. Correctness (no inconsistency, no invalid states)
   2. Performance (high concurrency, low response time)

## 2. Operational Model

1. Database behavior is abstracted around `read_item(X)` and `write_item(X)`.
2. Physical I/O is block-based, while logical operations are item-based.
3. Transaction boundaries define control points for correctness:
   1. Start
   2. End
   3. Commit or Rollback

Key insight: Even simple logical reads/writes hide a buffer and disk pipeline, which is why failures and interleavings matter.

## 3. Why Concurrency Control Is Necessary

Uncontrolled interleaving causes classic anomalies:

1. Lost update: one transaction's update overwrites another.
2. Dirty read (temporary update): reading uncommitted data that may later be rolled back.
3. Incorrect summary: aggregate computed over mixed old/new values.

Master-level framing: These are violations of serialization constraints under concurrent schedules.

## 4. Why Recovery Is Necessary

Failures are multi-source:

1. System crashes
2. Program and logic errors
3. Application-level abort conditions
4. Concurrency-control enforced aborts (for serializability/deadlock)
5. Disk/media failures
6. Catastrophic physical events

Recovery preserves atomicity and durability despite these failure modes.

## 5. Transaction Lifecycle and Recovery Semantics

### Transaction states

1. Active
2. Partially committed
3. Committed
4. Failed
5. Terminated

### Recovery manager primitives

1. Begin transaction
2. Read and write operations
3. End transaction
4. Commit transaction
5. Rollback/Abort
6. Undo and Redo

### Commit point principle

1. A transaction is considered committed only after its effects are safely reflected in log semantics.
2. Force-writing log before commit is essential to durability.

## 6. System Log: The Backbone of Recovery

Typical log records include:

1. Start transaction
2. Read item
3. Write item with before-image and after-image
4. Commit
5. Abort

Why it matters:

1. Undo: traverse backward to restore old values.
2. Redo: traverse forward to reapply committed updates not yet persisted.
3. This is the operational realization of Atomicity and Durability.

## 7. ACID at Graduate Depth

1. Atomicity: indivisible unit of effect.
2. Consistency: each committed transaction preserves integrity constraints.
3. Isolation: concurrent execution should be equivalent to an acceptable serial behavior.
4. Durability: committed effects survive later failures.

Important distinction: Consistency is a correctness property of transaction plus constraints; isolation is a scheduling property.

## 8. Schedule Theory and Recoverability

A schedule is an interleaving that preserves each transaction's internal order.

### Recoverability hierarchy

1. Recoverable schedule:
   1. If Tj reads value written by Ti, then Tj cannot commit before Ti commits.
2. Cascadeless schedule:
   1. Transactions only read committed values.
3. Strict schedule:
   1. No read or write of X until last writer of X commits.

Key relationship: Strict implies Cascadeless implies Recoverable.

Practical impact: Stricter classes simplify recovery and avoid cascading rollbacks.

## 9. Serializability Theory

1. Serial schedule: transactions run one after another.
2. Serializable schedule: non-serial execution equivalent to some serial order.

### Conflict perspective

1. Conflict equivalence preserves order of conflicting pairs.
2. Conflict-serializable if equivalent to a serial schedule under conflict equivalence.

### Graph test (precedence/serialization graph)

1. Nodes are transactions.
2. Edge Ti -> Tj if Ti operation conflicts and precedes Tj operation on same item.
3. Acyclic graph if and only if conflict-serializable.

### View perspective

1. View serializability is more permissive than conflict serializability.
2. All conflict-serializable schedules are view-serializable, but not all view-serializable schedules are conflict-serializable.
3. Blind writes are the classic source of this gap.

## 10. Practical Enforcement in DBMS

1. Directly checking full serializability online is hard.
2. DBMSs therefore enforce protocols, especially locking protocols such as two-phase locking.
3. Practical correctness is achieved by protocol guarantees, not by post-hoc schedule inspection.

## 11. SQL Transaction Semantics

1. A single SQL statement is atomic.
2. Transaction start is often implicit.
3. Transaction end must be explicit via Commit or Rollback.
4. `SET TRANSACTION` controls:
   1. Access mode (`READ ONLY`, `READ WRITE`)
   2. Isolation level
   3. Diagnostics settings

### Isolation levels and anomalies

1. Read Uncommitted: dirty read, nonrepeatable read, phantom possible.
2. Read Committed: blocks dirty read, allows nonrepeatable read and phantom.
3. Repeatable Read: blocks dirty and nonrepeatable read, phantom may remain.
4. Serializable: blocks all three.

Interpretation: Isolation level selection is an explicit consistency-throughput tradeoff.

## 12. High-Value Exam Synthesis

1. Concurrency control solves correctness under interleaving; recovery solves correctness under failure.
2. ACID is the contract; logging plus control protocols are implementation machinery.
3. Recoverability and serializability are distinct:
   1. Recoverability is about safe commit dependency.
   2. Serializability is about equivalent execution correctness.
4. Strict schedules are highly desirable because they reduce both anomaly risk and recovery complexity.

## 13. Quick Master Revision Checklist

1. Can you define and differentiate recoverable, cascadeless, and strict schedules?
2. Can you build and interpret a precedence graph and decide conflict serializability?
3. Can you explain why view serializability is broader than conflict serializability?
4. Can you map each SQL isolation level to dirty read, nonrepeatable read, and phantom behavior?
5. Can you justify force-writing log before commit in terms of durability?
