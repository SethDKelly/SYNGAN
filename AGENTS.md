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
- `docs/concepts/catalog-perimeter-candidate-rediscovery-boundary-audit.md`
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
008-G                      COMPLETE
008-H                      NEXT ELIGIBLE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or implementation plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current individual-concept authority

Phase 008 now has current authority for:

```text
008-B  purpose / justification
008-C  state / identity / history / invariants
008-D  actions / queries / transitions
008-E  operational principles / counterexamples
008-F  independence / genericity / familiarity / reuse
008-G  rejected/deferred candidate rediscovery / catalog perimeter
```

008-F establishes:

```text
independence != isolation
reuse        != universal presence
familiarity  != copying another product/object model
genericity   != generic infrastructure
```

008-G establishes that a useful/durable/typed/identified architecture object is not a concept unless it has an independent current product purpose, state/history, owned behavior, operational principle and clean boundary.

Current catalog result:

```text
accepted concepts          11
restored concepts           0
new concepts                0
missing current concept     NONE FOUND
```

Important 008-G dispositions to preserve:

- Generation Request / Condition remain Generation-owned;
- Attempt / Checkpoint remain Execution-owned/subordinate;
- Artifact/Dataset identity remains representation/integration;
- Reproducibility remains cross-cutting;
- Relationship remains Data Meaning-owned descriptive structure;
- generic Privacy remains rejected; future composable DP requires fresh mechanism-specific concept discovery;
- Use / Release Decision remains external authority;
- Resource/Admission/Backpressure/Approximation/DegradedMode/Cost remain owner-specific, cross-cutting or deployment policy;
- Synthetic Output remains Generation-owned result state until independent output lifecycle functionality exists;
- Source/Dependency/Authorization/Secret/Platform Capability remain context/security/architecture rather than synthetic-data concepts;
- Text/Tokenizer/Language Model and topology-mode words do not become concepts merely because implementations may represent them;
- umbrella terms such as Model, Run, Quality, Metadata, Validation, Artifact, Synthesizer and Policy must not erase accepted boundaries.

Future rediscovery triggers are not implementation permission.

## Current Phase 008 boundary

```text
008-A  COMPLETE — Methodology Authority Reset, Completion Matrix & Design-Only Guardrails
008-B  COMPLETE — Problem, Purpose, Outcome & Concept-Justification Traceability Revalidation
008-C  COMPLETE — Concept State Model, Identity, History & Invariant Normalization
008-D  COMPLETE — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure
008-E  COMPLETE — Operational Principle Completeness, Purpose Fulfillment & Counterexample Review
008-F  COMPLETE — Independence, Genericity, Familiarity & Reuse Revalidation
008-G  COMPLETE — Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit
008-H  NEXT ELIGIBLE — Phase 008 Consolidation, Individual-Concept Completeness Decision & Phase 009 Handoff
```

008-H must consolidate rather than invent new downstream work. It must verify that all individual-concept obligations are currently closed with no unresolved J1/J2 blocker, record any residual reopen trigger/debt, and decide only whether the individual-concept foundation is complete enough for Phase 009.

A positive 008-H may state only:

```text
INDIVIDUAL CONCEPT DESIGN   COMPLETE ENOUGH FOR PHASE 009
IMPLEMENTATION READINESS    NOT READY
IMPLEMENTATION START        NOT STARTED
IMPLEMENTATION NEXT         NOT YET
```

Do not subdivide Phase 009 until 008-H positively hands off. When Phase 009 becomes eligible, divide it immediately before entry using the final Phase 008 evidence.

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

For 008-H, agents may inspect and consolidate Phase 008 evidence, identify conflicts/residual gaps and reopen the smallest affected 008 subgroup if a genuine blocker is found.

Architecture/source/tests may be inspected only as feasibility or misfit evidence, not as authority over unfinished concepts.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies for future capability, package-topology changes, or executable architecture/fitness restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 008-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision. Even then, implementation itself requires a later explicit Phase 015.

## Current next boundary

**008-H — Phase 008 Consolidation, Individual-Concept Completeness Decision & Phase 009 Handoff**.

Do not begin implementation work.
