---
type: Documentation Authority
title: Agentic Conformance, Negative Controls, Drift Detection & CI
status: active
---

# Agentic Conformance, Negative Controls, Drift Detection & CI

## Purpose

Define the repository-owned executable conformance plane for SYNGAN agentic/documentation configuration.

This authority owns the canonical conformance command, validator composition, negative-control semantics, drift-report semantics, and dedicated CI boundary.

It does not own product C0-C9 behavior, provider runtime certification, implementation-package/ADR governance, dependency/supply-chain/secrets preflight, production readiness, or deployment.

## Canonical command

~~~bash
python tools/run_agentic_conformance.py --report agentic-conformance-report.md
~~~

The command is safe and non-destructive against the source checkout. Seeded negative controls execute only inside an isolated temporary repository copy.

Fixing a failure requires the surrounding human-selected task to authorize A2 work. Conformance failure itself does not grant edit authority.

## Validation order

1. Phase 016/current-status progression drift;
2. portable skill structure and task-boundary discipline;
3. tool-adapter and compatibility-state integrity;
4. agent-facing local reference/link integrity;
5. stable-reference registry/ownership drift;
6. deterministic generated OKF projection equality;
7. OKF v0.2/SYNGAN projection conformance;
8. deterministic UTF-8 context budgets;
9. implementation-package/traceability conformance;
10. engineering-preflight dependency/supply-chain/secrets/version conformance;
11. isolated engineering-preflight negative controls;
12. isolated implementation-package negative controls;
13. repository-readiness scorecard/residual-risk conformance;
14. isolated repository-readiness negative controls;
15. isolated cross-cutting agentic negative controls.

Each check has one owning validator. The unified runner composes results rather than duplicating validator logic.

## Status drift

Current status is checked across the canonical current-status authority, Phase 016 index/authority, and root AGENTS guidance.

016-G may be active only while explicitly authorized. 016-H and later work must remain unauthorized until 016-G closes. Passing conformance cannot self-authorize the next group.

## Skill conformance

Canonical skills must remain exactly the registered `.agents/skills/*/SKILL.md` set for the current foundation, use only `name` and `description` frontmatter, remain within the configured byte budget, declare an A1/A2 boundary, carry explicit stop conditions, and avoid provider-specific or autonomous permission metadata.

The A2 execution skill must preserve the completion invariant: report the next eligible dependency and stop rather than starting it.

## Adapter conformance

Cursor and Codex use root AGENTS plus `.agents/skills/` without competing semantic adapters. Claude uses `.claude/CLAUDE.md` plus thin command bridges to canonical skills.

Adapter validation rejects competing root/provider semantic surfaces, missing shared-authority imports, bridge duplication, incompatible workflow paths, and fabricated provider-runtime support.

Documented compatibility and runtime certification remain separate. During 016-G, Cursor, Codex, and Claude Code runtime state remains `unverified` unless a separately authorized provider-runtime evidence process changes that state.

## Link/reference conformance

Agent-facing current Markdown surfaces must not contain broken local Markdown links. Generated OKF references remain governed by the OKF validator; stable `syngan://...` identity remains governed by the stable-reference validator.

Search rank, history, generated routes, model memory, and adapter convenience cannot repair a broken deterministic current route.

## Context-budget conformance

`tools/measure_agent_context.py` remains the numerical owner for deterministic UTF-8 context budgets. Budget failure is repository agentic-configuration drift, not permission to remove required semantics.

## Negative controls

`tools/test_agentic_conformance_guards.py` copies the checkout to a temporary directory, introduces one defect at a time, runs the owning validator, and restores by discarding the temporary copy.

The suite must prove rejection of at least:

- unauthorized/self-progressed Phase 016 state;
- stable-reference target drift;
- generated OKF resource drift;
- persistent context-budget overflow;
- provider-specific/unsupported skill metadata;
- Claude/shared-authority adapter drift;
- fabricated provider-runtime support.

A negative control passes only when the intentionally corrupted repository fails its owning validator.

## Report semantics

The unified runner emits PASS/FAIL for each deterministic check, tool compatibility state, stable-reference and OKF counts, and an explicit scope disclaimer.

**PASS means only that the checked repository agentic/documentation configuration conforms to the current contracts.**

PASS does not prove:

- SYNGAN product/runtime correctness;
- C0-C9 behavioral success;
- provider runtime compatibility;
- production readiness;
- security certification;
- deployment readiness;
- external system health.

Conversely, an agentic conformance failure does not imply SYNGAN domain/runtime failure.

## Dedicated CI contract

`.github/workflows/agentic-conformance.yml` runs the canonical command for relevant pull requests and pushes to `main`.

The job intentionally requires only repository checkout and Python. It must not require coding-agent binaries, provider accounts, external network calls by the validators, secrets, cloud credentials, Databricks/Spark services, deployment, or production data.

The existing Verify/C0-C9 workflow remains separately authoritative for its established product/implementation gates.

## Drift repair discipline

A detected P16-0/P16-1/P16-2 configuration drift may be repaired inside an explicitly selected A2 task. If repair would change accepted semantics or architecture, reclassify as P16-3/P16-4 and reopen the smallest owner rather than weakening conformance.

## Phase boundary

Product/provider/runtime delivery remains outside Phase 016-G authority.

Agentic conformance never authorizes phase progression. 016-H package/traceability and 016-I engineering-preflight checks may compose into this conformance lane while remaining governed by their own canonical implementation authorities. A preflight PASS does not establish release authorization, license/legal approval, current vulnerability clearance, provider certification, or scale qualification. A readiness PASS likewise does not authorize the next implementation program.
