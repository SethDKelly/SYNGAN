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
- `docs/concepts/phase-008-individual-concept-consolidation.md`
- `docs/phases/008/index.md`

Phase 007 architecture is downstream evidence only until Phase 013 reconciliation.

Current state:

```text
accepted concepts          11
accepted synchronizations  15
current desired outcomes   16
Phase 008                  COMPLETE
individual concept design  COMPLETE ENOUGH FOR PHASE 009
Phase 009                  NEXT ELIGIBLE / NOT YET DECOMPOSED
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or implementation plans may expose misfits, but they may not veto upstream concept-design correction.**

## Phase 008 authority to preserve

Phase 008-A through 008-H provide current authority for:

```text
problem / purpose / outcomes / concept justification
concept state / identity / history / invariants
concept actions / queries / transition contracts
operational principles / counterexamples
independence / genericity / familiarity / reuse
candidate rediscovery / catalog perimeter
individual-concept consolidation
```

The catalog remains eleven concepts/fifteen synchronizations with no Phase 008 add/remove/restore/merge/split/rename.

Core distinctions include:

```text
Data Meaning          != Constraint
Synthesis Strategy    != implementation/plugin/runtime
Learning              != Learned State
Learning/Generation/
Evaluation             != Execution
Generation Condition  != Constraint
Evaluation Criterion  != Evaluation != Evidence
Evidence               != Provenance
Execution              != Attempt != platform job
```

Generation currently owns the completed logical synthetic-output result boundary. Relationship remains Data Meaning-owned descriptive structural semantics. Generic Privacy remains rejected; future mechanism-specific capabilities such as composable DP require fresh concept discovery before implementation. Use/Release Decision remains external authority.

## Current Phase 009 boundary

**Phase 009 — Concept Dependence, Application Family, Composition & Synchronization Closure** is next eligible.

Phase 009 has not yet been subdivided. Immediately before Phase 009 begins, derive dependency-safe subgroups from the completed Phase 008 authority and remaining methodology D/E obligations.

Phase 009 must explicitly distinguish:

- **Jackson inclusion dependence** — including concept C1 only makes sense if C2 is also included;
- reference dependency;
- validation/compatibility dependency;
- production/result-establishment dependency;
- operational/runtime realization dependency;
- authority dependency;
- provenance/historical relationship.

Existing non-Jackson dependency taxonomies are supporting evidence only.

At minimum Phase 009 must close or deliberately hand forward:

- D1 — application inclusion-dependence graph;
- D2 — meaningful valid concept subsets/application family;
- D3 — dependence-derived explanation/design ordering;
- D4 — reduced-application add/remove consequences;
- E1-E3 — synchronization ownership/economy/hidden-coordinator closure;
- the Phase 009 portion of E4/E5 — composition synergy/integrity.

Do not assume the existing fifteen synchronizations are final merely because 008-D can express them using owned actions/queries. Phase 009 must replay composition under the actual application-family/dependence model.

Do not introduce a new concept or hidden coordinator merely to make composition convenient. A genuine J2/J3 misfit must reopen the smallest affected upstream authority.

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

Before starting Phase 009, agents may inspect the completed Phase 008 authority and remaining D/E methodology obligations to define dependency-safe Phase 009 subgroups.

Once Phase 009 is explicitly entered, agents may perform design-only inclusion-dependence, application-family, composition and synchronization analysis within those subgroups.

Architecture/source/tests may be inspected only as feasibility or misfit evidence, not as authority over unfinished design.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies for future capability, package-topology changes, or executable architecture/fitness restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision. Even then, implementation itself requires a later explicit Phase 015.

## Current next boundary

**Phase 009 — Concept Dependence, Application Family, Composition & Synchronization Closure**.

Define its subgroups immediately before entry. Do not begin implementation work.
