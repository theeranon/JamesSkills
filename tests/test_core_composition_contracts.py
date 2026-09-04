#!/usr/bin/env python3
"""Behavioral guards for routing, composition, and anti-overfit across the portfolio.

Asserts behavior that the structural schema cannot: that the router covers the whole
roster without owning work, that output skills do not delegate to the general one, and
that specific safety rules survive rewrites.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def skill(name: str, catalog: dict) -> str:
    entry = next(item for item in catalog["skills"] if item["name"] == name)
    return read(f"plugins/{entry['category']}/skills/{name}/SKILL.md")


def main() -> int:
    catalog = json.loads(read("catalog.json"))
    names = [item["name"] for item in catalog["skills"]]

    router = skill("skill-router", catalog)
    never_again = skill("never-again", catalog)
    sum_meet = skill("sum-meet", catalog)
    one_page = skill("one-page-pls", catalog)
    done_for_me = skill("done-for-me", catalog)
    research_it = skill("research-it", catalog)
    dev_sure = skill("dev-are-you-sure", catalog)
    solutions = skill("give-me-solutions", catalog)
    zoom_out = skill("zoom-out", catalog)
    final_it = skill("final-it", catalog)
    adhd = skill("i-have-adhd", catalog)
    proactive_habits = skill("proactive-habits", catalog)
    proactive_dev = skill("proactive-dev", catalog)
    coach_me = skill("coach-me", catalog)
    grill_me = skill("grill-me", catalog)
    project_standard = skill("project-standard", catalog)
    visual_standard = read("plugins/james-software/skills/make-it-james-ux/references/standard.md")
    cases = read("tests/behavioral-cases.md")

    # The router must name every canonical package, derived from the catalog rather
    # than a hardcoded list, so a new skill cannot be added without routing coverage.
    for name in names:
        assert f"`{name}`" in router, f"router missing canonical package: {name}"

    # The router routes and never owns.
    assert "Never select it as the primary workflow" in router
    assert "Produces no user deliverable" in router
    assert "Candidate Card" in router and "approves the exact name and scope" in router
    assert "never let it become the primary workflow" in router

    # Anti-overfit: a durable correction needs same-mechanism and counter-case evidence.
    assert "a different case with the same mechanism" in never_again
    assert "a legitimate counter-case" in never_again
    assert "ai-context/LESSONS.md" in never_again

    # Specific output skills never hand their artifact to the general one.
    assert "-> `sum-meet`" in final_it and "-> `one-page-pls`" in final_it

    # Delegation and external-authority safety.
    assert "write-disjoint" in done_for_me
    assert "confirmation word" in done_for_me
    assert "exact target" in done_for_me
    assert "forbidden external effects" in done_for_me + project_standard + proactive_dev
    assert "independent" in done_for_me + dev_sure

    # Mode safety: presentation and decision posture never widen authority.
    assert "never widens authorization" in adhd.lower().replace("never widens authorisation", "never widens authorization")
    assert "does not carry into an unrelated conversation" in adhd
    assert "irreversible" in proactive_habits
    assert "batch" in proactive_habits.lower()

    # Data and architecture guards.
    assert "parallel store, table, or identity path" in project_standard
    assert "parallel store or duplicated identity path" in proactive_dev
    assert "not default to an app dashboard" in visual_standard

    # Evidence discipline.
    assert "ledger" in solutions and "no longer changes the ranking" in solutions
    assert "already owned" in solutions
    assert "falsifiable" in research_it and "commercial stake" in research_it
    assert "boundary" in dev_sure and "never transfers" in dev_sure
    assert "Reconcile the latest accepted decision" in zoom_out
    assert "candidate, never a requirement" in zoom_out
    assert "Never invents a fact" in final_it and "stays visibly unresolved" in final_it

    # Coaching and interrogation stay in their lanes.
    assert "questions only" in coach_me.lower()
    assert "never gives advice" in coach_me.lower()
    assert "recap" in grill_me.lower() and "complete, correct, on target" in grill_me

    # Every canonical package has a behavioral case tagged with its slug.
    for name in names:
        assert f"`{name}`" in cases, f"behavioral case missing for {name}"

    print(f"PASS full-portfolio routing, composition, and anti-overfit contracts ({len(names)} packages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
