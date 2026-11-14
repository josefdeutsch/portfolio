# JobResearcher — Engineering Implementation

> Source: the supplied private-project case-study export, reviewed on 14 November 2026. Test and deployment statements below describe that export and its dated records; they were not rerun in this public documentation repository.

## Integrating inconsistent external data

The adapters map provider records into a common job representation, including source identifiers, company, title, description, publication time, employment type, locations, remote policy, and canonical URL. Content hashes support change detection. Source configuration validation rejects malformed board identifiers and duplicate configurations.

Discovery is deliberately bounded. Request handling restricts destinations, limits JSON response size, disables automatic redirects, uses timeouts, and retries transient read failures within a deadline. Source reports distinguish successful retrieval, failure, deferred work, and reached scan limits. The recorded board expansion reused existing adapters rather than adding a new integration framework.

## Evidence-grounded AI

Research evaluation uses the OpenAI API with a strict JSON Schema for relevance score, eligibility, matched skills, gaps, explanation, demonstration proposal, and evidence IDs. Local validation checks structure, ranges, field types, and reference membership. Unknown location compatibility cannot silently become eligible without supporting information.

Evidence records identify repository, commit, path, excerpt, and verification level. Imported source evidence is explicitly source-only. The application portfolio cache checks curated source anchors after commit changes; it does not infer arbitrary new achievements from the contents of a repository. Evidence versions can trigger a bounded reevaluation of previously blocked qualification work without reopening attempted submissions.

Job text and portfolio content are described to the model as untrusted data. Schema validation and deterministic checks constrain the output, but neither prompts nor valid JSON prove that semantic judgments are correct. This is an API-integrated AI workflow, not a trained model, fine-tuned model, or measured improvement in inference quality.

## Deterministic selection and policy changes

Publication age is evaluated from the supplied publication timestamp, not from the date a listing first entered the database. Missing, invalid, and future timestamps are excluded until verified. Age is rechecked during reads, so cached results can expire between scheduled scans.

Education matching uses text and heading rules to distinguish requirements, alternatives, explicit no-degree statements, and optional qualifications. The latest user policy excludes degree-or-experience alternatives even when the employer might accept experience. This is a user preference, not a universal employment rule.

A reassessment utility applies the revised selection rules to saved technical assessments under a new context. The documented migration created new assessment records while retaining prior versions; it did not require a batch of paid AI calls. The text classifier remains heuristic, not a complete multilingual interpretation engine.

## Application documents

The companion asks the model to select supplied fact IDs and extract verbatim requirements. Preparation rejects unsupported facts, missing evidence for a claimed match, and quotes absent from the saved description.

A configured reference fixes the header and relevant-experience content. Required projects must remain represented, with one selected bullet for each in reference mode. Tailoring changes the emphasis and selection of verified evidence within those constraints. Application messages combine approved facts with role and company context through templates.

Chromium renders HTML/CSS into PDF. The package writer extracts PDF text with pypdf, checks expected content, and enforces a single page when reference mode is configured. A manifest associates the package with candidate version, job hash, document version, and PDF digest. Reusing or opening an artifact includes integrity checks. These controls demonstrate content and layout validation, not universal ATS parsing compatibility.

## Browser workflow and human handoff

Playwright uses persistent browser storage scoped to candidate and site. Form handling supports explicit recipes, saved answers, résumé attachment, and targeted handling of supported provider behavior. The review interface streams Chromium frames and forwards ordered batches of user input to the browser-owning thread. Only one interactive session is permitted at a time.

Upload handling verifies the expected application workflow and intended PDF before authorizing supported storage writes. It is not a general permission to write to arbitrary storage destinations. CAPTCHA and email challenges remain human intervention points in assisted operation.

The user can download the prepared résumé and open the employer's public form on their own device. That starts a separate browser session; it does not transfer the remote session or guarantee that fields will already be populated.

## Persistence and recovery

SQLite uniqueness constraints prevent duplicate candidate/opportunity entries. The ledger records state changes and submission intent before an external final action. Startup recovery treats interrupted submissions as uncertain, while interrupted preparation can be queued again. Confirmation and provider-rejection evidence are retained separately from the fact that an attempt occurred.

This is conservative duplicate prevention, not a distributed exactly-once delivery guarantee. Network errors after an external write require reconciliation or human investigation. Gmail code can search sent mail by message identifier; sending is guarded and not automatically retried.

Mailbox processing persists cursors and processed message identifiers. OAuth implements PKCE, state validation, limited authorization lifetime, token refresh, and scope checks. Credentials are external to source configuration and artifact content intended for publication.

## Security and maintainability

- Administrative, read-only research, and private review access are separated.
- Review actions use authenticated sessions and origin checks.
- External destinations, redirect behavior, response sizes, and browser operations are restricted in code.
- Containers run as non-root users with read-only root filesystems, dropped capabilities, resource limits, and persistent data volumes.
- Dependencies are recorded in lock files; tests use temporary databases, mocked providers, and real Chromium against synthetic forms.

These are implemented controls rather than a claim of independent security certification or a completed penetration test. The project favors small modules and explicit state over a queue cluster, orchestration platform, or general-purpose browser agent.
