
---
type: Implementation Authority
title: 015-G — Evaluation, Evidence, Provenance, Historical Read Composition & Reproducibility
status: active-current
---

# 015-G — Evaluation, Evidence, Provenance, Historical Read Composition & Reproducibility

## Purpose

Implement the current Evaluation/Evidence/Provenance/history/reproducibility architecture while preserving owner boundaries established by Phase 013 and verified by Phase 014.

015-G owns:

- Evaluation semantic lifecycle and completion validity;
- immutable Evidence finding establishment;
- mutable Evidence applicability without rewriting historical findings;
- typed canonical Provenance assertions over exact references;
- append/supersede/invalidate Provenance correction state;
- exact historical read composition with independent knowledge-basis and object-resolution axes;
- qualified derived reproducibility assessment;
- C6 verification.

015-G does not implement current actor authorization/disclosure, external release/use governance, provider/platform qualification, or scale certification.

## Governing rules

~~~text
runtime/platform success != Evaluation semantic completion
Evaluation completion    != favorable finding
Evidence                  != approval / release authorization
Provenance                != referenced owner state
projection miss           != historical absence
current unavailability    != rewritten historical fact
Reproducibility           != canonical Boolean state
~~~

## Evaluation

A committed Evaluation binds exact Criterion, subject, method and optional baseline/reference identities.

Completion requires:

- exact committed identities to match the normalized result;
- interpretable result semantics;
- valid material assumptions;
- explicit claim-strength support;
- one or more independently interpretable Evidence findings.

Failed/cancelled/semantically uninterpretable Evaluation may establish no Evidence.

Negative, unfavorable and indeterminate findings remain valid Evidence when the examination itself was semantically valid.

## Evidence

Each Evidence finding is immutable and independently identifiable.

Its immutable payload includes exact producing Evaluation, exact Criterion, exact subject, result, scope, method, claim strength, uncertainty, limitations and material reference/baseline identities.

Mutable applicability is maintained separately as owner state:

~~~text
applicable
superseded
stale
inapplicable
invalidated
~~~

Changing applicability never rewrites the original finding.

Stable finding identity is deterministic from the exact Evaluation plus finding slot, so replay is idempotent and conflicting reuse becomes a consistency defect.

## Generation completion handoff

015-G does not move Generation authority into Evidence.

The existing Generation-owned completion basis remains authoritative. 015-G supplies exact Evidence references plus current applicability for owner-side sufficiency decisions.

A later Evidence invalidation changes current reliance but does not rewrite a historical Generation completion basis.

## Provenance

Provenance assertions are immutable typed relationship facts over exact references.

Current assertion status is separate:

~~~text
active
superseded
invalidated
~~~

Historical knowledge basis is explicit:

~~~text
direct
reconstructed
partial
~~~

No generic related-to edge is used where relationship semantics affect interpretation.

## Historical read composition

Historical read composition preserves two independent dimensions:

~~~text
knowledge basis:
  direct / reconstructed / partial / unknown

current resolution:
  resolved / known-unavailable / unknown / invalid / withheld
~~~

015-G itself does not decide WITHHELD; 015-H authorization/disclosure may produce that later.

A missing immutable payload in the control store is treated as UNKNOWN unless canonical absence is independently established. It is not silently treated as historical nonexistence.

## Reproducibility

Reproducibility is a derived assessment only.

The portable model preserves three independent axes:

~~~text
historical supportability
current feasibility
actor-visible assessability
~~~

Supported historical classes are equivalent to:

~~~text
exact-deterministic
semantic
statistical
bounded-approximate
comparative
not-reproducible
~~~

The assessment never creates a canonical Reproducibility resource or active synchronization.

## Verification

015-G activates C6 and must verify at least:

- Evaluation valid completion vs failure/cancellation;
- negative/indeterminate Evidence remains valid;
- unsupported claim strength is rejected;
- stable finding-slot idempotency and conflicting replay detection;
- immutable Evidence vs mutable applicability;
- multiple Evidence findings from one Evaluation;
- required Evaluation->Evidence / Criterion / subject Provenance;
- Provenance reconstruction/correction status;
- historical knowledge basis independent from current resolution;
- current unavailable payload does not rewrite history;
- Evidence used in Generation completion remains exact after later invalidation;
- reproducibility supportability distinct from feasibility/assessability;
- no canonical Reproducibility state.

## Current authorization state

~~~text
015-A        COMPLETE
015-B        COMPLETE
015-C        COMPLETE
015-D        COMPLETE
015-E        COMPLETE
015-F        COMPLETE
015-G        AUTHORIZED / ACTIVE
015-H..015-J NOT AUTHORIZED
IMPLEMENTATION START STARTED
~~~
