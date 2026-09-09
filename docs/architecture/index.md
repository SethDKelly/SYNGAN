---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for representation/architecture design downstream of accepted concepts, synchronizations and experience authority.

## Start here — current architecture continuation

For current design, read only what the active question needs:

1. [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
2. [007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md);
3. [007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md);
4. [007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md);
5. [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md) where not refined later;
6. only directly relevant Phase 004 detailed authorities;
7. [ADRs](../decisions/index.md) for rationale/history.

## Current posture

Architecture design is **active**; production implementation expansion and new executable architecture enforcement remain frozen.

Existing 007-A through 007-C implementation artifacts are provisional feasibility/history evidence and may be revised later.

## 007-D — identity/reference/view foundation

007-D keeps separate:

```text
authority scope
logical identity
exact semantic revision / commitment
mutable current-state version / freshness
representation schema version
provider identity / locator when material
```

Handles resolve/present authority rather than own it, and serialization is representation rather than mutation authority.

## 007-E — control persistence foundation

007-E establishes owner-controlled writes, same-boundary atomic visibility, durable reconcilable cross-boundary intent, stale-write detection without conflating CAS with semantic validation, append-preserving material history, exact historical resolution, representation-oriented migration, and regressive-restore qualification under ADR-0009.

Concrete Phase 005-D persistence technologies remain implementation candidates rather than architecture requirements.

## 007-F — distributed data-state foundation

007-F refines the distributed data plane around this separation:

```text
mutable selector/access
        ↓
exact logical data state
        ↓
open distributed candidate
        ↓
sealed immutable physical subject
        ↓
owner validation / completion basis
        ↓
Generation promotion
        ↓
one logical completed-output identity
```

Key current rules include:

- logical subject and physical representation are distinct axes;
- distributed subjects may contain bounded logical scopes without creating `Dataset`, `Table`, `Series`, `Relationship` or `DataTopology` concepts;
- single-table, time-series, multi-table shared-key and composite subjects remain representable;
- topology presets/physical layout do not replace Data Meaning/Generation/Constraint authority;
- exact source state distinguishes identity, read binding, integrity coverage, retention/rereadability and cross-scope coordination strength;
- individually exact source scopes do not automatically establish one coherent cross-scope snapshot;
- manifests remain bounded roots over distributed/hierarchical/provider-native detail;
- candidates may make partial/scope-local physical progress without becoming final output;
- whole-candidate sealing establishes immutable physical closure, not semantic validity;
- required completion Evaluation binds the exact sealed subject;
- Generation promotion remains owner-controlled and may reuse sealed bytes without full-copy promotion;
- later equivalent compaction/relocation/re-encoding may preserve logical output identity while the original promotion basis remains historical fact;
- surviving physical material after recovery does not prove semantic promotion or current authority;
- normal data-state handling must remain distributed and avoid full-corpus driver collection/component enumeration.

Earlier Phase 005-E choices such as a portable Parquet manifest profile and concrete PySpark/reference classes remain implementation-planning evidence, not current architecture requirements.

## Current design counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts in 007-D/E/F   0
new synchronizations        0
new ADRs                    0
```

No `SYNC-16`.

ADR-0003 remains active and sufficient; 007-F refines it for multi-scope/time-series/composite topology rather than superseding it.

## Current next boundary

**007-G — Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation** is the next eligible **design** subgroup.

Production implementation remains frozen independently of design progression.
