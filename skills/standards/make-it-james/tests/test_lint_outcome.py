#!/usr/bin/env python3
"""Behavior checks for the portable Make It James linter."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
LINTER = SKILL_DIR / "scripts" / "lint_outcome.py"


def run_lint(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(LINTER), "--strict", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        valid = root / "valid.html"
        valid.write_text(
            """<style>
:root { --font-ui: 'IBM Plex Sans Thai', sans-serif; }
body { font-family: var(--font-ui); line-height: 1.4; }
.panel { border-radius: 6px; padding: 12px; }
.avatar { border-radius: 50%; }
</style><p>ประชุมเวลา 14:30 น.</p>
""",
            encoding="utf-8",
        )
        valid_result = run_lint(valid)
        assert valid_result.returncode == 0, valid_result.stdout + valid_result.stderr

        invalid = root / "invalid.html"
        invalid.write_text(
            """<style>
body { font-family: 'Poppins', sans-serif; line-height: 1.68; }
.card { border-left: 4px solid red; border-radius: 12px; background: linear-gradient(red, blue); }
.status-chip { padding: 4px; }
</style><p>ระบบกำลังคิด: พร้อมแล้ว → ส่งต่อ</p>
""",
            encoding="utf-8",
        )
        invalid_result = run_lint(invalid)
        assert invalid_result.returncode == 1, invalid_result.stdout + invalid_result.stderr
        for code in ("UI001", "UI002", "UI003", "UI004", "UI005", "UI006", "COPY001", "COPY002"):
            assert code in invalid_result.stdout, (code, invalid_result.stdout)

        missing_result = run_lint(root / "missing.html")
        assert missing_result.returncode == 2, missing_result.stdout + missing_result.stderr

    print("PASS make-it-james linter behavior")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
