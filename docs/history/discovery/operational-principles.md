---
type: Operational Principle Set
title: SYNGAN Candidate Operational Principles
status: provisional
---

# SYNGAN Candidate Operational Principles

## Purpose

This document develops archetypal operational principles for the eleven concept candidates carried from Phase 001-E.

Operational principles are not user stories, APIs, implementation flows, or final synchronization specifications. Each principle demonstrates how a candidate's own state and actions can fulfill its distinct purpose in an implementation-independent scenario.

A candidate that cannot tell a distinct operational story should not survive merely because its name is convenient.

## Reading rule

Each candidate is expressed through:

- **purpose** — the distinct need the candidate exists to satisfy;
- **archetypal scenario** — the smallest representative story showing the purpose being fulfilled;
- **owned state** — state required for that purpose rather than borrowed from implementation;
- **owned actions** — actions that materially advance the purpose;
- **synchronization pressure** — facts another concept must react to or provide, without assigning final synchronization design;
- **falsification result** — whether the operational principle supports retaining the candidate.

---

# OP01 — Data Meaning

## Purpose

Enable practitioners and data stewards to establish, inspect, and revise the semantic interpretation SYNGAN relies upon for structured data.

## Archetypal scenario

A practitioner introduces a Spark-resident source dataset. SYNGAN can observe structural facts, but several fields are semantically ambiguous. A steward declares that `customer_id` is an identifier, `birth_date` is a date rather than an arbitrary string, and `status_code` is categorical. Another field remains unknown, while a numeric field receives an inferred interpretation with recorded confidence.

Before learning begins, the practitioner reviews the effective interpretation and sees which meanings were declared, inferred, overridden, or unresolved. The steward later corrects one interpretation. The corrected meaning becomes the effective semantic input for subsequent synthesis work without rewriting the history of work performed under the prior interpretation.

## Owned state

- semantic interpretation by relevant data element/scope;
- declared, inferred, overridden, unresolved, or invalidated status;
- authority/source of an interpretation;
- confidence or uncertainty where inference is used;
- semantic version/revision identity sufficient to distinguish materially different interpretations.

Structural observations may support meaning but do not automatically become semantic authority.

## Owned actions

- declare;
- infer;
- review;
- override/correct;
- mark unknown/unsupported;
- supersede or invalidate an interpretation.

## Synchronization pressure

Learning, Generation, Constraint applicability, Strategy compatibility, Evaluation, and Provenance may depend on the effective Data Meaning revision.

## Falsification result

**Pass.** The actor-visible purpose exists before and independently of any particular synthesis algorithm, execution, or artifact representation.

---

# OP02 — Synthesis Strategy

## Purpose

Enable a practitioner to choose and configure the synthesis behavior to be used, while making its semantic capabilities, requirements, and limitations inspectable independently of a concrete Learning or Generation occurrence.

## Archetypal scenario

A practitioner has accepted Data Meaning for a dataset containing continuous values, high-cardinality categorical fields, missingness, and several Constraints. Before starting expensive work, the practitioner examines two available synthesis strategies.

One strategy supports the relevant semantic field types but cannot honor a requested generation capability. Another supports the capability but has a documented resource requirement and does not enforce one Constraint during learning. The practitioner selects the second strategy, configures its synthesis-relevant parameters, and validates the configured strategy against the current Data Meaning and requested capabilities. The validated strategy configuration is then reused for more than one Learning activity without being redefined by each execution.

The practitioner can later compare or revise the strategy configuration without pretending that the implementation class itself is the domain object.

## Owned state

- strategy identity and semantic version;
- synthesis-relevant configuration;
- declared capabilities;
- declared requirements;
- known semantic/operational limitations relevant to use;
- compatibility assessment state against specified semantic/capability needs.

Implementation registration, dependency loading, class discovery, and plugin mechanics are not concept state.

## Owned actions

- select;
- configure/revise;
- inspect capabilities and limitations;
- validate compatibility;
- compare strategy choices.

## Synchronization pressure

Data Meaning and Constraints provide compatibility inputs. Learning and/or Generation consume the selected strategy. Provenance records the strategy/configuration actually used.

## Falsification result

**Pass, with a strict genericity boundary.** The candidate has actor-visible value before a specific Learning or Generation execution and can be reused across activities. It survives only as synthesis-behavior/capability functionality. If later representation reduces it to `choose implementation class + options`, that representation has failed to realize this concept rather than proving the concept was merely a registry.

---

# OP03 — Learning

## Purpose

Derive reusable source-informed state according to accepted source meaning and synthesis behavior.

## Archetypal scenario

A practitioner chooses a source dataset, its effective Data Meaning, applicable Constraints, and a compatible Synthesis Strategy, then initiates Learning. The Learning becomes pending/running through an associated Execution. During the first physical attempt, infrastructure fails after substantial progress. The logical Learning has not produced valid Learned State.

The Execution retries or resumes according to supported semantics. A later attempt completes. Learning records completion and identifies the resulting Learned State. No Generation is required for the Learning to have fulfilled its purpose.

A different strategy that requires no reusable source-derived state simply has no Learning occurrence; the framework does not manufacture a no-op learning lifecycle for symmetry.

## Owned state

- learning intent/specification;
- source dataset reference;
- effective Data Meaning reference;
- selected strategy/configuration reference;
- applicable learning-relevant Constraints;
- semantic lifecycle state;
- resulting Learned State reference when successfully completed;
- learning-specific diagnostics/outcome information.

Generic retry/platform-job state belongs to Execution rather than Learning.

## Owned actions

- initiate;
- validate semantic prerequisites;
- observe domain-level status/result;
- cancel/withdraw when semantically permitted;
- complete;
- fail;
- associate a successful result.

## Synchronization pressure

Execution realizes long-running work. Successful completion creates or activates Learned State. Provenance records the source/meaning/strategy/execution/result relationship.

## Falsification result

**Pass.** Deriving reusable state is a distinct domain purpose from both executing work and generating synthetic data.

---

# OP04 — Learned State

## Purpose

Preserve reusable source-derived information independently of the Learning occurrence and concrete runtime object that produced it.

## Archetypal scenario

A successful Learning produces source-informed state. The original compute resources are released and the Learning Execution is complete. Weeks later, a practitioner selects that same Learned State to generate a small development dataset, then later a much larger synthetic dataset under different generation intent.

The Learned State remains identifiable as the same source-derived result, with known strategy compatibility, semantic provenance, and limitations. A newer Learning can create a newer Learned State without mutating the historical identity of the older one. The older state can later be retired from new use while historical generations remain traceable to it.

## Owned state

- stable logical identity/version;
- status such as usable, incompatible, retired, or invalidated;
- producing Learning reference;
- Synthesis Strategy/configuration identity;
- compatibility requirements/limitations needed for safe reuse;
- references to durable representation rather than assuming one local object;
- provenance linkage.

## Owned actions

- establish/register on successful Learning;
- inspect;
- validate compatibility for intended use;
- select/reuse;
- compare versions/results;
- retire or invalidate for future use.

Physical save/load/serialization mechanics are representation responsibilities.

## Synchronization pressure

Learning establishes Learned State. Generation consumes compatible Learned State when required. Provenance explains its derivation and subsequent uses.

## Falsification result

**Pass.** The state has independent value and lifecycle after Learning has ended and before any particular Generation occurs.

---

# OP05 — Generation

## Purpose

Define and fulfill an actor's intent to produce synthetic data.

## Archetypal scenario

A practitioner requests 200 million synthetic records from a compatible Learned State. The requested population includes a condition such as a target region distribution and must obey applicable Constraints. Generation first exists in a requested state: amount, scope, conditions, semantic references, strategy/learned-state choice, and reproducibility-relevant intent can be inspected before expensive work starts.

After validation, an associated Execution begins. Output is produced distributively rather than returned as one driver-local object. If the operation fails after partial materialization, Generation distinguishes incomplete/invalid partial output from a completed synthetic dataset. A successful completion identifies the resulting synthetic output and preserves the request semantics that caused it to be produced.

A second Generation can reuse the same Learned State with a different amount or conditions without changing the Learned State itself.

## Owned state

- requested generation intent;
- requested amount/scope;
- conditions or desired characteristics;
- applicable semantic/constraint references;
- strategy/learned-state references as applicable;
- reproducibility-relevant request state;
- lifecycle/result status at the domain level;
- resulting synthetic dataset reference on completion;
- generation-specific diagnostics and limitations.

## Owned actions

- define/request;
- amend before commitment where permitted;
- validate compatibility/satisfiability;
- initiate fulfillment;
- observe;
- cancel/withdraw when permitted;
- complete/fail;
- associate output.

## Subordinate semantics

`Generation Request` and `Condition` remain explicit semantics within Generation. Condition remains distinct from Constraint even though it is not an independent concept.

## Synchronization pressure

Data Meaning, Synthesis Strategy, Learned State, and Constraints affect validity. Execution realizes long-running work. Provenance links request/context to output.

## Falsification result

**Pass.** Generation has independent actor purpose and lifecycle. The operational principle also validates the 001-E decision to subordinate Generation Request and Condition rather than retain separate concepts.

---

# OP06 — Constraint

## Purpose

Let authorized actors state reusable prescriptive rules that applicable synthetic output is required to satisfy independently of the strategy or generation that attempts to honor them.

## Archetypal scenario

A data steward declares that `end_date >= start_date`, that a quantity cannot be negative, and that a particular pair of fields must obey a domain consistency rule. The rules apply across future synthesis work rather than only one Generation.

A practitioner chooses a Synthesis Strategy. Compatibility review shows that one Constraint can be enforced during generation while another can only be checked after generation. The unsupported/enforcement limitation remains visible; the framework does not silently drop the rule.

After synthetic data is generated, an Evaluation can assess whether the applicable Constraints were actually satisfied. The steward later supersedes a Constraint for future work without rewriting the rule set that governed prior results.

## Owned state

- rule definition;
- scope/applicability;
- authority/source;
- revision/supersession state;
- severity or requirement semantics where domain-relevant;
- strategy support/enforcement status only as a synchronized assessment, not as the rule's identity.

## Owned actions

- declare;
- inspect/review;
- revise/supersede;
- determine applicability;
- associate enforcement/validation expectations.

## Synchronization pressure

Data Meaning can determine rule applicability. Strategy/Learning/Generation may support or enforce a Constraint. Evaluation may test satisfaction. Provenance preserves which revision applied.

## Falsification result

**Pass.** Constraints are reusable, independently governed prescriptive state and are neither descriptive Data Meaning nor request-specific conditions.

---

# OP07 — Evaluation Criterion

## Purpose

Enable an actor to state and reuse the evaluative question or standard that matters independently of the method used to measure it or the execution that performs an Evaluation.

## Archetypal scenario

A downstream model owner defines a utility criterion: synthetic data should be assessed for fitness in a specified predictive task with an identified target/use context. Separately, a governance reviewer defines a disclosure-risk criterion describing the risk question that must be examined before considering broader use.

Neither actor selects the measurement implementation yet. Later, two different Evaluation methods are run against the same utility criterion so their evidence can be compared without pretending the metric itself defines the question. The criterion can also be reused across synthetic datasets generated by different strategies.

If the intended downstream use changes materially, the actor creates or supersedes the criterion rather than silently interpreting old evidence under a new question.

## Owned state

- criterion identity and revision;
- question/property being assessed;
- relevant scope/reference population/use context;
- actor/authority provenance;
- interpretation requirements or acceptance semantics where appropriate, without turning the criterion into an approval decision.

Metrics, algorithms, thresholds specific only to one measurement procedure belong to Evaluation unless they are semantically part of the criterion itself.

## Owned actions

- define;
- select/reuse;
- inspect;
- refine/supersede;
- associate applicable scope/use context.

## Synchronization pressure

Evaluation selects one or more Criteria and a method capable of examining them. Evidence references the Criterion so the result retains the question it answered.

## Falsification result

**Pass, with a strict boundary.** The criterion can be defined by a different actor, reused across evaluations and methods, and revised independently. It therefore has actor-visible functionality beyond being an anonymous field on one Evaluation request.

---

# OP08 — Evaluation

## Purpose

Examine explicit criteria using defined methods and inputs in order to produce inspectable evidence.

## Archetypal scenario

A practitioner has a completed synthetic dataset and selects several Evaluation Criteria: statistical fidelity, a downstream utility criterion, and Constraint validity. For each criterion, the practitioner selects an appropriate evaluation method with known scale/cost characteristics.

One evaluation operates distributively over the full source and synthetic datasets. Another uses a bounded sample because the method cannot scale directly; that limitation is explicit in the Evaluation specification and eventual Evidence. The Evaluation runs through an associated Execution, completes, and produces Evidence records tied to their criteria, methods, input identities, scopes, and limitations.

A later evaluation can use a different method against the same criterion without mutating the earlier evidence.

## Owned state

- evaluation specification;
- selected Criteria;
- method/metric identity and configuration;
- source/synthetic/learned-state inputs as applicable;
- evaluation scope and sampling/approximation semantics;
- domain lifecycle/result relationship;
- declared method limitations relevant to interpreting Evidence.

## Owned actions

- define/request;
- select method(s);
- validate prerequisites;
- initiate;
- observe;
- complete/fail;
- produce/associate Evidence;
- compare evaluations where meaningful.

## Synchronization pressure

Criteria define questions. Execution realizes long-running work. Evidence preserves results. Provenance captures inputs/method/execution context.

## Falsification result

**Pass.** Evaluation has an independent investigative purpose and lifecycle distinct from the durable Evidence it produces.

---

# OP09 — Evidence

## Purpose

Preserve an inspectable observation or result with enough scope, method, context, and limitations that actors can understand what was actually established without rerunning the Evaluation.

## Archetypal scenario

An Evaluation completes and reports that a synthetic dataset achieved a particular utility result under a specified criterion and method, while a separate disclosure-risk Evaluation reports its own result. Months later, a governance reviewer examines both records after the original compute environment no longer exists.

The reviewer can see which question each result answered, which datasets and method were used, whether sampling/approximation occurred, relevant limitations, and the Provenance needed to place the result in context. The evidence does not claim that the dataset is approved for release.

A newer Evaluation can create newer Evidence and mark earlier evidence as superseded or no longer applicable to the current dataset/version without deleting historical fact.

## Owned state

- evidence identity/revision;
- Criterion reference;
- observed result/score/finding;
- method and scope sufficient for interpretation;
- relevant input references;
- limitations/uncertainty;
- applicability/supersession state;
- provenance linkage.

## Owned actions

- record on Evaluation result;
- inspect;
- compare;
- mark superseded/obsolete/inapplicable without rewriting history;
- associate with downstream claims/decisions externally.

## Synchronization pressure

Evaluation creates Evidence. Provenance explains derivation. External consumers or governance systems may use Evidence without transferring their decision authority into SYNGAN.

## Falsification result

**Pass.** Evidence has durable actor value independent of the Evaluation lifecycle and remains distinct from both Provenance and approval decisions.

---

# OP10 — Execution

## Purpose

Give operationally significant work a durable logical identity and lifecycle independent of any one platform job, process, or retry.

## Archetypal scenario

A large Learning operation is submitted as one logical Execution. Its first physical attempt starts a distributed job and fails because an executor is lost. The failure is preserved as attempt history rather than replacing the logical work identity.

The practitioner retries. A second attempt resumes from a supported checkpoint and succeeds. Throughout, the practitioner observes one Execution with meaningful progress/status and two attempts. The Learning concept still determines what successful domain completion means and which Learned State results; Execution only provides the common operational lifecycle.

Later, a Generation and an Evaluation use the same Execution semantics without becoming generic workflow steps. Each remains a distinct domain activity synchronized with its own Execution.

## Owned state

- logical execution identity;
- operation reference/type;
- lifecycle state;
- attempt history;
- progress/health summary sufficient for users/operators;
- cancellation/retry/resume state where supported;
- failure summaries;
- relevant resource/runtime context references;
- checkpoint associations where needed for recovery.

## Owned actions

- submit/start;
- observe;
- cancel/interrupt;
- retry;
- resume where supported;
- record attempt start/end/failure;
- complete/fail/abandon logical work.

## Subordinate semantics

`Attempt` is explicit subordinate history inside Execution. Platform jobs, Spark stages, Databricks runs, processes, and scheduler records are representations or linked operational facts, not the concept definition.

## Synchronization pressure

Learning, Generation, and Evaluation synchronize their domain lifecycle with Execution. Provenance records material execution/attempt context without copying all Execution state.

## Falsification result

**Pass.** The common logical lifecycle has strong independent operational purpose at enterprise scale while remaining narrower than a workflow scheduler.

---

# OP11 — Provenance

## Purpose

Explain how material states and results came to exist by preserving derivation and context relationships among the concepts involved in synthesis work.

## Archetypal scenario

A reviewer receives a synthetic dataset and associated Evidence. The reviewer asks how the dataset was produced and whether the evidence applies to that exact result.

Using Provenance, the reviewer traverses from the synthetic output to its Generation, the Learned State used, the Learning that produced that state, the relevant source dataset reference and Data Meaning revision, the selected Synthesis Strategy/configuration, and the material Execution/attempt context. The reviewer then traverses from Evidence to the Evaluation, Criterion, inputs, and method context.

The substantive details remain owned by those concepts; Provenance stores typed relationships and enough production context to explain derivation without copying each concept into a second shadow model.

If a later Learning produces a new Learned State or an Evaluation produces new Evidence, new provenance relationships are appended rather than mutating historical derivation.

## Owned state

- typed derivation/context relationships;
- stable references to participating concept states/results;
- relevant temporal/actor/software/configuration context not canonically owned elsewhere but necessary to explain derivation;
- relationship history sufficient to preserve past production facts.

## Owned actions

- record a material derivation/context relationship;
- inspect/traverse;
- compare derivation paths;
- append new history;
- validate referential integrity at the conceptual level.

## Synchronization pressure

Material state transitions in Data Meaning, Strategy, Learning, Learned State, Generation, Evaluation, Evidence, and Execution may require provenance records. Final trigger rules belong to Phase 001-G synchronization design.

## Falsification result

**Pass.** Provenance has an independent explanatory/traversal purpose and actions distinct from the substantive state of the concepts it references.

---

# Cross-principle findings

## 1. All eleven candidates survive 001-F

The operational principles establish distinct actor-visible purposes for all eleven candidates carried from 001-E.

The two conditional candidates survive with narrowed boundaries:

- **Synthesis Strategy** survives as reusable actor-visible synthesis-behavior/capability state, not as plugin/implementation registration.
- **Evaluation Criterion** survives as a reusable actor-defined evaluative question/standard, not as a metric or anonymous field embedded in one Evaluation.

These remain provisional candidates until Phase 001-G tests composition/synchronization and Phase 001-H performs final consolidation.

## 2. Subordination decisions from 001-E are validated

Operational principles naturally accommodate:

- Generation Request as requested/pre-execution Generation state;
- Condition as request-specific Generation state;
- Attempt as Execution history.

No independent operational purpose was needed to explain these semantics.

## 3. Cross-cutting contracts remain non-concepts

Reproducibility, stable dataset/artifact references, privacy-guarantee discipline, and external use/release authority remain necessary design obligations without requiring generic concepts in the current set.

## 4. Domain activity and operational realization remain separate

Learning, Generation, and Evaluation each have domain-specific success/failure meaning. Execution supplies common long-running lifecycle functionality but cannot define what those activities mean.

## 5. Evaluation responsibility remains intentionally layered

Evaluation Criterion states the question; Evaluation applies a method; Evidence preserves the result; external actors/systems make use/release decisions. Provenance explains how these states/results relate.

## 6. Scale strengthens lifecycle distinctions without dictating representation

The principles require durable identities, retry/history, distributed-output semantics, and reviewable evidence when work exceeds interactive/local assumptions. They do not prescribe Spark ML, PyTorch, Databricks, storage formats, or a job scheduler.

## 7. Phase 001-G must test synchronization economy

The set can still fail conceptually if composition requires excessive all-to-all coupling. Phase 001-G must therefore determine which relationships are true synchronizations, which are ordinary references, which concept owns each state transition, and whether any candidate becomes redundant once composition is explicit.
