---
type: Design Authority
title: Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract
status: active
---

# Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract

## Purpose

Define the cross-cutting design rules that keep disclosure-risk findings, formal privacy guarantees, security disclosure/redaction and external release/use authorization distinct.

The contract exists because synthetic data may still memorize, reveal, link, or enable inference about sensitive source information, while formal privacy mechanisms and organizational release decisions have different purposes and authority.

This contract does **not** create a generic Privacy concept.

## Governing rule

> **Synthetic origin, favorable privacy-related Evidence, local/offline execution, or successful Generation MUST NOT be interpreted as a formal privacy guarantee, anonymization certification, or authorization to release/use data.**

## Four separate boundaries

SYNGAN MUST preserve four distinct responsibilities:

```text
privacy/disclosure question
        ↓
Criterion / Evaluation / Evidence

formal mechanism guarantee/accounting
        ↓
mechanism-specific authority when supported

current disclosure/redaction of sensitive facts
        ↓
security/authorization view policy

release/use approval
        ↓
external organizational governance authority
```

No one layer may silently substitute for another.

## Synthetic data is not inherently private

Generation creates synthetic data according to the committed synthesis contract.

It does not by itself establish:

- anonymization;
- de-identification;
- differential privacy;
- resistance to membership inference;
- resistance to linkage/attribute inference;
- absence of memorization;
- regulatory safe-harbor status;
- release/use approval.

A Strategy MAY be designed to reduce disclosure risk or to implement a formal privacy mechanism, but the corresponding semantics must be explicit.

## Data Meaning boundary

Data Meaning may identify semantic roles relevant to privacy/disclosure, such as sensitive fields, identifiers, quasi-identifiers, free-form text, entity identifiers, time roles or other domain interpretations.

Such labels inform compatibility, Criteria and policy but are not privacy guarantees.

A physical string, identifier or timestamp type is not sufficient to infer privacy safety.

## Disclosure-risk Evaluation

Disclosure risk is currently addressed through existing concepts:

- Evaluation Criterion owns the precise question/threat model;
- Evaluation owns the method, subject/reference, scope, coverage, sampling/approximation and uncertainty;
- Evidence owns the durable finding and claim-strength boundary.

Examples of legitimate Criteria include, where suitable methods exist:

- exact/near duplication;
- nearest-neighbor disclosure;
- membership inference;
- attribute inference;
- linkage/re-identification under stated attacker knowledge;
- memorization of rare text/records;
- trajectory/sequence uniqueness;
- multi-table linkage risk;
- Learned-State memorization/disclosure risk.

No finite list is canonical.

## Threat-model specificity

A favorable result under one threat model MUST NOT silently answer another.

Examples:

```text
no exact source duplicates
    !=
no linkage risk
```

```text
low sampled membership attack success
    !=
formal privacy guarantee
```

```text
low row-level risk
    !=
low multi-table or trajectory-level risk
```

Evidence must preserve the exact threat model, subject/scope, method and limitations required for interpretation.

## Text-generation consequence

The self-contained baseline text capability introduced by 006-D does not imply privacy.

A source-derived text Strategy may reproduce rare phrases, names, identifiers, semantic fragments or unusual trajectories from source data.

Accordingly:

- text capability/limitations remain Strategy authority;
- relevant sensitive/free-form semantic roles remain Data Meaning;
- disclosure/memorization questions remain Criterion/Evaluation/Evidence;
- advanced locally pretrained or runtime-network text capability does not weaken these boundaries;
- offline execution does not establish privacy merely because no data left the network boundary.

## Time-series and multi-table consequence

Disclosure may arise from coordinated structure rather than one field/table/row.

Evaluation must therefore be able to bind the relevant logical subject, including where appropriate:

- one or more related tables;
- shared-key/join context;
- entity-level longitudinal series;
- trajectory/order/cadence context;
- combinations of quasi-identifiers across scopes.

Per-constituent favorable Evidence MUST NOT automatically establish whole-output privacy/safety.

This contract does not decide the `Relationship` concept question; 006-G owns that boundary.

## Scale and approximation consequence

Privacy/disclosure Evaluation is subject to the Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract.

Where exhaustive analysis is infeasible, statistical/sampled/sketch methods may be valid when committed explicitly and methodologically appropriate.

However:

- sampled privacy Evidence remains sampled/statistical Evidence;
- rare-event/tail risk must not be hidden by average-case sampling;
- resource pressure cannot silently change a universal Criterion into a weaker sampled one;
- approximate findings cannot be represented as universal safety.

## Formal privacy guarantees are distinct from attack Evidence

A formal privacy mechanism may establish guarantees based on mathematical construction, mechanism parameters and assumptions rather than empirical attack success.

Therefore:

- favorable attack Evidence is not the guarantee;
- attack failure is not proof that the mechanism lacks its formal guarantee;
- implementation/configuration verification Evidence may support reliance on a mechanism but does not replace the mechanism's own authority/state;
- Strategy capability metadata alone is insufficient when a mechanism has independently meaningful reusable/accounting state.

## Mechanism-specific discovery rule

A generic `Privacy` or `PrivacyGuarantee` concept remains rejected.

Before SYNGAN implements a formal privacy mechanism that introduces independent state/actions, explicit Jackson-style concept discovery MUST reopen.

Trigger examples include:

- privacy unit/adjacency semantics;
- privacy-loss parameters;
- reusable/composable privacy budget;
- allocation/reservation/consumption of privacy loss;
- cross-release composition/accounting;
- mechanism-specific certificates/proof state;
- exhaustion preventing later operations;
- lifecycle that outlives one Learning/Generation/Evaluation.

The accepted concept, if any, must be mechanism/purpose specific rather than generic `Privacy`.

## Differential privacy scope decision

Differential privacy is **not part of the initial implementation baseline** accepted by Phase 006.

SYNGAN may later support a differential-privacy Strategy/mechanism, but implementation MUST NOT begin by merely adding `epsilon`, `delta`, privacy-budget fields or counters to generic Strategy/configuration metadata.

A future DP initiative must first perform concept discovery because composable privacy-loss accounting can have independent lifecycle and cross-release authority.

Until such discovery occurs, SYNGAN MUST NOT claim differential privacy as a built-in formal guarantee.

## Privacy Evidence versus formal guarantee state

Privacy-related Evidence may legitimately record:

- observed disclosure-risk estimates;
- attack outcomes;
- exact-match counts;
- statistical bounds/confidence;
- implementation/configuration verification findings;
- mechanism verification results where a formal mechanism exists.

Evidence remains durable finding authority.

Formal mechanism state, when later accepted, remains separate from Evidence and may be referenced by Evidence/Provenance rather than collapsed into an Evidence record.

## Generation completion boundary

Generation completion may depend on privacy-related Evidence only when the committed Generation contract explicitly requires a particular Criterion/claim strength as a completion condition.

Even then:

```text
Generation completed
        !=
release approved
```

and:

```text
privacy-related completion Evidence favorable
        !=
formal privacy guarantee
```

unless a separately accepted formal mechanism authority actually establishes such a guarantee.

## Release/use governance boundary

Use/Release Decision remains outside current SYNGAN concept authority.

External governance may consider:

- Evidence;
- Provenance;
- Data Meaning;
- legal/policy classifications;
- purpose/use context;
- destination;
- current authorization;
- formal privacy-mechanism state where applicable;
- other organizational controls.

SYNGAN may hand off exact Evidence/history to such systems and may enforce their current authorization decisions through the security boundary.

It MUST NOT create a hidden `approved=true` semantic state on Generation, Output, Evidence or Provenance merely because an external policy grants release.

The same Evidence may legitimately result in different release/use decisions under different external policies.

## Export authorization is distinct from release-governance semantics

005-I authorization may permit or deny `output.export`, `evidence.read`, `history.traverse` and related protected actions.

That current permission is operational/security authority.

It does not transform the underlying resource into a globally approved release or privacy-certified asset.

Likewise, historical approval does not grant permanent future export permission after policy/revocation changes.

## Redaction and disclosure boundary

Sensitive privacy Evidence may itself expose source-derived information, rare examples, attack traces, nearest neighbors or existence/count facts.

Authorized views must preserve distinctions among:

- absent;
- unknown/indeterminate;
- unavailable;
- withheld;
- redacted/authorized summary;
- invalid.

Redaction/withholding MUST NOT mutate canonical Evidence/Provenance/history.

Existence itself may be protected.

## Learned State boundary

Learned State can be a legitimate privacy/disclosure Evaluation subject.

A safe-looking generated sample does not prove that Learned State cannot memorize or expose sensitive source information through another attack/interface.

Likewise, Evidence about Learned State does not automatically apply to every generated output unless the Criterion and method support that scope.

## No universal privacy score

SYNGAN MUST NOT create a package-wide scalar such as:

```text
privacy_score = 0.92
safe_to_release = true
```

as universal privacy/release authority.

Different Criteria, threat models, mechanisms, formal guarantees and organizational policies are not necessarily commensurable.

A user-facing summary may aggregate or present findings only with explicit method/policy semantics and without erasing conflicting Evidence.

## Provenance and reproducibility

Material privacy/disclosure evaluations and future formal-mechanism facts must remain historically attributable.

Where applicable history must preserve exact:

- output/Learned-State/source/reference subject;
- Criterion/threat model;
- Evaluation method/configuration;
- sampling/approximation/uncertainty;
- Strategy/mechanism revision;
- formal mechanism/accounting identity when later supported;
- external dependency/runtime facts material to interpretation.

A later policy change does not rewrite historical Evidence or formal guarantee facts.

## Synchronization consequence

The current fifteen synchronization IDs remain sufficient for the initial baseline.

Most relevant:

- SYNC-09 — Criterion binding;
- SYNC-10 — method compatibility/claim strength;
- SYNC-11 — Evaluation operational realization;
- SYNC-12 — Evidence establishment;
- SYNC-13 — controlled external/Generation handoff;
- SYNC-14 / SYNC-15 — historical/reproducibility attribution.

No new synchronization is justified until a new mechanism-specific concept is accepted.

## Architecture/planning consequence

006-I must reconcile this contract into relevant architecture/Phase 005 planning, especially:

- privacy/disclosure Evaluation method extensibility;
- text/multi-table/time-series subject representation;
- Evidence diagnostic sensitivity and redaction;
- history/projection disclosure;
- external governance handoff;
- explicit non-claiming of formal DP in the initial baseline;
- concept-discovery gate before any future mechanism-specific privacy implementation.

## Invariants

1. Synthetic origin MUST NOT imply privacy, anonymization or release approval.
2. Privacy/disclosure Evidence MUST remain Criterion/threat-model/method/scope specific.
3. Favorable empirical Evidence MUST NOT become a formal privacy guarantee automatically.
4. Formal privacy mechanisms with independent state/actions MUST undergo mechanism-specific concept discovery before implementation.
5. Differential privacy is not an initial-baseline formal guarantee.
6. A future composable privacy-budget mechanism MUST NOT be reduced to generic Strategy metadata, deployment quota or Evidence state merely for implementation convenience.
7. Generation completion MUST NOT imply external release/use approval.
8. Evidence remains observation authority and MUST NOT become organizational approval authority.
9. External release/use policy MAY block or permit protected actions without rewriting Generation/Evidence history.
10. Redaction/withholding MUST NOT mutate canonical Evidence/Provenance/history.
11. Offline/self-contained execution MUST NOT be interpreted as a privacy guarantee.
12. Per-table/per-row favorable Evidence MUST NOT automatically establish multi-table/trajectory-level disclosure safety.
13. Sampled/approximate privacy Evaluation MUST NOT claim stronger coverage than supported.
14. No universal privacy/release score may erase distinct Criteria, threat models, formal guarantees or external policy.
15. No rule in this contract creates a generic Privacy, Memorization, Disclosure Risk, Release Decision or Differential Privacy concept in the current catalog.

## Operational principle

A practitioner generates a self-contained synthetic table containing free-form notes. Generation completes successfully. A sample-based membership-inference Evaluation and an exhaustive exact-duplicate Evaluation both produce favorable Evidence, but those findings remain scoped to their own questions and do not certify anonymization.

An external governance system receives the exact Evidence/Provenance context and denies export because the intended destination and current organizational policy require stronger assurance. SYNGAN preserves the completed Generation and favorable Evidence as historical truth while current authorization blocks export.

Later the project considers adding a composable differential-privacy mechanism. Because repeated releases would consume a shared privacy-loss budget, the team reopens Jackson concept discovery before implementation rather than adding `epsilon` and budget counters to Strategy metadata.