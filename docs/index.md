---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design & Implementation Knowledge
status: active
---

# SYNGAN Design & Implementation Knowledge

This directory is the canonical knowledge bundle for SYNGAN.

## Progressive disclosure

Read only what the active task needs:

1. [Authority](authority/index.md)
2. [Concepts](concepts/index.md) + [Synchronizations](synchronizations/index.md)
3. [Experience](experience/index.md)
4. [Architecture](architecture/index.md)
5. [Implementation Planning & Authority](implementation/index.md)
6. [ADRs](decisions/index.md) for rationale
7. [Backlog](backlog/index.md) for deferred work
8. [Phases](phases/index.md) for design/execution history and current progression

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > current architecture design
  > implementation planning
  > later explicit implementation re-entry
  > code / deployment
  > ADR rationale / phase history / backlog / examples
```

Code/tests never become upstream design authority because they already exist or pass.

## Current design posture

The current posture is governed by:

[Phase 007 Design Continuation & Implementation Freeze](authority/phase-007-design-continuation-implementation-freeze.md)

Phase 006 historically concluded that design was complete enough to consider implementation. Phase 007-A through 007-C then created a provisional repository/tool/package scaffold.

The project has now explicitly returned to **architecture/design refinement before further production implementation** so that provisional tests/source choices do not harden unsettled representation decisions.

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
architecture design         ACTIVE
new implementation          FROZEN
new executable restrictions FROZEN
```

No `SYNC-16`.

## Phase 007 design progression

```text
007-A  historical authority/bootstrap transition
007-B  historical repository/toolchain scaffold
007-C  historical/provisional source-topology scaffold
007-D  DESIGN COMPLETE
007-E  next eligible design subgroup — not started
007-F..007-K  not started
```

The frozen implementation authorization track remains:

```text
007-A  COMPLETE
007-B  COMPLETE
007-C  COMPLETE
007-D and later  NOT AUTHORIZED FOR IMPLEMENTATION
```

## 007-D result

[007-D — Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation](architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md) is complete as architecture design.

It separates:

- authority/namespace scope;
- stable logical resource identity;
- exact semantic revision/commitment snapshot;
- mutable current-state version/view freshness;
- representation schema version;
- external/provider identity or locator where material.

It also establishes that handles resolve/present authority rather than own it, serialization is representation rather than mutation authority, and programmatic views remain orthogonal rather than collapsing lifecycle/actionability/operation/disclosure/history into one object/status.

No concrete ID format, Python public class hierarchy, wire format, serializer, persistence schema, CAS/outbox mechanism, migration tool, test or executable enforcement was introduced by 007-D.

## Provisional executable scaffold

The 007-C source/tool/test scaffold remains in the repository for feasibility/history, but is downstream evidence only. It may be revised later if current design requires it.

No current design decision must preserve an implementation choice solely because existing tests encode it.

## Complete capability target

The structured-data target remains:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The complete supported baseline also retains source-derived/local free-form-text synthesis without mandatory public model-hub or runtime inference-service dependency.

## Current next boundary

**007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline** is the next eligible **design** subgroup.

It requires an explicit proceed decision. Production implementation remains frozen independently of design progression.

## Governance note

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 normalization remains non-blocking while authority is unambiguous.
