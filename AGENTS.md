# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-009-dependence-composition-consolidation.md`
- `docs/concepts/index.md`
- `docs/dependence/index.md`
- `docs/synchronizations/index.md`
- `docs/phases/009/index.md`

Current state:

```text
accepted concepts                    11
current desired outcomes             16
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
009-A..009-H                         COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            NEXT ELIGIBLE
Phase 010 decomposition              NOT YET PERFORMED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Phase 009 consolidated authority

Phase 009 is complete enough for Phase 010.

Current application-family kernels:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Current synchronization inventory:

```text
required-relational                    6
capability/occurrence conditional      7
SYNC-08                                RETIRED — Generation-local output lifecycle
SYNC-15                                RECLASSIFIED — Reproducibility Contract
SYNC-16                                NOT JUSTIFIED
```

`SYNC-06` remains conditional Generation/Learned State reuse.

Canonical cross-sync ownership:

```text
consumer exact binding / contextual assessment
  -> Learning / Generation / Evaluation

Learned State producer identity
  -> Learned State

Evidence producer identity
  -> Evidence

Execution parent binding + Attempts/retry/recovery
  -> Execution

Provenance typed relationship assertions
  -> Provenance

synchronization-owned canonical state
  -> NONE
```

Synchronization is occurrence-scoped, not a permanent live subscription.

```text
new Data Meaning revision  != rewrite committed activity
Strategy retirement        != rewrite historical activity
Constraint revision        != rewrite prior binding
Learned State retirement   != mutate prior Generation history
Criterion revision         != reinterpret historical Evidence
Evidence invalidation      != silently rewrite historical Generation completion
Provenance correction      != rewrite source history
```

## Critical application-family rules

- direct Generation is valid without Learning/Learned State;
- non-gated Generation is valid without Evaluation/Evidence;
- Constraint remains optional unless reusable prescriptive-rule capability is claimed;
- Execution remains optional unless durable operational realization is claimed;
- Provenance remains optional unless typed cross-concept history capability is claimed;
- SCC co-inclusion does not imply concept or architecture merger;
- conditional synchronization does not create universal inclusion dependence.

## Current Phase 010 boundary

**Phase 010 — Concept Mapping, Interaction, Linguistic & Experience Alignment** is next eligible.

Do not execute Phase 010 before first decomposing it into dependency-safe design subgroups using the completed Phase 009 handoff.

Phase 010 owns:

```text
F1  concept action -> human/programmatic interaction mapping
F2  concept state/query -> actor-visible inspection mapping
F3  linguistic mapping / vocabulary alignment
F4  physical/interaction mapping across relevant surfaces
F5  human/programmatic semantic parity
```

## Phase 010 mapping guardrails

Mapping MUST preserve current semantics and must not collapse:

```text
Learning / Generation / Evaluation -> generic Run
Learned State / Generation output / Evidence -> generic Artifact
Data Meaning / Constraint -> generic Rule or Schema
Evaluation Criterion / Evaluation / Evidence -> generic Metric
Execution / domain activity -> generic Job
Evidence / external decision -> generic Approval status
Provenance / source fact -> generic History owner
```

Mapping must preserve:

- application-family optionality;
- direct vs learned Generation;
- partial/candidate/awaiting-validation/completed Generation state;
- semantic vs operational completion;
- Criterion/Evaluation/Evidence distinctions;
- Evidence vs approval/release/privacy guarantee;
- Provenance relationship authority vs source ownership;
- exact historical binding inspectability;
- current status vs historical status;
- occurrence-scoped synchronization;
- human/programmatic semantic parity.

A concise representation is allowed. Semantic distinctions must remain recoverable and actor-understandable.

If mapping exposes a genuine concept/dependence/composition misfit, reopen the smallest affected upstream authority under J0-J7 rather than papering over the distinction.

## Critical interpretation

A concept, synchronization, mapping, composition plane, or synergy path is not automatically:

- a service call;
- an event/message;
- a transaction/saga;
- a queue/topic;
- an API endpoint;
- a package/module dependency;
- a schema foreign key;
- a workflow edge;
- a deployment unit;
- an observer/subscription mechanism.

Do not translate current design authority directly into implementation topology.

## Stop/reopen discipline

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → Phase 009 authority;
- mapping defect that does not prove an upstream issue → Phase 010.

Do not reopen completed authority merely to align with existing implementation structure.

## What agents may do now

Agents may decompose Phase 010 immediately before entry and then perform design-only concept mapping work.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not as upstream concept/mapping authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, event/service decomposition, or executable architecture restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 010-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**Phase 010 — Concept Mapping, Interaction, Linguistic & Experience Alignment**.

Decompose immediately before entry. Do not begin implementation work.
