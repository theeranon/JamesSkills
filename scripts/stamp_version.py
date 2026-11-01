#!/usr/bin/env python3
"""Stamp metadata.version in every canonical SKILL.md from VERSION, so a loaded skill says which
release it came from without reading the plugin manifest. `--check` fails when any stamp differs.
The stamp is metadata, not the description: descriptions are a 320-character trigger budget."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r'^(metadata:\n  kind: [^\n]+\n)(  version: [^\n]+\n)?', re.M)


def main(check):
    want = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    stale = []
    for path in sorted(ROOT.glob('plugins/*/skills/*/SKILL.md')):
        text = path.read_text(encoding='utf-8')
        match = BLOCK.search(text)
        if not match:
            raise SystemExit(f'FAIL {path}: no metadata.kind block to stamp')
        new = text[:match.start()] + match.group(1) + f'  version: {want}\n' + text[match.end():]
        if new != text:
            stale.append(path.relative_to(ROOT))
            if not check:
                path.write_text(new, encoding='utf-8')
    if check and stale:
        raise SystemExit(f'FAIL metadata.version differs from VERSION {want} in {len(stale)} skill(s); run scripts/stamp_version.py')
    print(f'{"PASS" if check else "STAMPED"} metadata.version {want} ({len(stale)} {"stale" if check else "changed"})')


if __name__ == '__main__':
    main('--check' in sys.argv[1:])
