---
type: Phase Record
title: 006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test
status: complete
---

# 006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test

## Objective

Stress-test SYNGAN's accepted concept/synchronization/runtime architecture against materially different synthesis, text, topology, state and Evaluation shapes before production implementation is authorized.

006-D uses concrete algorithm/runtime shapes as **falsification probes**, never as semantic templates or implementation work.

**Phase 006 remains design-only. No production source, algorithm implementation, package scaffold, Spark distribution code, model artifact, test suite, CI or deployment infrastructure is authorized or created.**

## Governing authority

006-D is downstream of:

- [Concept Design Methodology](../../authority/design-methodology.md);
- [Accepted Concepts](../../concepts/index.md);
- [Core Synchronizations](../../synchronizations/core-synchronizations.md);
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md);
- [Operational Authority Continuity & Regressive Recovery Contract](../../authority/operational-authority-continuity-regressive-recovery-contract.md);
- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Phase 005 Consolidated Implementation-Planning Contract](../../implementation/phase-005-consolidated-implementation-planning-contract.md);
- [006-A](006-A-post-planning-concept-completeness-mechanism-vs-concept-scope-boundary-revalidation.md);
- [006-B](006-B-temporal-authority-disaster-recovery-rollback-fork-historical-truth-refinement.md);
- [006-C](006-C-end-to-end-scenario-exception-failure-adversarial-synchronization-validation.md).

## Discovery evidence

The full probe matrix is preserved in:

[Reference Strategy/Method, Text & Distributed-Runtime Falsification Probes](../../discovery/reference-strategy-method-topology-text-distribution-probes.md).

That document remains design evidence rather than canonical authority.

## Probe set

006-D exercised thirteen materially different shapes:

1. Learning-based single-table deep-generative / CTGAN-like family;
2. direct/simple single-table Generation without fabricated Learning/Learned State;
3. self-contained free-form text-bearing table;
4. locally provisioned pretrained text Strategy;
5. runtime-network text Strategy;
6. mixed-field/composite Strategy;
7. time-series Strategy;
8. multi-table shared-key Strategy;
9. deterministic/bounded Evaluation;
10. statistical/approximate Evaluation;
11. large/sharded Learned State;
12. Spark cluster package/runtime distribution;
13. self-contained text execution across Spark executors.

No algorithm was implemented.

## Overall result

**PASS WITH TARGETED CROSS-CUTTING REFINEMENT.**

The accepted eleven concepts and fifteen synchronizations remain sufficient for the tested algorithm/runtime shapes.

006-D does not expose a need for:

- a CTGAN/GAN/PyTorch concept;
- a `Text` or `Language Model` concept;
- a `Tokenizer`/`Model Artifact` concept;
- a `Composite Strategy` concept;
- a `Runtime Environment`/`Cluster Package`/`Distribution` concept;
- a new synchronization ID.

The provisional `Relationship` candidate remains open for 006-G.

## Canonical cross-cutting authority established

006-D creates:

[Self-Contained Execution & Runtime Distribution Closure Contract](../../authority/self-contained-execution-runtime-distribution-closure-contract.md).

The contract is upstream of later runtime/package/platform realization.

Its governing rule is:

> **A supported execution profile is closed only when its declared material executable and artifact dependencies are resolvable without undeclared acquisition and are available compatibly to every runtime role that may execute the committed work. Driver-local availability alone is never proof of distributed readiness.**

## Self-contained text-bearing baseline decision

006-D accepts a stronger baseline requirement than merely permitting offline local artifacts.

The supported baseline installation/profile must include at least one **source-derived/local text-capable synthesis path** for structured tables containing free-form text fields.

The baseline MUST NOT require:

- Hugging Face Hub access;
- hosted LLM/inference APIs;
- first-use model download;
- externally provisioned pretrained weights;
- hidden remote fallback.

The exact text algorithm remains undecided.

A source-derived implementation might later use locally learned character/token/phrase/statistical/autoregressive/pattern state or another approach. The important contract is operability and self-containment, not one algorithm.

### Quality boundary

Self-contained baseline support does **not** promise foundation-model-level semantic/world knowledge.

A baseline Strategy may expose explicit limitations for coherence, long-context behavior, vocabulary, novelty, or semantic richness.

Where richer externally pretrained knowledge is required, the Strategy must declare that dependency explicitly.

## Text capability classes

006-D distinguishes three legitimate Strategy shapes:

### 1. Source-derived/self-contained text

Normal execution requires no externally acquired pretrained model and no runtime network service.

This capability is required in the supported baseline.

### 2. Local-artifact-enhanced text

A pretrained model/tokenizer/vocabulary or equivalent artifact is provisioned locally before committed execution.

This is optional capability and can remain fully offline at runtime, but it does not replace the package-only baseline requirement.

### 3. Runtime-network text

A hosted service/API is required during material execution.

This is optional, explicit, subject to egress/authorization policy, incompatible with self-contained/offline profiles, and never a hidden fallback.

## Text concept-boundary result

Free-form text remains a semantic role and Strategy capability rather than a new concept.

Ownership remains:

```text
free-form text semantic role
        -> Data Meaning

text synthesis capability / dependency / limitations
        -> Synthesis Strategy

source-derived reusable text model/vocabulary/state
        -> Learning / Learned State where applicable

requested text-bearing output
        -> Generation

fidelity / pattern / semantic / memorization / disclosure questions
        -> Constraint and/or Criterion / Evaluation / Evidence
```

The existing Data Meaning contract already rejects treating every physical string as categorical by default.

## Composite Strategy result

006-D confirms that one semantic Strategy may combine several implementation techniques for different field/groups without creating a new orchestration concept.

However, the Phase 005 assumption that one top-level implementation binding might be described through one primary distribution is too narrow if taken literally.

A future top-level `ImplementationBindingRef` may need to resolve an exact **implementation closure** containing:

- multiple implementation components;
- Python/native dependencies;
- codecs;
- model/tokenizer/base artifacts;
- accelerator/runtime requirements.

This closure remains architecture/integration state. The semantic Strategy still owns the combined behavior/capability declaration.

Material component selection cannot silently change during runtime.

## CTGAN-like probe result

A Learning-based deep-generative family composes cleanly with:

```text
Strategy
    ↓
Learning
    ↓
Learned State
    ↓
Generation
```

Its Learned State may include several manifested components rather than one model file, including encoder/transform state and neural parameters.

The design therefore does not need a universal `Model` object or `fit()/sample()` lifecycle.

Any source-size-proportional single-process preprocessing/training stage remains a scale cliff even when the source arrives as a Spark DataFrame.

## Direct-generation probe result

Direct/simple generation remains fully valid without fabricated Learning/Learned State.

This protects the public/runtime design from becoming CTGAN-shaped merely because a deep-generative family is an important initial method candidate.

## Time-series probe result

Time-series algorithms fit existing Learning/Generation/Execution/Evaluation ownership.

The unresolved semantic question remains the ownership of reusable sequence membership/order structure. That remains a 006-G falsification case for the provisional `Relationship` candidate.

006-D does not accept a `TimeSeries`, `SequenceModel`, or temporal-specific synchronization.

## Multi-table probe result

Multi-table shared-key algorithms can use:

- multi-component Learned State;
- coordinated multi-part Generation;
- whole-result completion;
- cross-scope Constraint/Evaluation requirements.

No runtime/concept redesign is required merely because several tables participate.

The descriptive shared-key relationship itself remains the 006-G concept question.

## Evaluation probe result

Both deterministic/exhaustive and statistical/approximate Evaluation shapes fit the current Criterion → Evaluation → Evidence contract.

The design correctly prevents:

- runtime `pass=true` from becoming Evidence directly;
- sampled/approximate findings from claiming universal proof;
- large diagnostic output from being forced into control-plane/driver memory;
- duplicate retry contributions from inflating coverage.

## Large/sharded Learned-State result

The current manifest/codec boundary survives only under an explicit non-driver-local interpretation.

A future runtime must be able to resolve/shard/stream large state/model components directly into worker/accelerator contexts.

A universal:

```text
load entire Learned State on driver
broadcast to workers
```

is rejected as an enterprise architecture assumption.

Small immutable broadcast remains possible where appropriate.

## Spark cluster distribution result

006-D establishes the following design distinction:

```text
driver can import/resolve implementation
        !=
all executors can execute implementation
```

For a distributed Attempt, every worker/runtime role that may execute material code must satisfy the exact compatible runtime distribution closure.

That closure can include:

- SYNGAN package/build;
- Strategy/Evaluation implementation components;
- Python/native dependencies;
- codecs;
- tokenizer/model/base artifacts;
- Learned-State components;
- accelerator/runtime requirements.

### Dynamic workers

Dynamic allocation/autoscaling means a one-time enumeration of current workers is not a sufficient universal design.

A deployment may instead prove closure through an immutable/proven worker image, environment bundle, bootstrap template or equivalent provider guarantee. Any later worker must satisfy the same closure before executing material work.

### No mandatory Spark distribution mechanism

006-D does not select `--py-files`, Spark archives, PEX, Conda, uv, provider libraries, containers or another specific mechanism.

Current Spark documentation demonstrates why mechanism choice must remain capability-specific: Spark native Python-file shipping handles `.py`/`.zip`/`.egg`, while more complete dependency environments require other mechanisms when Wheels/native dependencies are involved.

The architectural rule is exact closure, not the packaging command.

## Self-contained text + Spark result

A distributed text Strategy is self-contained only when both hold:

```text
acquisition closure
(no hidden remote/package/model fetch)

+

distribution closure
(exact compatible runtime on every worker)

=

distributed self-contained execution
```

A text implementation that is fully local on the driver but missing its tokenizer/runtime/model state on executors is not ready.

A missing executor dependency must fail/block readiness rather than download from the public Internet during the Attempt.

## Hugging Face disposition

Hugging Face/Transformers is neither prohibited nor required.

Current ecosystem support for offline local-file loading demonstrates that a future optional locally provisioned adapter is feasible.

However:

- Hugging Face Hub is not a baseline dependency;
- `transformers` is not a base semantic dependency;
- model/tokenizer download is provisioning/acquisition, not committed runtime behavior;
- `trust_remote_code`-style behavior is a material executable trust characteristic and must remain security-visible;
- local artifact identity must be exact/attributable when behaviorally material.

No Hugging Face integration is implemented in Phase 006.

## Synchronization result

No new synchronization is needed.

The refined existing rules already cover:

- Strategy/activity compatibility under SYNC-02/SYNC-06;
- current dependency/runtime/platform qualification for continuation under SYNC-04/SYNC-07/SYNC-11;
- material executable/artifact attribution under SYNC-14/SYNC-15.

006-I must ensure architecture/planning makes runtime distribution closure an explicit compatibility/admission input.

## Concept/synchronization counts

At 006-D exit:

```text
accepted concepts             11
accepted synchronizations     15
new accepted concepts          0
new synchronization IDs        0
new Phase 006 cross-cutting contracts
  - Operational Authority Continuity
  - Self-Contained Execution & Runtime Distribution Closure
reopened candidate concepts    Relationship
```

## BDR-003 disposition

**BDR-003 — representative Strategy/method/topology design probes is resolved by 006-D.**

The current model survives materially different algorithm and runtime shapes with targeted cross-cutting refinement rather than semantic redesign.

If 006-G accepts a new concept or 006-I materially changes runtime/Strategy architecture, affected probes must be replayed conceptually before 006-J approves readiness.

## Downstream obligations

### 006-E

Validate scale/resource/backpressure/degraded behavior for:

- large/sharded Learned State;
- text model/state/tokenization workloads;
- runtime distribution/cache pressure;
- dynamic workers;
- multi-table/time-series scaling;
- statistical/approximate Evaluation.

### 006-F

Text-generation probes strengthen the need to examine memorization/disclosure-risk semantics without pretending that self-contained text generation is automatically private or safe to release.

### 006-G

Make the `Relationship`/structured-topology concept decision. No text-specific concept decision remains open.

### 006-H

Experience must eventually make self-contained/offline readiness, missing cluster closure, optional pretrained artifacts and blocked/limited runtime availability understandable to human and programmatic actors.

### 006-I

Reconcile the new closure authority into at least:

- 004-E runtime/binding architecture;
- 004-H dependency/security architecture;
- 004-I platform/deployment architecture;
- 005-C packaging/distribution planning;
- 005-F implementation-binding/runtime planning;
- 005-I dependency/security planning;
- 005-J platform/deployment planning;
- verification/fitness obligations where appropriate.

Phase history is not rewritten.

## Exit assessment

**Status: complete.**

Findings:

- algorithm/model neutrality survives the representative probes;
- baseline text-bearing synthesis must be genuinely self-contained;
- externally knowledgeable/pretrained/network text remains optional and explicit;
- no Text/LanguageModel/Distribution concept is justified;
- implementation bindings must permit multi-component executable closure;
- driver availability is not cluster readiness;
- dynamic Spark executors must inherit/prove the same compatible runtime closure;
- large model/state distribution cannot universally depend on driver memory;
- no new synchronization is required;
- BDR-003 is resolved;
- production implementation remains unauthorized.

## Next group

**006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation**.
