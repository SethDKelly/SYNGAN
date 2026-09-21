---
type: Discovery Evidence
title: Structured-Data Topology & Relationship Concept/Extensibility Audit
status: historical
---

# Structured-Data Topology & Relationship Concept/Extensibility Audit

## Purpose

Preserve the 006-G falsification evidence used to decide whether the reopened `Relationship` candidate should become a standalone SYNGAN concept and to close the initial structured-topology scope decision.

This document is discovery evidence. Accepted authority lives under `docs/authority/`, `docs/concepts/`, and `docs/synchronizations/`.

## Evidence introduced before 006-G

Phase 006 established three desired capability families:

```text
single-table generation
time-series generation
multi-table generation with shared-key linkage
```

006-A reopened `Relationship` because multi-table shared-key linkage appeared to have descriptive meaning independent of referential-integrity Constraints, and time-series supplied a test of whether the same idea could express reusable sequence membership/order.

006-C showed that coordinated Generation/Execution/Evaluation can already preserve whole-result completion without a new synchronization.

006-D showed that single-table, time-series and multi-table Strategy/runtime shapes fit the current Strategy/Learning/Learned-State/Generation architecture.

006-E established topology-specific scale dimensions without introducing a topology concept.

006-F showed that privacy/disclosure Evaluation may need joined multi-table and longitudinal/trajectory subjects.

## Candidate alternatives

006-G compared five alternatives.

### Alternative A — accept generic `Relationship` as a standalone concept

Potential purpose:

> Describe reusable structural relationships among logical data subjects independently of any one synthesis activity or prescriptive rule.

Potential state/actions:

- declare endpoints/roles;
- describe linkage/order/cardinality semantics;
- revise/correct;
- review;
- supersede/invalidate;
- bind into Learning/Generation/Evaluation.

Weakness: these actions, lifecycle states, authority and revision semantics substantially duplicate Data Meaning.

### Alternative B — subordinate structural relationship assertions to Data Meaning

Data Meaning owns descriptive structural interpretation such as:

- key/identifier role;
- which logical key roles correspond across scopes;
- series/entity membership roles;
- which field establishes temporal/order role;
- descriptive cardinality/participation facts when they are meaning rather than requirements.

Constraint separately owns prescriptive rules such as referential integrity, uniqueness, monotonicity, mandatory participation or cadence validity.

Generation separately owns requested topology/scope/horizon/quantity.

This alternative reuses existing revision/binding authority through Data Meaning.

### Alternative C — absorb relationship semantics into Constraint

Rejected because:

```text
orders.customer_id refers to customers.customer_id
```

can be descriptive meaning even when the project does not require every child key to resolve.

The requirement:

```text
every orders.customer_id must resolve to customers.customer_id
```

is prescriptive and belongs to Constraint.

Collapsing the two would violate the established descriptive/prescriptive boundary.

### Alternative D — absorb topology into Generation

Rejected because relationships and sequence roles can be declared/reused/revised independently of one Generation.

Generation owns which logical scope/output topology is requested, not the underlying reusable semantic interpretation.

### Alternative E — introduce a broader `Data Topology` concept

Rejected as too representation-oriented/generic. It risks becoming a container for tables, keys, sequence structure, schema, physical layout and request mode without a distinct SYNGAN-specific lifecycle beyond existing Data Meaning/Generation authority.

## Jackson criteria review for standalone Relationship

### R1 — distinct purpose

**Partial pass.** Describing structural linkage is meaningful, but the purpose is a specialized form of semantic interpretation already covered by Data Meaning.

### R2 — meaningful state/history

**Pass as a distinction, weak as a separate concept.** Relationship assertions have meaningful historical state, but Data Meaning revisions already provide exactly the required historical ownership.

### R3 — actions/lifecycle

**Weak.** Declare/review/revise/supersede/invalidate mirrors Data Meaning nearly one-for-one.

### R4 — independent change

**Partial pass.** A relationship can change while field roles stay unchanged. But one semantic assertion inside a Data Meaning revision can likewise change independently without requiring a new concept.

### R5 — authority independence

**Weak.** The natural authority is generally the same data/domain steward authority that owns semantic interpretation. No independent organizational authority is required by the current product purpose.

### R6 — genericity/domain specificity

**Risk.** A very generic Relationship concept could expand into arbitrary graph semantics, foreign-key catalogs, schema relationships, lineage edges or workflow relationships. Keeping structural assertions under Data Meaning bounds the purpose to synthesis-relevant data semantics.

### R7 — representation independence

Both A and B can be representation-independent.

### R8 — synchronization economy

**Strong evidence against separation.** A standalone Relationship would need binding/compatibility/applicability/history coordination with Data Meaning, Strategy, Learning, Generation, Constraint, Evaluation and Provenance. Subordination to Data Meaning reuses SYNC-01 and existing contextual compatibility/Constraint rules.

### R9 — scale significance

Scale strengthens the need to represent relationships but does not create an independent lifecycle.

### R10 — outcome coverage

The distinction materially enables multi-table/time-series synthesis, but that outcome remains covered when the state is Data Meaning-owned.

### R11 — non-duplication

Standalone Relationship fails this criterion under the current evidence because its descriptive purpose/state/history overlap Data Meaning substantially.

### R12 — operational-principle readiness

A standalone scenario can be written, but it is indistinguishable from a specialized Data Meaning declaration/revision scenario.

## Disposition

**Standalone `Relationship` is rejected for the current catalog and reclassified as Data Meaning-owned structural relationship semantics.**

This is not loss of the semantic distinction.

The design must support inspectable, attributable, revision-bound structural relationship assertions where topology requires them.

## Multi-table shared-key analysis

A multi-table logical scope may contain structures equivalent to:

```text
customers.customer_id
    parent/shared-key role

orders.customer_id
    child/shared-key role

orders.customer_id
    relates to
customers.customer_id
```

Data Meaning owns the descriptive relationship.

Constraint may separately state:

```text
every order customer key resolves
customer key unique in customers
child count within domain limit
```

Generation owns:

- participating logical scopes;
- requested quantities/cardinality semantics per scope where applicable;
- requested output topology;
- mandatory/best-effort Conditions;
- whole-result completion.

Strategy owns whether it can synthesize the declared relationship/topology shape.

Evaluation/Evidence may examine referential fidelity, cardinality distribution, utility, disclosure risk or other Criteria over the coordinated subject.

## Time-series analysis

A time-series table may need meaning equivalent to:

```text
entity_id
    identifies sequence/entity membership

event_time
    establishes temporal/order role

records sharing entity_id
    participate in one logical sequence
    ordered by event_time
```

These are descriptive semantics and fit Data Meaning.

Constraint owns prescriptive temporal rules such as:

- monotonic/nondecreasing timestamps;
- unique time points when required;
- cadence/gap bounds;
- allowed horizon/domain validity;
- cross-field temporal validity.

Generation owns requested series/entity scope and requested future/history horizon.

Strategy owns sequence-generation capability and limitations.

Evaluation/Evidence owns temporal fidelity/validity/privacy questions.

No `TimeSeries`, `Series`, `Sequence`, or temporal Relationship concept is justified.

## Composition falsification

A mutually exclusive topology enum is insufficient as the sole semantic representation.

Valid future shapes can include:

```text
multi-table
  ├── customers
  └── observations
        └── time-series per customer
```

or multiple related time-series tables.

Therefore `single_table`, `time_series`, and `multi_table` may be useful API presets/capability labels, but the durable semantic model must permit composition through logical scope + Data Meaning structural assertions + Generation intent.

## Single-table result

Single-table remains valid without fabricated structural-relationship state.

A table may still contain multi-field Data Meaning and Constraints, but no relationship assertion is required merely because the common topology vocabulary includes one.

## Initial product capability scope

006-G accepts the first complete SYNGAN structured-data capability baseline as including all three families:

1. **single-table**;
2. **time-series**;
3. **multi-table shared-key**.

Implementation may be delivered in dependency-safe stages and individual Strategies may support only a subset.

However, the first complete baseline release must have at least one supported self-contained Strategy path for each family before claiming the complete structured-data baseline.

The multi-table baseline targets explicit shared-key relationships and common cardinality/participation shapes. Arbitrary recursive/cyclic graph synthesis is not promised universally; a Strategy may explicitly support or reject such shapes.

The time-series baseline targets explicit entity/series and order/time semantics without requiring all sequence algorithms or regular cadence.

## Topology selection/API consequence

A future convenience function may expose something equivalent to:

```text
mode="single_table"
mode="time_series"
mode="multi_table"
```

but that token is not sufficient durable semantic authority.

The committed work must retain the actual logical scope, structural relationship assertions, temporal/entity roles, topology-specific Generation intent and required Constraints/Evaluation context.

Advanced/composite topology must not be made impossible by an exclusive enum.

## Relationship assertion reference consequence

Constraints, Strategy compatibility, Generation, Evaluation and Provenance may need to refer to one specific structural assertion.

Architecture may therefore provide a stable assertion identifier/reference scoped to an exact Data Meaning revision.

That addressing requirement does not create a standalone Relationship concept/resource.

## Scenario replay

006-G conceptually replayed the 006-C topology-sensitive cases after this disposition:

- partial multi-table output;
- parent/child key mismatch;
- interrupted time-series continuation;
- temporal validation;
- joined/trajectory disclosure-risk Evaluation;
- multi-table/time-series scale pressure.

The cases remain coherent under existing SYNC-01/02/03/06/08/09/10/12/14/15 with structural relationship semantics owned by Data Meaning.

No new synchronization is required.

## Exit evidence

The strongest evidence favors **subordination to Data Meaning**, not promotion to a twelfth concept.

This yields a smaller model while preserving the exact semantics needed for single-table, time-series, multi-table and future composite topologies.