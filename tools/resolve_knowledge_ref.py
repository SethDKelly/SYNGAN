from __future__ import annotations

import argparse
import json

from stable_refs import StableReferenceError, reference_for_path, resolve_reference


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve SYNGAN stable knowledge references without search fallback."
    )
    parser.add_argument("value", help="Stable reference, or repository path with --from-path.")
    parser.add_argument(
        "--from-path",
        action="store_true",
        help="Reverse-resolve an exact repository path to its stable reference.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the complete registry entry as deterministic JSON.",
    )
    args = parser.parse_args()

    try:
        entry = reference_for_path(args.value) if args.from_path else resolve_reference(args.value)
    except StableReferenceError as exc:
        print(f"ERROR {exc}")
        return 2

    if args.json:
        print(json.dumps(entry, sort_keys=True, separators=(",", ":")))
    elif args.from_path:
        print(entry["ref"])
    else:
        print(entry["path"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
