#!/usr/bin/env python3
"""Behavioral checks for house-library search and registry integrity."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "framework_library.py"
SPEC = importlib.util.spec_from_file_location("framework_library", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main() -> int:
    registry = MODULE.load_registry()
    assert len(registry["items"]) >= 5
    for item in registry["items"]:
        assert item["version"]
        assert item["permitted_scope"]
        assert item["source_refs"]
        assert item["approval_record"]["status"]
        for source in item["source_refs"]:
            assert source["source_id"] and source["locator"] and source["retrieved"]

    productivity = MODULE.search("productivity workshop", registry["items"])
    assert productivity
    assert productivity[0][1]["id"] == "solutionsimpact-transformative-productivity-system"

    journey = MODULE.search("organization transformation coaching showcase", registry["items"])
    assert journey
    assert journey[0][1]["id"] == "solutionsimpact-five-phase-transformation-pattern"
    assert journey[0][1]["kind"] == "pattern"
    assert journey[0][1]["version"] == "offer-reference-2026-08-12"
    assert journey[0][1]["approval_record"]["status"] == "pilot-authorized"

    unapproved = {
        item["id"]: item
        for item in registry["items"]
        if item["lifecycle"] in {"candidate", "source-gap"}
    }
    assert unapproved
    assert all(item["approval_record"]["status"] == "not-approved" for item in unapproved.values())

    broken = json.loads(json.dumps(registry))
    broken["items"].append(dict(broken["items"][0]))
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "registry.json"
        path.write_text(json.dumps(broken), encoding="utf-8")
        try:
            MODULE.load_registry(path)
        except ValueError as error:
            assert "duplicate framework id" in str(error)
        else:
            raise AssertionError("duplicate framework id must fail")

    missing_provenance = json.loads(json.dumps(registry))
    del missing_provenance["items"][0]["source_refs"]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "registry.json"
        path.write_text(json.dumps(missing_provenance), encoding="utf-8")
        try:
            MODULE.load_registry(path)
        except ValueError as error:
            assert "source_refs" in str(error)
        else:
            raise AssertionError("missing source refs must fail")

    false_approval = json.loads(json.dumps(registry))
    false_approval["items"][0]["approval_record"]["status"] = "approved"
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "registry.json"
        path.write_text(json.dumps(false_approval), encoding="utf-8")
        try:
            MODULE.load_registry(path)
        except ValueError as error:
            assert "falsely claims approval" in str(error)
        else:
            raise AssertionError("source-gap item cannot claim approval")

    print("PASS framework registry validation and candidate search")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
