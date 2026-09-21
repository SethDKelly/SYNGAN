"""Non-regressing recovery-authority contract.

The authority lives outside the restorable control-store failure domain.
"""

from __future__ import annotations

from typing import Protocol

from syngan.foundation.identity import RecoveryFrontier


class RecoveryAuthority(Protocol):
    def current_frontier(self) -> RecoveryFrontier: ...

    def advance_after(self, observed: RecoveryFrontier) -> RecoveryFrontier: ...

    def close(self) -> None: ...
