#!/usr/bin/env python3
"""Contract regression checks for the portable output packages."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    sum_skill = read("plugins/james-productivity/skills/sum-meet/SKILL.md")
    sum_template = read("plugins/james-productivity/skills/sum-meet/assets/meeting-record.html")
    one_skill = read("plugins/james-productivity/skills/one-page-pls/SKILL.md")
    one_contract = read("plugins/james-productivity/skills/one-page-pls/references/content-contract.md")
    one_render_qa = read("plugins/james-productivity/skills/one-page-pls/references/render-qa.md")
    one_template = read("plugins/james-productivity/skills/one-page-pls/assets/a4-landscape-template.html")
    make_it_james = read("plugins/james-core/rules/make-it-james/make-it-james.md")
    make_it_james_ux = read("plugins/james-software/skills/make-it-james-ux/SKILL.md")
    make_it_james_standard = read("plugins/james-software/skills/make-it-james-ux/references/standard.md")
    final_it = read("plugins/james-productivity/skills/final-it/SKILL.md")
    behavior_cases = read("tests/behavioral-cases.md")

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
    assert "embed_ibm_plex_thai.py" in make_it_james_ux
    assert "not self-contained proof" in sum_skill + one_skill
    assert "HTML-only delivery" in make_it_james_ux
    assert "Never generate a PDF merely to prove" in make_it_james_ux
    assert "stays HTML-only" in final_it
    assert "HTML only by default" in one_skill
    assert "Do not create a PDF merely" in sum_skill
    assert "Never infer PDF need" in sum_skill
    assert "directly confirmed" in make_it_james + make_it_james_ux + make_it_james_standard + final_it + sum_skill
    assert "Never infer that constraint" in make_it_james_ux + make_it_james_standard
    assert "without exporting a PDF" in one_render_qa
    assert "If PDF was explicitly requested" in one_render_qa
    assert "browser print emulation" in behavior_cases
    assert "without exporting a PDF" in behavior_cases
    assert "Legitimate counter-case" in behavior_cases
    assert "directly confirmed" in sum_skill + behavior_cases
    assert "explicit PDF request" in make_it_james_standard

    action = re.compile(
        r"(?i)(?:create|generate|export|render|deliver|convert|produce|attach|include|save|"
        r"สร้าง|ผลิต|ส่งมอบ|แปลง|แนบ|เรนเดอร์).{0,100}\bpdf\b|"
        r"\bpdf\b.{0,100}(?:create|generate|export|render|deliver|convert|produce|attach|include|save|"
        r"สร้าง|ผลิต|ส่งมอบ|แปลง|แนบ|เรนเดอร์)"
    )
    condition = re.compile(
        r"(?i)explicit|request|when|if|confirmed|authoritative|only|never|unless|not|"
        r"ถ้า|เมื่อ|ขอ|เฉพาะ|ยืนยัน|ห้าม"
    )
    for path in sorted((ROOT / "skills").rglob("*.md")) + sorted((ROOT / "aliases").rglob("*.md")):
        in_frontmatter = False
        frontmatter_closed = False
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line_number == 1 and line.strip() == "---":
                in_frontmatter = True
                continue
            if in_frontmatter and line.strip() == "---":
                in_frontmatter = False
                frontmatter_closed = True
                continue
            if in_frontmatter or not frontmatter_closed and path.name == "SKILL.md":
                continue
            if action.search(line):
                assert condition.search(line), (
                    f"implicit PDF action without explicit condition: {path.relative_to(ROOT)}:{line_number}: {line}"
                )

    combined = sum_template + one_template
    for forbidden in ("Poppins", "linear-gradient(", "radial-gradient(", "border-left:"):
        assert forbidden not in combined, f"forbidden output pattern returned: {forbidden}"

    print("PASS output semantic and template contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
