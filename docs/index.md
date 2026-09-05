---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology, source/provenance, network/external-dependency, and reproducibility rules.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, outcomes and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary and compatibility mappings.
- [Accepted Concepts](concepts/index.md) — canonical concept purpose, ownership, actions, lifecycle, invariants and boundaries.
- [Accepted Synchronizations](synchronizations/index.md) — canonical cross-concept coordination rules.
- [Experience & Workflow Design](experience/index.md) — start implementation-facing review with the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — start with the [Phase 004 Consolidated Architecture Contract](architecture/phase-004-consolidated-architecture-contract.md).
- [Implementation Planning & Delivery Authority](implementation/index.md) — current planning authority through control/data/runtime/recovery/history/security.
- [Architecture Decision Records](decisions/index.md) — rationale/alternatives/supersession; normative architecture remains under `docs/architecture/`.
- [Concept Discovery](discovery/index.md) — historical hypotheses, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `references/` — external references used by the design.
- `backlog/` — unresolved/deferred work that is not canonical authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, design decision, or implementation rule has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation authority / planning
  > code / deployment
  > ADR rationale / phase history / summaries / backlog where applicable
```

Implementation planning and later code MUST NOT override upstream semantic, experience, or architecture contracts for convenience.

## Completed design layers

- **Phase 001 — Design Foundation & Concept Discovery — complete**
- **Phase 002 — Concept Specification & Invariant Refinement — complete** — eleven accepted concepts and fifteen synchronizations.
- **Phase 003 — Experience & Workflow Design — complete** — [consolidated experience contract](experience/phase-003-consolidated-experience-contract.md).
- **Phase 004 — Representation & Architecture Design — complete** — [consolidated architecture contract](architecture/phase-004-consolidated-architecture-contract.md).

## Current phase

**[Phase 005 — Implementation Planning & Delivery Decomposition](phases/005/index.md) is current and planning-only.**

Completed planning groups:

- [005-A](phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — implementation governance
- [005-B](phases/005/005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md) — verification/fitness/gates
- [005-C](phases/005/005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — source/package/toolchain topology
- [005-D](phases/005/005-D-public-resource-api-control-plane-identity-state-persistence-transactions-migration-implementation.md) — control identity/state/persistence
- [005-E](phases/005/005-E-spark-data-boundary-source-output-references-manifest-materialization-promotion-implementation-plan.md) — Spark/data/materialization/promotion
- [005-F](phases/005/005-F-strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-implementation-plan.md) — runtime SPI/Learned State
- [005-G](phases/005/005-G-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-implementation-plan.md) — Execution/recovery/fencing
- [005-H](phases/005/005-H-evaluation-evidence-provenance-historical-query-reproducibility-implementation-plan.md) — Evidence/Provenance/history/reproducibility
- [005-I](phases/005/005-I-dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-implementation-plan.md) — dependency/offline/security/disclosure

Canonical implementation-planning authority is indexed under [`docs/implementation/`](implementation/index.md).

The plan through 005-I preserves:

- one future `src/syngan` package with enforced inward boundaries and optional runtime/platform/security adapters;
- one durable ResourceRef/revision/state/schema model across all slices;
- exact distributed source/candidate/snapshot/output identity;
- model-neutral Strategy/method binding and activity-specific runtime contracts;
- Learned-State logical identity separate from representation/codec/loaded object;
- stable Execution/multiple Attempt history with epoch fencing, checkpoint/recovery and cancellation linearization;
- owner-established Evidence, typed canonical Provenance and derived bounded historical query/reproducibility views;
- dependency availability/identity/integrity/trust/compatibility/authorization kept distinct;
- no hidden runtime acquisition, remote fallback, telemetry or egress;
- first-class offline/no-egress support after approved local/private provisioning;
- action-specific authorization and Attempt-scoped capabilities rather than handle-as-credential authority;
- non-secret SecretRef plus ephemeral bearer credential handling;
- truthful redaction/withholding across canonical records and derived indexes/counts/history/reproducibility;
- security audit separate from Provenance and telemetry;
- explicit tenant/security-domain isolation across control/data/history/cache/runtime surfaces;
- Phase 005 as documentation/planning only—no production package, schema, security/runtime adapter, test suite or deployment infrastructure has been implemented.

## Jackson/design completeness gate

Phase 005-K must explicitly assess whether the Jackson-style design program has progressed far enough for later implementation. It may conclude that another concept/synchronization/experience/architecture/planning refinement phase is required.

A positive readiness conclusion still does not itself authorize coding; a later explicit implementation-authority phase is required.

Next:

**005-J — Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan**

005-J will map the accepted portable architecture, security and scale guarantees onto concrete deployment/platform capability profiles and expose limitations rather than weakening common guarantees.

## Documentation governance note

The repository continues to use its project-specific OKF profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been falsely declared resolved and remains documentation-governance debt until explicitly audited against current external authority.
