#!/usr/bin/env python3
"""Rebuild knowledge/00-index.md and checklists/02-master-audit-checklist.md
from the chapter files' frontmatter and their `## Audit checks` sections.
Run after editing any knowledge/chNN-*.md file."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
K = ROOT / "references" / "knowledge"

AREAS = [
    ("A. Goal, positioning & topic ownership", ["ch01", "ch03", "ch18"]),
    ("B. Measurement, baseline & tracking", ["ch05", "ch06", "ch08"]),
    ("C. Competitors & citation gaps", ["ch07", "ch02"]),
    ("D. Crawl, index, render & AI-ready foundations", ["ch10", "ch11"]),
    ("E. Topic plan, architecture & topical authority", ["ch09", "ch13"]),
    ("F. Bottom-of-funnel / commercial pages", ["ch12"]),
    ("G. Page-level quality & underperformers", ["ch14"]),
    ("H. Media, schema, datasets & creative assets", ["ch15", "ch23"]),
    ("I. Brand entity, consistency & profiles", ["ch16", "ch17"]),
    ("J. Reviews", ["ch19"]),
    ("K. Links, mentions & digital PR", ["ch20"]),
    ("L. Governance, risk, crawler policy & compliance", ["ch21"]),
    ("M. Strategy sanity (myths) & vocabulary", ["ch22", "ch04", "ch00"]),
]


def parse(f):
    t = f.read_text(encoding="utf-8")
    meta = {}
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    sec = re.search(r"(?ms)^## Audit checks\s*\n(.*?)(?=^## |\Z)", t)
    items = [l.strip() for l in (sec.group(1).splitlines() if sec else []) if l.strip().startswith("- [")]
    heads = re.findall(r"(?m)^## (.+)$", t)
    return meta, items, heads


files = {f.name[:4]: f for f in sorted(K.glob("ch*.md"))}
data = {cid: parse(f) for cid, f in files.items()}

idx = ["---", "id: index", "title: Knowledge base index", "tags: [index, map, chapters, overview]",
       "use_when: First file to read; find which chapter answers a question.", "---", "",
       "# AI SEO knowledge index (AI SEO For Dummies, Nathan Gotch — distilled)", "",
       "Search: `python3 scripts/search.py \"<english query>\" -k 5` · Section dump: `--section \"Audit checks\"`", "",
       "| id | file | use when |", "|---|---|---|"]
for cid, f in files.items():
    meta = data[cid][0]
    idx.append(f"| {cid} | [{f.name}]({f.name}) | {meta.get('use_when', '')} |")
idx += ["", "## Sections per chapter"]
for cid, f in files.items():
    idx.append(f"- **{cid} {data[cid][0].get('title', '')}** — " + " · ".join(h for h in data[cid][2]))
(K / "00-index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

out = ["---", "id: master-audit", "title: Master AI SEO audit checklist",
       "tags: [audit, checklist, master, scorecard, technical, content, brand, reviews, links, schema]",
       "use_when: Step 4 of the workflow — score every item against the real site with evidence.", "---", "",
       "# Master AI SEO audit checklist",
       "", "Score each item ✅ / ⚠️ / ❌ / ❓ with evidence (see 03-action-plan-template.md). "
       "Open the source chapter for criteria and fixes. Items marked off-site may need the user's accounts.", ""]
total = 0
for area, ids in AREAS:
    out.append(f"## {area}")
    for cid in ids:
        if cid not in data:
            continue
        for it in data[cid][1]:
            out.append(f"{it} `{cid}`")
            total += 1
    out.append("")
out.insert(8, f"Total items: {total}. Sources: every chapter's `## Audit checks` section (regenerate with scripts/build_index.py).\n")
(ROOT / "references" / "checklists" / "02-master-audit-checklist.md").write_text("\n".join(out), encoding="utf-8")
print(f"index: {len(files)} chapters · checklist: {total} items")
