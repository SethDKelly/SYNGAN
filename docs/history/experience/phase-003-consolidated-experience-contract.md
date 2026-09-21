---
type: Experience Contract
title: Phase 003 Consolidated Experience Contract
status: active
---

# Phase 003 Consolidated Experience Contract

## Purpose

Freeze the cross-workflow actor-visible and programmatic experience contract established by Phase 003 before SYNGAN enters representation and architecture design.

This document consolidates the invariant experience obligations established by the eight Phase 003 workflow authorities. It does not replace those detailed authorities, redefine concept ownership, or prescribe a Python/API/UI/storage/runtime architecture.

## Governing authority

This contract remains downstream of:

- [Design Authority](../authority/index.md)
- [Accepted Concepts](../concepts/index.md)
- [Accepted Synchronizations](../synchronizations/index.md)
- [Network and External Dependency Policy](../authority/network-external-dependency-policy.md)
- [Reproducibility Contract](../authority/reproducibility-contract.md)

Detailed experience authority remains in:

1. [Workflow Entry, Source Context & Lifecycle Orientation](workflow-entry-source-context-lifecycle-orientation.md)
2. [Data Meaning, Constraint & Strategy Preparation](data-meaning-constraint-strategy-preparation.md)
3. [Learning & Learned State Lifecycle](learning-learned-state-lifecycle.md)
4. [Generation Request, Condition, Validation & Output Promotion](generation-request-condition-validation-output-promotion.md)
5. [Evaluation, Evidence & Review](evaluation-evidence-review.md)
6. [Execution Monitoring, Failure, Recovery & Cancellation](execution-monitoring-failure-recovery-cancellation.md)
7. [Provenance, Reproducibility & Historical Inspection](provenance-reproducibility-historical-inspection.md)
8. [Enterprise Dependency, Offline/No-Egress & Safety](enterprise-dependency-offline-no-egress-safety.md)

## Cross-workflow model

The Phase 003 experience can be understood around four recurring barriers:

```text
1. PREPARATION / READINESS
   editable intent + contextual compatibility
                 ↓
2. SEMANTIC COMMITMENT
   exact material bindings become historical
                 ↓
3. OPERATIONAL REALIZATION
   Execution / Attempts / recovery / cancellation
                 ↓
4. SEMANTIC PROMOTION / FINDING
   owning domain concept establishes authoritative result
```

Historical inspection and enterprise safety cut across all four barriers:

```text
historical bindings / Provenance / reproducibility
                     +
dependency / network / egress / disclosure context
```

No implementation may collapse these barriers merely because one API call, page, notebook cell, or platform job happens to span several of them.

## Barrier 1 — preparation and readiness

### Contextual preparation

Before commitment, actors may compose information from several authorities to understand proposed work.

Typical preparation may include:

- source identity/context;
- Data Meaning;
- applicable Constraints and handling;
- Strategy/method capability;
- Learned State or direct-generation basis;
- Generation Conditions;
- Evaluation Criterion/method suitability;
- dependency/network/no-egress requirements;
- known completion or Evidence obligations.

This composition does not create a new `Preparation`, `Workflow`, `Metadata`, `Configuration`, `Compatibility`, or `Readiness` concept.

### Readiness is derived and local

Readiness is an experience assessment for a proposed commitment.

It may preserve states equivalent to:

- not ready / blocked by known issue;
- ready with explicit limitations;
- ready for commitment;
- readiness indeterminate.

Readiness MUST NOT become globally mutable state on Data Meaning, Constraint, Strategy, Learned State, Evaluation Criterion, or another shared authority.

A readiness result MUST be reconsidered when a material input changes.

### `blocked` is not a domain terminal state

`Blocked` is useful experience language for a proposed action that cannot currently proceed because of unresolved semantics, incompatibility, missing dependency, policy restriction, or indeterminate permission.

It MUST NOT be used as a substitute for the committed lifecycle states owned by Learning, Generation, Evaluation, or Execution.

## Barrier 2 — semantic commitment

### Commitment freezes material meaning

Learning, Generation, and Evaluation each cross a semantic commitment boundary.

The experience MUST make clear that after commitment, material changes such as the following are not ordinary edits/retries:

- source identity;
- Data Meaning revision;
- Strategy/configuration;
- applicable Constraint revisions/handling;
- Learning sampling/approximation semantics;
- Learned State/direct-generation basis;
- Generation Conditions/quantity/scope/tolerances;
- Evaluation Criterion/subject/reference/method/coverage;
- dependency/base-artifact identity;
- network/no-egress posture;
- materially behavior-changing reproducibility state.

Where such a change is material, the owning concept must create a new distinguishable commitment according to canonical semantics.

### Review-before-commit

Human and programmatic surfaces MUST make the material commitment inspectable before or at commitment.

Convenience APIs MAY infer/default/recommend state, but they MUST NOT make material semantic authority permanently invisible.

## Barrier 3 — operational realization

### Semantic and operational state remain distinct

Learning, Generation, and Evaluation own semantic intent and semantic completion.

Execution owns operational realization, Attempt history, operational progress/health, retry/resume/cancellation realization, and operational failure/unknown-state facts.

Therefore:

```text
Execution.completed
        !=
Learning.completed / Generation.completed / Evaluation.completed
```

The experience MUST preserve this distinction in both human and programmatic surfaces.

### One logical Execution, many physical realizations

A committed activity may have one logical Execution spanning many Attempts, platform jobs, worker sets, clusters, or scheduler submissions.

Platform job/run identity remains drill-down/reference information rather than SYNGAN Execution authority.

### Retry is same-semantics continuation

Retry/resume may be offered only when the same committed activity can continue safely.

Scheduler resubmission capability does not establish retry safety.

A material semantic change is not retry.

### Unknown state remains explicit

Operational uncertainty MUST NOT be coerced to success or failure merely to simplify recovery.

Unknown/indeterminate Attempt or side-effect state may require reconciliation/fencing before safe continuation.

### Cancellation request is not terminal cancellation

Cancellation is first intent and may resolve as cancelled, completed before cancellation took effect, failed during cancellation, or unknown pending reconciliation.

The parent domain concept retains authority over its semantic terminal state.

## Barrier 4 — semantic promotion and findings

### Physical existence is not domain authority

Phase 003 preserves three major non-final/result boundaries:

```text
checkpoint/intermediate learned material
        != Learned State

partial/complete candidate output
        != completed Generation output

partial/diagnostic evaluation material
        != Evidence answering the Criterion
```

Architecture MUST preserve a distinguishable semantic promotion/finding barrier even if physical bytes are reused in place.

### Single semantic promotion

Exactly-once physical computation is not required.

Repeated or overlapping physical work MUST NOT create ambiguous duplicate authoritative domain results.

Under the current model:

- successful Learning establishes zero or one primary logical Learned State;
- successful Generation establishes zero or one completed logical output;
- Evaluation establishes its legitimate Evidence set without duplicate authoritative findings caused solely by retries.

### Generation completion obligations stay requirement-specific

Generation completion may depend on quantity, mandatory Conditions, applicable required Constraints, candidate integrity, dependency/no-egress compliance, required Provenance, and Evidence of sufficient claim strength.

A generic `validation_passed=true` surface is insufficient where it would hide which obligation was actually established, violated, or remained indeterminate.

### Evaluation success and favorable Evidence remain different

A valid Evaluation can successfully establish unfavorable or indeterminate Evidence.

Operational success, Evaluation success, Evidence finding, and external decision authority MUST remain distinct.

## Evidence and decision contract

### Question, method, finding, decision remain separate

```text
Evaluation Criterion -> question
Evaluation           -> examination/method
Evidence             -> durable finding
External authority   -> approval/release/use/remediation decision
```

No available metric may silently define the Criterion, and Evidence MUST NOT become release/use authority.

### Claim strength remains bounded

Evidence strength MUST NOT exceed what the Evaluation method, scope, coverage, assumptions, uncertainty, and approximation semantics support.

Missing Evidence, unfavorable Evidence, indeterminate Evidence, stale Evidence, superseded Evidence, inapplicable Evidence, and invalidated Evidence remain distinguishable.

### Review remains multidimensional

Fidelity, utility, validity, privacy/disclosure risk, and other explicit Criteria remain independent unless an explicit decision rule combines them.

No generic `Quality` state or score may silently decide tradeoffs among these dimensions.

## Historical and current-state contract

### Historical truth is immutable context

Historical inspection MUST show the exact state actually bound/used by the historical activity.

Current source aliases, Data Meaning revisions, Strategy versions, Learned State lifecycle state, Evidence applicability, dependencies, or policy posture MUST NOT replace historical bindings.

### Provenance remains relational

Provenance owns typed historical relationships and stable references, not copies of all canonical concept state or platform telemetry.

Typed meanings such as `bound by`, `produced by`, `used`, `evaluated`, `operationally realized by`, and `recovered from` remain distinguishable where material.

### Reproducibility is assessed, not inherited

A reproducibility assessment states a target, preserved conditions, equivalence rule, dependencies, randomness/nondeterminism/approximation, and supported class.

Accepted classes remain:

- exact deterministic;
- semantic;
- statistical;
- bounded/approximate;
- comparative;
- not reproducible / insufficient context.

Re-execution, seed presence, or reproduction readiness does not establish successful reproduction.

Current reproduction capability may weaken without changing historical truth.

## Enterprise dependency and safety contract

### Dependency facts remain typed

The experience MUST keep separate:

1. dependency requirement/profile;
2. dependency availability;
3. dependency identity/integrity;
4. semantic compatibility;
5. external permission/policy compatibility;
6. network requirement;
7. data-egress behavior.

A dependency being present does not imply it is correct, compatible, permitted, or safe to transmit data to.

### Offline/no-egress behavior is explicit

Core supported structured/tabular workflows remain compatible with no required outbound network after required local provisioning.

Missing dependencies MUST NOT cause hidden downloads, model-hub access, remote fallback, telemetry egress, or silent artifact substitution.

Provisioning/acquisition-time network behavior remains distinct from runtime network behavior.

### Network and egress remain different

Where relevant, actor/programmatic surfaces preserve distinctions among:

- network access with no dataset/content egress;
- non-sensitive metadata/configuration transfer;
- source-derived information transfer;
- source-record transfer;
- generated-record transfer.

Disclosure does not grant authorization.

### Derived state is not presumed non-sensitive

Learned State, embeddings/statistics/model parameters, candidate/completed synthetic output, Evidence, diagnostics, and Provenance may be sensitive.

Synthetic origin does not imply anonymity, formal privacy, export permission, or release approval.

## Disclosure-state contract

The experience MUST preserve the distinction among:

- **absent** — the value/fact does not exist;
- **unknown** — the system cannot establish it;
- **unavailable** — expected/historical state cannot currently be resolved;
- **withheld** — the system knows material detail exists but this actor may not inspect it;
- **redacted/authorized summary** — a permitted transformed view is shown while underlying detail remains protected.

`withheld` MUST NOT be serialized/presented as ordinary null/unknown when the system knows the fact exists.

A disclosure restriction MUST NOT rewrite historical Provenance or canonical state.

## Typed-state language guardrail

Similar labels may appear in different lifecycle contexts and MUST remain typed by their owner/context rather than becoming one universal status enum.

Examples:

- `indeterminate` may describe readiness, operational state, Evidence, compatibility, policy result, or reproducibility support; the context and reason MUST remain explicit;
- `restricted` on Learned State describes current future-use lifecycle status, while `withheld` describes actor disclosure;
- `completed with limitations` applies only where the owning domain contract explicitly permits non-mandatory limitations;
- `blocked` describes inability to proceed in a contextual/pre-commit or policy decision, not a generic domain terminal state.

Architecture MAY reuse shared representation primitives, but it MUST preserve these semantic distinctions.

## Programmatic and human parity

Human UI, notebook, CLI, SDK, and API surfaces MAY differ in ergonomics but MUST preserve equivalent access to material semantic distinctions.

A convenience surface is insufficient if it exposes only:

- a DataFrame;
- a scalar `status`;
- a platform run ID;
- a Boolean `passed`/`reproducible`/`offline`/`secure` flag;
- a generic error string;
- a raw graph dump.

Programmatic users must be able to determine the material commitment, lifecycle, result authority, Evidence strength, recovery state, dependency/network posture, historical binding, and disclosure status applicable to their workflow.

## Enterprise-scale experience contract

Experience/state inspection MUST remain practical for sources and outputs containing tens/hundreds of millions of records and for executions with very large platform telemetry volumes.

Canonical experience state SHOULD rely on bounded control-plane facts, stable distributed references, summaries, manifests/fingerprints where later architecture supplies them, Evidence summaries, and selected platform references.

No ordinary experience requires full source/output/Learned State/diagnostic/log materialization in driver-local or UI memory.

## Anti-god-concept consolidation

Phase 003 does not justify introducing standalone authority for:

- Workflow;
- Session;
- Metadata;
- Configuration;
- Readiness;
- Compatibility;
- Validation;
- Quality;
- Scorecard;
- Model;
- Artifact;
- Run;
- Job;
- Attempt;
- Checkpoint;
- Retry;
- Recovery;
- Reconciliation;
- History;
- Lineage;
- Reproduction;
- Reproducibility Status;
- Security;
- Policy;
- Trust;
- Egress;
- Access Control;
- Approval.

These remain composed experiences, contextual assessments, subordinate state/actions, external authority, Provenance subsets, cross-cutting contracts, or downstream representation mechanisms.

## Architecture handoff obligations

Phase 004 MUST produce architecture capable of preserving at least:

1. stable concept/activity/result identity and historical revisions;
2. explicit semantic commitment snapshots;
3. contextual compatibility/readiness without global mutable truth;
4. one logical Execution with ordered Attempt history and platform mappings;
5. retry/resume/reconciliation/cancellation state without semantic mutation;
6. distinct non-final checkpoint/candidate/diagnostic state and semantic promotion;
7. distributed logical Learned State/output identities independent of one local file/object;
8. requirement-specific Evaluation/Evidence with coverage/uncertainty/claim strength;
9. typed Provenance with stable historical references and bounded materiality;
10. qualified reproducibility assessment without a universal copied state object;
11. dependency profile/resolution/identity/policy/egress separation;
12. no hidden network acquisition or remote fallback;
13. truthful withheld/redacted/unknown/absent/unavailable representation;
14. bounded enterprise-scale control-plane state with drill-down to distributed/platform-native detail;
15. equivalent semantic access across human and programmatic surfaces;
16. extension/runtime architecture that does not make CTGAN, GANs, Spark ML, PyTorch, HuggingFace, LLMs, Databricks, or one platform universal semantics.

## Representation boundary

This consolidated contract does not select:

- Python package/module layout;
- public class hierarchy;
- fluent-builder versus resource API;
- REST/CLI/UI surface;
- database/storage engine;
- graph/event/table provenance representation;
- manifest/hash/fingerprint technology;
- Spark table/file/output promotion technology;
- scheduler/orchestrator;
- checkpoint format;
- fencing/transaction/lease mechanism;
- strategy plugin system;
- model registry;
- authentication/authorization/policy engine;
- encryption/signing/DLP/egress technology;
- deployment topology;
- Databricks-specific architecture.

Those choices begin in Phase 004 and remain constrained by this contract.