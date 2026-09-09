---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Current authority

Phase 007 remains active under:

- [Phase 007 Implementation Authority Lock](phase-007-implementation-authority-lock.md)
- [Phase 007-B Bootstrap Execution Authority](phase-007-b-bootstrap-execution-authority.md)
- [Phase 007-C Source/Package Topology Execution Authority](phase-007-c-source-package-topology-execution-authority.md)

Current subgroup state:

```text
007-A  complete
007-B  complete
007-C  complete
007-D  NOT AUTHORIZED — next eligible
007-E..007-K  NOT AUTHORIZED
```

No 007-D behavior is currently authorized.

## Governing order

For implementation work, read current design/experience/architecture/planning authority first, then the Phase 007 implementation lock, the enduring 007-B/007-C contracts, and only the explicitly authorized current subgroup.

Code does not outrank this chain. Class 3 architecture or Class 4 semantic/experience conflicts stop implementation and reopen upstream authority.

## Executable substrate through 007-C

007-B established the reproducible tool/test/CI substrate. 007-C added the first production package architecture:

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

Import Linter now executes in the normal gate and enforces inward core dependency direction plus adapter/composition boundaries.

The repository verification flow installs the first-party package from locked tooling and then runs lint/format/type/unit/architecture/fitness/package checks:

```text
uv sync --all-groups --no-install-project --locked
uv sync --all-groups --locked --no-build-isolation
uv run --no-sync python tools/verify.py all
```

The package gate verifies imports, `py.typed`, and non-publishing wheel/sdist construction/content.

`[project].dependencies` remains empty. Hatchling and `editables` are build/development dependencies only. Portable-core pytest remains socket-denied after explicit provisioning.

## Evidence status

- [007-B phase record](../phases/007/007-B-repository-toolchain-bootstrap-reproducible-environment-verification-harness.md)
- [007-C phase record](../phases/007/007-C-source-package-topology-dependency-direction-architecture-fitness-enforcement.md)

007-C was reviewed as PR #1, passed the permanent `Verify` workflow on exact PR head `9f93b6eff7f8d8a1b19950745530dc273d462d6d`, and merged as `063f847953f69a525ee04315fa92bc0e9fa36a1c`.

`main` remains unprotected and Verify is not claimed as a required repository check. Material production-source work should continue using reviewable branches/PRs when supported and retain exact-head green evidence.

## Historical planning

Phase 005 and Phase 006 planning remain active beneath Phase 007 where not refined. The broader future wave sequence remains planning authority, but only an explicitly authorized Phase 007 subgroup may execute.

## Current next boundary

**007-D — Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation** is next eligible but **not yet authorized**.

An explicit proceed decision is required before 007-D implementation begins.
