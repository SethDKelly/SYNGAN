from __future__ import annotations

import pytest

from syngan.domain.execution import (
    AttemptStatus,
    ExecutionAggregate,
    ExecutionStatus,
    ProviderObservation,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    RecoveryFrontier,
    ResourceKey,
    ResourceKind,
    TypedReference,
)


def _commitment(kind: str, resource_id: str, snapshot: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=AuthorityScope("execution-unit"),
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        commitment_snapshot_id=CommitmentSnapshotId(snapshot),
    )


def _execution() -> ExecutionAggregate:
    return ExecutionAggregate(
        execution_reference=_commitment("execution", "execution-1", "e1"),
        activity_reference=_commitment("generation", "generation-1", "g1"),
        authority_frontier=RecoveryFrontier(0),
    )


def test_one_execution_can_record_multiple_distinguishable_attempts() -> None:
    state = _execution()
    plan1 = _commitment("execution-runtime-plan", "attempt-1", "p1")
    plan2 = _commitment("execution-runtime-plan", "attempt-2", "p2")

    first = state.prepare_attempt(LogicalId("attempt-1"), plan1, RecoveryFrontier(0))
    first = first.activate_attempt(LogicalId("attempt-1"), RecoveryFrontier(0))
    first = first.record_attempt_outcome(
        LogicalId("attempt-1"),
        AttemptStatus.FAILED,
        RecoveryFrontier(0),
    )

    second = first.prepare_attempt(LogicalId("attempt-2"), plan2, RecoveryFrontier(0))
    second = second.activate_attempt(LogicalId("attempt-2"), RecoveryFrontier(0))

    assert second.execution_reference == state.execution_reference
    assert second.attempt(LogicalId("attempt-1")).epoch == 1
    assert second.attempt(LogicalId("attempt-2")).epoch == 2
    assert second.current_attempt_id == LogicalId("attempt-2")
    assert second.status is ExecutionStatus.RUNNING


def test_old_attempt_cannot_mutate_after_new_attempt_becomes_current() -> None:
    state = _execution()
    state = state.prepare_attempt(
        LogicalId("attempt-1"),
        _commitment("execution-runtime-plan", "attempt-1", "p1"),
        RecoveryFrontier(0),
    )
    state = state.activate_attempt(LogicalId("attempt-1"), RecoveryFrontier(0))
    state = state.record_attempt_outcome(
        LogicalId("attempt-1"),
        AttemptStatus.FAILED,
        RecoveryFrontier(0),
    )
    state = state.prepare_attempt(
        LogicalId("attempt-2"),
        _commitment("execution-runtime-plan", "attempt-2", "p2"),
        RecoveryFrontier(0),
    )
    state = state.activate_attempt(LogicalId("attempt-2"), RecoveryFrontier(0))

    with pytest.raises(ValueError, match="current Execution mutation authority"):
        state.attach_checkpoint(
            LogicalId("attempt-1"),
            _commitment("execution-checkpoint", "checkpoint-1", "c1"),
            RecoveryFrontier(0),
        )


def test_cancellation_fences_attempt_and_late_success_is_observation_only() -> None:
    state = _execution()
    state = state.prepare_attempt(
        LogicalId("attempt-1"),
        _commitment("execution-runtime-plan", "attempt-1", "p1"),
        RecoveryFrontier(0),
    )
    state = state.activate_attempt(LogicalId("attempt-1"), RecoveryFrontier(0))

    cancelled = state.request_cancellation(RecoveryFrontier(0))
    late = cancelled.record_provider_observation(
        LogicalId("attempt-1"),
        ProviderObservation.SUCCEEDED,
        RecoveryFrontier(0),
        correlation="provider-job-7",
    )

    assert late.status is ExecutionStatus.CANCELLATION_REQUESTED
    assert late.current_attempt_id is None
    assert late.attempt(LogicalId("attempt-1")).status is AttemptStatus.FENCED
    assert (
        late.attempt(LogicalId("attempt-1")).provider_observation is ProviderObservation.SUCCEEDED
    )


def test_recovery_frontier_adoption_fences_restored_current_attempt() -> None:
    state = _execution()
    state = state.prepare_attempt(
        LogicalId("attempt-1"),
        _commitment("execution-runtime-plan", "attempt-1", "p1"),
        RecoveryFrontier(0),
    )
    state = state.activate_attempt(LogicalId("attempt-1"), RecoveryFrontier(0))

    recovered = state.adopt_recovery_frontier(RecoveryFrontier(4))

    assert recovered.authority_frontier == RecoveryFrontier(4)
    assert recovered.current_attempt_id is None
    assert recovered.status is ExecutionStatus.READY
    assert recovered.attempt(LogicalId("attempt-1")).status is AttemptStatus.FENCED

    with pytest.raises(ValueError, match="does not match current authority"):
        recovered.prepare_attempt(
            LogicalId("attempt-2"),
            _commitment("execution-runtime-plan", "attempt-2", "p2"),
            RecoveryFrontier(0),
        )
