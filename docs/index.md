---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design & Implementation Knowledge
status: active
---

# SYNGAN Design & Implementation Knowledge

This directory is the canonical knowledge bundle for SYNGAN.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > current architecture design
  > implementation planning
  > later explicit implementation re-entry
  > code / tests / deployment
  > ADR rationale / phase history / backlog / examples
```

Existing source/tests never become upstream design authority merely because they exist or pass.

## Current posture

[Phase 007 Design Continuation & Implementation Freeze](authority/phase-007-design-continuation-implementation-freeze.md) governs current work.

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
architecture design         ACTIVE
new implementation          FROZEN
new executable restrictions FROZEN
```

No `SYNC-16`.

## Phase 007 design progression

```text
007-A..007-C  historical/provisional bootstrap work
007-D         DESIGN COMPLETE
007-E         DESIGN COMPLETE
007-F         DESIGN COMPLETE
007-G         DESIGN COMPLETE
007-H         DESIGN COMPLETE
007-I         DESIGN COMPLETE
007-J         next eligible design subgroup — scope re-evaluation required
007-K         not started
```

Implementation remains frozen at the retained 007-C scaffold; 007-D and later production implementation are not authorized.

## Current architecture continuation

### 007-D — identity / references / views

[007-D architecture](architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md) separates logical identity, exact semantic revision/commitment, mutable current-state version/freshness, representation schema version and authority/provider context.

### 007-E — persistence / transactions / history / migration

[007-E architecture](architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md) establishes owner-controlled writes, same-boundary atomic visibility, durable cross-boundary intent, stale-write conflict detection, exact material history/reference semantics, migration as representation change, and regressive-recovery qualification.

### 007-F — distributed data state / topology / promotion

[007-F architecture](architecture/phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md) establishes logical subject/physical representation separation, bounded logical scopes, exact source-state strength, cross-scope coordination, bounded manifests, candidate/seal separation and Generation-owned promotion.

### 007-G — Strategy/runtime/security closure

[007-G architecture](architecture/phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md) separates semantic Strategy/method authority from executable binding/dependency/runtime realization; requires exact Attempt-scoped composite closure, explicit provisioning rather than hidden fallback, current authorization/use-time secrets, and role-specific distributed runtime closure.

### 007-H — Execution/recovery/admission

[007-H architecture](architecture/phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md) establishes stable Execution with distinguishable Attempts, operation-scoped idempotency, non-regressing recovery authority, stale-writer fencing, qualified immutable checkpoints, durable cancellation, and admission as current operational eligibility distinct from semantic readiness and write authority.

### 007-I — Evaluation/Evidence/history/reproducibility/disclosure

[007-I architecture](architecture/phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md) establishes:

- runtime Evaluation results distinct from semantic Evaluation validation and Evidence establishment;
- independently interpretable retry-idempotent Evidence findings;
- immutable Evidence finding semantics distinct from current applicability;
- negative and indeterminate Evidence preserved without overclaiming;
- exact Generation completion-basis history;
- privacy/disclosure Evidence distinct from formal privacy guarantee, disclosure authorization and release approval;
- narrow typed canonical Provenance over exact references;
- directly retained, reconstructed, partial and unknown historical knowledge distinctions;
- exact bounded historical query with derived non-authoritative projections;
- query freshness that does not pretend to be globally atomic when it is not;
- disclosure protection for existence, graph shape, counts, reverse traversal and reason text as well as values;
- canonical historical knowledge distinct from actor-visible knowledge;
- historical reproducibility support distinct from current reproduction feasibility and actor-visible assessability;
- strongest-defensible reproduction classes constrained by actual identity/nondeterminism/approximation/equivalence/history support;
- reproduction readiness distinct from actual new reproduction work.

Earlier Phase 005-D through 005-I concrete technologies, types, SPIs, storage/index/query APIs and package choices remain provisional implementation-planning evidence rather than current architecture requirements.

## Provisional executable scaffold

The retained 007-B/007-C package/tests/CI remain feasibility/history evidence and may be revised later if architecture requires it. Existing delivery-state fitness assertions are known to be provisional and are not updated during the design freeze merely to mirror each design subgroup transition.

## Complete capability target

The structured-data target remains:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The complete supported baseline also retains source-derived/local free-form-text synthesis without mandatory public model-hub or runtime inference-service dependency.

## Current next boundary

The earlier executable wording for 007-J must be re-evaluated before any reference implementation proof can be authorized.

**007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary** is the next eligible **design** subgroup.

It requires an explicit proceed decision. Production implementation remains frozen independently of design progression.
