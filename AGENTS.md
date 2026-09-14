# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 010 concept mapping is active.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-009-dependence-composition-consolidation.md`
- `docs/mapping/index.md`
- `docs/mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md`
- `docs/phases/010/index.md`
- `docs/phases/010/010-A-mapping-authority-coverage-model-actor-surface-taxonomy-evidence-baseline.md`
- `docs/experience/phase-003-consolidated-experience-contract.md`
- `docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md`

Current state:

```text
accepted concepts                    11
current desired outcomes             16
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                NEXT ELIGIBLE
F1                                   PARTIAL
F2                                   PARTIAL
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Phase 009 upstream authority

Phase 009 is complete enough for current mapping work.

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Current synchronization inventory:

```text
required-relational                    6
capability/occurrence conditional      7
SYNC-08                                RETIRED
SYNC-15                                RECLASSIFIED — Reproducibility Contract
SYNC-16                                NOT JUSTIFIED
```

Critical upstream rules:

- direct Generation is valid without Learning/Learned State;
- non-gated Generation is valid without Evaluation/Evidence;
- Constraint, Execution and Provenance remain capability-conditional;
- synchronization owns no canonical state;
- consumer activities own exact bindings/contextual assessments;
- Execution owns operational realization, not domain completion;
- Evidence owns findings, not approval/release or Generation completion;
- Provenance owns typed relationships, not source facts;
- synchronization is occurrence-scoped, not a permanent reactive subscription.

## 010-A mapping-control authority

010-A is complete and governs all later mapping work.

Every mapping record must preserve, where material:

```text
concept owner
conceptual action/query/state subject
actor intent / need
surface-neutral interaction / inspection obligation
semantic precondition and result semantics
non-success / uncertainty semantics
application-family applicability
synchronization relevance
temporal orientation
disclosure state
historical-knowledge state
scale / boundedness
candidate surface families
linguistic risk
evidence source
coverage status
misfit / reopen note
```

The controlled mapping progression is:

```text
SOURCE IDENTIFIED
  -> SEMANTICALLY MAPPED
  -> LINGUISTICALLY ALIGNED
  -> SURFACE-MAPPED
  -> FAMILY-REPLAYED
  -> PARITY-VALIDATED
```

`BLOCKED BY MISFIT` remains explicit when honest mapping is impossible.

These are documentation/mapping states, not runtime/domain states.

## Actor and surface taxonomies

Actor roles:

```text
A1 Data Practitioner
A2 Synthetic Data Consumer
A3 Data Owner / Steward
A4 Privacy / Risk / Governance Reviewer
A5 Platform Operator
A6 Library Maintainer
A7 Synthesizer / Extension Author
```

Surface families:

```text
S1 SDK / API automation
S2 notebook / interactive analysis
S3 CLI / operational interaction
S4 report / history / review artifact
S5 graphical UI
S6 operator / admin surface
S7 external integration / handoff
```

Actor roles are need/viewpoint categories, not permission models. Surface families are mapping lenses, not architecture components.

## Application-family mapping tags

Use the current tags rather than assuming full-suite workflow:

```text
AF-AUTH  authority-only usage
AF-L     L-KERNEL
AF-GD    direct Generation
AF-GL    learned-state-assisted Generation
AF-E     E-KERNEL / evaluation-focused use
AF-GE    evidence-gated Generation
AF-C     reusable Constraint present
AF-X     durable Execution present
AF-P     Provenance present
AF-FULL  full eleven-concept composition
AF-EXT   external integration/handoff
```

Do not turn these into product SKUs, packages, deployment profiles or feature flags.

## Active Phase 010 sequence

```text
010-A  COMPLETE — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  NEXT — action -> actor intent / interaction mapping
010-C  state/query/history -> inspection mapping
010-D  linguistic / vocabulary / typed status / disclosure semantics
010-E  physical interaction across candidate surface families
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  mapping consolidation / Phase 011 handoff
```

The sequence is strict by default.

## 010-B discipline

010-B maps every normalized state-changing action to actor intent and **surface-neutral** interaction obligations.

It may advance an action from `SOURCE IDENTIFIED` to `SEMANTICALLY MAPPED` only when the record preserves:

- canonical concept owner;
- current precondition/effect/postcondition semantics;
- principal/secondary actor needs;
- application-family applicability;
- synchronization relevance without synchronization-owned controls;
- temporal/disclosure/history/scale annotations where material;
- explicit non-success/indeterminate behavior.

010-B must not yet choose final actor-facing terminology or concrete controls/endpoints. Those belong to 010-D/E.

## Concept distinctions mapping must preserve

Do not collapse:

```text
Learning / Generation / Evaluation -> generic Run
Learned State / Generation output / Evidence -> generic Artifact
Data Meaning / Constraint -> generic Rule or Schema
Evaluation Criterion / Evaluation / Evidence -> generic Metric
Execution / domain activity -> generic Job
Evidence / external decision -> generic Approval status
Provenance / source fact -> generic History owner
```

Also preserve:

- direct vs learned Generation;
- partial/candidate/awaiting-validation/completed Generation state;
- semantic vs operational completion;
- exact historical bindings vs current status;
- Evidence claim strength/limitations/applicability;
- absent/unknown/unavailable/withheld/redacted disclosure distinctions;
- current vs reconstructed/incomplete historical knowledge;
- enterprise-scale bounded inspection;
- human/programmatic material semantic parity.

## Historical experience evidence rule

Phase 003 and Phase 006 experience documents are strong supporting evidence, not automatically complete current F1-F5 mapping authority.

010-A has already normalized stale assumptions:

```text
15 historical SYNC IDs != 15 active rules
SYNC-08 is retired
SYNC-15 is reclassified
Learning is not universal for Generation
Evaluation/Evidence are not universal for Generation
Execution is not universal
Provenance is not universal
Readiness/Validation are not global concept owners
```

Current Phase 008/009 authority wins where older workflow wording conflicts.

## Mapping misfit rule

If an accepted concept/action/query cannot be mapped intelligibly without violating purpose, ownership, application-family or synchronization semantics:

1. record the concrete mapping misfit;
2. identify whether it is local to Phase 010 or proves an upstream defect;
3. reopen only the smallest affected authority under J0-J7.

Do not invent generic Workflow, Run, Artifact, Metric, Validation, Quality, History or Approval authority merely to simplify an interface.

## Critical interpretation

A concept mapping is not automatically:

- a public class/method;
- an endpoint/resource schema;
- a CLI command;
- a UI widget/page;
- a report format;
- a service call;
- an event/message;
- a transaction/saga;
- a queue/topic;
- a package/module dependency;
- a schema foreign key;
- a runtime workflow edge;
- a deployment unit.

Do not translate current mapping work into implementation topology.

## Stop/reopen discipline

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → Phase 009 authority;
- mapping defect that does not prove an upstream issue → Phase 010.

## What agents may do now

For 010-B, agents may enumerate normalized concept actions and create surface-neutral actor-intent interaction mappings under the 010-A schema.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not upstream mapping authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, concrete implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, event/service decomposition, or executable architecture restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 010-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**010-B — Concept Action → Actor Intent & Interaction Mapping**.

Do not begin implementation work.
