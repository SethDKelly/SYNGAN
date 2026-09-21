---
type: Concept Discovery
title: Post-Planning Concept Revalidation & Structured-Data Topology Candidates
status: provisional
---

# Post-Planning Concept Revalidation & Structured-Data Topology Candidates

## Purpose

Preserve the Phase 006-A discovery evidence used to re-test SYNGAN's accepted concept catalog after Phase 005 implementation planning exposed more concrete representation, recovery, security, deployment and structured-data capability questions.

This document is **discovery evidence, not accepted concept authority**. The accepted concept catalog under `docs/concepts/` remains authoritative unless Phase 006 later promotes a revision explicitly.

Phase 006 remains design-only and creates no production implementation.

## Governing question

For every post-planning structure or proposed capability, ask:

> Does this thing have a distinct user/system purpose, independently meaningful state/actions, operational principles and synchronization responsibilities—or is it a subordinate representation, configuration choice, contextual assessment or mechanism belonging to an existing concept?

## Post-planning mechanism audit

| Structure | 006-A disposition | Reason |
|---|---|---|
| `ResourceRef` / `HistoricalRef` | representation mechanism | Stable identity/reference realization; does not own a new purpose or lifecycle. |
| Evidence finding slot | Evidence-owned implementation mechanism | Gives retry-safe finding identity; does not own finding meaning. |
| Generation completion basis | Generation-owned historical state | Preserves the exact candidate/requirements/Evidence used at promotion. |
| `ImplementationBindingRef` / `RuntimeSpiVersion` | architecture/integration mechanism | Separates executable realization from Strategy/method semantic authority. |
| `AttemptEpoch` / `WriterFence` | Execution/architecture mechanism | Protects operational mutation authority; Attempt remains subordinate to Execution. |
| Checkpoint / recovery decision | Execution-owned subordinate state | Recovery state has no independent purpose outside operational realization. |
| Dependency resolution / capability grant | contextual integration/security state | Requirement, resolution, authorization and runtime capability remain separate assessments/mechanisms. |
| `SecretRef` | non-secret integration reference | Identifies a secret source without becoming secret or domain authority. |
| `PlatformCapabilityDescriptor` / compatibility assessment | contextual deployment assessment | Describes environment guarantees for one context; not durable semantic authority. |
| `TelemetryContext` | observability correlation mechanism | Does not own semantic/operational history. |
| `ControlPlaneIncarnation` | **candidate recovery mechanism; unresolved upstream closure** | No independent concept purpose is established yet, but 006-B must test temporal-authority semantics before accepting it as sufficient architecture realization. |
| `GenerationMode` / `DataTopologyMode` | **not a concept** | A parameter may select a capability profile but cannot own the semantics of table relationships, temporal ordering, cardinality or validity. |

No post-planning mechanism above currently requires immediate promotion to a new accepted concept.

## New capability evidence supplied to Phase 006

Phase 006 must now consider at least three structured-data generation capability shapes:

1. **single-table generation**;
2. **time-series-based table generation**;
3. **multi-table generation with shared-key relationships**.

These are capability/workflow shapes, not automatically concepts and not necessarily one universal API enum.

A future convenience surface MAY offer a parameter or typed selection equivalent to:

```text
single_table
time_series
multi_table
```

but that selection only chooses which semantic structure is being requested. It MUST NOT hide or replace the actual Data Meaning, Relationship/structure, Constraint, Strategy, Generation, Evaluation and Provenance facts required by the selected shape.

## Single-table capability

### Current fit

Single-table structured generation composes cleanly with the existing eleven concepts.

- **Data Meaning** interprets fields and record/dataset scope.
- **Constraint** owns row, cross-field, cross-record and dataset validity rules.
- **Synthesis Strategy** declares supported semantics, scale and generation capabilities.
- **Learning / Learned State** own reusable source-derived behavior when required.
- **Generation** owns requested quantity/scope/Conditions and completion.
- **Evaluation Criterion / Evaluation / Evidence** assess exact results.
- **Execution** owns long-running operational realization.
- **Provenance** records material historical relationships.

### 006-A disposition

**Confirmed as the existing baseline capability. No new concept is required merely for `single_table`.**

A standalone `Table`, `Dataset`, `GenerationMode`, or `DataTopology` concept is not justified by single-table generation alone.

## Time-series capability

Time-series generation is not merely a physical table with a timestamp column.

Potentially material semantics include:

- one or more timestamp/time-role fields;
- entity/series partition identity;
- ordering within a series;
- start/end/horizon semantics;
- cadence or irregular-event semantics;
- lag/dependency structure;
- continuation versus independent-series generation;
- sequence length/quantity semantics;
- temporal Constraints;
- temporal Evaluation questions and claim strength;
- checkpoint/randomness implications for sequence-continuation methods.

### Existing concept coverage

The current concepts already own substantial parts:

- `event_time is a timestamp` → **Data Meaning**;
- `entity_id identifies a logical series` → **Data Meaning**;
- `timestamps must be monotonic within entity` → **Constraint**;
- `generate the next 90 days` → **Generation** request/scope/Condition semantics;
- temporal capability/limitations → **Synthesis Strategy**;
- temporal fidelity/autocorrelation/forecast-distribution questions → **Evaluation Criterion / Evaluation / Evidence**.

### Remaining question

The reusable descriptive fact:

```text
records sharing entity_id participate in one logical sequence
ordered by event_time
```

is not clearly a prescriptive Constraint and is richer than field-local semantic meaning.

006-A therefore does **not** create a standalone `Series` or `Temporal Structure` concept. Instead it requires 006-G to test whether temporal sequence structure can be expressed as a specialization of a more generic **Relationship** concept without distorting Data Meaning or Constraint.

### 006-A disposition

**Time-series becomes a required Phase 006 design target and representative probe, but not yet a separately accepted concept or guaranteed first-release scope.**

## Multi-table shared-key capability

A multi-table synthesis request with shared keys introduces reusable descriptive structure such as:

```text
customers.customer_id
        ↓ referenced by
orders.customer_id
```

with potentially material semantics for:

- participating logical scopes/tables;
- endpoint roles;
- key correspondence;
- parent/child or peer relationship meaning;
- cardinality/participation shape;
- generation ordering or coordination;
- cross-table Constraints;
- exact output-set completion;
- cross-table Evaluation/Evidence;
- history and Provenance of coordinated outputs.

### Existing concept coverage

Existing concepts remain necessary but do not obviously own the entire relation:

- `customer_id is an identifier` → **Data Meaning**;
- `orders.customer_id denotes customer identity` → partly **Data Meaning**;
- `every order customer key must resolve` → **Constraint**;
- `one customer may have many orders` may have both descriptive-structure and prescriptive-validity aspects;
- multi-table support/limitations → **Synthesis Strategy**;
- requested table/output quantities → **Generation**;
- referential/cardinality/fidelity questions → **Evaluation/Evidence**.

### Evidence for reopening `Relationship`

The descriptive linkage itself has a plausible independent purpose:

> Enable actors and activities to establish, inspect, revise and bind stable relationships among logical data scopes or record roles independently of any one synthesis Strategy or validity rule.

Candidate Relationship state could include bounded control-plane facts such as:

- participant logical scopes and roles;
- linkage/key-role semantics;
- relationship kind;
- descriptive cardinality/participation semantics where appropriate;
- temporal ordering/series-partition semantics where appropriate;
- authority/source and revision lifecycle;
- unresolved/conflicting relationship meaning.

Candidate actions could include:

- declare;
- infer/propose;
- review;
- revise/correct;
- supersede;
- invalidate.

This resembles the revisioned descriptive-authority pattern of Data Meaning while having a distinct cross-scope relationship purpose.

### Boundary hypothesis

If `Relationship` is accepted later:

- **Data Meaning** continues to own what individual fields/scopes mean;
- **Relationship** owns reusable descriptive linkage/ordering among logical scopes or record roles;
- **Constraint** owns prescriptive rules the relation/output must obey;
- **Generation** owns the request-specific set/quantity/horizon/Conditions;
- **Strategy** owns support and limitations;
- **Evaluation/Evidence** own assessment/findings;
- **Provenance** owns historical derivation/use relationships, not dataset-domain relationships.

The same generic Relationship concept might cover both cross-table shared-key relationships and temporal sequence membership/order, but 006-A does not assume that generalization is valid. 006-G must falsify it.

### 006-A disposition

**`Relationship` is formally reopened as a candidate concept for Phase 006-G. It is not yet accepted and the accepted catalog remains eleven concepts.**

## Why a function parameter is insufficient as semantic authority

An API could eventually offer a concise surface similar to:

```text
generate(..., structure = single-table specification)
generate(..., structure = time-series specification)
generate(..., structure = multi-table specification)
```

or another function parameter/builder shape.

That is an experience/representation decision only.

For example, selecting `multi_table` cannot by itself answer:

- which scopes participate;
- which keys correspond;
- whether one-to-many is descriptive intent or a required Constraint;
- how orphan rows are treated;
- how output completion spans tables;
- what Evidence is required for referential integrity.

Likewise selecting `time_series` cannot by itself answer:

- what identifies a series;
- which field establishes time;
- whether sequence order is strict;
- whether cadence is fixed/irregular;
- whether the request generates continuation or independent sequences;
- which temporal dependencies must be preserved.

The future API MAY make these choices ergonomic, but it must bind the underlying semantics explicitly enough for history, Strategy compatibility, Evaluation and reproducibility.

## Scope-boundary result

006-A does not yet decide the complete first implementation capability set.

Current status:

```text
single-table
    accepted current baseline capability

time-series
    required Phase 006 design target; initial-release inclusion TBD

multi-table shared-key
    required Phase 006 design target; initial-release inclusion TBD
    Relationship candidate reopened
```

This avoids both errors:

- expanding product scope automatically because a capability is conceivable;
- hard-coding the current implementation plan so those capabilities become impossible later.

## Concept-count result

At 006-A exit:

```text
accepted concepts: 11
accepted synchronizations: 15
new accepted concepts: 0
new accepted synchronizations: 0
reopened candidate concepts: Relationship
```

Potential temporal/relational changes remain deliberately provisional until 006-G and later consolidation.

## Required downstream Phase 006 work

### 006-B

Resolve temporal authority in the operational/disaster-recovery sense (`ControlPlaneIncarnation` and regressive restore). This is unrelated to time-series data semantics and the two meanings of `temporal` must remain distinct.

### 006-C

Add adversarial scenarios for topology-sensitive workflows, including partial multi-table output, missing parent/child output, temporal sequence interruption, retry across coordinated outputs, and exact Evidence subject identity across a logical output set.

### 006-D

Representative design probes must now cover topology diversity as well as algorithm diversity:

- Learning-based single-table deep-generative family;
- direct/simple single-table path;
- time-series Strategy shape;
- multi-table shared-key Strategy shape;
- deterministic/bounded and statistical/approximate Evaluation methods.

No algorithm implementation is authorized.

### 006-G

Broaden the former relational-only audit into explicit **single-table / time-series / multi-table structural-topology concept discovery and extensibility validation**.

006-G must decide whether:

1. existing concepts alone remain sufficient;
2. one generic `Relationship` concept is required;
3. temporal sequence semantics require a distinct concept;
4. another narrower concept boundary is more defensible.

Any accepted new concept requires corresponding synchronization, experience, architecture and implementation-plan reconciliation through 006-H/006-I.

## Exit conclusion

The Phase 005 planning mechanisms do not themselves require new concepts.

The user's structured-data capability direction does produce legitimate new concept-discovery evidence. Multi-table shared-key synthesis in particular is strong enough to reopen the previously deferred `Relationship` candidate, while time-series synthesis supplies a falsification case for whether that candidate is generic enough.

No accepted concept or synchronization is changed by this discovery record alone.