---
type: Implementation Authority
title: 015-F — Execution/Attempt, Admission, Fencing, Idempotency, Checkpoint, Cancellation & Recovery
status: complete-current
---

# 015-F — Execution/Attempt, Admission, Fencing, Idempotency, Checkpoint, Cancellation & Recovery

## Purpose

Implement the provider-neutral operational-authority spine for committed Learning, Generation, or Evaluation work while preserving owner-controlled semantic completion.

015-F owns:

- one stable logical Execution per operationalized committed activity;
- subordinate distinguishable Attempts;
- contextual admission with cause-preserving outcomes;
- Attempt epoch plus current recovery-frontier fencing;
- operation-scoped idempotent control transitions;
- durable provider-submission intent and ambiguous-effect observation;
- immutable checkpoint descriptors and contextual resume authority;
- durable cancellation intent and stale-effect fencing;
- a separate non-regressing recovery-authority reference mechanism;
- explicit reconciliation after potentially regressive control-state restore;
- C5 failure/recovery verification.

015-F does not implement Evaluation/Evidence/Provenance, authorization/disclosure policy, provider capability qualification, provider launch adapters, or scale certification.

## Governing rule

~~~text
provider observation
  != current mutation authority
  != operational outcome
  != parent semantic completion
~~~

Material framework mutation requires current control-store recovery frontier plus current Execution/Attempt authority. Attempt epoch alone is insufficient after potentially regressive restore.

## Recovery authority

The portable reference uses a recovery-authority store that is physically/logically separate from the restorable control store.

A potentially regressive restore follows:

~~~text
detect recovery-authority / control-frontier mismatch
-> block ordinary admission
-> establish a fresh frontier in the non-regressing authority
-> advance restored control persistence to that frontier
-> reconcile each Execution to that same frontier
-> fence restored current Attempts
-> permit later admission under new authority
~~~

The separate recovery-authority store is a reference mechanism. Operational deployments must place equivalent authority in a failure domain that is not rolled back with the restored control snapshot.

## Idempotency

State-changing application operations use operation-scoped transition identities. Repeating the same transition identity resolves the already-established state rather than duplicating authoritative effects.

External provider submission uses a durable coordination intent. A lost acknowledgement remains pending/unknown; it is not treated as proof that submission failed.

## Checkpoints

A committed checkpoint is immutable operational recovery state. It binds exact Execution/Attempt authority, runtime-plan identity, progress scope, codec/integrity identity, and material basis references.

Checkpoint existence does not imply current resume eligibility, Execution completion, Learned State, Generation output, or Evidence.

## Cancellation

Cancellation is durable intent. Once accepted, current Attempt mutation authority is fenced and ordinary new Attempt admission is blocked.

Late provider success remains historical provider observation only.

## Verification

015-F activates C5 and must include deterministic/unit plus file-backed failure/recovery tests, including:

- one stable Execution with multiple Attempts;
- stale Attempt epoch rejection;
- stale recovery-frontier rejection;
- idempotent replay of control operations;
- lost provider-ack ambiguity;
- checkpoint commit under current authority;
- checkpoint rejection from stale authority;
- cancellation fencing and late provider success;
- regressive control-store restore detected by separate recovery authority;
- fresh frontier establishment;
- restored Attempt fencing;
- old writer rejection after recovery.

## Entry authorization at 015-F start

~~~text
015-A        COMPLETE
015-B        COMPLETE
015-C        COMPLETE
015-D        COMPLETE
015-E        COMPLETE
015-F        AUTHORIZED / ACTIVE
015-G..015-J NOT AUTHORIZED
IMPLEMENTATION START STARTED
~~~

This block records the slice-entry authorization. The current post-completion authorization state is recorded below.


## Completion evidence

015-F now implements the provider-neutral framework operational spine with a separate recovery-authority reference mechanism.

~~~text
stable Execution / subordinate Attempts       IMPLEMENTED
admission cause preservation                  IMPLEMENTED
Attempt + recovery-frontier fencing           IMPLEMENTED
operation-scoped idempotency                  IMPLEMENTED
provider submission ambiguity                 IMPLEMENTED
immutable checkpoints / exact retry basis     IMPLEMENTED
cancellation fencing                          IMPLEMENTED
non-regressing recovery authority             IMPLEMENTED
regressive restore / stale-writer proof       VERIFIED
C5                                             ACTIVE / PASS

commit                                         dfa22c6202054c05058108316449c6e9ac5b294f
workflow run                                   35574929848
~~~

RR-03 and RR-07 framework-level controls are complete. Provider/storage-specific qualification remains assigned to 015-I and final adversarial consolidation to 015-J.

## Current authorization state

~~~text
015-A        COMPLETE
015-B        COMPLETE
015-C        COMPLETE
015-D        COMPLETE
015-E        COMPLETE
015-F        COMPLETE
015-G        NEXT ELIGIBLE / NOT AUTHORIZED
015-H..015-J NOT AUTHORIZED
IMPLEMENTATION START STARTED
~~~

## Current next boundary

**015-G — Evaluation, Evidence, Provenance, Historical Read Composition & Reproducibility** is next eligible but remains **NOT AUTHORIZED** pending explicit proceed.
