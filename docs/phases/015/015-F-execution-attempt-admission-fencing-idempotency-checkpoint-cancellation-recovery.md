---
type: Phase Record
title: 015-F — Execution/Attempt, Admission, Fencing, Idempotency, Checkpoint, Cancellation & Recovery
status: complete
---

# 015-F — Execution/Attempt, Admission, Fencing, Idempotency, Checkpoint, Cancellation & Recovery

## Result

~~~text
stable logical Execution                 IMPLEMENTED
subordinate distinguishable Attempts     IMPLEMENTED
Attempt epoch / current Attempt fence    IMPLEMENTED
contextual admission                     IMPLEMENTED
operation-scoped idempotent replay       IMPLEMENTED
provider-submission ambiguity            IMPLEMENTED
immutable checkpoint descriptors         IMPLEMENTED
checkpoint-qualified retry               IMPLEMENTED
durable cancellation intent              IMPLEMENTED
late provider success isolation          IMPLEMENTED
separate recovery authority              IMPLEMENTED
regressive-restore quarantine            IMPLEMENTED
fresh non-regressing frontier            IMPLEMENTED
restored Attempt fencing                 IMPLEMENTED
stale-writer rejection                   IMPLEMENTED
C5 verification                          ACTIVE / PASS

Evaluation/Evidence/Provenance            NOT IMPLEMENTED
security/disclosure policy                NOT IMPLEMENTED
provider launch adapters                  NOT IMPLEMENTED
provider guarantee qualification          NOT CLAIMED
scale certification                       NOT CLAIMED

ICLASS-3                                  0
ICLASS-4                                  0
upstream reopen                           NONE
~~~

## Implementation

015-F added:

- `syngan.domain.execution` for Execution/Attempt/admission/checkpoint operational semantics;
- `syngan.application.execution_service` for durable owner-state coordination and operation-scoped replay;
- `syngan.ports.recovery_authority` for a non-regressing recovery-frontier authority;
- `syngan.adapters.sqlite_recovery_authority` as a portable separate-failure-domain reference mechanism;
- immutable RuntimeRealizationPlan bindings for Attempts;
- durable provider-submission coordination intents;
- immutable checkpoint persistence and exact retry compatibility;
- cancellation fencing and late-provider-observation separation;
- C5 unit and file-backed recovery/integration verification.

## Authority boundaries preserved

~~~text
provider observation           != current mutation authority
provider success               != Execution completion by itself
Execution completion           != Learning/Generation/Evaluation completion
Attempt                        != provider job identity
Attempt epoch                  != sufficient regressive-recovery authority
checkpoint                     != Learned State / output / Evidence
checkpoint existence           != resume eligibility
queue/capacity                 != mutation authority
recovery-restored rows         != recreated mutation authority
late provider success          != permission to mutate fenced state
~~~

## Non-regressing recovery proof

The portable reference keeps recovery authority in a separate SQLite database from the restorable control database.

The C5 recovery test performs an actual rollback of the control database while retaining the newer recovery-authority database, then proves:

~~~text
restored control frontier < recovery authority
  -> admission = RECONCILIATION_REQUIRED
  -> fresh frontier minted above both observed values
  -> restored control store advanced to fresh frontier
  -> Execution adopts fresh frontier
  -> restored current Attempt becomes FENCED
  -> old frontier writer rejected by ControlStore
  -> later admission can proceed under the fresh frontier
~~~

Production deployments must place the equivalent recovery authority in a failure domain that is not rolled back with the protected control-state snapshot.

## Idempotency and ambiguous provider effects

A provider-submission operation uses a durable coordination intent plus operation-scoped transition identity.

Replay of the same operation returns the already-established state rather than duplicating authoritative effects.

A provider observation of UNKNOWN with no correlation leaves the submission intent pending. A later definite observation/correlation can acknowledge it. No lost acknowledgement is treated as proof of submission failure.

## Checkpoint and retry

Checkpoints retain exact:

- Execution reference;
- producing Attempt identity and epoch;
- recovery frontier;
- runtime-plan reference;
- progress scope;
- codec/integrity identity;
- material basis references.

A later retry may bind the exact checkpoint, but the reference implementation currently requires exact RuntimeRealizationPlan compatibility before allowing resume.

This deliberately favors safety over an unproven compatibility broadening rule.

## Readiness-risk disposition

### RR-03 — non-regressing recovery / stale-writer exclusion

~~~text
portable framework mechanism             IMPLEMENTED
separate recovery authority              IMPLEMENTED
regressive restore detection             VERIFIED
fresh frontier                           VERIFIED
restored Attempt fencing                 VERIFIED
old control writer rejection             VERIFIED
production failure-domain placement      DEPLOYMENT / PROVIDER QUALIFICATION
framework-level RR-03 control            COMPLETE
~~~

Provider/storage-specific durability and failure-domain claims remain part of 015-I qualification.

### RR-07 — Execution adversarial conformance

~~~text
stable Execution / multi-Attempt         VERIFIED
Attempt fencing                          VERIFIED
operation idempotency                    VERIFIED
submission ambiguity                     VERIFIED
checkpoint/retry                         VERIFIED
cancellation fencing                     VERIFIED
late provider success isolation          VERIFIED
regressive recovery                      VERIFIED
provider-specific adapter behavior       DEFERRED TO 015-I / 015-J
framework-level RR-07 control            COMPLETE
~~~

## Verification evidence

The completed executable 015-F implementation passed:

~~~text
commit        dfa22c6202054c05058108316449c6e9ac5b294f
workflow      Verify
run           35574929848

portable authority / fitness             PASS — 13
portable unit                            PASS — 37
portable fitness                         PASS — 14
control persistence                      PASS — 9
distributed data-state                   PASS — 4
Strategy runtime / Learned-State         PASS — 1
Execution / recovery                     PASS — 2
mypy                                     PASS — 38 source files
Import Linter                            PASS — 2 / 2
~~~

## Exit state

~~~text
015-A        COMPLETE
015-B        COMPLETE
015-C        COMPLETE
015-D        COMPLETE
015-E        COMPLETE
015-F        COMPLETE
015-G        NEXT ELIGIBLE / NOT AUTHORIZED
015-H..015-J NOT AUTHORIZED

IMPLEMENTATION READINESS   READY
IMPLEMENTATION START       STARTED
C5                         ACTIVE / PASS
upstream reopen            NONE
~~~

015-F does not authorize 015-G automatically.

## Full authority

See [015-F Execution / Attempt / Recovery Authority](../../implementation/phase-015-f-execution-attempt-admission-fencing-idempotency-checkpoint-cancellation-recovery-authority.md).

## Current next boundary

**015-G — Evaluation, Evidence, Provenance, Historical Read Composition & Reproducibility** is next eligible but remains **NOT AUTHORIZED** pending explicit proceed.
