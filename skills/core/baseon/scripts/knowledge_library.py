#!/usr/bin/env python3
"""Discover, scaffold, and validate the portable knowledge-lens library."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any


REGISTRY_PATH = Path("packs/knowledge/registry.json")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?$")
SOURCE_REF = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)#([a-z0-9]+(?:-[a-z0-9]+)*)`")
CLAIM_HEADING = re.compile(r"^([A-Z][A-Z0-9_-]*-[0-9]{3,})\s+—\s+.+$")
SELECTABLE = {"reviewed-private", "promoted"}
STATUSES = {"draft", "reviewed-private", "promoted", "retired"}
SOURCE_ACCESS = {"external-local", "web", "repository-authored", "mixed"}
ALLOWED_REFERENCE_NAMES = {"concepts.md", "applications.md", "limitations.md"}
SOURCE_FIELDS = {
    "schema_version",
    "id",
    "title",
    "creator",
    "edition_or_version",
    "source_type",
    "status",
    "source_access",
    "provenance",
    "reference_urls",
    "acquired_at",
    "rights_status",
    "rights_basis",
    "raw_source_in_repo",
    "content_sha256",
    "evidence_label",
    "locators",
    "scope",
    "not_for_use",
}


def discover_repo_root(start: Path) -> Path:
    configured = os.environ.get("JAMES_SKILLS_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    for candidate in (start.parent, *start.parents):
        if (candidate / REGISTRY_PATH).is_file():
            return candidate
    return start.parent.parent


REPO_ROOT = discover_repo_root(Path(__file__).resolve())
MANIFEST_FIELDS = {
    "schema_version",
    "id",
    "title",
    "kind",
    "version",
    "status",
    "entrypoint",
    "source_ids",
    "use_cases",
    "not_for",
    "creator_family_id",
    "model_family_id",
    "rights_class",
    "raw_source_in_repo",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def safe_path(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes repository: {relative}") from exc
    return path


def load_registry(root: Path) -> dict[str, Any]:
    path = root / REGISTRY_PATH
    if not path.is_file():
        raise FileNotFoundError(f"registry missing: {path}")
    registry = load_json(path)
    if registry.get("schema_version") != 1:
        raise ValueError("registry schema_version must be 1")
    return registry


def duplicate_ids(items: list[dict[str, Any]]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in items:
        item_id = item.get("id")
        if item_id in seen:
            duplicates.add(item_id)
        seen.add(item_id)
    return duplicates


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        registry = load_registry(root)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        return [str(exc)]

    source_entries = registry.get("sources", [])
    lens_entries = registry.get("lenses", [])
    if not isinstance(source_entries, list) or not isinstance(lens_entries, list):
        return ["registry sources and lenses must be arrays"]
    for group_name, items in (("source", source_entries), ("lens", lens_entries)):
        for duplicate in sorted(duplicate_ids(items)):
            errors.append(f"duplicate {group_name} id: {duplicate}")

    lens_ids = {entry.get("id") for entry in lens_entries}
    lens_aliases: dict[str, str] = {}
    for entry in lens_entries:
        lens_id = entry.get("id", "")
        aliases = entry.get("aliases", [])
        if not isinstance(aliases, list):
            errors.append(f"lens {lens_id} aliases must be an array")
            continue
        for alias in aliases:
            if not isinstance(alias, str) or not SLUG.fullmatch(alias):
                errors.append(f"lens {lens_id} has invalid alias: {alias!r}")
                continue
            if alias in lens_ids:
                errors.append(f"lens alias collides with canonical id: {alias}")
            if alias in lens_aliases:
                errors.append(
                    f"duplicate lens alias: {alias} ({lens_aliases[alias]} and {lens_id})"
                )
            lens_aliases[alias] = lens_id

    sources: dict[str, dict[str, Any]] = {}
    source_locators: dict[str, set[str]] = {}
    for entry in source_entries:
        source_id = entry.get("id", "")
        relative = entry.get("path", "")
        if not SLUG.fullmatch(source_id):
            errors.append(f"invalid source id: {source_id!r}")
            continue
        expected_relative = f"packs/knowledge/sources/{source_id}.json"
        if relative != expected_relative:
            errors.append(f"source {source_id} path must be {expected_relative}")
        try:
            path = safe_path(root, relative)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if not path.is_file():
            errors.append(f"source card missing: {relative}")
            continue
        try:
            card = load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"invalid source JSON {relative}: {exc}")
            continue
        missing = SOURCE_FIELDS - set(card)
        if missing:
            errors.append(f"source {source_id} missing fields: {sorted(missing)}")
        for field in (
            "title",
            "creator",
            "edition_or_version",
            "source_type",
            "provenance",
            "acquired_at",
            "rights_status",
            "rights_basis",
            "evidence_label",
        ):
            if not str(card.get(field, "")).strip():
                errors.append(f"source {source_id} has empty {field}")
        try:
            date.fromisoformat(str(card.get("acquired_at", "")))
        except ValueError:
            errors.append(f"source {source_id} acquired_at is not an ISO date")
        urls = card.get("reference_urls")
        if not isinstance(urls, list) or any(
            not isinstance(url, str) or not url.startswith(("https://", "http://"))
            for url in urls or []
        ):
            errors.append(f"source {source_id} has invalid reference_urls")
        if card.get("id") != source_id:
            errors.append(f"source id mismatch: {source_id} != {card.get('id')}")
        if card.get("schema_version") != 1:
            errors.append(f"source {source_id} schema_version must be 1")
        status = card.get("status")
        if status not in STATUSES:
            errors.append(f"source {source_id} has invalid status")
        source_access = card.get("source_access")
        if source_access not in SOURCE_ACCESS:
            errors.append(f"source {source_id} has invalid source_access")
        if card.get("raw_source_in_repo") is not False:
            errors.append(f"source {source_id} must keep raw_source_in_repo false")
        digest = card.get("content_sha256")
        if digest is not None and not SHA256.fullmatch(str(digest)):
            errors.append(f"source {source_id} has invalid SHA-256")
        repository_path = card.get("repository_path")
        if repository_path:
            try:
                authored_path = safe_path(root, repository_path)
            except ValueError as exc:
                errors.append(str(exc))
            else:
                if not authored_path.is_file():
                    errors.append(f"source {source_id} repository_path missing: {repository_path}")
                elif digest:
                    actual = hashlib.sha256(authored_path.read_bytes()).hexdigest()
                    if actual != digest:
                        errors.append(f"source {source_id} repository SHA-256 drift")
        serialized = json.dumps(card)
        if ("/" + "Users/") in serialized or ("C:" + "\\\\Users\\\\") in serialized:
            errors.append(f"source {source_id} contains a machine-specific path")
        locators = card.get("locators", [])
        locator_ids = [item.get("id") for item in locators if isinstance(item, dict)]
        if len(locator_ids) != len(locators) or len(locator_ids) != len(set(locator_ids)) or any(
            not isinstance(item, str) or not SLUG.fullmatch(item) for item in locator_ids
        ):
            errors.append(f"source {source_id} has invalid or duplicate locator ids")
        if status != "draft":
            if not locator_ids:
                errors.append(f"source {source_id} has no locators")
            if any(
                not str(item.get("location", "")).strip()
                or not str(item.get("scope", "")).strip()
                or "TODO" in str(item.get("location", ""))
                or item.get("id") == "add-locator"
                for item in locators
                if isinstance(item, dict)
            ):
                errors.append(f"source {source_id} has unresolved locator placeholders")
            if not card.get("scope") or not card.get("not_for_use"):
                errors.append(f"source {source_id} lacks scope or not_for_use")
            if source_access in {"external-local", "repository-authored", "mixed"} and not digest:
                errors.append(f"source {source_id} requires SHA-256 for {source_access}")
            has_pointer = bool(
                card.get("reference_urls") or card.get("isbn") or card.get("repository_path")
            )
            if not has_pointer:
                errors.append(f"source {source_id} lacks URL, ISBN, or repository pointer")
        if status == "promoted" and (
            str(card.get("rights_status", "")).strip().lower() in {"", "unknown"}
            or str(card.get("rights_basis", "")).strip().lower() in {"", "unknown"}
        ):
            errors.append(f"source {source_id} promoted with unresolved rights")
        sources[source_id] = card
        source_locators[source_id] = set(locator_ids)

    for entry in lens_entries:
        lens_id = entry.get("id", "")
        relative = entry.get("path", "")
        if not SLUG.fullmatch(lens_id):
            errors.append(f"invalid lens id: {lens_id!r}")
            continue
        expected_relative = f"packs/knowledge/lenses/{lens_id}/manifest.json"
        if relative != expected_relative:
            errors.append(f"lens {lens_id} path must be {expected_relative}")
        try:
            manifest_path = safe_path(root, relative)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if not manifest_path.is_file():
            errors.append(f"lens manifest missing: {relative}")
            continue
        try:
            manifest = load_json(manifest_path)
        except json.JSONDecodeError as exc:
            errors.append(f"invalid lens JSON {relative}: {exc}")
            continue
        missing = MANIFEST_FIELDS - set(manifest)
        if missing:
            errors.append(f"lens {lens_id} missing fields: {sorted(missing)}")
        if manifest.get("id") != lens_id:
            errors.append(f"lens id mismatch: {lens_id} != {manifest.get('id')}")
        if manifest.get("schema_version") != 1:
            errors.append(f"lens {lens_id} schema_version must be 1")
        lens_status = manifest.get("status")
        if lens_status not in STATUSES:
            errors.append(f"lens {lens_id} has invalid status")
        if not SEMVER.fullmatch(str(manifest.get("version", ""))):
            errors.append(f"lens {lens_id} version is not semantic")
        if manifest.get("raw_source_in_repo") is not False:
            errors.append(f"lens {lens_id} must keep raw_source_in_repo false")
        for field in ("creator_family_id", "model_family_id"):
            family_id = manifest.get(field)
            if lens_status != "draft" and (
                not isinstance(family_id, str) or not SLUG.fullmatch(family_id)
            ):
                errors.append(f"lens {lens_id} has invalid {field}")
        entrypoint = manifest.get("entrypoint")
        if entrypoint != "index.md":
            errors.append(f"lens {lens_id} entrypoint must be index.md")
        manifest_source_ids = manifest.get("source_ids", [])
        if not isinstance(manifest_source_ids, list) or not manifest_source_ids:
            errors.append(f"lens {lens_id} has no source_ids")
            manifest_source_ids = []
        for source_id in manifest_source_ids:
            if source_id not in sources:
                errors.append(f"lens {lens_id} references unknown source: {source_id}")
            elif lens_status in SELECTABLE and sources[source_id].get("status") not in SELECTABLE:
                errors.append(
                    f"lens {lens_id} is selectable but source {source_id} is "
                    f"{sources[source_id].get('status')}"
                )
        if lens_status != "draft" and (
            not isinstance(manifest.get("use_cases"), list)
            or not manifest.get("use_cases")
            or not isinstance(manifest.get("not_for"), list)
            or not manifest.get("not_for")
        ):
            errors.append(f"lens {lens_id} lacks use_cases or not_for")

        lens_dir = manifest_path.parent
        required_files = {
            "index.md",
            "references/concepts.md",
            "references/applications.md",
            "references/limitations.md",
        }
        for required in sorted(required_files):
            if not (lens_dir / required).is_file():
                errors.append(f"lens {lens_id} missing: {required}")
        index_path = lens_dir / "index.md"
        concepts_path = lens_dir / "references/concepts.md"
        applications_path = lens_dir / "references/applications.md"
        limitations_path = lens_dir / "references/limitations.md"
        if index_path.is_file() and "Independent private synthesis" not in index_path.read_text(encoding="utf-8"):
            errors.append(f"lens {lens_id} missing non-affiliation notice")
        if applications_path.is_file() and "Reversible experiments" not in applications_path.read_text(encoding="utf-8"):
            errors.append(f"lens {lens_id} missing reversible experiments")
        if limitations_path.is_file():
            limitations = limitations_path.read_text(encoding="utf-8")
            for heading in ("Evidence boundary", "Prohibited uses"):
                if heading not in limitations:
                    errors.append(f"lens {lens_id} missing limitations section: {heading}")
        if concepts_path.is_file():
            concepts = concepts_path.read_text(encoding="utf-8")
            sections = re.split(r"(?m)^##\s+", concepts)[1:]
            if not sections:
                errors.append(f"lens {lens_id} has no claim cards")
            claim_ids: set[str] = set()
            for section in sections:
                heading, _, body = section.partition("\n")
                match = CLAIM_HEADING.fullmatch(heading.strip())
                if not match:
                    errors.append(f"lens {lens_id} malformed claim heading: {heading.strip()}")
                    continue
                claim_id = match.group(1)
                if claim_id in claim_ids:
                    errors.append(f"lens {lens_id} duplicate claim id: {claim_id}")
                claim_ids.add(claim_id)
                evidence = re.findall(
                    r"(?m)^- Evidence: `\[(official claim|independent evidence|James rule|inference)\]`$",
                    body,
                )
                confidence = re.findall(
                    r"(?m)^- Confidence: `(source-faithful|supported|mixed|tentative)`$",
                    body,
                )
                refs = SOURCE_REF.findall(body)
                if len(evidence) != 1 or len(confidence) != 1 or not refs:
                    errors.append(f"lens {lens_id} claim {claim_id} lacks evidence, source, or confidence")
                for source_id, locator_id in refs:
                    if source_id not in manifest_source_ids:
                        errors.append(
                            f"lens {lens_id} claim {claim_id} uses undeclared source: {source_id}"
                        )
                    if source_id not in sources:
                        errors.append(
                            f"lens {lens_id} claim {claim_id} references unknown source: {source_id}"
                        )
                    elif locator_id not in source_locators.get(source_id, set()):
                        errors.append(
                            f"lens {lens_id} claim {claim_id} references unknown locator: "
                            f"{source_id}#{locator_id}"
                        )
            if lens_status != "draft" and ("TODO" in concepts or "#add-locator`" in concepts):
                errors.append(f"lens {lens_id} promoted with unresolved claim placeholders")

    knowledge_root = root / "packs/knowledge"
    if knowledge_root.is_dir():
        for path in knowledge_root.rglob("*"):
            if not path.is_file():
                continue
            if path.stat().st_size > 128_000:
                errors.append(f"knowledge file exceeds synthesis size gate: {path.relative_to(root)}")
            relative = path.relative_to(knowledge_root)
            parts = relative.parts
            allowed = relative.as_posix() == "registry.json"
            allowed = allowed or (
                len(parts) == 2 and parts[0] == "sources" and path.suffix == ".json"
            )
            allowed = allowed or (
                len(parts) == 3
                and parts[0] == "lenses"
                and parts[2] in {"manifest.json", "index.md"}
            )
            allowed = allowed or (
                len(parts) == 4
                and parts[0] == "lenses"
                and parts[2] == "references"
                and parts[3] in ALLOWED_REFERENCE_NAMES
            )
            if not allowed:
                errors.append(
                    f"unapproved or raw file in knowledge library: {path.relative_to(root)}"
                )
    return errors


def list_library(root: Path, include_unready: bool = False) -> int:
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    registry = load_registry(root)
    source_by_id = {item["id"]: item for item in registry.get("sources", [])}
    print("LENSES")
    for entry in registry.get("lenses", []):
        manifest = load_json(safe_path(root, entry["path"]))
        if not include_unready and manifest.get("status") not in SELECTABLE:
            continue
        print(
            f"{manifest['id']}\t{manifest['kind']}\t{manifest['version']}\t"
            f"{manifest['status']}\taliases={','.join(entry.get('aliases', []))}\t"
            f"sources={','.join(manifest['source_ids'])}"
        )
    print("SOURCES")
    for source_id in sorted(source_by_id):
        card = load_json(safe_path(root, source_by_id[source_id]["path"]))
        if not include_unready and card.get("status") not in SELECTABLE:
            continue
        print(f"{source_id}\t{card['source_type']}\t{card['status']}\t{card['title']}")
    return 0


def show_lens(root: Path, lens_id: str, allow_unready: bool = False) -> int:
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    registry = load_registry(root)
    entry = next(
        (
            item
            for item in registry.get("lenses", [])
            if item.get("id") == lens_id or lens_id in item.get("aliases", [])
        ),
        None,
    )
    if entry is None:
        print(f"Unknown lens: {lens_id}", file=sys.stderr)
        return 1
    manifest_path = safe_path(root, entry["path"])
    manifest = load_json(manifest_path)
    if lens_id != manifest["id"]:
        print(f"resolved\t{lens_id}\t{manifest['id']}")
    if not allow_unready and manifest.get("status") not in SELECTABLE:
        print(
            f"Lens is not runtime-ready: {lens_id} status={manifest.get('status')}",
            file=sys.stderr,
        )
        return 2
    lens_dir = manifest_path.parent
    print(f"manifest\t{manifest_path}")
    print(f"entrypoint\t{safe_path(lens_dir, manifest['entrypoint'])}")
    for name in ("concepts.md", "applications.md", "limitations.md"):
        print(f"reference\t{lens_dir / 'references' / name}")
    for source_id in manifest["source_ids"]:
        source_entry = next(item for item in registry["sources"] if item["id"] == source_id)
        source_path = safe_path(root, source_entry["path"])
        source = load_json(source_path)
        if not allow_unready and source.get("status") not in SELECTABLE:
            print(
                f"Source is not runtime-ready: {source_id} status={source.get('status')}",
                file=sys.stderr,
            )
            return 2
        print(f"source\t{source_path}")
    return 0


def update_registry(root: Path, registry: dict[str, Any]) -> None:
    registry["sources"] = sorted(registry.get("sources", []), key=lambda item: item["id"])
    registry["lenses"] = sorted(registry.get("lenses", []), key=lambda item: item["id"])
    write_json(root / REGISTRY_PATH, registry)


def create_source(root: Path, args: argparse.Namespace) -> int:
    if not SLUG.fullmatch(args.source_id):
        raise ValueError("source id must be lowercase kebab-case")
    registry = load_registry(root)
    if any(item["id"] == args.source_id for item in registry.get("sources", [])):
        raise ValueError(f"source already exists: {args.source_id}")
    relative = f"packs/knowledge/sources/{args.source_id}.json"
    path = safe_path(root, relative)
    card = {
        "schema_version": 1,
        "id": args.source_id,
        "title": args.title,
        "creator": args.creator,
        "edition_or_version": args.edition,
        "source_type": args.source_type,
        "status": "draft",
        "source_access": args.source_access,
        "provenance": args.provenance,
        "reference_urls": args.url,
        "acquired_at": args.acquired_at,
        "rights_status": args.rights_status,
        "rights_basis": "citation_and_original_paraphrase_only",
        "raw_source_in_repo": False,
        "content_sha256": args.sha256,
        "evidence_label": args.evidence_label,
        "locators": [
            {
                "id": "add-locator",
                "location": "TODO page, chapter, timestamp, or URL anchor",
                "scope": "Replace before promotion",
            }
        ],
        "scope": [],
        "not_for_use": [],
    }
    write_json(path, card)
    registry.setdefault("sources", []).append({"id": args.source_id, "path": relative})
    update_registry(root, registry)
    print(f"Created draft source: {relative}")
    return 0


def create_lens(root: Path, args: argparse.Namespace) -> int:
    if not SLUG.fullmatch(args.lens_id):
        raise ValueError("lens id must be lowercase kebab-case")
    registry = load_registry(root)
    source_ids = {item["id"] for item in registry.get("sources", [])}
    missing = sorted(set(args.source) - source_ids)
    if missing:
        raise ValueError(f"unknown source ids: {', '.join(missing)}")
    existing_lens_names = {
        value
        for item in registry.get("lenses", [])
        for value in (item["id"], *item.get("aliases", []))
    }
    if args.lens_id in existing_lens_names:
        raise ValueError(f"lens already exists: {args.lens_id}")
    relative = f"packs/knowledge/lenses/{args.lens_id}/manifest.json"
    manifest_path = safe_path(root, relative)
    lens_dir = manifest_path.parent
    manifest = {
        "schema_version": 1,
        "id": args.lens_id,
        "title": args.title,
        "kind": args.kind,
        "version": "0.1.0",
        "status": "draft",
        "entrypoint": "index.md",
        "source_ids": args.source,
        "use_cases": [],
        "not_for": [],
        "creator_family_id": None,
        "model_family_id": None,
        "rights_class": "private-original-synthesis",
        "raw_source_in_repo": False,
    }
    write_json(manifest_path, manifest)
    replacements = {
        "__TITLE__": args.title,
        "__LENS_ID__": args.lens_id,
        "__LENS_ID_UPPER__": args.lens_id.upper().replace("-", "_"),
        "__SOURCE_ID__": args.source[0],
    }
    asset_dir = root / "skills/core/baseon/assets"
    templates = {
        "lens-index.template.md": lens_dir / "index.md",
        "lens-concepts.template.md": lens_dir / "references/concepts.md",
        "lens-applications.template.md": lens_dir / "references/applications.md",
        "lens-limitations.template.md": lens_dir / "references/limitations.md",
    }
    for template_name, destination in templates.items():
        content = (asset_dir / template_name).read_text(encoding="utf-8")
        for old, new in replacements.items():
            content = content.replace(old, new)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
    registry.setdefault("lenses", []).append(
        {"id": args.lens_id, "aliases": [], "path": relative}
    )
    update_registry(root, registry)
    print(f"Created draft lens: {relative}")
    return 0


def sha256_file(path: Path) -> int:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    print(digest.hexdigest())
    return 0


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description=__doc__)
    value.add_argument("--root", type=Path, default=REPO_ROOT, help=argparse.SUPPRESS)
    commands = value.add_subparsers(dest="command", required=True)
    list_parser = commands.add_parser("list", help="List runtime-ready lenses and sources")
    list_parser.add_argument("--all", action="store_true", help="Include draft and retired items")
    validate_parser = commands.add_parser("validate", help="Validate source and lens contracts")
    validate_parser.set_defaults(command="validate")
    show = commands.add_parser("show", help="Show all files needed for one lens")
    show.add_argument("lens_id")
    show.add_argument(
        "--allow-unready", action="store_true", help="Open draft or retired material for maintenance"
    )
    digest = commands.add_parser("sha256", help="Hash an external source without copying it")
    digest.add_argument("path", type=Path)

    source = commands.add_parser("new-source", help="Register a new external source as draft")
    source.add_argument("source_id")
    source.add_argument("--title", required=True)
    source.add_argument("--creator", required=True)
    source.add_argument("--edition", required=True)
    source.add_argument("--source-type", default="book")
    source.add_argument(
        "--source-access",
        choices=tuple(sorted(SOURCE_ACCESS)),
        default="external-local",
    )
    source.add_argument("--provenance", required=True)
    source.add_argument("--url", action="append", default=[])
    source.add_argument("--acquired-at", default=date.today().isoformat())
    source.add_argument("--rights-status", default="unknown")
    source.add_argument("--sha256", default=None)
    source.add_argument("--evidence-label", default="official claim")

    lens = commands.add_parser("new-lens", help="Create a draft lens from registered sources")
    lens.add_argument("lens_id")
    lens.add_argument("--title", required=True)
    lens.add_argument("--kind", choices=("framework", "book", "topic", "james-owned"), required=True)
    lens.add_argument("--source", action="append", required=True)
    return value


def main() -> int:
    args = parser().parse_args()
    root = args.root.resolve()
    try:
        if args.command == "list":
            return list_library(root, include_unready=args.all)
        if args.command == "show":
            return show_lens(root, args.lens_id, allow_unready=args.allow_unready)
        if args.command == "validate":
            errors = validate(root)
            if errors:
                for error in errors:
                    print(f"FAIL {error}")
                return 1
            registry = load_registry(root)
            print(
                f"PASS knowledge library sources={len(registry['sources'])} "
                f"lenses={len(registry['lenses'])}"
            )
            return 0
        if args.command == "new-source":
            return create_source(root, args)
        if args.command == "new-lens":
            return create_lens(root, args)
        if args.command == "sha256":
            return sha256_file(args.path)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
