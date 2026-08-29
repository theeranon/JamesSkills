#!/usr/bin/env python3
"""Static contracts for the three transformation-design HTML templates."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


CONTRACTS = {
    "skills/core/build-framework/assets/framework-decision-report.html": (
        "build-framework@1",
        {
            "executive-decision",
            "house-library-review",
            "research-synthesis",
            "framework-model",
            "scenarios",
            "source-trace",
            "approval",
        },
    ),
    "skills/core/transformation-journey/assets/transformation-journey-blueprint.html": (
        "transformation-journey@1",
        {
            "executive-summary",
            "authority",
            "impact-chain",
            "macro-map",
            "interventions",
            "evidence",
            "source-trace",
            "decisions",
        },
    ),
    "skills/core/learning-experience-design/assets/learning-experience-design-pack.html": (
        "learning-experience-design@1",
        {
            "executive-summary",
            "authority",
            "learner-movement",
            "experience-map",
            "delivery-readiness",
            "impact-evidence",
            "source-trace",
            "decisions",
        },
    ),
}


def main() -> int:
    for relative, (contract, required_sections) in CONTRACTS.items():
        html = (ROOT / relative).read_text(encoding="utf-8")
        assert f'data-contract="{contract}"' in html
        sections = set(re.findall(r'data-section="([^"]+)"', html))
        assert required_sections <= sections, (relative, required_sections - sections)
        for marker in (
            "data-source-id=",
            "data-locator=",
            "data-evidence-class=",
            "data-confidence=",
            "@media print",
            'font-family: "IBM Plex Sans Thai"',
            ".table-scroll td::before",
            "data-label=",
        ):
            assert marker in html, f"{relative} missing {marker}"
        for visible_token in (
            "SOURCE_01_ID",
            "SOURCE_01_CITATION_AND_SUPPORTED_CLAIM",
            "SOURCE_01_LOCATOR",
            "SOURCE_01_CLASS",
            "SOURCE_01_RIGHTS",
            "SOURCE_01_RETRIEVED",
            "SOURCE_01_CONFIDENCE",
        ):
            assert re.search(
                rf">\[\[{visible_token}\]\]<", html
            ), f"{relative} hides source field {visible_token}"
        lowered = html.lower()
        for forbidden in (
            "poppins",
            "linear-gradient(",
            "radial-gradient(",
            "border-left:",
            "fonts.googleapis.com",
            "<script src=",
            "<img src=\"http",
            "min-width: 760px",
        ):
            assert forbidden not in lowered, f"{relative} contains {forbidden}"

    framework = (ROOT / next(iter(CONTRACTS))).read_text(encoding="utf-8")
    assert framework.index('data-section="house-library-review"') < framework.index(
        'data-section="framework-model"'
    )
    led = (ROOT / "skills/core/learning-experience-design/assets/learning-experience-design-pack.html").read_text(encoding="utf-8")
    assert led.index("[[EVIDENCE_01]]") < led.index("[[POST_DELIVERY_OBSERVATION_AND_REUSABLE_CANDIDATE]]")

    print("PASS three cited, printable transformation-design HTML contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
