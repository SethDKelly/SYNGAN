---
type: Implementation Authority
title: Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement
status: active
---

# Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement

## Purpose

Define the **current** repository-wide implementation governance contract: how authorized
work is scoped, traced, implemented, verified, reviewed, and merged without allowing code
or tooling convenience to redefine upstream authority.

The original Phase 005-A planning record is preserved as history at
[`docs/history/phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md`](../history/phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

## Current posture

~~~text
Jackson concept design                COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013 architecture                COMPLETE
Phase 014 whole-design/readiness      COMPLETE
Phase 015 implementation foundation   COMPLETE
Phase 016 repository hardening        COMPLETE
C0-C9                                 ACTIVE / PASS
repository implementation readiness   100 / 100
active implementation packages        0
next implementation program           REQUIRES EXPLICIT START GATE / NOT AUTHORIZED
product/provider/runtime delivery     NOT AUTHORIZED
~~~

Repository readiness does not create implementation authority. A future program begins
only through a new explicit human-selected start gate.

## Authority order

~~~text
cross-cutting authority / methodology
  -> accepted concepts and synchronizations
  -> experience and mapping
  -> current architecture topic owners
  -> current implementation governance / selected start gate
  -> implementation package and ADR/change-control evidence
  -> code / tests / runtime evidence
~~~

Code is executable evidence, not a permission source. When implementation conflicts with
current authority, correct the code or stop and reopen the smallest governing owner.

## Human-selected scope

The selected task defines the implementation envelope.

Agents and humans may complete directly necessary supporting work inside that envelope,
but must not self-start:

- the next package or delivery slice;
- a backlog item;
- a provider integration;
- a deployment/release activity;
- a semantic or architecture change.

Use the A1-A4 authority model in
[Agent Authority, Human-Directed Scope, Change Classes, Security & Trust Boundaries](../authority/agent-authority-human-directed-scope-security-trust.md).

## Change classes

Current Class 0-4 behavior is:

- **Class 0 — local/non-contractual maintenance:** normal review and relevant tests.
- **Class 1 — implementation realization:** trace to current authority and verification.
- **Class 2 — public/persisted/compatibility contract:** explicit compatibility/migration
  assessment plus contract evidence.
- **Class 3 — architecture-affecting:** stop ordinary implementation and reopen the
  architecture owner.
- **Class 4 — semantic/experience-affecting:** stop ordinary implementation and reopen the
  owning design/experience authority.

Prospective material Class 1/2 work follows
[Implementation Package, Traceability & ADR Change Control](implementation-package-traceability-adr-change-control.md).

An implementation package is scope/traceability/evidence metadata. It never authorizes
itself or a subsequent package.

## Current toolchain baseline

The repository-owned development baseline is:

~~~text
Python                 3.11 verified baseline
project metadata       pyproject.toml
environment/lock       uv 0.12.x + uv.lock
build backend          Hatchling
tests                  pytest / hypothesis
lint/format            Ruff
typing                 mypy strict
architecture fitness   import-linter + repository fitness tests
CI                     GitHub Actions
core runtime deps      none declared
~~~

Current exact dependency, supply-chain, secret, compatibility, benchmark, and
version/release hygiene is governed by
[Engineering Preflight](engineering-preflight-dependency-supply-chain-secrets-compatibility-benchmark-versioning.md).

## Stable developer commands

Provision the locked environment:

~~~bash
uv sync --all-groups --locked --no-build-isolation
~~~

Portable verification:

~~~bash
uv run --no-sync python tools/verify.py portable
~~~

Agent/documentation conformance:

~~~bash
python tools/run_agentic_conformance.py
~~~

Engineering-preflight changes:

~~~bash
uv run --no-sync python tools/verify.py preflight
~~~

Material implementation must also run the focused C-lanes and tests required by its
selected package/authority. Local and CI verification should use the same repository-owned
entry points.

## Branch and review governance

Implementation should use short-lived branches from the current verified `main` head,
one bounded work item per branch, reviewable pull requests, and automated verification.

The preferred branch/PR workflow is documented in [CONTRIBUTING.md](../../CONTRIBUTING.md).

A material PR should disclose the selected work/package, authorization basis, current
authority refs, change class, verification evidence, dependency/toolchain effects,
compatibility/migration impact, security/network implications, scale implications, and
deferred work.

Passing CI does not expand scope. A failing guard must not be deleted or weakened merely
to make the same change pass.

## Dependency, security, and network discipline

Direct dependencies are architecture/security/offline surface area. Add or materially
change them only with explicit purpose, bounded version policy, compatibility/security
review, and preflight evidence.

The supported portable/core path must not silently depend on:

- undeclared global packages;
- personal cloud credentials;
- hidden runtime package/model download;
- ambient provider configuration;
- untracked local state;
- optional provider SDKs imported by the portable core.

Real credentials, private keys, access tokens, passwords, or sensitive source payloads do
not belong in source, fixtures, logs, generated evidence, or canonical history.

## Documentation synchronization

Durable implementation choices belong in the smallest current implementation owner.
Architecture changes update current architecture and ADR rationale through Class 3
governance. Semantic/experience changes reopen the appropriate upstream layer.

README, examples, phase records, generated knowledge, tests, and source code remain below
canonical authority.

## Support / release non-claims

No implementation or merge may imply a broader support claim than executed evidence.

Current unqualified surfaces include production Spark/Databricks/provider support,
enterprise-scale qualification, Python lines beyond 3.11, public compatibility windows,
deployment/IaC, SLO/SLA, and public-release readiness.

The exact evidence boundaries and carried residuals are owned by
[Repository Implementation Readiness & Residual Risk](repository-implementation-readiness-residual-risk.md).

## Definition of done

A material authorized implementation slice is merge-ready only when:

1. current authority and scope are identified;
2. required package/traceability metadata is coherent;
3. implementation and documentation are synchronized at the smallest owner;
4. required deterministic/unit/fitness/integration/security/platform checks pass;
5. compatibility/migration effects are explicit where applicable;
6. dependency/network/security/scale implications are explicit;
7. unresolved limitations and follow-up remain visible;
8. completion does not self-authorize the next work item.

## Current boundary

**No next implementation program is authorized.** The repository is ready for a future
explicit start gate; that gate must select scope, authority, implementation-package
decomposition, verification obligations, relevant RR-016 residuals, and stop/reopen
conditions before sustained implementation begins.
