#!/usr/bin/env python3
"""Bootstrap and structurally validate a project-standard contract."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from datetime import date
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS = SKILL_ROOT / "assets"

AI_CONTEXT = "ai-context"
# The contract version a project was generated or repaired against. Stamped into every
# generated SRS so a project states which standard it follows.
CONTRACT_VERSION = "1.0"

BASE_FILES = {
    f"{AI_CONTEXT}/PROJECT.md": "PROJECT.template.md",
    f"{AI_CONTEXT}/STATUS.md": "STATUS.template.md",
    "AGENTS.md": "AGENTS.template.md",
    f"{AI_CONTEXT}/DECISIONS.md": "DECISIONS.template.md",
}
SOFTWARE_FILES = {
    f"{AI_CONTEXT}/ARCHITECTURE.md": "ARCHITECTURE.template.md",
    f"{AI_CONTEXT}/DATA_MODEL.md": "DATA_MODEL.template.md",
}

REQUIRED_HEADINGS = {
    f"{AI_CONTEXT}/PROJECT.md": (
        "## Outcome",
        "## Authority",
        "## Scope",
        "## Requirements",
        "## System boundaries",
        "## Need decision",
    ),
    f"{AI_CONTEXT}/STATUS.md": (
        "## Current outcome",
        "## Done",
        "## In progress",
        "## Requirement state",
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
    f"{AI_CONTEXT}/DECISIONS.md": ("# Decisions",),
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


LEGACY_CANONICAL_HEADINGS = {
    "PROJECT.md": REQUIRED_HEADINGS[f"{AI_CONTEXT}/PROJECT.md"],
    "STATUS.md": REQUIRED_HEADINGS[f"{AI_CONTEXT}/STATUS.md"],
    "docs/DECISIONS.md": REQUIRED_HEADINGS[f"{AI_CONTEXT}/DECISIONS.md"],
}
LEGACY_OPTIONAL_HEADINGS = {
    "ARCHITECTURE.md": ("## Components", "## Data and request flow"),
    "DATA_MODEL.md": ("## Canonical facts", "## Entities and relationships"),
}
# Known cross-reference strings rewritten after a file moves into ai-context/. Order matters:
# the docs/DECISIONS.md form must be checked before the bare DECISIONS.md form.
REPOINT = {
    "`docs/DECISIONS.md`": f"`{AI_CONTEXT}/DECISIONS.md`",
    "`PROJECT.md`": f"`{AI_CONTEXT}/PROJECT.md`",
    "`STATUS.md`": f"`{AI_CONTEXT}/STATUS.md`",
    "`DECISIONS.md`": f"`{AI_CONTEXT}/DECISIONS.md`",
    "`ARCHITECTURE.md`": f"`{AI_CONTEXT}/ARCHITECTURE.md`",
    "`DATA_MODEL.md`": f"`{AI_CONTEXT}/DATA_MODEL.md`",
}


def heading_present(text: str, heading: str) -> bool:
    return re.search(rf"^{re.escape(heading)}\b", text, flags=re.MULTILINE) is not None


def repoint_text(text: str) -> str:
    for old, new in REPOINT.items():
        text = text.replace(old, new)
    return text


def migrate(root: Path, name: str | None, profile: str) -> int:
    """Bring a project up to the ai-context/ layout, however it currently stands:
    - already on ai-context/: no-op.
    - no project-standard files at all: bootstrap a fresh v2 contract.
    - legacy root-level files whose headings already match the template: move them into
      ai-context/ and repoint every known cross-reference, mechanically, no rewrite needed.
    - legacy root-level files whose headings don't match (a pre-existing custom doc): leave
      them in place and report exactly what's missing — content-level rewriting is a judgment
      call for the Repair workflow (SKILL.md), not something this script guesses at.
    Returns 0 (done, nothing further needed), 1 (nothing found and no --name to bootstrap), or
    2 (some files moved, or none did, but at least one file still needs a manual rewrite).
    """
    if (root / AI_CONTEXT / "PROJECT.md").is_file():
        print(f"SKIP already on the {AI_CONTEXT}/ layout — nothing to migrate")
        return 0

    legacy_candidates = list(LEGACY_CANONICAL_HEADINGS) + list(LEGACY_OPTIONAL_HEADINGS)
    found_legacy = {rel: root / rel for rel in legacy_candidates if (root / rel).is_file()}

    if not found_legacy:
        if not name:
            print("FAIL no existing project-standard files found and no --name given to bootstrap")
            return 1
        print("No existing project-standard files found — bootstrapping a fresh v2 contract.")
        return bootstrap(root, name, profile)

    ready_to_move: dict[str, Path] = {}
    needs_rewrite: dict[str, list[str]] = {}
    for rel, path in found_legacy.items():
        text = path.read_text(encoding="utf-8")
        required = LEGACY_CANONICAL_HEADINGS.get(rel) or LEGACY_OPTIONAL_HEADINGS.get(rel, ())
        missing = [heading for heading in required if not heading_present(text, heading)]
        if missing:
            needs_rewrite[rel] = missing
        else:
            ready_to_move[rel] = path

    target_dir = root / AI_CONTEXT
    if ready_to_move:
        target_dir.mkdir(parents=True, exist_ok=True)

    for rel, path in ready_to_move.items():
        target = target_dir / path.name
        target.write_text(repoint_text(path.read_text(encoding="utf-8")), encoding="utf-8")
        path.unlink()
        print(f"MIGRATE {rel} -> {AI_CONTEXT}/{path.name}")
        if path.parent != root and path.parent.name == "docs":
            try:
                path.parent.rmdir()
            except OSError:
                pass  # docs/ still holds other files — leave it

    for adapter in ("AGENTS.md", "CLAUDE.md", "GEMINI.md"):
        adapter_path = root / adapter
        if not adapter_path.is_file():
            continue
        text = adapter_path.read_text(encoding="utf-8")
        new_text = repoint_text(text)
        if new_text != text:
            adapter_path.write_text(new_text, encoding="utf-8")
            print(f"REPOINT {adapter}")

    status_target = target_dir / "STATUS.md"
    if status_target.is_file():
        status_text = status_target.read_text(encoding="utf-8")
        if "Spec lock:" not in status_text:
            authority_line = re.search(rf"^Authority:.*$", status_text, flags=re.MULTILINE)
            if authority_line:
                status_text = (
                    status_text[: authority_line.end()]
                    + "\nSpec lock: Open"
                    + status_text[authority_line.end() :]
                )
            else:
                status_text = status_text.rstrip("\n") + "\n\nSpec lock: Open\n"
            status_target.write_text(status_text, encoding="utf-8")
            print(f"ADD {AI_CONTEXT}/STATUS.md Spec lock: Open")

    if needs_rewrite:
        print("")
        print(f"{len(needs_rewrite)} file(s) still need their headings rewritten before they can move:")
        for rel, missing in needs_rewrite.items():
            print(f"  HOLD {rel} — left at its current path, not moved")
            for heading in missing:
                print(f"       missing heading: {heading}")
        print(
            "Rewrite each file's content into the canonical headings (see references/contract.md), "
            "then re-run migrate — files already moved above are skipped automatically."
        )
        return 2

    if ready_to_move:
        print(f"Run render-srs next to generate {AI_CONTEXT}/SRS.html.")
    return 0


def check(root: Path, ready: bool = False) -> int:
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

    project_path = root / AI_CONTEXT / "PROJECT.md"
    project_requirement_ids: set[str] = set()
    if project_path.is_file():
        project_text = project_path.read_text(encoding="utf-8")
        project_requirement_ids = set(re.findall(r"\bREQ-\d{3,}\b", project_text))
        if not project_requirement_ids:
            failures.append("PROJECT.md has no stable requirement ID such as REQ-001")
        requirement_header = re.search(
            r"## Requirements\s*\n+([^\n]+)", project_text, flags=re.IGNORECASE
        )
        if requirement_header and re.search(
            r"\|\s*State\s*\|", requirement_header.group(1), flags=re.IGNORECASE
        ):
            failures.append("PROJECT.md duplicates mutable requirement State owned by STATUS.md")
        for required_pointer in ("STATUS.md", "DECISIONS.md"):
            if required_pointer not in project_text:
                failures.append(f"PROJECT.md does not point to {required_pointer}")

    status_path = root / AI_CONTEXT / "STATUS.md"
    if status_path.is_file():
        status_text = status_path.read_text(encoding="utf-8")
        status_requirement_ids = set(re.findall(r"\bREQ-\d{3,}\b", status_text))
        if project_requirement_ids != status_requirement_ids:
            failures.append(
                "STATUS.md requirement IDs do not match PROJECT.md "
                f"project={sorted(project_requirement_ids)} status={sorted(status_requirement_ids)}"
            )
        if ready:
            if re.search(r"## Current outcome\s*\n+\s*Not confirmed\b", status_text):
                failures.append("STATUS.md current outcome is not ready")
            if "| REQ-001 | Need decision | Named owner acceptance missing |" in status_text:
                failures.append("STATUS.md still contains the bootstrap requirement state")

    if ready and project_path.is_file():
        project_text = project_path.read_text(encoding="utf-8")
        bootstrap_signals = (
            "- Primary user: Not confirmed",
            "- Problem: Not confirmed",
            "- Successful outcome: Not confirmed",
            "| REQ-001 | Not confirmed | Not confirmed |",
        )
        for signal in bootstrap_signals:
            if signal in project_text:
                failures.append(f"PROJECT.md is not ready: {signal}")

    for optional, headings in {
        f"{AI_CONTEXT}/ARCHITECTURE.md": ("## Components", "## Data and request flow"),
        f"{AI_CONTEXT}/DATA_MODEL.md": ("## Canonical facts", "## Entities and relationships"),
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

    if project_path.is_file():
        lock_state, locked_hash = ("open", None)
        if status_path.is_file():
            lock_state, locked_hash = parse_spec_lock(status_path.read_text(encoding="utf-8"))
        current_hash = source_hash(root)

        if lock_state == "locked":
            if locked_hash and locked_hash != current_hash:
                failures.append(
                    "PROJECT.md or DATA_MODEL.md changed while STATUS.md's Spec lock is Locked — "
                    "revert the change, or record a Need decision to unlock and re-run lock-spec"
                )
        else:
            srs_path = root / AI_CONTEXT / "SRS.html"
            if srs_path.is_file():
                srs_hash_match = re.search(r"srs-source-hash:\s*([0-9a-f]{6,})", srs_path.read_text(encoding="utf-8"))
                if srs_hash_match and srs_hash_match.group(1) != current_hash:
                    failures.append(
                        f"{AI_CONTEXT}/SRS.html is stale — PROJECT.md/DATA_MODEL.md changed since the last "
                        "render-srs; run render-srs before committing (Spec lock: Open keeps SRS.html in sync)"
                    )

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    level = "ready" if ready else "structural"
    print(f"PASS project-standard/{CONTRACT_VERSION} {level} contract")
    return 0


def source_hash(root: Path) -> str:
    """Hash of PROJECT.md + DATA_MODEL.md content, used to detect drift for the Open-mode
    SRS-freshness check and the Locked-mode spec-lock check."""
    project_path = root / AI_CONTEXT / "PROJECT.md"
    data_model_path = root / AI_CONTEXT / "DATA_MODEL.md"
    project_text = project_path.read_text(encoding="utf-8") if project_path.is_file() else ""
    data_model_text = data_model_path.read_text(encoding="utf-8") if data_model_path.is_file() else ""
    digest = hashlib.sha256(f"{project_text}\x00{data_model_text}".encode("utf-8"))
    return digest.hexdigest()[:12]


def parse_spec_lock(status_text: str) -> tuple[str, str | None]:
    """Read STATUS.md's `Spec lock:` line. Missing line defaults to open (v1 compatibility)."""
    locked = re.search(
        r"Spec lock:\s*Locked\b.*?hash:\s*([0-9a-f]{6,})", status_text, flags=re.IGNORECASE | re.DOTALL
    )
    if locked:
        return "locked", locked.group(1)
    return "open", None


def extract_section(text: str, heading: str) -> str | None:
    """Return the section body under `heading`, or None if `heading` does not appear at all.

    Matches the heading line loosely — trailing text on the same line (a date stamp, a
    parenthetical note) does not break the match — but the heading text itself must appear;
    a differently-worded or differently-leveled heading in a pre-existing, non-template
    document will not match, and returns None rather than silently reading as "Not confirmed".
    """
    match = re.search(
        rf"^{re.escape(heading)}\b[^\n]*\n(.*?)(?=\n## |\Z)", text, flags=re.MULTILINE | re.DOTALL
    )
    return match.group(1).strip() if match else None


def md_table_to_html(section_text: str) -> str:
    lines = [line.strip() for line in section_text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return "<p><em>Not confirmed</em></p>"
    rows = [
        [cell.strip() for cell in line.strip("|").split("|")]
        for line in lines
        if not re.match(r"^\|?\s*-{2,}", line)
    ]
    if not rows:
        return "<p><em>Not confirmed</em></p>"
    header, *body = rows
    html = ["<table>", "<thead><tr>"]
    html += [f"<th>{cell}</th>" for cell in header]
    html.append("</tr></thead><tbody>")
    for row in body:
        html.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
    html.append("</tbody></table>")
    return "".join(html)


def section_prose_or_table(section_text: str | None, heading: str, source_file: str) -> str:
    if section_text is None:
        return (
            f'<p class="warn">⚠ Heading <code>{heading}</code> not found in <code>{source_file}</code> — '
            "this section is not a real \"Not confirmed\", the parser could not locate it. Check the "
            "heading text matches the project-standard template exactly (same wording and level).</p>"
        )
    if any(line.strip().startswith("|") for line in section_text.splitlines()):
        return md_table_to_html(section_text)
    if not section_text:
        return "<p><em>Not confirmed</em></p>"
    paragraphs = [p.strip() for p in section_text.split("\n\n") if p.strip()]
    return "".join(f"<p>{p}</p>" for p in paragraphs)


SRS_CSS = """
body { font-family: -apple-system, "Segoe UI", "Noto Sans Thai", sans-serif; max-width: 900px;
  margin: 40px auto; padding: 0 24px; color: #17202a; line-height: 1.5; }
h1 { font-size: 22px; margin-bottom: 4px; }
h2 { font-size: 16px; margin-top: 32px; border-bottom: 1px solid #d8dee6; padding-bottom: 6px; }
.meta { color: #52606d; font-size: 13px; margin-bottom: 24px; }
.note { background: #f5f7f9; border: 1px solid #d8dee6; border-radius: 6px; padding: 12px 16px;
  font-size: 13px; color: #52606d; margin-bottom: 24px; }
table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 12px 0; }
th, td { border-bottom: 1px solid #d8dee6; padding: 6px 8px; text-align: left; vertical-align: top; }
th { background: #f5f7f9; }
.warn { background: #fdf2e9; border: 1px solid #f0c896; border-radius: 6px; padding: 10px 14px;
  color: #8a4b0a; font-size: 13px; }
.warn code { font-size: 12px; }
"""


def render_srs(root: Path) -> tuple[str, list[str]]:
    """Returns (html, missing_headings). missing_headings names every canonical heading that
    was not found verbatim in its source file — a signal the source predates or diverges from
    the project-standard template, not that its content is genuinely unconfirmed."""
    project_path = root / AI_CONTEXT / "PROJECT.md"
    if not project_path.is_file():
        raise FileNotFoundError(f"{project_path} not found — bootstrap or write PROJECT.md first")
    project_text = project_path.read_text(encoding="utf-8")

    missing: list[str] = []

    data_model_path = root / AI_CONTEXT / "DATA_MODEL.md"
    permissions_html = "<p><em>No DATA_MODEL.md — no software profile in use.</em></p>"
    if data_model_path.is_file():
        data_model_text = data_model_path.read_text(encoding="utf-8")
        permissions_section = extract_section(data_model_text, "## Permissions")
        if permissions_section is None:
            missing.append("DATA_MODEL.md: ## Permissions")
        permissions_html = section_prose_or_table(permissions_section, "## Permissions", "DATA_MODEL.md")

    title_match = re.search(r"^# (.+)$", project_text, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Project"

    headings = (
        ("Outcome", "## Outcome"),
        ("Scope", "## Scope"),
        ("Requirements", "## Requirements"),
        ("Non-functional requirements", "## Non-functional requirements"),
        ("System boundaries", "## System boundaries"),
    )

    body = []
    for label, heading in headings:
        content = extract_section(project_text, heading)
        if content is None:
            missing.append(f"PROJECT.md: {heading}")
        body.append(f"<h2>{label}</h2>{section_prose_or_table(content, heading, 'PROJECT.md')}")
    body.append(f"<h2>Permissions</h2>{permissions_html}")

    banner = ""
    if missing:
        missing_list = "".join(f"<li><code>{m}</code></li>" for m in missing)
        banner = (
            '<div class="note warn">This source uses different headings than the project-standard '
            f"template for {len(missing)} section(s) below — those sections could not be located and are "
            f"flagged, not genuinely empty. Missing: <ul>{missing_list}</ul></div>"
        )

    html = f"""<!doctype html>
<!-- project-standard/{CONTRACT_VERSION} srs-source-hash: {source_hash(root)} — generated by project_standard.py render-srs; do not hand-edit -->
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} — SRS</title>
<style>{SRS_CSS}</style>
</head>
<body>
<h1>{title} — Software Requirement Spec</h1>
<p class="meta">project-standard/{CONTRACT_VERSION} · generated {date.today().isoformat()} from <code>ai-context/PROJECT.md</code>{" and <code>ai-context/DATA_MODEL.md</code>" if data_model_path.is_file() else ""}.</p>
<div class="note">This file is a generated view, not the source of truth. Edit <code>PROJECT.md</code> / <code>DATA_MODEL.md</code>, then re-run <code>project_standard.py render-srs</code> to refresh it.</div>
{banner}
{"".join(body)}
</body>
</html>
"""
    return html, missing


def lock_spec_command(root: Path) -> int:
    project_path = root / AI_CONTEXT / "PROJECT.md"
    if not project_path.is_file():
        print(f"FAIL {project_path} not found")
        return 1
    line = f"Spec lock: Locked (date: {date.today().isoformat()}, hash: {source_hash(root)})"
    print(line)
    print(f'Paste this line over the "Spec lock:" line in {AI_CONTEXT}/STATUS.md to freeze the spec.')
    print("Any further edit to PROJECT.md or DATA_MODEL.md will then fail `check` until re-locked or reverted.")
    return 0


def render_srs_command(root: Path) -> int:
    try:
        html, missing = render_srs(root)
    except FileNotFoundError as exc:
        print(f"FAIL {exc}")
        return 1
    target = root / AI_CONTEXT / "SRS.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(f"WRITE {AI_CONTEXT}/SRS.html")
    for heading in missing:
        print(f"WARN heading not found, section flagged not rendered: {heading}")
    if missing:
        print(
            f"WARN {len(missing)} section(s) use non-template headings — SRS.html shows them as "
            "flagged, not blank-by-content. Rename the heading in the source to match the "
            "project-standard template, or accept the gap."
        )
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
    check_parser.add_argument(
        "--ready",
        action="store_true",
        help="Also require owner-resolved outcome and non-bootstrap requirement state.",
    )

    srs_parser = subparsers.add_parser(
        "render-srs", help="Generate ai-context/SRS.html from PROJECT.md and DATA_MODEL.md."
    )
    srs_parser.add_argument("root", type=Path)

    lock_parser = subparsers.add_parser(
        "lock-spec", help="Print the Spec lock line to freeze PROJECT.md/DATA_MODEL.md at their current content."
    )
    lock_parser.add_argument("root", type=Path)

    migrate_parser = subparsers.add_parser(
        "migrate",
        help=(
            "Bring a project onto the ai-context/ layout: bootstrap if nothing exists, move "
            "legacy root files whose headings already match the template, and report anything "
            "that needs a content rewrite first."
        ),
    )
    migrate_parser.add_argument("root", type=Path)
    migrate_parser.add_argument("--name", help="Used only when bootstrapping a project with no existing files.")
    migrate_parser.add_argument(
        "--profile", choices=("minimal", "software"), default="minimal",
        help="Used only when bootstrapping a project with no existing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if args.command == "bootstrap":
        return bootstrap(root, args.name, args.profile)
    if args.command == "render-srs":
        return render_srs_command(root)
    if args.command == "lock-spec":
        return lock_spec_command(root)
    if args.command == "migrate":
        return migrate(root, args.name, args.profile)
    return check(root, ready=args.ready)


if __name__ == "__main__":
    sys.exit(main())
