---
type: Design Authority
title: Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract
status: active
---

# Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract

## Purpose

Define cross-cutting design rules for enterprise-scale workload compatibility, resource admission/backpressure, explicit approximation and degraded operation without allowing infrastructure pressure to silently redefine Learning, Generation, Evaluation, Evidence or Execution semantics.

This contract is **not** a new domain concept. It constrains Synthesis Strategy capability declarations, activity readiness/commitment, Execution, runtime/platform admission, Evaluation/Evidence claim strength, cleanup/retention and operator/programmatic degraded-state behavior.

## Governing rule

> **Resource pressure may delay, block, queue, retry, reduce observability, or require an explicitly different future semantic commitment, but it MUST NOT silently weaken an existing committed semantic contract.**

## Scale is multidimensional

Enterprise compatibility MUST be assessed against the material workload dimensions rather than one row-count label.

Where relevant, the workload/profile includes at least:

- rows and bytes;
- field/column width and nested/value size;
- categorical/key/token cardinality;
- skew, rare-event structure and partition imbalance;
- source and generated partition counts;
- output-to-source expansion ratio;
- Learned-State/checkpoint/model/tokenizer size;
- worker/executor/accelerator memory and count;
- shuffle/network/storage pressure;
- time-series entity count, sequence-length distribution, horizon/cadence/irregularity;
- multi-table table count, shared-key cardinality and parent/child fan-out;
- Evaluation population size, coverage method and diagnostics volume;
- concurrency and competing workload pressure;
- external dependency/service throughput where allowed.

A platform or Strategy that works for many narrow rows may be incompatible with fewer extremely wide/high-cardinality rows. `supports N rows` is not a complete design or support claim.

## Enterprise-compatibility rule

A Strategy/method/runtime profile is enterprise-compatible only when its material scale/resource assumptions remain within its declared supported envelope and no undisclosed source-size-proportional single-process/driver stage is required for the ordinary path.

Known scale cliffs MUST be visible during readiness/compatibility assessment where they can be established before commitment or expensive execution.

An implementation running inside Spark does not itself prove enterprise scalability.

## Control-plane boundedness

Canonical semantic/control state SHOULD scale with logical resources, revisions, Attempts, checkpoints, bounded summaries, Evidence and references—not with every source row, generated row, token, task, tensor, file, log event or metric sample.

Detailed distributed data and telemetry remain data-plane/platform concerns unless a bounded canonical fact is required for authority, recovery, Evidence, Provenance or reproducibility.

No ordinary enterprise operation may require collecting the entire source/output, all model state, or all task telemetry into the driver merely to maintain semantic/control correctness.

## Resource admission

Resource admission is contextual operational/deployment policy, not a new semantic owner.

Before or between Attempts, current readiness MAY determine that an Execution is:

- runnable now;
- runnable with explicitly permitted operational limitations;
- queued/deferred for capacity;
- blocked by unavailable resources/dependencies;
- incompatible with the current deployment;
- indeterminate because required capability facts cannot be established.

Exact labels are downstream representation choices.

### Known impossible work

When a declared Strategy/method requirement is known to exceed current supported capability or violate a committed deployment/security profile, readiness SHOULD reject/block rather than launch predictably invalid work merely to discover the same limitation after expensive computation.

### Queueing does not rewrite commitment

A committed Learning/Generation/Evaluation may remain semantically committed while Execution waits for resources.

Queue delay, quota pressure or capacity shortage does not by itself create a new Strategy, Generation scope, Evaluation method or semantic failure.

## Backpressure

Backpressure may be realized through mechanisms such as:

- queueing;
- pausing;
- rate limiting;
- bounded buffers;
- spilling;
- reduced operational concurrency;
- partition/task rescheduling;
- flow-control between runtime stages;
- compatible worker-count changes.

These are downstream mechanisms.

### Lossless authority rule

Backpressure MUST NOT silently:

- drop required records/work units;
- truncate committed Generation quantity/scope;
- omit mandatory table/sequence constituents;
- skip required Constraint/Evaluation coverage;
- discard Evidence-supporting facts required by the committed method;
- substitute a different dependency/model/Strategy;
- relax security/no-egress requirements;
- convert unknown/unavailable state into success.

If a mechanism cannot preserve the committed contract, execution becomes blocked/failed/limited according to the owning semantics rather than silently degrading the result.

## Approximation ownership

Approximation is not one generic lifecycle.

Material approximation belongs to the concept whose semantics it changes:

- **Learning** — sampling, sketching, truncation/windowing or approximate training state that affects learned behavior;
- **Generation** — best-effort/tolerance/approximate quantity or synthesis behavior only when explicitly part of the committed Generation semantics;
- **Evaluation** — sample/sketch/bounded/approximate method, coverage, error and uncertainty semantics;
- **Evidence** — preserves the supported claim strength/limitations produced by the Evaluation.

Operational tuning that is demonstrably semantics-neutral may vary between Attempts, but a material approximation change is not merely resource tuning.

## No hidden approximation under pressure

Resource exhaustion, cost pressure, runtime duration or queue congestion MUST NOT automatically convert:

- exhaustive Evaluation → sampled Evaluation;
- full committed horizon → truncated time-series horizon;
- full multi-table scope → partial constituent output;
- exact dependency/model → cheaper substitute;
- required universal Constraint validation → probabilistic assumption;
- committed source population → convenience sample;
- requested quantity → smaller best-effort result;

unless the owning semantic specification explicitly permits that alternative and the actual behavior remains bound/attributable.

If a materially weaker plan is desired after commitment, the owning concept determines whether a new activity/commitment is required.

## Evaluation and claim strength under scale

Scale pressure never authorizes Evidence to exceed methodological support.

If an exhaustive Criterion cannot be evaluated exhaustively with available resources, valid outcomes include:

- remain queued/blocked;
- fail the Evaluation;
- choose a different Criterion/Evaluation before commitment where policy permits;
- run an explicitly statistical/approximate Evaluation whose weaker Evidence is truthful.

It is invalid to run a sample and present it as universal proof merely because exhaustive evaluation was expensive.

Statistical/sketch methods remain first-class when their scope, sampling/approximation design, error/uncertainty and limitations are explicit.

## Time-series scale consequences

Time-series workload readiness must be able to consider material dimensions including:

- number of series/entities;
- distribution of sequence lengths;
- requested generation horizon;
- temporal resolution/cadence;
- irregular/missing intervals;
- history/context window requirements;
- temporal state size;
- cross-series/global-state requirements;
- partitioning/locality requirements.

A long or anomalous sequence MUST NOT be silently truncated because of memory pressure unless truncation/windowing is explicit Strategy/Learning/Generation semantics.

This contract does not decide whether reusable sequence structure becomes a `Relationship` concept; 006-G owns that question.

## Multi-table scale consequences

Multi-table readiness must be able to consider material dimensions including:

- number of participating tables/scopes;
- shared-key cardinality;
- parent/child fan-out and skew;
- per-table and total generated volume;
- cross-scope Constraint/Evaluation cost;
- coordinated output/materialization pressure.

A constituent table may be produced or retried independently operationally, but whole-result completion remains governed by SYNC-08.

Storage/capacity pressure MUST NOT make a mandatory child table optional after commitment.

## Text/model/state resource consequences

Text-bearing Strategies may have material resource characteristics including:

- token/vocabulary cardinality;
- sequence length;
- learned text-state size;
- tokenizer/configuration size;
- optional pretrained artifact size;
- accelerator/native runtime requirements;
- executor-local/shared cache pressure.

The self-contained baseline remains self-contained only when these dependencies satisfy the [Self-Contained Execution & Runtime Distribution Closure Contract](self-contained-execution-runtime-distribution-closure-contract.md).

Large state/artifacts must support scalable distributed resolution/loading; universal driver-load-and-broadcast is not required or accepted.

## Cache semantics

Worker/node/local caches are performance mechanisms, not canonical identity or dependency authority.

A cache hit MAY satisfy access to an exact already-authorized artifact/state when identity/integrity remain established.

A cache miss MAY re-resolve that exact artifact from an approved local/private source when permitted.

A cache miss MUST NOT justify:

- public-network acquisition under a closed/offline profile;
- `latest` substitution;
- a different model/tokenizer/package;
- unverified bytes;
- cross-tenant/security-domain leakage.

Cache eviction therefore affects performance/availability, not historical identity.

## Dynamic workers and resource churn

Autoscaling, worker replacement and resource churn MUST preserve runtime distribution closure.

A newly admitted worker is eligible for material work only when its exact required executable/artifact/runtime closure and current authorization are compatible.

If compatible workers are temporarily unavailable, work may queue/retry/fail according to Execution policy. The system MUST NOT admit an incompatible worker merely to maintain throughput.

Worker-count changes may be treated as operational tuning only when they remain inside the Strategy/method reproducibility and semantic envelope.

## Degraded operation is typed

There is no universal `degraded=true` authority state.

The effect of degradation depends on what capability is unavailable.

### Canonical persistence unavailable

If a required canonical transition cannot be durably established, SYNGAN MUST NOT report that transition as committed.

Read-only inspection may remain available only when served truthfully from sufficiently authoritative state.

### Projection/search unavailable

Canonical activity may continue when projection data is not required for correctness. Search/explain/history convenience may become unavailable or fall back to canonical reads where supported.

Projection loss does not mean canonical history loss.

### Telemetry unavailable

Loss of optional telemetry/log export may reduce observability but does not automatically invalidate semantic work.

If deployment policy declares a particular audit/monitoring capability mandatory for protected execution, readiness/continuation must respect that policy explicitly.

### Dependency/artifact source unavailable

New Attempts requiring unresolved dependencies are blocked. Already materialized exact artifacts may remain usable only when identity, integrity, trust and authorization remain valid.

No undeclared public fallback is allowed.

### Source/reference unavailable

An activity requiring an exact source/reference cannot continue by resolving a mutable `latest` or alternate snapshot.

### Output/checkpoint storage unavailable

Writes may block/fail/recover. Partial material remains non-final. The system cannot silently reduce required output scope or claim a checkpoint/result that was not durably established.

### Worker/accelerator unavailable

Execution may queue, retry or use another compatible resource profile only if the substitution preserves the exact committed/runtime-binding contract. A materially different runtime behavior is not an automatic fallback.

### Security/authorization unavailable or indeterminate

Protected actions fail closed according to current security authority.

## Partial capability and explicit limitation

A deployment may support some Strategies/workloads but not others.

`limited` support is legitimate only when the limitation is explicit and does not misrepresent semantic guarantees.

A capability limitation cannot be used as permission to weaken:

- Data Meaning;
- Constraints;
- Generation Conditions/scope;
- Evaluation Criteria/claim strength;
- historical identity;
- fencing/recovery safety;
- no-egress/security requirements.

Where a semantics-preserving fallback exists, it must be explicit. Otherwise the workload is incompatible/blocked/indeterminate.

## Progress and estimates

Progress, throughput, ETA, resource-utilization and queue-position observations are operational estimates unless the owning domain explicitly defines stronger semantics.

`100% tasks`, `100% partitions`, or `100% estimated progress` MUST NOT establish Learning, Generation or Evaluation semantic completion.

Approximate progress must remain distinguishable from exact completion/accounting.

## Cleanup and retention under pressure

Storage pressure does not override authority-aware retention.

Cleanup MAY remove disposable scratch, abandoned/quarantined material, expired caches and telemetry according to policy when doing so cannot invalidate required recovery/history/security/Evidence/reproducibility obligations.

Cleanup MUST NOT silently remove material still required by:

- a promoted Generation Output;
- usable Learned State;
- valid checkpoint/recovery path;
- Evidence support/diagnostics retained by policy;
- canonical history/Provenance requirements;
- reproducibility/retention commitments;
- security/audit requirements.

When payload legitimately expires while identity/history remains, the system preserves `known identity, payload unavailable` rather than collapsing to `absent`.

## Concurrency, quotas and fairness

Multiple independent activities may compete for resources.

Scheduling priority, fairness, quotas, budgets and admission policies are deployment/operator concerns unless a future product purpose justifies separate concept discovery.

They MUST NOT introduce global mutable runtime state that makes unrelated Executions semantically interfere with one another.

A quota/capacity decision can block execution without rewriting the committed activity.

## Reproducibility consequences

Material scale/runtime facts that can change behavior must remain attributable according to SYNC-15, such as where relevant:

- worker/accelerator topology;
- partitioning;
- approximation/sampling plan;
- checkpoint/resume;
- runtime/resource substitution;
- artifact/cache resolution basis when behaviorally material.

Operational changes may still support semantic/statistical/bounded reproducibility even when physical topology differs. Exact deterministic claims require stronger evidence.

## Synchronization consequence

This contract constrains existing synchronizations rather than introducing a new synchronization ID.

Most relevant:

- SYNC-02 — Strategy compatibility;
- SYNC-04 / 07 / 11 — current operational continuation qualification;
- SYNC-06 — Generation commitment/compatibility;
- SYNC-08 — whole logical-output completion;
- SYNC-10 / 12 — Evaluation method compatibility and Evidence claim strength;
- SYNC-14 / 15 — material historical/reproducibility attribution.

006-E does not create `SYNC-16` or another synchronization.

## Architecture/planning consequence

006-I must reconcile this contract into relevant architecture and Phase 005 planning, especially:

- runtime/Strategy binding resource envelopes;
- distributed data/state/materialization paths;
- Execution admission/retry/backpressure;
- Evaluation method/coverage planning;
- dependency/runtime distribution closure;
- platform capability assessment;
- scale/benchmark verification;
- retention/degraded-read behavior.

This authority does not itself select schedulers, autoscalers, caches, spill mechanisms, quota systems, benchmark thresholds or hardware profiles.

## Invariants

1. Enterprise-scale compatibility MUST be multidimensional and workload-specific.
2. An undisclosed source-size-proportional single-process/driver stage invalidates an enterprise-scale claim for that path.
3. Resource pressure MUST NOT silently weaken committed semantic requirements.
4. Material approximation MUST be explicit and owned by the concept whose semantics it changes.
5. Backpressure/admission may delay or block work but MUST NOT silently drop mandatory logical work/scope.
6. A sampled/sketched Evaluation MUST NOT become universal Evidence merely because exhaustive evaluation is expensive.
7. Whole-result completion remains authoritative under time-series/multi-table partial pressure.
8. Cache presence/absence MUST NOT redefine exact artifact/runtime identity.
9. Dynamic workers MUST preserve runtime distribution closure before executing material work.
10. Degraded operation MUST be capability-specific; a global degraded flag MUST NOT erase important distinctions.
11. Loss of projection/telemetry MUST NOT become loss of canonical semantic/history authority.
12. Canonical persistence failure MUST prevent uncommitted transitions from being reported as committed.
13. Exact source/reference unavailability MUST NOT trigger `latest` or substitute resolution.
14. Partial output/checkpoint material MUST remain non-final under storage/resource failure.
15. Security/authorization uncertainty MUST fail closed for protected actions.
16. Progress/ETA/resource estimates MUST NOT establish semantic completion.
17. Storage pressure MUST NOT violate authority-aware retention obligations.
18. No design-time row-count band is a benchmark/support guarantee.
19. No rule in this contract makes Spark scheduling, Kubernetes, Databricks, a quota product, autoscaler, cache or benchmark framework universal SYNGAN semantics.

## Operational principle

A Generation committed to produce a complete multi-table synthetic result is queued because the cluster is saturated. When capacity becomes available, its Execution starts on workers that satisfy runtime-distribution closure. During generation, a child-table stage encounters storage backpressure. The runtime pauses/spills/retries rather than dropping child records or promoting only the parent table. The Generation remains incomplete until the whole committed scope is materialized and validated.

A required universal referential-integrity Evaluation is too expensive for the temporarily available cluster. SYNGAN does not silently sample it. The Evaluation remains queued/blocked until compatible resources are available, or an actor deliberately creates a different statistical Criterion/Evaluation when such weaker assurance is acceptable. Any resulting Evidence remains bounded to its actual method and coverage.
