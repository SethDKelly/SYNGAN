---
type: Implementation Authority
title: Success Visibility, Holdout Evaluation & Anti-Gaming Methodology
status: active
---

# Success Visibility, Holdout Evaluation & Anti-Gaming Methodology

## Purpose

Define how SYNGAN exposes implementation success obligations while preserving independent evaluation
strength against metric gaming, overfitting, evaluator leakage, and same-context self-certification.

This authority specializes the evaluation portions of syngan://implementation/phase-lifecycle and
syngan://implementation/agent-delivery. It owns split visibility, holdout challenge generation,
evaluator independence, contamination/rotation, replay evidence, and anti-gaming rules.

It does not create product semantics, change an implementation phase's scope, authorize execution,
or replace phase-specific success/evidence contracts.

## Core invariant

SYNGAN uses **visible requirements with variable challenge realization**.

~~~text
public normative contract
  -> tells implementers what correctness means
  -> freezes before implementation
  -> names blocking obligations, non-claims, and required evidence classes

independent challenge layer
  -> varies how those known obligations are tested
  -> is selected/generated after candidate freeze when practical
  -> never invents a requirement absent from public authority
~~~

A holdout may hide the exact test realization. It may never hide the requirement.

## Visibility classes

### V0 — normative obligations: always visible

Implementers, reviewers, evaluators, and humans must be able to see:

- governing current authority and stable references;
- required semantics, invariants, and state-transition rules;
- included capability and explicit exclusions/non-claims;
- blocking vs non-blocking obligations;
- relevant security, authority, identity, recovery, history, compatibility, and evidence obligations;
- required verification/evidence dimensions;
- minimum representative success and failure scenario families;
- the acceptance rule used to decide whether an obligation passes.

V0 is part of the frozen success/evidence contract.

### V1 — representative evidence: visible

Representative tests, examples, fixtures, expected errors, ordinary boundary cases, deterministic
verification lanes, and implementation-created tests may be public.

V1 helps implementation converge on the actual contract. It is not independent holdout evidence
merely because it is comprehensive.

### H1 — evaluator-selected holdout realization

H1 contains challenge details intentionally absent from the implementer's execution context until
independent evaluation runs, including exact adversarial combinations, generated property/fuzz
seeds, specific boundary selections, mutation operators, fault/interleaving choices, holdout
fixtures, selected metamorphic transformations, differential cases, and evaluator-specific prompts.

H1 must be derivable from V0 obligations and known challenge families.

### H2 — externally private evidence: optional and claim-driven

Private CI, provider test systems, private security review material, or other external evidence may
remain non-public when a real external system provides that boundary.

H2 is not required merely to simulate secrecy in a public repository. Its use must be justified by
the claim being qualified and still produce auditable evidence at the permitted disclosure level.

## Success-contract publication and freeze

Before substantive implementation starts, each executable phase must publish a success/evidence
contract that identifies, for every material obligation:

- a stable obligation ID;
- governing authority reference(s);
- blocking or non-blocking disposition;
- the capability/claim supported;
- applicable E0-E5 evidence dimensions;
- required public representative scenarios;
- applicable holdout challenge families;
- explicit exclusions/non-claims;
- the acceptance rule.

The start gate freezes this contract for ordinary implementation.

A criterion may change only through the lifecycle contract's explicit correction/reopen discipline.
An implementation failure is never sufficient reason by itself to weaken the contract.

## Holdout challenge families

### CH-01 — partition and boundary variation

Exercise valid/invalid partitions, extrema, empty/singleton cases, size transitions, value
boundaries, missing/extra structure, and boundary combinations different from public fixtures.

### CH-02 — property and generative variation

Generate values or operation sequences from declared invariants and schemas. Seeds and exact
generated examples are holdout details; the invariant is public.

### CH-03 — metamorphic relations

Apply transformations whose expected relation follows from public semantics, including
representation-preserving transformations, equivalent retries, or stable round trips.

### CH-04 — mutation challenge

Perturb implementation, configuration, guards, or evidence-producing logic in ways the required
test/evidence system should detect.

Mutation score is diagnostic unless a threshold was explicitly frozen in V0.

### CH-05 — failure order, interleaving, and recovery

Vary failure points, retry/cancellation order, stale-writer timing, partial completion, restart,
dependency failure, and recovery ordering inside public recovery obligations.

### CH-06 — differential or independent oracle

Compare equivalent implementations, reference behaviors, independently derived calculations, or
other legitimate oracles where the public contract establishes comparability.

Historical implementation is not automatically an oracle if current authority superseded it.

### CH-07 — history, replay, and reproducibility

Challenge exact candidate identity, recorded inputs/configuration, historical reads, provenance
binding, deterministic/replay promises, and compatibility/migration behavior the public contract
claims.

### CH-08 — adversarial authority, security, and disclosure

Challenge authorization, protected existence, disclosure minimization, no-egress, secret handling,
scope boundaries, and other public trust/security obligations without expanding evaluator authority.

## Challenge selection and generation

Holdout generation occurs after candidate freeze when practical.

The evaluator should:

1. bind evaluation to the exact candidate commit and frozen success-contract revision;
2. derive applicable challenge families from each blocking V0 obligation;
3. select a stratified set so important obligations are not hidden by aggregate volume;
4. generate or choose exact cases independently of implementer conversation/history;
5. record seeds, operators, fixtures, environment, and mappings needed for replay;
6. execute without silently modifying the candidate;
7. classify every failure against a visible obligation or evaluator defect;
8. disclose enough evidence after the run to permit audit/replay;
9. treat exposed cases as contaminated for future holdout use.

Randomness is a selection mechanism, not evidence by itself. The generated case, seed, candidate,
environment, expected relation, and result must be recorded.

A deterministic hand-authored evaluator case is valid H1 when independently selected after freeze
and not exposed to the implementer in advance.

## Evaluator independence levels

### EI0 — first-party / same-context

The implementing agent runs or reviews its own tests using implementation context. Useful evidence,
but not independent certification.

### EI1 — fresh-context independent role

A reviewer/evaluator starts from repository-owned authority, the frozen success contract, exact
candidate/diff, and relevant evidence without the implementer's conversational history.

EI1 is the minimum independence level for an agent-assisted phase exit.

### EI2 — cross-provider or independently staffed role

A different provider or separately staffed reviewer performs EI1-style evaluation.

EI2 is preferred when practical because it reduces correlated tool/context blind spots. Provider
brand alone does not establish independence.

### EI3 — external/private qualification

An external provider, security system, benchmark environment, human audit, or private CI system
provides evidence that cannot be reproduced solely from repository-local execution.

EI3 is claim-driven and primarily corresponds to E5 qualification.

## Anti-gaming controls

### AG-01 — no hidden requirements
Every blocking failure must map to a V0 obligation that existed before implementation.

### AG-02 — no contract weakening after failure
Do not delete, relax, reinterpret, or reclassify a blocking obligation merely because the candidate fails it.

### AG-03 — candidate freeze before holdout selection
Independent holdout evaluation binds to an exact candidate. A product change creates a new candidate.

### AG-04 — no evaluator repair while certifying
The evaluator reports defects; it does not silently fix the frozen candidate.

### AG-05 — contamination requires rotation
Once an H1 case is exposed for repair, it becomes V1 regression evidence and fresh H1 realization is
required for renewed independent evaluation of the affected obligation.

### AG-06 — blocking obligations are non-compensatory
Passing counts, coverage, mutation score, or another aggregate metric cannot erase a failed blocking obligation.

### AG-07 — no cherry-picked retries
Failed generated cases and seeds remain evidence. Re-running until a favorable sample appears is not a valid pass.

### AG-08 — thresholds are frozen, not post-hoc
Coverage, mutation, statistical, performance, or stochastic thresholds bind only if declared before evaluation.

### AG-09 — challenge breadth follows obligation risk
Holdout volume must not concentrate on easy obligations while leaving high-consequence obligations unchallenged.

### AG-10 — evaluator context is minimized
Evaluator context is reconstructed from repository authority, frozen contract, candidate, and evidence.

### AG-11 — scope expansion earns no credit
Unrequested features or extra tests do not compensate for missing selected-package obligations.

### AG-12 — evaluation failure is not redesign authority
Repair remains inside authorized scope; Class 3/4 architecture/semantic conflicts use normal reopen rules.

## Contamination and repair cycle

~~~text
frozen candidate Cn
  -> independent H1 challenge exposes defect
  -> record failing challenge + V0 mapping
  -> exposed case becomes V1 regression evidence
  -> repair inside authorized package or reopen if required
  -> freeze candidate Cn+1
  -> rerun affected regression evidence
  -> generate/select fresh H1 for affected obligation
  -> preserve old and new evidence
~~~

Unchanged evidence may be reused only with recorded justification that the candidate change cannot
invalidate it.

## Evaluation run record

Each independent run records at least:

- evaluation/run ID;
- exact candidate commit;
- success-contract identity;
- evaluator role and independence level;
- provider/runtime or human identity at appropriate non-secret granularity;
- environment identity;
- V0 obligation IDs;
- challenge family IDs;
- holdout generation/selection method;
- seeds/operators/fixture identifiers after execution where disclosure is allowed;
- commands/tooling;
- result per obligation;
- failure/reproduction evidence;
- evaluator-defect dispositions;
- contamination state;
- reused-evidence justification;
- limitations/non-claims.

The record is evidence, not merge/release/progression authority.

## Failure attribution

A holdout failure is classified as:

1. **candidate defect** — reproducibly violates a visible V0 obligation;
2. **evaluator defect** — assumes a requirement absent from V0, uses an invalid oracle, or cannot
   validly exercise the candidate;
3. **indeterminate** — insufficient evidence for classification.

Only candidate defects block on the basis of the challenged obligation. Evaluator mistakes do not
become retroactive product requirements.

## Public repository rule

SYNGAN is public. Therefore checked-in "secret tests" are not secret. Obscurity, encoded fixtures,
and hidden filenames do not create independence.

Fresh generation, post-freeze selection, isolated evaluator context, and rotation after
contamination are the default holdout mechanisms. Genuine H2 evidence is used only when a real
external/private system exists.

## Relationship to phase and MVP qualification

This methodology defines reusable mechanics. Each implementation phase start gate chooses the
smallest sufficient challenge families and independence level for its claims.

Phase 017-G will define the v0.x MVP completion-testing portfolio and qualification decision using
this authority. Phase 025 will execute that qualification against a frozen v0.x candidate.

## Current authorization boundary

This methodology is planning/process authority established by Phase 017-D.

It does not authorize product implementation, create an implementation package, authorize Phase 018,
require provider/private infrastructure, or make release/provider/scale claims.
