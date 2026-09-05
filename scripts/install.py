#!/usr/bin/env python3
"""Validated local installation, preserving unrelated paths and host-specific loading.

Claude installed_plugins.json is read per pillar. Codex is reconciled through
its app-server; config.toml text is never treated as proof of a working plugin.
"""
from __future__ import annotations
import argparse
import json
import os
import shutil
import subprocess
import sys
import uuid
from pathlib import Path
from codex_skills import reconcile


def owned(path, root):
    if not path.is_symlink(): return False
    target = path.resolve()
    return any(base in target.parents for base in (root/'plugins', root/'aliases', root/'skills'))


def check_link(src, dst, root):
    if not src.is_dir(): raise RuntimeError(f'Missing source: {src}')
    if dst.is_symlink() and dst.resolve() == src.resolve(): return
    if dst.exists() or dst.is_symlink():
        if not owned(dst, root): raise RuntimeError(f'Collision; preserved existing path: {dst}')


def link(src, dst, root):
    check_link(src, dst, root)
    if dst.is_symlink() and dst.resolve() == src.resolve(): return
    dst.parent.mkdir(parents=True, exist_ok=True)
    # Create first, replace second: failed symlink creation preserves the old link.
    temporary = dst.with_name('.'+dst.name+'.'+uuid.uuid4().hex)
    try:
        temporary.symlink_to(src, target_is_directory=True)
        check_link(src, dst, root)
        temporary.replace(dst)
    finally:
        if temporary.is_symlink(): temporary.unlink()


def claude_pillars(home):
    claude_home = Path(os.environ.get('CLAUDE_CONFIG_DIR', str(home/'.claude')))
    manifest = claude_home/'plugins/installed_plugins.json'
    if not manifest.exists(): return {}
    config = claude_home/'settings.json'
    enabled = json.loads(config.read_text()).get('enabledPlugins', {}) if config.exists() else {}
    plugins = json.loads(manifest.read_text()).get('plugins', {})
    result = {}
    for key, installs in plugins.items():
        if not key.endswith('@james-skills') or enabled.get(key) is False: continue
        for entry in installs:
            path = Path(entry.get('installPath', ''))
            if entry.get('scope') == 'user' and (path/'.claude-plugin/plugin.json').is_file() and (path/'skills').is_dir():
                result[key.split('@')[0]] = path
    return result


def plan(root, home, catalog):
    claude_target = Path(os.environ.get('CLAUDE_CONFIG_DIR', str(home/'.claude')))/'skills'
    targets = [home/'.agents/skills', Path(os.environ.get('CODEX_HOME', str(home/'.codex')))/'skills', claude_target]
    for base in (home/'.cursor', home/'.gemini/config', home/'.gemini/antigravity/custom'):
        if base.is_dir(): targets.append(base/'skills')
    pillars = claude_pillars(home)
    links, removals = {}, set()
    promoted = [s for s in catalog['skills'] if s['status']=='promoted']
    for target in targets:
        gemini = target in (home/'.gemini/config/skills', home/'.gemini/antigravity/custom/skills')
        if gemini and any(s['status'] != 'promoted' for s in catalog['skills']):
            raise RuntimeError('Cannot expose whole Gemini plugin links containing pilot skills')
        if gemini:
            for category in sorted({s['category'] for s in promoted}):
                links[target.parent/'plugins'/category] = root/'plugins'/category
        for item in promoted:
            source = root/'plugins'/item['category']/'skills'/item['name']
            destination = target/item['name']
            if gemini:
                if owned(destination, root): removals.add(destination)
            elif target == claude_target and item['category'] in pillars and (pillars[item['category']]/'skills'/item['name']/'SKILL.md').is_file():
                if owned(destination, root): removals.add(destination)
                elif destination.exists() or destination.is_symlink():
                    raise RuntimeError(f'Collision with native plugin; preserved: {destination}')
            else:
                # Codex canonical paths are deduplicated by its own configuration below.
                links[destination] = source
            for alias in item.get('aliases', []): links[target/alias] = root/'aliases'/alias
        if target.is_dir():
            for existing in target.iterdir():
                if owned(existing, root) and existing not in links: removals.add(existing)
    for dst, src in links.items(): check_link(src, dst, root)
    return links, removals


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    home = Path.home()
    bash = shutil.which('bash')
    if not bash: raise RuntimeError('Bash is required for the full validator (Windows: Git Bash); nothing installed')
    subprocess.run([bash, str(root/'scripts/validate')], check=True)
    catalog = json.loads((root/'catalog.json').read_text())
    links, removals = plan(root, home, catalog)
    if args.check:
        wrong = [str(dst) for dst, src in links.items() if not dst.is_symlink() or dst.resolve()!=src.resolve()]
        if wrong or removals: raise RuntimeError(f'Discovery mismatch: missing/wrong={len(wrong)} stale={len(removals)}')
    else:
        for dst, src in links.items(): link(src, dst, root)
        for dst in sorted(removals): dst.unlink()
        subprocess.run([bash, str(root/'scripts/install-hooks')], check=True)
    if args.check and (root/'.git').exists():
        hooks = subprocess.run(['git', '-C', str(root), 'config', '--get', 'core.hooksPath'], capture_output=True, text=True)
        if hooks.stdout.strip() != '.githooks': raise RuntimeError('Git validation hooks are not installed')
    reconcile(root, home, catalog, repair=not args.check)
    print(f'PASS managed links={len(links)}; filesystem proof only for hosts not runtime-tested')
    return 0


if __name__ == '__main__':
    try: raise SystemExit(main())
    except (RuntimeError, OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f'FAIL {error}', file=sys.stderr)
        raise SystemExit(1)
