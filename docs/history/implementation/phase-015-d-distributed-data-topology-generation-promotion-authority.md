
---
type: Implementation Authority
title: 015-D — Distributed Data-State, Structured Topology, Candidate/Seal & Generation Promotion
status: complete-current
---

# 015-D — Distributed Data-State, Structured Topology, Candidate/Seal & Generation Promotion

## Purpose

Implement the provider-neutral distributed-data control-plane foundation required to identify exact physical subjects, represent structured topology, track Generation candidates, seal immutable physical subjects, and establish one Generation-owned completed-output binding without copying distributed payloads into the control plane.

015-D implements architecture roles, not new concepts.

## Governing authority

Primary current authority:

- Phase 013-D distributed-data/topology/candidate/promotion reconciliation;
- Spark Data Boundary / Manifest / Promotion architecture;
- Phase 013-C control-persistence reconciliation;
- current Generation concept and synchronization authority;
- completed 015-C identity/reference/control persistence;
- completed 015-B verification authority.

Historical Phase 007-F remains rationale evidence only.

## Scope

015-D may implement:

- bounded logical-scope/topology representation;
- exact semantic/topology bindings by reference;
- provider-neutral physical-scope bindings;
- multidimensional physical-subject strength;
- immutable sealed physical-subject representation;
- Generation candidate state subordinate to Generation;
- Generation-owned zero-or-one completed-output promotion;
- persistence of Generation data-state through the 015-C ControlStore port;
- C3 verification and a required data-state integration profile.

015-D may not implement:

- Spark/provider runtime writers;
- Strategy or Learning/Learned-State runtime behavior;
- Execution/Attempt scheduling, checkpoint, cancellation or recovery;
- actual provider capability qualification;
- Evaluation/Evidence/Provenance behavior;
- authorization/disclosure/security;
- enterprise-scale qualification.

## Core authority separation

~~~text
physical subject existence/readability/seal
  != Generation semantic completion

topology representation
  != Data Meaning relationship semantics

candidate state
  != completed output

provider/storage success
  != Generation promotion

completed output
  != external release/use approval
~~~

## Concrete implementation model

### Logical topology

A TopologyDescriptor contains:

- bounded logical scopes;
- exact semantic bindings that remain owned by their referenced authorities;
- optional convenience topology hints;
- whether the committed subject requires a coordinated cross-scope cut.

Topology hints are descriptive convenience only. Exact scope composition plus exact referenced authority remains the durable basis.

### Physical subject

A sealed physical subject uses:

- an exact TypedReference bound by CommitmentSnapshotId;
- one bounded physical binding per logical scope;
- opaque physical locator and immutable/version token;
- optional bounded structural/extent summaries;
- five independent strength dimensions:
  - identity;
  - exact read binding;
  - integrity/membership closure;
  - retention/resolvability;
  - cross-scope coordination.

A sealed subject requires exact identity and read binding plus closed-root-or-stronger integrity. A topology that requires coordinated cut also requires coordinated cross-scope strength.

This does not imply provider or enterprise support.

### Generation candidate aggregate

One Generation data-state aggregate contains bounded candidate metadata and zero or one completed-output binding.

Candidate states are subordinate Generation representation states:

~~~text
OPEN
SEALED
QUARANTINED
ABANDONED
PROMOTED
~~~

Multiple candidates may exist over Generation history. Only one may become the successful completed output.

### Promotion

Promotion is a Generation-owned metadata/control transition.

It:

- requires a sealed candidate;
- requires the exact immutable sealed-subject binding to be resolvable;
- may retain exact owner-approved completion-basis references;
- establishes one completed-output logical identity;
- does not copy physical data;
- does not infer Condition/Constraint/Evidence validity from physical seal;
- cannot be repeated to create a second authoritative completed output.

Later 015-G work may supply Evidence into the exact completion-basis reference set when the Generation is evidence-gated.

## Persistence strategy

015-D reuses the 015-C ControlStore port.

Generation data-state is persisted as opaque owner payload under the Generation ResourceKey with CAS/history semantics.

Sealed physical-subject descriptors are persisted as immutable bindings using exact CommitmentSnapshotId references.

This keeps:

~~~text
Generation semantic/data-state ownership -> Generation domain/application implementation
durability/concurrency/history             -> ControlStore
physical distributed payload              -> outside control store
~~~

A failed Generation-state CAS after immutable subject insertion may leave an unpromoted immutable physical subject. That is permissible; physical existence is not semantic completion and later reconciliation may inspect it.

## Large-state boundary

015-D must never require:

- row-level control records;
- entity/series-level canonical resources;
- file-by-file canonical control rows;
- full-corpus collect/toPandas;
- whole-payload copying during promotion.

The portable implementation stores only bounded descriptors and exact root/scope bindings.

## Verification activation

015-D activates C3.

~~~text
C0  ACTIVE
C2  ACTIVE
C3  ACTIVE — distributed-data/topology/physical-subject/promotion foundation
C1,C4-C9 DEFINED
~~~

A new required `data` profile will exercise portable C3 unit/integration behavior after the existing portable and control gates.

C3 acceptance covers:

1. bounded topology with unique scopes;
2. exact semantic binding requirements;
3. single-scope/time-series/multi-scope/composite representability;
4. physical-scope coverage without per-row/file expansion;
5. independent strength dimensions;
6. weak subject rejection at seal boundary;
7. coordinated-cut requirement enforcement;
8. exact sealed-subject immutable persistence;
9. multiple Generation candidates with zero-or-one promotion;
10. open/sealed-but-unpromoted candidates never exposed as completed result;
11. metadata-only promotion retaining the sealed subject;
12. durable reopen and exact completed-output binding;
13. stale Generation-state CAS rejection;
14. physical immutable-binding conflict detection.

## Historical choice disposition

~~~text
literal manifest object                 NOT REQUIRED
provider-native immutable snapshot      PERMITTED LATER
bounded root/scope descriptor           RETAIN
exclusive topology enum as authority    REJECT
one control row per file/row/entity     REJECT
data copy on promotion                  REJECT
provider success as completion          REJECT
Spark/provider dependency               DEFER TO 015-E/015-I
portable Parquet profile                DEFER
~~~

## Completion evidence

~~~text
bounded logical topology                         IMPLEMENTED
exact Data Meaning revision coverage             IMPLEMENTED
provider-neutral physical scope binding          IMPLEMENTED
multidimensional physical-subject strength       IMPLEMENTED
coordinated-cut qualification                    IMPLEMENTED
immutable sealed physical-subject binding        IMPLEMENTED
Generation multiple-candidate state              IMPLEMENTED
sealed/unpromoted != completed output             ENFORCED
zero-or-one Generation completed output           ENFORCED
metadata-only promotion                           IMPLEMENTED
durable reopen / exact completed-output binding   PASS
C3 data verification                              PASS
provider/Spark runtime                            NOT IMPLEMENTED
enterprise scale qualification                    NOT CLAIMED
RR-03 non-regressing recovery                     DEFERRED TO 015-F
RR-04 provider qualification                      DEFERRED TO 015-I
RR-05 no-egress runtime closure                   DEFERRED TO 015-E / 015-H
RR-06 scale qualification                         PARTIAL FOUNDATION ONLY
ICLASS-3                                          0
ICLASS-4                                          0
upstream reopen                                   NONE
~~~

Verification evidence:

~~~text
commit        aed1cea3da28d9cea76b35196010e186d34e76b1
workflow      Verify
run           35559547390
portable      PASS
control       PASS — 9 / 9 integration tests
data          PASS — 4 / 4 integration tests
portable unit PASS — 23 / 23
C3 unit       PASS — 11 / 11
Import Linter PASS — 2 / 2 contracts kept
~~~

The C3 data gate proves the provider-neutral control-plane foundation only. It does not establish Spark/provider support, no-egress closure, non-regressing recovery, or enterprise-scale qualification.

## Current authorization

~~~text
015-A        COMPLETE
015-B        COMPLETE
015-C        COMPLETE
015-D        COMPLETE
015-E        NEXT ELIGIBLE / NOT AUTHORIZED
015-F..015-J NOT AUTHORIZED
IMPLEMENTATION START  STARTED
~~~

## Current next boundary

**015-E — Strategy/Method Binding, Dependency Closure, Learning/Learned-State & Generation Runtime** is next eligible but remains **NOT AUTHORIZED** pending explicit proceed.
