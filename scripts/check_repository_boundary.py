#!/usr/bin/env python3
"""Scan tracked and non-ignored candidate text for portability and secret risks."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


MACHINE_HOME = re.compile(re.escape("/" + "Users" + "/"))
CREDENTIAL_ASSIGNMENT = re.compile(
    r"(?i)\b(?:api[_-]?key|access[_-]?token|password)\s*[:=]\s*['\"]?[^\s'\"`]+"
)
PRIVATE_KEY_MARKER = re.compile("-----BEGIN " + "PRIVATE KEY-----")
CHECKS = (
    ("machine-specific home path", MACHINE_HOME),
    ("possible credential assignment", CREDENTIAL_ASSIGNMENT),
    ("private key material", PRIVATE_KEY_MARKER),
)


def candidate_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "-z",
        ],
        capture_output=True,
        check=True,
    )
    return [root / item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def scan_text(text: str) -> list[tuple[str, int]]:
    findings: list[tuple[str, int]] = []
    for label, pattern in CHECKS:
        for match in pattern.finditer(text):
            findings.append((label, text.count("\n", 0, match.start()) + 1))
    return findings


def scan_repository(root: Path) -> list[tuple[Path, str, int]]:
    findings: list[tuple[Path, str, int]] = []
    for path in candidate_paths(root):
        if not path.is_file() or path.is_symlink():
            continue
        payload = path.read_bytes()
        if b"\0" in payload:
            continue
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for label, line in scan_text(text):
            findings.append((path.relative_to(root), label, line))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path.cwd())
    return parser.parse_args()


def main() -> int:
    root = parse_args().root.expanduser().resolve()
    findings = scan_repository(root)
    if findings:
        for path, label, line in findings:
            print(f"FAIL {path}:{line} {label}")
        return 1
    print("PASS repository text boundary scan")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
