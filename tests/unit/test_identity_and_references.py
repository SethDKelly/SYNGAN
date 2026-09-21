from __future__ import annotations

import json

import pytest

from syngan.foundation.identity import (
    AuthorityScope,
    LogicalId,
    MigrationRevision,
    RecoveryFrontier,
    RepresentationSchemaVersion,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import (
    EncodedPayload,
    ReferenceDecodingError,
    UnsupportedReferenceSchema,
    decode_reference,
    encode_reference,
)


def test_identity_tokens_reject_empty_or_whitespace_values() -> None:
    for constructor in (AuthorityScope, ResourceKind, LogicalId, SemanticRevisionId):
        with pytest.raises(ValueError):
            constructor("")
        with pytest.raises(ValueError):
            constructor("two tokens")


def test_locally_minted_ids_are_opaque_and_unique() -> None:
    first = LogicalId.new()
    second = LogicalId.new()
    revision = SemanticRevisionId.new()

    assert first != second
    assert first.value
    assert revision.value


def test_independent_version_axes_validate_their_own_ranges() -> None:
    assert StateVersion(0).next() == StateVersion(1)
    assert RepresentationSchemaVersion(1).value == 1
    assert RecoveryFrontier(0).value == 0
    assert MigrationRevision(1).value == 1

    with pytest.raises(ValueError):
        StateVersion(-1)
    with pytest.raises(ValueError):
        RepresentationSchemaVersion(0)
    with pytest.raises(ValueError):
        RecoveryFrontier(-1)
    with pytest.raises(ValueError):
        MigrationRevision(0)


def test_typed_reference_round_trip_preserves_exact_revision_binding() -> None:
    reference = TypedReference(
        key=ResourceKey(
            scope=AuthorityScope("local"),
            kind=ResourceKind("data-meaning"),
            resource_id=LogicalId("dm-7"),
        ),
        revision_id=SemanticRevisionId("r-3"),
    )

    encoded = encode_reference(reference)
    decoded = decode_reference(encoded)

    assert decoded == reference
    assert decoded.is_exact_revision
    assert decoded.require_exact_revision() == SemanticRevisionId("r-3")


def test_reference_codec_rejects_unknown_or_unsupported_representation() -> None:
    encoded = encode_reference(
        TypedReference(
            key=ResourceKey(
                scope=AuthorityScope("local"),
                kind=ResourceKind("strategy"),
                resource_id=LogicalId("s-1"),
            )
        )
    )
    payload = json.loads(encoded)
    payload["schema_version"] = 99

    with pytest.raises(UnsupportedReferenceSchema):
        decode_reference(json.dumps(payload))

    payload["schema_version"] = 1
    payload["unexpected"] = True
    with pytest.raises(ReferenceDecodingError):
        decode_reference(json.dumps(payload))


def test_encoded_payload_is_canonical_json_object() -> None:
    first = EncodedPayload.from_object({"b": 2, "a": 1})
    second = EncodedPayload.from_object({"a": 1, "b": 2})

    assert first == second
    assert first.json_text == '{"a":1,"b":2}'
    assert first.as_object() == {"a": 1, "b": 2}

    with pytest.raises(ValueError):
        EncodedPayload.from_object({"bad": float("nan")})
