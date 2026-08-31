#!/usr/bin/env python3
"""Contract and anti-overfit checks for catchup."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    skill = read("skills/core/catchup/SKILL.md")
    router = read("skills/internal/skill-router/SKILL.md")
    cases = read("tests/behavioral-cases.md")
    catalog = json.loads(read("catalog.json"))
    item = next(entry for entry in catalog["skills"] if entry["name"] == "catchup")

    assert item["status"] == "promoted"
    for required in (
        "comparison point not established",
        "Take the fast path first",
        "Intended:",
        "Actual:",
        "Active:",
        "Historical:",
        "Preserve dirty and untracked user work",
        "ไม่มี action เพิ่มใน scope นี้",
        "Do not widen a bounded status question",
        "project_snapshot.py",
        "ordinary progress inside an active task",
        "one isolated completion claim",
    ):
        assert required in skill, f"catchup contract missing: {required}"

    assert "`catchup`" in router
    assert "not ordinary active-task progress" in router
    assert "## Catchup" in cases
    print("PASS catchup routing, truth classes, fast path and counter-case contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
