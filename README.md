# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project deliberately completes conceptual, experience, architecture and implementation-planning work before production coding is authorized. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current authority includes:

- [`Phase 006 Consolidated Design Readiness Contract`](docs/authority/phase-006-consolidated-design-readiness-contract.md)
- [`Phase 006 Architecture Reconciliation Contract`](docs/architecture/phase-006-architecture-reconciliation-contract.md)
- [`Phase 006 Implementation-Planning Reconciliation`](docs/implementation/phase-006-implementation-planning-reconciliation.md)
- [`Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract`](docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md)
- Phase 006 cross-cutting authority under [`docs/authority/`](docs/authority/index.md)
- [`Core Synchronizations`](docs/synchronizations/core-synchronizations.md)

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- **Phase 001 — Design Foundation & Concept Discovery: complete**
- **Phase 002 — Concept Specification & Invariant Refinement: complete**
- **Phase 003 — Experience & Workflow Design: complete historical baseline**
- **Phase 004 — Representation & Architecture Design: complete historical baseline**
- **Phase 005 — Implementation Planning & Delivery Decomposition: complete as planning only**
- **Phase 006 — Post-Planning Design Validation & Adversarial Refinement: complete**
- **Phase 007 — Implementation Authority, Controlled Bootstrap & Evidence-Gated Delivery: subgroup design complete, not active**

No production implementation has begun or been authorized.

## Phase 006 exit

006-J completed the final cross-layer replay and residual design-debt audit.

The canonical decision is:

```text
DESIGN COMPLETE ENOUGH FOR A LATER
EXPLICIT IMPLEMENTATION-AUTHORITY PHASE
```

This is intentionally **not** equivalent to `implementation authorized`.

The current baseline remains:

```text
11 accepted concepts
15 accepted synchronizations
10 active ADRs
0 provisional concepts
```

No `SYNC-16` was required.

## Complete structured-data capability target

The first complete SYNGAN structured-data baseline includes:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

Topology remains composable, so a multi-table subject may contain time-series child scopes rather than being forced into one exclusive mode.

Before claiming complete-baseline support, later implementation must provide at least one supported self-contained Strategy path for each family.

The supported baseline also includes a source-derived/local free-form-text synthesis path that does not require a pretrained model hub or runtime inference API. Optional pretrained/world-knowledge text remains explicit local-artifact or network-dependent capability.

## Key architecture consequences

Phase 006 established, among other rules:

```text
restored control state
    != current mutation authority

driver import success
    != cluster executor readiness

resource pressure
    != permission to weaken semantics

topology preset
    != durable semantic topology

synthetic / favorable privacy Evidence
    != formal privacy guarantee
    != release approval
```

ADR-0009 adds non-regressing recovery authority after stale control-state restore.

ADR-0010 adds explicit acquisition closure plus distributed runtime closure across every material worker.

## Phase 007 logical subgroup design

The planned Phase 007 structure is documented at [`docs/phases/007/index.md`](docs/phases/007/index.md).

It intentionally does **not** attempt to implement the entire complete product baseline in the bootstrap phase. The sequence is:

```text
007-A  authority lock / slice authorization
007-B  reproducible toolchain + verification harness
007-C  source/package topology + architecture fitness
007-D  identity / serialization / public handle foundation
007-E  control persistence / CAS / history / migrations
007-F  distributed data / topology / manifests / promotion
007-G  runtime binding / dependency trust / security / worker closure
007-H  Execution / fencing / recovery / cancellation / admission
007-I  Evidence / Provenance / history / reproducibility / disclosure
007-J  bounded self-contained single-table Spark-local vertical proof
007-K  consolidation / evidence audit / next-delivery decision
```

007-J is deliberately a bounded first vertical proof, not a claim of complete topology breadth or enterprise-scale certification. The shared substrate must already remain compatible with time-series and multi-table topology so later delivery does not have to undo single-table assumptions.

## Current next step

**007-A — Implementation Authority Lock, Canonical Baseline, Change Control & Slice Authorization** is the proposed next subgroup.

Phase 007 is still **not active**. 007-A must be explicitly entered and complete the authority lock before any production package/source/schema/test/CI implementation is permitted.
