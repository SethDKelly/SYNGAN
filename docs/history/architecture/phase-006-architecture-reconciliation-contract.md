---
type: Architecture Contract
title: Phase 006 Architecture Reconciliation Contract
status: active
---

# Phase 006 Architecture Reconciliation Contract

## Purpose

Promote the accepted Phase 006 design refinements into current architecture authority and define how they modify the Phase 004 architecture baseline before any production implementation begins.

This contract is the **current architecture overlay** over the historical [Phase 004 Consolidated Architecture Contract](phase-004-consolidated-architecture-contract.md). Phase 004 remains valid for every rule not explicitly refined here.

This document does not authorize implementation. It selects no production schema, package class hierarchy, Spark packaging mechanism, database, scheduler, policy engine, UI, REST shape, deployment topology, model algorithm, or test harness.

## Governing upstream authority

This contract is downstream of:

- [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md);
- [Self-Contained Execution & Runtime Distribution Closure Contract](../authority/self-contained-execution-runtime-distribution-closure-contract.md);
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](../authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md);
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](../authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md);
- [Structured-Data Topology & Relationship Semantics Contract](../authority/structured-data-topology-relationship-semantics-contract.md);
- [Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract](../experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md);
- [Core Synchronizations](../synchronizations/core-synchronizations.md).

Accepted concept/synchronization counts remain **11 / 15**.

## Authority and precedence

For current architecture work:

```text
Phase 006 upstream authority / concepts / synchronizations / experience
        ↓
THIS Phase 006 Architecture Reconciliation Contract
        ↓
Phase 004 Consolidated Architecture Contract
        ↓
Phase 004 detailed architecture authorities
        ↓
Phase 006 implementation-planning reconciliation
        ↓
future implementation
```

Where this contract explicitly refines a Phase 004 statement, this contract governs current architecture. Otherwise the Phase 004 contract remains authoritative.

## ADR reconciliation result

Phase 006 does **not** supersede ADR-0001 through ADR-0008.

Most findings refine those existing decisions without changing their core alternatives/choice:

- ADR-0001 typed resource/handle API is refined by orthogonal actionability/disclosure/history views and topology summaries;
- ADR-0002 identity/version separation is refined by stable Data Meaning relationship-assertion references and historical reconstruction state;
- ADR-0003 distributed output promotion is refined by coordinated multi-scope/time-series completion;
- ADR-0004 semantic/runtime separation is refined by composite implementation closure and topology-specific Strategy capability;
- ADR-0005 Attempt fencing remains valid for ordinary recovery;
- ADR-0006 provenance/history is refined by reconstructed/partial/unknown historical knowledge;
- ADR-0007 security is refined by existence-protected disclosure and privacy/release boundary presentation;
- ADR-0008 platform negotiation is refined by runtime-distribution closure, multidimensional scale and capability-specific degraded support.

Two material new architecture decisions receive dedicated ADRs:

- [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](../decisions/ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md);
- [ADR-0010 — Self-Contained Distributed Runtime Closure](../decisions/ADR-0010-self-contained-distributed-runtime-closure.md).

These extend rather than supersede ADR-0005/0004/0008.

## Reconciled end-to-end architecture

The current architecture path is now:

```text
editable intent + resolved semantic topology
        ↓
contextual readiness / compatibility / actionability
        ↓
semantic commitment
exact revisions + logical scopes + topology semantics + requirements
        ↓
durable control identity / commitment snapshot
        ↓
dependency + security + platform + runtime-closure resolution
        ↓
Execution
        ↓
Attempt + writer fence + current recovery-authority frontier
        ↓
distributed runtime roles with exact compatible closure
        ↓
non-final candidate/checkpoint/diagnostic state
        ↓
whole-scope seal / validation / Evidence
        ↓
owner-side semantic promotion/finding
        ↓
typed Provenance + current/historical/reconstructed knowledge
        ↓
security-filtered bounded views / comparison / reproducibility
```

At every stage, resource pressure/admission may delay or block realization but cannot silently weaken the committed semantics.

## 1. Public API and experience representation reconciliation

### Orthogonal state instead of one universal status

Architecture SHALL support bounded typed views that can preserve independent dimensions equivalent to:

- owner semantic lifecycle state;
- Execution/Attempt operational state;
- current actionability;
- authority-continuity state;
- compatibility/support limitations;
- disclosure/redaction state;
- historical-knowledge quality.

These need not be seven universal enums or one persisted record. They are representational obligations.

A public handle/result interface MUST NOT require clients to infer these distinctions from one `status`, Boolean success flag, platform job state, or exception string.

### Actionability representation

Architecture must permit outcomes equivalent to:

- runnable/ready;
- queued/deferred;
- blocked;
- incompatible;
- supported with limitations;
- denied/non-disclosing security outcome where applicable;
- indeterminate.

Normal readiness/queueing/blockage should be representable as typed results/views rather than only exceptional control flow.

The exact API/HTTP/exception encoding remains later implementation design.

### Safe reason and next-action representation

Where disclosure policy permits, a result should be able to reference:

- affected requirement/capability;
- safe bounded reason/category;
- retry/resume qualification;
- legitimate next actions.

Suggested next actions cannot silently convert a semantic change into retry.

## 2. Control-plane identity, history and recovery reconciliation

### Non-regressing recovery authority

Potentially regressive restore adds an architecture axis distinct from existing `StateVersion`, `AttemptEpoch`, semantic revision, and schema version.

The realization may be named `ControlPlaneIncarnation`, recovery authority generation, external fence generation, or equivalent.

The invariant is:

> restored control state may describe historical truth but cannot by itself restore current mutation authority.

A recovery-authority frontier MUST be established from a source/mechanism that cannot be satisfied solely by stale values restored from the snapshot.

### Recovery quarantine/restricted state

During potentially regressive recovery, architecture must support a cross-cutting recovery-restricted condition in which:

- current write/promote authority is unverified;
- read-only inspection may remain possible;
- surviving work/effects are reconciled;
- restored writer/cancellation/security projections do not authorize mutation;
- new write-capable Attempt/capability issuance waits for a fresh authority frontier.

This condition is not duplicated into each domain lifecycle.

### Regressive restore and active credentials

Where stale external workers can bypass the current SYNGAN fence boundary, deployment/security adapters may need to rotate/revoke provider credentials, namespaces, tokens, leases or provider-native fence generations.

A platform that cannot achieve this must declare restore-safe overlapping recovery limited/unsupported.

### Historical knowledge quality

Historical/query architecture SHALL represent, where material:

- directly retained canonical fact;
- reconstructed fact with basis;
- partially known interval/state;
- unavailable retained material;
- unknown/indeterminate occurrence.

A reconstruction is append/audit history and MUST NOT silently masquerade as a directly retained original write.

Reconstruction may establish an owner transition only when the original owner's normal invariants and completion basis can be proven sufficiently.

## 3. Structured-data topology and Data Meaning reconciliation

### Logical scope graph without a new Relationship concept

Architecture must permit Data Meaning revisions to contain addressable structural assertions describing relationships among logical scopes/subjects.

Examples include:

- shared-key correspondence across scopes;
- parent/child/association roles;
- entity/series membership;
- ordering/time roles;
- descriptive cardinality/participation meaning.

Architecture MAY expose a stable assertion ID/reference scoped to the exact Data Meaning revision, conceptually:

```text
DataMeaningRevisionRef
    +
StructuralAssertionRef
```

This is precise addressing, not a standalone Relationship resource/concept.

### Descriptive/prescriptive/request separation

Representation must not merge:

```text
shared-key / sequence meaning       → Data Meaning
referential / temporal validity     → Constraint
requested topology / horizon/scope  → Generation
capability / limitations            → Strategy
finding / fidelity / privacy        → Evaluation / Evidence
```

A physical foreign key, Spark schema, catalog relation, or timestamp metadata may inform/realize these semantics but cannot replace them.

### Composable topology

The durable representation MUST support composition rather than require one exclusive `single_table | time_series | multi_table` discriminator.

A convenience preset may resolve into a richer structure, including a multi-table subject with one or more time-series child scopes.

### Complete baseline capability target

Architecture and verification/planning must remain capable of delivering at least one supported self-contained Strategy path for each complete-baseline family:

1. single-table;
2. time-series;
3. multi-table shared-key.

The architecture must not hard-code single-table assumptions into source/output refs, manifests, Strategy SPI, Evaluation subject identity, or result promotion.

## 4. Distributed data/materialization reconciliation

### Multi-scope logical source/output refs

A single committed logical source or completed Generation output may contain multiple named/typed logical scopes and/or sequence-bearing scopes.

The control plane stores bounded topology/scope descriptors and exact refs; row data remains distributed.

### Manifest requirements

A sealed logical candidate/output representation must be able to establish closure/integrity across all mandatory constituent scopes and distributed components.

Whole-result sealing/completion cannot treat one table/sequence as sufficient when another mandatory scope is absent or unresolved.

The manifest model may be hierarchical/composite. It need not require one flat file list or one table.

### Time-series semantics

Physical partition/file ordering is not semantic sequence order. Time-series ordering derives from committed Data Meaning roles/assertions and relevant Constraints/Generation scope.

A data provider's partition order cannot substitute for semantic time/order identity.

### Coordinated promotion

Promotion remains one logical Generation result, even when several table/sequence representations are involved.

Promotion may still be metadata-only when the provider can preserve immutable closure. No copy-on-promotion requirement is introduced.

## 5. Strategy/runtime architecture reconciliation

### Topology capability declaration

Strategy and Evaluation implementation bindings must be able to declare capability/limitations for topology shapes without owning structural meaning.

Capability may express support/limits for single-table, time-series, shared-key multi-table, composite shapes, cardinality/fan-out/horizon envelopes, and other runtime-relevant forms.

### Composite implementation closure

An exact implementation binding may resolve multiple code/runtime/artifact components rather than one package/file/model.

The immutable Attempt invocation binds the exact closure identity needed to explain/reproduce the execution.

### Acquisition closure

Runtime launch must not discover missing material by undeclared installation/download/model-hub access/remote fallback.

Acquisition/provisioning remains explicit and separate from runtime.

### Worker-distribution closure

Before material work is assigned, every material runtime role must satisfy compatible exact closure.

This may be established through immutable images, environment bundles, provider-managed libraries, archives, local artifact stores, worker bootstrap contracts, or another compliant profile-specific mechanism.

The architecture does not select one universal Spark packaging mechanism.

### Dynamic workers

Where workers can be added after readiness, the deployment profile must guarantee/inherit/prove the required closure for newly eligible workers.

### Large state/model distribution

Large Learned State/model/tokenizer artifacts may be sharded, cached locally by exact identity, or loaded from shared immutable storage. Driver broadcast is optional for suitably bounded state, never universal.

## 6. Execution/admission/backpressure/recovery reconciliation

### Admission versus semantic lifecycle

Queue/admission state remains operational/actionability context and does not become domain lifecycle state.

A valid committed activity may remain queued/deferred while waiting for compatible resources.

### Lossless backpressure

Operational backpressure may reduce concurrency/rate, spill, repartition, pause or queue work only when the committed logical work and mandatory requirements remain intact.

It may not silently:

- reduce requested record count;
- shorten time-series horizon;
- drop mandatory table scopes/children;
- reduce required Evaluation coverage;
- weaken Constraint enforcement/validation;
- relax network/security posture.

### Approximation

Approximation belongs to the semantic owner whose meaning is changed and must already be committed/allowed. Runtime resource pressure cannot create new approximation semantics.

### Retry qualification

Same-Execution retry/resume requires both unchanged committed semantics and current:

- authorization;
- dependency identity/integrity/availability;
- platform/runtime compatibility;
- checkpoint/recovery compatibility;
- non-regressing recovery authority.

## 7. Evaluation/Evidence/history reconciliation

### Topology-aware subjects

Evaluation subjects may identify a whole coordinated logical output, selected related scopes, joined/shared-key scope, longitudinal trajectory, or Learned State where the Criterion requires it.

A topology subject binds the exact Data Meaning structural assertions/revision needed for interpretation.

### Privacy/disclosure Evidence

Architecture must support threat-model-specific privacy/disclosure Criteria and sensitive diagnostic refs without introducing a universal privacy score or guarantee.

Empirical Evidence remains distinct from any future mechanism-specific formal privacy authority.

### Formal DP boundary

No initial architecture/persistence contract is permitted to imply built-in differential privacy through generic `epsilon`, `delta`, privacy-budget or guarantee fields.

If future composable DP enters scope, concept discovery must occur first; architecture follows the accepted mechanism-specific concept(s).

### External release governance

Architecture may expose an external governance handoff/integration and enforce current authorization, but no canonical Generation/Output/Evidence field becomes a universal release-approved flag.

### Historical/reproducibility gaps

Reproducibility assessment must incorporate historical continuity gaps. A known completed output can remain historically valid while reproduction support weakens to `insufficient context` because exact post-backup runtime/dependency/history facts are unavailable.

## 8. Security/disclosure reconciliation

### Existence-protected responses

When policy protects existence itself, outward views/errors may intentionally avoid distinguishing absent from forbidden/withheld.

Internal canonical/security-audit state remains precise where permitted.

Architecture must therefore separate:

- internal authorization/audit reason;
- actor-safe disclosure result/reason.

### Redaction remains view-time

Redaction/authorized summary does not mutate canonical Evidence/Provenance/history.

### Capability issuance after recovery

Sensitive/retry/resume capabilities are issued only under current authorization and established recovery authority. Restored old grants/capabilities are never sufficient by themselves.

### Offline/no-egress runtime closure

A no-egress profile is valid only if all runtime roles and required dependencies can execute without undeclared acquisition/egress. Driver-only offline readiness is insufficient.

## 9. Platform/compatibility/scale/observability reconciliation

### Platform capability vocabulary expands

Platform compatibility must cover at least:

- current recovery-authority enforcement after regressive restore;
- worker-runtime distribution closure;
- exact source/output snapshot/materialization semantics;
- stale-writer/candidate fencing;
- workload launch/reconciliation/cancellation;
- identity/secrets/network/egress/audit;
- topology/materialization capabilities;
- distributed Learned-State loading;
- multidimensional scale envelope;
- history/projection availability;
- telemetry capability.

### Capability-specific degraded support

A platform/deployment does not report one `degraded` Boolean. It reports which capability is absent/limited and the resulting actionability/semantic consequence.

### Multidimensional scale

Support claims consider at least rows, bytes, width, cardinality, skew, partitioning, model/Learned-State size, concurrency, Evaluation coverage, time-series horizon/entity distribution, and multi-table fan-out/cross-scope cost.

A source-size-proportional driver-local stage invalidates an enterprise-scale claim for that path.

### Observability lanes

Canonical history, runtime telemetry, and security audit remain distinct.

Telemetry loss generally reduces observability rather than semantic validity unless a deployment/security profile makes a particular audit/monitoring control mandatory.

No required external telemetry is introduced into offline/no-egress support.

## 10. Verification/fitness reconciliation

The future verification plan must add/strengthen architecture fitness checks for at least:

- regressive restore with surviving stale worker cannot regain authority;
- fresh recovery-authority frontier required before write-capable continuation;
- reconstructed/unknown historical interval does not become fabricated fact;
- driver import success does not establish executor/runtime closure;
- dynamically added incompatible worker cannot receive material work;
- missing runtime artifact cannot trigger undeclared public acquisition;
- large state can be loaded without universal driver materialization;
- resource pressure does not alter quantity/horizon/topology/coverage/Constraint semantics;
- topology preset resolves to exact semantic structure and composite topology remains representable;
- whole multi-scope/time-series result completion requires every mandatory constituent/validation;
- privacy Evidence cannot become formal guarantee/release approval;
- existence-protected query/error avoids enumeration while internal audit remains precise;
- queued/blocked/incompatible/denied/indeterminate remain distinguishable programmatically;
- current versus historical/reconstructed state remains distinguishable.

No executable test is created by this contract.

## 11. Architecture document reconciliation map

The detailed Phase 004 authorities remain current except as refined here:

| Phase 004 authority | Phase 006 refinement |
|---|---|
| 004-B public API | orthogonal experience/actionability/disclosure/history/topology views |
| 004-C identity/persistence | structural-assertion refs; historical reconstruction quality; recovery-authority axis |
| 004-D Spark data boundary | multi-scope/composite manifests; time-series semantics; whole-topology closure |
| 004-E runtime/SPI | composite implementation closure; topology capability; worker runtime closure |
| 004-F Execution/recovery | non-regressing restore authority; admission/backpressure/retry qualification |
| 004-G Evidence/history | topology subjects; privacy Evidence boundary; reconstructed/partial history |
| 004-H security | existence-protected outward errors; post-recovery capability issuance; offline worker closure |
| 004-I deployment | runtime-distribution capability; multidimensional scale/degraded support; restore-safe profile capability |

The Phase 004 documents need not be rewritten wholesale; this contract is the current canonical overlay and must be read first for implementation work affected by Phase 006.

## 12. Implementation-planning handoff

The current downstream planning overlay is:

[Phase 006 Implementation-Planning Reconciliation](../implementation/phase-006-implementation-planning-reconciliation.md).

That document updates the future delivery obligations of the Phase 005 plans without rewriting historical Phase 005 records.

## Invariants

1. Phase 006 architecture MUST remain downstream of the accepted 11 concepts / 15 synchronizations.
2. Regressive restore MUST NOT restore current mutation authority merely by restoring old current-state/fence values.
3. Recovery authority after possible regression MUST include a non-regressing frontier distinct from restored stale state.
4. Driver/coordinator runtime availability MUST NOT establish distributed-worker runtime closure.
5. Missing worker dependencies MUST NOT trigger undeclared acquisition or remote fallback.
6. Data topology MUST remain composable and MUST NOT be reduced to one exclusive mode enum.
7. Structural relationship semantics MUST remain Data Meaning-owned rather than becoming a hidden Relationship resource owner.
8. Multi-scope/time-series physical completion MUST NOT become whole Generation completion before all mandatory scope/validation obligations are met.
9. Resource pressure/admission/backpressure MUST NOT silently weaken committed semantics.
10. Privacy/disclosure Evidence MUST NOT become formal privacy guarantee or release approval.
11. Initial architecture MUST NOT advertise or encode generic built-in differential privacy accounting.
12. Existence-sensitive security responses MAY intentionally be non-disclosing while internal audit/canonical truth remains precise.
13. Historical reconstruction/unknown/unavailable MUST remain distinguishable from directly retained fact.
14. Public/programmatic surfaces MUST preserve actionability/recovery/disclosure/history distinctions without one universal status.
15. Platform support MUST remain capability-negotiated and capability-specific when limited/degraded.
16. No Phase 006 rule authorizes production implementation.

## Exit condition for 006-I architecture side

Architecture reconciliation is complete when:

- this contract is active and indexed as current architecture authority;
- ADR-0009 and ADR-0010 are active;
- the downstream implementation-planning reconciliation is active;
- the repository no longer routes new work directly from Phase 004/005 as though Phase 006 refinements did not exist;
- 006-J can replay the affected scenarios/probes against one coherent current architecture/planning baseline.
