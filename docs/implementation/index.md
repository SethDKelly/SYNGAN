---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Purpose

This directory is the canonical home for implementation-planning and delivery-governance decisions that translate the accepted SYNGAN architecture into source/module boundaries, toolchain expectations, persisted/wire representations, implementation slices, migrations, verification obligations, platform integration plans, delivery sequencing, and acceptance evidence.

Implementation authority is downstream of the [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md) and MUST NOT redefine accepted semantic, experience, or architecture authority for implementation convenience.

## Start here

- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — canonical 005-A implementation precedence, change/dependency/toolchain governance, migration discipline and repository enforcement.
- [Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md) — canonical 005-B verification layers, fitness-function catalog, fixture/test policy and Q0-Q4 quality-gate contract.
- [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — canonical 005-C source/package topology, Python/toolchain baseline, import dependency rules, optional-dependency isolation, test topology and CI command/check architecture.
- [Phase 005 navigator](../phases/005/index.md) — implementation-planning sequence and current work.

Additional implementation authorities will be added only when their Phase 005 slice promotes durable implementation decisions here.

## Authority relationship

Use the following downstream order when implementation work is involved:

```text
design / cross-cutting authority
        ↓
concepts + synchronizations
        ↓
experience contracts
        ↓
architecture contracts
        ↓
implementation authority / plans
        ↓
source code + deployment configuration
        ↓
runtime/platform realization
```

Code and configuration are executable realizations of accepted authority. They do not acquire permission to contradict an upstream contract merely because they already exist or because a dependency/platform makes another implementation easier.

If implementation exposes a genuine architecture contradiction or infeasibility, the conflict MUST be raised to the architecture layer and resolved explicitly rather than hidden in code.

## Progressive disclosure for implementers and agents

For a material implementation task, begin with:

1. [`docs/index.md`](../index.md);
2. the [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
3. this implementation index and the implementation authority relevant to the active slice;
4. the [005-B verification authority](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
5. the [005-C source/package authority](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) for source/import/dependency/toolchain constraints;
6. only the detailed architecture/concept/experience documents directly linked by that slice;
7. ADRs only when rationale/supersession history is needed;
8. phase/discovery history only when design provenance is needed.

Do not load the whole design corpus by default.

## Completed implementation-planning authority

### 005-A — Implementation governance

Established implementation precedence/conflict escalation, five-class change governance, delivery-slice traceability, completion-evidence requirements, toolchain/dependency governance, migration/compatibility discipline, repository agent instructions, and PR review enforcement without prematurely selecting source topology or concrete verification tools.

Phase record: [005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](../phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

Immediate repository enforcement includes:

- root [`AGENTS.md`](../../AGENTS.md);
- [`.github/pull_request_template.md`](../../.github/pull_request_template.md).

### 005-B — Verification architecture

Established logical verification layers V0-V11, architecture-fitness identifiers AF-01 through AF-20, reusable adapter conformance expectations, synthetic/non-sensitive fixture classes, deterministic versus statistical verification rules, explicit failure-injection/recovery scenarios, default-deny portable-core network testing, Q0-Q4 quality gates, flaky/quarantine/waiver governance, and bounded implementation acceptance-evidence requirements.

Phase record: [005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](../phases/005/005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md).

### 005-C — Source/package topology and dependency enforcement

Established one initial Python distribution/import package (`syngan`) using `src/` layout, Python >=3.11 as the portable-core floor, and the top-level production responsibilities:

```text
foundation
domain
ports
application
api
adapters
bootstrap
```

Accepted foundational toolchain:

- uv + committed lockfile for repository environment/resolution;
- Hatchling build backend;
- pytest + Hypothesis + pytest-socket for verification;
- Ruff for lint/format;
- mypy for static typing;
- Import Linter for dependency architecture;
- coverage reporting as diagnostic evidence;
- GitHub Actions as repository CI.

005-C also established:

- strict inward import direction and adapter isolation;
- anti-catch-all admission rules for `foundation`;
- model/platform-neutral base dependencies;
- reserved optional capability extras for Spark/Torch/Databricks owned by later slices;
- physical unit/contract/fitness/conformance/integration/scale/scenario/golden/support test topology;
- stable `tools/verify.py` Q0-Q4 command meanings;
- initial Q1 static/unit/fitness/package-offline check architecture;
- clean built-package import and no-hidden-optional-dependency/network verification.

Phase record: [005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](../phases/005/005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

## Current state

**Phase 005 — Implementation Planning & Delivery Decomposition is current.**

Next:

**005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**.

005-D now owns the first concrete behavioral implementation slice: typed public specifications/handles/resources, durable control-plane models, stable IDs/revisions/state versions, persistence port/repository contracts, transaction/CAS boundaries, schema migrations and the verification needed to preserve immutable historical authority.
