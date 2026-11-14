# JobResearcher — Worked Examples

These synthetic scenarios explain the supplied implementation descriptions. Names, identifiers, and intermediate labels are illustrative, not actual wire formats, extracted source, executed demonstrations, or new test results. Evidence IDs refer to [EVIDENCE.md](EVIDENCE.md).

## From vacancy discovery to a prepared application

**Scenario:** a supported ATS publishes a Python backend role within the configured freshness window. Approved project facts include typed APIs and SQLite workflow experience. Work authorization still needs confirmation.

| Step | Mechanism | Why it matters |
| --- | --- | --- |
| 1 | Normalize the provider record, canonical URL, publication date, and content hash. | Different ATS field names should not change the meaning of downstream rules. |
| 2 | Apply publication-age, education, and other configured selection checks. | A strong technical match cannot override explicit selection policy. |
| 3 | Reuse an assessment only in matching content/context, or request a bounded structured assessment with supplied evidence IDs. | A cached result is tied to its inputs rather than treated as permanently valid. |
| 4 | Persist assessment and source/run diagnostics. | A successful scan and an eligible job are separate facts. |
| 5 | Companion reads eligible work through the scoped API and checks readiness. | Missing mandatory personal information can block progress despite a high relevance score. |
| 6 | Once ready, select approved facts, validate quoted requirements, and generate a versioned PDF package. | Claims remain attributable; reference mode checks fixed sections, project coverage, and one-page output. |
| 7 | Open a supported form and hand the same browser session to the user. | Preparation is separate from personal verification and final submission. |

If a generated fact ID is not in the approved catalog, the local validator rejects it. If the source publication timestamp is missing or invalid, the configured freshness rule excludes the role until verified. This illustrates how deterministic validation surrounds model use. See E01–E04 and E06–E08.

**Private-source review:** inspect normalization fixtures, evidence-ID membership checks, requirement-quote validation, PDF content/page assertions, and a synthetic browser handoff test.

## Change selection policy without repeating technical model assessment

**Scenario:** a previously assessed role says “degree or equivalent experience.” A revised user policy excludes that alternative even if the technical relevance assessment remains useful.

The reassessment utility applies the new deterministic selection rules under a new assessment context and retains the earlier version. It does not need a batch of new model calls just to reinterpret that policy. This is the mechanism behind the recorded 13 November 2026 refresh of 1,722 jobs while preserving 2,098 older assessment records. Those counts come from the supplied deployment record, not this example.

The policy expresses one user's criteria; it is not a general rule about who should apply. Text/heading classification can still miss unfamiliar phrasing. See E04–E05 and [policy implementation](ENGINEERING.md).

**Private-source review:** inspect context versioning, alternative/optional education fixtures, cached-age expiry, and old-record preservation checks.

## An interrupted submission is different from interrupted preparation

**Scenario:** a supported final-action path records submission intent, but the process stops before confirmation is durably available.

On recovery, the ledger retains an uncertain outcome. It does not treat the absence of confirmation as proof that the employer received nothing. The opportunity stays protected from a blind retry while evidence is reconciled. An interruption during preparation, before submission intent, can use a different recovery path and become eligible for preparation again.

This scenario explains the documented ledger design, not an enabled unattended-submit mode. The latest recorded operation leaves final submission to the human. See E08–E09 and [recovery details](OPERATIONS.md).

**Private-source review:** inspect uniqueness constraints, intent/event ordering, interrupted-submission tests, and which states are allowed back into preparation. Browser-side verification and employer acceptance remain external facts.
