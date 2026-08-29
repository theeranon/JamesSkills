#!/usr/bin/env python3
"""Inspect the portable SolutionsIMPACT house-framework registry."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
REGISTRY = REPO_ROOT / "packs" / "frameworks" / "registry.json"
REQUIRED = {
    "id",
    "name",
    "owner",
    "kind",
    "level",
    "lifecycle",
    "version",
    "visibility",
    "fit",
    "permitted_scope",
    "boundary",
    "source_refs",
    "approval_record",
}

SOURCE_REQUIRED = {"source_id", "locator", "claim", "limitation", "rights", "retrieved"}
APPROVAL_REQUIRED = {"status", "approver", "date", "locator"}
ALLOWED_LIFECYCLES = {"source-gap", "candidate", "pilot", "approved", "superseded", "retired"}


def validate_locator(locator: str, item_id: str, field: str) -> None:
    if locator.startswith(("https://", "http://")):
        return
    candidate = (REPO_ROOT / locator.split("#", 1)[0]).resolve()
    try:
        candidate.relative_to(REPO_ROOT)
    except ValueError as error:
        raise ValueError(f"item {item_id} has out-of-repo {field} locator") from error
    if not candidate.is_file():
        raise ValueError(f"item {item_id} has missing {field} locator: {locator}")


def load_registry(path: Path = REGISTRY) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1 or not isinstance(payload.get("items"), list):
        raise ValueError("unsupported or empty framework registry")
    ids: set[str] = set()
    for index, item in enumerate(payload["items"]):
        missing = REQUIRED - set(item)
        if missing:
            raise ValueError(f"item {index} missing fields: {sorted(missing)}")
        if item["id"] in ids:
            raise ValueError(f"duplicate framework id: {item['id']}")
        if not isinstance(item["fit"], list) or not item["fit"]:
            raise ValueError(f"item {item['id']} has no fit terms")
        if item["lifecycle"] not in ALLOWED_LIFECYCLES:
            raise ValueError(f"item {item['id']} has invalid lifecycle: {item['lifecycle']}")
        for field in ("version", "permitted_scope", "boundary"):
            if not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f"item {item['id']} has empty {field}")
        if not isinstance(item["source_refs"], list) or not item["source_refs"]:
            raise ValueError(f"item {item['id']} has no source refs")
        for source in item["source_refs"]:
            source_missing = SOURCE_REQUIRED - set(source)
            if source_missing or not all(
                isinstance(source[key], str) and source[key].strip()
                for key in SOURCE_REQUIRED
            ):
                raise ValueError(
                    f"item {item['id']} has invalid source ref: {sorted(source_missing)}"
                )
            validate_locator(source["locator"], item["id"], "source")
        approval = item["approval_record"]
        if not isinstance(approval, dict) or APPROVAL_REQUIRED - set(approval):
            raise ValueError(f"item {item['id']} has invalid approval record")
        if not isinstance(approval["status"], str) or not isinstance(approval["locator"], str):
            raise ValueError(f"item {item['id']} has invalid approval status or locator")
        validate_locator(approval["locator"], item["id"], "approval")
        if item["lifecycle"] in {"source-gap", "candidate"} and approval["status"] != "not-approved":
            raise ValueError(f"item {item['id']} falsely claims approval")
        if item["lifecycle"] == "approved" and (
            approval["status"] != "approved"
            or not isinstance(approval["approver"], str)
            or not isinstance(approval["date"], str)
        ):
            raise ValueError(f"item {item['id']} lacks approved authority")
        if item["lifecycle"] == "pilot" and (
            approval["status"] != "pilot-authorized"
            or not isinstance(approval["approver"], str)
            or not isinstance(approval["date"], str)
        ):
            raise ValueError(f"item {item['id']} lacks pilot authority")
        ids.add(item["id"])
    return payload


def tokens(value: str) -> set[str]:
    return {
        token.casefold()
        for token in re.findall(r"[\w\-]+", value, flags=re.UNICODE)
        if len(token) > 1
    }


def search(query: str, items: list[dict]) -> list[tuple[int, dict]]:
    query_tokens = tokens(query)
    ranked: list[tuple[int, dict]] = []
    for item in items:
        searchable = " ".join(
            [
                item["id"],
                item["name"],
                item["kind"],
                item["level"],
                item["permitted_scope"],
                item["boundary"],
                *item["fit"],
            ]
        )
        item_tokens = tokens(searchable)
        score = len(query_tokens & item_tokens)
        if score:
            ranked.append((score, item))
    return sorted(ranked, key=lambda pair: (-pair[0], pair[1]["name"]))


def print_items(items: list[dict]) -> None:
    for item in items:
        print(
            f"{item['id']}\t{item['kind']}\t{item['level']}\t"
            f"{item['lifecycle']}\t{item['version']}\t{item['name']}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("list")
    search_parser = sub.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    registry = load_registry(args.registry.expanduser().resolve())
    if args.command == "validate":
        print(f"PASS framework registry items={len(registry['items'])}")
        return 0
    if args.command == "list":
        print_items(registry["items"])
        return 0

    ranked = search(args.query, registry["items"])
    if args.json:
        print(json.dumps([item for _score, item in ranked], ensure_ascii=False, indent=2))
    else:
        print_items([item for _score, item in ranked])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
