---
type: Phase Record
title: 005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement
status: complete
---

# 005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement

## Objective

Establish the governance and repository enforcement boundary required before SYNGAN selects detailed verification tooling, source/package topology, persistence technologies, runtime implementations, or platform integrations.

The phase prevents implementation/code-generation convenience from becoming a new authority layer and defines the evidence/review/dependency/toolchain discipline that later Phase 005 implementation plans must satisfy.

## Entry authority

005-A is downstream of:

- [Documentation Governance and Anti-Drift Rules](../../authority/documentation-governance.md);
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md);
- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [004-J — Phase 004 Exit](../004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md);
- [Phase 005 navigator](index.md).

## Repository observation at entry

At the start of 005-A, the repository intentionally contained only `README.md` and the design documentation tree. It did not yet contain production source/package topology, `pyproject.toml`, tests, CI workflows, or repository-wide agent instructions.

This was treated as an advantage: 005-A establishes governance before inventing implementation structure or selecting tools whose requirements have not yet been specified.

## Canonical authority created

005-A establishes:

- [Implementation Planning & Delivery Authority index](../../implementation/index.md);
- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](../../implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

The canonical implementation rule is:

> **Implementation is a realization of accepted authority, not a new authority layer that may silently redefine it. Every material implementation choice must either fit the accepted contracts or explicitly escalate the smallest required upstream revision.**

## Accepted implementation authority order

```text
design / documentation authority
        ↓
concepts + synchronizations
        ↓
experience
        ↓
architecture
        ↓
implementation authority / accepted slice plans
        ↓
source + migrations + configuration
        ↓
runtime / platform realization
```

Existing code does not outrank an accepted upstream contract.

## Change classification accepted

005-A defines five implementation-change classes:

| Class | Meaning | Governance consequence |
|---|---|---|
| 0 | local/non-contractual maintenance | normal review/tests |
| 1 | implementation realization decision | architecture trace + verification + durable implementation authority where needed |
| 2 | public/persisted/compatibility contract change | explicit plan, compatibility/migration analysis, contract tests |
| 3 | architecture-affecting change | stop and update/review canonical architecture before acceptance |
| 4 | semantic/experience change | reopen the appropriate upstream design authority explicitly |

This prevents implementation agents from disguising architecture/semantic change as refactoring.

## Delivery governance accepted

A material delivery slice must remain traceable through:

```text
concept / experience obligation
        ↓
architecture authority
        ↓
implementation authority / plan
        ↓
modules / ports / adapters / schemas
        ↓
implementation
        ↓
verification / architecture fitness
        ↓
acceptance evidence
```

A local successful run, compilation success, or one successful platform job is insufficient completion evidence by itself.

Experimental spikes remain non-authoritative until reconciled with the accepted architecture and implementation plan.

## Completion-evidence contract accepted

Material slices must account for, as applicable:

- upstream authority mapping;
- implementation boundary/plan;
- implementation files;
- automated tests/fitness checks;
- test/CI execution evidence;
- migration/compatibility effects;
- dependency/toolchain changes;
- network/egress/offline effects;
- security/disclosure effects;
- scale/resource assumptions;
- explicit deferred work.

005-B owns the concrete verification/evidence harness.

## Toolchain governance accepted

005-A deliberately separates **toolchain governance** from **tool selection**.

Accepted rules include:

- build/test/development behavior must be repository-declared and reproducible rather than workstation-defined;
- `pyproject.toml` should become the canonical Python project/build/tool metadata entry point once the Python package is created, unless a selected tool requires separate configuration;
- direct dependencies must be repository-declared;
- developer/CI dependency resolution must use a reproducible lock/constraints/equivalent mechanism once selected;
- supported Python/Spark/platform/runtime versions require an explicit compatibility matrix rather than accidental local-version inference;
- developers and CI should use the same underlying stable repository commands;
- supported workflows must not rely on undocumented global packages, personal credentials, notebook state, or hidden downloads.

Concrete Python/version manager/build/test/static-analysis tools remain deferred to 005-B/005-C.

## Dependency governance accepted

Dependencies must eventually be classified as:

1. core runtime;
2. development/verification;
3. optional adapter/runtime;
4. build/release.

Direct-dependency intake must consider purpose, compatibility, transitive/system requirements, license/security, network/telemetry behavior, offline/private provisioning, egress implications, and removal/substitution path where material.

Runtime package/model acquisition remains prohibited as a hidden fallback.

Optional platform/model-runtime integrations must remain isolatable from the portable/offline core.

## Repository enforcement created

### Root agent rules

Created [`AGENTS.md`](../../../AGENTS.md) as the concise repository-wide machine-facing governance entry.

It requires agents to:

- use progressive disclosure;
- identify the implementation slice/upstream authority;
- keep generated scope bounded;
- preserve architecture invariants;
- disclose dependencies/network/security/migration effects;
- add verification with behavior changes;
- avoid generic god-objects and hidden fallback behavior;
- never claim completion without evidence.

`AGENTS.md` is an enforcement/navigation aid and does not outrank canonical docs.

### Pull-request checklist

Created [`.github/pull_request_template.md`](../../../.github/pull_request_template.md) to require explicit disclosure of:

- implementation slice/change class;
- authority mapping;
- tests/fitness evidence;
- dependency/toolchain change;
- public/persisted/migration compatibility;
- security/network/egress effect;
- scale/platform effect;
- deferred work/waivers.

### Branch/CI enforcement boundary

005-A does **not** claim branch protection or required CI checks are already enabled.

Once implementation source/configuration exists, material changes should merge through reviewable PRs with automated required checks. 005-B must define those checks before repository protection is configured.

## Source topology decision

No placeholder source/package/test tree was created.

This is intentional.

005-B first defines verification/fitness obligations. 005-C then selects source/package boundaries and foundational concrete toolchain under those requirements.

## Migration and compatibility governance accepted

Future implementation must keep distinct:

```text
semantic revision
    !=
persistence schema migration
    !=
current lifecycle state update
```

Persisted/public/API/SPI/codec/protocol changes require compatibility analysis on their actual axis rather than being hidden behind one global package version.

Migrations cannot destructively rewrite immutable committed history as an ordinary schema upgrade.

## Agent parity accepted

Human and automated contributors use the same implementation authority, dependency, change-classification, verification, migration, and completion rules.

Agents receive no special permission to weaken architecture invariants or introduce dependencies/platform behavior for code-generation convenience.

## Architecture-fitness enforcement obligation

005-A establishes architecture-fitness checks as product-correctness controls rather than optional style tooling.

005-B should define executable checks for concerns including:

- inward dependency direction;
- optional/offline dependency closure;
- non-final versus promoted type separation;
- immutable committed history;
- stale-writer fencing;
- idempotent promotion/Evidence establishment;
- query-projection authority isolation;
- security/redaction/query isolation;
- no enterprise full-driver collection;
- platform capability fallback preserving semantics.

## No architecture/semantic revision required

005-A found no implementation-governance requirement that requires changing the Phase 004 architecture or accepted concepts/synchronizations.

No new ADR was required because the phase establishes downstream implementation governance rather than changing an architecture decision.

## Deferred decisions

005-A intentionally leaves to later Phase 005 groups:

- supported Python versions;
- dependency/environment manager;
- build backend;
- test runner;
- formatter/linter/type checker;
- source/package topology;
- CI workflow/check implementation;
- persistence/migration technology;
- Spark storage/catalog integration;
- scheduler/fencing implementation;
- plugin/runtime technologies;
- security/platform/observability technologies;
- release/versioning policy;
- benchmark/support claims.

## Exit criteria

- [x] canonical implementation authority created;
- [x] implementation precedence and conflict escalation defined;
- [x] change classification defined;
- [x] delivery/acceptance evidence contract defined;
- [x] toolchain governance established without premature tool selection;
- [x] dependency-introduction policy established;
- [x] migration/compatibility governance established;
- [x] repository-wide agent instructions created;
- [x] PR review checklist created;
- [x] branch/CI enforcement boundary stated truthfully;
- [x] source/package topology left to dependency-safe later phase;
- [x] Phase 004 architecture remains unchanged;
- [x] 005-B handoff is explicit.

## Exit decision

**005-A — complete.**

Next:

**005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**.
