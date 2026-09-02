#!/usr/bin/env python3
"""Portable deterministic gate for the Make It James standard."""

from __future__ import annotations

import argparse
import os
import re
from collections import Counter
from pathlib import Path


TEXT_EXTENSIONS = {
    ".css", ".scss", ".sass", ".less", ".html", ".htm", ".tsx", ".jsx",
    ".vue", ".svelte", ".md", ".txt",
}
UI_EXTENSIONS = {
    ".css", ".scss", ".sass", ".less", ".html", ".htm", ".tsx", ".jsx",
    ".vue", ".svelte",
}
SKIP_PARTS = {
    ".git", "node_modules", "dist", "build", ".next", "coverage", "vendor",
    "archive", "archives",
}
THAI = re.compile(r"[\u0E00-\u0E7F]")
RADIUS_DECL = re.compile(r"border-radius\s*:\s*([^;}]+)", re.I)
LENGTH = re.compile(r"([0-9]*\.?[0-9]+)\s*(px|rem|em|mm|cm|pt)\b", re.I)
NUMBER_WITH_OPTIONAL_UNIT = re.compile(
    r"(?<![#\w-])([0-9]*\.?[0-9]+)\s*(px|rem|em|mm|cm|pt)?\b", re.I
)
LEFT_RAIL = re.compile(r"border-left(?:-width)?\s*:\s*([^;}]+)", re.I)
FONT = re.compile(r"font-family\s*:\s*([^;}]+)", re.I)
LINE_HEIGHT = re.compile(r"line-height\s*:\s*([^;}]+)", re.I)
PILL_OR_CHIP = re.compile(
    r"(?:class\s*=\s*['\"][^'\"]*\b(?:pill|chip)s?\b|[.#][\w-]*(?:pill|chip)[\w-]*)",
    re.I,
)
GRADIENT = re.compile(r"(?:linear|radial|conic)-gradient\s*\(", re.I)
CSS_BLOCK = re.compile(r"([^{}]+)\{([^{}]*)\}", re.S)
ALLOWED_PILL = re.compile(
    r"james-ui:\s*(?:interactive-filter|removable-selection|status-scan)", re.I
)
STRUCTURAL_DIVIDER = re.compile(r"james-ui:\s*structural-divider", re.I)
META_COPY = re.compile(
    r"AI prepared|Powered by AI|Artifact Progress|ระบบกำลังคิด|เลขาเตรียม|"
    r"ระบบเตรียม|ตอนนี้มีแล้ว|บทนี้จะเติม|เพราะอะไรต้องเติม|production note|"
    r"design rationale",
    re.I,
)
FORBIDDEN_THAI_SYMBOL = re.compile(r"[:—–→/+|]|[\U0001F300-\U0001FAFF]")
QUOTED = re.compile(r"(['\"])(.*?)(?<!\\)\1")
MARKUP_TEXT = re.compile(r">([^<>]+)<")
EXACT_DATA = re.compile(
    r"https?://\S+|"
    r"\b\d{1,2}:\d{2}(?:\s|$)|"
    r"\b\d+(?:\.\d+)?:\d+(?:\.\d+)?\b|"
    r"\d{1,2}/\d{1,2}/\d{2,4}|"
    r"[\u0E00-\u0E7Fa-zA-Z0-9.]+/(?:[\u0E00-\u0E7Fa-zA-Z0-9.]+|(?=[,\s\)]|$))|"
    r"(?:^|\s)\+\s*[\u0E00-\u0E7Fa-zA-Z0-9%]+|"
    r"\+\d{1,4}(?:[\s-]?\d+)+"
)

UNIT_TO_PX = {
    "px": 1.0,
    "rem": 16.0,
    "em": 16.0,
    "mm": 96.0 / 25.4,
    "cm": 96.0 / 2.54,
    "pt": 96.0 / 72.0,
}


def to_px(value: str, unit: str) -> float:
    return float(value) * UNIT_TO_PX[unit.lower()]


def numeric_css_lengths(value: str) -> list[float]:
    lengths: list[float] = []
    for number, unit in NUMBER_WITH_OPTIONAL_UNIT.findall(value):
        lengths.append(float(number) if not unit else to_px(number, unit))
    return lengths


def pseudo_left_rails(text: str) -> list[tuple[int, str, str]]:
    findings: list[tuple[int, str, str]] = []
    for block in CSS_BLOCK.finditer(text):
        selector, body = block.group(1), block.group(2)
        combined = selector + "{" + body
        if "::before" not in selector and "::after" not in selector:
            continue
        if STRUCTURAL_DIVIDER.search(combined):
            continue
        positioned_left = re.search(r"position\s*:\s*absolute", body, re.I) and re.search(
            r"left\s*:\s*0(?:\D|$)", body, re.I
        )
        painted = re.search(r"(?:background(?:-color)?|border-left)\s*:", body, re.I)
        narrow = re.search(
            r"width\s*:\s*(?:[0-9]*\.?[0-9]+)(?:px|rem|em|mm|cm|pt)",
            body,
            re.I,
        )
        if positioned_left and painted and narrow:
            line = text.count("\n", 0, block.start()) + 1
            findings.append((line, "UI001", "positioned pseudo-element left rail"))
    return findings


def iter_files(paths: list[Path], extensions: set[str] = TEXT_EXTENSIONS):
    for root in paths:
        if root.is_file():
            if root.suffix.lower() in extensions:
                yield root
            continue
        for current, dirs, files in os.walk(root):
            dirs[:] = [
                name for name in dirs
                if name not in SKIP_PARTS and not name.startswith(".tmp")
            ]
            base = Path(current)
            for name in files:
                path = base / name
                if path.suffix.lower() in extensions:
                    yield path


def thai_fragments(line: str, suffix: str) -> list[str]:
    if suffix in {".tsx", ".jsx", ".vue", ".svelte", ".html", ".htm"}:
        fragments = [
            match.group(2) for match in QUOTED.finditer(line)
            if not any(token in match.group(2) for token in "<>{}")
        ]
        fragments.extend(
            match.group(1) for match in MARKUP_TEXT.finditer(line)
            if not any(token in match.group(1) for token in "{}")
        )
        return fragments
    return [line]


def valid_font(value: str) -> bool:
    normalized = value.strip().lower()
    if "var(--font-ui)" in normalized:
        return True
    first_family = normalized.split(",", 1)[0].strip(" '\"")
    if first_family == "ibm plex sans thai":
        return True
    return any(
        name in first_family
        for name in ("monospace", "fontawesome", "simple-line-icons")
    )


def lint_file(path: Path) -> list[tuple[int, str, str]]:
    findings: list[tuple[int, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return findings

    suffix = path.suffix.lower()
    if suffix in UI_EXTENSIONS:
        findings.extend(pseudo_left_rails(text))
    for number, line in enumerate(text.splitlines(), 1):
        if suffix in UI_EXTENSIONS:
            rail = LEFT_RAIL.search(line)
            if rail and not STRUCTURAL_DIVIDER.search(line):
                widths = numeric_css_lengths(rail.group(1))
                if widths and max(widths) > 0:
                    findings.append((number, "UI001", "left rail lacks structural-divider exemption"))

            for declaration in RADIUS_DECL.finditer(line):
                raw_radius = declaration.group(1)
                if re.fullmatch(r"\s*50%\s*", raw_radius):
                    continue
                lengths = numeric_css_lengths(raw_radius)
                if lengths and any(abs(length - 6.0) > 0.01 for length in lengths):
                    findings.append((number, "UI002", "rectangle radius must be 6px"))
                    break

            if GRADIENT.search(line):
                findings.append((number, "UI003", "decorative gradient"))
            if PILL_OR_CHIP.search(line) and not ALLOWED_PILL.search(line):
                findings.append((number, "UI004", "pill or chip requires explicit necessity"))

            for match in FONT.finditer(line):
                if not valid_font(match.group(1)):
                    findings.append((number, "UI005", "font is not IBM Plex Sans Thai"))

            for match in LINE_HEIGHT.finditer(line):
                value = match.group(1).strip()
                if re.fullmatch(r"[0-9]*\.?[0-9]+", value):
                    if float(value) > 1.5:
                        findings.append((number, "UI006", "unitless line-height above 1.5"))
                elif LENGTH.search(value):
                    findings.append((number, "UI006", "unit-based line-height bypasses density gate"))

        if META_COPY.search(line):
            findings.append((number, "COPY001", "conversation or production residue"))

        for fragment in thai_fragments(line, suffix):
            prose = EXACT_DATA.sub(" ", fragment)
            if THAI.search(prose) and FORBIDDEN_THAI_SYMBOL.search(prose):
                findings.append((number, "COPY002", "special symbol compresses Thai prose"))
                break

    return findings


def write_report(report: Path, root: Path, results) -> None:
    totals = Counter(code for _, findings in results for _, code, _ in findings)
    lines = [
        "# Make It James Audit",
        "",
        "Audit records debt. It does not claim historical files are repaired.",
        "",
        "| File | Verdict | Violations |",
        "|---|---|---:|",
    ]
    for path, findings in results:
        try:
            label = str(path.relative_to(root))
        except ValueError:
            label = path.name
        lines.append(f"| `{label}` | {'PASS' if not findings else 'FIX'} | {len(findings)} |")
    lines.extend(["", "## Violation totals", ""])
    lines.extend(f"- `{code}` {count}" for code, count in sorted(totals.items()))
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--strict", nargs="+", metavar="PATH")
    mode.add_argument("--audit", metavar="ROOT")
    parser.add_argument("--report", metavar="PATH")
    args = parser.parse_args()

    raw_paths = args.strict if args.strict else [args.audit]
    paths = [Path(item).resolve() for item in raw_paths]
    missing = [path for path in paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"FAIL missing path: {path}")
        return 2

    extensions = UI_EXTENSIONS if args.audit else TEXT_EXTENSIONS
    files = list(iter_files(paths, extensions))
    if not files:
        print("FAIL no supported files found")
        return 2

    all_results = [(path, lint_file(path)) for path in files]
    results = [(path, findings) for path, findings in all_results if findings]

    if args.audit:
        root = paths[0] if paths[0].is_dir() else paths[0].parent
        report = Path(args.report).resolve() if args.report else root / "make-it-james-audit.md"
        write_report(report, root, all_results)
        count = sum(len(findings) for _, findings in all_results)
        print(f"AUDIT files={len(files)} violations={count} report={report}")
        return 0

    for path, findings in results:
        for line, code, message in findings:
            print(f"{path}:{line}: {code} {message}")
    count = sum(len(findings) for _, findings in results)
    print(f"{'FAIL' if count else 'PASS'} files={len(files)} violations={count}")
    return 1 if count else 0


if __name__ == "__main__":
    raise SystemExit(main())
