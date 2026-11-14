# Technical Reviewer Guide

This portfolio supports an initial hiring assessment for backend, applied AI, and cloud-focused engineering work. The project documentation explains design and methodology; private implementation access provides the next level of verification. It is not a résumé or a record of employment history.

## Suggested reading paths

For an initial review, read the [project comparison](README.md), choose a project, and read its overview, decisions, and worked examples. For a deeper review, follow the evidence references into the architecture, implementation, and operations documents. Each case study is self-contained.

| File in each project | Review question |
| --- | --- |
| `README.md` | What problem does the system address, and what was implemented? |
| `DECISIONS.md` | Why were these technologies and boundaries chosen? What are the costs? |
| `EXAMPLES.md` | How does a representative request progress, and what happens on failure? |
| `ARCHITECTURE.md` | Which component owns state, work, and external effects? |
| `ENGINEERING.md` | What mechanisms enforce the intended behavior? |
| `OPERATIONS.md` | How was the system tested, deployed, monitored, and recovered? |
| `EVIDENCE.md` | Which claims have implementation, test, or dated operational support? |

## Competency-to-evidence map

Evidence identifiers are local to each project. For example, `qdf:E02` and `prospect-orchestrator:E02` identify different accomplishments.

| Competency | Concrete evidence | Useful follow-up |
| --- | --- | --- |
| API and service design | [QDF engineering](projects/qdf/ENGINEERING.md), [QDF E01–E02](projects/qdf/EVIDENCE.md) | Trace validation, authorization, quota receipt, and ownership acceptance for one request. |
| Concurrency and backpressure | [QDF E03](projects/qdf/EVIDENCE.md), [worked contention example](projects/qdf/EXAMPLES.md) | Inspect the same-key/full-queue regression and explain how waiting permits progress. |
| Safe file handling | [QDF E04–E05](projects/qdf/EVIDENCE.md), [attachment example](projects/qdf/EXAMPLES.md) | Follow descriptor validation, bounded copies, output selection, MIME construction, and cleanup. |
| Structured AI integration | [JobResearcher E03 and E07](projects/job-researcher/EVIDENCE.md), [QDF E06](projects/qdf/EVIDENCE.md) | Identify checks that run outside the model, and cases they cannot establish as correct. |
| Data and policy modelling | [JobResearcher E02, E04–E06](projects/job-researcher/EVIDENCE.md) | Inspect content/context versioning and preservation of old assessments after a policy change. |
| Browser automation and human handoff | [JobResearcher E08–E09](projects/job-researcher/EVIDENCE.md) | Inspect a synthetic form test, session ownership, submission intent, and recovery after interruption. |
| Transactional workflow ownership | [Prospect Orchestrator E03–E05](projects/prospect-orchestrator/EVIDENCE.md) | Trace a claim transaction and distinguish failed local work from an unresolved provider operation. |
| Paid-request recovery | [Prospect Orchestrator E08](projects/prospect-orchestrator/EVIDENCE.md), [receipt example](projects/prospect-orchestrator/EXAMPLES.md) | Inspect correlation checks, receipt writing, interrupted commit recovery, and unknown outcomes. |
| Container operations and recovery | [QDF operations](projects/qdf/OPERATIONS.md), [JobResearcher operations](projects/job-researcher/OPERATIONS.md), [Prospect Orchestrator operations](projects/prospect-orchestrator/OPERATIONS.md) | Review image definitions, state backups, disabled startup, and the original dated deployment evidence. |

## Interpreting evidence

The public technical explanations derive from supplied documentation exports. This repository does not include the private application source, original test outputs, or private source-to-claim mappings. Describing inspected implementation in an export is different from independently verifying that implementation from this public checkout.

- **Implementation described:** the export reports an inspected code path or configuration. Check private source for independent confirmation.
- **Test coverage described:** relevant assertions or harnesses were inspected; this alone does not establish execution.
- **Reported test execution:** an export or ledger records a completed run with a date and scope. QDF's export-time rerun and the other projects' earlier ledger results have different provenance.
- **Historical live observation:** a dated provider or deployment check supports that bounded observation. It does not establish current credentials, uptime, or universal provider compatibility.
- **Illustrative example:** a synthetic scenario explains the documented mechanism. It is not extracted source, a runnable demo, or an additional test result.

Assess metrics within their project and scope. Do not combine suite totals, convert synthetic records into customers, or interpret configured limits as measured performance. None of the projects establishes calibrated model accuracy, high availability, or quantified hiring/revenue outcomes.

## What to inspect with private access

Request access through the channel where this portfolio was shared, naming the project and capability of interest. Private review can connect the public evidence IDs to implementation and original verification records without publishing operational secrets or personal data.

A useful review is to select one claim, locate the corresponding implementation and tests, examine an adverse case, and reproduce the relevant offline check at an agreed revision. Test requirements and private fixtures should be checked before attempting a full suite. Live provider writes are separate from offline review and require explicit authorization and suitable credentials.

For authorship and responsibility, ask which parts were designed, implemented, debugged, or operated by the candidate and how AI assistance was used. Project artifacts alone do not establish a contribution percentage, team role, or employment relationship.

## Maintaining the public package

Keep project names and IDs stable. Update the project documents and `portfolio.json` together when scope or evidence changes. Attach a date, provenance, and limitation to new quantitative claims. Label proposed architecture and illustrative examples rather than presenting them as implemented results. Keep source access details, credentials, candidate records, and production addresses outside the public package.

Run `python3 scripts/check_portfolio.py` before submitting documentation changes. Its success checks the public package's consistency, not the truth of external records.
