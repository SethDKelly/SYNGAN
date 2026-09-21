"""SQLite reference adapter for a separately managed recovery authority."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from syngan.foundation.identity import RecoveryFrontier


class SQLiteRecoveryAuthority:
    """Portable reference monotonic frontier authority.

    The backing database must be placed in a failure domain that is not restored
    together with the control-store snapshot it protects.
    """

    def __init__(self, path: str | Path) -> None:
        self._connection = sqlite3.connect(str(path), isolation_level=None)
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS recovery_authority (
                singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
                frontier INTEGER NOT NULL
            )
            """
        )
        self._connection.execute(
            """
            INSERT INTO recovery_authority(singleton, frontier)
            VALUES (1, 0)
            ON CONFLICT(singleton) DO NOTHING
            """
        )

    def close(self) -> None:
        self._connection.close()

    def __enter__(self) -> SQLiteRecoveryAuthority:
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.close()

    def current_frontier(self) -> RecoveryFrontier:
        row = self._connection.execute(
            "SELECT frontier FROM recovery_authority WHERE singleton = 1"
        ).fetchone()
        if row is None:
            raise RuntimeError("recovery authority frontier is missing")
        return RecoveryFrontier(int(row[0]))

    def advance_after(self, observed: RecoveryFrontier) -> RecoveryFrontier:
        self._connection.execute("BEGIN IMMEDIATE")
        try:
            row = self._connection.execute(
                "SELECT frontier FROM recovery_authority WHERE singleton = 1"
            ).fetchone()
            if row is None:
                raise RuntimeError("recovery authority frontier is missing")
            current = int(row[0])
            next_value = max(current, observed.value) + 1
            self._connection.execute(
                "UPDATE recovery_authority SET frontier = ? WHERE singleton = 1",
                (next_value,),
            )
        except Exception:
            self._connection.rollback()
            raise
        else:
            self._connection.commit()
        return RecoveryFrontier(next_value)
