---
type: Phase Record
title: 007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation
status: complete
---

# 007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation

## Objective

Refine the distributed data-state and output-promotion architecture beneath the 007-D identity and 007-E persistence foundations without allowing Phase 005-E implementation planning or the provisional 007-A through 007-C scaffold to freeze file formats, Spark APIs, provider models, manifests, fencing, or tests prematurely.

007-F remains architecture/design work under the Phase 007 implementation freeze.

## Governing authority reviewed

007-F reconciled and refined:

- `docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md`;
- `docs/architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md`;
- `docs/authority/structured-data-topology-relationship-semantics-contract.md`;
- `docs/architecture/phase-006-architecture-reconciliation-contract.md`;
- `docs/architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md`;
- ADR-0003;
- the historical Phase 005-E implementation plan as downstream planning evidence.

## Result

**PASS — DISTRIBUTED DATA-STATE / STRUCTURED-TOPOLOGY / MANIFEST / CANDIDATE-SEAL / PROMOTION FOUNDATION REFINED AS ARCHITECTURE DESIGN.**

Canonical result:

`docs/architecture/phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md`

## Core separation

007-F preserves the architecture ladder:

```text
mutable selector / access object
        ↓
exact logical source/data state
        ↓
open distributed candidate/materialization
        ↓
immutable sealed whole-subject representation
        ↓
owner validation / completion basis
        ↓
Generation promotion
        ↓
one logical completed-output identity
```

A DataFrame, table, path, file set, provider object or manifest is not semantic authority by existence alone.

## Logical subject / physical representation split

A logical data subject describes what coordinated state is being referenced.

A physical representation describes where/how that exact subject can be read and how its physical extent/integrity are established.

The same logical output may later acquire another equivalent representation without rewriting the original promotion basis, while physically similar representations do not automatically mean the same logical subject.

## Logical scope foundation

A distributed subject may contain one or more stable logical scopes, such as customer, order or observation record collections.

Logical scope is an architecture addressing role, not a new `Table`, `Dataset`, `Series` or `DataTopology` concept.

Time-series entities are not represented as one control-plane scope per entity; entity/series membership remains Data Meaning over distributed records.

## Structured topology

The representation model supports:

- single-table;
- time-series;
- multi-table shared-key;
- composite relational + time-series subjects.

Topology presets remain summaries/convenience syntax rather than durable authority.

The exact subject binds participating scopes plus the exact Data Meaning revisions/structural assertion references required to interpret them.

Physical foreign keys, timestamps, storage nesting and partition order remain representation facts rather than semantic topology authority.

## Source exactness and coordination

007-F distinguishes at least these data-state guarantee dimensions:

```text
identity strength
read-binding strength
integrity coverage
retention / rereadability
cross-scope coordination strength
```

A strong guarantee in one dimension does not imply the others.

A key new refinement is that two individually exact source scopes do not automatically form one coherent multi-scope snapshot.

For example:

```text
customers C42
orders    O91
```

may each be historically exact while lacking a shared transactional/coordinated cut.

If committed semantics require stronger cross-scope coherence, readiness must establish an adequate coordination basis or report limitation/incompatibility.

## Scope-aware manifest architecture

The manifest remains a representation mechanism.

A whole-subject root may resolve:

```text
whole subject root
  scope customers    -> exact sealed representation
  scope orders       -> exact sealed representation
  scope observations -> exact sealed representation
  coordination / closure basis
        ↓
distributed/hierarchical component detail
```

The control plane remains bounded. Millions of files/components, rows, keys or series are not enumerated into ordinary canonical control state merely to establish identity.

## Candidate foundation

A Generation candidate is subordinate non-final physical materialization.

A multi-scope candidate may make partial progress such as:

```text
customers      closed
orders         materializing
observations   not started
```

This remains candidate progress, not completed output.

Scope-local physical closure can support retry/recovery/diagnosis, but a whole candidate cannot seal until every mandatory constituent required by the committed Generation scope is physically closed under the representation contract.

## Seal boundary

Whole-candidate sealing establishes an immutable exact physical subject to a declared identity/integrity strength.

It establishes physical closure such as required scope presence, immutable constituent membership, structural rereadability, writer exclusion at the sealed boundary and bounded root resolution.

It does **not** establish:

- referential-integrity Constraints;
- temporal Constraints;
- Generation quantity/horizon success merely from a weak estimate;
- fidelity;
- privacy/disclosure safety;
- favorable Evidence;
- semantic Generation completion;
- release approval.

This means a candidate may seal successfully and then fail semantic validation. The seal remains useful because Evaluation can identify the exact failed subject reproducibly.

## Time-series boundary

Physical file/partition sorting does not establish semantic sequence order.

A time-series subject retains exact Data Meaning references defining entity membership and temporal/order roles, while physical ordering metadata remains optional representation information.

## Multi-table boundary

A whole multi-table subject binds exact representations for all participating scopes plus exact structural-relationship assertion references.

Shared-key values are not materialized into the control plane merely to represent topology.

Referential/cardinality validity remains distributed Constraint/Evaluation work.

## Evaluation subject boundary

Any Evaluation used as a Generation completion prerequisite must bind the exact sealed subject it examined.

Whole-topology Criteria bind the root coordinated subject; scoped Criteria may bind one exact constituent plus the required topology context.

A new materially different sealed subject does not inherit prior completion Evidence automatically.

Detailed Evaluation/Evidence architecture remains 007-I work.

## Promotion foundation

Promotion remains a Generation-owned semantic transition.

A storage provider or sealed candidate cannot promote itself.

Where the control facts share one atomic persistence boundary, Generation completion, completed-output establishment, exact sealed representation binding and required local history should become visible together under 007-E.

One successful Generation establishes at most one primary logical completed output under the current concept contract.

Promotion may reuse the exact sealed distributed bytes/table snapshot in place and therefore does not require a second full-corpus copy.

Reserving an output identifier before promotion is allowed as a mechanism but does not establish the semantic completed output.

## Representation evolution

Later compaction, relocation, re-encoding or replication may remain another representation of the same logical output only when sufficient equivalence is established for the claimed use.

The exact original sealed promotion basis remains historical fact even when another representation becomes preferred for current access.

A transformation that changes values, semantic topology, required records or series membership cannot be hidden as mere representation maintenance.

## Retention and recovery

If promoted payloads expire, the logical output/history remains established while payload resolution may become unavailable.

If candidate/output files survive a control-state restore, physical existence does not prove semantic promotion or current writer authority.

Recovery/adoption requires current authority and sufficient owner completion evidence; detailed fencing/recovery remains 007-H.

## Scale boundary

007-F preserves enterprise-scale distributed behavior:

- bounded roots/scope summaries in control state;
- distributed/hierarchical/provider-native component detail;
- no ordinary full-corpus `collect()`/`toPandas()` requirement;
- no driver-local enumeration of millions of components;
- no control row per time-series entity by default;
- no control-plane enumeration of multi-table key domains;
- distributed seal/integrity/extent work where required;
- resource pressure cannot silently drop required scopes, rows, horizons or validations.

## Phase 005-E technology disposition

The earlier implementation plan proposed concrete choices such as:

- PySpark package/interface boundaries;
- `SourceStateRef`, `CandidateMaterializationRef` and `SealedDataSnapshotRef` names;
- a portable Parquet manifest profile;
- concrete Spark selectors/access classes;
- package/module ownership and provider interfaces.

007-F preserves the responsibilities but does not treat these spellings/technologies as settled architecture.

Parquet remains one possible implementation profile rather than a required data-plane format.

## Falsification scenarios reviewed

007-F tested the architecture against:

- a mutable source advancing after exact source commitment;
- individually exact tables lacking a coherent shared source cut;
- partial multi-table candidate materialization;
- physically unsorted time-series storage;
- physically sealed multi-table data later failing referential integrity;
- readable candidate data before promotion;
- duplicate physical components from retry/speculation;
- metadata-only promotion reusing sealed bytes;
- later compaction of a promoted output;
- complete payload expiry with retained logical history;
- restored control state finding surviving `final` files;
- composite relational/time-series output topology.

The architecture remained coherent without a new concept, synchronization or ADR.

## Concept / synchronization / ADR audit

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts               0
new synchronizations       0
new ADRs                    0
SYNC-16                     absent
```

`DataState`, `LogicalScope`, `Manifest`, `Candidate`, `Seal`, `Snapshot`, `CoordinationBasis`, `RepresentationBinding` and `PromotionBinding` remain architecture mechanisms.

ADR-0003 remains sufficient and is refined rather than superseded.

## Explicitly deferred

007-F intentionally does not select:

- data-reference classes/field formats;
- scope-ID format;
- manifest schema/encoding;
- file/table/object format;
- Parquet/Delta/Iceberg/Hudi choice;
- object-store/catalog provider;
- checksum/digest algorithm;
- exact component-index structure;
- writer-fence mechanism;
- candidate reseal/workspace mechanics;
- copy-on-promotion policy;
- representation-equivalence algorithm;
- retention/cleanup policy;
- exact Spark/PySpark public interfaces;
- provider capability API;
- distributed manifest implementation;
- source snapshot materialization algorithm;
- tests or architecture-fitness enforcement.

## Repository change boundary

007-F changes architecture/documentation only.

It introduces:

- no source behavior;
- no Spark dependency or adapter;
- no data format/provider dependency;
- no manifest implementation;
- no candidate/seal/promotion code;
- no persistence/data-plane schema;
- no tests;
- no Import Linter rules;
- no CI/deployment enforcement.

The retained Phase 007-A through 007-C scaffold remains provisional implementation evidence.

## Exit decision

**007-F DESIGN: COMPLETE.**

**007-F IMPLEMENTATION: NOT AUTHORIZED.**

The next eligible **design** subgroup is:

**007-G — Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation**.

007-G does not begin automatically; explicit proceed authority is required.
