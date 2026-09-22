---
type: Implementation Qualification Authority
title: v0.x MVP Completion Testing, Qualification & Independent Exit Method
status: active
---

# v0.x MVP Completion Testing, Qualification & Independent Exit Method

## Purpose

Define the exact qualification method that Phase 025 must use to decide whether the frozen v0.x
package-MVP candidate satisfies the bounded MVP contract.

This authority specializes the implementation phase lifecycle, split-visibility evaluation method,
v0.x MVP boundary, and Phase 018-025 implementation program.

It defines qualification mechanics and evidence sufficiency. It does not create product semantics,
authorize implementation, authorize Phase 025, create a release candidate, or add provider/scale
claims.

## Core rule

MVP qualification is **non-compensatory by blocking obligation**.

~~~text
many passing tests
  != permission to ignore one failed blocking obligation

high coverage
  != permission to ignore a recovery defect

high mutation score
  != permission to ignore a security defect

successful reference path
  != provider qualification
~~~

Every blocking MVP obligation must be individually traceable to sufficient evidence and an
independent qualification disposition.

Aggregate metrics may diagnose evidence quality. They may not override a blocking failure.

## Qualification subject

Phase 025 evaluates exactly one frozen Phase 024 package-MVP candidate at a time.

The qualification subject includes:

- exact candidate commit;
- exact package/build identity;
- exact non-placeholder v0.x candidate version;
- frozen Phase 024 candidate record;
- frozen Phase 025 qualification plan;
- frozen visible success/obligation inventory;
- declared support boundary and non-claims;
- environment identities used by qualification.

Any product change creates a new candidate.

The evaluator may inspect evidence and execute tests/challenges. The evaluator may not modify the
candidate while certifying it.

## Phase 025 qualification-plan freeze

Before independent H1 realization is selected or generated, the Phase 025 start gate must freeze a
qualification plan containing at least:

1. exact candidate identity;
2. all MVP-C01 through MVP-C08 capability mappings;
3. the lower-level blocking V0 obligations inherited from completed implementation phases;
4. blocking versus non-blocking disposition for every qualification obligation;
5. required E0-E4 evidence dimensions;
6. applicable CH-01 through CH-08 challenge families;
7. evaluator independence target;
8. property/generative budgets;
9. mutation operator classes and selected mutation scope;
10. fault/recovery/interleaving challenge budget;
11. environments and clean-install profiles;
12. replay/provenance capture requirements;
13. any frozen thresholds that are actually normative;
14. evidence-reuse assumptions;
15. explicit E5 exclusions/non-claims;
16. decision rule and carry-forward rules.

The plan may compile existing obligations into a qualification matrix. It may not invent a hidden
blocking requirement.

Challenge budgets and thresholds cannot be reduced after a failure merely to obtain a pass.

## Required qualification layers

### QL-01 — candidate identity, authority, and freeze integrity

Evidence:

- exact commit/build/version identity;
- Phase 024 candidate-freeze record;
- stable authority resolution;
- qualification-plan identity;
- evaluator context/independence declaration.

Primary evidence dimensions: E0, E4.

### QL-02 — traceability, blocking-obligation, and non-claim closure

Every blocking qualification obligation must map to:

- governing current authority;
- implementation/package realization;
- verification evidence;
- MVP capability supported;
- support claim permitted;
- explicit non-claims and residuals.

Primary evidence dimension: E0.

A missing mapping is a qualification failure even when tests happen to pass.

### QL-03 — deterministic repository, build, install, and static correctness

Required evidence includes the applicable deterministic repository gates plus candidate-level build,
install, import, serialization/schema, and clean-environment checks.

Primary evidence dimensions: E1, E4.

Repository configuration conformance is evidence only for the proposition it actually tests; it does
not independently prove runtime behavior.

### QL-04 — end-to-end behavioral, topology, and strategy qualification

Execute the real package composition path rather than a test-only shortcut.

Evidence must cover the selected v0.x workflow and the baseline topology/strategy boundary:

- minimal complete end-to-end workflow;
- single-table structured data;
- time-series structured data;
- multi-table shared-key structured data;
- direct/reuse behavior;
- Learning/Learned-State-assisted behavior;
- result/evidence/provenance/history access.

Primary evidence dimension: E2.

### QL-05 — property, generative, boundary, and metamorphic qualification

Use independently selected/generated cases derived from visible invariants.

The Phase 025 qualification plan freezes the generation budget before execution.

Failed generated cases and seeds remain evidence and must be replayable. Re-running until a favorable
sample appears is invalid.

Applicable challenge families: CH-01, CH-02, CH-03.

Primary evidence dimensions: E2, E3 where invalid/failure behavior is exercised.

### QL-06 — mutation sensitivity

Use targeted mutation against high-consequence guards, state transitions, authority/security checks,
recovery logic, evidence-producing logic, and other areas selected by the frozen plan.

The purpose is to demonstrate that the evidence system detects meaningful regressions.

Every selected surviving mutation must be classified as one of:

- candidate/evidence weakness requiring correction;
- equivalent/invalid mutation with justification;
- out-of-scope mutation with explicit qualification-plan justification.

There is no universal MVP mutation-percentage threshold in Phase 017-G.

A percentage becomes blocking only when the Phase 025 plan freezes a justified threshold before
evaluation.

Applicable challenge family: CH-04.

Primary evidence dimensions: E2, E3.

### QL-07 — failure, recovery, concurrency, and distributed qualification

Challenge the integrated candidate across applicable:

- failure points;
- retry/cancellation ordering;
- stale/fenced writers;
- partial completion;
- restart/reconstruction;
- dependency/runtime failure;
- materialization/promotion behavior;
- distributed identity;
- Spark-capable no-hidden-collect behavior;
- recovery ordering and idempotency.

Applicable challenge family: CH-05.

Primary evidence dimension: E3.

This layer qualifies only the bounded Spark-capable MVP claim. It does not establish production
provider or enterprise-scale support.

### QL-08 — authority, security, disclosure, and no-egress qualification

Challenge the candidate against visible trust obligations including:

- authorization;
- disclosure minimization;
- protected existence;
- scope boundaries;
- secret-handling rules;
- dependency trust;
- offline/no-egress behavior where applicable.

Applicable challenge family: CH-08.

Primary evidence dimension: E3.

The evaluator receives no extra product authority merely because it is performing adversarial tests.

### QL-09 — reproducibility, history, compatibility, and candidate replay

Evidence must challenge:

- exact candidate identity binding;
- historical reads;
- provenance/evidence reconstruction;
- recorded input/configuration binding;
- deterministic/replay promises where they exist;
- compatibility/migration behavior actually claimed by v0.x;
- clean-environment candidate replay.

Applicable challenge family: CH-07.

Primary evidence dimension: E4.

When a product behavior is intentionally stochastic, qualification checks the declared reproducible
relation, seed/configuration/provenance behavior, and evidence contract rather than inventing a
determinism requirement.

### QL-10 — independent holdout portfolio and exit decision

The evaluator independently selects or generates H1 realization after candidate freeze.

Minimum independence is EI1.

EI2 is preferred where practical for the final package-MVP decision because it reduces correlated
tool/context blind spots.

EI3 is required only for an E5 claim that actually depends on an external/private environment.
The bounded package MVP does not require EI3 merely to simulate secrecy.

The final decision must reconcile every blocking obligation, every failed challenge, evidence reuse,
contamination, carry-forward, and support non-claim.

## Challenge-family portfolio

The package-MVP portfolio requires these challenge families when their corresponding visible
obligations exist:

| Family | MVP qualification rule |
|---|---|
| CH-01 boundary/partition | required |
| CH-02 property/generative | required |
| CH-03 metamorphic | required |
| CH-04 mutation | required |
| CH-05 failure/interleaving/recovery | required |
| CH-06 differential/independent oracle | required when a legitimate oracle exists; otherwise explicit N/A |
| CH-07 history/replay/reproducibility | required |
| CH-08 authority/security/disclosure | required |

An N/A disposition must explain why the family cannot add valid evidence for the obligation. It may
not be used merely because a challenge is difficult.

## MVP capability-to-portfolio mapping

The Phase 025 ledger must map MVP-C01 through MVP-C08 to the concrete qualification obligations and
layers. At minimum:

| MVP capability | Required qualification emphasis |
|---|---|
| MVP-C01 | QL-01, QL-02, QL-03, QL-10 |
| MVP-C02 | QL-04, QL-05, QL-07, QL-09, QL-10 |
| MVP-C03 | QL-04, QL-05, QL-10 |
| MVP-C04 | QL-04, QL-07, QL-09, QL-10 |
| MVP-C05 | QL-05, QL-06, QL-07, QL-08, QL-09, QL-10 |
| MVP-C06 | QL-02, QL-04, QL-09, QL-10 |
| MVP-C07 | QL-01, QL-02, QL-03, QL-09, QL-10 |
| MVP-C08 | all applicable qualification layers and final decision |

This is a minimum mapping. Lower-level blocking obligations remain controlling and cannot disappear
inside the coarse MVP-C01..MVP-C08 labels.

## Qualification evidence ledger

Phase 025 must maintain one auditable logical ledger covering:

- qualification obligation ID;
- MVP capability ID;
- governing stable authority reference;
- blocking/non-blocking disposition;
- E0-E5 requirements;
- V1 representative evidence;
- H1 challenge family and exact run references;
- result;
- failure classification;
- contamination state;
- reused-evidence justification;
- residual/carry-forward destination;
- support claim allowed;
- claim still prohibited.

The ledger can be represented in one or more repository artifacts, but it must be deterministic and
machine-checkable enough to prove that no blocking obligation was omitted.

A raw test log is not a qualification ledger.

## Run-record requirements

Every independent qualification run records at least:

- run ID;
- exact candidate commit/build/version;
- qualification-plan identity;
- evaluator role and independence level;
- environment identity;
- obligation IDs;
- challenge family IDs;
- selection/generation method;
- seeds/operators/fixtures after execution where disclosure is allowed;
- commands/tooling;
- expected relation/oracle;
- result per obligation;
- failure/reproduction evidence;
- candidate/evaluator/indeterminate failure attribution;
- contamination state;
- evidence-reuse references;
- limitations/non-claims.

A run record is evidence. It is not authorization.

## Anchor suite after every candidate change

Every new candidate created after a repair must rerun at least:

1. exact candidate identity/build/install checks;
2. the required repository verification baseline;
3. the minimal end-to-end package workflow.

In addition:

- all evidence affected by the change must be rerun;
- exposed H1 cases become V1 regression evidence;
- affected obligations receive fresh H1 realization;
- unchanged evidence may be reused only with recorded impact justification.

This prevents a narrow repair from silently invalidating the qualification baseline.

## Failure attribution

Use the existing evaluation-method classifications:

- candidate defect;
- evaluator defect;
- indeterminate.

A reproducible candidate defect against a blocking V0 obligation causes NOT READY TO EXIT.

An evaluator defect must be corrected in the evaluation method/run without becoming a retroactive
product requirement.

An indeterminate result remains unresolved and blocks only when the affected blocking obligation
cannot otherwise be established with sufficient evidence.

## Decision rules

Phase 025 uses exactly the lifecycle outcomes:

### PASS

Allowed only when:

- every blocking MVP qualification obligation is satisfied;
- required qualification layers are complete;
- required H1 portfolio is complete;
- no unresolved candidate defect affects a blocking obligation;
- evidence reuse is justified;
- non-claims remain accurate.

PASS establishes successful package-MVP qualification.

### PASS WITH CARRY-FORWARD

Allowed only when:

- every blocking MVP qualification obligation is satisfied;
- every carry-forward is explicitly non-blocking for the bounded package-MVP claim;
- each carry-forward has an owner/destination/trigger;
- each prohibited claim remains explicitly prohibited;
- no failed blocking obligation is reclassified merely to exit.

PASS WITH CARRY-FORWARD is a successful package-MVP qualification outcome for the bounded MVP only.
It does not qualify the carried property.

### NOT READY TO EXIT

Required when any of the following remains:

- failed blocking obligation;
- blocking candidate defect;
- missing required evidence dimension;
- insufficient independent evaluation;
- omitted required challenge family without valid N/A;
- unclassified/indeterminate evidence gap that prevents a blocking obligation from being proven;
- candidate changed during evaluation;
- qualification contract was weakened after failure;
- Class 3/4 conflict remains unresolved;
- qualification documentation/ledger is incoherent.

NOT READY does not authorize repair.

## Repair and requalification

A Phase 025 candidate defect follows the v0.x program repair rule:

~~~text
record defect and contaminated challenge
  -> NOT READY disposition
  -> human selects smallest repair owner
  -> repair under normal phase/package authority
  -> freeze new candidate
  -> rerun anchor suite
  -> rerun affected evidence
  -> generate/select fresh H1 for affected obligations
  -> independent requalification
~~~

The evaluator does not become the implementer merely because the repair is obvious.

## E5 boundary

E5 provider/scale/release evidence is outside the bounded package-MVP qualification unless the
candidate attempts one of those claims.

Phase 025 must verify that such unqualified claims remain absent.

The qualification method does not close distribution-license, release-vulnerability,
Python-greater-than-3.11, production-provider, enterprise-scale, deployment, or SLO/SLA residuals.

## Phase 025 logical artifacts

Before Phase 025 exits, its evidence set must contain logical equivalents of:

- frozen qualification plan;
- qualification obligation/evidence ledger;
- independent run records;
- contamination/replay record;
- defect/evaluator-disposition record;
- evidence-reuse impact record where applicable;
- final qualification decision;
- handoff/non-claim record.

Exact file names are deferred to the Phase 025 start gate.

## Current authorization boundary

This authority is planning/process authority established by Phase 017-G.

It does not authorize Phase 018-025 execution, create an implementation package, mutate product
code, select the eventual candidate version, create a release candidate, or publish an artifact.
