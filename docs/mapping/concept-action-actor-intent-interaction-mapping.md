---
type: Concept Mapping Design Authority
title: Concept Action → Actor Intent & Interaction Mapping
status: active
---

# Concept Action → Actor Intent & Interaction Mapping

## Purpose

Provide the Phase 010-B surface-neutral mapping of every normalized SYNGAN state-changing concept action to actor intent and human/programmatic interaction obligations.

This authority closes the current **semantic action-mapping** portion of F1. It does not select concrete API methods, endpoints, CLI commands, widgets, pages, events, transactions, persistence representations, or service boundaries.

The governing rule is:

> **A conceptual command is mapped to what actors/programmatic consumers must be able to request, cause, review, distinguish, observe, or understand—not mechanically to one physical control.**

Some conceptual commands are actor-initiated. Others are system-established consequences of valid concept behavior or synchronization. Every command still needs an interaction mapping so that its meaning and authority are not hidden.

---

# 1. Governing authority

This mapping consumes:

- [Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline](mapping-authority-coverage-actor-surface-evidence-baseline.md)
- [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](../concepts/action-query-lifecycle-normalization.md)
- [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Current Synchronization Authority](../synchronizations/index.md)
- [Actors & Needs](../problem/actors.md)
- [Semantic Distinctions](../terminology/semantic-distinctions.md)
- retained Phase 003/006 experience evidence

Where retained workflow language conflicts with current Phase 008/009 semantics, current concept/composition authority governs.

---

# 2. Scope and accounting

010-B maps the normalized command headings in the current Phase 008-D authority.

```text
Data Meaning             7
Synthesis Strategy       4
Learning                 8
Learned State            4
Generation              11
Constraint               4
Evaluation Criterion     4
Evaluation               8
Evidence                 3
Execution                11
Provenance               2
                         --
TOTAL                    66 action groups
```

Every one of these 66 action groups reaches `SEMANTICALLY MAPPED` in this authority.

Queries/observations are not claimed complete here; they remain `SOURCE IDENTIFIED` pending 010-C.

---

# 3. Common record interpretation

Each record below instantiates the 010-A mapping schema.

For compactness, the records use these columns:

- **ID / action** → M1/M2/M3
- **actors + intent/obligation** → M4/M5
- **guard → result / non-success** → M6/M7/M8
- **AF / sync** → M9/M10
- **time / disclosure-history-scale** → M11-M14
- **surfaces / vocabulary risk** → M15/M16
- **evidence / status** → M17/M18

Unless a row says otherwise:

- M17 evidence is the owning concept's Phase 008-D command plus current actor/composition authority and applicable Phase 003/006 evidence;
- M18 is `SEMANTICALLY MAPPED`;
- M19 is `NONE FOUND`—no mapping-driven upstream reopen is required;
- disclosure may restrict detail but cannot rewrite canonical concept state;
- ordinary interaction must use bounded summaries/references rather than full enterprise-scale materialization.

Surface labels follow 010-A: `S1` SDK/API, `S2` notebook, `S3` CLI, `S4` report/history/review, `S5` graphical UI, `S6` operator/admin, `S7` external handoff.

---

# 4. Data Meaning action mappings

## DM-A01 — Create / Declare draft meaning

- **Actors + intent/obligation:** A3 Data Owner/Steward and A1 Data Practitioner primarily; A7 Extension Author where extension semantics are declared. Actors must be able to state semantic assertions for an identifiable subject/scope and distinguish their declared origin from inference.
- **Guard → result / non-success:** identifiable scope + representable declaration authority → draft declared assertion exists and remains non-effective until effectiveness is established. Missing/ambiguous scope or authority must not silently create effective meaning.
- **AF / sync:** `AF-AUTH`, and any family member later consuming Meaning; no synchronization is owned by this action.
- **Time / D-H-E:** proposed/editable; declaration origin must remain inspectable; bounded semantic metadata.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `schema`, `metadata`, `type` must not imply Data Meaning is merely physical structure.

## DM-A02 — Infer meaning

- **Actors + intent/obligation:** A1 and A3 need assisted interpretation; A7 may supply inference capability. The interaction must expose that the assertion is inferred, its basis/method, and uncertainty.
- **Guard → result / non-success:** identifiable subject + inspectable inference basis → inferred assertion recorded. Insufficient basis yields unresolved/indeterminate inference rather than a fabricated declaration.
- **AF / sync:** `AF-AUTH`; no direct sync ownership.
- **Time / D-H-E:** proposed/current candidate; inference provenance and uncertainty visible; bounded summaries rather than corpus materialization.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `detected`, `auto`, `confidence` must not imply authoritative declaration.

## DM-A03 — Mark unresolved / conflicting / unsupported

- **Actors + intent/obligation:** A1/A3 must be able to preserve non-resolution rather than choose a convenient default; A4 may need visibility where the uncertainty affects review.
- **Guard → result / non-success:** identifiable semantic proposition → explicit unresolved/conflicting/unsupported state. If the system cannot characterize the issue strongly enough, it remains unknown/indeterminate rather than resolved.
- **AF / sync:** `AF-AUTH`; consumed by activities through their own validation.
- **Time / D-H-E:** proposed/current-use; disclosure/history preserve the exact assertion and reason.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: generic `invalid` or null must not erase unresolved/conflict semantics.

## DM-A04 — Correct / Revise

- **Actors + intent/obligation:** A3/A1 must be able to propose corrected interpretation while retaining the exact prior revision used historically.
- **Guard → result / non-success:** material correction/new interpretation → new distinguishable revision. In-place rewrite of bound historical meaning is not allowed.
- **AF / sync:** `AF-AUTH`; later activities may bind the new revision through `SYNC-01` at their own commit.
- **Time / D-H-E:** current new revision + historical prior revision; current versus historical meaning must remain jointly inspectable.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `edit` must not imply destructive mutation of committed history.

## DM-A05 — Make effective

- **Actors + intent/obligation:** A3/A1 need to distinguish draft/inferred/revised semantics from a revision eligible for new committed reliance.
- **Guard → result / non-success:** coherent-enough revision + required authority → current-use status effective. Unresolved material conflict prevents false effectiveness.
- **AF / sync:** `AF-AUTH`; establishes eligibility only, not activity compatibility; `SYNC-01` occurs when a consuming activity commits an exact binding.
- **Time / D-H-E:** current-use/future-use eligibility; effective status does not rewrite historical revisions.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `approve` should not imply external governance authority beyond Data Meaning effectiveness.

## DM-A06 — Supersede

- **Actors + intent/obligation:** A3/A1 need to move future default/current selection to a newer revision while preserving prior bindings.
- **Guard → result / non-success:** newer revision designated → prior becomes superseded for new selection. Historical use remains authoritative as-used.
- **AF / sync:** `AF-AUTH`; no retroactive `SYNC-01` propagation.
- **Time / D-H-E:** future-use status change + historical continuity.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `latest` must not substitute for exact historical revision.

## DM-A07 — Invalidate

- **Actors + intent/obligation:** A3/A1/A4 need to mark a material defect that blocks ordinary new reliance and understand historical impact without rewriting past activity.
- **Guard → result / non-success:** material defect established → invalid for new reliance with reason. If defect is only suspected, status must remain appropriately indeterminate/restricted rather than falsely invalidated.
- **AF / sync:** `AF-AUTH`; consuming activities decide current-use consequences; historical bindings do not mutate.
- **Time / D-H-E:** current/future-use invalidity + preserved historical binding truth.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `deleted`, `revoked history` must not imply historical erasure.

---

# 5. Synthesis Strategy action mappings

## SS-A01 — Define draft Strategy revision

- **Actors + intent/obligation:** A7 Extension Author and A6 Library Maintainer primarily; A1 later selects. They must be able to declare synthesis behavior, capabilities, requirements, limits, learning/generation mode and dependency posture independently of one implementation class.
- **Guard → result / non-success:** behavior describable as a Strategy → draft revision exists; incomplete material declarations remain draft/ineligible rather than implicitly usable.
- **AF / sync:** `AF-AUTH`; later Learning/Generation compatibility uses `SYNC-02`.
- **Time / D-H-E:** proposed/editable; bounded capability/dependency declarations.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `model`, `plugin`, `algorithm` cannot replace Strategy semantics.

## SS-A02 — Configure / Revise material semantics

- **Actors + intent/obligation:** A7/A6 must be able to change material Strategy behavior/configuration while preserving exact prior activity bindings.
- **Guard → result / non-success:** material behavior/config/dependency/reproducibility change → distinguishable revision/configuration. Cosmetic/non-semantic representation changes need not fabricate a semantic revision.
- **AF / sync:** `AF-AUTH`; consuming activities bind exact revisions/configs through `SYNC-02`.
- **Time / D-H-E:** proposed/current revision + preserved historical bindings.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `settings` must not hide behavior-changing semantic revision.

## SS-A03 — Make effective

- **Actors + intent/obligation:** A7/A6 need to mark a Strategy revision eligible for contextual selection; A1 must understand that eligibility is not proof of compatibility with a particular activity.
- **Guard → result / non-success:** declarations coherent enough → eligible/effective. Missing material declarations leave it ineligible/indeterminate.
- **AF / sync:** `AF-AUTH`; `SYNC-02` remains activity-owned compatibility/binding.
- **Time / D-H-E:** current/future-use eligibility.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `supported` must be scoped and must not imply universal compatibility.

## SS-A04 — Supersede / Retire / Invalidate

- **Actors + intent/obligation:** A7/A6 need to change future selection eligibility and expose the reason while preserving historical activity bindings; A1 needs clear current-use implications.
- **Guard → result / non-success:** justified future-use status change → exact revision becomes superseded/retired/invalidated as appropriate. No silent fallback substitution is allowed.
- **AF / sync:** `AF-AUTH`; no reactive rewrite of `SYNC-02` historical bindings.
- **Time / D-H-E:** current/future-use status plus historical-as-used view.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `deprecated` must not collapse retire/invalidate/supersede distinctions where material.

---

# 6. Learning action mappings

## LRN-A01 — Propose

- **Actors + intent/obligation:** A1 Data Practitioner primarily. Actor/programmatic consumer must be able to begin an editable Learning intent only when reusable source-informed state is actually desired/required.
- **Guard → result / non-success:** learning intent + relevant Strategy mode → editable Learning occurrence. Direct-generation workflows must not be forced through this action.
- **AF / sync:** `AF-L` and learned workflows; no sync yet.
- **Time / D-H-E:** proposed/editable; ordinary proposal is bounded control-plane state.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `train` is too narrow for all Learning.

## LRN-A02 — Amend pre-commit specification

- **Actors + intent/obligation:** A1 must be able to refine source/scope/bindings/parameters/approximation/dependency/reproducibility intent before commitment and understand that material amendments stale prior validation.
- **Guard → result / non-success:** still pre-commit → proposal changes and affected validation becomes non-current. Post-commit material changes require a new Learning, not amend.
- **AF / sync:** `AF-L`; no synchronization state owner.
- **Time / D-H-E:** proposed/editable only.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `edit` must be blocked/redirected after semantic commitment.

## LRN-A03 — Validate prerequisites / context

- **Actors + intent/obligation:** A1 needs to know whether the proposed Learning can be committed and why; A3/A5/A7 may contribute meaning, operational/dependency, or Strategy facts. Surfaces must show activity-owned compatibility rather than global mutable readiness.
- **Guard → result / non-success:** enough proposal context → ready / ready-with-limitations / incompatible / indeterminate assessment owned by Learning. Missing evidence does not become ready.
- **AF / sync:** `AF-L`, optional `AF-C`; `SYNC-02` and optional `SYNC-03` are relevant; Meaning sufficiency informs later `SYNC-01` binding.
- **Time / D-H-E:** proposed/current assessment; recalculated when material proposal inputs change.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: generic `validation passed` or shared `readiness` state.

## LRN-A04 — Commit

- **Actors + intent/obligation:** A1 must be able to review material commitments and deliberately establish the exact historical Learning basis.
- **Guard → result / non-success:** prerequisite/context validation sufficient + exact material bindings identifiable → immutable semantic commitment. Insufficient/indeterminate mandatory prerequisites block normal commit.
- **AF / sync:** `AF-L`; `SYNC-01`, `SYNC-02`, optional `SYNC-03`; optional `SYNC-14` material provenance recording.
- **Time / D-H-E:** committed historical; exact bindings inspectable later.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `start` must not substitute for semantic commit.

## LRN-A05 — Initiate realization / Mark active

- **Actors + intent/obligation:** A1 initiates committed Learning realization; A5 may operate the realization. Interaction must separate Learning active state from Execution/Attempt details.
- **Guard → result / non-success:** committed Learning + operational realization permitted → Learning records realization underway; Execution, when present, owns operational state.
- **AF / sync:** `AF-L` + `AF-X` when durable Execution is used; `SYNC-04`.
- **Time / D-H-E:** committed/current semantic activity plus separate operational view.
- **Surfaces / vocabulary risk:** S1, S2, S3, S5, S6; risk: `running` must be owner-qualified.

## LRN-A06 — Request cancellation / Resolve cancellation

- **Actors + intent/obligation:** A1 requests semantic cancellation; A5 may participate operationally. Surfaces must distinguish cancellation intent from eventual terminal resolution and expose race outcomes without erasing history.
- **Guard → result / non-success:** cancellation allowed before controlling completion → intent recorded; terminal cancelled only when operational/semantic facts justify. Completion-before-cancel remains completion; unknown stays indeterminate.
- **AF / sync:** `AF-L`; optional `AF-X` with Execution cancellation; optional provenance.
- **Time / D-H-E:** committed current action + historical attempts/results retained.
- **Surfaces / vocabulary risk:** S1, S2, S3, S5, S6; risk: `cancelled` must not be shown immediately upon request.

## LRN-A07 — Fail

- **Actors + intent/obligation:** A1 must understand terminal semantic failure and why no valid same-semantics path can establish intended Learned State; A5 needs distinction from merely failed Attempt.
- **Guard → result / non-success:** Learning can no longer satisfy semantic contract → terminal Learning failure; diagnostics/history remain and no primary usable Learned State is established.
- **AF / sync:** `AF-L`; optional Execution/provenance relations.
- **Time / D-H-E:** committed historical terminal state; failure does not erase attempts.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S6; risk: platform/job failure must not automatically map to Learning failure.

## LRN-A08 — Complete

- **Actors + intent/obligation:** A1 needs an authoritative semantic completion distinct from operational success; A2/A3 may later consume/review the resulting Learned State context.
- **Guard → result / non-success:** committed Learning sufficiently realized + valid reusable source-informed result established → Learning completed and zero/one primary Learned State established. Execution success alone is insufficient.
- **AF / sync:** `AF-L`; `SYNC-05`, optional `SYNC-14`.
- **Time / D-H-E:** terminal historical completion + exact producer/result relationship.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `training succeeded`, `job completed`, `model saved` are not semantic completion by themselves.

---

# 7. Learned State action mappings

## LS-A01 — Establish

- **Actors + intent/obligation:** primarily a system-established consequence of valid Learning completion; A1/A2/A3 need the establishment and producing Learning to be visible without requiring a separate actor gesture.
- **Guard → result / non-success:** producing Learning satisfies semantic completion and result is distinguishable from checkpoint/intermediate state → stable logical Learned State established. Partial/recovery material cannot be promoted by physical existence alone.
- **AF / sync:** `AF-L`; `SYNC-05`; later `AF-GL` may reuse it through `SYNC-06`.
- **Time / D-H-E:** immutable historical result + future-use status dimension; bounded identity/derivation summaries.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `model`, `artifact`, `checkpoint` cannot substitute for Learned State.

## LS-A02 — Restrict

- **Actors + intent/obligation:** A1/A3/A4/A6, where relevant authority exists, need to record a current/future-use limitation without claiming the historical Learned State was necessarily wrong.
- **Guard → result / non-success:** established limitation → restricted future-use state with reason. Uncertain concerns should not be overstated as invalidation.
- **AF / sync:** any family containing Learned State; Generation owns contextual reuse response through `SYNC-06` when used.
- **Time / D-H-E:** current/future-use status + unchanged historical content/derivation.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: `blocked`, `invalid` must not erase distinction from restriction.

## LS-A03 — Retire

- **Actors + intent/obligation:** A1/A6 need to stop ordinary future selection without asserting historical defect; prior Generations remain attributable.
- **Guard → result / non-success:** retirement decision established → retired for ordinary new use.
- **AF / sync:** family containing Learned State; no retroactive `SYNC-06` propagation.
- **Time / D-H-E:** current/future-use retired + preserved historical producer/consumer relationships.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `deleted` or `invalid` overstates retirement.

## LS-A04 — Invalidate

- **Actors + intent/obligation:** A1/A3/A4/A6 need to block ordinary future reliance when a material defect is established while preserving producing history and prior uses.
- **Guard → result / non-success:** material defect/incompatibility → invalid for new reliance with inspectable reason; suspected defect may remain restricted/indeterminate instead.
- **AF / sync:** family containing Learned State; Generation evaluates current reuse compatibility, historical Generations remain unchanged.
- **Time / D-H-E:** current/future-use invalid + preserved historical result.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: invalidation must not imply retroactive mutation of completed Generations.

---

# 8. Generation action mappings

## GEN-A01 — Propose / Request

- **Actors + intent/obligation:** A1 primarily; programmatic callers need to state requested logical output, quantity/scope, Conditions and proposed basis without being forced into Learning/Evaluation/Execution/Provenance when those capabilities are absent.
- **Guard → result / non-success:** distinguishable synthesis intent → editable Generation proposal. Insufficiently specified intent remains proposed/incomplete rather than committed.
- **AF / sync:** `AF-GD` or `AF-GL`; optional `AF-C`, `AF-GE`, `AF-X`, `AF-P` only when requested capability needs them.
- **Time / D-H-E:** proposed/editable; bounded request metadata.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `sample` must not imply source sampling; `run` must not erase Generation identity.

## GEN-A02 — Amend / Withdraw pre-commit

- **Actors + intent/obligation:** A1 must be able to revise/withdraw intent before commitment and see stale validation invalidated by material edits.
- **Guard → result / non-success:** still pre-commit → proposal changes or is withdrawn; no completed result is created. Post-commit material changes require a new Generation.
- **AF / sync:** all Generation variants.
- **Time / D-H-E:** proposed/editable only.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `edit job` must not mutate committed semantics.

## GEN-A03 — Validate proposed Generation

- **Actors + intent/obligation:** A1 needs a reasoned compatibility/applicability/handling/feasibility assessment; A3/A4/A5/A7 may supply semantic, rule, risk, runtime or Strategy facts. Assessment remains Generation-owned.
- **Guard → result / non-success:** enough proposal context → ready/limited/incompatible/indeterminate dimensions as appropriate. Mandatory unsupported/unknown conditions block normal commitment where determination is required.
- **AF / sync:** `AF-GD` or `AF-GL`; `SYNC-02`, optional `SYNC-03`, and `SYNC-06` only for learned-state-assisted reuse.
- **Time / D-H-E:** proposed/current assessment, invalidated by material proposal changes.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: generic `validation passed`, `compatible=true`, `ready` without owner/reason.

## GEN-A04 — Commit

- **Actors + intent/obligation:** A1 must review and deliberately freeze the exact success-defining Generation context; programmatic automation must receive the same material semantic contract.
- **Guard → result / non-success:** required validation sufficient + exact basis identifiable → immutable committed Generation. Material indeterminacy blocks commit where required.
- **AF / sync:** all Generation variants; `SYNC-01`, `SYNC-02`, optional `SYNC-03`, optional learned-state `SYNC-06`; optional `SYNC-14` provenance recording.
- **Time / D-H-E:** committed historical exact basis; later status changes of authorities do not rewrite it.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `submit`, `start`, `run` must not obscure semantic commitment.

## GEN-A05 — Initiate fulfillment / Mark fulfilling

- **Actors + intent/obligation:** A1 initiates fulfillment; A5 may operate execution. Surfaces must show Generation-level fulfillment separately from Attempt/platform progress.
- **Guard → result / non-success:** committed and permitted → Generation fulfilling; detailed operational realization remains Execution-owned if present.
- **AF / sync:** Generation variants; `SYNC-07` only with `AF-X`.
- **Time / D-H-E:** committed/current semantic activity + separate operational state.
- **Surfaces / vocabulary risk:** S1, S2, S3, S5, S6; risk: `running` owner ambiguity.

## GEN-A06 — Record partial / candidate result state

- **Actors + intent/obligation:** A1/A2 and downstream automation must be able to encounter physically present material without confusing it with authoritative completed output.
- **Guard → result / non-success:** identifiable fulfillment material exists → partial or complete candidate recorded as non-final where obligations remain. Material existence alone cannot promote completion.
- **AF / sync:** all Generation variants; **no active `SYNC-08`**—this is Generation-local state.
- **Time / D-H-E:** committed/current candidate state; candidate may later become abandoned, superseded by same-Generation recovery, or contribute to completion.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: `output`, `dataset ready`, `artifact complete` can falsely imply finality.

## GEN-A07 — Enter awaiting-required-validation

- **Actors + intent/obligation:** A1/A4/A2 must understand that physical production may be complete while mandatory semantic completion evidence remains outstanding.
- **Guard → result / non-success:** candidate sufficient for outstanding checks but requirements not established → awaiting-required-validation. Missing/indeterminate evidence remains pending/non-success.
- **AF / sync:** primarily `AF-GE` or other Generation with deferred mandatory checks; `SYNC-13` may later participate.
- **Time / D-H-E:** current non-final semantic state; candidate remains non-authoritative.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: generic `complete`, `done`, `validation pending` without identifying Generation ownership/requirements.

## GEN-A08 — Evaluate completion basis

- **Actors + intent/obligation:** A1 needs requirement-specific explanation of whether committed completion conditions are satisfied; A4 may inspect Evidence; A2 may need resulting limitations. The interaction must show that Generation owns the decision and Evidence supports only scoped claims.
- **Guard → result / non-success:** candidate + mandatory completion inputs available at required strength → Generation-owned satisfied/failed/indeterminate assessment. Missing/weak Evidence cannot be promoted to success.
- **AF / sync:** all Generation where completion conditions need resolution; `SYNC-13` only for evidence-gated completion; optional Constraint relation already represented through its handling/basis.
- **Time / D-H-E:** current completion assessment bound to exact committed requirements and Evidence revisions.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `approved`, `passed`, `quality score` must not replace requirement-specific completion basis.

## GEN-A09 — Complete / Complete with limitations

- **Actors + intent/obligation:** A1/A2 need one authoritative completed logical output state and any permitted limitations; automation must not infer completion from physical files or Execution alone.
- **Guard → result / non-success:** all mandatory committed conditions satisfied; explicit limitations permitted where non-mandatory → zero/one authoritative completed logical output. Mandatory failure/indeterminacy prevents completion.
- **AF / sync:** all Generation variants; optional `SYNC-13` may have supplied Evidence; optional `SYNC-14` records material relationships.
- **Time / D-H-E:** terminal historical completion; current-use status may later differ without rewriting historical completion.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: `job succeeded`, `files written`, `validated`, `approved` are insufficient synonyms.

## GEN-A10 — Fail

- **Actors + intent/obligation:** A1 must understand semantic terminal failure and retained non-final candidate material; A5 must distinguish it from operational failure.
- **Guard → result / non-success:** same-semantics fulfillment impossible or mandatory requirement failed with no valid recovery → Generation failed; candidate remains non-final.
- **AF / sync:** all Generation variants; optional Execution/Evidence/Constraint facts inform but do not own the transition.
- **Time / D-H-E:** terminal historical semantic failure with retained attempts/candidates as non-final history.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S6; risk: execution failure alone cannot automatically label Generation failed.

## GEN-A11 — Request / Resolve cancellation

- **Actors + intent/obligation:** A1 requests cancellation; A5 may operate it. Interaction must expose cancellation intent, race resolution, and completed-before-cancel cases.
- **Guard → result / non-success:** cancellation allowed before controlling semantic completion → intent; cancelled terminal only when known. Unknown race stays indeterminate; completed-before-cancel remains completed.
- **AF / sync:** all Generation variants; optional `AF-X` operational cancellation relation.
- **Time / D-H-E:** current intent + eventual historical terminal resolution; no candidate promotion on cancellation.
- **Surfaces / vocabulary risk:** S1, S2, S3, S5, S6; risk: request acknowledgement must not be labeled terminal cancellation.

---

# 9. Constraint action mappings

## CON-A01 — Declare draft rule

- **Actors + intent/obligation:** A3 Data Owner/Steward primarily; A1/A4 may contribute domain/risk rules. Actors must be able to state prescriptive rule, scope, authority and requirement semantics distinctly from descriptive Meaning and Generation Conditions.
- **Guard → result / non-success:** identifiable prescriptive rule/scope/authority → draft Constraint revision; ambiguity remains draft/unresolved rather than universally enforced.
- **AF / sync:** `AF-AUTH`; consumed only where `AF-C` relation exists.
- **Time / D-H-E:** proposed/editable rule revision.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `schema`, `validation rule`, `condition` must not collapse semantic distinctions.

## CON-A02 — Revise / Correct

- **Actors + intent/obligation:** A3/A1 must change material rule semantics by new revision while retaining exact historical bindings.
- **Guard → result / non-success:** material change → distinguishable new Constraint revision, not in-place edit of a bound revision.
- **AF / sync:** `AF-AUTH`; later contextual use via optional `SYNC-03`.
- **Time / D-H-E:** current new revision + historical prior rule.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: destructive `edit` language.

## CON-A03 — Make effective

- **Actors + intent/obligation:** A3/A1 need to mark a rule eligible for contextual consideration while preserving that effectiveness is not universal applicability/satisfaction.
- **Guard → result / non-success:** coherent rule/scope/prereqs → effective/eligible for new binding.
- **AF / sync:** `AF-AUTH`; `SYNC-03` occurs only in consuming activity contexts.
- **Time / D-H-E:** current/future-use eligibility.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `enforced globally`, `passed` must not follow from effectiveness.

## CON-A04 — Supersede / Retire / Invalidate

- **Actors + intent/obligation:** A3/A1/A4 need future-use status changes with reasons while historical activities stay governed by exact bound revisions.
- **Guard → result / non-success:** justified status change → new-selection eligibility changes; no retroactive rewrite.
- **AF / sync:** `AF-AUTH`; no permanent `SYNC-03` subscription.
- **Time / D-H-E:** current/future status + historical binding preservation.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: generic `disabled` hides material distinctions.

---

# 10. Evaluation Criterion action mappings

## CRIT-A01 — Define draft Criterion

- **Actors + intent/obligation:** A1/A4/A3 primarily. Actors must be able to state the evaluative question/property, scope, reference context and answer interpretation independently of any available metric/method.
- **Guard → result / non-success:** identifiable evaluative question/scope → draft Criterion revision; unavailable metric does not erase the question.
- **AF / sync:** `AF-AUTH` and `AF-E`; no Evaluation exists merely from definition.
- **Time / D-H-E:** proposed/editable question.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `metric`, `test`, `threshold` must not replace Criterion.

## CRIT-A02 — Revise / Correct

- **Actors + intent/obligation:** A1/A4/A3 must create a new Criterion revision when question/scope/reference/tolerance/answer-strength changes, retaining historical Evidence's exact question.
- **Guard → result / non-success:** material change → distinguishable revision.
- **AF / sync:** `AF-AUTH`; later Evaluation binds through `SYNC-09`.
- **Time / D-H-E:** current new revision + historical exact prior Criterion.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: editing a metric configuration must not silently rewrite historical Criterion.

## CRIT-A03 — Make effective

- **Actors + intent/obligation:** A1/A4 need to mark a sufficiently coherent Criterion eligible for proposed Evaluation without implying a method.
- **Guard → result / non-success:** question/scope/reference/answer-strength coherent → eligible for selection; no method compatibility claimed.
- **AF / sync:** `AF-AUTH`/`AF-E`; `SYNC-09/10` occur in Evaluation context.
- **Time / D-H-E:** current/future-use eligibility.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `test enabled` must not imply method sufficiency.

## CRIT-A04 — Supersede / Retire / Invalidate

- **Actors + intent/obligation:** A1/A4/A3 need current/future-use status changes while preserving what historical Evidence actually answered.
- **Guard → result / non-success:** justified status change → selection eligibility changes; historical Evidence remains tied to old revision.
- **AF / sync:** `AF-AUTH`; no retroactive rewrite of `SYNC-09` historical bindings.
- **Time / D-H-E:** current/future status + historical Criterion/Evidence truth.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5; risk: `metric deprecated` is insufficiently precise.

---

# 11. Evaluation action mappings

## EVAL-A01 — Propose

- **Actors + intent/obligation:** A1/A4 primarily; A2 may request downstream evaluation context. Actors must be able to begin an editable examination intent with Criterion/subject/method context without establishing Evidence.
- **Guard → result / non-success:** evaluative intent identifiable → proposed Evaluation; no finding exists merely from proposal.
- **AF / sync:** `AF-E`, and `AF-GE` when serving Generation gating.
- **Time / D-H-E:** proposed/editable.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `run metric`, `score` can hide Criterion/subject/method distinctions.

## EVAL-A02 — Amend pre-commit specification

- **Actors + intent/obligation:** A1/A4 must refine Criterion/input/reference/method/scope/coverage/uncertainty before commitment and understand material edits stale prior method validation.
- **Guard → result / non-success:** still pre-commit → proposal changes; post-commit material change requires a new Evaluation.
- **AF / sync:** `AF-E`/`AF-GE`.
- **Time / D-H-E:** proposed/editable.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `edit evaluation run` after commit.

## EVAL-A03 — Validate method / context

- **Actors + intent/obligation:** A1/A4 need to understand whether selected method can answer the Criterion at represented strength under subject/reference/scope/dependency conditions; A7 may expose method capability.
- **Guard → result / non-success:** enough proposal context → Evaluation-owned compatible/sufficient, incompatible or indeterminate assessment. Execution convenience cannot make method sufficient.
- **AF / sync:** `AF-E`/`AF-GE`; `SYNC-10`, optional `SYNC-03` where reusable Constraint applies.
- **Time / D-H-E:** proposed/current assessment; changes when method/context changes.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: generic `valid`, `supported` without claim-strength scope.

## EVAL-A04 — Commit

- **Actors + intent/obligation:** A1/A4 must review and freeze exact Criterion, subject/reference, method, scope, coverage, uncertainty and dependencies.
- **Guard → result / non-success:** validation sufficient + exact basis identifiable → committed Evaluation; material indeterminacy blocks commit where required.
- **AF / sync:** `AF-E`/`AF-GE`; `SYNC-09` plus method context established under `SYNC-10`; optional `SYNC-03`, optional provenance.
- **Time / D-H-E:** committed historical exact examination basis.
- **Surfaces / vocabulary risk:** S1, S2, S5; risk: `execute metric` must not substitute for semantic commit.

## EVAL-A05 — Initiate / Mark evaluating

- **Actors + intent/obligation:** A1/A4 initiate examination; A5 may operate durable execution. Evaluation-level examination state must remain separate from Attempt progress.
- **Guard → result / non-success:** committed and permitted → evaluating; Execution owns operational realization where present.
- **AF / sync:** `AF-E`/`AF-GE`; `SYNC-11` only with `AF-X`.
- **Time / D-H-E:** committed/current semantic activity + separate operational state.
- **Surfaces / vocabulary risk:** S1, S2, S3, S5, S6; risk: `running` ambiguity.

## EVAL-A06 — Request / Resolve cancellation

- **Actors + intent/obligation:** A1/A4 request; A5 may operate cancellation. Partial diagnostics must remain non-Evidence unless the Evaluation independently satisfies completion.
- **Guard → result / non-success:** cancellation permitted before semantic completion → intent; terminal cancellation only when justified; completion-before-cancel/unknown races remain truthful.
- **AF / sync:** `AF-E`/`AF-GE`; optional `AF-X` Execution cancellation.
- **Time / D-H-E:** current intent + historical outcome; partial diagnostics remain non-authoritative.
- **Surfaces / vocabulary risk:** S1, S2, S3, S5, S6; risk: cancellation request ≠ terminal cancelled.

## EVAL-A07 — Complete / Complete with limitations

- **Actors + intent/obligation:** A1/A4/A2 need authoritative valid-examination completion with interpretable scope/limitations and zero-or-more Evidence findings; favorable subject outcome is not required.
- **Guard → result / non-success:** bound examination validly realized + supportable claim strength + interpretable assumptions/coverage → Evaluation completed and Evidence may be established. Unsupported strength/invalid method blocks completion at that claim.
- **AF / sync:** `AF-E`/`AF-GE`; `SYNC-12`, optional `SYNC-14`.
- **Time / D-H-E:** terminal historical examination + produced Evidence identities.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: `passed` or `successful metric` must not imply favorable finding.

## EVAL-A08 — Fail

- **Actors + intent/obligation:** A1/A4 need to know that the committed examination cannot validly establish interpretable Evidence at intended/allowed strength; A5 needs distinction from Attempt failure.
- **Guard → result / non-success:** semantic examination contract cannot be met under same specification → terminal Evaluation failure; diagnostics/numbers do not become Evidence.
- **AF / sync:** `AF-E`/`AF-GE`; Execution operational facts may inform but do not own failure.
- **Time / D-H-E:** terminal historical semantic failure; diagnostics remain non-Evidence.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S6; risk: a failed platform task is not automatically Evaluation failure, and partial metric output is not Evidence.

---

# 12. Evidence action mappings

## EVD-A01 — Establish

- **Actors + intent/obligation:** primarily a system-established consequence of a valid completed Evaluation; A1/A2/A4 need each finding, its exact question/method/scope/strength/uncertainty/limitations and producing Evaluation to be inspectable.
- **Guard → result / non-success:** valid Evaluation + independently interpretable finding → immutable Evidence identity. Unsupported or merely diagnostic material cannot be established as Evidence answering the Criterion.
- **AF / sync:** `AF-E` and optionally `AF-GE`; `SYNC-12`; later `SYNC-13` may let Generation consume it.
- **Time / D-H-E:** immutable historical finding plus separate current applicability status.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: `metric result`, `score`, `approval`, `guarantee` may overstate Evidence.

## EVD-A02 — Mark superseded / stale / inapplicable

- **Actors + intent/obligation:** A1/A4/A2 need to express that a historical finding remains true-as-recorded but should not be relied on for a current context, and understand why.
- **Guard → result / non-success:** current context establishes newer/preferred evidence or non-applicability → current-use/applicability status changes without editing finding. Uncertain applicability remains indeterminate.
- **AF / sync:** family containing Evidence; Generation or external consumers own their own current reliance decisions.
- **Time / D-H-E:** current applicability + immutable historical finding; later status must not rewrite completed historical Generation.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: `expired` or `failed` must not erase historical finding semantics.

## EVD-A03 — Invalidate

- **Actors + intent/obligation:** A1/A4 need to flag a material methodological/data defect that undermines current reliance while retaining auditable history and downstream historical bindings.
- **Guard → result / non-success:** material defect established → invalid for reliance; defect and original finding remain. Suspected defect stays appropriately uncertain rather than silently invalidating.
- **AF / sync:** family containing Evidence; no reactive rewrite of historical `SYNC-13` Generation completion.
- **Time / D-H-E:** current invalidity + historical finding preserved.
- **Surfaces / vocabulary risk:** S1, S2, S4, S5, S7; risk: `retracted` may be acceptable only if it does not imply historical deletion; `Generation invalid` is not an automatic consequence.

---

# 13. Execution action mappings

## EXE-A01 — Prepare

- **Actors + intent/obligation:** A5 Platform Operator and A1 activity owner need a logical operational realization associated with the exact committed parent without implying any Attempt/job has succeeded.
- **Guard → result / non-success:** committed parent activity requires durable realization → prepared Execution bound to exact parent. If no durable Execution capability is used, parent workflow must remain valid without fabricating one.
- **AF / sync:** `AF-X` with one of `AF-L`, Generation, or `AF-E`; `SYNC-04`, `SYNC-07`, or `SYNC-11` according to parent.
- **Time / D-H-E:** current operational preparation attached to committed historical parent.
- **Surfaces / vocabulary risk:** S1, S3, S5, S6; risk: `job`, `run` must not erase logical Execution versus platform realization.

## EXE-A02 — Accept / Queue

- **Actors + intent/obligation:** A5/A1 must understand work is operationally eligible but waiting/deferred, not semantically blocked or failed.
- **Guard → result / non-success:** prepared Execution eligible for admission → queued/pending. Incompatibility/denial/missing prerequisite must not be mislabeled queueing.
- **AF / sync:** `AF-X`; parent synchronization already establishes parent binding.
- **Time / D-H-E:** current operational state.
- **Surfaces / vocabulary risk:** S1, S3, S5, S6; risk: `pending` without reason can collapse queued/blocked/indeterminate.

## EXE-A03 — Start Attempt

- **Actors + intent/obligation:** A5 operates; A1 can observe. A new Attempt must be distinguishable from Execution and platform job identity and must preserve same committed parent semantics.
- **Guard → result / non-success:** current authority permits work + same-semantic Attempt can be distinguished → new Attempt/running state. Unverified recovery authority or semantic mutation blocks same-Execution start.
- **AF / sync:** `AF-X`.
- **Time / D-H-E:** current Attempt + ordered historical Attempt lineage.
- **Surfaces / vocabulary risk:** S1, S3, S5, S6; risk: `rerun` must not imply new domain activity or erase prior Attempt.

## EXE-A04 — Record Attempt outcome

- **Actors + intent/obligation:** primarily system/operator-established; A5/A1 must be able to see exact Attempt outcome and understand that it does not decide parent semantic outcome.
- **Guard → result / non-success:** sufficient operational evidence → classified Attempt outcome at supported strength; ambiguity remains indeterminate.
- **AF / sync:** `AF-X`; no domain completion transfer.
- **Time / D-H-E:** historical Attempt fact; bounded diagnostics/reference may drill down.
- **Surfaces / vocabulary risk:** S1, S3, S4, S5, S6; risk: `success`, `failure` must be qualified as Attempt/operational.

## EXE-A05 — Enter recovery pending

- **Actors + intent/obligation:** A5/A1 need to know same-Execution recovery may remain possible but a new Attempt is not yet authorized/qualified.
- **Guard → result / non-success:** no progressing Attempt + recovery potentially valid → recovery-pending. Unknown side effects/authority stay explicit.
- **AF / sync:** `AF-X`.
- **Time / D-H-E:** current operational state with historical Attempts preserved.
- **Surfaces / vocabulary risk:** S1, S3, S5, S6; risk: `retrying`/`resuming` before qualification.

## EXE-A06 — Request cancellation

- **Actors + intent/obligation:** A1 or A5 may request according to product authority; surfaces must show intent separately from terminal cancellation and protect already-established domain results.
- **Guard → result / non-success:** Execution not controlling-terminal → cancellation intent. Race may later resolve cancelled/completed-before-cancel/failed/indeterminate.
- **AF / sync:** `AF-X`; parent domain cancellation remains separately owned.
- **Time / D-H-E:** current operational intent + preserved history.
- **Surfaces / vocabulary risk:** S1, S3, S5, S6; risk: `cancelled` on request acknowledgement.

## EXE-A07 — Retry / Resume by starting a new Attempt

- **Actors + intent/obligation:** A5 operates; A1 needs qualification explanation. Interaction must demonstrate same committed parent semantics, valid authority, safe/reconciled prior effects and compatible recovery material where used.
- **Guard → result / non-success:** retry/resume eligibility established → new Attempt within same Execution. Material semantic change requires new parent activity; unresolved safety/authority blocks or leaves indeterminate.
- **AF / sync:** `AF-X`; no new `SYNC-04/07/11` parent activity unless there is actually a new parent.
- **Time / D-H-E:** current recovery action + immutable prior Attempt history.
- **Surfaces / vocabulary risk:** S1, S3, S5, S6; risk: `retry` as generic button without eligibility semantics.

## EXE-A08 — Reconcile indeterminate state

- **Actors + intent/obligation:** A5/A1 need to narrow unknown operational/side-effect state only as strongly as independent evidence supports, particularly after recovery.
- **Guard → result / non-success:** ambiguous state + sufficient evidence → narrower operational classification; unresolved uncertainty stays explicit.
- **AF / sync:** `AF-X`; optional provenance records material reconstruction/relationships.
- **Time / D-H-E:** current classification may include reconstructed historical knowledge; disclose reconstruction basis where allowed.
- **Surfaces / vocabulary risk:** S1, S3, S4, S5, S6; risk: `repair`, `assume failed`, `assume success` without evidence.

## EXE-A09 — Complete operationally

- **Actors + intent/obligation:** A5/A1 must see that operational endpoint is reached while parent Learning/Generation/Evaluation still owns semantic completion.
- **Guard → result / non-success:** operational contract reached with no unresolved operational defect → Execution completed. Parent may still be pending/failed/awaiting validation.
- **AF / sync:** `AF-X`; parent relation remains `SYNC-04`, `07`, or `11`; no semantic-completion ownership transfer.
- **Time / D-H-E:** terminal operational history + separate parent semantic state.
- **Surfaces / vocabulary risk:** S1, S3, S4, S5, S6; risk: bare `completed`/`100%` must not imply domain completion.

## EXE-A10 — Fail terminally

- **Actors + intent/obligation:** A5/A1 need to know no valid same-semantics retry/resume remains; parent concept receives the fact but decides its own semantic terminal state.
- **Guard → result / non-success:** no safe valid same-semantics recovery path → Execution failed terminally.
- **AF / sync:** `AF-X`; parent semantic failure remains separate.
- **Time / D-H-E:** terminal operational history.
- **Surfaces / vocabulary risk:** S1, S3, S4, S5, S6; risk: `Generation failed`/`Learning failed`/`Evaluation failed` must not be inferred solely from Execution failure.

## EXE-A11 — Cancel terminally

- **Actors + intent/obligation:** A5/A1 need a truthful terminal operational cancellation classification while committed parent history and already-established domain results remain intact.
- **Guard → result / non-success:** cancellation has taken effect sufficiently → Execution cancelled. Unknown cancellation state remains indeterminate until reconciled.
- **AF / sync:** `AF-X`; parent domain cancellation is separately resolved.
- **Time / D-H-E:** terminal operational history.
- **Surfaces / vocabulary risk:** S1, S3, S4, S5, S6; risk: operational cancellation must not automatically rewrite parent semantic state.

---

# 14. Provenance action mappings

## PROV-A01 — Record typed relationship

- **Actors + intent/obligation:** primarily system-established at material transitions/relationships; A1/A2/A3/A4/A5/A6 need later explainability. The interaction must expose relation type and stable historical references without copying or owning upstream state.
- **Guard → result / non-success:** source facts/references established strongly enough + relation material → typed provenance assertion appended. Missing/uncertain source facts cannot be fabricated by Provenance.
- **AF / sync:** `AF-P`; `SYNC-14`.
- **Time / D-H-E:** historical relationship assertion; disclosure may limit details while preserving truthful existence semantics according to policy; bounded graph/path summaries with drill-down.
- **Surfaces / vocabulary risk:** S1, S4, S5, S7; risk: `history`, `lineage`, `source truth` must not make Provenance canonical owner of upstream facts.

## PROV-A02 — Correct / Supersede / Invalidate provenance assertion

- **Actors + intent/obligation:** A6/A1/A3/A4 where relevant evidence/authority exists need to correct relationship assertions audibly without erasing the prior assertion or changing source-concept state.
- **Guard → result / non-success:** prior assertion known incomplete/incorrect/unsuitable + corrective basis → auditable correction/supersession/invalidation. Insufficient corrective evidence leaves uncertainty explicit.
- **AF / sync:** `AF-P`; no reverse mutation of source concepts.
- **Time / D-H-E:** current relationship applicability/correctness plus preserved assertion history; reconstructed corrections identified as such where applicable.
- **Surfaces / vocabulary risk:** S1, S4, S5; risk: `fix source history` or destructive `edit lineage` must not imply upstream mutation.

---

# 15. Cross-concept action-mapping rules

## 15.1 Validation is consumer-owned

The action map preserves:

```text
Strategy facts      -> Learning / Generation compatibility assessment
Constraint facts    -> Learning / Generation / Evaluation applicability/handling
Learned State facts -> Generation reuse assessment
Criterion facts     -> Evaluation method sufficiency assessment
Evidence finding    -> Generation completion-basis assessment or external decision input
```

There is no mapped global `Validate`, `Compatibility`, `Readiness`, or `Approval` command owner.

## 15.2 Synchronization does not receive a control

A synchronization ID may be relevant to an action record, but no record maps to “execute SYNC-xx”.

Actors encounter the participating concept-owned actions and resulting facts.

## 15.3 Result-establishment actions may be system-established

`LearnedState.Establish`, `Evidence.Establish`, `Execution.RecordAttemptOutcome`, and `Provenance.RecordTypedRelationship` demonstrate why conceptual command does not mean direct user control.

A valid mapping may require:

- an initiating actor-visible command on another concept;
- automatic/synchronized establishment;
- actor-visible result/status inspection;
- programmatic observability;
- no dedicated physical control at all.

## 15.4 Cancellation is two-stage where authority says so

Learning, Generation, Evaluation and Execution all preserve request/intent versus resolved terminal state.

A physical surface that collapses “request accepted” into “cancelled” would violate the mapping.

## 15.5 Operational actions remain Execution-owned

Retry/resume/reconcile/Attempt outcomes remain Execution actions. Learning, Generation and Evaluation may expose related semantic consequences but do not absorb those actions into a generic `Run` lifecycle.

## 15.6 Candidate and diagnostic material are not authoritative results

Generation candidate state and failed/partial Evaluation diagnostics must remain distinguishable from completed Generation output and Evidence establishment respectively.

`SYNC-08` is not resurrected by mapping.

## 15.7 Current-use status change does not rewrite historical use

Supersede/retire/restrict/invalidate/stale actions change current/future interpretation or eligibility according to the owning concept. They do not create live reactive mutation of prior committed activities.

---

# 16. Actor coverage result

The action map covers all seven 010-A actor lenses without inventing one interface per role.

```text
A1 Data Practitioner                 broad author/operate/review coverage
A2 Synthetic Data Consumer           result/Evidence/history handoff coverage
A3 Data Owner / Steward              Meaning/Constraint/history/review coverage
A4 Privacy/Risk/Governance Reviewer  Criterion/Evidence/risk/history coverage
A5 Platform Operator                 Execution/recovery/operational coverage
A6 Library Maintainer                Strategy/evolution/provenance/misfit coverage
A7 Synthesizer/Extension Author      Strategy/method/dependency declaration coverage
```

Role coverage expresses needs, not authorization or product persona design.

---

# 17. Application-family action coverage

The 66 action records preserve the current family rather than forming one mandatory workflow.

## Authority-only

Data Meaning, Strategy, Constraint and Criterion authoring/status actions can exist independently where Phase 009 permits `AF-AUTH`.

## Direct Generation

Required semantic action path can remain:

```text
Generation propose
  -> validate
  -> commit
  -> fulfill / candidate
  -> completion-basis resolution
  -> complete | fail | cancel
```

No Learning/Learned State action is fabricated.

## Learned-state-assisted Generation

Adds the legitimate Learning/Learned State lifecycle and Generation reuse assessment/binding; Learned State is not mutated by selection.

## Evaluation-focused

Criterion/Evaluation/Evidence actions can operate without Generation where valid.

## Evidence-gated Generation

Generation candidate/awaiting-validation/completion-basis actions compose with Evaluation/Evidence while Generation retains completion ownership.

## Execution-bearing variants

Execution actions appear only with `AF-X`; Execution-light valid variants do not receive fake Attempts/jobs.

## Provenance-bearing variants

Provenance recording/correction appears only with `AF-P`; concept-local history remains authoritative without Provenance capability.

---

# 18. Coverage ledger after 010-B

## Ledger A — concept behavior coverage

All normalized command groups:

```text
66 / 66  SEMANTICALLY MAPPED
```

Per concept:

```text
Data Meaning             7 / 7
Synthesis Strategy       4 / 4
Learning                 8 / 8
Learned State            4 / 4
Generation              11 / 11
Constraint               4 / 4
Evaluation Criterion     4 / 4
Evaluation               8 / 8
Evidence                 3 / 3
Execution                11 / 11
Provenance               2 / 2
```

Query/state/history inspection coverage remains for 010-C.

## Current coverage-state advancement

For action subjects only:

```text
SOURCE IDENTIFIED -> SEMANTICALLY MAPPED
```

No action mapping is yet claimed `LINGUISTICALLY ALIGNED`, `SURFACE-MAPPED`, `FAMILY-REPLAYED`, or `PARITY-VALIDATED`; later subgroups own those stages.

---

# 19. Mapping-misfit and upstream reopen audit

010-B finds no action that requires:

- a new accepted concept;
- a concept merge/split/rename;
- new inclusion-dependence edge;
- new synchronization;
- resurrected `SYNC-08`;
- synchronization-owned state;
- global Workflow/Run/Artifact/Validation/Quality/Approval authority;
- mandatory full-suite workflow.

Current result:

```text
J1 local concept-specification blocker    NONE FOUND
J2 purpose/catalog/boundary blocker       NONE FOUND
J3 dependence/composition blocker         NONE FOUND
010-B local action-mapping blocker        NONE FOUND
```

Physical-surface awkwardness, if discovered later, belongs to 010-E/G unless it proves a genuine upstream defect.

---

# 20. Methodology disposition

F1 now has a complete surface-neutral semantic action mapping for the current concept catalog:

```text
F1  CURRENTLY CLOSED FOR SEMANTIC ACTION MAPPING
    66 / 66 normalized command groups mapped
    final Phase 010 consolidation remains 010-H
```

This does not close F4 physical interaction mapping or F5 parity.

F2 remains pending 010-C; F3 remains pending 010-D; F4 remains pending 010-E/F; F5 remains pending 010-G.

---

# 21. Representation / implementation boundary

Nothing in this action map prescribes:

- one method/endpoint/command/button per action;
- one resource type per concept;
- one event per transition;
- one transaction per synchronization;
- one database status enum;
- one UI page per lifecycle;
- one service per concept;
- an implementation Workflow/Run abstraction.

The mapping authority states semantic interaction obligations only.

---

# 22. Current next boundary

**010-C — Concept State, Query, History & Explanation → Inspection Mapping** is next eligible after 010-B consolidation/status propagation.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
