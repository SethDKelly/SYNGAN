---
type: Phase Record
title: 006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation
status: complete
---

# 006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation

## Objective

Re-test the accepted concept catalog after Phase 005 implementation planning exposed more concrete identity, runtime, recovery, security, deployment and structured-data capability structures.

The group asks whether any post-planning mechanism has acquired a distinct Jackson-style purpose/state/action boundary that requires promotion to a concept, and whether the initial structured-data scope remains coherent and extensible before implementation is authorized.

**Phase 006 remains design-only. No production implementation is authorized or performed.**

## Entry authority

006-A is downstream of:

- [Concept Design Methodology](../../authority/design-methodology.md);
- [Accepted Concepts](../../concepts/index.md);
- [Accepted Synchronizations](../../synchronizations/index.md);
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md);
- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Phase 005 Consolidated Implementation-Planning Contract](../../implementation/phase-005-consolidated-implementation-planning-contract.md);
- [SYNGAN Design & Delivery Backlog](../../backlog/index.md).

## Discovery evidence created

006-A establishes the provisional discovery record:

[Post-Planning Concept Revalidation & Structured-Data Topology Candidates](../../discovery/post-planning-concept-revalidation-structured-topology-candidates.md).

That file is design evidence rather than accepted concept authority.

## Post-planning mechanism audit

006-A finds **no immediate new accepted concept** among the implementation-planning structures introduced in Phase 005.

The following remain subordinate representation/integration/operational mechanisms:

- `ResourceRef` / `HistoricalRef`;
- Evidence finding slots;
- Generation completion basis;
- `ImplementationBindingRef` / `RuntimeSpiVersion`;
- `AttemptEpoch` / `WriterFence`;
- Checkpoint / recovery-decision representations;
- dependency-resolution records;
- AuthorizationDecision / CapabilityGrant / SecretRef;
- PlatformCapabilityDescriptor / PlatformCompatibilityAssessment;
- TelemetryContext / SupportClaim.

`ControlPlaneIncarnation` remains a plausible disaster-recovery fencing realization rather than a concept at 006-A exit, but 006-B must still test whether regressive-restore semantics expose missing temporal-authority purpose or synchronization.

## Structured-data capability evidence

The Phase 006 design scope now explicitly considers three capability shapes:

1. single-table generation;
2. time-series-based table generation;
3. multi-table generation with shared-key relationships.

A future API may permit an actor to select one of these shapes through a function parameter, typed specification, builder or equivalent convenience surface.

However, **selection syntax is not semantic authority**. The selected shape must still expose/bind the underlying meaning, relationship/ordering, validity, Strategy capability, Generation scope, Evaluation and historical facts required for the workflow.

## Single-table assessment

**Disposition: existing baseline capability; no new concept required.**

The current eleven concepts compose cleanly for ordinary single-table structured synthesis.

A standalone `Table`, `Dataset`, `GenerationMode` or `DataTopology` concept is not justified merely because a function may select single-table operation.

## Time-series assessment

**Disposition: required Phase 006 design target; no new concept accepted yet.**

Existing ownership already covers much of time-series semantics:

- timestamp/entity semantic roles → Data Meaning;
- temporal validity/monotonicity/cadence requirements → Constraint;
- requested horizon/continuation/quantity → Generation;
- support/limitations → Synthesis Strategy;
- temporal fidelity and uncertainty → Evaluation Criterion / Evaluation / Evidence.

The unresolved question is whether reusable descriptive sequence structure—for example records sharing one entity identity and ordered by one temporal role—belongs entirely inside Data Meaning or is better represented through a generic Relationship concept.

006-A rejects immediate creation of separate `Series`, `Temporal Structure`, or `TimeSeriesMode` concepts. 006-G must use time-series as a falsification case for the Relationship candidate.

## Multi-table shared-key assessment

**Disposition: strong evidence to reopen the deferred `Relationship` candidate.**

Multi-table synthesis introduces a descriptive linkage that is not naturally identical to either:

- Data Meaning such as `customer_id is an identifier`; or
- Constraint such as `every child key must resolve to a parent`.

The reusable descriptive fact that one logical scope/key role relates to another logical scope/key role has a plausible independent purpose and revision lifecycle.

006-A therefore formally reopens `Relationship` for 006-G concept discovery.

It remains **provisional**. The accepted catalog remains eleven concepts until later Phase 006 authority explicitly accepts a change.

## Candidate Relationship boundary hypothesis

A later accepted Relationship concept, if justified, would likely own reusable descriptive linkage among logical scopes/record roles, such as:

- participant scopes/roles;
- linkage/key-role semantics;
- descriptive cardinality/participation;
- temporal sequence partition/ordering semantics where genericity survives testing;
- revision/history/authority of that relationship description.

It would not absorb:

- individual field meaning → Data Meaning;
- prescriptive referential/cardinality/temporal validity rules → Constraint;
- request-specific output set/horizon/quantity → Generation;
- Strategy support/limitations → Synthesis Strategy;
- historical derivation/use relationships → Provenance.

006-G must attempt to falsify this boundary rather than accepting it from terminology alone.

## Function-parameter conclusion

The user's proposed control surface is compatible with the design **as an experience/API choice**.

Conceptually, a future surface may be equivalent to:

```text
single_table
time_series
multi_table
```

but the parameter may only select the workflow/capability profile. It cannot be the sole durable representation of:

- participating scopes;
- shared keys;
- sequence/entity/time roles;
- cardinality;
- ordering;
- validity requirements;
- completion across a logical output set;
- required Evidence.

The exact public API remains downstream representation work.

## Concept and synchronization count

At 006-A exit:

```text
accepted concepts             11
accepted synchronizations     15
new accepted concepts          0
new accepted synchronizations  0
reopened candidate concepts    Relationship
```

No existing concept is split or merged by 006-A.

## Scope-boundary classification

006-A intentionally does not decide that all three generation shapes must ship in the first implementation.

Current design status:

- **single-table** — current baseline capability;
- **time-series** — required Phase 006 design target; first-implementation inclusion TBD;
- **multi-table shared-key** — required Phase 006 design target; first-implementation inclusion TBD; Relationship candidate reopened.

This distinction lets Phase 006 validate future extensibility without expanding first-release scope automatically.

## Downstream consequences

### 006-B

Proceed with operational temporal-authority/disaster-recovery refinement. The word `temporal` in 006-B concerns authority over time after rollback/restore and MUST NOT be confused with time-series data semantics.

### 006-C

Adversarial scenarios should include topology-sensitive cases such as:

- partial multi-table output;
- parent/child output mismatch;
- retry across coordinated table materializations;
- interrupted time-series continuation;
- Evidence bound to one exact multi-part logical result;
- history/recovery when one part of a coordinated output is unavailable.

### 006-D

Algorithm-neutrality probes must now include topology diversity:

- Learning-based single-table deep-generative family;
- direct/simple single-table path;
- time-series Strategy shape;
- multi-table shared-key Strategy shape;
- representative deterministic/bounded and statistical/approximate Evaluation methods.

No algorithm is implemented during Phase 006.

### 006-G

006-G is broadened from a relational-only audit into a structured-data topology concept/extensibility audit covering **single-table, time-series and multi-table shared-key** behavior.

It must decide whether:

1. the existing eleven concepts remain sufficient;
2. one generic Relationship concept should be accepted;
3. temporal sequence semantics require a separate concept;
4. another narrower concept boundary is required.

### 006-H / 006-I

Any new accepted Relationship/temporal semantics must be propagated deliberately into experience, architecture, synchronizations and the Phase 005 implementation-planning baseline. Phase history is not rewritten.

## Backlog impact

006-A keeps BDR-001 through BDR-004 open.

It sharpens BDR-004 so initial-scope/future-extensibility closure includes the three structured-data topology shapes above. Time-series is added as an explicit baseline-scope decision rather than being hidden under generic single-table terminology.

## Exit assessment

**Status: complete.**

Findings:

- Phase 005 mechanisms have not accidentally become concepts;
- `ControlPlaneIncarnation` remains a recovery mechanism hypothesis pending 006-B;
- `GenerationMode`/`DataTopologyMode` is rejected as a standalone concept;
- single-table generation remains conceptually supported by the existing catalog;
- time-series generation is now an explicit design target;
- multi-table shared-key generation reopens the deferred `Relationship` candidate;
- the accepted concept/synchronization counts remain unchanged pending 006-G.

## Next group

**006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement**.