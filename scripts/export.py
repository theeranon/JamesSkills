#!/usr/bin/env python3
"""Export plain project-local skill files without changing global installation.

File export includes declared helper and pack dependencies. It does not prove discovery or duplicate-free
loading in any host. Verify those separately in the destination project.
"""
from __future__ import annotations
import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_catalog():
    return json.loads((ROOT/'catalog.json').read_text())


def resolve_skill(catalog, name):
    for item in catalog['skills']:
        if item['name'] == name or name in item.get('aliases', []):
            return item
    return None


def export(target, names, catalog=None):
    """Copy each named skill's real directory into target/.agents/skills/<name>/.

    Pack-backed skills include .agents/packs and .agents/research. Meeting/page
    outputs include the sibling font helper at james-software/skills/, matching
    the unchanged instruction's literal relative path. Fonts remain external.

    Returns the list of skill names actually written. Raises RuntimeError on
    any unknown name or missing source so a partial, silently-wrong export
    never lands.
    """
    target = Path(target)
    if target.is_symlink() or not target.is_dir():
        raise RuntimeError(f'Unsafe target directory: {target}')
    catalog = catalog or load_catalog()
    if names is None:
        names = [s['name'] for s in catalog['skills'] if s['status'] == 'promoted']
    destination_root = target/'.agents/skills'
    # Validate the entire request and all destinations before creating any file.
    plan = []
    seen = set()
    for parent in [target / '.agents', destination_root]:
        if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
            raise RuntimeError(f'Unsafe discovery directory: {parent}')
    for name in names:
        item = resolve_skill(catalog, name)
        if item is None:
            raise RuntimeError(f'Unknown skill: {name}')
        if item['status'] != 'promoted':
            raise RuntimeError(f'Skill is not promoted: {name}')
        if item['name'] in seen:
            continue
        seen.add(item['name'])
        source = ROOT/'plugins'/item['category']/'skills'/item['name']
        if source.is_symlink() or any(p.is_symlink() for p in source.rglob('*')):
            raise RuntimeError(f'Unsafe source symlink: {source}')
        if not (source/'SKILL.md').is_file():
            raise RuntimeError(f'Missing source: {source}')
        destination = destination_root/item['name']
        if destination.exists() or destination.is_symlink():
            # Existing files may belong to another agent or the user. Never delete them.
            if destination.is_symlink() or not destination.is_dir():
                raise RuntimeError(f'Existing destination preserved: {destination}')
            def snapshot(folder):
                result = {}
                for file in folder.rglob('*'):
                    if file.is_symlink():
                        raise RuntimeError(f'Existing symlink preserved: {file}')
                    if file.is_file() and '__pycache__' not in file.parts and file.suffix != '.pyc':
                        result[str(file.relative_to(folder))] = file.read_bytes()
                return result
            if snapshot(source) != snapshot(destination):
                raise RuntimeError(f'Existing destination differs; preserved: {destination}')
            plan.append((source, destination, False))
        else:
            plan.append((source, destination, True))
    # Preserve literal relative helper paths without duplicating instruction bodies.
    dependencies = []
    if seen & {'baseon', 'coach-me', 'proactive-dev'}:
        dependencies.append((ROOT/'plugins/james-productivity/packs', target/'.agents/packs'))
        dependencies.append((ROOT/'plugins/james-productivity/research', target/'.agents/research'))
    if seen & {'sum-meet', 'one-page-pls'}:
        dependencies.append((ROOT/'plugins/james-software/skills/make-it-james-ux/scripts',
                             target/'james-software/skills/make-it-james-ux/scripts'))
    for source, destination in dependencies:
        if source.is_symlink() or any(p.is_symlink() for p in source.rglob('*')):
            raise RuntimeError(f'Unsafe dependency symlink: {source}')
        if not source.is_dir():
            raise RuntimeError(f'Missing dependency: {source}')
        for parent in (destination, *destination.parents):
            if parent == target:
                break
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise RuntimeError(f'Unsafe dependency directory: {parent}')
        def dependency_snapshot(folder):
            result = {}
            for file in folder.rglob('*'):
                if file.is_symlink():
                    raise RuntimeError(f'Existing symlink preserved: {file}')
                if file.is_file() and '__pycache__' not in file.parts and file.suffix != '.pyc':
                    result[str(file.relative_to(folder))] = file.read_bytes()
            return result
        if destination.exists() and dependency_snapshot(source) != dependency_snapshot(destination):
            raise RuntimeError(f'Existing dependency differs; preserved: {destination}')
        plan.append((source, destination, not destination.exists()))
    written = []
    created = []
    try:
        for source, destination, needed in plan:
            if needed:
                # Reserve an empty directory exclusively; never replace a concurrent writer.
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.mkdir()
                created.append(destination)
                shutil.copytree(source, destination, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            if destination.parent == destination_root:
                written.append(destination.name)
    except Exception:
        for destination in reversed(created):
            shutil.rmtree(destination)
        raise

    return written


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', help='Path to the project repo to export skills into')
    parser.add_argument('skills', nargs='*', help='Skill names to export (default: every promoted skill)')
    args = parser.parse_args()
    target = Path(args.target).resolve()
    if not target.is_dir():
        raise RuntimeError(f'Not a directory: {target}')
    written = export(target, args.skills or None)
    for name in written:
        print(f'wrote {target}/.agents/skills/{name}/SKILL.md')
    if set(written) & {'baseon', 'coach-me', 'proactive-dev'}:
        print(f'dependencies: {target}/.agents/packs and {target}/.agents/research')
    if set(written) & {'sum-meet', 'one-page-pls'}:
        print(f'font helper: {target}/james-software/skills/make-it-james-ux/scripts (font files not bundled)')
    print(f'PASS exported {len(written)} skill(s) as plain files into {target}/.agents/skills')
    print('Project-local plain copies created; nothing committed. Include dependency directories when committing.')
    print('Host discovery and invocation must be verified separately; global installations are unchanged.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (RuntimeError, OSError) as error:
        print(f'FAIL {error}', file=sys.stderr)
        raise SystemExit(1)
