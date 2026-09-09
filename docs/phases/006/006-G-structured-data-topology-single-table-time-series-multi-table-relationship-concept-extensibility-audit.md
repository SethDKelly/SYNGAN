---
type: Phase Record
title: 006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit
status: complete
---

# 006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit

## Objective

Resolve the reopened `Relationship` candidate, define the semantic ownership of single-table/time-series/multi-table topology, and close the initial structured-data capability/extensibility blocker before any production implementation is authorized.

**Phase 006 remains design-only. No relational/time-series algorithm, schema, package API, persistence table, Spark materialization code, test suite, CI or deployment infrastructure is authorized or created.**

## Governing authority

006-G is downstream of:

- [Concept Design Methodology](../../authority/design-methodology.md);
- [Concept Review Criteria](../../discovery/concept-review-criteria.md);
- [Data Meaning](../../concepts/data-meaning.md);
- [Constraint](../../concepts/constraint.md);
- [Generation](../../concepts/generation.md);
- [Evaluation](../../concepts/evaluation.md);
- [Evidence](../../concepts/evidence.md);
- [Core Synchronizations](../../synchronizations/core-synchronizations.md);
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](../../authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md);
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](../../authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md);
- 006-A through 006-F design evidence.

## Discovery evidence

The full candidate/falsification record is preserved in:

[Structured-Data Topology & Relationship Concept/Extensibility Audit](../../discovery/structured-data-topology-relationship-concept-extensibility-audit.md).

That record is historical design evidence rather than canonical authority.

## Overall result

**PASS WITH RELATIONSHIP SUBORDINATION, TOPOLOGY CONTRACT PROMOTION & BASELINE-SCOPE CLOSURE.**

006-G establishes the canonical:

[Structured-Data Topology & Relationship Semantics Contract](../../authority/structured-data-topology-relationship-semantics-contract.md).

No new standalone concept or synchronization is accepted.

Current counts remain:

```text
accepted concepts             11
accepted synchronizations     15
new Phase 006 concepts          0
new Phase 006 sync IDs          0
reopened candidate concepts     0
```

The `Relationship` candidate is now resolved rather than provisional.

## Relationship disposition

**Disposition: reject as standalone concept; subordinate material structural relationship semantics to Data Meaning.**

The distinction remains first-class, but current evidence does not justify separate concept authority.

### Why it is not promoted

Relationship has meaningful state, but its purpose/lifecycle substantially duplicates Data Meaning:

```text
declare descriptive interpretation
review authority/uncertainty
revise/correct
supersede/invalidate
bind exact historical revision
```

The natural authority is also generally the same data/domain steward authority.

A separate Relationship concept would therefore require substantial new synchronization with Data Meaning, Strategy, Learning, Generation, Constraint, Evaluation and Provenance without adding enough independent actor reasoning.

### Why it is not discarded

Structural relationship semantics are required for topology-sensitive synthesis.

Data Meaning must be able to express inspectable assertions equivalent to:

```text
orders.customer_id
    corresponds to
customers.customer_id
```

and, for temporal data:

```text
records sharing entity_id
    form one logical series
    ordered by event_time
```

These semantics are historically bound through the exact Data Meaning revision.

## Descriptive versus prescriptive boundary

006-G preserves a strong distinction.

### Descriptive Data Meaning

```text
orders.customer_id refers to customers.customer_id
```

### Prescriptive Constraint

```text
every generated orders.customer_id must resolve
```

Likewise:

### Descriptive Data Meaning

```text
event_time establishes order within entity_id
```

### Prescriptive Constraint

```text
event_time must be nondecreasing and unique per entity
```

A request-specific cardinality/distribution target remains Generation-owned Condition rather than Relationship or Constraint merely because it references the same subjects.

## Single-table result

Single-table is a valid topology with no fabricated Relationship/structural assertion when none is needed.

The design continues to support field/group/record-level Data Meaning, cross-field Constraints, Conditions, Learning/Generation and Evaluation normally.

## Time-series result

Time-series is **not** `single_table + timestamp`.

The semantic model must be able to preserve where material:

- entity/series membership role;
- temporal/order role;
- sequence grouping/order relationship;
- static/context versus event-varying roles where applicable;
- uncertainty/authority for these interpretations.

Constraint owns cadence/order/uniqueness/gap/domain rules.

Generation owns requested entity/series scope and horizon/continuation semantics.

Strategy owns time-series synthesis capability/limitations.

Evaluation/Evidence owns temporal validity/fidelity/privacy findings.

No TimeSeries/Series/Sequence concept is introduced.

## Multi-table shared-key result

Multi-table shared-key topology uses explicit Data Meaning structural assertions spanning logical scopes.

The baseline semantics may represent common shapes including:

- one-to-one;
- one-to-many / many-to-one;
- composite keys;
- association/junction tables when supported;
- multiple coordinated tables/scopes.

Constraint owns referential-integrity/uniqueness/mandatory participation rules.

Generation owns participating output scopes, quantity/cardinality intent and whole-result completion.

Strategy owns topology capability and may explicitly reject unsupported cyclic/recursive shapes.

Evaluation/Evidence may examine joined/coordinated subjects.

## Composite-topology result

006-G explicitly rejects an architecture in which topology is forever one mutually exclusive discriminator.

A valid future shape can be:

```text
customers
  └── observations
        └── time-series per customer
```

or several related sequence-bearing scopes.

Therefore an API convenience token equivalent to:

```text
single_table | time_series | multi_table
```

may exist as a preset, but cannot be the sole durable semantic representation.

The committed semantic model must preserve the actual logical scope and structural/temporal meaning.

## Initial complete baseline scope decision

006-G closes BDR-004 by accepting three required structured-data capability families for the first **complete SYNGAN structured-data baseline**:

1. **single-table generation**;
2. **time-series generation**;
3. **multi-table shared-key generation**.

Implementation may be staged dependency-safely and a Strategy may support only a subset.

A release must not claim the complete structured-data baseline until at least one supported self-contained Strategy path exists for each family.

### Scope limits

The baseline does not imply:

- every time-series model family;
- streaming/online generation;
- arbitrary temporal hierarchy;
- every cyclic/recursive relational topology;
- arbitrary graph synthesis;
- equal Strategy breadth/maturity across topology families.

Those remain Strategy-specific or future capability scope.

## Stable relationship-assertion reference

Downstream Constraints/Evaluations may need to refer to one structural assertion precisely.

006-G therefore requires later architecture to support a stable assertion identity/reference scoped to an exact Data Meaning revision where necessary.

This is a representation/identity mechanism, not an independent Relationship resource/concept.

## Historical correction result

Changing a material relationship interpretation creates a new Data Meaning revision.

Historical Learning/Generation/Evaluation remain bound to the exact earlier revision.

A later corrected relationship can be evaluated against historical output through a new Evaluation, but the original work is not retroactively reinterpreted.

## Scale result

006-E scale rules remain intact.

Time-series compatibility must consider entity count, sequence-length distribution, horizon/cadence/context-window and partition/locality needs.

Multi-table compatibility must consider table count, shared-key cardinality, fan-out/skew, per-table/total output and cross-scope Evaluation cost.

Resource pressure cannot shorten the committed horizon, drop mandatory child scopes or weaken topology-dependent Constraints.

## Privacy/disclosure result

006-F's privacy boundary composes cleanly.

Disclosure Criteria may bind joined multi-table or complete trajectory/sequence subjects using the exact Data Meaning structural semantics.

Per-table/per-row favorable Evidence does not automatically establish whole-topology disclosure safety.

Relationship semantics themselves do not own privacy or release authority.

## Synchronization decision

No new synchronization is required.

Existing synchronization ownership remains sufficient:

- SYNC-01 — binds exact Data Meaning revision including structural assertions;
- SYNC-02 — Strategy/topology compatibility;
- SYNC-03 — topology-dependent Constraint binding;
- SYNC-06 — Generation scope/topology commitment;
- SYNC-08 — coordinated whole-result completion;
- SYNC-09/10/12 — exact Evaluation subject/method/Evidence strength;
- SYNC-14/15 — historical/reproducibility context.

The topology-sensitive 006-C scenarios were conceptually replayed after the Relationship disposition and remain coherent. No `SYNC-16` is justified.

## BDR-004 disposition

**BDR-004 — initial-baseline scope and future-extensibility closure is resolved by 006-G.**

The design now explicitly:

- includes single-table/time-series/multi-table shared-key in the complete baseline capability target;
- prevents a topology parameter from becoming semantic authority;
- permits composite topology;
- assigns structural relationship meaning to Data Meaning;
- keeps prescriptive topology validity in Constraint;
- keeps topology request/fulfillment in Generation;
- requires Strategy capability declarations rather than universal support;
- avoids permanent single-table architecture assumptions.

## Downstream obligations

### 006-H

Experience must make topology requirements and limitations understandable without exposing Data Meaning/Constraint/Generation ownership as confusing implementation jargon.

It must also cover recovery/security/degraded/history/privacy semantics accumulated during 006-B through 006-G.

### 006-I

Architecture/ADR/planning reconciliation must back-propagate at least:

- logical multi-scope data/output representation;
- structural relationship assertion references bound to Data Meaning revisions;
- Strategy topology capability profiles;
- Generation topology specification/completion;
- time-series/multi-table materialization and manifests;
- Evaluation subjects spanning related scopes/sequences;
- verification/conformance for all three complete-baseline families;
- composable topology rather than exclusive-enum assumptions.

Phase 005 history must not be rewritten.

### 006-J

The final readiness audit must replay materially affected scenarios/probes and verify that architecture/planning did not reintroduce a standalone hidden Relationship owner, permanent single-table assumption, or mutually exclusive topology limitation.

## Exit assessment

**Status: complete.**

Findings:

- standalone Relationship is not justified;
- structural relationship semantics remain explicit as Data Meaning-owned state;
- descriptive linkage/order remains separate from prescriptive Constraint authority;
- single-table requires no fabricated relationship state;
- time-series is not reducible to timestamp type;
- multi-table shared-key semantics are first-class without a new concept;
- composite topology must remain representable;
- topology presets may be convenience syntax but not semantic authority;
- single-table, time-series and multi-table shared-key are all required families in the complete baseline capability target;
- BDR-004 is resolved;
- accepted counts remain eleven concepts/fifteen synchronizations;
- production implementation remains unauthorized.

## Next group

**006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows**.