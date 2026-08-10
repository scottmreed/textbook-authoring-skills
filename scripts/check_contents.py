#!/usr/bin/env python3
"""Generate or verify the tracked-file inventory in CONTENTS.md."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENTS_PATH = REPO_ROOT / "CONTENTS.md"
START_MARKER = "<!-- BEGIN GENERATED REPOSITORY INVENTORY -->"
END_MARKER = "<!-- END GENERATED REPOSITORY INVENTORY -->"

DESCRIPTIONS = {
    ".gitignore": "ignored local tooling, caches, and scratch outputs",
    "CONTENTS.md": "this repository map",
    "LICENSE": "MIT license",
    "README.md": "project overview and clean-checkout workflow",
    "config": "chapter map and molecule-alias curation",
    "data": "tracked placeholders for local cache data",
    "notes": "dated reader chemistry and link-fix notes",
    "outputs": "tracked placeholders for ignored local analysis outputs",
    "prompts": "portable stand-ins for omitted helper agents",
    "reports": "dated QA snapshots and curated comparison releases",
    "requirements.txt": "optional Python tooling dependencies",
    "scripts": "reproducible repository helper scripts",
    "skills": "authoring and review skill packages",
    "tests": "automated regression checks",
}


def tracked_top_level_entries(root: Path) -> list[str]:
    """List public top-level paths from the repository index."""
    completed = subprocess.run(
        ["git", "-C", str(root), "ls-files"],
        capture_output=True,
        text=True,
        check=True,
    )
    return sorted({line.split("/", 1)[0] for line in completed.stdout.splitlines() if line})


def render_inventory(root: Path) -> str:
    """Render the generated inventory block for CONTENTS.md."""
    entries = tracked_top_level_entries(root)
    unknown = [entry for entry in entries if entry not in DESCRIPTIONS]
    if unknown:
        raise ValueError(
            "Add descriptions for tracked top-level entries: " + ", ".join(unknown)
        )

    lines = [START_MARKER, "", "## Generated repository inventory", "", "```text"]
    lines.append(f"{root.name}/")
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└──" if is_last else "├──"
        suffix = "/" if (root / entry).is_dir() else ""
        label = entry + suffix
        lines.append(f"{connector} {label:<24} # {DESCRIPTIONS[entry]}")
    lines.extend(["```", "", END_MARKER])
    return "\n".join(lines)


def replace_inventory(contents: str, inventory: str) -> str:
    """Replace the single managed inventory block, preserving all commentary."""
    start = contents.find(START_MARKER)
    end = contents.find(END_MARKER)
    if start < 0 or end < 0 or end < start:
        raise ValueError("CONTENTS.md is missing the generated inventory markers")
    end += len(END_MARKER)
    return contents[:start] + inventory + contents[end:]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="fail if CONTENTS.md is stale")
    group.add_argument("--write", action="store_true", help="rewrite the generated inventory")
    args = parser.parse_args()

    inventory = render_inventory(REPO_ROOT)
    current = CONTENTS_PATH.read_text(encoding="utf-8")
    try:
        updated = replace_inventory(current, inventory)
    except ValueError as error:
        if args.check:
            print(error)
            return 1
        raise

    if args.write:
        CONTENTS_PATH.write_text(updated, encoding="utf-8")
        return 0
    if current != updated:
        print("CONTENTS.md inventory is stale; run: python scripts/check_contents.py --write")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
