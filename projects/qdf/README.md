# QDF — AI Email Processing Framework

QDF turns requests in a service-owned Gmail mailbox into authorized AI tasks and replies with selected attachments. The problem is coordinating quota, concurrency, files, and provider handoffs while distinguishing accepted work from completed delivery.

## My contribution

- **Architecture:** Drawing on my Python development experience, I defined QDF’s requirements and email-to-AI architecture, including API/webhook interfaces, project structure, FastAPI endpoints, and separation of execution orchestration (`exec/`) from workload logic (`task/`).
- **Fix contract:** I designed independent Fixes that adapt a reference implementation, own their code/dependencies/container, and share request-handling and delivery contracts for text, attachments, or both. I chose simple ownership boundaries: after receiver acceptance, the sender finishes without tracking downstream completion.
- **AI-assisted development:** I began using cloud Codex in February 2026, prioritizing prompt critique and iterative specification refinement over test-driven development. Drawing on Andrew Ng’s reflection teaching, I experimented with critiques and reviewed prompts/AI output until ambiguous requirements became clear. Natural-language requirements → API mocks was one example. Early execution testing used unit tests and mocked APIs, without live-provider tests.
- **Deployment and validation:** I personally configured and deployed QDF on EC2 end to end, ran runtime commands including `docker exec`, used a test Fix for container lifecycle validation, and confirmed reply receipt in a separate email session. I developed operational contracts/guides through personal work and AI assistance, with AI writing functions under my direction.
- **Privacy:** My original requirement was to inspect incoming metadata without retaining it. The implementation retains limited operational state: quota receipts, a mailbox-history checkpoint, and diagnostic identifiers; this differs from the original requirement.
- **Tracking and roadmap:** Correlation IDs, timestamps, and lifecycle events already track workflows. My next priority is durable preservation of that evidence for operational reliability, toward recovering interrupted AI workloads without user resubmission. Durable execution, retries, replay, and reconciliation remain planned; preserved metadata is a foundation, not complete recovery.

## Implemented solution

A selected request follows **Gmail ingress → admission → routing → task → delivery**. Seven Compose services support multiple task implementations; the retrieval-oriented task was excluded from operational acceptance.

- **Admission:** SQLite entitlement checks and transactional receipts prevent repeated quota charges for recorded request IDs ([E02](EVIDENCE.md)).
- **Execution:** bounded process-local queues and same-key exclusion control contention; queue entries remain volatile ([E03](EVIDENCE.md)).
- **Files and AI:** receiver-owned copies, explicit output selection, typed agent output, and deterministic source checks support attachment processing and MIME delivery ([E04–E07](EVIDENCE.md)).

Operational contracts distinguish process health, local readiness, handoff ownership, and provider outcome. A successful handoff is not proof of mailbox receipt.

Python, FastAPI, Pydantic, SQLite, Gmail/Pub/Sub, and OpenAI Responses API/Agents SDK underpin the system. Docker Compose and Nginx support its recorded single-host EC2 deployment. The [decision record](DECISIONS.md) explains the tradeoffs.

## Strongest supported result

The supplied export reports **138 passing tests and 3 passing subtests on 14 November 2026**, across three suites with providers mocked and website tests excluded ([E11](EVIDENCE.md)). Application tests were not run in this public checkout. These checks cover backend behavior, not model accuracy or exactly-once delivery; full scope and historical observations are in [EVIDENCE.md](EVIDENCE.md).

## Deeper review

[Architecture](ARCHITECTURE.md) · [Engineering](ENGINEERING.md) · [Decisions](DECISIONS.md) · [Illustrative examples](EXAMPLES.md) · [Operations](OPERATIONS.md) · [Evidence](EVIDENCE.md)

Private implementation access is available on request for deeper verification. Start with the quota transaction, queue-contention regression, or attachment handoff tests. Documentation baseline: 14 November 2026.
