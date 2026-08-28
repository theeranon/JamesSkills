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
        assert (root / "PROJECT.md").read_text(encoding="utf-8").startswith(
            "# Example Project"
        )
        assert not (root / "ARCHITECTURE.md").exists()

        original = (root / "PROJECT.md").read_text(encoding="utf-8")
        assert MODULE.bootstrap(root, "Changed Name", "software") == 0
        assert (root / "PROJECT.md").read_text(encoding="utf-8") == original
        assert (root / "ARCHITECTURE.md").is_file()
        assert (root / "DATA_MODEL.md").is_file()
        assert MODULE.check(root) == 0

        project = root / "PROJECT.md"
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
        status = root / "STATUS.md"
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

        (root / "STATUS.md").unlink()
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        assert MODULE.bootstrap(root, "Placeholder Test", "minimal") == 0
        project = root / "PROJECT.md"
        project.write_text(
            project.read_text(encoding="utf-8") + "\n{{UNRESOLVED}}\n",
            encoding="utf-8",
        )
        with redirect_stdout(io.StringIO()):
            assert MODULE.check(root) == 1

    print("PASS project-standard bootstrap, preserve, profile and failure gates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
