#!/usr/bin/env python3
"""Bootstrap and structurally validate a project-standard contract."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS = SKILL_ROOT / "assets"

BASE_FILES = {
    "PROJECT.md": "PROJECT.template.md",
    "STATUS.md": "STATUS.template.md",
    "AGENTS.md": "AGENTS.template.md",
    "docs/DECISIONS.md": "DECISIONS.template.md",
}
SOFTWARE_FILES = {
    "ARCHITECTURE.md": "ARCHITECTURE.template.md",
    "DATA_MODEL.md": "DATA_MODEL.template.md",
}

REQUIRED_HEADINGS = {
    "PROJECT.md": (
        "## Outcome",
        "## Authority",
        "## Scope",
        "## Requirements",
        "## System boundaries",
        "## Need decision",
    ),
    "STATUS.md": (
        "## Current outcome",
        "## Done",
        "## In progress",
        "## Next",
        "## Blockers",
        "## Need decision",
        "## Verification",
    ),
    "AGENTS.md": (
        "## Required context",
        "## Working rules",
        "## Commands",
        "## Completion",
    ),
    "docs/DECISIONS.md": ("# Decisions",),
}


def render(template_name: str, project_name: str) -> str:
    source = (ASSETS / template_name).read_text(encoding="utf-8")
    return source.replace("{{PROJECT_NAME}}", project_name).replace(
        "{{DATE}}", date.today().isoformat()
    )


def bootstrap(root: Path, project_name: str, profile: str) -> int:
    root.mkdir(parents=True, exist_ok=True)
    selected = dict(BASE_FILES)
    if profile == "software":
        selected.update(SOFTWARE_FILES)

    created: list[str] = []
    preserved: list[str] = []
    for relative, template in selected.items():
        target = root / relative
        if target.exists():
            preserved.append(relative)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(template, project_name), encoding="utf-8")
        created.append(relative)

    for relative in created:
        print(f"CREATE {relative}")
    for relative in preserved:
        print(f"PRESERVE {relative}")
    return 0


def check(root: Path) -> int:
    failures: list[str] = []
    for relative, headings in REQUIRED_HEADINGS.items():
        path = root / relative
        if not path.is_file():
            failures.append(f"missing {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                failures.append(f"{relative} missing heading {heading}")
        if re.search(r"\{\{[^}]+\}\}", text):
            failures.append(f"{relative} contains unresolved template placeholder")

    agents_path = root / "AGENTS.md"
    if agents_path.is_file():
        agents_text = agents_path.read_text(encoding="utf-8")
        for required_pointer in ("PROJECT.md", "STATUS.md"):
            if required_pointer not in agents_text:
                failures.append(f"AGENTS.md does not point to {required_pointer}")

    project_path = root / "PROJECT.md"
    if project_path.is_file():
        project_text = project_path.read_text(encoding="utf-8")
        if not re.search(r"\bREQ-\d{3,}\b", project_text):
            failures.append("PROJECT.md has no stable requirement ID such as REQ-001")
        for required_pointer in ("STATUS.md", "docs/DECISIONS.md"):
            if required_pointer not in project_text:
                failures.append(f"PROJECT.md does not point to {required_pointer}")

    for optional, headings in {
        "ARCHITECTURE.md": ("## Components", "## Data and request flow"),
        "DATA_MODEL.md": ("## Canonical facts", "## Entities and relationships"),
    }.items():
        path = root / optional
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                failures.append(f"{optional} missing heading {heading}")
        if re.search(r"\{\{[^}]+\}\}", text):
            failures.append(f"{optional} contains unresolved template placeholder")

    for adapter in ("CLAUDE.md", "GEMINI.md"):
        path = root / adapter
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "AGENTS.md" not in text:
            failures.append(f"{adapter} does not point to AGENTS.md")
        meaningful_lines = [line for line in text.splitlines() if line.strip()]
        if len(meaningful_lines) > 80:
            failures.append(f"{adapter} is not a thin provider adapter")
        if re.search(r"\{\{[^}]+\}\}", text):
            failures.append(f"{adapter} contains unresolved template placeholder")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("PASS project-standard structural contract")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    bootstrap_parser = subparsers.add_parser(
        "bootstrap", help="Create missing contract files without overwriting existing files."
    )
    bootstrap_parser.add_argument("root", type=Path)
    bootstrap_parser.add_argument("--name", required=True)
    bootstrap_parser.add_argument(
        "--profile", choices=("minimal", "software"), default="minimal"
    )

    check_parser = subparsers.add_parser(
        "check", help="Validate the structural project contract."
    )
    check_parser.add_argument("root", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if args.command == "bootstrap":
        return bootstrap(root, args.name, args.profile)
    return check(root)


if __name__ == "__main__":
    sys.exit(main())
