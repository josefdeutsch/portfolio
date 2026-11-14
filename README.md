# Backend & Applied AI Engineering Portfolio

Three engineering case studies covering Python backends, AI integrations, persistent workflows, and single-host cloud operations. Each project explains its problem, implementation, technology choices, failure handling, and verification evidence so a hiring reviewer can assess technical fit before requesting private source access.

This public repository contains documentation, illustrative examples, and a machine-readable project index. The application implementations, original tests, and detailed source-to-claim mappings are in private repositories and supporting records. **Private implementation access is available on request for technical review.** Use the contact channel through which you received this portfolio; no public application endpoint or credentials are required.

## Projects at a glance

| Project | Problem and implemented approach | Engineering focus | Start here |
| --- | --- | --- | --- |
| **QDF — AI Email Processing Framework** | Turn requests arriving in a service-owned Gmail mailbox into authorized, bounded AI tasks and email replies with selected attachments. | API contracts, transactional quota accounting, queue concurrency, file ownership, typed AI outputs. | [QDF case study](projects/qdf/README.md) |
| **JobResearcher** | Discover vacancies, assess relevance against attributable evidence, prepare validated application documents, and hand supported forms to a human for final submission. | Data adapters, versioned assessments, deterministic policy, PDF validation, Playwright, recovery. | [JobResearcher case study](projects/job-researcher/README.md) |
| **Prospect Orchestrator** | Coordinate company/person enrichment, AI classification, and controlled invitation handoff while retaining evidence of uncertain external operations. | Relational identity, transactional claims, asynchronous integration, paid-result recovery, duplicate prevention. | [Prospect Orchestrator case study](projects/prospect-orchestrator/README.md) |

QDF and Prospect Orchestrator are separate systems. The supplied Prospect Orchestrator export uses the longer name “QDF Prospect Orchestrator”; its storage, runtime, and execution guarantees must not be attributed to the email framework.

## What the portfolio demonstrates

- **Backend engineering:** FastAPI contracts, Pydantic validation, SQLite transactions, state ownership, and bounded execution. Start with [QDF's attachment handoff](projects/qdf/EXAMPLES.md).
- **Applied AI engineering:** OpenAI API integration, structured outputs, attributable evidence, deterministic validation, and explicit uncertainty. Start with [JobResearcher's assessment and preparation workflow](projects/job-researcher/EXAMPLES.md).
- **Reliability engineering:** distinguish accepted work from completed work; preserve state across failures; reconcile uncertain external writes. Start with [Prospect Orchestrator's recovery example](projects/prospect-orchestrator/EXAMPLES.md).
- **Cloud operations:** Docker Compose on Linux/AWS EC2, persistent state, restricted containers, backups, and dated deployment checks. Each project's `OPERATIONS.md` explains its actual scope.

Technology choices are explained per project, including why SQLite, local queues or polling, and single-host Compose were suitable for the implemented scope and what would require redesign. These case studies support discussion of engineering decisions; they do not imply employment tenure, exclusive authorship, or measured commercial impact.

## Evidence snapshot

These results are reported by the supplied exports and their dated records. Application tests were **not** executed in this public repository. Counts have different scopes and should be assessed separately.

| Project | Reported result | Date and qualification | Evidence |
| --- | --- | --- | --- |
| QDF | 138 tests passed; 3 subtests passed | 14 November 2026 export-time rerun, providers mocked; website excluded. | [QDF evidence, E11](projects/qdf/EVIDENCE.md) |
| JobResearcher | 379 tests passed; one warning | Recorded suite on 13 November 2026; no new suite run for the export. | [JobResearcher evidence](projects/job-researcher/EVIDENCE.md) |
| Prospect Orchestrator | 616 tests passed; three Search-related exclusions | Development ledger on 1 November 2026; no new suite run for the export. | [Prospect Orchestrator evidence](projects/prospect-orchestrator/EVIDENCE.md) |

Historical deployment records establish dated observations, not current availability. Synthetic scenarios and configured limits are identified as such. Source descriptions, reported test execution, and live-provider observations are separate evidence classes.

## How to review

1. Read the relevant project overview for the problem, implementation, and strongest evidence.
2. Follow `DECISIONS.md` for technology rationale and `EXAMPLES.md` for a concrete workflow and failure case.
3. Inspect `ARCHITECTURE.md`, `ENGINEERING.md`, and `OPERATIONS.md` for technical depth.
4. Use `EVIDENCE.md` to check the claim's scope, date, and limitations. Request private implementation access to verify the source and original tests.

The [reviewer guide](REVIEW_GUIDE.md) maps competencies to evidence and proposes source-review questions. Automated readers can start with [portfolio.json](portfolio.json); [AGENTS.md](AGENTS.md) explains navigation and evidence interpretation. Every project uses the same seven-file layout and works as a standalone case study.

## Repository validation

Run `python3 scripts/check_portfolio.py` from this directory. It checks the project index, local links, document structure, evidence references, and required project files using the Python standard library. GitHub Actions runs the same check on pushes and pull requests. These checks validate the documentation package, not the private applications or historical results.

Content baseline: supplied exports reviewed on **14 November 2026**. No application setup or credentials are needed to read or validate this repository.
