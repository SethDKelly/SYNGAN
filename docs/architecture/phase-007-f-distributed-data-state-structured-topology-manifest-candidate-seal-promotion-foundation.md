---
type: Architecture Authority
title: Phase 007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation
status: active
---

# Phase 007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation

## Purpose

Refine SYNGAN's distributed data-state architecture for exact source-state binding, composable structured topology, bounded manifested physical representation, Generation candidate materialization, immutable sealing, coordinated whole-result promotion, partial failure, and later representation evolution **without selecting a file/table format, provider, manifest serialization, Spark API class, object-store layout, table-format transaction model, or executable verification implementation**.

007-F continues the architecture/design track governed by the [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md). It is design authority, not permission to implement data-plane behavior.

## Governing authority

007-F is downstream of:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
- [Phase 007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md);
- [Phase 007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md);
- [Structured-Data Topology & Relationship Semantics Contract](../authority/structured-data-topology-relationship-semantics-contract.md);
- [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md);
- accepted concepts, synchronizations and experience authority.

Earlier Phase 005-E choices such as a portable Parquet profile, concrete reference/class names, exact package extras and provider interfaces remain implementation-planning evidence. They are not binding architecture during the current design freeze.

## Design result

007-F accepts this distributed-data foundation:

> **A distributed data state is identified by an exact logical subject and a declared physical identity/read/integrity basis; neither a DataFrame, table/path alias, provider object nor manifest by itself becomes semantic authority.**

> **Structured topology is represented as a bounded logical-scope composition bound to exact Data Meaning structural semantics, while row-scale/entity-scale data and physical components remain distributed.**

> **Sealing establishes an immutable, closed physical subject to a declared strength. It does not establish Constraint satisfaction, privacy, Generation completion or release approval.**

> **Generation promotion binds one logical completed-output identity to one exact sealed coordinated subject after the owning Generation completion requirements are satisfied. Promotion may be metadata/control-plane-only and need not copy the distributed payload.**

## 1. Data-state roles and non-concepts

007-F uses several architecture roles that are not new domain concepts:

- data state;
- logical scope;
- scope composition;
- selector/access object;
- exact source-state binding;
- representation binding;
- manifest/root manifest;
- component index/tree;
- candidate materialization;
- sealed snapshot;
- extent/integrity summary;
- promotion binding;
- representation-equivalence assertion.

None of these creates a universal `Dataset`, `Table`, `Series`, `Artifact`, `Manifest`, `Relationship`, `DataTopology`, or `Output` concept.

The accepted concept count remains unchanged.

## 2. Core data-state separation

Architecture preserves at least these distinct roles:

```text
mutable access / selector
        ↓ resolve / pin / snapshot
exact logical data state
        ↓ realize / materialize
open candidate or physical snapshot workspace
        ↓ close / seal
immutable manifested physical subject
        ↓ owner validation / promotion
promoted logical result
```

For Generation:

```text
Generation commitment
  exact semantic topology + required logical scope
        ↓
open candidate materialization
        ↓
sealed whole-candidate subject
        ↓
required Evaluation / Constraint / completion checks
        ↓
Generation promotion
        ↓
one completed logical output identity
```

Each step has different authority and must remain distinguishable even when one platform operation realizes several steps efficiently.

## 3. Logical subject and physical representation are different axes

### 3.1 Logical subject

A logical data subject describes **what coordinated data state is being referred to** for one source, candidate, Evaluation subject or completed result.

It may contain one or more logical scopes.

### 3.2 Physical representation

A physical representation describes **where/how the subject can be read and what physical state belongs to it**, potentially through:

- provider-native immutable snapshot identity;
- table/file/object versions;
- a bounded root manifest plus distributed component index;
- another immutable/versioned provider representation.

### 3.3 Separation invariant

A logical subject can survive representation relocation/re-encoding when equivalence is established strongly enough for the owning use.

Conversely, two representations with similar schemas/paths are not automatically the same logical subject.

## 4. Logical scope composition

### 4.1 Scope is a bounded addressing role

A **logical scope** is a bounded addressable portion of one coordinated data subject, such as a table-like record collection or another meaningful structured component.

Scope exists to support exact representation, topology binding, Evaluation targeting and whole-result closure.

It is not automatically an independently owned domain resource.

### 4.2 Scope identity within a subject

Architecture must permit scopes to be distinguished stably within the exact data-state subject so references can identify, for example:

```text
output O17
  scope customers
  scope orders
  scope observations
```

The exact scope-ID encoding is deferred.

A scope-local identifier without the parent data-state identity is not necessarily globally meaningful.

### 4.3 Logical scopes are not per-row/per-entity objects

For time-series data, millions of series/entities do not imply millions of control-plane logical scopes.

Entity/series membership remains described by Data Meaning roles and distributed row values. A time-series event collection may remain one logical scope containing many entity sequences.

This preserves bounded control-plane state.

### 4.4 Scope composition is not semantic Relationship authority

The data-state representation may say that scopes participate in one coordinated subject and may retain references to exact Data Meaning structural assertions.

It does not redefine what those relationships mean.

For example:

```text
subject scopes: customers + orders
Data Meaning assertion ref: orders.customer_id corresponds to customers.customer_id
```

The scope composition records participation/binding; Data Meaning owns the descriptive relationship semantics.

## 5. Composable structured topology

007-F must support representation of:

- single-table subjects;
- time-series subjects;
- multi-table shared-key subjects;
- composite subjects such as relational scopes containing sequence-bearing child/event scopes.

### 5.1 No exclusive topology discriminator as authority

A convenience classification may summarize a subject as `single_table`, `time_series`, `multi_table`, or similar.

That summary cannot be the sole durable topology representation.

The durable subject must retain enough exact context equivalent to:

- participating logical scopes;
- exact Data Meaning revision(s) governing their interpretation;
- structural assertion references where material;
- Generation-requested required scope/horizon/quantity semantics by reference or committed summary;
- applicable Constraint/Evaluation bindings by reference where required;
- representation binding per scope/subject.

### 5.2 Physical layout does not define semantic topology

The following do not independently establish SYNGAN topology meaning:

- one Spark DataFrame;
- one or several storage tables;
- foreign-key metadata;
- partition directory nesting;
- file naming;
- provider table relationships;
- sort order;
- a timestamp physical type.

They may realize or inform the committed semantic topology but cannot replace it.

## 6. Exact source-state architecture

### 6.1 Selector versus exact source state

Preparation may accept mutable or ephemeral access forms such as:

- a live Spark DataFrame;
- table/catalog alias;
- path/URI;
- query;
- provider object;
- external dataset version reference.

These are selectors/access mechanisms until they resolve to an exact source-state binding sufficient for the committed activity.

### 6.2 Exact per-scope state

For every source scope whose exact state matters, architecture must identify a stable state/read boundary strong enough that execution cannot silently observe later mutable contents instead.

Possible architectural bases include provider-native versions, immutable manifested snapshots, external authoritative snapshot identity or other equivalent mechanisms.

No one mechanism is required.

### 6.3 Exactness has several independent strengths

Architecture must avoid one unqualified `immutable=true` or `snapshot=true` claim.

Where material, source/data-state representation must be able to distinguish dimensions equivalent to:

1. **identity strength** — can this state be distinguished from another state?;
2. **read-binding strength** — can execution reread the exact state rather than a later/mixed state?;
3. **integrity coverage** — what physical bytes/components/membership are actually protected/verified?;
4. **retention/resolvability** — is the referenced state expected to remain rereadable for the required period?;
5. **cross-scope coordination strength** — for multi-scope subjects, what establishes that the set of scope states forms the intended coordinated cut?

A strong claim in one dimension does not imply the others.

## 7. Multi-scope source coordination

### 7.1 Exact individual scopes do not imply one coherent cut

Suppose:

```text
customers at version C42
orders at version O91
```

Both states may be individually exact while their pair does not correspond to one transactionally coherent domain moment.

007-F therefore requires multi-scope source subjects to preserve a declared **coordination basis/strength** where cross-scope consistency matters.

### 7.2 Coordination bases

A coordinated source subject may be justified by mechanisms equivalent to:

- one provider-native atomic multi-scope snapshot/version;
- a transaction/read frontier shared across scopes;
- immutable scope snapshots captured under an explicit coordination protocol;
- externally authoritative coordinated snapshot identity;
- independently exact scope states where the committed semantics explicitly do not require stronger cross-scope simultaneity.

No one realization is selected.

### 7.3 Readiness consequence

If the committed Learning/Generation/Evaluation semantics require a coordinated source cut and the provider can establish only independently exact scopes without sufficient coordination, readiness must report limitation/incompatibility or block commitment.

It must not silently promote individual exactness into cross-scope coherence.

## 8. Structural descriptor versus Data Meaning

Physical representation may preserve structural facts required for safe reading, such as:

- field/column names;
- physical types/nullability;
- nested representation;
- partition/bucketing/layout hints;
- encoding/format/provider information;
- physical ordering/sort metadata where relevant to reading/performance.

This remains **structural representation**, not Data Meaning.

For time-series subjects:

```text
physical file/order metadata
        !=
semantic sequence order
```

Semantic entity membership and temporal order come from Data Meaning and applicable Constraints/Generation semantics.

## 9. Manifest role

### 9.1 Manifest is representation, not authority owner

A manifest identifies and closes the physical representation of an exact data state to a declared strength.

It does not own Generation, Data Meaning, Constraint, Evidence, Provenance, authorization, privacy, or release semantics.

### 9.2 Bounded root, distributed detail

A manifested state may contain millions of files/objects/partitions/components.

The control plane must not require all component membership to be stored in one canonical control row or loaded into one driver/client collection.

Architecture therefore permits:

```text
bounded root manifest / snapshot descriptor
        ↓
logical-scope entries or nested roots
        ↓
distributed/hierarchical component index
        ↓
physical provider components
```

A provider-native immutable table/multi-table snapshot may collapse some levels when its guarantee is sufficient.

### 9.3 Logical-scope-aware root

For a multi-scope candidate/source/output, the root must be capable of identifying the exact constituent logical scopes and their representation bindings without requiring one flat physical file list.

Conceptually:

```text
whole subject root
  scope A -> sealed representation A
  scope B -> sealed representation B
  scope C -> sealed representation C
  coordination / closure basis
```

This is a responsibility model, not a committed schema.

## 10. Candidate materialization model

### 10.1 Candidate is subordinate Generation material

Generation may create one or more distinguishable non-final candidate materializations during its fulfillment/recovery history.

Candidate identity exists for operational ownership, sealing, Evaluation binding, diagnosis and recovery.

It is not the completed-output semantic identity.

### 10.2 Whole-candidate scope

A candidate corresponds to one attempted physical realization of the committed Generation output scope/topology.

It may contain multiple constituent scope materializations.

### 10.3 Partial physical progress is first-class

During materialization, states may include situations equivalent to:

```text
customers      physically closed
orders         materializing
observations   not started
```

This is valid candidate progress.

It is not a completed logical output and must not be discoverable as such.

### 10.4 Scope-local physical closure is subordinate

Individual scope representations may become physically closed/sealed before the whole candidate can be sealed.

Such subordinate closure is useful for retry/recovery and may support scoped diagnostics, but it does not independently satisfy whole-Generation completion.

## 11. Candidate isolation and visibility

Default completed-output discovery must not confuse any of these with the promoted output:

- allocated/open candidate;
- partially materialized candidate;
- scope-sealed but whole-candidate-open material;
- whole-candidate sealed but unpromoted subject;
- failed candidate;
- cancelled candidate;
- quarantined/abandoned candidate.

A platform profile must provide enough isolation/versioning/labeling/resolution semantics to maintain that distinction.

If it cannot, readiness/compatibility must expose the limitation rather than relying on naming convention alone.

Authorized diagnostic access to candidate material may exist later but must preserve non-final status.

## 12. Writer/seal authority seam

007-F does not define Attempt/fencing mechanics; those remain for the Execution/recovery design.

However, data-state mutation/seal architecture must reserve a current-authority seam so stale/superseded writers cannot silently alter the subject treated as current.

Potential realizations may include Attempt epochs, writer fences, provider transaction versions, unique immutable namespaces, conditional manifest updates or other mechanisms.

No realization is selected here.

## 13. Sealing architecture

### 13.1 What sealing establishes

A whole candidate may become an exact sealed subject only when, to the declared representation/provider strength:

- the candidate is bound to the intended Generation commitment;
- the exact required logical scope set for this physical realization is known;
- every mandatory constituent representation required for whole-candidate closure is present;
- constituent membership/extent is closed to ordinary mutation under the sealed identity;
- no current authoritative writer can mutate that sealed membership;
- required physical component/index accounting is closed;
- required structural representation is coherent enough to reread;
- integrity/identity checks required by the representation contract succeed;
- the root can resolve the exact constituent scope representations and coordination/closure basis;
- the resulting sealed snapshot has immutable distinguishability from later material changes.

### 13.2 What sealing does not establish

Sealing does not prove:

- Condition fulfillment;
- referential-integrity Constraint satisfaction;
- temporal Constraint satisfaction;
- requested Generation quantity/horizon success beyond physical extent facts;
- statistical fidelity;
- privacy/disclosure safety;
- Evidence favorability;
- Generation semantic completion;
- current export authorization;
- external release/use approval.

Those remain owner-specific checks after an exact physical subject exists.

### 13.3 Mandatory scope source

Sealing does not invent which scopes are mandatory.

It closes the candidate against the exact committed Generation scope/topology obligations supplied by Generation authority.

### 13.4 Post-seal mutation

A sealed subject is immutable under its identity.

If material data/membership changes later, architecture must produce another distinguishable sealed subject.

007-F does not require whether that happens through a new candidate identity, a new generation within one candidate workspace, or another implementation mechanism; it only requires that the prior sealed identity never change meaning.

## 14. Whole-scope seal versus semantic cross-scope validation

For a multi-table candidate, whole-scope sealing establishes that all required scope representations belong to one closed candidate subject.

It does **not** automatically establish semantic relationships such as:

```text
every order.customer_id resolves to customers.customer_id
```

That remains a Constraint/Evaluation matter.

Likewise, a time-series scope may seal without proving monotonic timestamps or cadence validity.

This separation allows an exact immutable candidate to exist precisely so semantic validation can examine it reproducibly.

## 15. Physical extent and completeness facts

A sealed representation may preserve bounded physical facts such as:

- exact/estimated row count by scope;
- component/partition count;
- byte size;
- min/max physical partition statistics where useful;
- declared structural schema;
- identity/integrity basis;
- manifest closure status;
- scope presence;
- provider snapshot/version identity.

These remain physical facts.

Generation decides whether observed extent satisfies committed quantity/cardinality/horizon semantics.

An estimated extent cannot silently satisfy a requirement that demands exact quantity proof.

## 16. Time-series representation boundary

A time-series subject remains distributed and may be physically partitioned/sorted in many ways.

007-F requires only that the exact subject retain enough structural/semantic references to interpret:

- which logical scope contains the sequence-bearing records;
- which Data Meaning revision/assertions define entity membership and order roles;
- which Generation horizon/scope is committed;
- which representation contains the records.

Physical sort/order metadata may be retained as an optimization/representation property.

It is never sufficient by itself to establish semantic order or temporal validity.

## 17. Multi-table representation boundary

A multi-table subject may bind several logical scopes with separate physical representations.

The whole subject must preserve enough exact binding to identify:

- all committed participating scopes;
- exact representation state per scope;
- exact Data Meaning structural assertions used to interpret cross-scope relationships;
- coordination/closure basis;
- applicable whole-subject Evaluation/Constraint references where material.

It must not require materializing shared-key value sets into the control plane.

Referential/cardinality checks remain distributed Evaluation/Constraint work.

## 18. Composite topology boundary

A subject such as:

```text
customers
  └── observations
        entity/customer key
        time-series ordering by event_time
```

may be one coordinated logical output.

The representation does not need to classify it as either exclusively `multi_table` or `time_series`.

The scope composition plus exact Data Meaning/Generation bindings are authoritative.

## 19. Evaluation-subject binding

Any Evaluation used as a Generation completion prerequisite must bind the exact sealed subject it examined.

For whole-topology Criteria this means the root coordinated sealed subject, not merely one constituent scope.

For scoped Criteria the Evaluation may bind a selected exact scope representation plus the relevant topology/semantic context.

If any material constituent changes and a new sealed subject is created, prior completion Evidence does not automatically apply.

Detailed Evaluation/Evidence representation is refined in 007-I.

## 20. Promotion architecture

### 20.1 Promotion is owner-side semantic establishment

Promotion is the Generation-controlled transition that establishes the one logical completed-output result and binds it to the exact sealed physical subject that satisfied the completion basis.

A candidate seal cannot promote itself.

A storage adapter cannot mark Generation complete merely because a provider transaction succeeded.

### 20.2 Promotion input responsibilities

Conceptually, promotion needs exact context equivalent to:

```text
Generation commitment identity
expected current Generation state / concurrency context
exact sealed whole-candidate subject
required completion/Evaluation basis
current authorization / recovery qualification where required
```

The exact control API is deferred.

### 20.3 Atomic control transition

Where Generation completion, completed-output establishment, representation binding and required local material-history facts share one atomic control boundary, they should become visible together under 007-E.

Where a required post-promotion action crosses that boundary, durable intent/reconciliation rules apply.

### 20.4 One completed logical output

One successful Generation establishes at most one primary logical completed output under the current Generation contract.

Retries, speculative work, abandoned candidates or repeated physical dispatch cannot create multiple authoritative outputs for the same successful Generation.

### 20.5 Promotion may be metadata-only

Promotion does not universally require copying/renaming/re-writing the distributed payload.

If the exact sealed bytes/table snapshot already satisfy the representation contract, the completed output may bind that representation in place.

A provider/deployment may choose copy-on-promotion for isolation or compatibility, but copying is not semantic finality.

### 20.6 Reserved identifier is not result establishment

An implementation may reserve an output identifier before promotion for coordination convenience.

That reservation does not mean the completed-output semantic result exists before Generation successfully promotes it.

## 21. Representation evolution after promotion

A completed logical output may later acquire another physical representation without becoming a different logical output **only when the new representation is established equivalent to the required strength for that use**.

Potential examples include:

- compaction;
- physical relocation;
- re-encoding;
- provider-native migration;
- redundant replica creation.

### 21.1 Original promotion basis remains historical fact

The exact sealed representation used for original promotion remains part of historical provenance even if another representation later becomes preferred/current for access.

### 21.2 Representation change versus data change

A physical transformation that preserves the logical data state may be representation evolution.

A transformation that changes values, semantic topology, required records, sequence membership, or other material data meaning creates a distinguishable logical data state and cannot be hidden as mere representation maintenance.

### 21.3 Equivalence is strength-scoped

A schema match, row count or sample hash is not automatically enough to prove full representation equivalence.

The required proof depends on the claim/use and is left for later implementation/Evaluation design.

## 22. Retention and garbage-collection boundary

### 22.1 Candidate retention

Unpromoted candidates may eventually be cleaned according to retention/recovery/diagnostic policy.

Cleaning them must not erase canonical history required to explain what occurred.

### 22.2 Promoted representation retention

If all readable representations of a historical output expire, the logical completed-output identity/history may remain known while payload resolution becomes `unavailable` under 007-D/007-E.

Loss of payload availability does not rewrite the historical Generation into failure/non-occurrence.

### 22.3 No retention duration selected

007-F does not choose candidate TTLs, output retention periods, storage classes or cleanup algorithms.

## 23. Recovery and stale physical effects

After a control-state restore or coordinator failure, physical candidate/output material may survive even when canonical records are incomplete or regressed.

007-F preserves these rules:

- physical existence does not prove semantic promotion;
- a surviving candidate can be reconciled/adopted only under current recovery authority and sufficient evidence;
- an old writer cannot regain authority because its files still exist;
- a sealed subject may remain useful evidence if its identity/integrity can still be established;
- reconstructed promotion requires the normal owner completion basis, not merely finding a `final` path;
- unknown/indeterminate history remains possible.

Detailed operational recovery/fencing belongs to 007-H.

## 24. Scale consequences

The architecture must remain valid for hundreds of millions of rows and distributed component counts.

Therefore:

- normal control operations store bounded roots/scope summaries rather than row-scale state;
- manifest detail may be hierarchical/distributed/provider-native;
- no universal `collect()` / `toPandas()` / driver-local file-list enumeration is allowed as a requirement;
- time-series entity count does not become one control-plane record per series by default;
- multi-table shared-key domains are not enumerated into control persistence merely to represent topology;
- sealing/extent/integrity computation may itself be distributed;
- resource pressure may delay sealing/validation but cannot silently drop required scopes, rows, horizons or validation obligations.

## 25. Provider capability model

A future data-state provider profile must be able to declare capability/limitations equivalent to:

- exact historical snapshot identity;
- exact historical reread;
- snapshot retention semantics;
- per-scope and coordinated multi-scope snapshot support;
- bounded/hierarchical component indexing;
- candidate isolation;
- writer/seal authority integration;
- immutable seal support;
- extent/integrity proof strength;
- metadata-only promotion compatibility;
- representation-equivalence/relocation support;
- large-scale distributed read/write behavior.

Provider brand or table-format name is never the guarantee itself.

## 26. Phase 005-E implementation-planning disposition

Phase 005-E selected/proposed implementation details including:

- an optional PySpark extra/package boundary;
- concrete `SourceStateRef`, `CandidateMaterializationRef`, `SealedDataSnapshotRef` names;
- a portable manifested-Parquet profile;
- concrete Spark selector/access/provider classes;
- future package/file ownership;
- particular extent/identity descriptor names.

007-F does not reject those as implementation candidates.

It reclassifies them as implementation-planning evidence that must be re-evaluated during later implementation re-entry against this architecture.

In particular:

- Parquet is not a required architecture choice;
- directory/file manifests are not the only valid realization;
- a provider-native multi-table/table-format snapshot may satisfy the same contract;
- exact Python class/module spelling remains open;
- PySpark-facing APIs must preserve Spark-native distributed behavior, but 007-F does not freeze their concrete package/interface shape.

## 27. Falsification scenarios

007-F checked the architecture against the following scenarios.

### Scenario A — mutable table changes after commitment

A mutable table selector resolves to exact provider version V8; the table later advances to V9.

**Result:** committed work remains bound to V8; the selector remains only current access context.

### Scenario B — two exact tables are not one coherent snapshot

Customers C42 and Orders O91 are individually exact but captured under unrelated provider moments while the committed analysis requires cross-table consistency.

**Result:** per-scope exactness is insufficient; readiness requires adequate coordination basis or reports incompatibility/limitation.

### Scenario C — multi-table candidate partially completes

Customers seals, Orders is still open, Payments fails.

**Result:** subordinate scope progress exists but whole candidate cannot seal/promote while mandatory scope closure is missing.

### Scenario D — time-series files are unsorted

Physical partitions are not globally sorted, but entity/time Data Meaning is exact and readers can evaluate semantic order distributedly.

**Result:** physical unsorted layout does not invalidate identity; semantic temporal validity remains Constraint/Evaluation authority.

### Scenario E — whole candidate seals but referential integrity fails

All table representations are immutable and closed, then Evaluation finds orphaned child keys.

**Result:** seal remains valid as exact physical subject; Generation does not promote unless its completion rules allow the finding.

### Scenario F — candidate readable before promotion

A platform exposes sealed candidate files directly.

**Result:** readable bytes remain non-final. Completed-output discovery and actor experience must preserve candidate status/isolation.

### Scenario G — retry writes duplicate components

Two physical Attempts compute overlapping partitions/components.

**Result:** duplicate physical work is allowed; manifest/seal/fencing architecture must establish unambiguous current membership before seal.

### Scenario H — semantic promotion reuses existing bytes

A sealed candidate satisfies all completion requirements.

**Result:** Generation can establish one completed logical output by control-plane binding without copying every row.

### Scenario I — promoted output is compacted later

Files are compacted into fewer components with equivalent logical data.

**Result:** logical output may retain identity if sufficient equivalence is established; original promotion basis remains historical fact.

### Scenario J — all payload expires

Retention deletes readable output representations years later while canonical history remains.

**Result:** logical output remains historically established but payload resolution becomes unavailable.

### Scenario K — control database restore finds surviving `final` files

Physical files exist after restored control state no longer contains the promotion transition.

**Result:** file/path naming is not proof of promotion; recovery reconciliation must establish the owner transition or preserve unknown/indeterminate history.

### Scenario L — composite relational/time-series subject

Customer scope plus observations scope forms a relational subject in which observations are ordered per customer.

**Result:** scope composition + Data Meaning assertions represent both relational and temporal semantics without forcing one exclusive topology mode.

No scenario requires a new concept or synchronization.

## 28. Deferred architecture choices

007-F intentionally leaves open:

- exact data-reference class/field encoding;
- exact logical-scope identifier format;
- manifest wire/persistence schema;
- file/table/object format;
- Parquet/Delta/Iceberg/Hudi or another table-format decision;
- object-store/catalog provider;
- path/namespace convention;
- component digest/checksum algorithm;
- whether whole/scope seals are represented as distinct stored resources or nested descriptors;
- exact writer-fence mechanism;
- exact candidate workspace/reseal mechanics;
- copy-on-promotion policy by provider;
- representation-equivalence proof algorithm;
- retention/garbage-collection policy;
- Spark/PySpark public class/interface spelling;
- provider capability API shape;
- distributed manifest implementation;
- source-snapshot materialization algorithm;
- tests/fitness enforcement.

## 29. Concept and synchronization audit

007-F introduces **no new concept**.

`DataState`, `LogicalScope`, `Manifest`, `Candidate`, `Seal`, `Snapshot`, `RepresentationBinding`, `CoordinationBasis` and `PromotionBinding` remain architecture roles/mechanisms.

Accepted concept count remains **11**.

007-F introduces **no new synchronization**.

Existing synchronization authority remains sufficient, particularly:

- SYNC-01 exact Data Meaning revision binding;
- SYNC-02 Strategy/topology compatibility;
- SYNC-03 Constraint binding;
- SYNC-06 Generation scope/commitment;
- SYNC-07 Generation operational realization;
- SYNC-08 whole logical-output establishment;
- SYNC-09/10/11/12 exact Evaluation subject/method/realization/Evidence;
- SYNC-14 material Provenance;
- SYNC-15 reproducibility-relevant commitment snapshot.

Accepted synchronization count remains **15**. No `SYNC-16` is created.

## 30. ADR audit

007-F does not create a new ADR.

ADR-0003 already records the durable architecture decision to separate open candidate materialization, immutable sealed subject and semantic promotion while avoiding universal row-copy promotion.

007-F refines that accepted decision for multi-scope/time-series/composite topology and source coordination without reversing the chosen alternative.

## 31. Architecture invariants

1. DataFrame/table/path/provider object identity MUST NOT become canonical logical data-state identity merely because it is convenient.
2. Committed source-dependent work MUST bind an exact source state strong enough for its required read semantics.
3. Per-scope exactness MUST NOT be represented as cross-scope coherence without an adequate coordination basis.
4. Logical scope composition MUST remain bounded control metadata and MUST NOT enumerate every row/entity/series into canonical control state.
5. Scope composition MUST NOT take ownership of Data Meaning relationship semantics.
6. Physical schema/layout MUST NOT substitute for Data Meaning.
7. Time-series semantic order MUST NOT be inferred solely from physical file/partition order.
8. The manifest/root MUST remain bounded while component detail may remain distributed/hierarchical/provider-native.
9. An open or partial candidate MUST NOT be represented as a completed output.
10. Scope-local physical closure MUST NOT become whole-candidate closure when mandatory constituents remain unresolved.
11. Sealing MUST establish immutable physical subject closure to a declared strength and MUST NOT imply semantic validity.
12. Semantic referential/temporal/privacy/fidelity checks MUST remain outside manifest ownership.
13. A sealed subject MUST NOT mutate under the same identity.
14. Any material post-seal change MUST yield a distinguishable sealed subject.
15. Required completion Evaluation MUST bind the exact sealed subject it examined.
16. Generation promotion MUST remain owner-controlled and separate from physical write/seal success.
17. One successful Generation MUST NOT acquire multiple authoritative primary completed outputs through retries/duplicate physical work.
18. Promotion MUST NOT universally require distributed row-copying.
19. Reserving an output identifier MUST NOT establish the semantic output before promotion.
20. Physical representation evolution MUST NOT rewrite the original promotion basis.
21. Representation equivalence MUST be strength-scoped and MUST NOT be inferred from weak summaries alone.
22. Payload expiry MUST NOT rewrite historical semantic completion into absence/failure.
23. Surviving physical material after recovery MUST NOT prove promotion/current writer authority.
24. Distributed data-state handling MUST NOT require ordinary full-corpus collection or driver-local component enumeration.
25. Provider brand/table-format name MUST NOT substitute for explicit capability guarantees.
26. No rule in 007-F authorizes production implementation or executable design enforcement.

## Exit condition

007-F design is complete when:

- logical subject and physical representation responsibilities are explicit;
- source exactness and cross-scope coordination are separated;
- topology composition supports single-table, time-series, multi-table and composite subjects without a new concept;
- manifest/root architecture remains bounded and scope-aware;
- partial candidate, scope closure, whole-candidate seal and semantic promotion are distinct;
- whole-result promotion is exact-subject-bound and control-plane-safe;
- representation evolution/retention/recovery boundaries remain historically truthful;
- concrete provider/file/API/fencing/test decisions remain deferred;
- concept/synchronization/ADR audits are clean;
- implementation remains frozen.

The next architecture design group may then refine Strategy/method binding, dependency/security/runtime closure without requiring the current data-state representation to be implemented first.
