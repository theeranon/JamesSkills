#!/usr/bin/env python3
"""Generate a thin plugin slash Command per promoted skill.

Claude Code plugins only auto-discover slash commands from a `commands/`
folder (per the official plugin-dev reference); a `skills/` folder alone
never appears in the "/" picker, no matter how correctly it is installed.
Each generated command just loads its skill's real SKILL.md via the
documented ${CLAUDE_PLUGIN_ROOT} variable, so there is exactly one
canonical instruction body per skill — this file never duplicates it.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def generate():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    written = []
    for item in catalog["skills"]:
        if item["status"] != "promoted":
            continue
        name = item["name"]
        category = item["category"]
        skill_md = ROOT / "plugins" / category / "skills" / name / "SKILL.md"
        if not skill_md.is_file():
            raise RuntimeError(f"missing SKILL.md for promoted skill: {skill_md}")
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            raise RuntimeError(f"{skill_md} has no frontmatter")
        end = text.index("---", 3)
        frontmatter = text[3:end]
        description = ""
        for line in frontmatter.splitlines():
            if line.startswith("description:"):
                description = line.split("description:", 1)[1].strip()
                break
        if not description:
            raise RuntimeError(f"{skill_md} has no description field")

        commands_dir = ROOT / "plugins" / category / "commands"
        commands_dir.mkdir(parents=True, exist_ok=True)
        command_path = commands_dir / f"{name}.md"
        command_path.write_text(
            f"---\ndescription: {description}\n---\n\n"
            f"@${{CLAUDE_PLUGIN_ROOT}}/skills/{name}/SKILL.md\n\n"
            f"Follow the instructions above for the rest of this conversation.\n",
            encoding="utf-8",
        )
        written.append(command_path)
    return written


def main():
    written = generate()
    for path in written:
        print(f"wrote {path.relative_to(ROOT)}")
    print(f"PASS generated {len(written)} command(s)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, OSError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        raise SystemExit(1)
