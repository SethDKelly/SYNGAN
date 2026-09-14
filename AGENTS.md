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
- `docs/mapping/concept-action-actor-intent-interaction-mapping.md`
- `docs/mapping/concept-state-query-history-explanation-inspection-mapping.md`
- `docs/phases/010/index.md`

Current state:

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                COMPLETE
010-D                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   CURRENTLY CLOSED
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current mapping authority

010-A defines the mapping schema/coverage/actor/surface/family/evidence model.

010-B maps all 66 normalized command groups to actor intent and surface-neutral interaction obligations.

010-C maps all 52 normalized query groups, all 11 lifecycle/history envelopes and five cross-concept explanation patterns to surface-neutral inspection obligations.

```text
commands                         66 / 66 SEMANTICALLY MAPPED
queries                          52 / 52 SEMANTICALLY MAPPED
lifecycle/history envelopes      11 / 11 SEMANTICALLY MAPPED
F1                               CURRENTLY CLOSED
F2                               CURRENTLY CLOSED
```

## Inspection discipline

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

Do not turn a combined view, cache, report, dashboard, history index, graph traversal or status summary into new canonical domain state.

Preserve:

- current versus exact historical state;
- semantic versus operational state;
- candidate/checkpoint/diagnostic versus authoritative result;
- exact Meaning/Strategy/Constraint/Learned State/Criterion/Evidence bindings;
- Evidence finding/strength/uncertainty/limitations/current applicability;
- Provenance relationship assertions versus referenced source facts;
- directly retained versus reconstructed/partial/unavailable/indeterminate history;
- visible/redacted/withheld/unavailable/unknown/absent disclosure distinctions;
- bounded enterprise-scale inspection;
- application-family optionality.

## Current Phase 010 sequence

```text
010-A  COMPLETE — mapping control / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — action -> actor intent / interaction mapping
010-C  COMPLETE — state/query/history/explanation -> inspection mapping
010-D  NEXT — linguistic / vocabulary / typed status / disclosure semantics
010-E  physical interaction across candidate surface families
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  mapping consolidation / Phase 011 handoff
```

## 010-D discipline

010-D must align vocabulary and typed status/disclosure language across actors and programmatic surfaces without changing mapped semantics.

Pay particular attention to overloaded or risky words such as:

```text
model
run
job
artifact
metric
validation
valid
passed
ready
quality
safe
private
reproducible
history
current
complete
```

Do not use one generic status vocabulary to erase concept-owner differences.

010-C semantic categories such as `DIRECT`, `RECONSTRUCTED`, `PARTIAL`, `WITHHELD`, `UNKNOWN` or `ABSENT` are mapping distinctions awaiting linguistic alignment. They are not permission to create public/runtime enums.

## Mapping misfit rule

If a mapping cannot be expressed intelligibly without violating purpose, ownership, application-family or synchronization semantics:

1. record the concrete mapping misfit;
2. identify whether it is local to Phase 010 or proves an upstream defect;
3. reopen only the smallest affected authority under J0-J7.

Do not invent generic Workflow, Run, Artifact, Metric, Validation, Quality, History, Status, Lineage or Approval authority merely to simplify a surface.

## Critical interpretation

A concept mapping is not automatically:

- a public class/method;
- endpoint/resource schema;
- CLI command;
- UI widget/page;
- report format;
- database/materialized view;
- cache/search index;
- graph database;
- service call;
- event/message;
- transaction/saga;
- queue/topic;
- package/module dependency;
- runtime workflow edge;
- deployment unit.

## Stop/reopen discipline

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → Phase 009 authority;
- mapping defect without upstream proof → Phase 010.

## What agents may do now

Agents may perform design-only 010-D linguistic mapping using current action/inspection mappings and terminology authority.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not upstream mapping authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, query endpoints, dashboards/materialized views, graph/search technologies, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, event/service decomposition, or executable architecture restrictions merely to freeze evolving design.

## Readiness rule

Phases 010-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**010-D — Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics**.
