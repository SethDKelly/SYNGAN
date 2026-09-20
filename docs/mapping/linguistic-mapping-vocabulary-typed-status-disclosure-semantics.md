---
type: Concept Mapping Design Authority
title: Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics
status: active
---

# Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics

## Purpose

Establish the Phase 010-D linguistic contract for expressing SYNGAN concept actions, state, history, uncertainty and disclosure without changing the semantics established by Phases 008 through 010-C.

This authority closes the current F3 linguistic-mapping / vocabulary-alignment obligation. It does not define public API identifiers, serialized enums, CLI syntax, UI copy, schemas or runtime mechanisms.

> **Words may simplify presentation, but they may not erase ownership, semantic dimension, historical scope, uncertainty or disclosure meaning.**

## Current Phase 014 completion note

This document preserves its Phase 010 derivation and original subgroup handoff as historical provenance. Phase 010 F1-F5 are complete; Phase 012 confirmed mapping completion; Phase 013 preserved mapping semantics in architecture; Phase 014-D re-audits the current mapping layer. Current subgroup sequencing is governed by [Phase 014](../phases/014/index.md).

## Governing authority

This mapping consumes the Terminology Policy, Domain Lexicon, Semantic Distinctions, Ecosystem Compatibility Vocabulary, Phase 008 action/query normalization, 010-B action mapping and 010-C inspection mapping.

Canonical SYNGAN semantics outrank familiar ecosystem vocabulary.

## Canonical concept names

The accepted concept names remain:

```text
Data Meaning
Synthesis Strategy
Learning
Learned State
Generation
Constraint
Evaluation Criterion
Evaluation
Evidence
Execution
Provenance
```

010-D does not rename a concept.

Contextual short forms such as Strategy, Criterion or Meaning are acceptable after ownership is clear.

## Typed-status grammar

SYNGAN has no universal status dimension. A status expression must preserve its semantic type when the distinction matters.

| Type | Question |
|---|---|
| revision/current-use status | May this reusable revision/result ordinarily be selected or relied upon now? |
| activity lifecycle | Where is Learning, Generation or Evaluation relative to proposal, commitment and terminal outcome? |
| contextual assessment | Is a proposed use sufficiently established for this exact context? |
| operational lifecycle | What is happening in Execution or an Attempt? |
| material finality | Is material partial, candidate/intermediate or authoritative completed output? |
| finding / claim strength | What did Evidence actually establish, with what strength and uncertainty? |
| handling / applicability | How is a Constraint treated in this activity context? |
| disclosure state | What may this actor be told? |
| history quality | How directly and completely is historical knowledge retained or reconstructed? |

A surface may summarize several dimensions but must not create one canonical state machine from them.

Unqualified words such as `complete`, `failed`, `cancelled`, `valid`, `ready`, `passed` and `current` are unsafe where more than one owner or dimension is visible.

Prefer owner-qualified language such as:

```text
Generation completed
Execution completed operationally
Evaluation completed
Learning prerequisite assessment: ready with limitations
Generation compatibility: indeterminate
Constraint handling: validated later
Evidence finding: violated
```

## Reusable revision/current-use vocabulary

Where supported by the owning concept, preserve distinctions among:

```text
draft
effective
usable/current for ordinary reliance
restricted
superseded
retired
stale/obsolete
inapplicable
invalidated
```

These terms are not synonyms.

- **superseded** — a newer revision/result is preferred; historical bindings remain exact.
- **retired** — ordinary new selection stops without claiming historical error.
- **restricted** — use is permitted only under an explicit limitation/context.
- **stale/obsolete** — historical observation may remain true but is no longer appropriate for ordinary current reliance.
- **inapplicable** — the state/finding does not govern or answer this requested context.
- **invalidated** — a material defect undermines ordinary reliance without erasing history.

`deprecated` is only a compatibility label unless the canonical distinction remains recoverable.

## Semantic activity vocabulary

Learning, Generation and Evaluation are semantic activities, not platform jobs.

Their language must preserve distinctions equivalent to:

```text
proposed/draft
validated or assessed for commitment
committed
active / fulfilling / evaluating
cancellation requested where material
completed / completed with allowed limitations
failed
cancelled
```

`commit` means the material semantic specification becomes historically fixed. `start`, `run`, `execute` or `submit` must not substitute for commitment.

Generation may be `awaiting required validation` after candidate material exists. Evaluation completion means the examination validly produced interpretable Evidence; it does not mean the subject passed.

## Contextual assessment vocabulary

Contextual validation belongs to the consuming activity.

Preferred result language is:

```text
ready
ready with limitations
incompatible
indeterminate
```

`ready` means sufficient for the next semantic decision under that exact context. It does not mean universally supported, safe, private, operationally available or complete.

`indeterminate` means the required answer cannot be established strongly enough. It must not be silently converted to ready, false, failed or unsupported.

`blocked` is an actionability description, not a universal canonical lifecycle state. When used, expose the reason and owner.

## Constraint language

Constraint surfaces must keep separate:

```text
rule authority / revision state
contextual applicability
activity handling
actual output finding
```

Current handling language includes:

```text
enforced
validated later
unsupported
not applicable
```

Actual findings may be expressed as satisfied, violated, not assessed or indeterminate in the appropriate Generation/Evaluation/Evidence context.

`enforced` is not automatically synonymous with `satisfied`.

## Generation material-finality vocabulary

Preserve:

```text
partial materialization
candidate materialization
candidate complete / awaiting required validation
completed output
abandoned or quarantined non-final material
```

`generated`, `written`, `materialized`, `files present` or `100% written` do not by themselves mean `Generation completed`.

## Execution / Attempt vocabulary

Execution owns operational realization only.

Preferred Execution distinctions are equivalent to:

```text
prepared
queued/pending
running
recovery pending
cancellation requested
completed operationally
failed terminally
cancelled
indeterminate/unknown
```

Attempt outcomes preserve operational success, retryable/recoverable failure, non-recoverable failure, cancellation, superseded/abandoned recovery attempts and indeterminate/unknown outcomes.

`run` and `job` are compatibility/platform words and must be qualified when ambiguity matters: SYNGAN Execution, Execution Attempt, Spark job, Databricks run, platform task.

## Evaluation and Evidence vocabulary

A successful Evaluation may produce unfavorable Evidence.

`Evaluation completed` does not mean:

```text
criterion passed
subject acceptable
output safe
privacy established
release approved
```

Evidence finding language is Criterion/method dependent and may include property satisfied, property violated, estimated value with uncertainty, comparative result, scoped risk estimate, indeterminate/inconclusive result, bounded result or diagnostic/partial observation.

No universal Evidence pass/fail enum is established.

Where material, preserve claim-strength language equivalent to:

```text
exhaustive/universal for the stated scope
deterministic bounded/certificate-backed
statistical
approximate/sketch-based
diagnostic/partial
```

Use `supports` rather than `proves` unless the method actually establishes the stronger claim.

## Disclosure vocabulary

Disclosure state is orthogonal to canonical domain state and history quality.

| Category | Meaning |
|---|---|
| visible | relevant content may be shown to this actor |
| authorized summary / redacted | a permitted partial representation may be shown while protected detail remains undisclosed |
| withheld | information is known to exist/be available but policy prevents disclosure to this actor, where revealing existence is itself permitted |
| unavailable | information should be resolvable in principle but cannot currently be retrieved/resolved sufficiently |
| unknown | the underlying fact/content cannot be established sufficiently |
| absent | canonical state establishes that the relevant fact/result/reference does not exist for the stated scope |

`not applicable` is separate: the capability/question does not apply to the current application-family/workflow context.

If revealing existence is sensitive, an actor boundary may intentionally collapse several outward states. That is disclosure policy, not canonical-state mutation.

## Historical-knowledge vocabulary

010-C placeholders are normalized as:

```text
DIRECT        -> directly retained
RECONSTRUCTED -> reconstructed
PARTIAL       -> partial/incomplete
UNAVAILABLE   -> history unavailable
INDETERMINATE -> history indeterminate
```

These are semantic descriptors, not required public/runtime enums.

History quality and disclosure remain separate dimensions. `directly retained but withheld` and `reconstructed and visible` are both valid combinations.

## High-risk words

The following require qualification when ambiguity affects meaning:

- **model** — model family, Learned State, implementation object or ecosystem model;
- **run** — domain activity, Execution, Attempt or platform run;
- **job** — platform/runtime representation;
- **artifact** — durable representation/materialization, not canonical authority by itself;
- **metric** — method/measurement, not Criterion/Evaluation/Evidence by itself;
- **metadata** — umbrella term; qualify kind;
- **validation / valid** — state the exact proposition and owner;
- **passed** — use only where an explicit Criterion/policy defines pass semantics;
- **quality** — name the dimension such as fidelity, utility, validity or disclosure risk;
- **safe/private/anonymous** — state the exact Evidence/threat-model/mechanism claim instead;
- **reproducible** — qualify exact, statistical, bounded/approximate or another explicit expectation;
- **current/latest** — identify current-use/applicability/operational dimension; latest never replaces exact historical binding;
- **complete** — qualify semantic owner or material dimension.

## Ecosystem aliases

| Term | Disposition |
|---|---|
| fit | compatibility verb for Learning when semantics map clearly |
| train | use only when Learning actually performs training/optimization |
| sample | avoid for generic synthetic production; prefer generate |
| synthesizer | compatibility/API candidate, not a concept-boundary replacement |
| lineage | derivational subset of Provenance, not all Provenance |
| checkpoint | operational recovery material; non-final unless another owner promotes a result |

## Human/programmatic parity

Human and programmatic surfaces may use different presentation forms, but the same material owner, dimension, uncertainty, limitation, historical scope and disclosure meaning must remain recoverable.

010-D does not choose concrete field names or UI labels.

## Application-family vocabulary

Optional concepts must not appear as mandatory empty workflow steps.

Direct Generation must not imply failed/missing Learning. A family without Execution must not show an empty required Execution lifecycle. A family without Provenance must not fabricate a failed provenance state. `not applicable` may explain an omitted capability where useful.

## F3 result

```text
11 / 11 accepted concept names                 ALIGNED
66 / 66 action groups                         GOVERNED BY OWNER/VERB RULES
52 / 52 query groups                          GOVERNED BY INSPECTION LANGUAGE RULES
11 / 11 lifecycle/history envelopes           OWNER-QUALIFIED LANGUAGE ESTABLISHED
reusable current-use state                     TYPED
activity lifecycle                             TYPED
contextual assessment                          TYPED
Execution/Attempt operational state             TYPED
Generation material finality                    TYPED
Evidence finding/claim strength                 TYPED
Constraint handling/satisfaction                TYPED
disclosure semantics                            TYPED
history-quality semantics                       TYPED
high-risk ecosystem aliases                     QUALIFIED
```

No concept rename, new concept, new synchronization or global Status/Validation/Quality owner is required.

**F3 is CURRENTLY CLOSED**, subject to Phase 010-H revalidation.

## Stop / reopen audit

```text
J1 local concept defect                 NONE FOUND
J2 purpose/catalog/boundary defect      NONE FOUND
J3 dependence/composition defect        NONE FOUND
concept rename required                 NO
new concept                             NO
new synchronization                     NO
global Status/Validation/Quality owner  REJECTED
010-D local linguistic blocker          NONE FOUND
```

## Representation boundary

010-D does not establish public enum values, Python identifiers, JSON fields, endpoint/status codes, CLI syntax, UI components, report schemas, database columns, exception taxonomies, localization mechanisms, access-control mechanisms or platform adapters.

## Current next boundary

**010-E — Physical / Interaction Mapping Across SDK, Notebook, CLI, API, Report, UI & Operator Surfaces** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
