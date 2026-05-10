#!/usr/bin/env python3
"""Check Atlas repository file naming conventions."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ALLOWED_EXACT = {
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "CODEOWNERS",
}
ALLOWED_DIRS = {".git"}
LOWER_HYPHEN = re.compile(r"^[a-z0-9][a-z0-9._-]*[a-z0-9]$|^[a-z0-9]$")


def should_skip(path: pathlib.Path) -> bool:
    parts = set(path.parts)
    return bool(parts & ALLOWED_DIRS)


def main() -> int:
    failures: list[str] = []

    for path in ROOT.rglob("*"):
        if should_skip(path) or path.is_dir():
            continue

        name = path.name
        rel = path.relative_to(ROOT)

        if name in ALLOWED_EXACT:
            continue

        if " " in name:
            failures.append(f"{rel}: file name contains spaces")
            continue

        if name.lower() != name:
            failures.append(f"{rel}: file name must be lowercase")
            continue

        if not LOWER_HYPHEN.match(name):
            failures.append(f"{rel}: use lowercase letters, numbers, dots, underscores, or hyphens")

    if failures:
        print("File naming check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("File naming check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
