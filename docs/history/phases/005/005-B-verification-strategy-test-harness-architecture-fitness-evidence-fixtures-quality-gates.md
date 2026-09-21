---
type: Phase Record
title: 005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates
status: complete
---

# 005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates

## Objective

Define the verification architecture that later source/package topology and implementation slices must satisfy so Phase 004 invariants become executable product-correctness controls rather than retrospective documentation.

005-B intentionally precedes package/source topology and concrete test-tool selection.

## Entry authority

005-B is downstream of:

- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](../../implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md);
- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md);
- [Phase 005 navigator](index.md).

## Canonical authority created

005-B establishes:

[Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md).

The central rule is:

> **A test oracle comes from accepted authority, not from current code, platform behavior, or previously captured output. Verification must prove that the implementation preserves the contract, not merely that the implementation is self-consistent.**

## Verification layers accepted

005-B defines logical verification layers V0 through V11:

| Layer | Scope |
|---|---|
| V0 | Repository and authority conformance |
| V1 | Deterministic semantic/control unit verification |
| V2 | Component and port contract verification |
| V3 | Architecture fitness verification |
| V4 | Persistence, concurrency and migration verification |
| V5 | Spark/distributed data-boundary verification |
| V6 | Runtime-extension and Learned-State verification |
| V7 | Execution, failure-injection and recovery verification |
| V8 | Evaluation/Evidence, Provenance and reproducibility verification |
| V9 | Dependency, security, offline/no-egress and disclosure verification |
| V10 | Platform-adapter and capability-conformance verification |
| V11 | Scale, performance and compatibility verification |

These are logical test responsibilities rather than final directory/package names.

## Architecture-fitness catalog accepted

005-B creates stable fitness identifiers AF-01 through AF-20 covering:

- inward dependency direction;
- optional/offline dependency closure;
- canonical identity separation;
- non-final/promoted result separation;
- immutable commitments/history;
- stale lifecycle-write rejection;
- stale Attempt fencing;
- idempotent promotion/Evidence establishment;
- runtime/platform non-authority;
- Provenance/query projection isolation;
- authorization on historical/query paths;
- hidden acquisition/network/telemetry prohibition;
- no enterprise full-driver collection;
- semantics-preserving platform fallback;
- secret exclusion;
- typed status/disclosure semantics;
- exact historical reference resolution;
- transition/Provenance crash consistency;
- Evaluation retry double-count prevention;
- managed-platform identity/lineage/retry subordination.

005-C and later slices must choose concrete mechanisms to enforce these properties. Tool choice may change; the protected property cannot be silently dropped.

## Quality-gate model accepted

005-B defines quality gates by cadence/cost:

```text
Q0  local / pre-commit fast feedback
Q1  required pull-request verification
Q2  integration / distributed verification
Q3  scheduled compatibility / resilience verification
Q4  release / support certification
```

Gate cadence does not define importance. A heavy invariant may live in Q2/Q3 while still blocking a support/release claim.

Change-aware test selection is allowed only when conservative/reviewable and must expand around shared identity, persistence, security, runtime or public-contract changes.

## Default offline/network posture accepted

Portable/core verification should execute with outbound network unavailable or explicitly denied where enforceable.

Unexpected network access is a test failure rather than an implicit test dependency.

Networked managed-platform/remote-service tests run only through explicit opt-in integration profiles with declared service, credential, permitted data classification, egress behavior and cleanup requirements.

This directly enforces the Phase 004 no-hidden-acquisition/no-egress architecture.

## Fixture architecture accepted

Fixtures are synthetic/non-sensitive by default.

Fixture classes include:

1. micro deterministic fixtures;
2. reproducibly generated medium/local-Spark fixtures;
3. ephemeral large/scale fixtures created outside ordinary Git blobs;
4. fault/control fixtures for time, randomness, provider outcomes, fencing state and failure schedules.

Reusable scenario families must cover revisioned semantic authorities, exact/mutable source states, committed activities, direct/learned generation, candidate states, Learned State lifecycle, Attempt epochs, checkpoint compatibility, Evidence claim strength, Provenance correction, dependency/security states, disclosure states and platform capability negotiation.

Real customer/production data and real secrets are prohibited from ordinary repository fixtures.

## Golden-fixture discipline accepted

Golden/snapshot fixtures are compatibility tools, not self-authorizing truth.

They are appropriate when stable persisted/wire/public representation compatibility matters.

They are not the sole oracle for stochastic synthetic values, distributed ordering, platform IDs, timestamps, runtime nondeterminism or semantic quality claims.

A material golden update to a public/persisted contract requires the appropriate Class 2+ governance rather than blind snapshot refresh.

## Deterministic and stochastic lanes separated

Identity, lifecycle, promotion, fencing, authorization and migration rules should be deterministically testable through controllable time/randomness/provider/failure seams.

Statistical/stochastic verification must predefine its hypothesis, fixture, seeds, sample/replication policy, acceptance/confidence threshold and variability bounds.

`Retry until pass` is explicitly rejected as stochastic-test reliability behavior.

## Failure/recovery verification accepted

005-B requires deliberate failure injection around material boundaries including provider submission, durable mutation, checkpoint closure, candidate sealing, Evidence establishment and semantic promotion.

Required recovery scenarios include stale writers, lost acknowledgements, unknown external effects, incomplete checkpoints, resume incompatibility, cancellation races, duplicate physical work, Evaluation double counting, and repeated promotion/Evidence requests.

This ensures at-least-once physical realization is verified against one authoritative semantic result.

## Adapter conformance accepted

Production adapters must run reusable conformance suites for the ports/capabilities they claim.

Fakes/mocks may isolate consumers but cannot replace testing the actual production adapter behavior whose property is under test.

Provider-specific suites may strengthen/common-test coverage but must not substitute weaker provider-native expectations for SYNGAN's accepted contract.

## Flakiness and quarantine policy accepted

Test assertion failures cannot be erased by silent retry-to-green.

Quarantine requires explicit defect, protected requirement/risk, owner, expiry/review condition and follow-up.

If the quarantined check is the only enforcement for a non-waivable architecture invariant, the affected capability/support claim remains blocked until valid enforcement exists.

## Waiver governance accepted

Quality-gate waivers require the exact gate/check, rationale/evidence, affected invariant, owner, expiry/review point, compensating control and follow-up.

Waivers cannot authorize semantic contradiction, known historical corruption, hidden egress/acquisition, stale-writer acceptance, duplicate semantic promotion, secret disclosure or falsified Evidence/Provenance.

Those require actual correction.

## Acceptance-evidence contract refined

A material implementation slice should retain bounded delivery evidence including:

- slice/change ID;
- upstream authority;
- implementation-plan revision;
- changed source/config/migrations;
- verification profiles and fitness results;
- fixture/scenario versions;
- relevant environment/runtime/platform versions;
- pass/fail/waiver outcomes;
- migration/compatibility/security/offline/scale results as applicable;
- known limitations/deferred items;
- CI/run/artifact references.

This delivery evidence must not be confused with the canonical SYNGAN `Evidence` domain concept.

## No premature concrete-tool selection

005-B deliberately does not choose:

- pytest or another runner;
- property-test/mocking library;
- coverage tool/threshold;
- formatter/linter/type checker;
- dependency manager/build backend;
- CI vendor;
- exact physical source/test directory layout;
- Python/Spark support versions.

Those are implementation choices for 005-C constrained by the verification properties defined here.

## 005-C handoff

005-C must choose source/package/shared-foundation topology and the foundational concrete Python/build/test/static-analysis toolchain so that:

- logical V0-V11 responsibilities have clean homes;
- AF-01 through AF-20 are enforceable;
- Q0/Q1 have stable local/CI commands;
- heavier Q2-Q4 profiles have explicit entry points;
- adapter conformance suites are reusable without core-to-adapter dependencies;
- optional dependency isolation supports offline-core verification;
- test seams support deterministic time/randomness/provider/failure injection;
- compatibility/golden fixtures are versioned deliberately;
- initial CI checks can be mapped without architecture drift.

## No architecture/semantic revision required

005-B found no verification requirement requiring changes to accepted concepts, synchronizations, Phase 003 experience, or Phase 004 architecture.

No ADR is required because 005-B defines downstream implementation-verification architecture rather than changing an architecture decision.

## Exit criteria

- [x] verification layers V0-V11 defined;
- [x] architecture-fitness catalog AF-01 through AF-20 established;
- [x] distributed/runtime/recovery/Evidence/security/platform/scale test obligations defined;
- [x] fixture and golden-data policy established;
- [x] deterministic and stochastic verification separated;
- [x] default offline/no-network core test posture established;
- [x] adapter conformance expectations established;
- [x] Q0-Q4 quality gates defined;
- [x] flakiness/quarantine/waiver governance established;
- [x] bounded acceptance-evidence contract refined;
- [x] concrete tools/topology deliberately left to 005-C;
- [x] 005-C handoff explicit.

## Exit decision

**005-B — complete.**

Next:

**005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**.
