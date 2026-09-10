# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/problem/index.md`
- `docs/concepts/index.md`
- `docs/concepts/state-identity-history-invariant-normalization.md`
- `docs/concepts/action-query-lifecycle-normalization.md`
- `docs/concepts/operational-principle-purpose-counterexample-normalization.md`
- `docs/concepts/independence-genericity-familiarity-reuse-normalization.md`
- `docs/phases/008/index.md`

Phase 007 architecture is downstream evidence only until Phase 013 reconciliation.

Current state:

```text
accepted concepts          11
accepted synchronizations  15
current desired outcomes   16
Phase 008                  ACTIVE
008-A                      COMPLETE
008-B                      COMPLETE
008-C                      COMPLETE
008-D                      COMPLETE
008-E                      COMPLETE
008-F                      COMPLETE
008-G                      NEXT ELIGIBLE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or implementation plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current individual-concept authority

Phase 008 has current authority for:

```text
008-B  purpose / justification
008-C  state / identity / history / invariants
008-D  actions / queries / transitions
008-E  operational principles / counterexamples
008-F  independence / genericity / familiarity / reuse
```

008-F establishes:

```text
independence != isolation
reuse        != universal presence
familiarity  != copying another product/object model
genericity   != generic infrastructure
```

All eleven accepted concepts pass the current independence/genericity/familiarity/reuse review and all eleven names are retained. That is **not** catalog finality.

## Current Phase 008 boundary

```text
008-A  COMPLETE — Methodology Authority Reset, Completion Matrix & Design-Only Guardrails
008-B  COMPLETE — Problem, Purpose, Outcome & Concept-Justification Traceability Revalidation
008-C  COMPLETE — Concept State Model, Identity, History & Invariant Normalization
008-D  COMPLETE — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure
008-E  COMPLETE — Operational Principle Completeness, Purpose Fulfillment & Counterexample Review
008-F  COMPLETE — Independence, Genericity, Familiarity & Reuse Revalidation
008-G  NEXT ELIGIBLE — Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit
008-H  PLANNED — Phase 008 Consolidation & Phase 009 Handoff
```

008-G must deliberately re-evaluate every rejected, subordinated, deferred, externalized or representation-classified candidate using the **current** 008-B through 008-F criteria. Do not merely restate Phase 001 dispositions.

A candidate may become accepted only if it now has a distinct problem-facing purpose, meaningful state/history, concept-owned actions/queries, an operational principle, independence, appropriate genericity and a clean authority boundary. A class/table/file/job/API/manifest/runtime role is not sufficient evidence.

Candidates explicitly requiring rediscovery include at least:

- Generation Request and Condition;
- Attempt / Checkpoint / Retry / cancellation-related candidates;
- Dataset / Artifact identity;
- Reproducibility;
- mechanism-specific privacy state/guarantee;
- Relationship / topology-related candidates;
- Use / Release Decision;
- Source Characterization / Profile;
- Resource / Admission / Backpressure / Approximation / Degraded Mode / Cost / Quota-like candidates;
- umbrella terms such as Validation, Metric, Quality, Model, Metadata, Run, Artifact and Synthesizer.

Do not promote any candidate for catalog symmetry or because retained architecture already has an object for it.

## Jackson distinctions to preserve

- purpose explains why a concept exists;
- operational principles demonstrate purpose but do not replace complete state/action specification;
- actions/queries define conceptual behavior independent of interface mechanisms;
- synchronizations compose independently defined concepts without transferring state ownership;
- concept dependence means application inclusion dependence, not import/reference/runtime dependency;
- concept mapping is downstream of concept behavior and must preserve it;
- specificity, familiarity and integrity are design criteria, not implementation metrics.

## Stop/reopen classes

Follow J0-J7 in the completion matrix. Reopen the smallest affected upstream authority for a real defect; do not patch a conceptual defect only in architecture/code/tests.

## What agents may do now

For 008-G, agents may inspect historical discovery and later design evidence, re-run candidate criteria, refine the catalog or boundaries when genuinely justified, and record why candidates remain rejected/subordinate/deferred/external/representation-only.

Architecture/source/tests may be inspected only as feasibility or misfit evidence, not as authority over unfinished concepts.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, runtime/build dependencies for future capability, package-topology changes, or executable architecture/fitness restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 008-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision. Even then, implementation itself requires a later explicit Phase 015.

## Current next boundary

**008-G — Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit**.

Do not begin implementation work.
