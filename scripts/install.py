#!/usr/bin/env python3
"""Cross-platform installer. Mirrors scripts/install (bash) exactly so Windows
gets the same, evidence-based behavior as macOS and Linux — no fabricated CLI
surface, no invented config file.

Claude Code registers plugins through installed_plugins.json. When the three
pillars are installed that way, loose skill links would duplicate every skill,
so this installer writes only aliases into ~/.claude/skills. Aliases have no
plugin counterpart, so they never collide. See scripts/install for the
canonical logic and ai-context/DECISIONS.md DEC-017 for why.
"""
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def print_step(msg):
    print(f"[*] {msg}")


def print_success(msg):
    print(f"[SUCCESS] {msg}")


def print_error(msg):
    print(f"[ERROR] {msg}")


def link(src: Path, dst: Path) -> None:
    """Create a link from dst to src: a symlink on macOS/Linux, a directory
    junction on Windows (needs no administrator rights), falling back to a
    plain copy only if the junction call itself fails."""
    if dst.exists() or dst.is_symlink():
        try:
            if dst.is_symlink() or dst.is_file():
                dst.unlink()
            else:
                shutil.rmtree(dst)
        except OSError:
            pass
    if platform.system() == "Windows":
        try:
            import _winapi

            _winapi.CreateJunction(str(src), str(dst))
            return
        except OSError:
            pass
    try:
        os.symlink(src, dst, target_is_directory=src.is_dir())
    except OSError:
        shutil.copytree(src, dst)


def unlink_if_owned(link_path: Path, repo_dir: Path, prefix: str) -> None:
    """Remove link_path only if it is a symlink/junction this repository
    created, resolving under repo_dir/prefix."""
    if not link_path.is_symlink():
        return
    try:
        target = str(link_path.resolve())
    except OSError:
        return
    if target.startswith(str((repo_dir / prefix).resolve())):
        link_path.unlink()


def main() -> int:
    repo_dir = Path(__file__).resolve().parent.parent
    home = Path.home()

    print_step("Validating repository...")
    if platform.system() != "Windows":
        result = subprocess.run([str(repo_dir / "scripts" / "validate")])
        if result.returncode != 0:
            print_error("Repository validation failed. Aborting installation.")
            return 1
        subprocess.run([str(repo_dir / "scripts" / "install-hooks")], check=False)

    catalog = json.loads((repo_dir / "catalog.json").read_text(encoding="utf-8"))
    promoted = [item for item in catalog.get("skills", []) if item.get("status") == "promoted"]

    claude_manifest = home / ".claude" / "plugins" / "installed_plugins.json"
    claude_uses_plugins = claude_manifest.is_file() and "@james-skills" in claude_manifest.read_text(encoding="utf-8")
    if claude_uses_plugins:
        print_step("Claude Code has the james-skills plugins installed; writing aliases only to ~/.claude/skills")

    targets = [home / ".agents", home / ".codex", home / ".claude"]
    if (home / ".cursor").is_dir():
        targets.append(home / ".cursor")
    if (home / ".gemini" / "config").is_dir():
        targets.append(home / ".gemini" / "config")
    if (home / ".gemini" / "antigravity" / "custom").is_dir():
        targets.append(home / ".gemini" / "antigravity" / "custom")

    plugin_dirs = sorted(p for p in (repo_dir / "plugins").iterdir() if p.is_dir())

    for base_dir in targets:
        skills_target = base_dir / "skills"
        skills_target.mkdir(parents=True, exist_ok=True)

        if ".gemini" in str(base_dir):
            plugins_target = base_dir / "plugins"
            plugins_target.mkdir(parents=True, exist_ok=True)
            for existing in skills_target.iterdir():
                unlink_if_owned(existing, repo_dir, "skills")
                unlink_if_owned(existing, repo_dir, "plugins")
            for plugin_dir in plugin_dirs:
                link(plugin_dir, plugins_target / plugin_dir.name)
        elif base_dir == home / ".claude" and claude_uses_plugins:
            for existing in skills_target.iterdir():
                unlink_if_owned(existing, repo_dir, "plugins")
        else:
            for plugin_dir in plugin_dirs:
                for skill_dir in (plugin_dir / "skills").iterdir():
                    if skill_dir.is_dir():
                        link(skill_dir, skills_target / skill_dir.name)

        for item in promoted:
            for alias in item.get("aliases", []):
                alias_dir = repo_dir / "aliases" / alias
                if not (alias_dir / "SKILL.md").is_file():
                    print_error(f"alias target missing: {alias} -> {item['name']}")
                    return 1
                link(alias_dir, skills_target / alias)

    print_success(f"Installed successfully to all platforms from {repo_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
