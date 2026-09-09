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
4. [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md) where not refined later;
5. [Phase 004 Consolidated Architecture Contract](phase-004-consolidated-architecture-contract.md) and only relevant detailed authorities;
6. [ADRs](../decisions/index.md) for rationale/history.

## Current posture

Architecture design is **active**; production implementation expansion and new executable architecture enforcement are frozen.

Existing 007-A through 007-C implementation artifacts are provisional feasibility/history evidence and may be revised later.

## 007-D foundation

007-D keeps independent representation axes for authority scope, stable logical identity, exact semantic revision/commitment, mutable current-state version/freshness, representation schema version and external/provider identity/locator where material.

It also establishes that typed handles resolve/present authority rather than own it, and serialization is representation rather than mutation authority.

## 007-E persistence foundation

007-E adds current architecture rules for persistence:

- persistence preserves authority rather than creating it by physical durability;
- semantic/application owners validate transitions; persistence commits them under consistency preconditions;
- same-boundary canonical facts required for one material transition become visible atomically or not at all;
- required cross-boundary work retains durable detectable/reconcilable intent when atomic completion is impossible;
- durable intent is not proof of target success;
- material current-state mutation uses conflict-detectable observation/version semantics, while CAS does not replace semantic validation;
- no universal global transaction, distributed 2PC or event-sourcing model is required;
- material transition history is append-preserving enough for explanation/recovery while full event sourcing remains optional;
- historical resolution is exact-target-first and never substitutes current/latest;
- derived indexes/search projections remain non-authoritative;
- migration is representation change by default and must preserve historical meaning where semantics did not change;
- migration revision is distinct from semantic revision, current-state version, representation schema version and recovery authority;
- canonical-state rollback is a potentially regressive recovery event under ADR-0009;
- a copied control store does not automatically retain the original authority scope when used as a clone/fork.

Earlier Phase 005-D choices such as UUIDv4, JSON, SQLAlchemy Core, Alembic, PostgreSQL, SQLite and Psycopg remain implementation-planning evidence, not current architecture requirements.

## Current design counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts in 007-D/E     0
new synchronizations        0
```

No `SYNC-16`.

007-E did not create a new ADR because its transaction/CAS/history decisions refine the existing persistence architecture and ADR-0002/ADR-0009 rather than selecting a new concrete persistence mechanism.

## Current next boundary

**007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation** is the next eligible **design** subgroup.

Production implementation remains frozen independently of design progression.
