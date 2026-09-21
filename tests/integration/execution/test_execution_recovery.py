from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from syngan.adapters.sqlite_control_store import SQLiteControlStore
from syngan.adapters.sqlite_recovery_authority import SQLiteRecoveryAuthority
from syngan.application.execution_service import ExecutionService
from syngan.domain.execution import (
    AdmissionFacts,
    AdmissionStatus,
    AttemptStatus,
    CheckpointDescriptor,
    ExecutionAggregate,
    ProviderObservation,
    checkpoint_reference,
    execution_reference,
    execution_state_key,
    execution_to_payload,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    RecoveryFrontier,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload
from syngan.foundation.runtime import (
    DependencyProfile,
    RuntimeRealizationPlan,
)
from syngan.ports.control_store import (
    CoordinationIntentState,
    RecoveryFrontierConflict,
)

pytestmark = [pytest.mark.integration, pytest.mark.failure]


def _commitment(
    scope: AuthorityScope,
    kind: str,
    resource_id: str,
    snapshot: str,
) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=scope,
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        commitment_snapshot_id=CommitmentSnapshotId(snapshot),
    )


def _revision(
    scope: AuthorityScope,
    kind: str,
    resource_id: str,
    revision: str,
) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=scope,
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        revision_id=SemanticRevisionId(revision),
    )


def _plan(scope: AuthorityScope, activity: TypedReference) -> RuntimeRealizationPlan:
    return RuntimeRealizationPlan(
        activity_reference=activity,
        strategy_reference=_revision(scope, "synthesis-strategy", "strategy-1", "r1"),
        binding_id="reference-binding",
        build_identity="reference-build-v1",
        dependency_profile=DependencyProfile.SELF_CONTAINED,
        closure_identity="closure-1",
        exact_dependency_identities=(),
        exact_role_environment_identities=(("local-worker", "python-3.11-portable"),),
        runtime_roles=("local-worker",),
        direct_input_references=(_commitment(scope, "source-state", "source-1", "s1"),),
    )


def _facts() -> AdmissionFacts:
    return AdmissionFacts(
        current_authorization=True,
        runtime_closure_current=True,
        references_resolvable=True,
        provider_guarantees_sufficient=True,
        capacity_available=True,
    )


def test_execution_submission_checkpoint_retry_and_operation_idempotency(
    tmp_path: Path,
) -> None:
    scope = AuthorityScope("execution-integration")
    control_path = tmp_path / "control.db"
    recovery_path = tmp_path / "recovery-authority.db"
    activity = _commitment(scope, "generation", "generation-1", "g1")
    execution = execution_reference(
        activity,
        LogicalId("execution-1"),
        CommitmentSnapshotId("execution-snapshot-1"),
    )
    plan = _plan(scope, activity)

    with (
        SQLiteRecoveryAuthority(recovery_path) as recovery,
        SQLiteControlStore(control_path, scope) as store,
    ):
        service = ExecutionService(store, recovery)
        snapshot = service.initialize_execution(
            ExecutionAggregate(
                execution_reference=execution,
                activity_reference=activity,
                authority_frontier=RecoveryFrontier(0),
            ),
            LogicalId("execution-initialized"),
        )

        prepared = service.prepare_attempt(
            execution,
            snapshot.state_version,
            LogicalId("attempt-1"),
            plan,
            CommitmentSnapshotId("runtime-plan-1"),
            RecoveryFrontier(0),
            LogicalId("attempt-1-prepared"),
        )
        active = service.activate_attempt(
            execution,
            prepared.state_version,
            LogicalId("attempt-1"),
            _facts(),
            RecoveryFrontier(0),
            LogicalId("attempt-1-active"),
        )

        submitted, intent = service.prepare_provider_submission(
            execution,
            active.state_version,
            LogicalId("attempt-1"),
            LogicalId("provider-submit-1"),
            RecoveryFrontier(0),
        )
        assert intent.state is CoordinationIntentState.PENDING

        replayed, replay_intent = service.prepare_provider_submission(
            execution,
            active.state_version,
            LogicalId("attempt-1"),
            LogicalId("provider-submit-1"),
            RecoveryFrontier(0),
        )
        assert replayed.state_version == submitted.state_version
        assert replay_intent == intent

        unknown = service.record_provider_observation(
            execution,
            submitted.state_version,
            LogicalId("attempt-1"),
            ProviderObservation.UNKNOWN,
            RecoveryFrontier(0),
            LogicalId("provider-observation-unknown"),
        )
        assert (
            store.get_coordination_intent(LogicalId("provider-submit-1")).state
            is CoordinationIntentState.PENDING
        )

        running = service.record_provider_observation(
            execution,
            unknown.state_version,
            LogicalId("attempt-1"),
            ProviderObservation.RUNNING,
            RecoveryFrontier(0),
            LogicalId("provider-observation-running"),
            correlation="provider-job-1",
        )
        assert (
            store.get_coordination_intent(LogicalId("provider-submit-1")).state
            is CoordinationIntentState.ACKNOWLEDGED
        )

        attempt = running.state.attempt(LogicalId("attempt-1"))
        checkpoint = CheckpointDescriptor(
            reference=checkpoint_reference(
                execution,
                LogicalId("checkpoint-1"),
                CommitmentSnapshotId("checkpoint-snapshot-1"),
            ),
            execution_reference=execution,
            attempt_id=attempt.attempt_id,
            attempt_epoch=attempt.epoch,
            authority_frontier=RecoveryFrontier(0),
            runtime_plan_reference=attempt.runtime_plan_reference,
            progress_scope="partition-set-1",
            codec_identity="checkpoint-codec-v1",
            integrity_identity="sha256:checkpoint-1",
            basis_references=plan.direct_input_references,
        )
        checkpointed = service.commit_checkpoint(
            execution,
            running.state_version,
            checkpoint,
            RecoveryFrontier(0),
            LogicalId("checkpoint-1-committed"),
        )

        failed = service.record_attempt_outcome(
            execution,
            checkpointed.state_version,
            LogicalId("attempt-1"),
            AttemptStatus.FAILED,
            RecoveryFrontier(0),
            LogicalId("attempt-1-failed"),
        )
        retry = service.prepare_attempt(
            execution,
            failed.state_version,
            LogicalId("attempt-2"),
            plan,
            CommitmentSnapshotId("runtime-plan-2"),
            RecoveryFrontier(0),
            LogicalId("attempt-2-prepared"),
            resume_checkpoint_reference=checkpoint.reference,
        )

        assert retry.state.attempt(LogicalId("attempt-2")).epoch == 2
        assert (
            retry.state.attempt(LogicalId("attempt-2")).resume_checkpoint_reference
            == checkpoint.reference
        )


def test_regressive_restore_requires_fresh_frontier_and_fences_restored_attempt(
    tmp_path: Path,
) -> None:
    scope = AuthorityScope("recovery-integration")
    control_path = tmp_path / "control.db"
    backup_path = tmp_path / "control-backup.db"
    recovery_path = tmp_path / "recovery-authority.db"
    activity = _commitment(scope, "generation", "generation-1", "g1")
    execution = execution_reference(
        activity,
        LogicalId("execution-1"),
        CommitmentSnapshotId("execution-snapshot-1"),
    )
    plan = _plan(scope, activity)

    recovery = SQLiteRecoveryAuthority(recovery_path)
    try:
        with SQLiteControlStore(control_path, scope) as store:
            service = ExecutionService(store, recovery)
            initialized = service.initialize_execution(
                ExecutionAggregate(
                    execution_reference=execution,
                    activity_reference=activity,
                    authority_frontier=RecoveryFrontier(0),
                ),
                LogicalId("execution-initialized"),
            )
            prepared = service.prepare_attempt(
                execution,
                initialized.state_version,
                LogicalId("attempt-1"),
                plan,
                CommitmentSnapshotId("runtime-plan-1"),
                RecoveryFrontier(0),
                LogicalId("attempt-1-prepared"),
            )
            active = service.activate_attempt(
                execution,
                prepared.state_version,
                LogicalId("attempt-1"),
                _facts(),
                RecoveryFrontier(0),
                LogicalId("attempt-1-active"),
            )
            assert active.state.current_attempt_id == LogicalId("attempt-1")

        shutil.copy2(control_path, backup_path)

        with SQLiteControlStore(control_path, scope) as store:
            service = ExecutionService(store, recovery)
            fresh = service.begin_regressive_recovery()
            current = service.load(execution)
            service.reconcile_execution_after_recovery(
                execution,
                current.state_version,
                fresh,
                LogicalId("first-recovery"),
            )
            assert fresh == RecoveryFrontier(1)

        shutil.copy2(backup_path, control_path)

        with SQLiteControlStore(control_path, scope) as restored:
            service = ExecutionService(restored, recovery)
            decision = service.assess_admission(execution, _facts())
            assert decision.status is AdmissionStatus.RECONCILIATION_REQUIRED

            fresh = service.begin_regressive_recovery()
            assert fresh == RecoveryFrontier(2)
            restored_snapshot = service.load(execution)
            reconciled = service.reconcile_execution_after_recovery(
                execution,
                restored_snapshot.state_version,
                fresh,
                LogicalId("second-recovery"),
            )

            assert reconciled.state.authority_frontier == RecoveryFrontier(2)
            assert reconciled.state.current_attempt_id is None
            assert (
                reconciled.state.attempt(LogicalId("attempt-1")).status
                is AttemptStatus.FENCED
            )
            assert service.assess_admission(execution, _facts()).status is AdmissionStatus.ADMITTED

            current_record = restored.get_current_state(execution_state_key(execution))
            assert current_record is not None
            with pytest.raises(RecoveryFrontierConflict):
                restored.compare_and_swap_current_state(
                    key=execution_state_key(execution),
                    expected_state_version=reconciled.state_version,
                    authority_frontier=RecoveryFrontier(0),
                    schema_version=current_record.schema_version,
                    payload=execution_to_payload(reconciled.state),
                    transition_id=LogicalId("stale-writer"),
                    transition_kind="stale-writer-attempt",
                    transition_detail=EncodedPayload.from_object({}),
                )
    finally:
        recovery.close()
