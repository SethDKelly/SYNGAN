"""Stable identity and independent technical version axes.

These types represent architecture roles. They do not define concept-specific semantics.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4


def _require_token(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be a non-empty token")
    if any(character.isspace() for character in normalized):
        raise ValueError(f"{label} must not contain whitespace")
    return normalized


@dataclass(frozen=True, slots=True, order=True)
class AuthorityScope:
    value: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _require_token(self.value, "authority scope"))


@dataclass(frozen=True, slots=True, order=True)
class ResourceKind:
    value: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _require_token(self.value, "resource kind"))


@dataclass(frozen=True, slots=True, order=True)
class LogicalId:
    value: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _require_token(self.value, "logical id"))

    @classmethod
    def new(cls) -> LogicalId:
        return cls(str(uuid4()))


@dataclass(frozen=True, slots=True, order=True)
class SemanticRevisionId:
    value: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _require_token(self.value, "semantic revision id"))

    @classmethod
    def new(cls) -> SemanticRevisionId:
        return cls(str(uuid4()))


@dataclass(frozen=True, slots=True, order=True)
class StateVersion:
    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("state version must be non-negative")

    def next(self) -> StateVersion:
        return StateVersion(self.value + 1)


@dataclass(frozen=True, slots=True, order=True)
class RepresentationSchemaVersion:
    value: int

    def __post_init__(self) -> None:
        if self.value < 1:
            raise ValueError("representation schema version must be positive")


@dataclass(frozen=True, slots=True, order=True)
class RecoveryFrontier:
    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("recovery frontier must be non-negative")


@dataclass(frozen=True, slots=True, order=True)
class MigrationRevision:
    value: int

    def __post_init__(self) -> None:
        if self.value < 1:
            raise ValueError("migration revision must be positive")


@dataclass(frozen=True, slots=True)
class ResourceKey:
    scope: AuthorityScope
    kind: ResourceKind
    resource_id: LogicalId


@dataclass(frozen=True, slots=True)
class TypedReference:
    key: ResourceKey
    revision_id: SemanticRevisionId | None = None

    @property
    def is_exact_revision(self) -> bool:
        return self.revision_id is not None

    def require_exact_revision(self) -> SemanticRevisionId:
        if self.revision_id is None:
            raise ValueError("an exact semantic revision is required")
        return self.revision_id
