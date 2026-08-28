#!/usr/bin/env python3
"""Regression checks for course and transformation-journey boundaries."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    course = read("skills/core/design-the-course/SKILL.md")
    course_method = read("skills/core/design-the-course/references/method.md")
    journey = read("skills/core/design-the-journey/SKILL.md")
    phase_model = read("skills/core/design-the-journey/references/five-phase-model.md")
    router = read("skills/internal/james-skill-router/SKILL.md")
    catalog = json.loads(read("catalog.json"))

    for required in (
        "one bounded learning experience",
        "artifact is evidence",
        "Reality Snapshot",
        "request coverage ledger",
        "before state -> trigger -> activity or practice -> output -> after state",
        "design-the-journey",
    ):
        assert required in course + course_method, f"course contract missing: {required}"

    for phase in (
        "`pre`",
        "`workshop`",
        "`coaching_consult`",
        "`showcase`",
        "`after_transformation`",
    ):
        assert phase in journey and phase in phase_model, f"journey phase missing: {phase}"

    assert "Map all five phases before writing a day-by-day agenda" in journey
    assert "Then use `design-the-course`" in journey
    assert "Composition runs one way" in phase_model
    assert "promise traceability ledger" in journey + phase_model
    assert "older Phase 0 to Phase 4 sample" in phase_model
    assert "approved names of all six TPS dimensions remain unresolved" in phase_model

    catalog_by_name = {item["name"]: item for item in catalog["skills"]}
    assert catalog_by_name["design-the-course"]["aliases"] == [
        "learning-experience-design"
    ]
    assert catalog_by_name["design-the-journey"]["aliases"] == [
        "transformation-journey"
    ]
    assert "design-the-course" in router and "design-the-journey" in router

    print("PASS learning design scope, five-phase spine, and composition contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
