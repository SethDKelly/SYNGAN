---
type: Design Authority
title: Structured-Data Topology & Relationship Semantics Contract
status: active
---

# Structured-Data Topology & Relationship Semantics Contract

## Purpose

Define current ownership and extensibility rules for single-table, time-series, multi-table shared-key and composite structured-data topology without introducing standalone `Relationship`, `Table`, `Series`, `Dataset`, `DataTopology`, `LogicalScope`, `Manifest` or `Output` concepts.

This contract is current cross-cutting authority and is interpreted beneath completed Phase 012 concept design and completed Phase 013 reconciliation decisions.

## Governing rule

> **Topology selection may be convenient syntax, but committed semantics come from exact logical scope, Data Meaning structural interpretation, Generation intent, applicable Constraints, Strategy capability and Evaluation requirements. A topology label or physical layout never substitutes for those authorities.**

## Concept disposition

`Relationship` remains subordinate to existing concept authority rather than a standalone concept.

Its current descriptive purpose—reusable structural linkage/order among synthesis-relevant logical data subjects—is owned by Data Meaning.

Architecture may provide stable references to structural assertions, logical scopes and coordinated subjects. Addressability does not create another semantic owner.

## Ownership boundaries

### Data Meaning

Data Meaning owns descriptive structural interpretation where material, including semantics equivalent to:

- identifier/key roles;
- corresponding key roles across logical scopes;
- parent/child or association-role meaning;
- series/entity membership roles;
- temporal/order roles;
- descriptive relationship direction;
- descriptive cardinality/participation interpretation;
- uncertainty/conflict/authority around those interpretations.

A structural relationship assertion is historically bound through the exact Data Meaning revision that contains it. Material correction creates a new Data Meaning revision rather than rewriting historical commitments.

### Constraint

Constraint owns prescriptive validity.

Examples:

```text
orders.customer_id corresponds to customers.customer_id
    -> descriptive Data Meaning

every orders.customer_id must resolve to customers.customer_id
    -> Constraint

event_time defines order within entity_id
    -> descriptive Data Meaning

timestamps must be nondecreasing within each entity
    -> Constraint
```

Cardinality/participation must be classified by purpose: descriptive domain fact -> Data Meaning; required validity rule -> Constraint; request-specific desired population characteristic -> Generation-owned Condition.

### Generation

Generation owns requested logical output scope/topology fulfillment.

Where material, a committed Generation may bind:

- participating logical scopes;
- requested quantity/cardinality semantics per scope;
- entity/series scope;
- temporal horizon or continuation scope;
- topology-specific Conditions;
- exact Data Meaning revision/assertions;
- applicable topology-dependent Constraints;
- whole-result completion requirements;
- exact direct-source or Learned-State basis where applicable;
- material approximation/tolerance semantics.

Generation does not own reusable relationship meaning merely because its output uses that meaning.

### Synthesis Strategy

Strategy owns reusable topology capability and limitations. A Strategy may support one or more of:

- single-table;
- time-series;
- multi-table shared-key;
- composite multi-scope/sequence structures;
- narrower key/cardinality/sequence shapes.

Compatibility is contextual. An incompatible Strategy cannot silently simplify a committed topology.

### Evaluation / Evidence

Evaluation may bind a subject spanning one or more logical scopes or sequences when the Criterion requires it.

Evidence remains bounded to the exact subject, method, scope, coverage, assumptions and claim strength. Per-table/per-row findings do not automatically establish whole-topology claims.

## Single-table profile

Single-table Generation is valid and requires no fabricated relationship state.

It may still use field/group/record-level Data Meaning, cross-field Constraints, direct or Learned-State Strategies, Conditions and Evaluation.

## Time-series profile

Time-series semantics must not be reduced to `single table + timestamp`.

Where material:

- Data Meaning identifies entity/series membership and temporal/order roles;
- Constraint owns temporal validity requirements;
- Generation owns entity/scope/horizon/quantity intent;
- Strategy owns sequence-generation capability/limitations;
- Evaluation/Evidence owns temporal fidelity/validity/privacy findings.

Physical sort metadata or timestamp type alone does not establish semantic sequence meaning.

## Multi-table shared-key profile

Multi-table Generation may contain several logical scopes connected by explicit Data Meaning structural assertions.

The baseline may include common one-to-one, one-to-many/many-to-one, composite-key and association-table structures where supported by Strategy capability.

Whole-result completion applies to the exact committed coordinated scope. Completion of one constituent does not complete the Generation while another mandatory constituent or required cross-scope obligation remains incomplete, violated or indeterminate.

Arbitrary recursive/cyclic graph lifecycle is not a universal baseline promise.

## Composite topology

Topology families are composable rather than permanently mutually exclusive.

For example:

```text
customers
  └── observations
        ordered time series per customer
```

may be one legitimate coordinated subject.

A convenience selector such as:

```text
single_table | time_series | multi_table
```

may exist, but it must not be the sole durable semantic representation if it prevents valid composition.

## Logical scope and relationship references

Architecture may provide bounded logical-scope identity and stable relationship-assertion references scoped to an exact Data Meaning revision.

These mechanisms exist for exact addressing, topology composition, historical binding, Evaluation targeting and distributed representation. They do not create independently owned concepts/resources by implication.

Millions of rows/entities/series do not imply millions of control-plane logical scopes.

## Structured-data capability baseline

The current complete structured-data capability baseline continues to include:

1. single-table generation;
2. time-series generation;
3. multi-table shared-key generation.

Composite structures must remain representable even when not every combination is supported by the first Strategy catalog.

Individual Strategies may support subsets. A complete product capability claim requires supported paths for the required baseline families; it does not imply equal algorithm breadth or maturity.

The baseline does not automatically include arbitrary recursive graph synthesis, streaming/session/feed lifecycle or future product-owned graph relationship authority.

## Scale and approximation consequence

Topology support remains Spark-scale and bounded/reference-first.

Resource pressure cannot silently:

- truncate committed horizons;
- drop required scopes/children;
- weaken relationship Constraints;
- convert exact requirements into sampled/estimated proof;
- convert whole-result completion into partial success.

Approximation is valid only when the owning semantic contract permits it and the resulting limitation remains explicit.

## Privacy/disclosure consequence

Topology relationships may materially affect disclosure risk, so privacy/disclosure Criteria may require a coordinated subject including joins or trajectories.

Structural relationship semantics do not own privacy guarantees, anonymization claims or release/use authority.

## Current synchronization consequence

Current Phase 009 authority controls all synchronization numbering and ownership.

Relevant current rules include:

```text
SYNC-01  exact Data Meaning revision binding
SYNC-02  Strategy compatibility including requested topology/scope
SYNC-03  Constraint binding and handling
SYNC-06  Generation / Learned State reuse compatibility when reusable
         Learned State participates; direct Generation does not activate it
SYNC-07  Generation operational realization; candidate state remains non-final
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method/scope/coverage compatibility
SYNC-11  Evaluation operational realization
SYNC-12  Evaluation produces Evidence bound to the exact subject
SYNC-13  controlled Evidence consumption / Generation handoff
SYNC-14  material Provenance relationship recording
```

Current Phase 009 disposition also controls:

```text
SYNC-08  RETIRED as cross-concept synchronization;
         candidate/completed-output establishment is Generation-local behavior.

SYNC-15  RECLASSIFIED under the cross-cutting Reproducibility contract;
         not active synchronization-owned state.
```

No new synchronization is introduced by topology representation.

A future independent topology/relationship purpose with its own durable state/history/actions/lifecycle would return to concept discovery before architecture or implementation.

## Phase 013 architecture consequence

Current architecture must preserve:

- logical multi-scope/source/output references;
- exact Data Meaning relationship-assertion references;
- Strategy topology capability declarations;
- Generation topology specifications and whole-scope completion;
- time-series/multi-table materialization without driver-local enumeration;
- Evaluation subjects spanning exact related scopes/sequences;
- multi-scope snapshot/coordination strength when required;
- manifest/provider-equivalent immutable subject boundaries;
- candidate non-finality and Generation-owned completed-output establishment;
- scale and disclosure limitations without semantic weakening;
- topology presets as convenience rather than semantic authority.

[Phase 013-D Distributed Data Reconciliation](../history/architecture/phase-013-d-distributed-data-topology-manifest-candidate-promotion-reconciliation.md) is the current downstream architecture interpretation of this contract.

## Invariants

1. `Relationship` and `DataTopology` are not standalone accepted concepts under current scope.
2. Material structural relationship semantics remain explicit and historically bound through Data Meaning.
3. Descriptive structural meaning remains distinct from prescriptive Constraint semantics.
4. Generation owns requested topology/scope fulfillment, not reusable relationship authority.
5. Strategy owns reusable topology capability/limitations, not relationship meaning.
6. Single-table work does not fabricate relationship state when none is needed.
7. Time-series meaning is not reducible to physical timestamp type or sort order.
8. Multi-table shared-key meaning is not reducible to provider foreign-key metadata.
9. Whole-result completion covers the exact committed coordinated scope.
10. Per-constituent Evaluation/Evidence does not automatically establish whole-topology claims.
11. Topology convenience syntax is not sole durable authority.
12. Composite relational/time-series structures remain representable.
13. Relationship correction creates new Data Meaning authority for future work rather than rewriting historical bindings.
14. Physical/provider exactness is consumed only at the guarantee actually established.
15. Resource pressure cannot silently weaken committed topology/scope/validation semantics.
16. No topology rule makes a specific table format, provider product, manifest format, Spark class or storage layout canonical SYNGAN semantics.
17. Current Phase 009 synchronization authority supersedes historical Phase 006/007 synchronization numbering/meaning where they conflict.

## Operational principle

A steward declares a Data Meaning revision in which `customers.customer_id` is the parent identifier and `orders.customer_id` is the corresponding child key. A Constraint separately requires every generated order key to resolve to a generated customer. A Generation commits both scopes and the exact relevant authority. Strategy compatibility confirms support for the relationship shape. Distributed materialization may close each scope separately, but the Generation remains incomplete until the whole required subject and completion basis are sufficient.

In a time-series subject, `sensor_id` may identify series membership and `event_time` semantic ordering. A Generation requesting twelve future months cannot silently shorten the committed horizon under resource pressure. A composite dataset may contain customer metadata plus time-series observations; architecture represents it through logical scope plus exact Data Meaning/Generation bindings rather than a mutually exclusive topology enum.
