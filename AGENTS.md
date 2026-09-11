# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/dependence/index.md`
- `docs/synchronizations/index.md`
- `docs/synchronizations/application-family-revalidation.md`
- `docs/synchronizations/trigger-ownership-normalization.md`
- `docs/phases/009/index.md`

Current state:

```text
accepted concepts                       11
historical synchronization IDs          15
active synchronizations                 13
required-relational                      6
capability/occurrence conditional        7
Phase 008                               COMPLETE
Phase 009                               ACTIVE
009-A                                   COMPLETE
009-B                                   COMPLETE
009-C                                   COMPLETE
009-D                                   COMPLETE
009-E                                   COMPLETE
009-F                                   COMPLETE
009-G                                   NEXT ELIGIBLE
D1-D4                                   CURRENTLY CLOSED
E1                                      CURRENTLY CLOSED
E2                                      CURRENTLY CLOSED
E3                                      PARTIAL TO STRONG
E4                                      PARTIAL
E5                                      STRONG EVIDENCE / REVALIDATION REQUIRED
Jackson design completion               IN PROGRESS
implementation readiness                NOT READY
implementation start                    NOT STARTED
implementation next                     NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current synchronization inventory

### Required-relational

```text
SYNC-01  Data Meaning revision binding
SYNC-02  Strategy selection and compatibility
SYNC-05  Learning produces Learned State
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-12  Evaluation produces Evidence
```

### Capability / occurrence conditional

```text
SYNC-03  Constraint binding and handling disposition
SYNC-04  Learning operational realization
SYNC-06  Generation / Learned State reuse compatibility and exact basis binding
SYNC-07  Generation operational realization
SYNC-11  Evaluation operational realization
SYNC-13  Generation / Evidence evidence-gated completion handoff
SYNC-14  Provenance recording at material transitions
```

`SYNC-06` is not active for direct Generation.

Historical IDs:

```text
SYNC-08  RETIRED — Generation-local output candidate/completion/promotion
SYNC-15  RECLASSIFIED — Reproducibility Contract
```

Do not reuse or resurrect them for numbering symmetry. No `SYNC-16` is justified.

## Canonical synchronization ownership

### Bindings / contextual assessments

The consuming activity owns exact bindings and contextual decisions.

Do not create canonical state such as:

```text
Strategy.compatibleWith[*]
Constraint.satisfiedBy[*]
LearnedState.compatibleWith[*]
Criterion.supportedByMethod[*]
Evidence.approves[*]
```

### Activity/result relation

```text
Learned State owns producing Learning identity
Evidence owns producing Evaluation identity
```

Learning/Evaluation own semantic completion. Reverse result lookup may be derived.

### Operational realization

Execution owns:

- exact parent Learning/Generation/Evaluation binding;
- Attempts;
- retry/resume/recovery/cancellation;
- operational progress/health/indeterminacy.

Domain activities own semantic lifecycle and MUST NOT duplicate Execution state.

### Provenance

Provenance owns typed relationship assertions only. It MUST NOT establish or alter the source facts it references.

### Synchronization

Synchronization owns **no canonical state**.

Do not create `Synchronization.status`, `Composition.status`, generic compatibility state, promotion state, or reproducibility state.

## Hidden-coordinator rule

009-F finds no current need for a generic:

- Compatibility / Validation / Readiness coordinator;
- Workflow / Run coordinator owning domain completion;
- Promotion / Artifact coordinator;
- Quality / Approval coordinator;
- coordinator above Provenance;
- Reproducibility concept/state owner;
- Composition/Synchronization state owner.

If future work appears to require one, treat that as a J2/J3 design signal, not permission to add infrastructure-shaped concept authority.

## Family replay

```text
L-KERNEL
  required: SYNC-01, SYNC-02, SYNC-05

G-KERNEL direct
  required: SYNC-01, SYNC-02
  SYNC-06 absent

learned-state-assisted Generation
  adds: SYNC-06

E-KERNEL
  required: SYNC-09, SYNC-10, SYNC-12
```

Constraint, Execution, Evidence-gating and Provenance synchronization activate only when the actual semantic relation occurs.

## Critical interpretation

A conceptual synchronization does **not** imply:

- an event/message;
- a transaction;
- a saga;
- a service call;
- a workflow engine edge;
- a database foreign key;
- a package dependency;
- a distributed lock;
- exactly-once execution.

Do not translate 009-F contracts into implementation topology.

## Current 009-G boundary

**009-G — Composition Economy, Coupling, Synergy & Integrity Closure** is next eligible.

009-G must evaluate the thirteen active rules together for:

- synchronization count/density and burden;
- remaining redundant coupling;
- interaction hot spots;
- conditional activation discipline;
- composition synergy;
- combined synchronization integrity;
- authority cycles/inversions under multi-rule activation;
- whether Provenance remains high fan-in / low authority fan-out;
- whether further simplification or upstream reopening is needed.

Do not begin Phase 010 mapping or implementation early.

## Stop/reopen discipline

Follow J0-J7 in the methodology matrix. Reopen the smallest affected upstream authority for a real defect.

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → Phase 009.

## What agents may do now

For 009-G, agents may analyze the normalized thirteen-rule composition graph and application-family variants for coupling/economy/synergy/integrity.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not composition authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, APIs, schemas, Spark/runtime/model/platform/security adapters, recovery implementations, synchronization services/events/transactions, package-topology changes, privacy mechanisms, or executable architecture restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**009-G — Composition Economy, Coupling, Synergy & Integrity Closure**.

Do not begin implementation work.