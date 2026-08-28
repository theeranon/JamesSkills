#!/usr/bin/env python3
"""Contract regression checks for the portable output packages."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    sum_skill = read("skills/outputs/sum-meet/SKILL.md")
    sum_template = read("skills/outputs/sum-meet/assets/meeting-record.html")
    one_skill = read("skills/outputs/one-page-pls/SKILL.md")
    one_contract = read("skills/outputs/one-page-pls/references/content-contract.md")
    one_template = read("skills/outputs/one-page-pls/assets/a4-landscape-template.html")
    make_it_james = read("skills/standards/make-it-james/SKILL.md")

    for required in (
        "current conversation",
        "one self-contained A4 portrait HTML file",
        "every topic",
        "same file",
        "source evidence",
    ):
        assert required in sum_skill, f"sum-meet contract missing: {required}"
    assert "size: A4 portrait" in sum_template
    assert ".topic-zone + .topic-zone" in sum_template
    assert "[[DOCUMENT_TITLE]]" in sum_template

    for required in (
        "one topic = one file",
        "Never mix independent agendas",
        "appendix or full record",
        "one-page unsuitable",
    ):
        assert required in one_skill + one_contract, f"one-page contract missing: {required}"
    assert "size: A4 landscape" in one_template
    assert one_template.count('class="page"') == 1
    assert "[[TOPIC_TITLE]]" in one_template
    assert "Project Cedar" not in one_template
    assert "font embedding helper" in sum_skill and "font embedding helper" in one_skill
    assert "embed_ibm_plex_thai.py" in make_it_james
    assert "not self-contained proof" in sum_skill + one_skill

    combined = sum_template + one_template
    for forbidden in ("Poppins", "linear-gradient(", "radial-gradient(", "border-left:"):
        assert forbidden not in combined, f"forbidden output pattern returned: {forbidden}"

    print("PASS output semantic and template contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
