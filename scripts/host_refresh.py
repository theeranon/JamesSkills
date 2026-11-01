#!/usr/bin/env python3
"""Refresh and verify the per-host plugin copies that do not read this repository live.

Claude Code copies every installed plugin into ~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/
at install or update time, even when the marketplace was added from a local path; Codex keeps a Git
snapshot under ~/.codex/.tmp/marketplaces/<marketplace>/. Neither follows a new commit until the host's
own update command runs (LESSON-020). Symlinked hosts (Antigravity, Cursor via the plugin) need nothing.

    host_refresh.py           refresh both hosts through their bundled CLIs
    host_refresh.py --check   fail when a host copy is not at VERSION
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from codex_skills import find_codex  # noqa: E402

MARKET = 'james-skills'


def repo_version():
    return (ROOT / 'VERSION').read_text(encoding='utf-8').strip()


def _version_key(path):
    return [int(part) if part.isdigit() else part for part in path.parts[-5].split('.')]


def find_claude():
    found = shutil.which('claude')
    if found:
        return found
    # Claude Desktop keeps its own Claude Code build outside PATH (README, "Desktop uses a different binary").
    bundle = Path.home() / 'Library/Application Support/Claude/claude-code'
    candidates = sorted(bundle.glob('*/*/claude.app/Contents/MacOS/claude'), key=_version_key)
    for candidate in reversed(candidates):
        if os.access(candidate, os.X_OK):
            return str(candidate)
    return None


def claude_state(home):
    claude_home = Path(os.environ.get('CLAUDE_CONFIG_DIR', str(home / '.claude')))
    manifest = claude_home / 'plugins/installed_plugins.json'
    if not manifest.exists():
        return {}
    plugins = json.loads(manifest.read_text(encoding='utf-8')).get('plugins', {})
    return {
        key.split('@')[0]: sorted({entry.get('version', '?') for entry in installs if entry.get('scope') == 'user'})
        for key, installs in plugins.items()
        if key.endswith('@' + MARKET)
    }


def codex_state(home):
    snapshot = Path(os.environ.get('CODEX_HOME', str(home / '.codex'))) / '.tmp/marketplaces' / MARKET / 'VERSION'
    return snapshot.read_text(encoding='utf-8').strip() if snapshot.exists() else None


def refresh(home):
    state = claude_state(home)
    if state:
        cli = find_claude()
        if not cli:
            raise RuntimeError('Claude Code CLI not found on PATH or in the Desktop bundle; the plugin cache stays stale')
        subprocess.run([cli, 'plugin', 'marketplace', 'update', MARKET], check=True)
        for name in state:
            subprocess.run([cli, 'plugin', 'update', f'{name}@{MARKET}'], check=True)
    else:
        print('SKIP Claude: no james-skills plugin installed for this user')
    if codex_state(home) is not None:
        codex = find_codex()
        if not codex:
            raise RuntimeError('Codex binary not found; the marketplace snapshot stays stale')
        subprocess.run([codex, 'plugin', 'marketplace', 'upgrade', MARKET], check=True)
    else:
        print('SKIP Codex: no james-skills marketplace snapshot for this user')


def check(home):
    want = repo_version()
    problems = []
    claude = claude_state(home)
    for name, versions in claude.items():
        if versions != [want]:
            problems.append(f'Claude cache {name} at {",".join(versions) or "none"}')
    codex = codex_state(home)
    if codex is not None and codex != want:
        problems.append(f'Codex snapshot at {codex}')
    if problems:
        raise RuntimeError(f'repository at {want} but {"; ".join(problems)}. Push, run scripts/update, then restart the app')
    print(f'PASS host copies at {want}: Claude plugins={len(claude)} Codex snapshot={codex or "n/a"}; a running app shows it only after restart')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    home = Path.home()
    if args.check:
        check(home)
    else:
        refresh(home)
        check(home)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print(f'FAIL {error}', file=sys.stderr)
        raise SystemExit(1)
