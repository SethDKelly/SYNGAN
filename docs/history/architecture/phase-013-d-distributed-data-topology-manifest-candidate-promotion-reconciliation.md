---
type: Architecture Reconciliation Authority
title: Phase 013-D — Distributed Data Boundary, Structured Topology, Manifest, Candidate/Seal/Promotion & Large-State Reconciliation
status: active
---

# Phase 013-D — Distributed Data Boundary, Structured Topology, Manifest, Candidate/Seal/Promotion & Large-State Reconciliation

## Purpose

Reconcile SYNGAN's retained distributed data-state architecture against the completed concept design, current synchronization authority, 013-B representation rules, and 013-C persistence/recovery rules before runtime and Execution architecture are reconciled.

013-D asks:

> **Can SYNGAN identify, coordinate, seal, evaluate, recover and promote Spark-scale structured data while preserving exact logical scope/topology and preventing physical/provider/manifest state from becoming semantic authority?**

Current answer:

```text
YES — THE DISTRIBUTED DATA-STATE SPINE REMAINS SOUND WITH BOUNDED CLARIFICATIONS.
NO AMAT-2 DATA-PLANE DEFECT IS FOUND.
NO AMAT-3 BLOCKER OR AR-9 UPSTREAM CONTRADICTION IS FOUND.
```

This authority is downstream of the completed Phase 012 concept design, current Phase 009/010 authority, the Phase 013 reconciliation method, 013-B representation reconciliation, and 013-C persistence/recovery reconciliation.

---

## 1. Reconciliation subjects

Primary retained subjects reviewed here are:

- `spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md`;
- `phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md`;
- `structured-data-topology-relationship-semantics-contract.md`;
- Generation's current candidate/completion/output semantics;
- ADR-0003 as rationale input;
- current Phase 009 synchronization ownership;
- 013-C exact-history, persistence and recovery-authority rules.

Writer/Attempt mechanics remain 013-F. Strategy/runtime distribution remains 013-E. Evaluation/Evidence/Provenance representation remains 013-G.

---

## 2. Governing distributed-data rule

> **A distributed physical state may establish an exact subject to a declared identity/read/integrity/coordination strength. It does not establish semantic meaning, Constraint satisfaction, Evidence, Generation completion, privacy, release authority or current mutation authority merely because it exists, is readable, is sealed, or was committed by a provider.**

The architecture therefore preserves distinct roles equivalent to:

```text
mutable selector / access representation
        ↓ exact resolution
exact logical data state
        ↓ physical realization
open / partial candidate materialization
        ↓ close to declared physical strength
immutable sealed physical subject
        ↓ owner-specific semantic validation
Generation result establishment / completed-output binding
```

These are architecture/representation roles. They are not a mandatory user workflow and do not create `Dataset`, `Manifest`, `Candidate`, `Seal`, `Promotion`, `Topology`, `Scope`, `Relationship`, or `Output` concepts.

---

## 3. Spark and large-state boundary

The retained Spark-scale boundary is retained.

A Spark DataFrame, table alias, path, query, provider object, catalog alias, file listing or in-memory object may be an access/locator representation. It is not sufficient historical identity when the referenced state can change materially.

Ordinary supported behavior must not require:

- full-corpus `collect()`;
- `toPandas()` for identity/completion;
- driver-local enumeration of every file/object;
- one control-plane row per generated record;
- one control-plane object per time-series entity;
- copying whole output merely to express semantic finality.

Bounded root references, scope summaries, provider-native immutable versions, hierarchical/distributed indexes and distributed validation remain valid realizations.

---

## 4. Exact data-state strength is multidimensional

013-D retains the Phase 007-F rule that exactness must not collapse into one boolean such as `immutable=true` or `snapshot=true`.

Where material, architecture must be able to qualify dimensions equivalent to:

```text
identity strength
read-binding strength
integrity / membership coverage
retention / future resolvability
cross-scope coordination strength
```

A strong claim in one dimension does not imply another.

Examples:

- a schema hash does not identify row content;
- a row count does not establish content equality;
- a sample fingerprint does not prove full-corpus equality;
- a provider commit does not establish Generation completion;
- exact per-table versions do not by themselves establish a coherent multi-table cut;
- physical readability does not establish finality.

Provider brand/product names are not guarantees. Architecture consumes only the guarantee actually established.

---

## 5. Structured topology reconciliation

Current topology semantics remain distributed across existing owners rather than becoming a `DataTopology` or `Relationship` concept.

### Data Meaning owns descriptive structure

Where material, Data Meaning owns reusable descriptive interpretation such as:

- identifier/key roles;
- cross-scope corresponding-key/parent-child association meaning;
- entity/series membership roles;
- temporal/order roles;
- descriptive cardinality/participation meaning.

### Constraint owns prescriptive validity

Prescriptive rules such as referential integrity, monotonic timestamps, uniqueness, cadence limits or required participation remain Constraint-owned.

### Generation owns requested result scope/topology fulfillment

Generation binds its requested logical scopes, quantity/cardinality/horizon semantics, topology-specific Conditions and exact relevant semantic authorities at commitment.

### Strategy owns reusable topology capability/limitations

Strategy declares whether it supports the relevant single-table, time-series, multi-scope/shared-key or composite shape.

### Evaluation/Evidence owns question/method/finding

Cross-scope or temporal Evaluation binds the exact subject it examines; Evidence cannot generalize from a narrower subject/coverage without sufficient support.

### Representation consequence

A convenience label such as:

```text
single_table
time_series
multi_table
```

may exist, but it is never the sole durable topology authority. The exact committed composition is established through logical scope plus the relevant owner bindings.

Composite forms remain representable; topology families are not permanently mutually exclusive.

---

## 6. Logical scope remains an architecture role

A logical scope is a bounded addressing role inside one coordinated data subject.

It supports:

- exact subject identity;
- physical representation binding;
- topology composition;
- Evaluation targeting;
- whole-result closure.

It is not automatically an independent domain resource or concept.

Scope identity is interpreted with its parent subject and exact semantic context. Row/entity/series membership remains distributed data plus Data Meaning semantics; millions of entities do not require millions of canonical control-plane scope resources.

---

## 7. Multi-scope source coordination

Exact individual scopes do not automatically form one coherent cross-scope state.

If committed semantics require a coordinated cut, architecture must preserve a coordination basis/strength sufficient for that requirement, such as an atomic provider snapshot, shared read frontier, explicitly coordinated immutable scope snapshots, or equivalent guarantee.

If independently exact scopes are sufficient for the committed semantics, architecture need not invent stronger simultaneity.

Readiness/compatibility must expose when the required cross-scope guarantee cannot be established; it must not silently upgrade weaker provider facts.

---

## 8. Manifest / snapshot role

A manifest is an architecture representation for an exact physical subject. It is not semantic authority.

The retained bounded-root model remains valid:

```text
bounded root subject / snapshot descriptor
        ↓
logical-scope entries or nested roots
        ↓
distributed / hierarchical component index
        ↓
physical provider components
```

A provider-native immutable/versioned snapshot may satisfy the same responsibility without materializing a literal SYNGAN manifest tree.

### Clarified seal rule

`Seal` means the architecture establishes an immutable, closed physical subject under a declared representation/provider contract.

It does **not** require a literal object named `Manifest`, a specific manifest serialization, an enumerated file list, or a separate stored `Seal` resource.

A provider-equivalent immutable snapshot boundary is valid when it establishes the required closure, identity, read and integrity guarantees.

This clarification prevents the historical term `manifest-gated` from becoming an implementation mandate.

---

## 9. What physical sealing establishes

To its declared strength, sealing may establish that:

- the intended physical subject is distinguishable and closed under its identity;
- required scope/component membership is closed to ordinary mutation;
- relevant representation/integrity checks have succeeded;
- the exact subject can be resolved consistently enough for owner validation;
- current authorized writers cannot silently mutate that sealed identity.

Sealing does not establish:

```text
Data Meaning correctness
Condition fulfillment
Constraint satisfaction
Evaluation validity
Evidence favorability
privacy / disclosure safety
Generation completion
external release / use approval
```

If material content changes after a seal boundary, the changed data must receive a distinguishable exact physical-subject identity.

---

## 10. Candidate materialization reconciliation

Candidate/partial materialization remains subordinate Generation representation state.

Architecture may distinguish physical states equivalent to:

```text
allocated / prepared
materializing / partial
scope-closed / whole-subject-open
whole-subject sealed
quarantined / abandoned
physical basis of promoted completed output
```

These states help recovery, Evaluation binding, diagnosis and data isolation. They do not replace Generation's semantic lifecycle.

A Generation may have multiple physical candidates over retry/recovery/resynthesis history while still producing zero or one successful logical completed output under current Generation semantics.

Default completed-output discovery must never present an open, partial, sealed-but-unpromoted, failed, cancelled, quarantined or abandoned candidate as the successful result.

---

## 11. Physical extent, quantity and approximation

A manifest/snapshot may preserve bounded physical facts such as row counts, component counts, byte sizes, scope presence, structural descriptors or provider snapshot identity.

Those facts do not decide semantic fulfillment.

Generation remains the owner of whether physical extent satisfies its committed quantity/cardinality/horizon/scope semantics.

Therefore:

- estimated extent cannot silently satisfy an exact-quantity requirement;
- sampled integrity cannot silently become full integrity proof;
- resource pressure cannot silently truncate required rows/scopes/horizon;
- approximation is valid only when the owning semantic contract permits it and its limitations remain explicit;
- physical success on one mandatory scope cannot become whole-result completion while another required scope is absent, violated or unresolved.

---

## 12. Evaluation subject binding

Any Evaluation used to satisfy a Generation completion requirement must bind the exact immutable physical subject it examined together with the semantic context needed to interpret that subject.

For a whole-topology Criterion, this may be the coordinated sealed root subject. For a scoped Criterion it may be an exact constituent scope plus the required topology/context references.

If a material constituent changes and a new exact subject is established, prior Evidence does not automatically apply to that changed subject.

This is subject identity discipline, not a new cross-concept owner.

---

## 13. Promotion / completed-output reconciliation

The historical term `promotion` is retained as an architecture name for the durable representation transition by which **Generation establishes its own completed-output result**.

Promotion is not:

- an independent concept;
- a generic storage/catalog lifecycle;
- a provider transaction status;
- a separate semantic owner;
- external publication/release.

Current ownership is:

```text
Generation owns candidate/finality/completion and completed-output association.
Architecture supplies exact sealed-subject identity + durable binding mechanics.
Execution supplies operational facts, not semantic completion.
Provider/storage state supplies only qualified physical facts.
```

The completed-output logical identity may reference the same underlying sealed bytes in place; semantic finality does not require whole-data copying.

A provider transaction, `final` path, catalog registration or physical table existence cannot independently establish the completed output.

Single-result cardinality remains Generation-owned: retries/speculation/recovery cannot create multiple authoritative successful outputs for one Generation.

---

## 14. Representation evolution after completion

A completed logical output may acquire another physical representation without becoming a new logical output only when equivalence is established strongly enough for the intended use.

Potential representation evolution includes compaction, relocation, re-encoding or replica creation.

The original promotion/establishment basis remains historical fact.

Representation equivalence remains strength-scoped. Schema similarity, row count or sampled fingerprint alone is not automatically sufficient for stronger equivalence claims.

If the transformation changes material values, semantic scope/topology, required records or other owner-relevant meaning, it is not mere representation maintenance.

---

## 15. Recovery and stale physical effects

013-C recovery rules apply directly to the data plane.

After coordinator/control-store failure or regressive restore:

- surviving bytes do not prove prior promotion;
- a `final` path or provider snapshot does not prove semantic completion;
- old writers do not regain authority because their material survives;
- immutable candidate material may be reconciled/adopted only under current recovery authority and sufficient exact context/integrity evidence;
- reconstructed promotion/completion requires the owning Generation completion basis;
- unresolved history remains unknown/unavailable/continuity-qualified where proof is insufficient.

Physical state is evidence to reconciliation, not current mutation authority.

---

## 16. Baseline structured-data scope

The current structured-data product baseline continues to include architectural support for:

1. single-table generation;
2. time-series generation with explicit entity/order semantics;
3. multi-table shared-key generation;
4. representation of composite topologies so combinations are not precluded by an exclusive topology enum.

Individual Strategies may support subsets. A complete structured-data capability claim still requires supported paths for the required baseline families under current product authority.

This does not pre-authorize arbitrary recursive graph lifecycle or streaming/session/feed concepts; those remain outside current scope or future rediscovery triggers as applicable.

---

## 17. Current synchronization reconciliation

The [Current Cross-Concept Synchronization Contract](../synchronizations/current-cross-concept-synchronizations.md) controls current numbering, scope and ownership.

For distributed-data architecture the relevant current semantics are:

```text
SYNC-01  exact Data Meaning revision binding when Data Meaning participates
SYNC-02  Strategy selection / contextual compatibility, including requested topology/scope
SYNC-03  Constraint binding / contextual handling when Constraint participates
SYNC-06  Generation / Learned State reuse compatibility and exact Learned State
         basis binding when reusable Learned State is selected
SYNC-07  Generation operational realization; physical candidate/retry state remains non-final
SYNC-09  exact Evaluation Criterion binding
SYNC-10  Evaluation method/scope/coverage compatibility
SYNC-11  Evaluation operational realization
SYNC-12  completed Evidence-producing Evaluation establishes Evidence bound to the exact subject
SYNC-13  Generation / Evidence completion handoff only when Generation is evidence-gated
SYNC-14  material Provenance relationship recording
```

Direct Generation does not activate `SYNC-06`. Generation quantity/scope/approximation commitments remain Generation-owned, with Strategy/Constraint relations governed by their applicable rules rather than being folded into `SYNC-06`.

External consumption, release/use approval and governance handoff are not `SYNC-13`; they remain external interaction/authority boundaries.

`SYNC-08` is retired as a cross-concept synchronization because candidate/completed-output establishment is Generation-local behavior.

Historical `SYNC-15` is reclassified under the cross-cutting Reproducibility contract; it is not active synchronization-owned state.

### Phase 014-E propagation note

Phase 014-E detected that this detailed architecture section retained pre-014-C synchronization scope wording after the current synchronization contract had been narrowed. The architecture responsibilities themselves were already compatible; this section is corrected to the current `SYNC-06` and `SYNC-13` scopes without changing architecture structure, concept ownership, synchronization count or application-family validity.

---

## 18. ADR-0003 disposition

ADR-0003 remains **PROVISIONAL RETAIN** pending the final 013-I ADR sweep.

Its durable rationale remains valid:

- exact immutable physical subject before completion-critical Evaluation/promotion;
- candidate state distinct from completed output;
- semantic finality separate from storage/path existence;
- no universal row-copy-on-promotion requirement;
- no exactly-once physical-computation requirement.

013-D clarifies its title/wording so `manifest-gated` means a manifest **or provider-equivalent immutable subject boundary**, not a mandatory literal manifest implementation.

---

## 19. Finding ledger

```text
A13-D-001  literal manifest/seal interpretation risk
             AR-7         AMAT-1  CLARIFY             RESOLVED

A13-D-002  promotion wording could imply separate owner/lifecycle
             AR-3         AMAT-1  CLARIFY             RESOLVED

A13-D-003  topology selector could become semantic authority
             AR-0         AMAT-0  RETAIN GUARDRAIL    CLOSED

A13-D-004  physical extent/integrity could inflate semantic strength
             AR-4         AMAT-1  CLARIFY             RESOLVED

A13-D-005  active structured-topology contract uses historical sync meanings
             AR-1 / AR-2  AMAT-1  CORRECT             RESOLVED IN 013-D

A13-D-006  retained 007-F reports 15 active synchronizations / old IDs
             AR-1         AMAT-1  SEMANTICALLY SUPERSEDED
                                              CORPUS CLEANUP -> 013-I

A13-D-007  candidate/sealed physical lifecycle versus Generation lifecycle
             AR-3 / AR-4  AMAT-1  CLARIFY             RESOLVED

A13-D-008  post-promotion representation equivalence strength
             AR-4         AMAT-1  CLARIFY             RESOLVED
```

---

## 20. Retained subject disposition

```text
Phase 004-D distributed data architecture   ALIGNED-WITH-CLARIFICATION
Phase 007-F distributed data refinement     ALIGNED-WITH-CLARIFICATION
Structured topology contract                ALIGNED AFTER CURRENT-AUTHORITY CORRECTION
ADR-0003                                    PROVISIONAL RETAIN
```

Final legacy document/ADR lifecycle cleanup remains 013-I work.

---

## 21. Materiality result

```text
AMAT-2 distributed-data defects    0
AMAT-3 blockers                    0
AR-9 contradictions                0
upstream reopen                    NONE
new concepts                       0
new synchronizations               0
mandatory storage/table format     0
mandatory literal manifest type    0
```

No concept, application-family, synchronization or mapping authority is reopened.

---

## 22. 013-E / 013-F handoff

013-E must preserve exact source/data-state identities and bounded distributed runtime references without requiring driver-local closure or provider-specific semantic identity.

013-F must ensure Attempt/writer/fencing/recovery mechanics cannot mutate a sealed subject under its identity or promote candidate material independently of Generation authority.

Both later groups inherit:

- exact-strength qualification;
- scope/topology owner separation;
- manifest/provider-equivalent seal semantics;
- candidate non-finality;
- Generation-owned completion/promotion;
- bounded Spark-scale control state;
- non-regressing recovery authority.

---

## Exit review

```text
013-D                               COMPLETE
distributed data-state spine       RETAINED WITH BOUNDED CLARIFICATION
AMAT-2                              0
AMAT-3                              0
AR-9                                0
upstream reopen                     NONE
R1                                  DOWNSTREAM / IN PROGRESS
013-E                               NEXT ELIGIBLE
```

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
