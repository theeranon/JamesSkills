#!/usr/bin/env python3
"""Regression tests for knowledge-source intake and lens contracts."""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import tempfile
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "knowledge_library.py"
SPEC = importlib.util.spec_from_file_location("knowledge_library", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def copy_live_knowledge(destination: Path) -> None:
    shutil.copytree(ROOT / "packs/knowledge", destination / "packs/knowledge")
    research = destination / "research"
    research.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        ROOT / "research/2026-08-28-framework-knowledge-source-audit.md",
        research / "2026-08-28-framework-knowledge-source-audit.md",
    )


def main() -> int:
    assert MODULE.discover_repo_root(SCRIPT) == ROOT
    assert MODULE.validate(ROOT) == [], "live knowledge library must validate"

    output = StringIO()
    with redirect_stdout(output):
        assert MODULE.list_library(ROOT) == 0
    listing = output.getvalue()
    for required in ("wealth-spectrum", "wealth-dynamics", "talent-dynamics", "reviewed-private"):
        assert required in listing, f"library listing missing: {required}"

    wealth_dynamics = ROOT / "packs/knowledge/lenses/wealth-dynamics/manifest.json"
    wealth_spectrum = ROOT / "packs/knowledge/lenses/wealth-spectrum/manifest.json"
    assert wealth_dynamics.is_file()
    assert not (ROOT / "packs/knowledge/lenses/talent-dynamics").exists()
    dynamics_manifest = MODULE.load_json(wealth_dynamics)
    spectrum_manifest = MODULE.load_json(wealth_spectrum)
    assert dynamics_manifest["creator_family_id"] == spectrum_manifest["creator_family_id"]
    assert dynamics_manifest["model_family_id"] != spectrum_manifest["model_family_id"]

    resolved_paths: dict[str, str] = {}
    for lens_name in ("wealth-dynamics", "talent-dynamics", "wealth-spectrum"):
        shown = StringIO()
        with redirect_stdout(shown):
            assert MODULE.show_lens(ROOT, lens_name) == 0
        resolved_paths[lens_name] = next(
            line.split("\t", 1)[1]
            for line in shown.getvalue().splitlines()
            if line.startswith("manifest\t")
        )
    assert resolved_paths["wealth-dynamics"] == resolved_paths["talent-dynamics"]
    assert resolved_paths["wealth-spectrum"] != resolved_paths["wealth-dynamics"]

    wealth_index = (ROOT / "packs/knowledge/lenses/wealth-spectrum/index.md").read_text(
        encoding="utf-8"
    )
    talent_limits = (
        ROOT / "packs/knowledge/lenses/wealth-dynamics/references/limitations.md"
    ).read_text(encoding="utf-8")
    assert "generic full pack" in wealth_index and "James's personal assessment" in wealth_index
    assert "No personal Talent Dynamics" in talent_limits

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        write_json(
            sandbox / "packs/knowledge/registry.json",
            {"schema_version": 1, "sources": [], "lenses": []},
        )
        assets = sandbox / "plugins/james-productivity/skills/baseon/assets"
        shutil.copytree(ROOT / "plugins/james-productivity/skills/baseon/assets", assets)

        source_args = argparse.Namespace(
            source_id="example-book",
            title="Example Book",
            creator="Example Author",
            edition="First edition",
            source_type="book",
            source_access="external-local",
            provenance="User-owned copy",
            url=[],
            acquired_at="2026-08-28",
            rights_status="private reading copy; reuse unknown",
            sha256=None,
            evidence_label="official claim",
        )
        assert MODULE.create_source(sandbox, source_args) == 0
        registry = MODULE.load_registry(sandbox)
        assert len(registry["sources"]) == 1
        assert registry["lenses"] == [], "a book must not automatically become a lens"

        lens_args = argparse.Namespace(
            lens_id="example-model",
            title="Example Model",
            kind="book",
            source=["example-book"],
        )
        assert MODULE.create_lens(sandbox, lens_args) == 0
        assert MODULE.validate(sandbox) == [], "fresh draft source and lens must be structurally valid"

        visible = StringIO()
        with redirect_stdout(visible):
            assert MODULE.list_library(sandbox) == 0
        assert "example-model" not in visible.getvalue(), "draft lens must stay out of runtime list"
        with redirect_stderr(StringIO()):
            assert MODULE.show_lens(sandbox, "example-model") == 2
        with redirect_stdout(StringIO()):
            assert MODULE.show_lens(sandbox, "example-model", allow_unready=True) == 0

        concepts = sandbox / "packs/knowledge/lenses/example-model/references/concepts.md"
        concepts.write_text(
            concepts.read_text(encoding="utf-8").replace("#add-locator`", "#missing-locator`"),
            encoding="utf-8",
        )
        errors = MODULE.validate(sandbox)
        assert any("unknown locator" in error for error in errors), "broken provenance must fail"

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        registry_path = sandbox / "packs/knowledge/registry.json"
        registry = MODULE.load_json(registry_path)
        spectrum_entry = next(item for item in registry["lenses"] if item["id"] == "wealth-spectrum")
        spectrum_entry["aliases"] = ["talent-dynamics", "wealth-dynamics"]
        write_json(registry_path, registry)
        errors = MODULE.validate(sandbox)
        assert any("duplicate lens alias" in error for error in errors)
        assert any("alias collides with canonical id" in error for error in errors)

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        raw = sandbox / "packs/knowledge/paid-book-fulltext.txt"
        raw.write_text("copyrighted book text", encoding="utf-8")
        assert any("unapproved or raw file" in error for error in MODULE.validate(sandbox))

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        concepts = sandbox / "packs/knowledge/lenses/wealth-spectrum/references/concepts.md"
        concepts.write_text(
            concepts.read_text(encoding="utf-8") + "\n## WS-999 — Missing metadata\n\nClaim.\n",
            encoding="utf-8",
        )
        assert any("WS-999 lacks evidence" in error for error in MODULE.validate(sandbox))

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        concepts = sandbox / "packs/knowledge/lenses/wealth-spectrum/references/concepts.md"
        concepts.write_text(
            concepts.read_text(encoding="utf-8")
            + "\n## WS-001 — Duplicate\n\n"
            + "- Evidence: `[official claim]`\n"
            + "- Source: `wealth-spectrum-fullpack-2011#pdf-p3-p5`\n"
            + "- Confidence: `source-faithful`\n\nDuplicate.\n",
            encoding="utf-8",
        )
        assert any("duplicate claim id" in error for error in MODULE.validate(sandbox))

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        concepts = sandbox / "packs/knowledge/lenses/wealth-spectrum/references/concepts.md"
        concepts.write_text(
            concepts.read_text(encoding="utf-8").replace(
                "wealth-spectrum-fullpack-2011#pdf-p3-p5",
                "talent-dynamics-genius-guide-2015#pdf-p3-p5",
                1,
            ),
            encoding="utf-8",
        )
        assert any("uses undeclared source" in error for error in MODULE.validate(sandbox))

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        manifest_path = sandbox / "packs/knowledge/lenses/wealth-spectrum/manifest.json"
        manifest = MODULE.load_json(manifest_path)
        manifest["version"] = "banana"
        write_json(manifest_path, manifest)
        assert any("version is not semantic" in error for error in MODULE.validate(sandbox))

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        manifest_path = sandbox / "packs/knowledge/lenses/wealth-spectrum/manifest.json"
        manifest = MODULE.load_json(manifest_path)
        manifest["entrypoint"] = "../../../../research/2026-08-28-framework-knowledge-source-audit.md"
        write_json(manifest_path, manifest)
        assert any("entrypoint must be index.md" in error for error in MODULE.validate(sandbox))

    with tempfile.TemporaryDirectory() as temp:
        sandbox = Path(temp)
        copy_live_knowledge(sandbox)
        source_path = sandbox / "packs/knowledge/sources/wealth-spectrum-fullpack-2011.json"
        source = MODULE.load_json(source_path)
        source.update(
            {
                "status": "promoted",
                "reference_urls": [],
                "content_sha256": None,
                "rights_status": "unknown",
                "rights_basis": "unknown",
                "acquired_at": "",
            }
        )
        write_json(source_path, source)
        errors = MODULE.validate(sandbox)
        for required in ("requires SHA-256", "lacks URL", "unresolved rights", "ISO date"):
            assert any(required in error for error in errors), f"source gate missing: {required}"

    skill = (ROOT / "plugins/james-productivity/skills/baseon/SKILL.md").read_text(encoding="utf-8")
    for required in (
        "official_user_declared",
        "working_hypothesis",
        "A stored profile label without a user-confirmed official report",
        "Never select a `draft` or `retired`",
        "Case fact",
        "Source claim",
        "competing explanation",
        "Never reproduce proprietary test items",
        "`wealth-dynamics` and `talent-dynamics` resolve to one shared Dynamics lens",
        "`wealth-spectrum` is a separate stage model",
    ):
        assert required in skill, f"workflow contract missing: {required}"

    print("PASS baseon intake, alias, provenance, misuse, and library contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
