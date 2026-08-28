#!/usr/bin/env python3
"""Prove failed candidate validation cannot replace the active checkout."""

from __future__ import annotations

import os
import shutil
import stat
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPDATE = ROOT / "scripts" / "update"


def run(*args: str, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    return subprocess.run(
        args,
        cwd=cwd,
        env=environment,
        text=True,
        capture_output=True,
        check=check,
    )


def write_executable(path: Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


def commit(repo: Path, message: str) -> str:
    run("git", "add", ".", cwd=repo)
    run("git", "commit", "-m", message, cwd=repo)
    return run("git", "rev-parse", "HEAD", cwd=repo).stdout.strip()


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary)
        remote = base / "remote.git"
        seed = base / "seed"
        live = base / "live"

        run("git", "init", "--bare", str(remote), cwd=base)
        run("git", "init", "-b", "main", str(seed), cwd=base)
        run("git", "config", "user.email", "test@example.invalid", cwd=seed)
        run("git", "config", "user.name", "JamesSkills Test", cwd=seed)
        (seed / "scripts").mkdir()
        shutil.copy2(UPDATE, seed / "scripts" / "update")
        (seed / "scripts" / "update").chmod((seed / "scripts" / "update").stat().st_mode | stat.S_IXUSR)
        write_executable(
            seed / "scripts" / "validate",
            "#!/usr/bin/env bash\nset -euo pipefail\n"
            "fixture_dir=\"$(cd \"$(dirname \"${BASH_SOURCE[0]}\")/..\" && pwd)\"\n"
            "[[ \"$(cat \"$fixture_dir/VALID\")\" == pass ]]\n",
        )
        write_executable(seed / "scripts" / "install", "#!/usr/bin/env bash\nexit 0\n")
        write_executable(seed / "scripts" / "doctor", "#!/usr/bin/env bash\nexit 0\n")
        (seed / "VALID").write_text("pass\n", encoding="utf-8")
        first = commit(seed, "valid initial")
        run("git", "remote", "add", "origin", str(remote), cwd=seed)
        run("git", "push", "-u", "origin", "main", cwd=seed)
        run("git", "clone", "-b", "main", str(remote), str(live), cwd=base)

        (live / "LOCAL_ONLY").write_text("do not mix\n", encoding="utf-8")
        dirty = run(str(live / "scripts" / "update"), cwd=live, check=False)
        assert dirty.returncode != 0, dirty.stdout + dirty.stderr
        assert "working tree is dirty" in dirty.stdout
        (live / "LOCAL_ONLY").unlink()

        (seed / "VALID").write_text("fail\n", encoding="utf-8")
        commit(seed, "invalid candidate")
        run("git", "push", cwd=seed)

        failed = run(str(live / "scripts" / "update"), cwd=live, check=False)
        assert failed.returncode != 0, failed.stdout + failed.stderr
        assert run("git", "rev-parse", "HEAD", cwd=live).stdout.strip() == first

        (seed / "VALID").write_text("pass\n", encoding="utf-8")
        accepted = commit(seed, "valid candidate")
        run("git", "push", cwd=seed)
        passed = run(str(live / "scripts" / "update"), cwd=live, check=False)
        assert passed.returncode == 0, passed.stdout + passed.stderr
        assert run("git", "rev-parse", "HEAD", cwd=live).stdout.strip() == accepted

    print("PASS update validates candidate before fast-forwarding active checkout")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
