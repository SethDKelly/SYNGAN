---
type: Architecture Decision Record
title: ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery
status: active
---

# ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery

## Decision context

ADR-0005 establishes Attempt-epoch fencing for ordinary retries, overlapping Attempts, coordinator loss, and stale writers. Phase 005-J and Phase 006-B exposed a stronger failure mode: the persistence substrate that records the current Attempt/fence may itself be restored to an older point while post-backup workers or external effects still exist.

Example:

```text
T1  control-state backup
T2  newer Attempt/fence/cancellation/security state established
T3  external worker continues
T4  control store fails
T5  restore T1 backup
```

If the restored control state is accepted as current authority, an old fence or Attempt that was superseded after T1 can appear current again. Ordinary CAS, AttemptEpoch, cancellation generation, or database transaction correctness cannot prevent this because the authoritative persistence history itself has regressed.

The architecture therefore needs a recovery authority boundary that does not derive its freshness solely from the state being restored.

## Governing authority

- [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md)
- [Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract](../experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md)
- [Execution](../concepts/execution.md)
- [Core Synchronizations](../synchronizations/core-synchronizations.md)
- [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md)

## Decision

SYNGAN adopts a **non-regressing recovery-authority boundary** for any recovery that may restore canonical control state to an earlier authority point.

A potentially regressive restore SHALL enter a recovery-restricted/quarantine condition in which restored current-state/fence/cancellation/security projections are historical evidence, not sufficient current mutation authority.

Before ordinary write-capable work resumes, the deployment SHALL establish a fresh authority frontier that cannot be satisfied solely by stale state from the restored snapshot.

An implementation may realize this through a `ControlPlaneIncarnation`, external monotonic generation, provider-native fencing generation, rotated credential/namespace boundary, or another mechanism that provides equivalent non-regression semantics.

The exact mechanism is not a domain concept and is deployment/control architecture.

Effective write authority after recovery is conceptually constrained by:

```text
fresh recovery authority frontier
        +
Execution / Attempt authority
        +
Attempt epoch / writer fence
        +
cancellation generation
        +
current security capability
```

where material.

Surviving post-backup workers never regain their prior writer authority merely because they remain alive. Verified immutable effects MAY be adopted by current recovery authority after reconciliation; adoption is not resurrection of the old writer.

Missing post-backup canonical facts remain reconstructed/partial/unknown/unavailable according to retained evidence. Physical artifact existence neither proves nor disproves that a semantic transition occurred.

## Alternatives considered

### 1. Trust the restored current Attempt/fence

Rejected. This directly permits stale authority resurrection when the backup predates a newer Attempt, cancellation, revocation, or semantic transition.

### 2. Rely only on ADR-0005 AttemptEpoch

Rejected as incomplete for regressive restore. AttemptEpoch is monotonic only relative to the persisted history that issued it. Restoring older persistence can restore an older maximum epoch.

ADR-0005 remains necessary inside one non-regressing authority frontier; ADR-0009 adds the cross-restore boundary.

### 3. Stop all known workers before restore

Rejected as a universal correctness mechanism. A provider may be unreachable, acknowledgement may be ambiguous, credentials may have escaped to surviving processes, or the system may not know every external effect. Worker termination is useful operational hygiene but is not sufficient authority proof.

### 4. Treat all post-backup effects as invalid

Rejected because independently verified immutable effects may legitimately be reusable and because some semantic transitions may have occurred even when the restored database no longer records them.

### 5. Treat all observed post-backup effects as authoritative

Rejected because artifact/process existence is insufficient evidence of owner-side semantic completion or canonical promotion.

### 6. Fork canonical history into two equally current branches

Rejected for the current product model. SYNGAN eventually re-establishes one current authority frontier. Uncertain post-backup facts are reconciled/reconstructed/quarantined rather than treated as an indefinitely branching current-state model.

## Consequences

### Positive

- database restore cannot silently resurrect stale writers;
- cancellation/revocation/fencing safety survives regressive persistence recovery;
- surviving workers can be reconciled without granting them current authority;
- historical uncertainty remains truthful rather than being coerced to absence/failure/success;
- immutable work may still be adopted safely when independently verified;
- recovery semantics remain portable across control stores and workload providers.

### Costs

- deployments need one non-regressing authority mechanism outside or above the restored snapshot's stale authority projection;
- recovery has a quarantine/reconciliation phase before ordinary writes resume;
- platform adapters may need credential/namespace rotation when stale external processes can otherwise mutate shared targets;
- backup/restore testing must include surviving workers and post-backup effects, not only database integrity;
- historical query/UI/API must represent incomplete/reconstructed history.

## Compatibility / migration impact

No production persistence/runtime exists yet, so there is no data migration.

Future control/runtime contracts must reserve a recovery-authority/incarnation equivalent separate from `StateVersion`, `AttemptEpoch`, semantic revision, and credential identity. A future schema may encode this explicitly or obtain it from an external fencing authority, but it must not overload one existing version field.

Any platform profile unable to enforce a non-regressing boundary in the presence of surviving stale writers must declare restore-safe overlapping recovery unsupported or limited rather than silently claiming full support.

## Canonical architecture affected

- [Phase 006 Architecture Reconciliation Contract](../architecture/phase-006-architecture-reconciliation-contract.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](../architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md)

## Relationship to prior ADRs

ADR-0009 **extends but does not supersede ADR-0005**. Attempt-epoch fencing remains authoritative for ordinary Execution/Attempt stale-writer safety; ADR-0009 defines the additional boundary needed when the persistence source of that authority may regress.

It also composes with ADR-0007 current scoped authorization and ADR-0008 platform capability negotiation.

## Supersession

Supersedes: none.

Superseded by: none.
