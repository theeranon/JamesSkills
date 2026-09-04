#!/usr/bin/env python3
"""Prevent the repository that ships project-standard from exempting itself."""

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "plugins/james-software/skills/project-standard/scripts/project_standard.py"


def main() -> int:
    validation = (ROOT / "scripts/validate").read_text(encoding="utf-8")
    result = subprocess.run(
        ["python3", str(CHECKER), "check", str(ROOT), "--ready"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "project-standard/scripts/project_standard.py" in validation
    assert 'check "$repo_dir" --ready' in validation
    assert not (ROOT / "ARCHITECTURE.md").exists(), (
        "do not manufacture architecture documentation for a source-only skill library"
    )
    assert not (ROOT / "DATA_MODEL.md").exists(), (
        "do not manufacture a data model for a repository with no persistent store"
    )
    print("PASS JamesSkills self-applies the minimal project-standard ready gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
