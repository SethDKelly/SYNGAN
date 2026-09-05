---
type: Architecture Contract
title: Phase 004 Consolidated Architecture Contract
status: active
---

# Phase 004 Consolidated Architecture Contract

## Purpose

Freeze the cross-architecture implementation-facing contract established by Phase 004 before SYNGAN enters implementation planning.

This document consolidates the invariant architecture obligations established by 004-A through 004-I. It does not replace the detailed architecture authorities, redefine accepted concept ownership, select final implementation technologies, or turn architectural mechanisms into new domain concepts.

## Governing authority

This contract remains downstream of:

- [Design Authority](../authority/index.md);
- [Accepted Concepts](../concepts/index.md);
- [Accepted Synchronizations](../synchronizations/index.md);
- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md).

Detailed architecture authority remains in:

1. [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md)
2. [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md)
3. [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md)
4. [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
5. [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md)
6. [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
7. [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](evaluation-evidence-provenance-reproducibility-historical-query.md)
8. [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
9. [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](deployment-scalability-observability-portability-compatibility-platform-integration.md)

Decision rationale remains under [Architecture Decision Records](../decisions/index.md), ADR-0001 through ADR-0008.

## Phase 004 exit verdict

The Phase 004 cross-architecture audit finds no contradiction requiring concept, synchronization, experience, or architecture redesign before implementation planning.

The accepted semantic baseline remains:

- eleven concepts;
- fifteen synchronization rules;
- no new standalone domain concept introduced by architecture;
- no new synchronization ID required by architecture.

Phase 004 therefore closes with the architecture contract below as the implementation-planning baseline.

## End-to-end architecture model

The integrated architecture can be read as one authority-preserving path:

```text
editable specification / contextual readiness
                    ↓
semantic commitment
exact immutable material bindings
                    ↓
durable activity identity + commitment snapshot
                    ↓
dependency / platform / security capability resolution
                    ↓
Execution
one stable operational identity
                    ↓
Attempt
immutable invocation + current epoch/fence + scoped capabilities
                    ↓
runtime adapter
Spark-native / distributed model runtime / compatible external runtime
                    ↓
non-final physical state
checkpoint / learned-state candidate / output candidate / diagnostics
                    ↓
seal / integrity / exact-subject binding
                    ↓
owner-side semantic validation
                    ↓
Learned State / completed output / Evidence
                    ↓
typed Provenance + exact historical references
                    ↓
historical query / comparison / reproducibility assessment
```

Security, current authorization, disclosure, deployment capability, observability, and retention operate across this path without replacing semantic ownership.

## Authority and dependency direction

The implementation MUST preserve the authority order:

```text
authority
  ↓
concepts / synchronizations
  ↓
experience
  ↓
architecture
  ↓
implementation plan
  ↓
code / deployment
```

Implementation modules MAY combine responsibilities for efficiency, but they MUST NOT reverse this authority direction.

Dependencies flow inward toward stable semantic/control contracts:

```text
composition/bootstrap
        ↓
adapters/integrations
        ↓
ports/extension contracts
        ↓
application coordination
        ↓
semantic/control contracts
```

Platform, storage, runtime, security, lineage, and observability adapters depend on SYNGAN contracts. The portable semantic/control core does not depend on their concrete SDKs or lifecycle models.

## Canonical ownership matrix

| Concern | Canonical owner / authority | Architectural representation consequence |
|---|---|---|
| semantic interpretation | Data Meaning | immutable/revisioned authority reference |
| reusable synthesis behavior | Synthesis Strategy | semantic revision distinct from implementation binding |
| derivation activity | Learning | committed activity resource |
| reusable learned result | Learned State | logical result identity distinct from payload/runtime object |
| requested synthetic outcome | Generation | committed activity + one possible promoted output |
| reusable validity rule | Constraint | revisioned authority reference |
| evaluative question | Evaluation Criterion | exact revision bound by Evaluation |
| examination | Evaluation | committed activity + method/runtime result validation |
| durable finding | Evidence | immutable finding + separately versioned applicability |
| operational realization | Execution | one logical Execution with subordinate Attempts |
| historical relationships | Provenance | typed stable-reference assertions |
| reproduction meaning | Reproducibility Contract | derived current assessment, not master state |
| release/use authorization | external governance | never inferred from Generation/Evidence completion |

Architectural mechanisms such as handles, manifests, snapshots, checkpoints, Attempt epochs, capability descriptors, authorization decisions, query projections, compatibility matrices, platforms, and telemetry remain non-concept implementation structures.

## Identity and version model

Implementation MUST keep the following axes distinguishable where material:

1. stable logical resource identity;
2. immutable semantic revision identity for revisioned authorities;
3. immutable commitment-snapshot identity for committed activities;
4. mutable lifecycle/current-state version or concurrency token;
5. persistence/wire representation schema version;
6. Strategy/method implementation-binding revision;
7. extension/SPI version;
8. Learned State representation/codec version;
9. Attempt epoch/fencing generation;
10. candidate/manifest generation or sealed-snapshot identity;
11. checkpoint representation identity/version;
12. platform/runtime/dependency versions relevant to compatibility/reproducibility.

A single generic `version` field MUST NOT silently carry several of these meanings.

Mutable aliases, paths, table names, model tags, URLs, Spark job IDs, Databricks run IDs, Python object identity, and process-local handles are not sufficient durable semantic identity when referenced state can change materially.

## Public resource contract

The canonical public representation remains:

```text
editable specification
        ↓
contextual readiness result
        ↓
committed typed activity handle
        ↓
Execution / Attempt inspection
        ↓
promoted typed result handle(s)
        ↓
explicit distributed payload access
```

Required consequences:

- handles resolve canonical state; they do not embody or duplicate it;
- handles remain useful after client/process/cluster turnover;
- handles identify resources but are not bearer credentials;
- candidate output, checkpoint, diagnostics, and runtime method results remain type-distinct from promoted results;
- convenience `fit`/`generate`/`evaluate` flows may exist but cannot make the authoritative activity/result/history inaccessible;
- a DataFrame, model object, scalar score, platform run, generic `Result`, or process-local Future cannot be the only canonical result representation;
- status remains typed by owner/context rather than collapsed into one universal enum.

## Control-plane and distributed-data-plane contract

The bounded control plane owns/references:

- identities/revisions/commitments;
- lifecycle/current state;
- Execution/Attempt summaries;
- result identities;
- Evidence findings/summaries;
- typed Provenance;
- dependency/security/runtime/platform references;
- bounded query/index state.

Potentially large data-plane material remains distributed:

- source rows;
- candidate/completed output rows;
- Learned State components;
- checkpoints;
- Evaluation diagnostics;
- distributed manifest/index components;
- large runtime intermediates.

Ordinary enterprise workflows MUST NOT require full source/output/Learned-State/diagnostic/telemetry collection to the driver merely to coordinate, inspect, authorize, promote, explain, or reproduce work.

Physical durability in the data plane never establishes semantic authority by itself.

## Source and distributed representation contract

Committed source-dependent work binds an exact historical data state and a stable read boundary.

A Spark DataFrame, table alias, path, query, or catalog name may be a source selector/access object, but must resolve to an immutable/versioned source reference or be snapshotted/materialized strongly enough for the required historical contract.

No universal full-corpus hash is required. Provider-native immutable versions, distributed manifests, snapshots, fingerprints, or other mechanisms may comply when their declared guarantees are sufficient.

One logical source/output/Learned State may have many distributed physical components.

Physical layout, partition order, file order, and incidental execution order do not become semantic identity unless explicitly part of the committed contract.

## Semantic commitment contract

Learning, Generation, and Evaluation commitment freezes the material semantic inputs of that activity occurrence.

A material post-commit change to source, Strategy/configuration, Data Meaning, Constraint handling, Learned State/direct-generation basis, Generation Conditions/quantity/scope, Evaluation Criterion/method/subject/reference/coverage, dependency identity, or committed network/egress posture is not an ordinary retry or in-place edit.

It requires a new distinguishable domain commitment where canonical semantics require one.

Persisted drafts do not fabricate committed historical activity identities.

## Runtime extension contract

Semantic Strategy/method authority remains separate from executable implementation binding.

An implementation binding may narrow supported capabilities or add implementation-specific limitations, but cannot silently broaden or redefine the bound semantic contract.

Each Attempt executes an immutable invocation bound to exact committed inputs, implementation/runtime/dependency identity, security posture, and write boundaries.

Runtime adapters may execute computation and write non-final material through supplied ports, but cannot directly:

- complete Learning/Generation/Evaluation semantically;
- establish Learned State authority;
- promote completed output;
- establish Evidence without owner-side Evaluation validation;
- rewrite committed semantics;
- authorize network/egress;
- create canonical Provenance arbitrarily.

Direct-generation Strategies remain first-class and do not fabricate Learning/Learned State.

## Execution, retry, and recovery contract

One committed domain activity may have one stable logical Execution spanning many Attempts/platform jobs/processes.

Physical execution is at-least-once where necessary; canonical side effects are protected by fencing, operation-scoped idempotency, and reconciliation.

Required rules:

- write-capable Attempts use supersedable ordered epochs/fencing generations or an equivalent strong mechanism;
- lease/liveness expiry does not substitute for stale-writer fencing;
- scheduler retry identity does not become SYNGAN Attempt authority;
- idempotency scope is specific to the protected operation/semantic target;
- unknown/indeterminate side-effect state remains explicit until reconciled or safely fenced;
- external side effects that cannot be fenced, deduplicated, or queried may block automatic retry;
- automatic retry has no authority shortcut around semantic, dependency, authorization, network, egress, or cancellation checks;
- cancellation is durable intent followed by reconciled operational outcome;
- late platform success cannot regain superseded framework mutation authority.

The invariant remains:

> **single semantic authority, not exactly-once physical execution.**

## Checkpoint and non-final state contract

A checkpoint is an immutable recovery snapshot only after its own closure/integrity requirements are established.

Checkpoint existence does not imply:

- successful Attempt;
- resume eligibility;
- Learned State;
- completed output;
- Evidence.

Resume compatibility is contextual to the exact committed activity, implementation/runtime/state codec/dependencies, represented progress, and relevant security/availability state.

Retry from start, resume from checkpoint, reconcile first, and cannot continue the same Execution remain distinct outcomes.

## Learning result contract

Learning runtime may produce distributed candidate learned-state material and checkpoints.

Only Learning owner-side semantic validation may establish the one primary logical Learned State.

Learned State identity remains distinct from:

- checkpoint identity;
- one file/path;
- PyTorch module/state dict;
- Spark ML model object;
- currently loaded runtime state.

Representation conversion may preserve Learned State identity only when an explicit equivalence/integrity contract establishes semantic preservation. Fine-tuning/adaptation that materially changes synthesis behavior requires distinguishable learned history through Learning semantics.

## Generation materialization and promotion contract

Generation writes into an unpromoted candidate boundary.

The accepted physical/semantic sequence is:

```text
open candidate materialization
        ↓
distributed writes under current Attempt authority
        ↓
immutable sealed candidate snapshot
        ↓
Evaluation/Evidence bound to that exact sealed candidate
        ↓
Generation completion review
        ↓
idempotent semantic promotion
        ↓
one authoritative logical completed output
```

Sealing proves an immutable-enough physical subject; it does not prove Generation completion.

Promotion may be metadata-only when the storage provider guarantees sufficient immutable/isolation semantics. Copying the whole dataset is not required merely to establish finality.

At most one authoritative completed logical output may be established for one successful Generation. Promotion retries for the same candidate resolve idempotently; a different candidate after successful promotion conflicts rather than creating a second successful output.

Evidence against one sealed candidate does not automatically apply to another candidate produced by retry/recovery.

## Evaluation and Evidence contract

Evaluation runtime output is non-final until owner-side semantic validation verifies the exact Criterion, subject/reference, method/configuration, scope/coverage, assumptions, uncertainty, approximation, dependencies, and supported claim strength.

One Evaluation may establish zero or more independently interpretable Evidence resources.

Evidence establishment is idempotent per logical finding role/slot and exact Evaluation context so runtime retries do not manufacture duplicate findings.

Evidence stores immutable historical finding semantics plus separately conflict-versioned current applicability.

Evidence claim strength cannot exceed what the producing Evaluation actually supports.

Large diagnostics remain separately referenced data-plane material.

Generation completion retains the exact candidate/requirement/Criterion/Evidence basis actually used at promotion. Later Evidence may relate to the output but does not enter that historical promotion basis retroactively.

Evaluation success, favorable Evidence, Generation completion, privacy assurance, and external release/use approval remain distinct.

## Provenance and historical-query contract

Canonical Provenance is a typed stable-reference assertion layer. It records material historical relationships without becoming a copied metadata warehouse or master state graph.

Required rules:

- material relationship meaning remains typed;
- Provenance writes are idempotent with the originating transition/role;
- required Provenance remains recoverably consistent with transitions whose semantics require traceability;
- Provenance correction is append/supersede/invalidate rather than destructive rewrite;
- correcting a Provenance assertion does not rewrite another concept's state;
- external lineage/catalog observations do not automatically become canonical Provenance.

Historical explain/search/compare/adjacency structures are derived read projections. They may be eventually consistent and rebuildable; they do not become canonical write authority.

Historical comparison may report structural differences but cannot infer causality, quality, or superiority without Evaluation/Evidence.

## Reproducibility contract

Reproducibility remains a current qualified assessment assembled for one exact target from canonical historical facts.

The assessment preserves:

- target;
- preserved conditions;
- equivalence rule/class;
- exact semantic/revision identities;
- source/result representation identity;
- implementation/runtime/dependency identity;
- randomness/nondeterminism;
- sampling/approximation/coverage;
- material recovery facts when behavior-affecting;
- current dependency/security/platform availability where relevant.

Accepted classes remain exact deterministic, semantic, statistical, bounded/approximate, comparative, and not reproducible/insufficient context.

The supported class cannot exceed the weakest unresolved material identity, dependency, nondeterminism, or equivalence boundary.

A seed does not establish exact determinism. Re-execution does not establish reproduction. Reproduction readiness does not establish successful reproduction.

## Dependency, offline/no-egress, and security contract

Dependency requirement, availability, exact identity/integrity, semantic/runtime compatibility, trust/approval, current authorization, network capability, and egress behavior remain separate facts.

Dependency/package/model acquisition is explicit provisioning. Committed runtime code does not hide downloads, package installation, model-hub access, remote fallback, telemetry, or dependency substitution.

Supported core structured/tabular workflows remain deployable without required outbound network after approved local provisioning.

Network connectivity and sensitive-data egress remain separately authorized.

Current authorization is action/resource/context-specific. It can change after commitment without rewriting historical semantics.

Durable handles are not bearer credentials. Attempt runtimes receive only scoped capabilities no broader than:

```text
committed semantic requirement
      ∩ current authorization
      ∩ deployment capability
```

Secret values remain operational credentials and are excluded from canonical commitments, Evidence, Provenance, manifests, checkpoints, handles, and ordinary logs.

Source, Learned State, candidate/output, diagnostics, Evidence, Provenance, history/query, and export actions may be independently protected.

Redaction/withholding is an actor-specific view transformation and must preserve truthful distinctions among absent, unknown/indeterminate, unavailable, withheld, redacted summary, and invalid where disclosure permits. A restricted view must not falsify canonical history, while disclosure logic must also avoid leaking the existence/count/shape of relationships when existence itself is sensitive.

Derived query/index/comparison/reproducibility views remain inside the authorization boundary.

Security audit remains distinct from Provenance.

## Deployment and platform contract

The portable semantic/application/control core binds to explicit technical capability contracts rather than platform brand names.

A platform/environment adapter declares relevant guarantees such as:

- immutable/versioned reads;
- distributed read/write;
- candidate isolation;
- conditional mutation/fencing;
- checkpoint representation;
- workload launch/correlation;
- workload identity;
- storage authorization;
- secret delegation;
- network/egress enforcement;
- local dependency resolution;
- accelerator/runtime capability;
- historical version resolution;
- observability/query integration.

Capability negotiation may conclude direct support, semantics-preserving fallback, acceptable declared limitation, incompatibility, or indeterminacy.

A missing guarantee cannot be papered over by weakening semantics silently.

Databricks remains an important managed-platform adapter target, not package/semantic identity. Generic/self-managed Spark and private/offline deployments remain valid when they provide the required guarantees.

Platform-native jobs, retries, lineage, model metadata, table IDs, catalog objects, and observability references remain external integrations rather than replacements for SYNGAN Execution, Attempt, Learned State, Output, Evidence, Provenance, or semantic completion.

## Observability contract

At least three logical information lanes remain distinct:

1. canonical semantic/operational history;
2. platform/runtime logs, metrics, traces and telemetry;
3. security audit.

Correlation across lanes is encouraged where authorized, but no lane becomes another's authority.

Logs/metrics/traces do not establish semantic completion. Trace IDs do not become resource identities. Progress remains operational/method-specific and does not become an invented universal semantic percentage.

Supported offline/no-egress deployments cannot require external telemetry for ordinary operation.

## Compatibility and migration contract

Compatibility is multi-axis rather than one package-level Boolean.

Implementation planning must account for, where relevant:

- public API/package version;
- control/persistence/wire schema versions;
- semantic revisions;
- implementation-binding version;
- SPI version;
- Learned State codec;
- manifest/checkpoint schema;
- Provenance schema;
- Spark/Python/runtime/platform version;
- storage/catalog provider;
- external dependencies/services.

Rolling/mixed-version deployments require explicit protocol/schema compatibility. Components must not write representations that peers cannot safely interpret.

Schema migration preserves stable resource identity, immutable historical bindings, lifecycle meaning, correction/supersession state, and disclosure semantics.

## Retention and cleanup contract

Retention policies may differ across canonical control state, large payloads, candidates/checkpoints/scratch, Evidence diagnostics, query projections, platform telemetry, and security audit.

Cleanup cannot silently destroy state still required for:

- current Attempt authority;
- sealed/promoted representations;
- valid checkpoint recovery;
- retained Evidence interpretation;
- historical investigation;
- declared reproducibility guarantees.

When payload retention expires but identity/history remains retained, the result remains `identity known / payload unavailable` rather than fabricated absence.

## Enterprise-scale and concurrency contract

Scale is multidimensional. Implementation and benchmarks must disclose material limits across row/byte volume, width, cardinality, skew, partition count, model/Learned-State size, accelerator/worker memory, shuffle/data movement, Evaluation coverage cost, concurrency, and external dependency throughput.

An implementation advertised for enterprise-scale use must disclose any hidden single-node or source-size-proportional stage.

Concurrent coordinators/clients/runtimes may operate safely only through canonical state-version, idempotency, fencing, authorization, and projection rules. Global mutable process-local state and last-writer-wins are incompatible with the accepted architecture.

## Cross-architecture invariants

The following invariants are frozen for implementation planning:

1. Upstream semantic/experience authority cannot be redefined by architecture or implementation convenience.
2. Each substantive state remains owned by one canonical semantic authority.
3. Architecture mechanisms do not become domain concepts merely because they have persistent records or public representations.
4. Stable resource identity remains distinct from location, alias, platform ID, and runtime object identity.
5. Semantic revision, commitment snapshot, lifecycle state version, schema version, implementation version, Attempt epoch, and physical snapshot identity remain distinguishable.
6. Committed semantic bindings are immutable historical facts.
7. Mutable aliases/latest revisions never replace exact historical bindings silently.
8. Public handles resolve canonical resources and are not canonical payload copies or bearer credentials.
9. Readiness/compatibility remains contextual and does not become globally mutable authority.
10. Control-plane state remains bounded and references large distributed payloads.
11. Ordinary enterprise workflows do not require full driver-local source/output/Learned-State/diagnostic/log materialization.
12. Spark-native means distributed Spark-scale data boundaries, not universal Spark ML implementation.
13. The core remains model-neutral and supports both Learning-based and direct-generation Strategies.
14. Strategy/method semantic authority remains separate from executable implementation binding.
15. Runtime invocation is immutable per Attempt.
16. Runtime/platform adapters cannot directly establish semantic result authority.
17. One committed activity has one logical Execution even across multiple Attempts/platform realizations.
18. Retry/resume preserves committed semantics; material semantic change creates new domain work.
19. Attempt fencing and liveness/leases remain separate concerns.
20. Duplicate physical work is allowed; duplicate authoritative semantic results are not.
21. Operation-scoped idempotency does not bypass stale-writer fencing.
22. Unknown external/platform side effects remain explicit until safely reconciled/fenced.
23. Checkpoint/intermediate learned material remains distinct from Learned State.
24. Candidate output remains distinct from completed output.
25. Evaluation runtime/diagnostic material remains distinct from Evidence.
26. Sealed candidate identity is the exact subject for completion Evaluation when Generation requires it.
27. Semantic promotion remains an owner-authorized transition and may reuse physical bytes without copying.
28. Evaluation success and Evidence favorability remain separate.
29. Evidence claim strength remains bounded by method, scope, coverage, assumptions, uncertainty, and approximation.
30. Generation promotion retains the exact Evidence/completion basis used historically.
31. Provenance remains typed relationship authority with high fan-in and low authority fan-out.
32. Provenance references canonical owners rather than copying their full payload/state.
33. Provenance corrections preserve auditability and do not rewrite another owner.
34. Historical projections/indexes are derived and non-authoritative.
35. Historical differences do not imply causality or quality.
36. Reproducibility is a qualified target-specific assessment, not a permanent Boolean.
37. Re-execution, seed presence, or readiness does not establish successful reproduction.
38. Dependency availability, identity/integrity, compatibility, trust, authorization, network, and egress remain separate.
39. Missing dependencies do not trigger hidden acquisition, substitution, network, or remote fallback.
40. Current authorization cannot broaden committed semantics and later revocation cannot rewrite history.
41. Attempt runtime authority is bounded by semantic requirement, current authorization, and deployment capability.
42. Secret bearer values remain outside canonical semantic/history state.
43. Redaction/withholding is a view concern; it cannot falsify history or leak protected graph/existence facts.
44. Security audit, platform telemetry, and canonical semantic/operational history remain distinct.
45. Platform adapters add capabilities without becoming semantic authority.
46. Platform capability gaps require explicit fallback, limitation, incompatibility, or indeterminacy rather than silent weakening.
47. Databricks is a first-class managed target but not SYNGAN package identity or semantic authority.
48. Generic/self-managed Spark and private/offline deployment remain legitimate targets when required guarantees are supplied.
49. Compatibility is multi-axis and rolling upgrades require explicit protocol/schema compatibility.
50. Retention/cleanup cannot silently erase still-authoritative or historically required state.
51. Convenience facades, generic registries, metadata stores, managers, sessions, engines, graphs, and platform objects cannot become god-owners by implementation accident.
52. Human/programmatic interfaces must preserve the same material semantic distinctions even when syntax differs.

## Cross-architecture audit findings

### No authority inversion found

No accepted architecture requires a platform/runtime/security/query adapter to own or redefine an accepted concept.

### No lifecycle contradiction found

Preparation/readiness, semantic commitment, operational realization, non-final physical state, semantic result establishment, and historical inspection remain distinguishable across Learning, Generation, and Evaluation.

### No identity/version contradiction found

The version axes introduced in 004-C through 004-I are complementary rather than competing. Implementation planning must preserve typed fields/contracts rather than collapsing them.

### No promotion/recovery contradiction found

004-D promotion and 004-F retry/fencing compose correctly: duplicate physical work may occur, while candidate sealing and semantic promotion remain fenced/idempotent and stale Attempts cannot regain authority.

### No Evidence/Provenance contradiction found

004-G preserves Evidence as finding authority and Provenance as relationship authority. Neither becomes approval authority or a copied metadata warehouse.

### No security/history contradiction found

004-H permits current authorization/redaction to restrict actions and views while preserving canonical historical truth. Derived query projections remain inside the same disclosure boundary.

### No portability contradiction found

004-I preserves platform specialization through capability adapters without making Databricks or another platform semantic authority. Portability is guarantee-preserving rather than lowest-common-denominator degradation.

### No scale contradiction found

The architecture consistently keeps bulk data and detailed diagnostics/telemetry out of bounded control-plane requirements and does not require ordinary full-corpus driver materialization.

## Deferred decisions that do not block Phase 004 exit

Implementation planning still needs to select or plan, without reopening semantics:

- Python package/module/source topology;
- exact public class/function names;
- persistence database/transaction implementation;
- ID encoding;
- serialization/wire schemas;
- Spark table/file/catalog providers;
- source fingerprint/snapshot mechanisms;
- manifest serialization/index format;
- candidate/checkpoint physical layouts;
- scheduler/orchestrator integration;
- Attempt fencing/CAS/lease mechanics;
- Strategy/plugin discovery mechanism;
- PyTorch/distributed runtime technology;
- Learned State codecs;
- provenance/query physical persistence;
- authentication/IAM/policy-engine integrations;
- secret manager/KMS/encryption controls;
- network/egress enforcement mechanisms;
- observability stack;
- Databricks-specific integration details;
- CI/CD/deployment topology;
- retention defaults;
- benchmark methodology and support matrices.

The following domain topics remain intentionally outside the current implementation baseline unless separately reopened through upstream design authority:

- relational/multi-table synthesis concepts;
- mechanism-specific privacy concepts/guarantees;
- external use/release governance authority;
- additional Strategy/Evaluation method catalog breadth.

## No-new-concept audit

Phase 004 architecture does not justify adding standalone concepts for:

- Resource / Handle;
- Snapshot / Manifest / Artifact;
- Candidate / Promotion;
- Plugin / Runtime / Adapter;
- Attempt / Checkpoint / Recovery;
- Evidence Set / Finding Slot;
- History / Lineage Graph / Historical View;
- Reproducibility Assessment;
- Dependency / Trust / Security / Authorization / Egress;
- Deployment / Platform / Capability / Compatibility;
- Telemetry / Metric / Trace;
- Registry / Session / Context / Metadata.

These remain architecture mechanisms, subordinate operational state, derived views, external authority, or compatibility vocabulary beneath the accepted concept model.

## ADR consolidation

The active Phase 004 ADR set is coherent and non-overlapping:

- ADR-0001 — typed resource/handle public API;
- ADR-0002 — immutable semantic snapshots and versioned lifecycle state;
- ADR-0003 — sealed manifest-gated output promotion;
- ADR-0004 — semantic extension/runtime-binding separation;
- ADR-0005 — Attempt-epoch fencing and recoverable at-least-once execution;
- ADR-0006 — typed canonical Provenance and derived historical projections;
- ADR-0007 — explicit dependency resolution and scoped capability security;
- ADR-0008 — portable core and capability-negotiated platform adapters.

No ADR is superseded by the Phase 004 exit audit.

## Implementation-planning handoff

Phase 005 should map this contract through a traceable implementation chain:

```text
upstream concept / experience invariant
        ↓
Phase 004 architecture contract
        ↓
module / port / adapter / persisted representation
        ↓
implementation slice
        ↓
verification / architecture fitness test
        ↓
acceptance evidence
```

Implementation planning MUST NOT begin from a preferred package tree or technology and then retrofit semantic ownership afterward.

The first implementation-planning group should establish implementation authority, delivery governance, repository/toolchain constraints, and how architecture conformance will be enforced before implementation slices are decomposed.

## Exit condition

Phase 004 is complete when:

- this consolidated architecture contract is active;
- 004-A through 004-I remain canonical and non-conflicting;
- ADR-0001 through ADR-0008 remain active and linked;
- the Phase 004 exit review records no blocking redesign;
- repository navigation advances to Phase 005 implementation planning.
