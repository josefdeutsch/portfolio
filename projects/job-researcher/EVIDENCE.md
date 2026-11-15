# JobResearcher — Evidence and Claim Boundaries

> Source: the supplied private-project case-study export, reviewed on 14 November 2026. Test and deployment statements below describe that export and its dated records; they were not rerun in this public documentation repository.

## How to read this portfolio

This export summarizes repository evidence inspected on **14 November 2026**. Implementation claims are grounded in source and tests; deployment claims are grounded in dated operational records. The private source-reference report is intentionally excluded from this directory. Public readers can understand these documents without access to the underlying repository, but cannot independently inspect omitted private source from this export alone.

| Label | Meaning |
|---|---|
| Implemented | A corresponding code path or deployment definition exists and was inspected. |
| Tested | The behavior is covered by automated tests; recorded passing results are dated below. |
| Deployment recorded | Operational records describe deployment and verification on a specified date. |
| Limited / conditional | Behavior depends on provider support, configuration, credentials, or human action. |
| Not established | There is insufficient evidence for the broader claim. |

## Verifiable engineering accomplishments

The IDs below map to a separate private evidence report, rather than inaccessible public links.

| ID | Accomplishment | Evidence class and scope |
|---|---|---|
| E01 | Normalized public listings across Greenhouse, Ashby, Lever, and Remotive using existing adapters. | Implemented; adapter and source-expansion tests; recorded verification of 104 added boards from 106 candidates, giving 109 configured sources. |
| E02 | Associated assessments with content/context and retained historical observations. | Implemented and tested; preserves previous assessment versions and distinguishes observation from proof of closure. |
| E03 | Integrated structured AI assessments with supplied evidence identifiers and local validation. | Implemented and tested; no independent model-accuracy score established. |
| E04 | Added deterministic publication-age and degree-requirement checks. | Implemented and tested for boundary cases, optional wording, alternative routes, and expiration of cached results. Heuristic text coverage remains limited. |
| E05 | Reassessed 1,722 stored jobs while retaining 2,098 prior assessment records. | Deployment recorded on 13 November 2026; technical assessments were reused, with no batch model calls for that policy refresh. Resulting total: 3,820 assessment versions. |
| E06 | Separated application preparation from discovery through a scoped read-only API and separate databases. | Implemented, tested, and deployment recorded; avoids sharing research WAL files with the consumer. |
| E07 | Constrained résumé tailoring to approved facts and required projects; validated generated PDFs. | Implemented and tested, including one-page reference mode, fixed sections, project coverage, text extraction, and integrity checks. |
| E08 | Built an interactive handoff to the same remote Chromium session. | Implemented, browser-tested with synthetic forms, and deployment recorded; supports one interactive session and human final submission. |
| E09 | Implemented opportunity uniqueness, submission intent, receipts, and uncertainty holds. | Implemented and failure-tested; historical records were checked during deployment. Not an exactly-once guarantee across external systems. |
| E10 | Added Gmail OAuth, mailbox processing, guarded sending, and sent-mail reconciliation code. | Implemented and tested with mocked interactions. Current deployment mode does not enable autonomous sending. |
| E11 | Refreshed curated project evidence against commit-pinned source anchors. | Implemented and tested for changed commits, missing anchors, authentication failure, and visibility changes. Source verification is not production verification. |
| E12 | Added persistent user dismissal without erasing submission safety history. | Implemented and tested through the browser interface, authorization checks, refresh/restart persistence, and preservation of receipts/events. |
| E13 | Containerized both services with persistent data and bounded operating controls. | Deployment definitions inspected; recorded healthy deployment and database checks on 13 November 2026. No high-availability claim. |

## Quantitative evidence

- **379 tests passed**, one warning, in the recorded 13 November 2026 suite.
- **104 of 106 additional boards verified** in the recorded expansion; two responses exceeded the existing response-size bound. This was not proof that those two boards were permanently invalid.
- **109 total configured sources** after preserving the five original feeds.
- **1,722 saved jobs** received updated policy assessments in the latest recorded migration; **2,098 previous assessment records** remained intact.

These are dated engineering observations. They are not customer adoption, hiring conversion, uptime, accuracy, or cloud-cost metrics. Source checks were bounded and do not demonstrate exhaustive vacancy coverage.

## Implemented but conditional capabilities

The repository includes direct email delivery, registration/login recipes, persisted browser state, verification-response handling, and provider-specific upload controls. Supported workflows require suitable recipes and authorization. Mocked success does not prove arbitrary live account creation or general ATS automation. Current recorded operation uses human review and final action.

CAPTCHA, personal declarations, and unsupported controls can require human action. PDF text/page checks validate the configured document constraints, not universal ATS compatibility. A valid response schema does not establish semantic accuracy.

Changing a portfolio repository's identity or visibility can invalidate its cached verification state under the present implementation. The export documents that constraint; it does not change visibility policy or repair the running integration.

## Experimental, planned, or unproven areas

- Remote browser interaction is an implemented feature with practical latency and provider-verification limitations, not a universally smooth interface.
- Universal autonomous applications, CAPTCHA bypass, automatic resolution of unknown mandatory declarations, and guaranteed provider acceptance are not demonstrated.
- No evidence establishes distributed orchestration, multi-region deployment, high availability, Kubernetes operation, model training, fine-tuning, or a vector-search/RAG subsystem in this project.
- No quantitative claims are made for increased hiring success, saved labor, reduced model spend beyond the documented zero-call policy refresh, or commercial scale.

## Scope of this publication package

The original five-document export contains engineering descriptions and aggregate operational evidence only. This public case study adds an explanatory decision record and illustrative worked examples, without adding application execution evidence. The package excludes candidate data, employer correspondence, original application answers, source excerpts from other projects, credentials, infrastructure addresses, sensitive endpoints, and internal access procedures. Project links remain within this standalone directory.

Preparing the original export did not change application code, runtime configuration, deployment, or repository visibility. The public documentation refactor does not establish a new deployment, provider check, or application test run.
