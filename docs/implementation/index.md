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

- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — canonical Phase 005-A authority for implementation precedence, change classification, dependency/toolchain governance, repository/agent rules, migration discipline, and completion evidence.
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

If implementation exposes a genuine architecture contradiction or infeasibility, the conflict MUST be raised to the architecture layer and resolved explicitly rather than hidden inside code.

## Progressive disclosure for implementers and agents

For an implementation task, begin with:

1. [`docs/index.md`](../index.md);
2. the [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
3. this implementation index and the relevant implementation authority;
4. only the detailed architecture/concept/experience documents directly linked by that implementation slice;
5. ADRs only when decision rationale or supersession history is needed;
6. phase history/discovery only when the task requires design provenance.

Do not load the whole design corpus by default.

## Completed implementation-planning authority

### 005-A — Implementation governance

Established implementation precedence/conflict escalation, five-class change governance, delivery-slice traceability, completion-evidence requirements, toolchain/dependency governance, migration/compatibility discipline, repository agent instructions, and PR review enforcement without prematurely selecting source topology or concrete verification tools.

Phase record: [005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](../phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

Immediate repository enforcement includes:

- root [`AGENTS.md`](../../AGENTS.md);
- [`.github/pull_request_template.md`](../../.github/pull_request_template.md).

These are enforcement/navigation aids below canonical implementation authority.

## Current state

**Phase 005 — Implementation Planning & Delivery Decomposition is current.**

Next:

**005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**.
