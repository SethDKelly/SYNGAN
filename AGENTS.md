# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/phases/008/index.md`
- relevant canonical problem/concept/synchronization/experience authority
- Phase 007 architecture only when it supplies downstream evidence or a design counterexample

Current state:

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
Phase 008                  ACTIVE
008-A                      COMPLETE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or implementation plans may expose misfits, but they may not veto upstream concept-design correction.**

The 007-K bounded implementation-reentry conclusion is superseded as premature. Its architecture/scaffold findings remain historical/downstream evidence.

## Methodology completion matrix

The canonical `docs/authority/jackson-methodology-completion-matrix.md` is the current ledger for remaining design obligations.

Do not infer methodology completion from historical `complete` phase labels. Use the matrix state and owning closure phase.

Artifact roles are:

- Class A — current upstream design authority;
- Class B — supporting design evidence;
- Class C — downstream architecture evidence pending reconciliation;
- Class D — historical implementation-planning/executable evidence.

Class C/D may reveal a misfit. They may not silently define unfinished Class A behavior.

## Current design roadmap

```text
008  Individual Concept Design Normalization & Completeness
009  Concept Dependence, Application Family, Composition & Synchronization Closure
010  Concept Mapping, Interaction, Linguistic & Experience Alignment
011  Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Design Validation
012  Jackson Concept-Design Consolidation & Completion Decision
013  Post-Concept Representation & Architecture Reconciliation
014  Whole-Design Consolidation, Residual Debt Audit & Implementation-Readiness Decision
---
015  Implementation Authority & Controlled Delivery — FUTURE ONLY
```

Only the current high-level phase is decomposed in advance. Phases 009-014 must be divided into dependency-safe subgroups immediately before they start.

## Current Phase 008 boundary

```text
008-A  COMPLETE — Methodology Authority Reset, Completion Matrix & Design-Only Guardrails
008-B  NEXT ELIGIBLE — Problem, Purpose, Outcome & Concept-Justification Traceability Revalidation
008-C  PLANNED — Concept State Model, Identity, History & Invariant Normalization
008-D  PLANNED — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure
008-E  PLANNED — Operational Principle Completeness, Purpose Fulfillment & Counterexample Review
008-F  PLANNED — Independence, Genericity, Familiarity & Reuse Revalidation
008-G  PLANNED — Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit
008-H  PLANNED — Phase 008 Consolidation, Individual-Concept Completeness Decision & Phase 009 Handoff
```

008-H does not declare Jackson concept design complete; it only decides whether individual concepts are ready for cross-concept dependence/composition work.

## Jackson methodology distinctions agents must preserve

- purpose explains why each concept exists;
- operational principles demonstrate how the concept fulfills its purpose;
- conceptual state/actions/queries specify behavior independently of interface mechanisms;
- actions are conceptual acts, not buttons, endpoints, jobs or implementation functions;
- concepts are independently understandable functional units, not classes/services/objects by default;
- synchronizations compose concept actions without transferring state ownership;
- **concept dependence means inclusion dependence in this application**, not import/reference/runtime dependency;
- valid concept subsets/application families must eventually respect inclusion dependence;
- concept mapping connects state/actions/queries to physical and linguistic interaction surfaces without redefining concept semantics;
- specificity, familiarity and integrity are design criteria, not implementation metrics;
- misfits discovered from architecture or implementation planning must reopen the smallest affected upstream design authority.

## Stop/reopen classes

Follow the J0-J7 classes in the completion matrix:

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

For explicitly entered design subgroups, agents may inspect repository evidence, refine current design documents within the subgroup's authority, record alternatives/counterexamples/misfits, and revise upstream design when justified.

Downstream architecture may be used as feasibility or counterexample evidence without becoming upstream authority.

## What agents must not do until Phase 014 passes

Do not:

- add production behavior;
- add or expand public implementation APIs;
- add persistence/data-plane schemas or migrations;
- add Spark/runtime/model/platform/security adapters;
- add Execution/recovery/fencing/checkpoint/admission implementations;
- add Evidence/Provenance/history/query implementations;
- add reference Strategy/vertical-slice implementation;
- add runtime/build dependencies for future capability work;
- add new executable architecture/fitness restrictions merely to freeze evolving design;
- modify package topology because a future architecture seems likely;
- repair stale implementation tests solely to make implementation appear ready;
- start Phase 015 or any implementation tranche.

Existing `src/syngan`, tests, Import Linter rules, tooling and CI may remain as historical/provisional evidence.

## Readiness rule

Phases 008-013 always retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final full-design readiness decision.

If Phase 014 passes, the allowed state is:

```text
READY / NOT STARTED / NEXT
```

That state still requires an explicit future Phase 015 before implementation begins.

## Current next boundary

**008-B — Problem, Purpose, Outcome & Concept-Justification Traceability Revalidation** is the next eligible subgroup.

Do not begin implementation work.