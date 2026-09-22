---
type: Phase Record
title: 017-C — Cursor/Codex Autonomous Delivery Operating Model & Runtime Qualification
status: complete
---

# 017-C — Cursor/Codex Autonomous Delivery Operating Model & Runtime Qualification

## Purpose

Establish the concrete provider-neutral autonomous-delivery model for Cursor/Codex and define the
real-runtime evidence required before implementation execution may rely on either provider.

## Evidence basis

017-C reviewed current official provider documentation on 2026-09-22.

Cursor currently documents:

- root/nested `AGENTS.md` project instructions;
- automatic project `.agents/skills/` discovery;
- dedicated Agent Review;
- isolated subagent contexts and isolated worktrees/cloud environments;
- configurable execution/run modes.

Codex currently documents:

- hierarchical `AGENTS.md` discovery and precedence;
- repository `.agents/skills/` discovery;
- configurable sandbox/approval modes;
- a dedicated `/review` flow that reports findings without editing the work tree;
- interactive and repeatable CLI execution.

These facts establish documented compatibility only.

## Decisions

### 1. One shared workflow source

SYNGAN keeps:

~~~text
AGENTS.md
.agents/skills/
syngan:// current authority
repository-owned verification
~~~

as the cross-provider source.

No duplicate Cursor or Codex semantic rulebook is introduced.

### 2. Role-separated bounded autonomy

The operating cycle is:

~~~text
human-selected package
  -> implementer
  -> independent fresh-context reviewer
  -> repair in same package
  -> candidate freeze
  -> independent exit evaluation
  -> CI
  -> stop
~~~

Completion does not authorize another package.

### 3. Cursor/Codex role rotation

Default package rotation alternates Cursor and Codex implementer/reviewer roles.

Provider brand alone is not independence; fresh context, read-oriented review, exact candidate state,
and repository-owned authority are required.

### 4. Autonomous multi-agent capability is deliberately bounded

Cursor's Projects/subagents/cloud/autopilot and Codex repeatable/cloud execution may be useful
mechanics, but they may operate only inside a human-selected package.

They may not form an unattended roadmap queue, select the next package, bypass A3/A4 boundaries, or
serve as the sole exit authority.

### 5. Runtime qualification is evidence-controlled

017-C defines ten mandatory RQ probes covering instruction/skill discovery, bounded context,
selected-task execution, no-self-progression, A3/A4 stops, reviewer isolation, verification
fidelity, cross-provider handoff, and replayable evidence.

Both providers remain:

~~~text
documented compatibility    COMPATIBLE
runtime qualification       PENDING TOOL-IN-LOOP
~~~

Actual provider qualification is deferred to the Phase 018 start gate because this ChatGPT/GitHub
planning environment is not itself a Cursor or Codex runtime.

### 6. Main protection timing

Per explicit human direction, main-branch protection is intentionally deferred until the
implementation plan is fully built.

This does not weaken the Phase 018 prerequisite: protected main and old merged-branch cleanup must
still be verified before executable product implementation begins.

## Durable authority

Current owner:

[Cursor/Codex Autonomous Delivery Operating Model & Runtime Qualification](../../implementation/cursor-codex-autonomous-delivery-runtime-qualification.md)

Stable reference:

`syngan://implementation/agent-delivery`

Machine-readable qualification state:

`docs/implementation/agent-runtime-qualification-profile.json`

## Scope / change class

~~~text
agent action class                 A2 bounded planning/repository change
product implementation             NONE
active implementation packages     0
semantic reopen                    NONE
architecture reopen                NONE
provider product integration       NONE
runtime provider certification     PENDING TOOL-IN-LOOP
~~~

## Completion evidence

017-C is complete when:

- the durable operating-model owner exists and is routed by stable reference;
- Cursor/Codex provider roles, rotation, branch/package mechanics, and context isolation are
  explicit;
- provider-specific autonomy is bounded below human-selected package authority;
- documented compatibility is refreshed against current official sources;
- runtime qualification probes/states/requalification triggers are explicit and machine-readable;
- fabricated runtime qualification remains mechanically rejectable;
- actual tool-in-the-loop qualification remains a Phase 018 start-gate prerequisite;
- status/index/OKF routing is coherent;
- repository Verify and Agentic conformance pass.

## Handoff

017-D should define the success-visibility, holdout-evaluation, challenge-generation, anti-gaming,
and replay methodology used by independent phase/package evaluation.

017-D is **NEXT ELIGIBLE / NOT AUTHORIZED** until explicitly selected.

Product implementation remains **NOT AUTHORIZED**.
