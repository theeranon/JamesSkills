#!/usr/bin/env python3
"""Regression checks for the three promoted transformation-design skills."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    framework = read("skills/core/build-framework/SKILL.md")
    framework_contract = read(
        "skills/core/build-framework/references/framework-contract.md"
    )
    provenance = read(
        "skills/core/build-framework/references/research-provenance.md"
    )
    led = read("skills/core/learning-experience-design/SKILL.md")
    led_method = read("skills/core/learning-experience-design/references/method.md")
    journey = read("skills/core/transformation-journey/SKILL.md")
    ai_offer = read(
        "skills/core/transformation-journey/references/ai-transformation-five-phase.md"
    )
    router = read("skills/internal/james-skill-router/SKILL.md")
    renderer = read("tests/render_transformation_design_examples.cjs")
    cases = read("tests/behavioral-cases.md")
    catalog = json.loads(read("catalog.json"))
    by_name = {item["name"]: item for item in catalog["skills"]}

    expected = {
        "build-framework": [],
        "learning-experience-design": ["design-the-course"],
        "transformation-journey": ["design-the-journey"],
    }
    for name, aliases in expected.items():
        assert by_name[name]["status"] == "promoted"
        assert by_name[name]["aliases"] == aliases
        body = read(f"skills/core/{name}/SKILL.md")
        assert f"name: {name}" in body
        assert "Pilot only" not in body and "[TODO" not in body
        assert name in router

    assert "design-the-course" not in by_name
    assert "design-the-journey" not in by_name

    for direct_route in (
        "recurring cross-project company method",
        "macro organization change across interventions",
        "one bounded course, workshop, learning day, or intervention",
    ):
        assert direct_route in router

    registry = json.loads(read("packs/frameworks/registry.json"))
    registry_by_id = {item["id"]: item for item in registry["items"]}
    five_phase = registry_by_id["solutionsimpact-five-phase-transformation-pattern"]
    fixture_identity = (
        f"{five_phase['id']} / version {five_phase['version']} / "
        f"kind {five_phase['kind']} / lifecycle {five_phase['lifecycle']} / AI offer scope"
    )
    assert fixture_identity in renderer
    assert five_phase["kind"] == "pattern"

    ordered = [
        framework.index("use an existing framework"),
        framework.index("upgrade an existing framework"),
        framework.index("build a new framework"),
    ]
    assert ordered == sorted(ordered)
    for required in (
        "inspect the house library",
        "three branded name candidates",
        "only when the decision creates a new framework",
        "Preserve the registered name",
        "three materially different scenarios",
        "legitimate counter-case",
        "executive HTML report",
        "James is the V1 approver",
    ):
        assert required in framework + framework_contract
    for required in (
        "Source ID",
        "Claim used",
        "Limitation",
        "Rights",
        "rename another owner's framework",
    ):
        assert required in provenance
    assert "Do not ask the user to select an internal mode" in framework

    assert "one bounded learning experience" in led
    assert "multi-day course can still be LED" in led
    assert "one available house framework inside LED" in led
    assert "not the definition of LED" in led
    assert "never label a principle or pattern as a framework" in led
    assert "provisional, reversible skeleton" in led
    assert "cannot satisfy the delivery-ready gate" in led
    assert "Call it delivery-ready only when every" in led
    assert "Duration alone does not decide" in led_method
    assert led_method.index("credible evidence") < led_method.index("learner artifact")
    assert "Do not ask the user to choose this label" in led

    assert "macro architecture" in journey
    assert "learning-experience-design" in journey
    assert "preferred house candidate" in journey
    assert "not a universal law" in journey
    assert "current lifecycle is pilot" in journey
    assert "lifecycle-bounded candidate" in journey
    assert "Lock the macro architecture before writing daily agendas" in journey
    assert "may not rewrite the macro outcome" in journey
    assert "Do not ask the user to choose this label" in journey

    for phase in (
        "`pre`",
        "`workshop`",
        "`coaching_consult`",
        "`showcase`",
        "`after_transformation`",
    ):
        assert phase in ai_offer
    assert "does not prove a universal offer model" in ai_offer
    assert "learning-experience-design" in ai_offer

    for body in (led, journey):
        for evidence_state in ("Produced", "Applied", "Impact Proven"):
            assert evidence_state in body
        assert "Satisfaction" in body and "breadcrumb" in body

    for case_id in (
        "BF-S1",
        "BF-F1",
        "BF-C1",
        "LED-S1",
        "LED-F1",
        "LED-C1",
        "TJ-S1",
        "TJ-F1",
        "TJ-C1",
        "MODE-C1",
    ):
        assert case_id in cases, f"missing behavioral case {case_id}"

    print("PASS promoted framework, journey, LED, routing and impact contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
