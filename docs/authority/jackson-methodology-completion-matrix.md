---
type: Design Authority
title: Jackson Methodology Completion Matrix
status: active
---

# Jackson Methodology Completion Matrix

## Purpose

Provide the current, conservative completion ledger for SYNGAN's remaining Daniel Jackson-style concept-design work.

This matrix prevents historical phase labels, detailed architecture, implementation plans, code, tests, or a previously positive engineering-readiness audit from being mistaken for proof that the current concept design or whole design is complete.

It is governed by:

- [Concept Design Methodology](design-methodology.md);
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md);
- current problem, concept, synchronization and experience authority.

## Controlling implementation posture

Until Phase 014 positively passes the whole-design readiness gate:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

No row in this matrix, by itself, can change that posture.

## Completion-state vocabulary

The matrix uses these states deliberately:

- **CURRENTLY CLOSED** — the obligation is sufficiently established in current upstream authority for the present design stage. A later discovered misfit may still reopen it.
- **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** — substantial prior work exists, but the latest design has not yet been replayed against the fuller Jackson rubric.
- **PARTIAL** — relevant work exists, but one or more material Jackson obligations are not explicit or not consolidated.
- **OPEN** — the required Jackson analysis has not yet been performed as a dedicated current-state activity.
- **DOWNSTREAM / PENDING RECONCILIATION** — useful representation or architecture design exists but cannot become final until the completed concept design is known.
- **HISTORICAL / NON-AUTHORITATIVE FOR COMPLETION** — implementation planning, executable scaffold, tests, CI, or historical decisions may provide evidence or counterexamples but cannot satisfy an unfinished design obligation merely by existing.

A phase being historically marked `complete` does not automatically mean its subject is **CURRENTLY CLOSED** under this matrix.

## Artifact authority classes

### Class A — current upstream design authority

May define current product functionality and conceptual meaning:

- `docs/authority/` methodology and active cross-cutting design authority;
- `docs/problem/` current problem knowledge;
- `docs/concepts/` accepted concept specifications;
- `docs/synchronizations/` accepted synchronization authority;
- current concept-dependence/composition authority once Phase 009 creates it;
- current concept-mapping/experience authority once Phase 010 reconciles it.

### Class B — current supporting design evidence

May inform, challenge, or justify Class A authority but does not silently override it:

- discovery records;
- completed phase records;
- actor/workflow analyses;
- adversarial scenario analyses;
- terminology/domain references;
- design probes and counterexamples.

### Class C — downstream representation/architecture evidence

The Phase 004, 006 and 007 architecture corpus remains valuable, but until Phase 013 it is downstream evidence rather than proof of concept-design completion.

If upstream concept design changes, Class C must be reconciled to it. Architecture detail cannot veto an upstream design correction merely because it is mature.

### Class D — historical implementation-planning/executable evidence

Includes:

- Phase 005 implementation planning;
- Phase 006 implementation-planning reconciliation;
- 007-A/007-B/007-C implementation/bootstrap authorities and scaffold;
- current `src/`, tests, Import Linter rules, tooling, dependency lock and CI;
- the historical 007-K implementation-reentry conclusion.

Class D may expose feasibility concerns or design misfits. It cannot make implementation ready, define unfinished concepts, or become an executable design constraint during Phases 008-014.

## Jackson completion matrix

| ID | Methodology obligation | Evidence through Phase 007 | Current state | Owning closure phase |
|---|---|---|---|---|
| A1 | Application problem, actors, needs, outcomes and environmental constraints | Phase 001 problem/purpose work plus later scale, recovery, privacy and topology refinements | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-B |
| A2 | Distinct purpose/justification for every accepted concept | Phase 001 candidate review and accepted concept purposes | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-B |
| A3 | Problem/outcome → concept traceability and absence consequence | Distributed across Phase 001 and concept documents; not one current traceability ledger | **PARTIAL** | 008-B |
| B1 | Divergent candidate concept discovery | Phase 001-D candidate discovery | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-G |
| B2 | Candidate reduction, merger, subordination, defer/reject decisions | Phase 001-E and later Phase 006 reviews | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-G |
| B3 | Independence and appropriate domain genericity | Phase 001-E/F/G plus later audits | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-F |
| B4 | Explicit familiarity/reuse comparison | Some analogy/genericity reasoning exists, but no systematic final-catalog familiarity pass | **PARTIAL** | 008-F |
| B5 | Missing-concept, accidental god-concept and representation-leakage audit | Strong repeated anti-god-concept work, but latest deferred/rejected set has not been replayed as one current audit | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-G |
| C1 | Concept name and distinct purpose | Present for all accepted concepts | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-B/008-F |
| C2 | Operational principle demonstrating purpose | Phase 001-F and concept specifications provide OPs | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-E |
| C3 | Complete conceptual state model | Phase 002 concept specifications are substantial; later 006/007 findings may require normalization | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-C |
| C4 | Conceptual actions | Present in accepted concept specs but not yet normalized after later design refinements | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-D |
| C5 | Conceptual queries/observations | Actor inspection exists strongly in experience work, but query surfaces are unevenly explicit in individual concept specs | **PARTIAL** | 008-D |
| C6 | Preconditions/effects/postconditions sufficient for behavioral reasoning | Present unevenly; synchronizations/architecture sometimes carry behavioral detail that may belong upstream | **PARTIAL** | 008-D |
| C7 | Invariants, lifecycle/history, unresolved/invalidated states | Strong in Phase 002 and later temporal refinements | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-C/008-D |
| C8 | Explicit boundaries/non-responsibilities independent of representation | Strong across concept docs and anti-god-concept analysis | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 008-F/008-G |
| D1 | Jackson application inclusion-dependence graph | Existing dependency taxonomy is reference/validation/production/operational/provenance, not inclusion dependence | **OPEN** | 009 |
| D2 | Meaningful valid concept subsets/application family | Direct-generation possibility is known, but no systematic subset/product-family derivation exists | **OPEN** | 009 |
| D3 | Explanation/design ordering implied by inclusion dependence | Not explicitly derived | **OPEN** | 009 |
| D4 | Product-scope consequences of adding/removing concepts | Some local reasoning exists; no consolidated dependence-based scope analysis | **PARTIAL** | 009 |
| E1 | Explicit concept synchronizations | Fifteen accepted synchronization rules plus extensive later stress testing | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 009 |
| E2 | Singular state ownership across synchronizations | Strong authority-oriented composition work exists | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 009 |
| E3 | Composition burden/economy and hidden coordinator avoidance | Strong Phase 001-G/002-H/006-C evidence | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 009 |
| E4 | Composition synergy — combined concepts provide intended application benefit | Benefits are often implicit; no dedicated current synergy audit | **PARTIAL** | 009/011 |
| E5 | Integrity under composition | Extensively stress-tested, but not yet consolidated under the final Jackson integrity rubric | **PARTIAL TO STRONG** | 009/011 |
| F1 | Concept action → human/programmatic interaction mapping | Phase 003 experience describes required workflows, but not one explicit action-to-surface map | **PARTIAL** | 010 |
| F2 | Concept state/query → actor-visible view/inspection mapping | Phase 003 gives strong visibility requirements but mappings are not normalized concept-by-concept | **PARTIAL** | 010 |
| F3 | Linguistic mapping and vocabulary alignment | Strong terminology foundation exists; actor-facing conceptual vocabulary still requires explicit mapping audit | **PARTIAL** | 010 |
| F4 | Physical/interaction mapping appropriate to SDK/notebook/CLI/API/report/UI | Some workflow/interface obligations exist; explicit mapping remains unfinished | **PARTIAL** | 010 |
| F5 | Human/programmatic semantic parity | Strong Phase 003 contract; must be checked against explicit mappings | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 010 |
| G1 | Specificity across the final composed concept set | Strong earlier purpose separation; requires final current-state whole-design evaluation | **PARTIAL TO STRONG** | 011 |
| G2 | Familiarity across the final composed concept set | Not systematically complete | **PARTIAL** | 011 |
| G3 | Integrity across all synchronizations/mappings | Strong adversarial evidence, not yet one final Jackson integrity decision | **PARTIAL TO STRONG** | 011 |
| G4 | Synergy and simplicity/generic fitness | Not yet a dedicated whole-design decision | **PARTIAL** | 011 |
| G5 | Archetypal, exceptional, degraded, adversarial and recovery misfit analysis | Very strong Phase 006/007 evidence, but must be replayed after Phases 008-010 | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 011 |
| G6 | Future-scope/extensibility misfit analysis | Time-series, multi-table, text, privacy and runtime closure received substantial probes; needs final composed replay | **STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED** | 011 |
| G7 | Explicit residual conceptual misfit register | Historical blockers/debt exist; no final post-mapping Jackson residual register | **PARTIAL** | 011/012 |
| H1 | One current-state consolidated Jackson concept-design audit | No audit yet covers the fuller rubric after all current refinements | **OPEN** | 012 |
| H2 | Explicit Jackson concept-design completion decision | Historical readiness decisions used narrower criteria | **OPEN** | 012 |
| R1 | Representation/architecture reconciled downstream to completed concept design | Extensive architecture exists, but concept design is not yet complete | **DOWNSTREAM / PENDING RECONCILIATION** | 013 |
| R2 | Whole design audited across problem → concepts → dependence/sync → mapping/experience → architecture | Not yet possible | **OPEN** | 014 |
| R3 | Implementation-readiness decision based on complete design | Historical 007-K result is superseded | **OPEN** | 014 |

## Current methodological verdict

```text
JACKSON CONCEPT DESIGN COMPLETE     NO
REPRESENTATION/ARCHITECTURE FINAL   NO — RETAINED, PENDING RECONCILIATION
WHOLE DESIGN COMPLETE               NO
IMPLEMENTATION READINESS            NOT READY
IMPLEMENTATION START                NOT STARTED
IMPLEMENTATION NEXT                 NOT YET
```

The matrix intentionally contains no percentage-complete score. Different obligations have different semantic weight, and a single open purpose/boundary/integrity defect can invalidate downstream work regardless of how many other rows are strong.

## Phase ownership and dependency order

The current design sequence is:

```text
008  normalize and close individual-concept design
        ↓
009  close inclusion dependence / application family / composition / synchronization
        ↓
010  close concept mapping and actor-visible linguistic/interaction alignment
        ↓
011  evaluate specificity / familiarity / integrity / synergy / misfit as a composed design
        ↓
012  decide whether Jackson concept design is complete
        ↓
013  reconcile representation / architecture downstream of that completed concept design
        ↓
014  audit the entire design and decide implementation readiness
```

Later phases may reopen earlier work when a real misfit is discovered. The dependency order prevents later artifacts from becoming premature constraints.

## Stop/reopen classification

### J0 — editorial/non-semantic correction

Examples: broken link, typo, duplicate prose, formatting.

May be corrected locally without reopening design if conceptual meaning is unchanged.

### J1 — local specification incompleteness

A current concept's purpose remains stable, but state/action/query/OP wording is incomplete or internally inconsistent.

Reopen the smallest active Phase 008 authority or accepted concept specification needed to resolve it.

### J2 — purpose/boundary/catalog defect

Evidence shows a concept has no independent purpose, combines unrelated purposes, is missing, should be merged/subordinated, or a previously rejected/deferred candidate now has independent purpose/state/actions.

Stop downstream ordinary work. Reopen the relevant Phase 008 discovery/purpose/boundary authority and propagate the result forward.

### J3 — dependence/composition/synchronization defect

Evidence changes inclusion dependence, valid application subsets, synchronization ownership, or concept integrity under composition.

Stop later mapping/architecture closure as needed and reopen Phase 009 plus any affected concept authority.

### J4 — concept-mapping/experience defect

The concept model is coherent but actor-visible interaction or vocabulary cannot faithfully expose it, or the mapping reveals a hidden conceptual mismatch.

Reopen Phase 010; if the problem is truly conceptual, escalate to J1-J3 rather than altering the concept merely for interface convenience.

### J5 — generic design-quality/misfit defect

Specificity, familiarity, integrity, synergy, exceptional/adversarial scenarios, or future scope reveal a substantive design defect.

Phase 011 owns diagnosis. Reopen the smallest upstream authority indicated by the defect.

### J6 — architecture reconciliation defect

Completed concept design cannot be faithfully represented by some retained Phase 004/006/007 architecture decision.

Phase 013 revises/supersedes the architecture. Architecture may not force an upstream concept change unless it reveals a genuine J1-J5 conceptual misfit.

### J7 — whole-design readiness defect

Phase 014 finds unresolved design uncertainty material enough that implementation would be asked to discover product behavior, semantics, mappings, or architecture rather than merely realize them.

Implementation remains NOT READY. Reopen the smallest affected design phase.

## Guardrails during Phases 008-014

Do not:

- add production feature behavior;
- add or expand public implementation APIs;
- add persistence/data-plane schemas or migrations;
- add runtime/model/platform/security adapters;
- add reference algorithms or vertical slices;
- add implementation dependencies for future capability;
- alter package topology to anticipate likely design;
- add new executable architecture/fitness rules to freeze a design hypothesis;
- repair historical/stale implementation tests merely to make the repository appear delivery-ready;
- treat green CI, code structure, implementation plans or existing ADR detail as methodology completion evidence by themselves.

May:

- inspect any repository evidence for counterexamples or feasibility/misfit information;
- update design documents and canonical concept/synchronization/experience authority within the active design subgroup;
- record alternatives, unresolved questions and falsification evidence;
- revise upstream design when justified, even if downstream architecture/code/tests must later change.

## Evidence discipline

Every later phase should classify material evidence as one of:

1. **problem evidence** — actor need, purpose, outcome, domain/environment constraint;
2. **concept evidence** — purpose/state/action/OP/invariant/boundary evidence;
3. **composition evidence** — dependence, synchronization, integrity, synergy evidence;
4. **mapping/experience evidence** — how actors encounter and understand concepts;
5. **downstream feasibility/misfit evidence** — architecture, implementation plan, code/test/runtime fact exposing a constraint or counterexample.

Category 5 may motivate an upstream correction but cannot silently redefine categories 1-4.

## Completion discipline

A future phase may mark only the obligations it actually closes. In particular:

- Phase 008 cannot declare Jackson concept design complete;
- Phase 009 cannot declare mapping complete;
- Phase 010 cannot declare final integrity/misfit validation complete;
- Phase 011 cannot skip the consolidated Phase 012 completion decision;
- Phase 012 cannot make implementation ready;
- Phase 013 cannot make implementation ready;
- only Phase 014 may make implementation **READY / NOT STARTED / NEXT** after the whole design passes.

If Phase 014 does not pass, implementation remains **NOT READY / NOT STARTED / NOT YET**.