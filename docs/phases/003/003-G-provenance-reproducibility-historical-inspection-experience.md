---
type: Phase Record
title: 003-G — Provenance, Reproducibility & Historical Inspection Experience
status: complete
---

# 003-G — Provenance, Reproducibility & Historical Inspection Experience

## Objective

Translate accepted Provenance, historical binding, Execution/Attempt materiality, Evidence history, dependency identity, and Reproducibility Contract semantics into a coherent actor-visible and programmatic historical-inspection experience.

003-G focuses on explaining and comparing historical derivations and assessing current reproduction capability without making Provenance a shadow metadata database or Reproducibility a standalone concept/state object.

## Governing authority

- [Provenance](../../concepts/provenance.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)
- [002-G — Provenance, Reproducibility Contract & Historical Binding Specification](../002/002-G-provenance-reproducibility-historical-binding-specification.md)
- [003-C — Learning & Learned State Lifecycle Experience](003-C-learning-learned-state-lifecycle-experience.md)
- [003-D — Generation Request, Condition, Validation & Output Promotion Experience](003-D-generation-request-condition-validation-output-promotion-experience.md)
- [003-E — Evaluation, Evidence & Review Experience](003-E-evaluation-evidence-review-experience.md)
- [003-F — Execution Monitoring, Failure, Recovery & Cancellation Experience](003-F-execution-monitoring-failure-recovery-cancellation-experience.md)
- [Accepted Synchronizations](../../synchronizations/index.md)

## Canonical experience authority created

- [Provenance, Reproducibility & Historical Inspection](../../experience/provenance-reproducibility-historical-inspection.md)

## Main decisions

### 1. Historical inspection has three primary actor goals

003-G defines three complementary experiences:

1. **Explain this result** — traverse the material historical path that produced a result/finding;
2. **Compare these historical paths** — show exact material differences without inventing causality;
3. **Assess reproducibility now** — state the strongest currently supportable reproduction class and its limiting context.

No single giant graph view is required.

### 2. Provenance stays relational and non-duplicative

The experience follows typed relationships to canonical owners rather than copying Data Meaning, Constraint, Strategy, Learning, Generation, Evidence, Execution, or payload state into a provenance warehouse.

High fan-in / low authority fan-out remains intact.

### 3. Historical truth and current state are distinct

Old Learning/Generation/Evaluation views show the exact revisions and identities actually used.

Current facts such as a newer Data Meaning revision, retired Strategy, restricted Learned State, stale Evidence, unavailable dependency, or changed source alias are shown as current context—not replacements for historical bindings.

### 4. Mutable aliases do not masquerade as historical identity

Human-friendly names may be shown, but the experience also exposes the historically distinguishing version/snapshot/fingerprint/identity basis when material.

If the same table alias resolved to S7 for one activity and S8 for another, historical comparison shows that the source changed.

### 5. Weak or missing identity remains explicit

A missing source version, lost base artifact, mutable remote endpoint, unknown runtime version, or missing material recovery record becomes an explicit historical/reproduction limitation.

Current state is not substituted merely to make the history appear complete.

### 6. Relationship types remain visible

The experience preserves distinctions such as:

- bound/governed by;
- derived from/produced by;
- used/depended on;
- evaluated/referenced;
- operationally realized by;
- recovered/resumed from;
- superseded/restricted/retired/invalidated context.

`related to` alone is insufficient where interpretation depends on relationship meaning.

### 7. Provenance gaps and corrections are inspectable

Required derivation/commitment paths can be checked for completeness.

If an assertion is corrected later, the current corrected assertion and earlier assertion history remain distinguishable when auditability requires it.

A provenance correction does not mutate the canonical history owned by another concept.

### 8. Reproducibility remains an assessment/contract, not state authority

003-G preserves the accepted classes:

- exact deterministic;
- semantic;
- statistical;
- bounded/approximate;
- comparative;
- not reproducible / insufficient context.

The experience does not reduce them to `reproducible=true/false`.

### 9. Reproduction claims must be explainable

A reproducibility assessment exposes:

- target;
- preserved conditions;
- dependencies;
- randomness/nondeterminism;
- approximations;
- materially relevant retry/recovery facts;
- missing/mutable context;
- supported class;
- why stronger classes are unsupported.

### 10. Seed visibility cannot inflate determinism claims

A recorded seed may be shown, but exact deterministic reproduction is not claimed unless RNG semantics, distributed ordering, accelerator/runtime behavior, dependencies, and other material factors support that equivalence.

### 11. Reproduction readiness and reproduction success are separate

Historical inspection may determine that sufficient context exists to **attempt** a reproduction.

That is not proof that a new attempt reproduces the target.

Actual reproduction is new Learning/Generation/Evaluation work as appropriate, with explicit equivalence Criteria/Evidence where needed.

### 12. Re-execution is not reproduction by default

The experience can show that a workflow/job is technically rerunnable while historical reproduction is unsupported because source/dependency identity has drifted or cannot be reconstructed.

Same API call, alias, seed, model family, or endpoint does not establish reproduction.

### 13. Current reproducibility can degrade without historical corruption

A historical output may remain fully traceable while a required artifact is no longer available today.

The experience then shows complete historical Provenance plus weakened current reproducibility rather than treating history as invalid.

### 14. Historical comparison is difference-oriented, not causal

Two derivations can be compared across source, Data Meaning, Constraints, Strategy, Learned State, Conditions, Criteria/methods, dependencies, runtime, Attempts, and Evidence.

A difference is not automatically a causal explanation or a quality judgment.

Causal/fitness claims require explicit Evaluation/Evidence.

### 15. Evidence history remains scoped

Historical inspection can traverse Evidence to its exact Criterion/Evaluation/subject/reference/method/coverage context and distinguish original finding from current applicability.

Evidence used in Generation completion is visibly tied to the original promotion decision; later Evidence is not retroactively inserted into that decision.

### 16. Execution history is materiality-bounded

Material Attempts, recovery, cancellation, unknown-state reconciliation, runtime/dependency changes, and platform references can be traversed.

Every low-level task/log/metric remains outside canonical Provenance unless material.

### 17. Restricted provenance must not fabricate history

003-G recognizes that Provenance may be sensitive.

Until 003-H deepens disclosure/access semantics, the experience requires that withheld detail be represented as withheld rather than replaced with false or current substitute data.

### 18. Enterprise-scale historical inspection remains control-plane oriented

Historical explanation and reproducibility assessment use stable references, revisions, typed relationships, bounded Attempt summaries, dependency identities, and Evidence summaries without collecting full source/output/Learned State/log payloads into one process.

## Historical explanation example

```text
Output O42

Produced by
- Generation G42
- Strategy v2 / config C9
- Learned State LS17
- Conditions K1/K2
- Constraints C1/C2

Learned State LS17
- produced by Learning L12
- source snapshot S8
- Data Meaning DM4
- base artifact B3

Execution
- Attempt A1 failed recoverably
- Attempt A2 resumed from R1

Completion Evidence
- E31 / E32 / E33

Current changes
- source alias now points to S12
- Strategy v2 retired
- base artifact B3 still available
```

This is an experience example, not a required UI or graph representation.

## Reproducibility example

```text
Target
- Generation G42 / Output O42

Supported reproduction class
- statistical

Preserved
- source snapshot S8
- Data Meaning DM4
- Strategy/config C9
- Learned State LS17
- Conditions/Constraints
- base artifact B3 identity
- RNG/seed policy

Limits
- nondeterministic GPU kernels
- distributed ordering not fixed

Unsupported stronger class
- exact deterministic
```

## Actor experience conclusions

### Data Practitioner

Needs concise derivation explanation, exact revisions, material changes between results, Evidence context, and reproduction feasibility.

### Platform Operator

Needs material Execution/Attempt/recovery/runtime history without replacing the domain path with telemetry.

### Data Owner / Steward

Needs exact source/semantic/rule versions, corrections, and historical-versus-current state.

### Privacy / Risk / Governance Reviewer

Needs dependency/egress and Evidence lineage, current applicability, reproducibility limitations, and appropriate treatment of sensitive Provenance.

### Synthetic Data Consumer

Needs understandable production history, relevant Evidence/limitations, and reproduction context without implementation internals by default.

## No new concept result

003-G does not require standalone concepts for:

- Lineage;
- History;
- Historical View;
- Run Comparison;
- Difference;
- Reproduction;
- Reproduction Attempt;
- Reproducibility Status;
- Reproduction Readiness;
- Metadata Graph;
- Manifest;
- Snapshot;
- Artifact.

These remain Provenance subsets/actions, experience compositions/assessments, new domain activities where actually executed, or future representation mechanisms.

## Deferred to later Phase 003 groups

### 003-H

Deepen access/disclosure boundaries for sensitive Provenance, dependency trust, artifact acquisition, offline/no-egress enforcement visibility, sensitive diagnostic data, and enterprise safety posture.

### 003-I

Audit cross-workflow consistency across preparation, Learning, Generation, Evaluation, Execution, Provenance/reproducibility, and enterprise safety before Phase 003 exit.

## Representation questions intentionally deferred

003-G does not select:

- provenance graph/store technology;
- provenance event schema;
- query language/API;
- graph visualization;
- OpenLineage/MLflow/catalog integration;
- snapshot/version/fingerprint/hash/manifest mechanism;
- software environment capture implementation;
- reproduction orchestrator;
- diff visualization;
- dependency registry;
- provenance access-control/redaction implementation;
- retention policy.

## Exit criteria

- [x] result-explanation historical traversal defined;
- [x] historical-path comparison defined;
- [x] current reproducibility assessment defined;
- [x] Provenance remains non-duplicative typed relationship authority;
- [x] historical bindings remain distinct from current state;
- [x] mutable aliases rejected as sole historical identity;
- [x] identity/provenance gaps remain explicit;
- [x] provenance correction/auditability experience defined;
- [x] accepted reproduction classes preserved;
- [x] reproduction claim explanation includes target/conditions/limits;
- [x] seed does not imply determinism;
- [x] reproduction readiness distinguished from actual reproduction success;
- [x] re-execution distinguished from reproduction;
- [x] current reproducibility degradation does not rewrite history;
- [x] historical difference does not imply causality;
- [x] Evidence historical/current applicability distinctions preserved;
- [x] material Execution history remains traversable without telemetry explosion;
- [x] sensitive Provenance is not falsified when disclosure is restricted;
- [x] programmatic/human semantic parity preserved;
- [x] enterprise-scale inspection avoids mandatory full payload/log collection;
- [x] no representation architecture selected prematurely.

## Exit assessment

**Status: complete.**

SYNGAN now has a canonical historical-inspection experience that can explain and compare material derivations, preserve historical truth independently of current state, and state current reproducibility at the strongest defensible class without duplicating canonical state or overstating identity, dependency, or nondeterminism guarantees.

## Next phase

**003-H — Enterprise Dependency, Offline/No-Egress & Safety Experience**
