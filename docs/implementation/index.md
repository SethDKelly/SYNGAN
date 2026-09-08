---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Purpose

This directory is the canonical home for **implementation planning** that translates accepted architecture into future source boundaries, interfaces, persistence, deployment, verification, delivery sequencing and acceptance evidence.

**Phase 005 remains planning-only.** These documents may select concrete future technologies and contracts, but they do not authorize production code, schema, adapters, tests, CI or deployment infrastructure.

Implementation planning is downstream of the [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md) and cannot redefine concepts, synchronizations, experience or architecture for implementation convenience.

005-K must explicitly determine whether the Jackson design program is complete enough for a later implementation-authority phase or whether another design/refinement phase is required.

## Start here

1. [Implementation governance](implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — 005-A.
2. [Verification/fitness/quality gates](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md) — 005-B.
3. [Source/package/toolchain topology](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — 005-C.
4. [Public/control-plane identity, persistence and migration](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) — 005-D.
5. [Spark data boundary, manifests and promotion](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md) — 005-E.
6. [Runtime extension SPI and Learned State](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md) — 005-F.
7. [Execution/recovery/fencing/cancellation](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md) — 005-G.
8. [Evidence/Provenance/history/reproducibility](evaluation-evidence-provenance-historical-query-reproducibility-plan.md) — 005-H.
9. [Dependency/offline/security/redaction](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-plan.md) — 005-I.
10. [Deployment/platform/observability/compatibility/scale](deployment-platform-adapters-observability-compatibility-scale-performance-plan.md) — 005-J.
11. [Phase 005 navigator](../phases/005/index.md) — current sequence and exit gate.

For progressive disclosure, read only the active slice plus directly referenced upstream authority; do not load the full corpus by default.

## Authority relationship

```text
authority / concepts / synchronizations
        ↓
experience
        ↓
architecture
        ↓
implementation planning
        ↓
future code / deployment
```

Future code remains realization, not authority over upstream contracts.

## Consolidated plan map

| Slice | Future implementation responsibility |
|---|---|
| 005-A | change governance, dependency/toolchain policy, acceptance evidence |
| 005-B | V0-V11 verification, AF-01..20 fitness, Q0-Q4 gates |
| 005-C | one `src/syngan` package, inward dependency direction, foundational toolchain |
| 005-D | ResourceRef/revision/state/schema model, public handles, SQL control persistence, CAS/outbox/migrations |
| 005-E | exact source state, distributed manifests, candidate/sealed snapshot/output promotion |
| 005-F | executable bindings, activity-specific runtime SPI, Learned-State representation/codecs |
| 005-G | Execution/Attempt, AttemptEpoch/WriterFence, checkpoints, recovery, reconciliation, cancellation |
| 005-H | Evidence establishment, canonical typed Provenance, bounded history/query, reproducibility assessment |
| 005-I | dependency resolution/trust, offline/no-egress, authorization, capabilities, secrets, redaction/isolation |
| 005-J | deployment profiles, platform adapters, observability, HA/DR, compatibility/support, scale/performance |

## Key cross-slice invariants

Future implementation must preserve at least:

- platform/runtime/payload objects never replace SYNGAN durable identity;
- exact historical references never silently resolve to latest;
- semantic completion remains owner-side and distinct from runtime/platform success;
- duplicate physical work cannot create duplicate semantic authority;
- stale Attempts are fenced; lease expiry is not fencing;
- checkpoint/candidate/runtime material remains non-final;
- Evidence claim strength cannot exceed Evaluation support;
- Provenance remains typed canonical relationships, not a metadata warehouse;
- query/search/telemetry/security audit remain derived or separate lanes;
- reproducibility remains qualified assessment, not Boolean inheritance;
- authorization cannot broaden committed semantics;
- handles are not credentials and bearer secrets are non-canonical;
- offline/no-egress profiles have no hidden acquisition, telemetry or remote fallback;
- enterprise paths do not require full source/output/Learned-State collection on the driver;
- platform support is capability-negotiated and fallback must preserve semantics;
- a regressive control-store restore cannot resurrect stale writer authority: recovery quarantine and a fresh `ControlPlaneIncarnation`/equivalent fence context are required where needed.

## 005-J deployment/platform plan

005-J adds the future deployment realization contract:

- local/development, portable Spark, managed Databricks-oriented and private/offline/no-egress profiles;
- optional advanced hybrid composition with explicit cross-domain/security requirements;
- guarantee-oriented `PlatformCapabilityDescriptor` and contextual `PlatformCompatibilityAssessment`;
- durable reference transport across service boundaries rather than serialized live DataFrame/model/session objects;
- restartable/horizontally safe coordinators over the PostgreSQL reference control-store family;
- generic Spark as a first-class profile when required contracts are supplied;
- Databricks as an optional adapter target whose jobs/versioning/identity/secrets/lineage remain subordinate integrations;
- optional OpenTelemetry/OTLP-oriented vendor-neutral telemetry integration with no offline exporter requirement;
- canonical history, runtime telemetry and security audit kept distinct;
- multi-axis compatibility/support tiers and rolling-upgrade safety;
- multi-dimensional benchmark evidence rather than row-count-only scale claims;
- disaster-recovery quarantine and `ControlPlaneIncarnation`/equivalent fencing after potentially regressive restore;
- V10/V11 and AF-01/02/03/07/09/10/11/12/13/14/15/17/18/20 obligations.

No deployment/platform implementation was created by 005-J.

Phase record: [005-J](../phases/005/005-J-deployment-platform-adapters-observability-compatibility-scale-performance-implementation-plan.md).

## Current state

**005-A through 005-J are complete as plans only.**

Next:

**005-K — Cross-Slice Integration, Delivery Sequencing, Backlog Closure, Jackson-Methodology Completeness & Implementation-Readiness Exit**.

005-K must not assume coding is next. It must either approve a later explicit implementation-authority phase or require additional design refinement.
