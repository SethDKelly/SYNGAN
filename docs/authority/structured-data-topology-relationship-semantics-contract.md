---
type: Design Authority
title: Structured-Data Topology & Relationship Semantics Contract
status: active
---

# Structured-Data Topology & Relationship Semantics Contract

## Purpose

Define canonical ownership and extensibility rules for single-table, time-series, multi-table shared-key and composite structured-data topologies without introducing a standalone `Relationship`, `Table`, `Series`, `Dataset`, or `DataTopology` concept.

## Governing rule

> **Topology selection may be convenient API syntax, but committed semantics come from exact logical scope, Data Meaning structural relationship assertions, Generation intent, applicable Constraints and Evaluation requirements. A topology label never substitutes for those authorities.**

## Concept disposition

`Relationship` is **not accepted as a standalone concept**.

Its current purpose—describing reusable structural linkage/order among synthesis-relevant logical data subjects—substantially overlaps the descriptive interpretation lifecycle already owned by Data Meaning.

Structural relationship semantics are therefore **subordinate Data Meaning state**.

This disposition preserves the semantic distinction while avoiding a second concept with nearly identical declaration, revision, authority and historical-binding behavior.

## Data Meaning ownership

Data Meaning owns descriptive structural interpretation where material, including semantics equivalent to:

- identifier/key roles;
- corresponding key roles across logical scopes;
- parent/child or association role meaning;
- series/entity membership roles;
- temporal/order roles;
- descriptive relationship direction;
- descriptive cardinality/participation interpretation when it states what the data structure means rather than what valid output must obey;
- uncertainty/conflict/authority around those interpretations.

A structural relationship assertion is bound historically through the exact Data Meaning revision that contains it.

Changing a material relationship interpretation creates a new Data Meaning revision rather than mutating historical work.

## Constraint boundary

Constraint remains prescriptive authority.

Examples:

```text
orders.customer_id refers to customers.customer_id
```

is descriptive Data Meaning.

```text
every orders.customer_id must resolve to customers.customer_id
```

is a Constraint.

Likewise:

```text
event_time establishes ordering within entity_id
```

is descriptive Data Meaning.

```text
timestamps must be nondecreasing and unique within each entity
```

is a Constraint.

Cardinality/participation information must be classified by purpose. A descriptive domain fact may be Data Meaning; a required validity rule is Constraint; a request-specific desired distribution is Generation-owned Condition.

## Generation boundary

Generation owns the requested logical output scope and topology fulfillment semantics.

Where material, a Generation may bind/request:

- participating logical scopes;
- requested quantity/cardinality semantics per scope;
- requested entity/series scope;
- requested temporal horizon or continuation scope;
- topology-specific Conditions;
- exact Data Meaning revision containing required structural relationship assertions;
- applicable topology-dependent Constraints;
- whole-result completion requirements.

Generation does not own reusable relationship meaning merely because it requests an output that uses it.

## Strategy boundary

Synthesis Strategy owns reusable capability/limitations for topology shapes.

A Strategy may support:

- single-table only;
- time-series only;
- multi-table shared-key only;
- several of these;
- composed multi-table/time-series structures;
- narrower cardinality/key/sequence shapes.

Compatibility is contextual. A Strategy that cannot support the committed topology/relationship shape is incompatible or limited; SYNGAN must not silently simplify the topology.

## Evaluation/Evidence boundary

Evaluation may bind a subject spanning one or more logical scopes or longitudinal sequences when the Criterion requires it.

Examples include:

- referential integrity;
- parent/child cardinality distributions;
- join-level fidelity;
- temporal ordering/cadence validity;
- sequence/trajectory utility;
- multi-table linkage disclosure risk;
- longitudinal uniqueness/memorization risk.

Evidence remains bounded to the exact subject, relationship semantics, method, scope and claim strength.

Per-table or per-row Evidence does not automatically establish whole-topology claims.

## Single-table profile

Single-table generation is a valid topology requiring no fabricated relationship state.

It may still use:

- field/group/record-level Data Meaning;
- cross-field Constraints;
- direct or Learned-State Strategies;
- Conditions and Evaluation.

The absence of structural relationship assertions is valid when no such semantics are required.

## Time-series profile

Time-series generation must not be reduced to `single_table + timestamp`.

Where material, Data Meaning identifies semantics such as:

- entity/series membership role;
- temporal/order field role;
- sequence grouping/order relationship;
- static/context versus event-varying roles where relevant.

Constraint owns prescriptive temporal rules such as:

- monotonicity/order validity;
- uniqueness;
- cadence/gap bounds;
- allowed temporal domain;
- cross-field temporal consistency.

Generation owns requested entity count/scope, horizon/continuation and quantity intent.

Strategy owns sequence-generation capability and limitations.

Evaluation/Evidence owns temporal fidelity/validity/privacy findings.

No standalone `TimeSeries`, `Series`, `Sequence`, or temporal Relationship concept is accepted.

## Multi-table shared-key profile

Multi-table generation may include several logical scopes connected by explicit shared-key structural relationship assertions.

The initial baseline may represent common structures including:

- one-to-one;
- one-to-many / many-to-one;
- composite shared keys;
- junction/association tables where the Strategy supports them;
- multiple related scopes.

Arbitrary recursive/cyclic graph synthesis is not a universal baseline guarantee. Strategy capability may explicitly support, limit or reject such shapes.

Whole-result completion remains governed by the committed logical Generation scope. A mandatory constituent or cross-scope requirement cannot disappear because another constituent completed.

## Composite topology

Topology families are not permanently mutually exclusive.

A legitimate future subject can be equivalent to:

```text
customers
  └── observations
        └── ordered time-series per customer
```

or several related time-series scopes.

Therefore a high-level topology selector may exist for common cases, but the durable model must permit composition.

A global exclusive enum such as:

```text
single_table | time_series | multi_table
```

MUST NOT be the sole semantic representation if it prevents valid composite structures.

## Convenience API boundary

A future public API may expose a convenience parameter or typed preset equivalent to:

```text
mode="single_table"
mode="time_series"
mode="multi_table"
```

This is an experience/representation mechanism.

Before commitment it must resolve into enough exact semantic state to preserve:

- logical scope;
- required Data Meaning revision;
- structural relationship assertions where applicable;
- temporal/entity roles where applicable;
- topology-dependent Conditions;
- applicable Constraints;
- Strategy compatibility;
- completion/Evaluation requirements.

Two requests using the same `mode` may therefore have materially different semantics.

## Relationship assertion addressing

Downstream rules and Evaluations may need to identify one structural relationship assertion precisely.

Later architecture may provide a stable assertion identifier/reference scoped to the exact Data Meaning revision.

That mechanism exists for historical resolution and precise binding. It does not create a globally independent Relationship resource or concept.

## Historical correction

A relationship correction follows Data Meaning revision semantics.

Example:

```text
DM-R3:
orders.customer_id -> customers.customer_id

later correction:
orders.account_id -> accounts.account_id
```

The correction creates a new Data Meaning revision for future work.

Historical Learning/Generation/Evaluation remain bound to the exact prior revision they used.

Later Evaluation may assess historical output under the corrected/new structure, but it must be a new question rather than retroactive reinterpretation.

## Initial complete structured-data capability baseline

The first **complete SYNGAN structured-data capability baseline** includes three required capability families:

1. **single-table generation**;
2. **time-series generation**;
3. **multi-table shared-key generation**.

Implementation may be delivered in dependency-safe stages and individual Strategies may support only subsets.

However, a release must not claim the complete structured-data baseline until at least one supported self-contained Strategy path exists for each family.

This requirement does not imply equal algorithm breadth or maturity across all three families.

## Initial scope boundaries

### Single-table

Required baseline capability.

### Time-series

Required baseline capability with explicit entity/series and ordering/time semantics. The baseline does not promise every sequence-model family, regular cadence, streaming/online generation, or arbitrary temporal hierarchy.

### Multi-table shared-key

Required baseline capability for explicit shared-key relationships and common relational structures. The baseline does not promise arbitrary recursive graph synthesis or every cyclic/self-referential relationship shape.

### Composite topologies

Must remain representable by architecture and future Strategy capability even when not every composite combination is supported by the first Strategy catalog.

## Scale consequence

Topology support is subject to the Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract.

Time-series readiness includes entity count, sequence-length distribution, horizon/cadence/context-window and partition/locality pressure.

Multi-table readiness includes table count, key cardinality, fan-out/skew, per-scope/total volume and cross-scope validation cost.

Resource pressure cannot silently truncate horizons, drop child scopes, weaken relationship Constraints or convert whole-result completion into partial success.

## Privacy/disclosure consequence

Topology relationships may materially affect disclosure risk.

Privacy/disclosure Criteria may need the coordinated subject, including joins and trajectories.

Structural Relationship semantics themselves do not own privacy meaning or release authority.

## Synchronization consequence

No new synchronization ID is introduced.

Existing rules remain sufficient:

- SYNC-01 binds the exact Data Meaning revision, including material structural relationship assertions;
- SYNC-02 validates Strategy compatibility with the topology/relationship semantics;
- SYNC-03 binds applicable topology-dependent Constraints;
- SYNC-06 binds Generation scope/topology intent;
- SYNC-08 governs whole logical-output completion;
- SYNC-09/10/12 preserve exact Evaluation subject/method/Evidence claim strength;
- SYNC-14/15 preserve exact historical/reproducibility context.

If a future capability reveals structural state with a genuinely independent purpose/lifecycle not captured by Data Meaning, concept discovery may reopen. Current evidence does not justify that separation.

## 006-I architecture/planning consequence

006-I must back-propagate this contract into architecture/planning without rewriting phase history, including:

- logical multi-scope/source/output references;
- Data Meaning relationship-assertion representation/reference;
- Strategy topology capability declarations;
- Generation topology specifications and completion;
- time-series/multi-table materialization/manifests;
- Evaluation subjects spanning related scopes/sequences;
- scale and privacy implications;
- package/API design that treats topology presets as convenience rather than semantic authority;
- verification/conformance for all three baseline capability families.

## Invariants

1. `Relationship` is not a standalone accepted concept under the current design.
2. Material structural relationship semantics MUST remain explicit, inspectable and historically bound through Data Meaning.
3. Descriptive relationship meaning MUST remain distinct from prescriptive Constraint semantics.
4. Generation owns requested topology/scope, not reusable relationship authority.
5. Strategy owns topology capability/limitations, not relationship meaning.
6. Single-table work MUST NOT fabricate relationship state when none is needed.
7. Time-series MUST NOT be reduced to a physical timestamp type or topology label.
8. Multi-table shared-key semantics MUST NOT be reduced to physical foreign-key metadata alone.
9. Whole-result completion MUST cover the committed coordinated scope.
10. Per-constituent Evaluation/Evidence MUST NOT automatically establish whole-topology claims.
11. A topology convenience parameter MUST NOT be the sole durable semantic representation.
12. The semantic model MUST permit composition such as multi-table subjects containing time-series scopes.
13. A relationship correction MUST create new semantic authority for future work rather than rewriting historical bindings.
14. The complete baseline capability claim requires at least one supported self-contained Strategy path for single-table, time-series and multi-table shared-key generation.
15. No rule in this contract makes a particular table/schema/foreign-key/time-series library/Spark representation canonical SYNGAN semantics.

## Operational principle

A steward declares a Data Meaning revision in which `customers.customer_id` is the parent identifier and `orders.customer_id` is the corresponding child key. A Constraint separately requires every generated order key to resolve to a generated customer. A practitioner requests a multi-table Generation covering both scopes. Strategy compatibility confirms support for the relationship shape, and the Generation remains incomplete until both scopes and required cross-scope validation are completion-sufficient.

In another dataset, `sensor_id` identifies a series and `event_time` establishes order within each series. A Generation requests twelve future months. Resource pressure may delay execution but cannot shorten the committed horizon. A future composite dataset may contain customer metadata plus a time-series observations table; the design represents this through logical scope and Data Meaning structural assertions rather than forcing the work into one mutually exclusive topology enum.