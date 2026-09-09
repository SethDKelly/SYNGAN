---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Current authority

Phase 007 is active under:

[Phase 007 Implementation Authority Lock](phase-007-implementation-authority-lock.md)

Current authorization is intentionally narrow:

```text
007-A  complete
007-B  AUTHORIZED
007-C..007-K  NOT AUTHORIZED
```

The active production implementation authority is limited to **007-B repository/toolchain/verification bootstrap**.

## Governing order

For implementation work, read:

1. [Phase 006 Consolidated Design Readiness Contract](../authority/phase-006-consolidated-design-readiness-contract.md)
2. current cross-cutting authority, concepts and synchronizations
3. current experience authority
4. [Phase 006 Architecture Reconciliation Contract](../architecture/phase-006-architecture-reconciliation-contract.md)
5. [Phase 006 Implementation-Planning Reconciliation](phase-006-implementation-planning-reconciliation.md)
6. relevant Phase 005 detailed plan where not refined
7. [Phase 007 Implementation Authority Lock](phase-007-implementation-authority-lock.md)
8. the active authorized Phase 007 subgroup

Code does not outrank this chain.

## 007-A locked baseline

Entry baseline:

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     843a518c12f7482229cfb012da658887cb92dfaa
```

Design counts:

```text
11 concepts
15 synchronizations
10 active ADRs
0 provisional concepts
```

## 007-B allowed implementation

007-B may introduce repository-owned project/build/test/static-analysis/verification bootstrap such as `pyproject.toml`, `uv.lock`, `tools/verify.py`, bootstrap-only tests and verification-only GitHub Actions.

It must not introduce `src/syngan/` or substantive domain/runtime/platform behavior.

Authorized initial toolchain:

```text
Python >=3.11
uv
Hatchling
pytest
Hypothesis
pytest-socket
Ruff
mypy
Import Linter
coverage.py / pytest-compatible coverage integration
```

No PySpark/PyTorch/Hugging Face/Databricks/MLflow/cloud/database/runtime-service dependency is authorized in the 007-B base/runtime closure.

## Evidence discipline

Every material Phase 007 subgroup must retain its entry commit, authority trace, files/change classes, dependency changes, commands/results, architecture-fitness evidence, compatibility/migration/network/security/distributed/scale implications, explicit non-claims, waivers/debt, Class 3/4 conflict disposition and next-subgroup authorization decision.

Class 3 architecture conflicts and Class 4 semantic/experience conflicts stop ordinary implementation and reopen upstream authority.

## Branch/review posture

At 007-A entry, `main` was unprotected and had no required checks. Direct-to-main is permitted for explicitly authorized 007-B work but is not independent review/CI evidence. 007-B must establish repository verification entry points; 007-C must revisit review/PR enforcement.

## Historical planning

Phase 005 and Phase 006 planning remain active beneath the Phase 007 lock where not superseded/refined. The broader future wave sequence is still valid, but only the currently authorized subgroup may execute.

## Current next

**007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness**
