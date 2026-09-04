#!/usr/bin/env python3
"""Regression tests for project-standard bootstrap and structural checks."""

from __future__ import annotations

import importlib.util
import io
import tempfile
from contextlib import redirect_stdout
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "project_standard.py"
SPEC = importlib.util.spec_from_file_location("project_standard", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main() -> int:
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        assert MODULE.bootstrap(root, "Example Project", "minimal") == 0
        assert MODULE.check(root) == 0
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root, ready=True) == 1
        assert (root / "ai-context" / "PROJECT.md").read_text(encoding="utf-8").startswith(
            "# Example Project"
        )
        assert not (root / "ai-context" / "ARCHITECTURE.md").exists()
        assert (root / "AGENTS.md").is_file()
        assert not (root / "PROJECT.md").exists()

        original = (root / "ai-context" / "PROJECT.md").read_text(encoding="utf-8")
        assert MODULE.bootstrap(root, "Changed Name", "software") == 0
        assert (root / "ai-context" / "PROJECT.md").read_text(encoding="utf-8") == original
        assert (root / "ai-context" / "ARCHITECTURE.md").is_file()
        assert (root / "ai-context" / "DATA_MODEL.md").is_file()
        assert MODULE.check(root) == 0

        project = root / "ai-context" / "PROJECT.md"
        project.write_text(
            project.read_text(encoding="utf-8")
            .replace("- Primary user: Not confirmed", "- Primary user: Operations lead")
            .replace("- Problem: Not confirmed", "- Problem: Current state is not traceable")
            .replace(
                "- Successful outcome: Not confirmed",
                "- Successful outcome: Fresh agents recover verified state",
            )
            .replace(
                "| REQ-001 | Not confirmed | Not confirmed | Owner accepts the first requirement | Named owner decision |",
                "| REQ-001 | Fresh agents recover current state | No chat-only facts | Agent identifies state and proof | Independent handoff test |",
            ),
            encoding="utf-8",
        )
        status = root / "ai-context" / "STATUS.md"
        status.write_text(
            status.read_text(encoding="utf-8")
            .replace("## Current outcome\n\nNot confirmed", "## Current outcome\n\nContract ready for handoff")
            .replace(
                "| REQ-001 | Need decision | Named owner acceptance missing |",
                "| REQ-001 | Verified | Independent handoff test passed |",
            ),
            encoding="utf-8",
        )
        assert MODULE.check(root, ready=True) == 0

        # SRS.html: Open mode requires it to stay in sync once it exists.
        assert MODULE.render_srs_command(root) == 0
        srs = (root / "ai-context" / "SRS.html").read_text(encoding="utf-8")
        assert "Example Project" in srs
        assert "<table>" in srs
        assert MODULE.check(root) == 0

        project.write_text(
            project.read_text(encoding="utf-8").replace(
                "Fresh agents recover current state", "Fresh agents recover current state, updated"
            ),
            encoding="utf-8",
        )
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1  # SRS.html now stale
        assert MODULE.render_srs_command(root) == 0
        assert MODULE.check(root) == 0  # regenerating clears the staleness failure

        # Spec lock: Locked freezes PROJECT.md/DATA_MODEL.md; any further edit fails check.
        with redirect_stdout(io.StringIO()) as lock_out:
            assert MODULE.lock_spec_command(root) == 0
        lock_line = [line for line in lock_out.getvalue().splitlines() if line.startswith("Spec lock:")][0]
        status.write_text(
            status.read_text(encoding="utf-8").replace("Spec lock: Open", lock_line),
            encoding="utf-8",
        )
        assert MODULE.check(root) == 0  # locked immediately after lock-spec: hash matches

        project.write_text(
            project.read_text(encoding="utf-8") + "\n<!-- drift -->\n",
            encoding="utf-8",
        )
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1  # PROJECT.md drifted from the locked hash
        with redirect_stdout(io.StringIO()) as relock_out:
            assert MODULE.lock_spec_command(root) == 0
        relock_line = [line for line in relock_out.getvalue().splitlines() if line.startswith("Spec lock:")][0]
        status.write_text(
            status.read_text(encoding="utf-8").replace(lock_line, relock_line),
            encoding="utf-8",
        )
        assert MODULE.check(root) == 0  # re-locking at the new content clears the drift failure

        status.write_text(
            status.read_text(encoding="utf-8").replace(relock_line, "Spec lock: Open"),
            encoding="utf-8",
        )
        assert MODULE.render_srs_command(root) == 0
        assert MODULE.check(root) == 0  # back to Open with a freshly regenerated SRS.html

        status.write_text(
            status.read_text(encoding="utf-8").replace("REQ-001", "REQ-999"),
            encoding="utf-8",
        )
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1
        status.write_text(
            status.read_text(encoding="utf-8").replace("REQ-999", "REQ-001"),
            encoding="utf-8",
        )

        (root / "CLAUDE.md").write_text(
            "# Claude instructions\n\nUse Next.js and Vercel.\n", encoding="utf-8"
        )
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1
        (root / "CLAUDE.md").write_text(
            "# Claude adapter\n\nRead and follow `AGENTS.md`.\n", encoding="utf-8"
        )
        assert MODULE.check(root) == 0

        (root / "ai-context" / "STATUS.md").unlink()
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        assert MODULE.bootstrap(root, "Placeholder Test", "minimal") == 0
        project = root / "ai-context" / "PROJECT.md"
        project.write_text(
            project.read_text(encoding="utf-8") + "\n{{UNRESOLVED}}\n",
            encoding="utf-8",
        )
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1

    with tempfile.TemporaryDirectory() as temp:
        # Regression: a real-world heading carrying a trailing annotation (a date stamp, a
        # parenthetical note) must still be found — a bare `.*` under DOTALL previously
        # swallowed the rest of the document instead of just the heading's own line.
        root = Path(temp)
        (root / "ai-context").mkdir(parents=True)
        (root / "ai-context" / "PROJECT.md").write_text(
            "# T\n\n"
            "## Outcome\n\n- x\n\n"
            "## Requirements (updated 2026-09-01)\n\n"
            "| ID | Requirement |\n|---|---|\n| REQ-001 | Ship it |\n\n"
            "## System boundaries\n\nz\n",
            encoding="utf-8",
        )
        html, missing = MODULE.render_srs(root)
        assert "<table>" in html and "Ship it" in html
        assert missing == ["PROJECT.md: ## Scope", "PROJECT.md: ## Non-functional requirements"]
        assert "not found in <code>PROJECT.md</code>" in html
        # A heading that matches exactly must not be reported missing.
        assert "## Outcome" not in "\n".join(missing)
        assert "## System boundaries" not in "\n".join(missing)

    with tempfile.TemporaryDirectory() as temp:
        # migrate case 1: nothing exists yet.
        root = Path(temp)
        with redirect_stdout(io.StringIO()):
            assert MODULE.migrate(root, None, "minimal") == 1  # no --name to bootstrap with
        assert MODULE.migrate(root, "Fresh Project", "minimal") == 0
        assert (root / "ai-context" / "PROJECT.md").is_file()
        assert MODULE.migrate(root, None, "minimal") == 0  # already migrated: no-op, no crash

    with tempfile.TemporaryDirectory() as temp:
        # migrate case 2: a genuine v1 project (root-level files, canonical headings) moves
        # automatically and every known cross-reference is repointed.
        root = Path(temp)
        assert MODULE.bootstrap(root, "Old V1 Project", "software") == 0
        ac = root / "ai-context"
        (root / "docs").mkdir()
        for name in ("PROJECT.md", "STATUS.md", "ARCHITECTURE.md", "DATA_MODEL.md"):
            (ac / name).rename(root / name)
        (ac / "DECISIONS.md").rename(root / "docs" / "DECISIONS.md")
        ac.rmdir()
        agents = root / "AGENTS.md"
        agents.write_text(
            agents.read_text(encoding="utf-8")
            .replace("ai-context/PROJECT.md", "PROJECT.md")
            .replace("ai-context/STATUS.md", "STATUS.md")
            .replace("ai-context/DECISIONS.md", "docs/DECISIONS.md")
            .replace("ai-context/ARCHITECTURE.md", "ARCHITECTURE.md")
            .replace("ai-context/DATA_MODEL.md", "DATA_MODEL.md"),
            encoding="utf-8",
        )

        assert MODULE.migrate(root, None, "minimal") == 0
        for name in ("PROJECT.md", "STATUS.md", "ARCHITECTURE.md", "DATA_MODEL.md", "DECISIONS.md"):
            assert (root / "ai-context" / name).is_file()
            assert not (root / name).exists()
        assert not (root / "docs").exists()
        assert "ai-context/PROJECT.md" in agents.read_text(encoding="utf-8")
        assert "Spec lock: Open" in (root / "ai-context" / "STATUS.md").read_text(encoding="utf-8")
        assert MODULE.check(root) == 0

    with tempfile.TemporaryDirectory() as temp:
        # migrate case 3: a pre-existing custom document (foreign headings, e.g. a real annotated
        # heading found during the workspace audit) is never moved — only reported.
        root = Path(temp)
        (root / "PROJECT.md").write_text(
            "# Foreign\n\n## Outcome\n\n- x\n\n## Scope\n\n- y\n\n"
            "## Requirements (อัปเดตตาม PHP Architecture Pivot 2026-09-01)\n\n"
            "| ID | Requirement |\n|---|---|\n| REQ-001 | z |\n\n## System boundaries\n\n- w\n",
            encoding="utf-8",
        )
        with redirect_stdout(io.StringIO()) as out:
            assert MODULE.migrate(root, None, "minimal") == 2
        report = out.getvalue()
        assert "HOLD PROJECT.md" in report
        assert "missing heading: ## Authority" in report
        assert (root / "PROJECT.md").is_file()  # left in place, not moved
        assert not (root / "ai-context").exists()

    with tempfile.TemporaryDirectory() as temp:
        # migrate case 4 (mixed): one file matches the template and moves; a sibling with a
        # foreign heading is held back. Partial migration must not silently drop the held file.
        root = Path(temp)
        assert MODULE.bootstrap(root, "Mixed Project", "minimal") == 0
        (root / "ai-context" / "PROJECT.md").rename(root / "PROJECT.md")
        (root / "ai-context" / "STATUS.md").rename(root / "STATUS.md")
        (root / "docs").mkdir()
        (root / "ai-context" / "DECISIONS.md").rename(root / "docs" / "DECISIONS.md")
        (root / "ai-context").rmdir()
        status = root / "STATUS.md"
        status.write_text(
            status.read_text(encoding="utf-8").replace("## Blockers", "## Blocked Items"),
            encoding="utf-8",
        )
        with redirect_stdout(io.StringIO()) as out:
            assert MODULE.migrate(root, None, "minimal") == 2
        report = out.getvalue()
        assert "MIGRATE PROJECT.md" in report
        assert "HOLD STATUS.md" in report
        assert (root / "ai-context" / "PROJECT.md").is_file()
        assert (root / "ai-context" / "DECISIONS.md").is_file()
        assert (root / "STATUS.md").is_file()  # held, not silently dropped

    print("PASS project-standard bootstrap, preserve, profile and failure gates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
