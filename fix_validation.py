import re

# Fix scripts/validate
with open("scripts/validate", "r") as f:
    content = f.read()

# Replace root / "skills" / item["category"] / item["name"] / "SKILL.md"
content = content.replace(
    'path = root / "skills" / item["category"] / item["name"] / "SKILL.md"',
    'type_ = item.get("type", "skill")\n    folder = "rules" if type_ == "rule" else "skills"\n    filename = item["name"] + ".md" if type_ == "rule" else "SKILL.md"\n    path = root / "plugins" / item["category"] / folder / item["name"] / filename'
)
content = content.replace(
    'disk_paths = {path.resolve() for path in (root / "skills").glob("*/*/SKILL.md")}',
    'disk_paths = {path.resolve() for path in list((root / "plugins").glob("*/skills/*/SKILL.md")) + list((root / "plugins").glob("*/rules/*/*.md"))}'
)
content = content.replace(
    'skill_count = len(list((root / "skills").glob("*/*/SKILL.md")))',
    'skill_count = len(disk_paths)'
)

with open("scripts/validate", "w") as f:
    f.write(content)

# Fix tests/test_skill_handbook.py
with open("tests/test_skill_handbook.py", "r") as f:
    content = f.read()
content = content.replace('f"../skills/{item[\'category\']}/{name}/SKILL.md"', 'f"../plugins/{item[\'category\']}/skills/{name}/SKILL.md" if item.get("type") != "rule" else f"../plugins/{item[\'category\']}/rules/{name}/{name}.md"')
with open("tests/test_skill_handbook.py", "w") as f:
    f.write(content)
