"""Ports for scoped platform capability evidence."""

from __future__ import annotations

from typing import Protocol

from syngan.foundation.platform import (
    CapabilityAssertion,
    PlatformQualificationContext,
)


class PlatformCapabilityProvider(Protocol):
    def describe_capabilities(
        self,
        context: PlatformQualificationContext,
    ) -> tuple[CapabilityAssertion, ...]: ...
