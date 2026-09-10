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
- `docs/problem/concept-justification-traceability.md`
- `docs/phases/008/index.md`
- relevant canonical concept/synchronization/experience authority
- Phase 007 architecture only when it supplies downstream evidence or a design counterexample

Current state:

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
current desired outcomes   16
Phase 008                  ACTIVE
008-A                      COMPLETE
008-B                      COMPLETE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or implementation plans may expose misfits, but they may not veto upstream concept-design correction.**

The 007-K bounded implementation-reentry conclusion remains superseded. Its architecture/scaffold findings remain historical/downstream evidence.

## Current problem-purpose authority

008-B reconciled the upstream problem corpus. Agents must now preserve these current scope facts unless later explicit design authority changes them:

- supported structured-data capability target includes single-table, time-series, and multi-table shared-key generation;
- legitimate composite structured topology must remain representable;
- arbitrary recursive/cyclic graph synthesis is not a universal baseline guarantee;
- free-form/source-language text fields **inside structured data** are in scope;
- at least one supported baseline text-bearing path must be self-contained/source-derived or local without mandatory public pretrained model, hidden first-use download, or runtime inference service;
- general unstructured/free-standing text generation remains outside current scope;
- streaming/real-time serving remains outside the current baseline;
- synthetic origin never implies privacy or release approval.

These are problem/design commitments, not implementation or architecture permissions.

## Methodology completion matrix

Use `docs/authority/jackson-methodology-completion-matrix.md` as the current ledger. Historical `complete` phase labels do not automatically establish current methodology closure.

Artifact roles remain:

- Class A — current upstream design authority;
- Class B — supporting design evidence;
- Class C — downstream architecture evidence pending reconciliation;
- Class D — historical implementation-planning/executable evidence.

Class C/D may reveal a misfit. They may not silently define unfinished Class A behavior.

## Current Phase 008 boundary

```text
008-A  COMPLETE — Methodology Authority Reset, Completion Matrix & Design-Only Guardrails
008-B  COMPLETE — Problem, Purpose, Outcome & Concept-Justification Traceability Revalidation
008-C  NEXT ELIGIBLE — Concept State Model, Identity, History & Invariant Normalization
008-D  PLANNED — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure
008-E  PLANNED — Operational Principle Completeness, Purpose Fulfillment & Counterexample Review
008-F  PLANNED — Independence, Genericity, Familiarity & Reuse Revalidation
008-G  PLANNED — Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit
008-H  PLANNED — Phase 008 Consolidation, Individual-Concept Completeness Decision & Phase 009 Handoff
```

008-B positively justified all eleven concepts at the full-product purpose level. Do **not** treat that as proof that every concept is independent, familiarly named, behaviorally complete, or required in every valid application subset.

## Jackson methodology distinctions agents must preserve

- purpose explains why each concept exists;
- operational principles demonstrate how the concept fulfills its purpose;
- conceptual state/actions/queries specify behavior independently of interface mechanisms;
- actions are conceptual acts, not buttons, endpoints, jobs or implementation functions;
- concepts are independently understandable functional units, not classes/services/objects by default;
- synchronizations compose concept actions without transferring state ownership;
- **concept dependence means inclusion dependence in this application**, not import/reference/runtime dependency;
- concept mapping connects state/actions/queries to physical and linguistic interaction without redefining semantics;
- specificity, familiarity and integrity are design criteria, not implementation metrics;
- downstream misfit evidence reopens the smallest affected upstream authority.

## Stop/reopen classes

Follow J0-J7 in the completion matrix:

- J0 editorial/non-semantic;
- J1 local concept specification gap;
- J2 purpose/boundary/catalog defect;
- J3 dependence/composition/synchronization defect;
- J4 concept-mapping/experience defect;
- J5 design-quality/misfit defect;
- J6 architecture reconciliation defect;
- J7 whole-design readiness defect.

Do not patch a higher-class conceptual defect only in downstream architecture/code/tests.

## What agents may do now

For explicitly entered design subgroups, agents may inspect repository evidence, refine current design documents within subgroup authority, record alternatives/counterexamples/misfits, and revise upstream design when justified.

For 008-C specifically, normalize conceptual state, identity, history, lifecycle and invariants independently of storage/schema/API/runtime representation. Phase 007 architecture may provide counterexamples but may not dictate concept state.

## What agents must not do until Phase 014 passes

Do not add production behavior; implementation APIs; persistence/data-plane schemas or migrations; Spark/runtime/model/platform/security adapters; Execution/recovery implementations; Evidence/Provenance/history implementations; reference Strategies/vertical slices; runtime/build dependencies for future capability; new executable architecture/fitness restrictions; package-topology changes; or stale-test repairs made merely to create implementation readiness.

Existing `src/syngan`, tests, Import Linter rules, tooling and CI remain historical/provisional evidence.

## Readiness rule

Phases 008-013 retain:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

Only Phase 014 may make the final whole-design readiness decision. If it passes, the allowed state is **READY / NOT STARTED / NEXT**, still requiring an explicit future Phase 015 before implementation begins.

## Current next boundary

**008-C — Concept State Model, Identity, History & Invariant Normalization** is the next eligible subgroup.

Do not begin implementation work.