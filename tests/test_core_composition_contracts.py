#!/usr/bin/env python3
"""Deterministic guards for core routing and anti-overfit composition."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    router = read("skills/internal/skill-router/SKILL.md")
    never_again = read("skills/core/never-again/SKILL.md")
    cases = read("tests/behavioral-cases.md")
    sum_meet = read("skills/outputs/sum-meet/SKILL.md")
    one_page = read("skills/outputs/one-page-pls/SKILL.md")
    done_for_me = read("skills/core/done-for-me/SKILL.md")
    prove_it = read("skills/core/prove-it/SKILL.md")
    solutions = read("skills/core/give-me-solutions/SKILL.md")
    zoom_out = read("skills/core/zoom-out/SKILL.md")
    final_it = read("skills/outputs/final-it/SKILL.md")
    adhd = read("skills/modes/i-have-adhd/SKILL.md")
    project_standard = read("skills/standards/project-standard/SKILL.md")
    visual_standard = read("skills/standards/make-it-james/references/standard.md")

    for name in (
        "zoom-out",
        "give-me-solutions",
        "baseon",
        "done-for-me",
        "prove-it",
        "never-again",
        "project-standard",
        "sum-meet",
        "one-page-pls",
        "final-it",
        "i-have-adhd",
        "make-it-james",
    ):
        assert f"`{name}`" in router, f"router missing promoted package: {name}"

    assert "Give one primary workflow ownership" in router
    assert "Do not load a whole chain" in router
    assert "never select it as the primary user workflow" in router
    assert "This router produces no user deliverable and never owns the work" in router
    assert "request spanning several responsibilities" in router
    assert "different case with the same mechanism" in never_again
    assert "legitimate counter-case" in never_again
    assert "`final-it`" not in sum_meet
    assert "`final-it`" not in one_page
    assert "owns recipient readiness" in sum_meet and "owns recipient readiness" in one_page
    assert "write-disjoint" in done_for_me
    assert "Do not ask the user to repeat it as a magic confirmation word" in done_for_me
    assert "action-time safety boundary" in done_for_me
    assert "exact target" in done_for_me
    assert "forbidden external effects" in done_for_me + project_standard
    assert "independent verifier" in done_for_me + prove_it
    assert "silently edited old message" in adhd
    assert "never expands authorization" in adhd
    assert "Do not carry it silently into an unrelated conversation" in adhd
    assert "parallel store, table, or identity" in project_standard
    assert "not default to an app dashboard" in visual_standard
    assert "source ledger" in solutions and "another search pass" in solutions
    assert "existing owned assets" in solutions
    assert "Reconcile the latest accepted decision" in zoom_out
    assert "role, a capability, a product, and the whole system" in zoom_out
    assert "identify the target" in prove_it and "semantic correctness" in prove_it
    assert "Never invent or silently resolve" in final_it
    assert "Do not load JamesOS" in router

    for heading in (
        "## Zoom Out",
        "## Prove It",
        "## Never Again",
        "## James Skill Router",
    ):
        assert heading in cases, f"behavioral case missing: {heading}"

    print("PASS full-portfolio routing, composition, and anti-overfit contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
