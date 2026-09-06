#!/usr/bin/env python3
"""Static instruction-presence guards, not behavioral proof.

Actual composition outcomes are recorded separately in release receipts.
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

    router = skill("hand-it-off", catalog)
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

    # Canonical discovery belongs to catalog; the router need not duplicate it.
    assert "Candidate Card" in router

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
    assert "ledger" in solutions
    assert "already owned" in solutions
    assert "falsifiable" in research_it and "commercial stake" in research_it
    assert "boundary" in dev_sure and "never transfers" in dev_sure
    assert "accepted project decisions" in zoom_out
    assert "candidate, not a requirement" in zoom_out
    assert "Never invents a fact" in final_it and "stays visibly unresolved" in final_it

    # Coaching and interrogation stay in their lanes.
    assert "question" in coach_me.lower()
    assert "diagnos" in coach_me.lower()
    assert "decision" in grill_me.lower()

    # Every canonical package has a behavioral case tagged with its slug.
    for name in names:
        assert f"`{name}`" in cases, f"behavioral case missing for {name}"

    print(f"PASS static instruction-presence and case-coverage checks ({len(names)} packages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
