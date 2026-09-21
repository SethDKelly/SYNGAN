---
type: Architecture Authority
title: Phase 007 Consolidated Architecture Contract
status: active
---

# Phase 007 Consolidated Architecture Contract

## Purpose

Consolidate the current SYNGAN representation/architecture authority established by 007-D through 007-J into one implementation-facing architecture spine without replacing the underlying detailed authorities or promoting implementation mechanisms into concepts.

This contract is the canonical Phase 007 architecture handoff for later implementation. The detailed 007-D through 007-J documents remain authoritative for their owned boundaries; this document defines how they compose.

## Governing precedence

Interpret this contract under the following authority order:

```text
problem / methodology / cross-cutting authority
        ↓
accepted concepts + synchronizations
        ↓
current experience authority
        ↓
THIS Phase 007 consolidated architecture
        ↓
007-D through 007-J detailed architecture where more specific
        ↓
active ADR rationale
        ↓
implementation planning / later explicit implementation authority
        ↓
production code / tests / platform realization
```

If a concrete implementation or historical Phase 005/007-A..C artifact conflicts with this architecture, the implementation artifact is reconsidered. Architecture is not weakened merely to preserve already-written scaffold code or tests.

## Catalog baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
SYNC-16                     absent
```

No new concept, synchronization or ADR is introduced by this consolidation.

## Consolidated architecture spine

The current architecture composes as:

```text
accepted semantic authority / exact commitments
        ↓
007-D stable typed identity + exact revision/reference/view boundaries
        ↓
007-E owner-controlled persistence + concurrency + durable coordination + exact history
        ↓
007-F exact logical data state + composable topology + manifested physical subject
        ↓
007-G semantic Strategy/method ↔ exact executable/dependency/runtime realization
        ↓
007-H stable Execution + distinguishable Attempts + idempotency/fencing/recovery/admission
        ↓
007-F sealed candidate / immutable material subject
        ↓
owner semantic validation / promotion
        ↓
007-I Evaluation validation → Evidence → typed Provenance
        ↓
exact historical query + qualified reproducibility + actor-safe disclosure
        ↓
007-J bounded proof/claim portfolio for implementation evidence
```

This is an authority/dependency composition, not a required process pipeline for every activity. Direct Generation may omit Learning/Learned State when its Strategy semantics do not require them. Not every Evaluation or activity requires every optional architecture role.

## 1. Identity, revision, state and representation

Current architecture preserves independent dimensions for:

- authority/namespace context where material;
- stable logical resource identity;
- exact immutable semantic revision or commitment;
- mutable current lifecycle/applicability state and its concurrency/freshness observation;
- representation schema version;
- provider/external identity or locator where useful.

A database key, path, Spark object, platform run, serialized view or provider identifier does not silently replace SYNGAN logical identity.

Historical references that require exact meaning never resolve implicitly to `latest` or current state.

Public handles/views are resolvers and actor-facing projections over canonical authority. They are not detached mutable canonical objects, and a handle/reference is not a bearer credential merely because it is serializable.

## 2. Persistence, transaction and historical-state boundaries

Canonical control persistence preserves bounded authority facts; it does not create semantic authority merely by storing them.

Owner/application logic validates material transitions. Persistence applies already-authorized transitions under the required concurrency/consistency boundary.

Where one invariant is inside a common atomic boundary, coupled canonical facts become visible together or not at all. Where coordination crosses an atomic boundary, the architecture requires durable, detectable and reconcilable intent rather than a universal distributed transaction.

Compare-and-set protects an observed mutable authority boundary but does not prove semantic transition validity, current authorization, external side-effect success or semantic completion.

Material history is append-preserving enough to explain authority transitions without requiring universal event sourcing or duplicating full canonical payloads into a shadow history store.

Migration changes representation unless an explicit upstream semantic correction says otherwise. Regressive restore cannot silently rewrite historical truth or recreate current mutation authority.

## 3. Exact data state, topology, manifestation, sealing and promotion

Logical data subject and physical representation are independent axes.

A logical subject may contain one or more bounded logical scopes and may represent:

- single-table data;
- time-series data;
- multi-table shared-key data;
- composite relational + sequence-bearing topology.

Physical table/file layout, Spark partitioning, foreign-key metadata, sort order or timestamp type does not define semantic topology. Structural relationship semantics remain Data Meaning-owned, with stable assertion addressing bound to the exact Data Meaning revision where required.

Exact source/data-state claims remain multidimensional: identity strength, read-binding strength, integrity coverage, retention/resolvability and cross-scope coordination strength must not be collapsed into one `immutable` or `snapshot` Boolean.

For generated data:

```text
open / partial candidate
    != sealed exact physical subject
    != semantically promoted logical output
```

Sealing establishes closure/integrity of the physical subject to a declared strength; it does not establish Constraint satisfaction, privacy, release approval or Generation completion.

Generation owns promotion of one successful logical completed-output identity after the committed whole-result completion barrier is satisfied.

## 4. Strategy/method authority versus executable realization

Synthesis Strategy and committed Evaluation method semantics remain separate from:

- implementation binding;
- package/model/component identity;
- resolved dependency closure;
- integrity/authenticity/trust assessment;
- current authorization;
- network/egress qualification;
- runtime-role distribution closure;
- live secret/capability access;
- physical runtime realization.

A material Attempt binds an exact executable/dependency realization before execution. Runtime cannot silently hot-swap missing packages, models, codecs, services or other behaviorally material components.

A later Attempt may use another compatible realization only when unchanged semantic commitment explicitly permits implementation-neutral realization and the new Attempt is independently attributable.

Acquisition/provisioning is separate from material runtime execution. Missing components do not justify hidden first-use installation, model download, network expansion or remote fallback.

Secret values are operational material, not canonical semantic/history/Provenance payloads. Current action authorization is evaluated at use time.

Driver/coordinator readiness is not distributed worker closure. Every material runtime role, including dynamically introduced workers, must satisfy its exact compatible role-specific closure.

## 5. Execution, Attempts, idempotency, fencing, recovery and admission

One committed Learning, Generation or Evaluation may have one stable logical Execution and multiple distinguishable Attempts while the committed semantics remain unchanged.

Observed physical/platform state is separate from current framework mutation authority.

For material writes, current authority may require the intersection of:

```text
current non-regressing recovery frontier
∩ current Execution / Attempt authority
∩ resource-local generation/precondition where required
∩ current action authorization/capability
```

Attempt epoch alone is insufficient after potentially regressive restore. Lease/heartbeat proves liveness coordination, not stale-writer exclusion.

Operation-scoped idempotency prevents ambiguous duplicate canonical effects but never grants authority after a newer fence, recovery frontier, cancellation, owner-state transition or authorization change.

Potentially regressive recovery enters continuity-unverified quarantine. A fresh non-regressing authority boundary excludes old writers before surviving effects are reconciled, reconstructed or adopted by current authority.

Surviving immutable material does not revive the producer's authority and does not by itself prove semantic promotion.

Checkpoint durability, checkpoint resume compatibility and semantic result establishment remain distinct.

Cancellation is durable intent before terminal outcome and cannot be erased merely by restoring an older control snapshot.

Admission is current operational eligibility. It is distinct from semantic readiness, authorization, queue placement, resource reservation and mutation authority. Resource shortage cannot silently weaken committed scope, quantity, topology, Evaluation coverage or security posture.

The operational target remains:

```text
at-least-once physical realization
+ fenced / idempotent / reconcilable canonical effects
→ at-most-one authoritative semantic result transition
```

## 6. Evaluation, Evidence and Generation completion

A runtime/method result is non-final until Evaluation authority validates the exact committed examination.

Validation preserves the exact Criterion, subject/reference, method/configuration, topology/scope/coverage, sampling/approximation, assumptions, uncertainty, executable realization and retry/recovery contribution context needed to support the finding.

A valid Evaluation may establish zero or more independently interpretable Evidence findings. Logical finding identity is retry-idempotent; materially conflicting replay is a consistency defect, not overwrite.

Evidence preserves immutable historical finding semantics separately from mutable current applicability.

Negative, unfavorable and indeterminate findings remain legitimate Evidence when the examination itself was valid.

Evidence claim strength cannot exceed the actual method/scope/coverage/assumption/uncertainty support.

Where Generation completion depends on validation, Generation preserves an immutable completion basis identifying the exact candidate, requirement/Constraint/Condition, Criterion and Evidence used. Later Evidence cannot retroactively enter or rewrite the original promotion basis.

Evidence never directly owns Generation promotion.

## 7. Provenance, history, reproducibility and disclosure

Canonical Provenance is typed relationship authority over exact stable references. It is not a duplicated metadata graph containing copies of canonical owner payloads.

History distinguishes at least:

```text
directly retained canonical fact
reconstructed fact with sufficient basis
partially known fact
unknown / occurrence not establishable
```

Object/reference resolution and historical-knowledge quality remain separate axes. A known historical identity may have unavailable payload; a missing projection may coexist with known canonical history.

After regressive recovery, surviving files, jobs, provider events or external lineage may support reconstruction, but do not automatically establish missing semantic transitions, Evidence or Provenance.

Historical query is bounded read composition over canonical authorities. Derived search/adjacency/reporting projections remain rebuildable and non-authoritative, and response freshness must not imply a global atomic snapshot when none exists.

Historical comparison may report differences but does not create causal, superiority or quality claims without supporting Evaluation/Evidence.

Reproducibility separates:

- historical supportability of a reproduction/comparison class;
- current reproduction feasibility under current dependencies/security/runtime/admission;
- what the current actor is authorized to inspect.

A seed alone never proves exact deterministic reproduction. Actual reproduction is new domain work whose result must meet the declared equivalence/comparison rule.

Disclosure is current actor/view authority and may protect values, existence, graph shape, endpoint identity, counts/cardinality, reverse traversal, diagnostics, dependency/runtime identities and reproducibility reasons. Redaction or non-disclosure never mutates canonical historical truth.

## 8. Privacy, security and release boundary

The architecture preserves:

```text
current security authorization
    != empirical privacy/disclosure-risk Evidence
    != formal privacy guarantee
    != external release/use approval
```

Synthetic origin, local execution or favorable Evaluation cannot create a universal `private`, `safe`, `approved` or `safe_to_release` property.

Formal/composable differential privacy remains outside the initial baseline and requires mechanism-specific concept discovery before it can become framework-owned implementation state.

## 9. Complete capability baseline

The complete structured-data capability target remains:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

with composable topology and at least one supported self-contained Strategy path for each required family before complete-baseline support is claimed.

The supported baseline also requires a source-derived/local free-form-text-capable path without mandatory pretrained model, public model hub, first-use model download or runtime inference service.

Implementation may stage these capabilities. A single-table implementation must not hard-code representation, APIs or lifecycle assumptions that make the other required families structurally impossible.

## 10. Implementation proof and claim boundary

Implementation evidence is layered into distinct claim classes:

1. architecture-conformance proof;
2. capability proof;
3. runtime/platform-profile proof;
4. resilience/adversarial proof;
5. scale/release qualification.

A first learning-based single-table local/Spark-local path may be an effective bounded reference capability proof after explicit re-entry. It is not proof of direct-generation neutrality, time-series, multi-table, distributed-worker closure, regressive recovery, managed-platform support, enterprise scale, privacy/release guarantees or release readiness.

Separate evidence is required for those claims.

## 11. Historical scaffold disposition

The retained 007-B/007-C scaffold is feasibility evidence, not an architecture premise.

Directionally compatible elements include:

- one `syngan` distribution and `src/` packaging;
- a repository-owned locked toolchain and verification entry point;
- a typed package marker;
- inward dependency intent and separation of core from adapters/bootstrap;
- portable-core network denial after explicit provisioning;
- reviewable CI as evidence rather than semantic authority.

The following remain provisional and must be explicitly reconciled at implementation re-entry:

- the exact seven top-level package set;
- exact Import Linter contracts;
- exact build/test/tool versions;
- root import restrictions;
- socket-denial exceptions required for local Spark process plumbing;
- delivery-state fitness tests that encode historical phase navigation rather than durable architecture invariants.

## 12. Architecture-fitness obligations for later executable conformance

When implementation resumes, executable fitness/conformance must be derived from durable architecture invariants rather than copied from provisional delivery structure.

Coverage must eventually include, where claimed:

- identity/revision/history exactness;
- owner-controlled transition and stale-write behavior;
- composable topology and whole-result completion;
- candidate/seal/promotion separation;
- semantic Strategy versus executable binding separation;
- no hidden acquisition;
- distributed worker closure;
- stable Execution/Attempt separation;
- idempotency/fencing/current-authority separation;
- non-regressing restore recovery;
- checkpoint/cancellation/admission distinctions;
- Evaluation validation before Evidence;
- retry-safe Evidence/Provenance establishment;
- historical reconstruction/unknown/unavailable distinctions;
- disclosure without canonical-truth mutation;
- qualified reproducibility;
- non-overclaiming across platform/scale/privacy/release boundaries.

No single test suite shape or technology is mandated by this document.

## 13. Architecture completeness verdict

Phase 007 consolidation finds no unresolved concept owner, synchronization responsibility, experience seam, architecture authority conflict or ADR decision that blocks controlled implementation re-entry.

Remaining unresolved choices are predominantly implementation realization and release qualification, including concrete classes/types, identifier encoding, databases, schemas, transaction levels, file/table formats, Spark APIs, algorithms, package/runtime distribution, policy/secret products, provider mappings, query/index engines, API spelling, benchmark thresholds and release/support matrices.

These are constrained by this architecture but do not require another design phase by default.

## Current authority state

```text
Phase 007 architecture            CONSOLIDATED
concept/synchronization model     PRESERVED — 11 / 15
new architecture blocker          NONE
implementation technology         UNSELECTED unless historically provisional
implementation re-entry           governed separately by 007-K readiness authority
```
