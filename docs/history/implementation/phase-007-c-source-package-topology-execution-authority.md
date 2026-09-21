---
type: Historical Implementation Authority
title: Phase 007-C Source/Package Topology Execution Authority
status: superseded
superseded_by: ../authority/phase-007-consolidated-architecture-implementation-reentry-readiness-contract.md
---

# Phase 007-C Source/Package Topology Execution Authority — Historical / Provisional

## Status

This document preserves the source/package topology authority that governed 007-C. It is **no longer current implementation authority**.

Current architecture and re-entry authority are:

- [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md);
- [Phase 007 Consolidated Architecture & Implementation-Reentry Readiness Contract](../authority/phase-007-consolidated-architecture-implementation-reentry-readiness-contract.md).

The 007-C implementation remains useful feasibility evidence, but its exact package/test constraints are provisional until R0/008-A revalidates them.

## Historical topology

007-C established:

```text
src/syngan/
├── __init__.py
├── py.typed
├── foundation/
├── domain/
├── ports/
├── application/
├── api/
├── adapters/
└── bootstrap/
```

with inward dependency intent, core/adapter/bootstrap separation, Import Linter enforcement, an importable typed package and no production runtime dependencies.

These were implementation responsibility boundaries, not concepts.

## Historical dependency intent

The architectural intent remains directionally sound:

```text
foundation
    ↑
domain
    ↑
ports
    ↑
application
    ↑
api

core contracts
    ↑
adapters
    ↑
bootstrap / composition
```

Inner/core packages should not depend on outer technology/composition merely for convenience, and optional runtime/provider dependencies should not leak into the portable base import path.

However, the exact seven-package set and exact Import Linter contracts are no longer self-authorizing architecture rules.

## Historical useful evidence

007-C demonstrated that SYNGAN can support:

- one `syngan` distribution using `src/` layout;
- `py.typed` packaging;
- an empty base runtime dependency set at scaffold time;
- repository-owned package build/smoke verification;
- inward dependency checks;
- a small root package without optional runtime import side effects;
- reviewable CI evidence for material source changes.

## Current provisional items

R0/008-A must explicitly retain, revise, relax or remove:

- the exact seven top-level package set;
- exact Import Linter layer and forbidden-dependency contracts;
- the import-free root-package assertion;
- exact package/build smoke assumptions;
- phase-state fitness assertions written around 007-C delivery progression;
- socket/test rules when future local Spark process communication is introduced.

No existing 007-C test may veto a sound implementation of the consolidated Phase 007 architecture merely because the test predates 007-D through 007-J.

## Current non-authority

This document does not authorize concept behavior, identity/reference contracts, persistence, Spark/data-state behavior, Strategy/runtime implementation, Execution/recovery, security, Evidence/history/query, platform adapters, benchmarks or release work.

Those require current explicit implementation authority after R0 re-baselining.
