---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design & Implementation Knowledge
status: active
---

# SYNGAN Design & Implementation Knowledge

This directory is the canonical knowledge bundle for SYNGAN.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > current architecture design
  > implementation planning
  > later explicit implementation re-entry
  > code / tests / deployment
  > ADR rationale / phase history / backlog / examples
```

Existing source/tests never become upstream design authority merely because they exist or pass.

## Current posture

[Phase 007 Design Continuation & Implementation Freeze](authority/phase-007-design-continuation-implementation-freeze.md) governs current work.

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
007-A..007-C  historical/provisional bootstrap work
007-D         DESIGN COMPLETE
007-E         DESIGN COMPLETE
007-F         next eligible design subgroup — not started
007-G..007-K  not started
```

Implementation remains frozen at the retained 007-C scaffold; 007-D and later production implementation are not authorized.

## Current architecture continuation

### 007-D — identity / references / views

[007-D architecture](architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md) separates logical identity, exact semantic revision/commitment, mutable current-state version/freshness, representation schema version and authority/provider context.

Handles resolve/present authority; serialization is representation, not mutation authority.

### 007-E — persistence / transactions / history / migration

[007-E architecture](architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md) establishes:

- owner-controlled canonical writes;
- atomic same-boundary coupled facts;
- durable reconcilable intent for required cross-boundary work;
- stale-write detection without treating CAS as semantic validation;
- material history without universal event sourcing;
- exact historical resolution without `latest` substitution;
- derived projections as non-authoritative;
- migration as representation change by default;
- canonical-state rollback as potentially regressive recovery.

Earlier concrete Phase 005-D technology selections are provisional implementation-planning evidence, not current architecture commitments.

## Provisional executable scaffold

The retained 007-B/007-C package/tests/CI remain feasibility/history evidence and may be revised later if architecture requires it. No current design choice must preserve them solely because executable checks encode them.

## Complete capability target

The structured-data target remains:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The complete supported baseline also retains source-derived/local free-form-text synthesis without mandatory public model-hub or runtime inference-service dependency.

## Current next boundary

**007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation** is the next eligible **design** subgroup.

It requires an explicit proceed decision. Production implementation remains frozen independently of design progression.
