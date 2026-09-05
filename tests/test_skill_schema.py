#!/usr/bin/env python3
"""Structural contract for every canonical SKILL.md.

Enforces docs/SKILL-SCHEMA.md. Asserts structure, never judgment: it cannot tell
whether a bounded job is genuinely distinct or a principle correctly attributed.
Those are settled by tests/behavioral-cases.md.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

KINDS = {
    "workflow",
    "mode",
    "shared-standard",
    "output",
    "knowledge-lens",
    "internal-routing",
}

MIDDLE = {
    "workflow": ["## Procedure", "## Stop when"],
    "output": ["## Procedure", "## Stop when"],
    "knowledge-lens": ["## Procedure", "## Stop when"],
    "internal-routing": ["## Procedure", "## Stop when"],
    "mode": ["## Behavior", "## Stays active until"],
    "shared-standard": ["## Behavior", "## Applies to"],
}

BODY_LINE_CAP = {
    "mode": 120,
    "shared-standard": 120,
    "internal-routing": 140,
    "workflow": 220,
    "output": 220,
    "knowledge-lens": 220,
}

MIN_COUNTER_CASES = {"mode": 2, "shared-standard": 2, "internal-routing": 2}

DESCRIPTION_MIN = 25
DESCRIPTION_MAX = 320


def fail(errors: list[str], skill: str, message: str) -> None:
    errors.append(f"{skill}: {message}")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.index("\n---\n", 4)
    raw = text[4:end]
    body = text[end + 5 :]
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ": " in line and not line.startswith(" "):
            key, value = line.split(": ", 1)
            meta[key.strip()] = value.strip()
    return meta, body


def sections(body: str) -> dict[str, str]:
    found: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current is not None:
                found[current] = "\n".join(buffer)
            current = line.strip()
            buffer = []
        elif current is not None:
            buffer.append(line)
    if current is not None:
        found[current] = "\n".join(buffer)
    return found


def main() -> int:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    entries = catalog["skills"]
    names = {entry["name"] for entry in entries}
    aliases = {alias for entry in entries for alias in entry.get("aliases", [])}
    resolvable = names | aliases

    errors: list[str] = []
    excluded_toward: Counter[str] = Counter()
    cases = (ROOT / "tests" / "behavioral-cases.md").read_text(encoding="utf-8")

    for entry in entries:
        skill = entry["name"]
        path = ROOT / "plugins" / entry["category"] / "skills" / skill / "SKILL.md"
        if not path.is_file():
            fail(errors, skill, "SKILL.md missing")
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)

        # --- frontmatter ---
        if meta.get("name") != skill:
            fail(errors, skill, f"frontmatter name is {meta.get('name')!r}")
        kind = meta.get("kind", "")
        if kind not in KINDS:
            fail(errors, skill, f"kind {kind!r} is not one of {sorted(KINDS)}")
            continue
        if entry.get("kind") != kind:
            fail(errors, skill, f"catalog kind {entry.get('kind')!r} != file kind {kind!r}")
        # `license` is part of the portable Agent Skills frontmatter vocabulary and
        # must match the repository licence, so any redistributed copy carries terms.
        if meta.get("license") != "CC-BY-NC-4.0":
            fail(errors, skill, f"license is {meta.get('license')!r}, expected 'CC-BY-NC-4.0'")
        description = meta.get("description", "")
        if not DESCRIPTION_MIN <= len(description) <= DESCRIPTION_MAX:
            fail(errors, skill, f"description is {len(description)} chars, budget {DESCRIPTION_MIN}-{DESCRIPTION_MAX}")

        # --- stance line ---
        h1 = [line for line in body.splitlines() if line.startswith("# ")]
        if len(h1) != 1:
            fail(errors, skill, f"expected exactly one H1, found {len(h1)}")
        after = body.split(h1[0], 1)[1].lstrip("\n") if h1 else ""
        stance = after.splitlines()[0].strip() if after.splitlines() else ""
        if not stance or stance.startswith("#"):
            fail(errors, skill, "missing stance line after the H1")
        else:
            if len(stance.split()) > 20:
                fail(errors, skill, f"stance line is {len(stance.split())} words, cap 20")
            if stance.lower().startswith("this skill"):
                fail(errors, skill, "stance line must not begin with 'This skill'")

        # --- heading spine ---
        found = sections(body)
        required = ["## Scope", "## Do not use this when", *MIDDLE[kind], "## Principles", "## Counter-case", "## Hand back"]
        order = [line.strip() for line in body.splitlines() if line.startswith("## ")]
        for heading in required:
            if heading not in found:
                fail(errors, skill, f"missing {heading}")
        allowed = set(required) | {"## Sources"}
        for heading in order:
            if heading not in allowed:
                fail(errors, skill, f"unexpected heading {heading}")
        present = [h for h in order if h in required]
        if present != [h for h in required if h in found]:
            fail(errors, skill, f"heading order is {present}, expected {required}")

        # --- scope ---
        scope = found.get("## Scope", "")
        for key in ("- Kind: ", "- Owns: ", "- Boundary: "):
            if key not in scope:
                fail(errors, skill, f"## Scope missing {key.strip()}")
        declared = re.search(r"^- Kind: (\S+)", scope, re.M)
        if declared and declared.group(1) != kind:
            fail(errors, skill, f"## Scope kind {declared.group(1)!r} != frontmatter {kind!r}")

        # --- anti-triggers ---
        anti = found.get("## Do not use this when", "")
        bullets = [line for line in anti.splitlines() if line.startswith("- ")]
        if len(bullets) < 2:
            fail(errors, skill, f"## Do not use this when has {len(bullets)} bullets, need 2")
        for bullet in bullets:
            owners = re.findall(r"`([a-z0-9-]+)`", bullet)
            real = [owner for owner in owners if owner in resolvable]
            if not real:
                fail(errors, skill, f"anti-trigger names no real sibling: {bullet[:70]}")
            for owner in real:
                if owner != skill:
                    excluded_toward[owner] += 1

        # --- principles ---
        principles = [line for line in found.get("## Principles", "").splitlines() if line.startswith("**")]
        if not 2 <= len(principles) <= 5:
            fail(errors, skill, f"{len(principles)} principles, need 2-5")
        for line in principles:
            if not re.match(r"^\*\*[^*]+\*\* — .+", line):
                fail(errors, skill, f"principle must read '**Name** — rule.': {line[:70]}")

        # --- counter-case ---
        counter = found.get("## Counter-case", "")
        counters = [line for line in counter.splitlines() if line.startswith("- ")]
        minimum = MIN_COUNTER_CASES.get(kind, 1)
        if len(counters) < minimum:
            fail(errors, skill, f"{len(counters)} counter-cases, need {minimum}")
        # At least one counter-case routes elsewhere. Others may be permission
        # counter-cases: a legitimate request the rule must still allow.
        if counters and not any(re.search(r"`([a-z0-9-]+)`", line) for line in counters):
            fail(errors, skill, "no counter-case names the sibling that owns it instead")

        # --- sources ---
        if "Source:" in found.get("## Principles", "") and "## Sources" not in found:
            fail(errors, skill, "principles cite a source but ## Sources is missing")

        # --- length budget ---
        used = len([line for line in body.splitlines() if line.strip()])
        if used > BODY_LINE_CAP[kind]:
            fail(errors, skill, f"body is {used} non-blank lines, cap {BODY_LINE_CAP[kind]} for {kind}")

        # --- behavioral coverage ---
        title = skill.replace("-", " ")
        if f"`{skill}`" not in cases and not re.search(rf"^## .*{re.escape(title)}", cases, re.M | re.I):
            fail(errors, skill, "no entry in tests/behavioral-cases.md")

    # --- plugin packaging: marketplace, manifests, and catalog must agree ---
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    listed = {entry["name"] for entry in marketplace["plugins"]}
    on_disk = {path.name for path in (ROOT / "plugins").iterdir() if path.is_dir()}
    if listed != on_disk:
        errors.append(f"marketplace.json lists {sorted(listed)} but plugins/ holds {sorted(on_disk)}")
    if marketplace.get("version") != version:
        errors.append(f"marketplace.json version {marketplace.get('version')!r} != VERSION {version!r}")
    for entry in marketplace["plugins"]:
        name = entry["name"]
        if entry.get("source") != f"./plugins/{name}":
            errors.append(f"{name}: marketplace source is {entry.get('source')!r}")
        canonical = ROOT / "plugins" / name / ".claude-plugin" / "plugin.json"
        if not canonical.is_file():
            errors.append(f"{name}: missing .claude-plugin/plugin.json")
            continue
        manifest = json.loads(canonical.read_text(encoding="utf-8"))
        if manifest.get("name") != name or manifest.get("version") != version:
            errors.append(f"{name}: plugin manifest name/version disagrees with the marketplace")
        # A bare plugin.json is kept for hosts that read it; it must never drift.
        bare_path = ROOT / "plugins" / name / "plugin.json"
        if bare_path.is_file():
            bare = json.loads(bare_path.read_text(encoding="utf-8"))
            if bare.get("name") != manifest["name"] or bare.get("version") != manifest["version"]:
                errors.append(f"{name}: plugin.json has drifted from .claude-plugin/plugin.json")

    # --- boundary graph: every skill must be excluded toward by a sibling ---
    for name in sorted(names):
        if excluded_toward[name] == 0:
            errors.append(f"{name}: no sibling excludes toward it; its job is not distinct")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        print(f"Skill schema failed: {len(errors)} issue(s)")
        return 1
    print(f"PASS skill schema canonical={len(entries)} boundary-graph in-degree>=1 for all")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
