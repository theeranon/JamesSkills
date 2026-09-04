#!/usr/bin/env python3
"""Keep the human skill handbook complete and honest against the catalog."""

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    handbook = (ROOT / "docs/SKILLS.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    cards = re.findall(r"^### `(/?[^`]+)`$", handbook, flags=re.MULTILINE)
    card_names = [card.removeprefix("/") for card in cards]
    counts = Counter(card_names)
    expected = {item["name"] for item in catalog["skills"]}

    assert set(card_names) == expected, (
        f"handbook mismatch missing={sorted(expected - set(card_names))} "
        f"extra={sorted(set(card_names) - expected)}"
    )
    assert all(count == 1 for count in counts.values()), f"duplicate cards: {counts}"
    assert "docs/SKILLS.md" in readme, "README must delegate detailed usage"

    for index, raw_heading in enumerate(cards):
        name = raw_heading.removeprefix("/")
        item = next(entry for entry in catalog["skills"] if entry["name"] == name)
        start = handbook.index(f"### `{raw_heading}`")
        later = [
            handbook.find(f"### `{next_heading}`", start + 1)
            for next_heading in cards[index + 1 :]
        ]
        later = [position for position in later if position >= 0]
        end = min(later) if later else len(handbook)
        card = handbook[start:end]

        assert f"- Canonical package: `{name}`" in card
        assert f"- Category: `{item['category']}`" in card
        assert f"- Lifecycle: `{item['status']}`" in card
        assert "- Use when:" in card and "- Result:" in card and "- Do not use when:" in card
        assert f"../plugins/{item['category']}/skills/{name}/SKILL.md" in card
        for alias in item.get("aliases", []):
            assert f"`{alias}`" in card, f"{name} card missing alias {alias}"

        if item["status"] == "pilot":
            assert not raw_heading.startswith("/"), f"pilot shown as slash call: {name}"
            assert "Not installed" in card, f"pilot availability unclear: {name}"
        elif item["name"] == "skill-router":
            assert not raw_heading.startswith("/"), f"internal shown as human call: {name}"
            assert "Internal support" in card, f"internal boundary unclear: {name}"
        else:
            assert raw_heading.startswith("/"), f"promoted call missing slash: {name}"

    print(f"PASS handbook canonical={len(expected)} aliases={sum(len(item.get('aliases', [])) for item in catalog['skills'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
