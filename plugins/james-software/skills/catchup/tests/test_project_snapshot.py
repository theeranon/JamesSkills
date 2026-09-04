#!/usr/bin/env python3
"""Behavior tests for the read-only catchup project snapshot."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "project_snapshot.py"
SPEC = importlib.util.spec_from_file_location("catchup_project_snapshot", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def run(*arguments: str, cwd: Path) -> str:
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    return subprocess.run(
        arguments,
        cwd=cwd,
        env=environment,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def initialize(root: Path) -> None:
    root.mkdir()
    run("git", "init", "-b", "main", cwd=root)
    run("git", "config", "user.email", "test@example.invalid", cwd=root)
    run("git", "config", "user.name", "Catchup Test", cwd=root)


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary)

        root = base / "project"
        initialize(root)
        (root / "PROJECT.md").write_text("# Project\n", encoding="utf-8")
        (root / "STATUS.md").write_text("# Status\n\nCurrent\n", encoding="utf-8")
        run("git", "add", "PROJECT.md", "STATUS.md", cwd=root)
        run("git", "commit", "-m", "baseline", cwd=root)
        baseline = run("git", "rev-parse", "HEAD", cwd=root)

        clean = MODULE.snapshot(root)
        assert clean["git"]["branch"] == "main"
        assert clean["git"]["head_state"] == "branch"
        assert clean["git"]["dirty"] is False
        assert clean["git"]["status_state"] == "ok"
        assert clean["git"]["upstream_state"] == "not_configured"
        assert clean["git"]["remotes"] == []
        assert {item["path"] for item in clean["contract_files"] if item["exists"]} >= {
            "PROJECT.md",
            "STATUS.md",
        }

        (root / "STATUS.md").write_text("# Status\n\nChanged\n", encoding="utf-8")
        run("git", "add", "STATUS.md", cwd=root)
        run("git", "commit", "-m", "change status", cwd=root)
        (root / "PROJECT.md").write_text("# Project\n\nLocal edit\n", encoding="utf-8")
        (root / "LOCAL_NOTES.md").write_text("uncommitted\n", encoding="utf-8")

        changed = MODULE.snapshot(root, baseline)
        assert changed["git"]["dirty"] is True
        assert changed["git"]["changed_count"] == 2
        assert changed["git"]["status"] == [
            {"code": " M", "path": "PROJECT.md"},
            {"code": "??", "path": "LOCAL_NOTES.md"},
        ]
        assert changed["checkpoint"]["valid"] is True
        assert changed["checkpoint"]["ancestry_state"] == "ancestor"
        assert changed["checkpoint"]["delta_state"] == "ok"
        assert changed["checkpoint"]["head_changes"] == [
            {"code": "M", "path": "STATUS.md"}
        ]

        invalid = MODULE.snapshot(root, "not-a-real-checkpoint")
        assert invalid["checkpoint"] == {
            "requested": "not-a-real-checkpoint",
            "valid": False,
        }

        index = root / ".git" / "index"
        original_index = index.read_bytes()
        index.write_bytes(b"invalid index")
        failed_status = MODULE.snapshot(root)
        assert failed_status["git"]["status_state"] == "error"
        assert failed_status["git"]["dirty"] is None
        assert failed_status["git"]["changed_count"] is None
        assert failed_status["git"]["status"] is None
        index.write_bytes(original_index)

        remote_repo = base / "remote.git"
        run("git", "init", "--bare", str(remote_repo), cwd=base)
        run("git", "remote", "add", "origin", str(remote_repo), cwd=root)
        run("git", "push", "-u", "origin", "main", cwd=root)
        configured = MODULE.snapshot(root)
        assert configured["git"]["upstream_state"] == "configured"
        assert configured["git"]["upstream"] == "origin/main"
        assert configured["git"]["ahead"] == configured["git"]["behind"] == 0

        run("git", "checkout", "--detach", cwd=root)
        detached = MODULE.snapshot(root)
        assert detached["git"]["head_state"] == "detached"
        assert detached["git"]["branch"] is None
        assert detached["git"]["upstream_state"] == "not_applicable"
        run("git", "checkout", "main", cwd=root)
        run("git", "update-ref", "-d", "refs/remotes/origin/main", cwd=root)
        gone = MODULE.snapshot(root)
        assert gone["git"]["upstream_state"] == "gone"
        assert gone["git"]["upstream"] is None

        monorepo = base / "monorepo"
        initialize(monorepo)
        workstream = monorepo / "apps" / "widget"
        workstream.mkdir(parents=True)
        (monorepo / "ROOT.md").write_text("root\n", encoding="utf-8")
        (workstream / "PROJECT.md").write_text("# Widget\n", encoding="utf-8")
        (workstream / "STATUS.md").write_text("# Widget status\n", encoding="utf-8")
        (workstream / "old name.txt").write_text("same\n", encoding="utf-8")
        run("git", "add", ".", cwd=monorepo)
        run("git", "commit", "-m", "monorepo baseline", cwd=monorepo)
        monorepo_baseline = run("git", "rev-parse", "HEAD", cwd=monorepo)
        run("git", "config", "status.renames", "false", cwd=monorepo)
        run("git", "config", "diff.renames", "false", cwd=monorepo)
        run("git", "mv", "ROOT.md", "ROOT-renamed.md", cwd=monorepo)
        run(
            "git",
            "mv",
            "apps/widget/old name.txt",
            "apps/widget/new name.txt",
            cwd=monorepo,
        )

        staged_scope = MODULE.snapshot(workstream)
        assert staged_scope["evidence_root"] == str(workstream.resolve())
        assert staged_scope["git"]["scope"] == "apps/widget"
        assert staged_scope["git"]["changed_count"] == 1
        assert staged_scope["git"]["status"] == [
            {
                "code": "R ",
                "path": "apps/widget/new name.txt",
                "original_path": "apps/widget/old name.txt",
            }
        ]
        assert {item["path"] for item in staged_scope["contract_files"] if item["exists"]} >= {
            "PROJECT.md",
            "STATUS.md",
        }

        run("git", "commit", "-m", "rename root and widget files", cwd=monorepo)
        (monorepo / "ROOT-NOTE.md").write_text("outside scope\n", encoding="utf-8")
        (workstream / "LOCAL.md").write_text("inside scope\n", encoding="utf-8")
        scoped = MODULE.snapshot(workstream, monorepo_baseline)
        assert scoped["git"]["status"] == [
            {"code": "??", "path": "apps/widget/LOCAL.md"}
        ]
        assert scoped["checkpoint"]["head_changes"] == [
            {
                "code": "R100",
                "path": "apps/widget/new name.txt",
                "original_path": "apps/widget/old name.txt",
            }
        ]

        plain = base / "plain"
        plain.mkdir()
        (plain / "README.md").write_text("# Plain\n", encoding="utf-8")
        non_git = MODULE.snapshot(plain)
        assert non_git["git"]["is_repository"] is False
        assert non_git["git"]["probe_error"]
        assert non_git["checkpoint"] is None
        non_git_checkpoint = MODULE.snapshot(plain, "HEAD")
        assert non_git_checkpoint["checkpoint"] == {
            "requested": "HEAD",
            "valid": False,
            "reason": "not a Git repository",
        }

    print(
        "PASS catchup clean, dirty, Git-error, upstream, detached, rename, "
        "subproject, checkpoint and non-Git snapshots"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
