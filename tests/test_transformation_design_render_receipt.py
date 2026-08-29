#!/usr/bin/env python3
"""Bind the release claim to a real HTML browser-render receipt."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "tests/receipts/transformation-design-v0.9.0.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    assert RECEIPT.is_file(), "missing tracked HTML render receipt"
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    assert receipt["schema_version"] == 1
    assert receipt["release"] == "0.9.0"
    assert receipt["pdf_generated"] is False
    assert receipt["renderer"]["path"] == "tests/render_transformation_design_examples.cjs"
    assert receipt["renderer"]["sha256"] == digest(ROOT / receipt["renderer"]["path"])

    expected_inputs = {
        "package.json",
        "package-lock.json",
        "skills/standards/make-it-james/scripts/embed_ibm_plex_thai.py",
        "skills/standards/make-it-james/scripts/lint_outcome.py",
    }
    assert {item["path"] for item in receipt["inputs"]} == expected_inputs
    for item in receipt["inputs"]:
        assert item["sha256"] == digest(ROOT / item["path"]), f"stale render input: {item['path']}"

    expected_templates = {
        "skills/core/build-framework/assets/framework-decision-report.html",
        "skills/core/transformation-journey/assets/transformation-journey-blueprint.html",
        "skills/core/learning-experience-design/assets/learning-experience-design-pack.html",
    }
    assert {item["path"] for item in receipt["templates"]} == expected_templates
    for item in receipt["templates"]:
        assert item["sha256"] == digest(ROOT / item["path"]), f"stale render receipt: {item['path']}"

    cases = receipt["cases"]
    assert len(cases) == 3
    assert all(item["ok"] for item in cases)
    for item in cases:
        assert item["loaded_font_faces"] >= 4
        assert item["unresolved_tokens"] is False
        assert item["desktop_overflow_nodes"] == 0 and item["desktop_width_fits"]
        assert item["mobile_overflow_nodes"] == 0 and item["mobile_width_fits"]
        assert item["mobile_unlabeled_cells"] == 0 and item["mobile_unstacked_cells"] == 0
        assert item["print_overflow_nodes"] == 0 and item["print_width_fits"]
        assert item["title_visible_in_print"] and item["visible_source_ledger"]
        assert item["remote_request_count"] == 0

    print("PASS hash-bound HTML render receipt; PDF generation disabled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
