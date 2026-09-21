from __future__ import annotations

import pytest

from syngan.adapters.sqlite_control_store import SQLiteControlStore
from syngan.application.learning_state import LearningStateService
from syngan.domain.learning_state import (
    LearnedStateMaterialDescriptor,
    LearnedStateRecord,
    LearnedStateStatus,
    LearningAggregate,
    LearningStatus,
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
from syngan.ports.control_store import ResolutionStatus


pytestmark = pytest.mark.integration


def _revision(scope: AuthorityScope, kind: str, resource_id: str, revision: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=scope,
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        revision_id=SemanticRevisionId(revision),
    )


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


def test_learning_completion_establishes_one_durable_primary_learned_state(tmp_path) -> None:
    scope = AuthorityScope("runtime-test")
    path = tmp_path / "control.db"
    learning = _commitment(scope, "learning", "learning-1", "l1")
    strategy = _revision(scope, "synthesis-strategy", "strategy-1", "r1")
    source = _commitment(scope, "source-state", "source-1", "s1")
    learned_reference = _revision(scope, "learned-state", "state-1", "ls1")
    material_reference = _commitment(
        scope,
        "learned-state-material",
        "material-1",
        "m1",
    )
    component_reference = _commitment(scope, "runtime-component", "component-1", "c1")
    material = LearnedStateMaterialDescriptor(
        reference=material_reference,
        component_references=(component_reference,),
        codec_identity="source-derived-text-v1",
        limitations=("bounded-distinct-value-summary",),
    )
    learned_state = LearnedStateRecord(
        reference=learned_reference,
        producing_learning_reference=learning,
        strategy_reference=strategy,
        material_reference=material_reference,
        dependency_references=(),
        limitations=material.limitations,
    )

    with SQLiteControlStore(path, scope) as store:
        service = LearningStateService(store)
        initialized = service.initialize_learning(
            LearningAggregate(
                learning_commitment=learning,
                strategy_reference=strategy,
                source_references=(source,),
            ),
            RecoveryFrontier(0),
            LogicalId("learning-init"),
        )
        assert initialized.state.status is LearningStatus.COMMITTED

        active = service.activate_learning(
            learning,
            initialized.state_version,
            RecoveryFrontier(0),
            LogicalId("learning-active"),
        )
        assert active.state.status is LearningStatus.ACTIVE

        completed, established = service.establish_learned_state(
            learning_commitment=learning,
            expected_learning_state_version=active.state_version,
            learned_state=learned_state,
            material=material,
            authority_frontier=RecoveryFrontier(0),
            learned_state_transition_id=LogicalId("learned-state-established"),
            learning_transition_id=LogicalId("learning-completed"),
            intent_id=LogicalId("establishment-intent"),
        )

        assert completed.state.status is LearningStatus.COMPLETED
        assert completed.state.learned_state_reference == learned_reference
        assert established.state.status is LearnedStateStatus.USABLE

        material_resolution = store.resolve_immutable_binding(material_reference)
        assert material_resolution.status is ResolutionStatus.RESOLVED

        restricted = service.change_learned_state_status(
            learned_reference,
            established.state_version,
            LearnedStateStatus.RESTRICTED,
            RecoveryFrontier(0),
            LogicalId("learned-state-restricted"),
            limitations=("approved-region-only",),
        )
        assert restricted.state.status is LearnedStateStatus.RESTRICTED
        assert restricted.state.limitations == ("approved-region-only",)

        with pytest.raises(ValueError, match="only committed or active Learning"):
            service.establish_learned_state(
                learning_commitment=learning,
                expected_learning_state_version=completed.state_version,
                learned_state=LearnedStateRecord(
                    reference=_revision(scope, "learned-state", "state-2", "ls2"),
                    producing_learning_reference=learning,
                    strategy_reference=strategy,
                    material_reference=_commitment(
                        scope,
                        "learned-state-material",
                        "material-2",
                        "m2",
                    ),
                    dependency_references=(),
                ),
                material=LearnedStateMaterialDescriptor(
                    reference=_commitment(
                        scope,
                        "learned-state-material",
                        "material-2",
                        "m2",
                    ),
                    component_references=(component_reference,),
                ),
                authority_frontier=RecoveryFrontier(0),
                learned_state_transition_id=LogicalId("state-2-established"),
                learning_transition_id=LogicalId("learning-completed-again"),
                intent_id=LogicalId("establishment-intent-2"),
            )

    with SQLiteControlStore(path, scope) as store:
        reopened = LearningStateService(store)
        persisted_learning = reopened.load_learning(learning)
        persisted_state = reopened.load_learned_state(learned_reference)

        assert persisted_learning.state.status is LearningStatus.COMPLETED
        assert persisted_learning.state.learned_state_reference == learned_reference
        assert persisted_state.state.status is LearnedStateStatus.RESTRICTED
        assert persisted_state.state.limitations == ("approved-region-only",)
