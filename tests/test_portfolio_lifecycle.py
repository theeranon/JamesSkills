#!/usr/bin/env python3
"""Regression checks for candidate approval and promotion boundaries."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    maintainer = read("AGENTS.md")
    router = read("skills/internal/james-skill-router/SKILL.md")
    never_again = read("skills/core/never-again/SKILL.md")

    assert "Authorization to build the library is not approval" in maintainer
    assert "Candidate Card" in maintainer and "Candidate Card" in router
    assert "cross-case evidence" in maintainer
    assert "legitimate counter-case" in maintainer + router + never_again
    assert "outside global installs" in router
    assert "Approval to repair the failure is not approval" in never_again

    print("PASS candidate approval, anti-overfit, and promotion lifecycle contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
