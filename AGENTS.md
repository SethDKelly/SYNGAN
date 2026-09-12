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
- `docs/phases/010/index.md`
- `docs/phases/010/010-entry-decomposition.md`
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
Phase 010 decomposition              COMPLETE
010-A                                NEXT ELIGIBLE
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

## Active Phase 010 sequence

```text
010-A  NEXT — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  action -> actor intent / interaction mapping
010-C  state/query/history -> inspection mapping
010-D  linguistic / vocabulary / typed status / disclosure semantics
010-E  physical interaction across candidate surface families
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  mapping consolidation / Phase 011 handoff
```

The sequence is dependency-safe and strict by default.

## Mapping discipline

Use this order:

```text
concept semantics
  -> surface-neutral actor intent / inspection obligation
  -> linguistic mapping
  -> candidate physical interaction mapping
  -> application-family workflow composition
  -> human/programmatic parity and misfit audit
```

Do not begin from preferred classes, endpoints, commands, widgets, reports, pages or implementation resource types.

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

Replay them against Phase 008 normalized concepts and Phase 009 application-family/composition authority. If older workflow wording conflicts with current concept ownership or synchronization scope, current upstream authority wins and the stale experience statement must be reconciled in Phase 010.

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

Do not reopen completed authority merely to align with existing implementation structure.

## What agents may do now

For 010-A, agents may establish mapping-unit schema, coverage rules, actor-role mapping needs, surface-family taxonomy, evidence adoption/staleness register, application-family tags, history/disclosure/scale annotations and mapping-misfit rules.

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

**010-A — Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline**.

Do not begin implementation work.