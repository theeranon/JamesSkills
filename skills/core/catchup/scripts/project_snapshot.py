#!/usr/bin/env python3
"""Create a read-only, machine-readable project and Git snapshot for catchup."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CONTRACT_PATHS = (
    "PROJECT.md",
    "STATUS.md",
    "AGENTS.md",
    "docs/DECISIONS.md",
    "ARCHITECTURE.md",
    "DATA_MODEL.md",
    "README.md",
)
RENAME_CODES = {"R", "C"}


def git_environment() -> dict[str, str]:
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    return environment


def run_git(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *arguments],
        env=git_environment(),
        text=True,
        capture_output=True,
        check=False,
    )


def git_text(root: Path, *arguments: str) -> str | None:
    result = run_git(root, *arguments)
    if result.returncode != 0:
        return None
    value = result.stdout.rstrip("\r\n")
    return value or None


def command_error(result: subprocess.CompletedProcess[str]) -> str:
    return (
        result.stderr.strip()
        or result.stdout.strip()
        or f"git exited with status {result.returncode}"
    )


def parse_status_z(payload: str) -> list[dict[str, str]]:
    tokens = payload.split("\0")
    if tokens and tokens[-1] == "":
        tokens.pop()
    records: list[dict[str, str]] = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if len(token) < 4 or token[2] != " ":
            raise ValueError(f"unexpected Git status record: {token!r}")
        code = token[:2]
        record = {"code": code, "path": token[3:]}
        index += 1
        if any(character in RENAME_CODES for character in code):
            if index >= len(tokens):
                raise ValueError("Git rename status is missing its original path")
            record["original_path"] = tokens[index]
            index += 1
        records.append(record)
    return records


def parse_name_status_z(payload: str) -> list[dict[str, str]]:
    tokens = payload.split("\0")
    if tokens and tokens[-1] == "":
        tokens.pop()
    records: list[dict[str, str]] = []
    index = 0
    while index < len(tokens):
        code = tokens[index]
        index += 1
        if index >= len(tokens):
            raise ValueError(f"Git diff record {code!r} is missing a path")
        first_path = tokens[index]
        index += 1
        if code[:1] in RENAME_CODES:
            if index >= len(tokens):
                raise ValueError(f"Git rename diff {code!r} is missing its new path")
            new_path = tokens[index]
            index += 1
            records.append(
                {"code": code, "path": new_path, "original_path": first_path}
            )
        else:
            records.append({"code": code, "path": first_path})
    return records


def file_record(root: Path, relative: str) -> dict[str, Any]:
    path = root / relative
    if not path.is_file():
        return {"path": relative, "exists": False}
    stat = path.stat()
    return {
        "path": relative,
        "exists": True,
        "bytes": stat.st_size,
        "modified_utc": datetime.fromtimestamp(
            stat.st_mtime, tz=timezone.utc
        ).isoformat(),
    }


def checkpoint_record(
    root: Path, checkpoint: str | None, scope: str
) -> dict[str, Any] | None:
    if checkpoint is None:
        return None
    if checkpoint.startswith("-"):
        return {"requested": checkpoint, "valid": False}
    resolved = git_text(root, "rev-parse", "--verify", f"{checkpoint}^{{commit}}")
    if resolved is None:
        return {"requested": checkpoint, "valid": False}

    ancestor = run_git(root, "merge-base", "--is-ancestor", resolved, "HEAD")
    if ancestor.returncode == 0:
        ancestry_state = "ancestor"
        is_ancestor: bool | None = True
        ancestry_error = None
    elif ancestor.returncode == 1:
        ancestry_state = "not_ancestor"
        is_ancestor = False
        ancestry_error = None
    else:
        ancestry_state = "error"
        is_ancestor = None
        ancestry_error = command_error(ancestor)

    changed = run_git(
        root,
        "-c",
        "core.quotepath=false",
        "-c",
        "diff.renames=true",
        "diff",
        "--name-status",
        "-z",
        f"{resolved}..HEAD",
        "--",
        scope,
    )
    if changed.returncode == 0:
        delta_state = "ok"
        delta_error = None
        head_changes = parse_name_status_z(changed.stdout)
    else:
        delta_state = "error"
        delta_error = command_error(changed)
        head_changes = None

    return {
        "requested": checkpoint,
        "valid": True,
        "commit": resolved,
        "ancestry_state": ancestry_state,
        "is_ancestor_of_head": is_ancestor,
        "ancestry_error": ancestry_error,
        "delta_state": delta_state,
        "delta_error": delta_error,
        "head_changes": head_changes,
    }


def branch_record(root: Path) -> dict[str, Any]:
    head = git_text(root, "rev-parse", "--verify", "HEAD")
    symbolic = run_git(root, "symbolic-ref", "--quiet", "--short", "HEAD")
    if symbolic.returncode == 0:
        branch = symbolic.stdout.rstrip("\r\n") or None
        head_state = "branch" if head else "unborn"
        head_error = None
    elif symbolic.returncode == 1 and head:
        branch = None
        head_state = "detached"
        head_error = None
    else:
        branch = None
        head_state = "error"
        head_error = command_error(symbolic)
    return {
        "head": head,
        "head_state": head_state,
        "head_error": head_error,
        "branch": branch,
    }


def upstream_record(root: Path, branch: str | None) -> dict[str, Any]:
    if branch is None:
        return {
            "upstream": None,
            "upstream_state": "not_applicable",
            "upstream_error": None,
        }

    remote_config = run_git(root, "config", "--get", f"branch.{branch}.remote")
    merge_config = run_git(root, "config", "--get", f"branch.{branch}.merge")
    config_errors = [
        command_error(result)
        for result in (remote_config, merge_config)
        if result.returncode not in (0, 1)
    ]
    if config_errors:
        return {
            "upstream": None,
            "upstream_state": "error",
            "upstream_error": "; ".join(config_errors),
        }
    if remote_config.returncode == 1 or merge_config.returncode == 1:
        return {
            "upstream": None,
            "upstream_state": "not_configured",
            "upstream_error": None,
        }

    upstream = run_git(
        root, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"
    )
    if upstream.returncode == 0:
        return {
            "upstream": upstream.stdout.rstrip("\r\n") or None,
            "upstream_state": "configured",
            "upstream_error": None,
        }
    return {
        "upstream": None,
        "upstream_state": "gone",
        "upstream_error": command_error(upstream),
    }


def snapshot(root: Path, checkpoint: str | None = None) -> dict[str, Any]:
    requested = root.expanduser().resolve()
    if not requested.is_dir():
        raise NotADirectoryError(f"project root is not a directory: {requested}")

    probe = run_git(requested, "rev-parse", "--show-toplevel")
    top_level_text = probe.stdout.rstrip("\r\n") if probe.returncode == 0 else None
    git_root = Path(top_level_text).resolve() if top_level_text else None
    result: dict[str, Any] = {
        "requested_root": str(requested),
        "evidence_root": str(requested),
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "contract_files": [file_record(requested, path) for path in CONTRACT_PATHS],
        "git": {
            "is_repository": git_root is not None,
            "probe_error": None if git_root is not None else command_error(probe),
        },
    }

    if git_root is None:
        result["checkpoint"] = (
            None
            if checkpoint is None
            else {
                "requested": checkpoint,
                "valid": False,
                "reason": "not a Git repository",
            }
        )
        return result

    scope_path = requested.relative_to(git_root)
    scope = scope_path.as_posix() if scope_path.parts else "."
    status_result = run_git(
        git_root,
        "-c",
        "core.quotepath=false",
        "-c",
        "status.renames=true",
        "status",
        "--porcelain=v1",
        "-z",
        "--untracked-files=normal",
        "--",
        scope,
    )
    if status_result.returncode == 0:
        status_state = "ok"
        status_error = None
        status = parse_status_z(status_result.stdout)
        dirty: bool | None = bool(status)
        changed_count: int | None = len(status)
    else:
        status_state = "error"
        status_error = command_error(status_result)
        status = None
        dirty = None
        changed_count = None

    branch = branch_record(git_root)
    upstream = upstream_record(git_root, branch["branch"])
    remote_result = run_git(git_root, "remote")
    if remote_result.returncode == 0:
        remote_state = "ok"
        remote_error = None
        remote_text = remote_result.stdout.rstrip("\r\n")
        remotes: list[str] | None = remote_text.splitlines() if remote_text else []
    else:
        remote_state = "error"
        remote_error = command_error(remote_result)
        remotes = None

    ahead: int | None = None
    behind: int | None = None
    divergence_state = "not_applicable"
    divergence_error = None
    if upstream["upstream_state"] == "configured":
        divergence = run_git(
            git_root,
            "rev-list",
            "--left-right",
            "--count",
            "HEAD...@{upstream}",
        )
        if divergence.returncode == 0:
            left, right = divergence.stdout.split()
            ahead, behind = int(left), int(right)
            divergence_state = "ok"
        else:
            divergence_state = "error"
            divergence_error = command_error(divergence)

    result["git"] = {
        "is_repository": True,
        "probe_error": None,
        "top_level": str(git_root),
        "scope": scope,
        **branch,
        **upstream,
        "remote_state": remote_state,
        "remote_error": remote_error,
        "remotes": remotes,
        "divergence_state": divergence_state,
        "divergence_error": divergence_error,
        "ahead": ahead,
        "behind": behind,
        "status_state": status_state,
        "status_error": status_error,
        "untracked_mode": "normal",
        "dirty": dirty,
        "changed_count": changed_count,
        "status": status,
    }
    result["checkpoint"] = checkpoint_record(git_root, checkpoint, scope)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Existing project or workstream directory")
    parser.add_argument(
        "--checkpoint",
        help="Optional Git revision used to describe committed changes to HEAD",
    )
    parser.add_argument(
        "--compact", action="store_true", help="Emit compact JSON instead of indented JSON"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        payload = snapshot(args.root, args.checkpoint)
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        return 2
    print(
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=None if args.compact else 2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
