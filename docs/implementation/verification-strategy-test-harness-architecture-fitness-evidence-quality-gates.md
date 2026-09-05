---
type: Implementation Authority
title: Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates
status: active
---

# Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates

## Purpose

Define the implementation-verification architecture SYNGAN must use before source/package topology and concrete implementation slices are selected.

This document is the canonical Phase 005-B implementation authority for:

- verification layers and test profiles;
- architecture-fitness functions;
- contract/conformance testing;
- deterministic, stochastic, distributed, failure-injection, security, migration and compatibility verification;
- evidence-fixture design;
- CI/review quality-gate semantics;
- test evidence and retention;
- flaky-test and waiver handling;
- the verification requirements 005-C must support when it chooses package/source topology and concrete tooling.

It intentionally does **not** yet select the final Python version, test runner, property-testing library, formatter/linter/type checker, dependency manager, CI vendor, container runtime, Spark distribution, database, scheduler, or exact physical `tests/` directory topology.

## Governing authority

Verification is downstream of:

- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](implementation-authority-delivery-governance-toolchain-repository-enforcement.md);
- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md);
- the accepted concepts and synchronizations relevant to the tested behavior.

The governing verification rule is:

> **A test oracle comes from accepted authority, not from current code, platform behavior, or previously captured output. Verification must prove that the implementation preserves the contract, not merely that the implementation is self-consistent.**

## Verification model

SYNGAN SHALL use a layered verification model in which fast deterministic contract checks protect core invariants continuously, while heavier distributed/platform/statistical verification runs in explicitly scoped profiles.

Conceptually:

```text
accepted authority
      ↓
verification obligation
      ↓
small deterministic oracle where possible
      ↓
component / contract / architecture-fitness verification
      ↓
distributed / failure / security / migration / platform verification
      ↓
scale / compatibility / statistical evidence
      ↓
acceptance evidence for the implementation slice
```

No single test class or environment is sufficient for every guarantee.

## Verification layers

The following are logical verification layers. 005-C may map them into directories/packages/tasks without changing their meaning.

### V0 — repository and authority conformance

Verifies repository-declared governance and structural correctness that can be checked without executing substantive domain behavior.

Examples:

- required canonical documentation/index references remain valid;
- implementation decisions are promoted to the correct authority surface;
- prohibited secret-bearing files/patterns are absent where tooling supports detection;
- required project metadata/configuration exists once introduced;
- generated artifacts or vendored material follow repository policy;
- public/persisted contract changes include required migration/compatibility evidence metadata.

V0 must not pretend that documentation consistency proves runtime correctness.

### V1 — deterministic semantic/control unit verification

Tests bounded logic whose oracle can be established without external services or distributed execution.

Examples include:

- typed identity/reference behavior;
- lifecycle-transition validation;
- immutable commitment semantics;
- readiness/result-state distinctions;
- Evidence claim-strength bounds;
- Provenance relationship typing/correction rules;
- disclosure-state distinctions;
- compatibility-decision combination rules;
- idempotency-key construction rules where defined;
- checkpoint/candidate/promoted-result type separation.

These tests SHOULD be fast, hermetic, and deterministic.

### V2 — component and port contract verification

Verifies one implementation component against the port/contract it claims to implement.

Examples:

- control-store persistence behavior;
- source-reference resolver behavior;
- candidate writer/sealer contract;
- Strategy/method implementation binding behavior;
- Execution launcher correlation/reconciliation contract;
- authorization/secret/dependency resolver contract;
- historical query projection behavior.

A fake/in-memory implementation MAY be used to exercise consumers, but every production adapter must also run a reusable conformance suite against the same contract.

### V3 — architecture fitness verification

Protects Phase 004 architecture properties that can regress even when unit tests still pass.

The implementation MUST support executable checks for properties including:

1. semantic/control layers do not depend on concrete platform/runtime adapters;
2. optional adapters/runtime-network integrations are absent from the supported portable/offline-core dependency closure;
3. raw DataFrame/model/platform objects cannot satisfy canonical resource/result identity contracts accidentally;
4. candidate/checkpoint/diagnostic/runtime-result representations cannot be substituted for promoted Learned State/output/Evidence;
5. committed semantic snapshots are not mutated by current-state update paths;
6. adapter/platform state cannot directly establish semantic completion;
7. Provenance/query projections cannot become canonical owner write dependencies;
8. security audit/telemetry cannot become semantic state dependencies;
9. hidden runtime package/model acquisition or remote fallback is absent from supported core execution paths;
10. enterprise-scale supported paths do not require full driver-local source/output/Learned-State/diagnostic collection;
11. platform capability fallback must preserve the required semantic contract or surface limitation/incompatibility;
12. durable handles remain non-bearing identity references rather than embedded permanent credentials.

Some fitness checks may be static/import-graph checks; others require behavioral contract tests. Tool choice is deferred, but the protected property is not optional.

### V4 — persistence, concurrency and migration verification

Verifies durable-control behavior under storage/concurrency evolution.

Required scenarios include, as applicable:

- stable resource identity survives serialization/schema migration;
- semantic revision, commitment snapshot, lifecycle state version and representation schema version remain distinguishable;
- optimistic concurrency/CAS rejects stale lifecycle writes;
- immutable historical commitments cannot be edited through migration/update APIs;
- migration preserves exact historical references and correction/supersession semantics;
- tombstone/unavailable behavior remains different from absent;
- derived projections can be rebuilt without becoming canonical write authority;
- migration rollback/forward-recovery behavior is defined where supported.

Golden serialized fixtures MAY be used for compatibility tests, but they are versioned compatibility evidence rather than semantic truth independent of authority.

### V5 — Spark/distributed data-boundary verification

Verifies distributed source/output behavior without reducing the contract to local pandas or driver-memory success.

Required scenarios include, as applicable:

- mutable alias/source selector resolves to exact immutable/versioned state or explicit snapshot;
- execution reads the exact source state bound at commitment;
- candidate writes remain distributed;
- candidate sealing freezes the exact subject evaluated;
- Evidence against candidate SC1 cannot be reused for SC2 without explicit equivalence;
- promotion establishes one logical completed output without requiring physical row copying where provider guarantees permit metadata-only promotion;
- distributed output remains resolvable after client/SparkSession turnover;
- physical partition/file ordering does not become semantic identity accidentally;
- compaction/relocation preserves logical identity only through an explicit equivalence contract;
- no ordinary enterprise path requires `collect()`/equivalent full materialization merely for coordination or result access.

Small local Spark fixtures MAY validate contract mechanics quickly; larger/distributed profiles are separately required to detect scale/distribution-specific defects.

### V6 — runtime-extension and Learned-State verification

Verifies Strategy/method runtime boundaries independently of one model family.

Required scenarios include:

- semantic Strategy revision is separate from implementation binding/version;
- implementation binding cannot broaden semantic capability silently;
- immutable Attempt invocation contains the exact bound inputs/dependencies/runtime context;
- runtime adapter cannot mutate committed specifications;
- Learning runtime candidate/checkpoint material does not become Learned State without owner-side promotion;
- loaded PyTorch/Spark/native runtime object does not become Learned State identity;
- direct Generation operates without fabricated Learning/Learned State;
- optional runtime dependencies can be absent without breaking portable-core import/use paths;
- runtime network behavior follows the declared/authorized profile rather than self-enabling.

Every implementation binding SHOULD be tested through a reusable Strategy/method runtime conformance suite plus binding-specific behavior tests.

### V7 — Execution, failure-injection and recovery verification

Recovery properties SHALL be tested as state-machine/failure scenarios rather than only happy-path retries.

Required scenario families include:

- one stable Execution across multiple Attempts;
- stale lifecycle write conflict;
- lease expiry without automatic write authority;
- newer Attempt epoch fences an older writer;
- old process wakes after supersession and its canonical write is rejected;
- duplicate physical computation does not create duplicate semantic output;
- platform submission succeeds but coordinator loses acknowledgement;
- unknown external effect requires reconciliation before unsafe retry;
- checkpoint write interrupted before closure is not resumable checkpoint authority;
- valid checkpoint resumes only when exact compatibility/security/dependency requirements still hold;
- restart-from-beginning and resume are distinguishable;
- cancellation request races with late success/failure;
- late platform success after cancellation/supersession cannot regain canonical mutation authority;
- Evaluation duplicate logical work units are not double-counted after retry;
- semantic promotion and Evidence establishment remain idempotent under repeated requests/crash windows.

Failure injection SHOULD occur at explicit seams such as before/after durable mutation, provider submission, checkpoint commit, candidate seal, Evidence establishment and promotion rather than relying only on random process kills.

### V8 — Evaluation, Evidence, Provenance and reproducibility verification

Required scenario families include:

- successful Evaluation can establish negative or indeterminate Evidence;
- runtime metric/result cannot bypass Evaluation semantic validation;
- Evidence claim strength cannot exceed method/coverage/uncertainty support;
- repeated same logical finding establishment is idempotent;
- conflicting repeated finding content is surfaced as consistency failure;
- immutable Evidence finding remains historically stable while applicability can change;
- Generation promotion records the exact candidate/requirement/Criterion/Evidence basis used;
- later Evidence does not retroactively become the historical promotion basis;
- Provenance records typed stable references rather than copied owner payloads;
- repeated transition recording does not create duplicate canonical assertions;
- Provenance correction supersedes rather than destructively rewrites;
- derived explain/compare/search projection staleness cannot alter canonical history;
- historical comparison reports differences without inventing causal/quality claims;
- reproducibility assessment is bounded by weakest unresolved identity/dependency/nondeterminism/equivalence boundary;
- seed presence or re-execution readiness cannot be treated as successful reproduction.

### V9 — dependency, security, offline/no-egress and disclosure verification

Supported portable-core verification SHOULD deny outbound network by default.

Required scenarios include, as applicable:

- missing dependency does not trigger hidden download/install/model-hub access/remote fallback;
- dependency availability, exact identity/integrity, compatibility, trust and authorization remain distinguishable;
- network permission does not grant data-egress permission;
- current authorization can block retry/access without rewriting historical commitment;
- durable resource-handle possession alone does not authorize payload/action access;
- Attempt receives only scoped capabilities appropriate to exact invocation;
- secret references can be resolved through approved test brokers without persisting secret values in canonical state/logs/fixtures;
- source, Learned State, candidate/output, diagnostics, Evidence, Provenance and query actions can be independently protected;
- `absent`, `unknown`, `unavailable`, `withheld`, `redacted` and `invalid` remain distinguishable when disclosure permits;
- existence/count/graph shape is not leaked through derived query paths where existence is protected;
- security audit remains separate from canonical Provenance;
- supported offline profile executes without public network after explicit local provisioning.

Tests requiring real external network/service access MUST run only in an explicitly named opt-in integration profile and must never be a hidden prerequisite of portable-core verification.

### V10 — platform-adapter and capability-conformance verification

Every supported platform adapter SHOULD run reusable capability/contract suites proving the guarantees it advertises.

Examples:

- exact historical/versioned source read;
- distributed read/write;
- candidate isolation/sealing;
- CAS/fencing semantics;
- checkpoint durability;
- workload submission/correlation/reconciliation;
- workload identity and secret delegation;
- network/egress enforcement where claimed;
- historical-version retention/resolution;
- observability correlation without authority inversion.

A provider-specific test MUST NOT replace a common conformance test with a weaker expectation merely because the provider behaves differently.

When a capability is unavailable, tests should verify the accepted semantics-preserving fallback or explicit incompatibility/limitation result.

### V11 — scale, performance and compatibility verification

Scale/performance verification is evidence against declared envelopes, not a blanket benchmark claim.

Profiles SHOULD vary material dimensions such as:

- row/byte volume;
- width;
- high-cardinality features;
- skew/partition imbalance;
- output volume;
- Learned State size;
- worker/driver/GPU memory;
- shuffle/data movement;
- concurrency;
- Evaluation coverage/cost;
- dependency/service throughput.

Performance results MUST record enough environment/workload context to avoid claims such as `supports 100M rows` without qualification.

Compatibility verification SHOULD exercise supported combinations across the independent version axes defined by Phase 004, using a bounded support matrix rather than a Cartesian-product promise that cannot be maintained.

## Architecture-fitness function catalog

005-C and later implementation slices MUST provide concrete enforcement for the following catalog. The implementation mechanism may evolve, but deleting the protected property requires the relevant authority change.

| Fitness ID | Protected property | Preferred verification character |
|---|---|---|
| AF-01 | dependency direction points inward; core does not import concrete adapters | static/import graph + smoke import |
| AF-02 | portable/offline core dependency closure excludes optional remote/platform runtimes | packaging/import/network-deny tests |
| AF-03 | canonical identities are not raw DataFrame/model/path/platform IDs | type/contract tests |
| AF-04 | non-final material cannot satisfy promoted-result contracts | type + behavioral tests |
| AF-05 | immutable commitments/history cannot be rewritten through ordinary mutation/migration | persistence/contract tests |
| AF-06 | lifecycle stale writes are rejected | concurrency tests |
| AF-07 | stale Attempt writers are fenced | failure/concurrency tests |
| AF-08 | promotion and Evidence establishment are idempotent | crash/retry contract tests |
| AF-09 | runtime/platform success cannot establish semantic completion directly | contract tests |
| AF-10 | Provenance/query projections are not canonical owner dependencies | dependency + persistence tests |
| AF-11 | protected history/query paths honor disclosure/authorization | security conformance tests |
| AF-12 | hidden acquisition/remote fallback/telemetry is absent from supported core | network-deny tests |
| AF-13 | enterprise paths do not require full driver collection | static targeted checks + distributed behavioral tests |
| AF-14 | platform fallback preserves semantics or reports limitation/incompatibility | adapter conformance tests |
| AF-15 | secret bearer values are excluded from canonical records/log fixtures | schema/log/static tests |
| AF-16 | typed status/disclosure contexts remain distinguishable | API/serialization contract tests |
| AF-17 | historical exact references do not silently resolve to latest aliases | persistence/resolution tests |
| AF-18 | required transition/Provenance consistency is recoverable after crash | failure-injection tests |
| AF-19 | duplicate Evaluation work is not double-counted after retry | distributed/recovery tests |
| AF-20 | managed-platform IDs/retries/lineage remain subordinate external references | adapter/API contract tests |

The catalog may gain additional IDs as later implementation plans discover concrete enforcement needs. A new fitness function does not create a new semantic concept.

## Test oracle discipline

### Authority-derived oracles

Assertions should state the contract being protected, directly or through a stable requirement/fitness identifier.

A copied production implementation is not an independent oracle.

Examples of weak verification include:

- serializing an object and asserting it equals itself after round-trip without checking historical/version semantics;
- capturing current implementation output as a golden file and treating that output as correct merely because it was previously produced;
- mocking a persistence adapter so completely that concurrency/fencing semantics are never exercised;
- asserting platform `SUCCESS` maps to domain completion because the adapter currently does so.

### Golden fixtures

Golden files are appropriate for stable public/persisted/wire compatibility representations when deliberate byte/shape compatibility matters.

They are inappropriate as the sole oracle for:

- stochastic synthetic row values;
- distributed physical ordering;
- platform-generated identifiers;
- timestamps;
- nondeterministic optimizer/runtime detail;
- semantic quality claims requiring statistical Evaluation.

Golden updates that alter a public/persisted contract require the appropriate Class 2+ review rather than an automatic snapshot refresh.

## Fixture architecture

Fixtures SHALL be synthetic/non-sensitive unless a separately governed integration environment explicitly authorizes other test data.

### Canonical scenario fixture families

The verification harness should provide reusable scenario builders/fixtures equivalent to:

- revisioned Data Meaning / Strategy / Constraint / Criterion families;
- stable and mutable source selectors with at least two historical source states;
- committed Learning/Generation/Evaluation snapshots;
- direct-generation and Learned-State generation paths;
- open, partial, sealed and alternate Generation candidates;
- usable/restricted/retired Learned State states;
- Execution with ordered Attempts/epochs and stale writer scenarios;
- complete/incomplete/incompatible checkpoints;
- favorable/unfavorable/indeterminate Evidence with varied claim strength;
- typed Provenance chains including correction/supersession;
- dependency resolution states: missing, wrong identity, untrusted, unauthorized, network-required;
- disclosure states: absent/unknown/unavailable/withheld/redacted;
- platform capability descriptors supporting direct, fallback, incompatible and indeterminate outcomes.

Scenario fixtures SHOULD use stable human-readable test IDs independent of production ID encoding so test intent remains clear.

### Data-scale fixture classes

Use several fixture classes rather than committing large production-like datasets to Git:

1. **micro fixtures** — tiny deterministic rows for unit/contract tests;
2. **generated medium fixtures** — reproducibly generated data for local Spark/integration tests;
3. **ephemeral large/scale fixtures** — created in dedicated scale environments, referenced by test manifest, not stored as ordinary repository blobs;
4. **fault/control fixtures** — fake clocks, deterministic randomness, simulated provider responses, fencing/correlation state and failure schedules.

Fixture generation logic should itself be deterministic where deterministic behavior is expected and should record seeds/configuration when randomness is intentional.

### Sensitive-data prohibition

Ordinary repository fixtures MUST NOT contain real production/customer/source records, real secrets, real bearer tokens, or sensitive Learned State payloads.

Security tests use clearly synthetic placeholders and test-scoped credentials supplied by the test environment.

## Determinism and stochastic verification

### Deterministic lane

Identity, lifecycle, promotion cardinality, fencing, authorization decisions, migration behavior and other contract logic SHOULD be deterministically testable.

Time, randomness, provider responses, generated IDs and failure points SHOULD be injectable/controllable where they otherwise make these tests nondeterministic.

### Statistical/stochastic lane

Statistical synthesis/evaluation behavior cannot always assert exact row equality.

Such tests must define before execution:

- hypothesis/property being tested;
- dataset/fixture profile;
- sample/replication count where needed;
- seed handling;
- acceptance threshold or confidence rule;
- allowed stochastic variability;
- failure interpretation.

A stochastic test MUST NOT use unbounded `retry until pass` as its reliability mechanism.

A failed statistical threshold is evidence to investigate; rerunning until green without recording the failure invalidates the gate.

## Mock, fake and emulator policy

Fakes/mocks are useful for isolating coordination logic but may not erase the property under test.

Examples:

- use a fake scheduler to test application coordination, but run the real scheduler/platform adapter through the common launcher conformance suite;
- use an in-memory repository to test lifecycle consumers, but test CAS/migration/fencing semantics against the production persistence implementation;
- mock a policy decision response for unit tests, but run authorization/redaction conformance against the selected policy adapter;
- fake Spark source handles for pure reference logic, but run exact snapshot/read binding against real Spark/provider integration.

Adapter conformance suites SHOULD be reusable so every concrete adapter inherits the same minimum contract.

## Network and external-service test policy

### Default-deny core verification

The portable/core test profile SHOULD run with outbound network unavailable or actively denied where the environment can enforce it.

Unexpected network attempts should fail tests rather than be silently ignored.

### Explicit external integration profile

Tests that require a managed service, remote API, package/artifact repository, Databricks workspace or other networked dependency must be explicitly opt-in/profiled and document:

- service/dependency required;
- credential source;
- data classification permitted;
- network/egress behavior;
- cleanup/isolation behavior;
- whether the test is a merge gate, scheduled gate or release/support certification gate.

No external-integration test may use real production data merely for convenience.

## Quality-gate model

Quality gates are grouped by cadence/cost, not by importance.

### Gate Q0 — pre-commit/local fast feedback

Expected to include, once tooling exists:

- repository/config sanity;
- deterministic unit tests for touched behavior;
- selected fast architecture-fitness checks;
- static/lint/type checks selected by 005-C;
- no-network smoke/import verification for core where practical.

These commands should be fast enough for routine local use.

### Gate Q1 — required pull-request gate

Every material PR should pass a reproducible required profile including:

- V0 repository/authority checks;
- V1 deterministic semantic/control tests;
- relevant V2 component/contract suites;
- fast/essential V3 architecture-fitness functions;
- affected migration/serialization contract tests;
- portable-core no-hidden-network checks;
- test/fixture hygiene and secret/sensitive-data checks where tooling supports them.

If a PR changes Spark/runtime/recovery/security behavior, the relevant bounded integration/conformance suites become part of Q1 even if they are not run for unrelated documentation-only changes.

### Gate Q2 — integration/distributed gate

Runs environment-dependent suites such as:

- Spark/local-distributed data boundary integration;
- persistence/CAS/migration integration;
- runtime binding conformance;
- deterministic failure injection/recovery;
- security/dependency adapter conformance;
- projection/history integration;
- offline install/runtime profile.

Q2 may run on every relevant PR or as a required merge queue depending on eventual CI cost, but a slice cannot be accepted without the required Q2 evidence when its contract depends on these behaviors.

### Gate Q3 — scheduled compatibility/resilience gate

Runs heavier recurring coverage such as:

- supported Python/Spark/runtime/platform version matrix slices;
- multiple storage/provider adapters;
- prolonged failure/reconciliation scenarios;
- repeated stochastic/statistical tests;
- packaging/private/offline installation matrices;
- broader adapter capability conformance.

A scheduled gate failure must be triaged as a product compatibility regression, test defect, or support-matrix issue; it cannot remain indefinitely red without affecting support claims.

### Gate Q4 — release/support certification gate

Before publishing or claiming a supported environment/scale profile, execute the applicable:

- package/install/build verification;
- migration compatibility checks;
- full supported conformance matrix subset;
- security/offline/no-egress certification profile;
- scale/performance methodology;
- reproducibility/evidence fixtures relevant to the release;
- release artifact integrity/provenance checks defined by later phases.

A release gate certifies only the explicitly tested support matrix and workload envelope.

## Change-aware gate selection

CI MAY use path/impact selection to avoid running every expensive suite for every edit, but selection must be conservative and reviewable.

A change to shared identity, lifecycle, serialization, persistence, capability, security, runtime invocation or public contracts should expand the affected suite rather than rely solely on narrow file paths.

Skipping a gate because no test files changed is not sufficient justification.

005-C should design module boundaries/ownership metadata so later gate-selection logic can map implementation changes to affected contracts reliably.

## Failure, flakiness and quarantine policy

### No silent retry-to-green

Automatic infrastructure retry MAY rerun a job that failed before tests executed, but test assertion failures must remain visible.

A flaky test may be repeated for diagnosis, but passing on retry does not erase the initial failure from evidence.

### Quarantine

A test may be quarantined only when:

- the defect/flakiness is documented;
- the protected requirement and risk are known;
- an owner/follow-up exists;
- quarantine has an expiry/review condition;
- the quarantine does not make a mandatory Phase 004 invariant effectively unenforced.

If the quarantined test is the only enforcement for a non-waivable invariant, the affected feature/support claim must be considered blocked until another valid check exists.

### Test defect versus product defect

When a test conflicts with canonical authority, update the test.

When implementation conflicts with canonical authority, update the implementation unless an explicit upstream change is approved.

Do not weaken an assertion merely because production code currently fails it.

## Waiver governance

Waivers are exceptional delivery controls, not alternate authority.

A waiver record must state:

- exact gate/check being waived;
- reason and evidence;
- implementation slice/change;
- risk/affected invariant;
- owner;
- expiry or next review point;
- compensating control where applicable;
- follow-up issue/backlog location.

Waivers cannot authorize:

- semantic/experience contradiction;
- known historical corruption;
- hidden egress/acquisition;
- deliberate stale-writer acceptance;
- duplicate semantic promotion;
- secret disclosure;
- falsified Evidence/Provenance.

Such cases require actual design/implementation correction rather than a quality-gate exception.

## Acceptance evidence format

A completed implementation slice should retain a bounded evidence record equivalent to:

```text
slice / change identifier
upstream authority references
implementation plan/version
source/config/migration changes
verification profiles executed
fitness-function results
fixture/scenario versions
environment/runtime/platform versions when material
pass/fail/waiver outcomes
migration/compatibility result
security/network/offline result
scale/performance result where applicable
known limitations / deferred items
CI/run/artifact references where available
```

The evidence record is delivery evidence, not Evidence in the SYNGAN domain-concept sense.

005-C/later phases may choose a machine-readable manifest format. The name and schema must avoid confusing delivery evidence with the canonical `Evidence` concept.

## Evidence retention

Fast test logs need not be retained forever, but enough evidence should remain to support:

- why a material slice was accepted;
- which required gates ran;
- which compatibility/platform profile was certified;
- whether a waiver existed;
- migration/release support decisions.

Large transient logs/artifacts should be referenced through CI/platform artifact retention rather than copied into canonical documentation.

Canonical docs should record durable rules/decisions, not every test log.

## Verification-tool selection requirements for 005-C

When 005-C chooses the foundational Python/build/static-analysis/test tooling and source topology, it MUST preserve this verification architecture.

The selected tools should support or compose cleanly with:

- deterministic unit/contract tests;
- parametrized reusable adapter conformance suites;
- controllable time/randomness/failure injection;
- Spark/integration test profiles;
- architecture/import/dependency checks;
- coverage of serialization/migration contracts;
- explicit markers/profiles for network/platform/slow/statistical tests;
- machine-readable CI result output;
- reproducible local/CI invocation;
- optional-dependency isolation;
- no hidden outbound network in portable-core profiles.

Tool popularity alone is not sufficient selection rationale.

## Verification anti-patterns

Implementation MUST avoid treating the following as adequate proof:

- `it compiles`;
- one notebook run;
- one successful Databricks/Spark job;
- line coverage percentage without contract assertions;
- snapshot/golden updates that merely bless new current behavior;
- mocks that eliminate the concurrency/security/distributed property being tested;
- platform `SUCCESS` as domain completion proof;
- rerunning stochastic tests until they pass;
- full driver collection in tests when the production contract is distributed;
- testing only the newest schema/version and deleting backward-compatibility fixtures;
- allowing network in all tests because one optional adapter needs it;
- using production/customer data as convenient fixtures;
- measuring performance without recording workload/environment context.

## 005-C handoff obligations

005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement — must use this verification architecture to select code boundaries that are enforceable.

005-C must specifically determine:

- physical source/test topology corresponding to logical verification layers;
- the concrete Python test/static/build toolchain;
- architecture/import/dependency checking mechanism;
- stable repository commands for Q0/Q1 and entry points for heavier profiles;
- test/fixture package boundaries that do not create production back-dependencies;
- optional dependency/extras topology that supports AF-02/AF-12;
- how conformance suites are shared across adapters without coupling core to adapters;
- how failure clocks/randomness/provider fakes are exposed through test seams;
- where compatibility/golden fixtures live and how they are versioned;
- initial CI workflow/check mapping for the required gates.

005-C must not weaken a verification requirement merely to simplify package topology.

## Deferred decisions

005-B intentionally leaves open:

- test-runner/property-test/mocking libraries;
- formatter/linter/type checker;
- coverage tool/threshold;
- CI vendor/workflow syntax;
- exact source/test directory names;
- Python/Spark support versions;
- persistence/runtime/platform technologies;
- exact performance thresholds;
- exact scale datasets/hardware profiles;
- artifact-retention durations;
- machine-readable acceptance-evidence schema;
- branch-protection configuration.

These are downstream choices constrained by this authority.

## Exit criteria

005-B is complete when:

- verification layers are defined;
- architecture-fitness properties are enumerated;
- distributed/runtime/recovery/Evidence/security/platform/scale verification obligations are explicit;
- fixture and golden-data rules are defined;
- deterministic versus stochastic verification is separated;
- default network/offline test posture is defined;
- adapter conformance-suite expectations are defined;
- PR/integration/scheduled/release quality-gate semantics are defined;
- flakiness/quarantine/waiver rules are explicit;
- acceptance-evidence requirements are defined;
- 005-C has concrete tool/topology requirements without premature tool selection.
