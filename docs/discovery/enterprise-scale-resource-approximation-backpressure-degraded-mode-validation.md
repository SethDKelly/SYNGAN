---
type: Discovery Evidence
title: Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Validation
status: historical
---

# Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Validation

## Purpose

Preserve the Phase 006-E falsification evidence used to test whether SYNGAN's accepted concepts, synchronizations, recovery/security/runtime-closure contracts and Phase 005 planning remain coherent under enterprise-scale resource pressure and partial/degraded platform conditions.

This document is discovery evidence. Accepted authority is promoted separately.

## Method

006-E probes the design using workload shapes where one or more dimensions become difficult independently of row count:

- hundreds of millions of rows;
- very wide records;
- high-cardinality categorical/identifier fields;
- severe skew and uneven partitions;
- output larger than source;
- large/sharded Learned State;
- free-form text with large token/vocabulary/state footprints;
- dynamic Spark workers and executor churn;
- runtime/package/artifact cache pressure;
- time-series with many entities, long horizons and irregular cadence;
- multi-table parent/child fan-out and shared-key cardinality;
- exhaustive Evaluation that is expensive but semantically mandatory;
- sampled/sketched Evaluation with explicit uncertainty;
- many concurrent Learning/Generation/Evaluation activities;
- control-store, projection, telemetry, dependency, storage and accelerator degradation.

The goal is not to invent benchmark numbers. It is to determine whether scale/resource/degraded behavior requires a new concept or reveals hidden semantic degradation.

## Candidate concept review

### Resource / Capacity

Rejected as a domain concept for the current scope.

Resource capacity has no independent synthesis-domain purpose. Strategy declares requirements/limitations; Execution records operational realization/resource facts; deployment/admission policy decides current capacity. A resource reservation may be a future implementation mechanism.

### Backpressure / Queue / Admission

Rejected as a domain concept.

Backpressure controls when/how operational work may proceed. It does not own Learning, Generation or Evaluation semantics. Queueing/admission state belongs to operational realization/deployment policy and must not redefine semantic commitments.

### Approximation

Rejected as a standalone concept.

Approximation is owner-specific semantic state:

- Learning owns sampling/approximation that materially affects learned behavior;
- Generation owns approximate/best-effort output semantics only when explicitly committed;
- Evaluation owns sampling/sketching/error/coverage semantics;
- Evidence preserves the resulting claim-strength boundary.

A universal Approximation concept would erase these distinct purposes.

### Degraded Mode

Rejected as a domain concept.

Degradation is contextual capability/availability state. Different losses have different consequences: projection outage, worker loss, source unavailability, control-store outage and artifact-cache miss are not one lifecycle owned by a generic DegradedMode object.

### Cost / Budget / Quota

Rejected as a current domain concept.

Budgets/quotas may later be operator/deployment policy or product/accounting capabilities, but no independent synthesis-domain lifecycle is currently justified.

## Governing falsification rule

The central adversarial rule is:

> **Resource pressure may delay, block, retry, degrade observability, or require an explicitly different future semantic commitment, but it MUST NOT silently weaken an existing committed semantic contract.**

## Scenario matrix

### S1 — 500M narrow rows, ordinary distributed path

Expected: source remains distributed; bounded control summaries only; no full driver collection. Passes current data/runtime contracts.

### S2 — 20M extremely wide rows

Expected: Strategy readiness may be limited/incompatible due to width/model parameterization even though row count is modest. Confirms scale is multidimensional.

### S3 — high-cardinality field explodes model/state size

Expected: Strategy exposes cardinality/resource limitation; readiness may fail before expensive Learning. No implicit hashing/truncation/category collapsing if behavior would materially change semantics without explicit Strategy/configuration.

### S4 — severe Spark partition skew

Expected: repartitioning/adaptive operational tuning is permitted only when semantic/reproducibility requirements remain preserved. A hot partition does not justify dropping records or weakening scope.

### S5 — generated output exceeds source size

Expected: Generation remains distributed and quantity/scope remains authoritative. Backpressure may pause/queue/spill; it may not silently cap the output below a mandatory committed quantity.

### S6 — large/sharded Learned State

Expected: worker/direct distributed loading; cache and locality may optimize access, but full driver load/broadcast is not universal.

### S7 — large source-derived text model/vocabulary

Expected: state/tokenization footprint becomes a Strategy/runtime resource characteristic. The self-contained baseline remains valid only if package/state distribution can scale without hidden acquisition or universal driver materialization.

### S8 — executor-local artifact cache fills

Expected: cache eviction is operational. An exact artifact may be re-resolved from its approved local/private immutable source; cache miss cannot change artifact identity or trigger undeclared public acquisition.

### S9 — dynamic executor churn

Expected: new workers must inherit/prove runtime distribution closure. Work is delayed/reassigned if no compatible worker is available; commitment remains unchanged.

### S10 — cluster loses GPU capacity mid-Learning

Expected: current Attempt may fail/become recoverable; same Execution continues only if a compatible runtime/resource substitution preserves committed semantics. CPU fallback is not automatically valid if it materially changes behavior/reproducibility or violates the binding.

### S11 — time-series with millions of entities and long horizon

Expected: scale dimensions include entity cardinality, sequence-length distribution, horizon, ordering/cadence state and generated volume. The design does not centralize all series on the driver. Horizon cannot be shortened silently.

### S12 — one entity has extreme sequence length

Expected: Strategy may declare limitation or use explicit bounded/windowed semantics if committed. Truncating the outlier due to memory pressure without semantic authority is invalid.

### S13 — multi-table high fan-out

Expected: parent/child fan-out, key cardinality and coordinated component volume are scale dimensions. Child generation may be partitioned independently, but whole-result completion still applies.

### S14 — child table storage pressure

Expected: parent table completion cannot promote the Generation while mandatory child scope is incomplete. Storage pressure causes blocked/failed/recoverable operational state, not partial semantic success.

### S15 — exhaustive mandatory Constraint Evaluation is expensive

Expected: if universal satisfaction is required, resource pressure cannot silently switch to sampling. The Evaluation remains pending/blocked or a new semantically different Criterion/Evaluation policy must be chosen before commitment where allowed.

### S16 — statistical fidelity Evaluation at scale

Expected: explicit stratified/sample/sketch method is valid when committed Criterion accepts that support. Evidence preserves sample design, error and limitations.

### S17 — approximation chosen after execution starts solely to save cost

Expected: rejected if it materially changes Learning/Generation/Evaluation semantics or claim strength. Operational-only tuning may vary only inside the predeclared semantic envelope.

### S18 — concurrency saturates cluster

Expected: admission/queueing/backpressure may prioritize or defer Executions. Queue delay does not change activity semantics and does not imply failure.

### S19 — quota exceeded before Attempt starts

Expected: Execution may remain queued/blocked or admission may be rejected according to policy. Historical semantic commitment remains distinct from current capacity.

### S20 — resource capacity disappears between Attempts

Expected: same-Execution continuation is blocked until a compatible environment exists. Current capacity loss does not authorize Strategy/dependency/topology substitution.

### S21 — canonical control persistence unavailable

Expected: new canonical writes/promotions cannot be claimed. Read-only/degraded inspection may remain available only if truthful. Runtime work that cannot safely register authoritative effects must pause/fail/fence according to its contract.

### S22 — history/search projection unavailable

Expected: canonical activity may continue if it does not require projection data. History search/explain becomes unavailable or slower via canonical fallback; projection loss cannot become canonical history loss.

### S23 — telemetry exporter unavailable

Expected: canonical execution/history continues if telemetry is optional. Telemetry outage is not semantic failure unless an explicit policy makes that telemetry a required operational control.

### S24 — approved local dependency repository unavailable

Expected: new Attempts needing unresolved artifacts are blocked. Already materialized exact artifacts may remain usable if integrity/trust/authorization hold. No public fallback.

### S25 — source snapshot payload temporarily unavailable

Expected: activity cannot continue if exact input cannot be read. It must not resolve `latest` or substitute another snapshot.

### S26 — output storage temporarily unavailable

Expected: candidate writes may pause/fail; partial material remains non-final. Generation cannot claim smaller output or another location if that changes committed/security semantics without explicit requalification.

### S27 — accelerator pool only partially satisfies cluster closure

Expected: scheduler/admission may constrain work to compatible workers. An incompatible worker is ineligible rather than allowed to run a degraded implementation.

### S28 — backpressure changes partition count

Expected: allowed as operational tuning only when Strategy/reproducibility contracts state partition-count changes are semantically neutral enough. Otherwise it is a material change requiring attribution or a new commitment.

### S29 — approximate progress shows 100%

Expected: progress estimate is not semantic completion. Existing Execution/Generation/Evaluation barriers remain authoritative.

### S30 — cleanup under storage pressure

Expected: scratch/abandoned material can be policy-cleaned when safe, but payload/history/Evidence/checkpoint/reproducibility dependencies cannot be deleted merely because storage is tight. Retained identity remains distinguishable from payload availability.

## Findings

### Finding A — no new concept is justified

All probed responsibilities remain owned by Strategy, Learning, Generation, Evaluation, Evidence, Execution or deployment/security/recovery contracts. Resource/admission/degradation structures remain cross-cutting mechanisms/policies.

### Finding B — scale is part of compatibility and semantic readiness

A Strategy/method that can technically launch but requires an undisclosed single-process stage or exceeds its declared width/cardinality/state envelope is not legitimately enterprise-compatible for that workload.

### Finding C — approximation must be owner-bound

Approximation is acceptable only when its semantic owner records the scope, method, error/coverage and limitations before the corresponding semantic result relies upon it. Resource pressure is not authority to invent approximation.

### Finding D — admission is not semantic commitment

SYNGAN may preserve a committed activity while its Execution is queued or temporarily blocked by current capacity. Conversely, known impossible/incompatible resource requirements should fail readiness rather than launch expensive doomed work.

### Finding E — degraded mode is capability-specific

There is no useful global `degraded=true` semantic state. Each missing capability must expose its consequence and permitted operations. Projection loss, telemetry loss, control-store loss, dependency loss and worker loss differ materially.

### Finding F — backpressure must be lossless with respect to authority

Queueing, pausing, bounded buffering, spilling, rate limiting and worker-concurrency changes may reduce throughput but cannot silently drop logical work or mandatory output scope.

### Finding G — topology adds scale dimensions without yet forcing a topology concept

Time-series adds entity cardinality, sequence length/horizon and irregularity. Multi-table adds table count, fan-out, key cardinality and coordinated component scale. These must remain inspectable in Strategy/platform readiness whether or not 006-G accepts `Relationship`.

### Finding H — cache is never authority

Executor/node caches may accelerate exact packages/artifacts/state but cache presence/absence does not establish identity or permit fallback. Canonical binding remains the exact implementation/artifact reference.

## Proposed accepted cross-cutting rule

006-E evidence supports promotion of a cross-cutting Enterprise Scale, Resource Admission, Approximation & Degraded Operation contract with these themes:

1. enterprise compatibility is workload-profile-specific and multidimensional;
2. semantic commitments are invariant under resource pressure unless an explicit new commitment is made;
3. approximation is explicit owner-bound semantics, never hidden degradation;
4. admission/backpressure affect operational realization, not semantic ownership;
5. degraded capability must be typed and fail closed where authority/correctness is affected;
6. lossless control-plane semantics remain bounded and do not require per-row/task canonical state;
7. exact runtime/distribution closure remains required under autoscaling/churn;
8. topology-specific scale dimensions remain visible;
9. no benchmark/support threshold is asserted by design alone.

## Synchronization assessment

No new synchronization ID is justified.

Existing rules already cover the material boundaries:

- SYNC-02 / SYNC-06 — Strategy and Generation compatibility;
- SYNC-04 / SYNC-07 / SYNC-11 — operational realization/continuation under current capability;
- SYNC-08 — whole-result Generation completion;
- SYNC-10 / SYNC-12 — Evaluation method compatibility and Evidence claim strength;
- SYNC-14 / SYNC-15 — material scale/runtime/approximation attribution where required.

No canonical synchronization wording change is required solely from 006-E; 006-I should ensure architecture/planning realizes the new cross-cutting contract.

## Exit evidence

The tested design passes enterprise-scale/resource/degraded-mode falsification with targeted cross-cutting refinement. No production implementation or benchmark evidence exists yet.