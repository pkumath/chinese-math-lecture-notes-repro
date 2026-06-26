#!/usr/bin/env python3
"""Run the lecture-note validator on bundled examples."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_lecture_note.py"
CURRENT_PASSING_EXAMPLES = [
    ROOT / "examples" / "notes" / "mup_tensor_programs_lecture7.md",
]


def run_note(path: Path) -> tuple[bool, str]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), "--note", str(path), "--mode", "full"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode == 0, proc.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--current-only", action="store_true", help="validate only current passing examples")
    group.add_argument("--all", action="store_true", help="validate every bundled full-note example")
    args = parser.parse_args()

    examples = CURRENT_PASSING_EXAMPLES
    if args.all:
        examples = sorted((ROOT / "examples" / "notes").glob("*.md"))

    failures = 0
    for path in examples:
        ok, output = run_note(path)
        rel = path.relative_to(ROOT)
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {rel}")
        if output:
            print(f"  {output}")
        if not ok:
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
