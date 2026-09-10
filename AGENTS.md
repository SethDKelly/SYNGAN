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
008-D                      NEXT ELIGIBLE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or implementation plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current concept-state authority

008-C established five intentional state-shape families:

```text
reusable revisioned authorities  Data Meaning / Strategy / Constraint / Criterion
committed domain activities      Learning / Generation / Evaluation
durable established results     Learned State / Evidence
operational realization          Execution
typed historical relationships  Provenance
```

Agents must preserve these distinctions and must not normalize them into one generic lifecycle merely for implementation convenience.

Also preserve:

- lineage identity != semantic revision != activity occurrence != result identity != current-use status;
- material historical meaning is non-destructive;
- current eligibility/applicability is separate from historical fact;
- contextual compatibility/applicability remains contextual;
- unknown/indeterminate state stays explicit where false certainty would matter;
- physical durability != semantic establishment/completion;
- operational completion != domain completion;
- restored historical persistence does not itself restore current conceptual authority;
- bulk rows/tasks/logs are not canonical control-plane concept state by default.

## Current Phase 008 boundary

```text
008-A  COMPLETE — Methodology Authority Reset, Completion Matrix & Design-Only Guardrails
008-B  COMPLETE — Problem, Purpose, Outcome & Concept-Justification Traceability Revalidation
008-C  COMPLETE — Concept State Model, Identity, History & Invariant Normalization
008-D  NEXT ELIGIBLE — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure
008-E  PLANNED — Operational Principle Completeness, Purpose Fulfillment & Counterexample Review
008-F  PLANNED — Independence, Genericity, Familiarity & Reuse Revalidation
008-G  PLANNED — Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit
008-H  PLANNED — Phase 008 Consolidation & Phase 009 Handoff
```

008-D must reason about conceptual actions and state-observing queries. Do not convert buttons, HTTP methods, Python functions, Spark jobs, database transitions, scheduler events or manifest operations into concept actions merely because they are implementation candidates.

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

For an explicitly entered design subgroup, agents may inspect repository evidence, refine current design authority within that subgroup, record counterexamples/misfits, and revise upstream design when justified.

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

**008-D — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure**.

Do not begin implementation work.