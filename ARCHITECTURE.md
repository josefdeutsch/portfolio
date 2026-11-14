# Architecture

## System shape

QDF is a single-host application composed of seven independently packaged Python services and one persistent relational database. Services coordinate through committed database state; there is no central workflow service, message broker or direct downstream-service invocation.

Each implemented service runs one asynchronous execution owner. The common runtime polls for eligible work, while synchronous database operations run in worker threads. Network operations have separate timeouts and do not hold database writer locks.

```mermaid
flowchart TD
    Seed[Validated input] --> List[List discovery]
    Search[Search discovery: scaffold only] -. alternative .-> DB[(Shared SQLite)]
    List <--> DB
    Account[Company enrichment] <--> DB
    Employees[Employee discovery] <--> DB
    Profile[Profile enrichment] <--> DB
    Classifier[AI classification] <--> DB
    Invite[Invitation handoff] <--> DB
    List --> PB[PhantomBuster]
    Account --> PB
    Employees --> PB
    Profile --> PB
    Invite --> PB
    Classifier --> Reader[Bounded company-site reader]
    Classifier --> LLM[OpenAI Chat Completions]
```

Arrows to the database represent eligibility checks, work ownership and committed results. They do not imply that every service can dispatch work concurrently without limits.

## Components and responsibilities

| Component | Responsibility | Implementation boundary |
| --- | --- | --- |
| List discovery | Validate a selected list, admit companies and retain continuation state | Implemented adapter |
| Search discovery | Alternative discovery entry point | Service scaffold; business adapter absent |
| Company enrichment | Attach provider-attributed company facts | Implemented adapter |
| Employee discovery | Associate candidate people with selected companies | Implemented adapter; discovery does not establish qualification |
| Profile enrichment | Store reusable person-level evidence with source references | Implemented adapter |
| Classifier | Research bounded company-site evidence and validate a structured decision | Implemented adapter |
| Invitation handoff | Select eligible decisions, enforce policy and preserve contact suppression | Implemented adapter; acknowledgment is not delivery proof |
| Shared runtime | Intake, polling, claims, execution bounds, failure handling and status | Reused across service packages |
| Shared storage | Schema, identity resolution, transactions, guards, references and backup primitive | SQLite-backed package |

## Data flow and ownership

The dependency order is list discovery, company enrichment, employee discovery, profile enrichment, classification and invitation handoff. Each stage consumes eligible committed evidence and records its own result. A service's failure does not replace another service's source facts.

Companies and people have stable identities. Separate association records represent a person connected to a target company. This avoids treating a selected target company as proof of the person's current employer. Alias handling permits corroborated profile identifiers to resolve to the same person.

Work records include the owning service, input fingerprint, source references, local lifecycle state and external execution identifier. Result-reference tables permit reuse across inputs and related associations without copying whole upstream datasets. Changed material evidence or classification policy can require a new decision while retaining earlier history.

## Persistence and concurrency

SQLite uses WAL journaling, foreign keys, STRICT tables, uniqueness checks and bounded lock waits. Transactional claims acquire a writer reservation, verify eligibility and persist ownership before external I/O. Result insertion and local completion are committed together.

Short transactions make a shared database practical at the intended scale. The tradeoff is a single writer and shared schema: independent service packages do not imply independent databases, horizontal scaling or distributed fault isolation. Multiple hosts sharing a live SQLite file are not established by this design.

## External operations and recovery

```mermaid
sequenceDiagram
    participant R as Service runtime
    participant D as SQLite
    participant P as External provider
    R->>D: Claim eligible work and persist guard
    R->>P: Submit bounded operation
    P-->>R: Return execution identifier
    R->>D: Persist identifier
    R->>P: Observe the same operation
    P-->>R: Terminal status and result
    R->>D: Validate and atomically commit result/completion
    Note over R,D: After a crash, retain uncertainty and reconcile known IDs
```

There is an unavoidable uncertainty window if a provider accepts a request but its identifier is lost. The application retains a guard instead of claiming exactly-once execution or assuming that a timeout means nothing happened. Local work can be failed while the external operation still requires reconciliation.

## Decisions and tradeoffs

- **Database polling instead of a broker:** reduces infrastructure and keeps dependencies transactional, at the cost of polling latency and database contention.
- **Shared packages instead of duplicated service logic:** gives consistent recovery and input validation, but increases the importance of cross-service regression checks.
- **Conservative scalar provider inputs:** avoids guessing unsupported batch serialization, at the cost of additional launches. Provider batch caps are separate from workflow capacity.
- **Failure state separate from uncertainty guards:** makes failures visible without making dangerous retries eligible. Some unresolved work intentionally remains blocked.
- **Reference-aware retention:** removes eligible operational detail while retaining evidence needed downstream and permanent contact protection. Recovery must preserve those references.
- **Limited coordination scope:** alternative discovery services share a guard, and each service has its own execution slot. A universal non-overlap scheduler for every Phantom is not implemented.

No queue cluster, Kubernetes deployment, vector database or model-training subsystem is needed to explain the implemented architecture. No high-availability or measured production-scale claim is made.

See [engineering](ENGINEERING.md) for implementation mechanisms and [evidence](EVIDENCE.md) for verification boundaries.
