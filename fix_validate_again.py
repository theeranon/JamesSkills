with open("scripts/validate", "r") as f:
    content = f.read()

# Replace: 
# type_ = item.get("type", "skill")
# folder = "rules" if type_ == "rule" else "skills"
# filename = item["name"] + ".md" if type_ == "rule" else "SKILL.md"
# path = root / "plugins" / item["category"] / folder / item["name"] / filename
# With:
# path = root / "plugins" / item["category"] / "skills" / item["name"] / "SKILL.md"

import re
content = re.sub(
    r'type_ = item\.get\("type", "skill"\)\n    folder = "rules" if type_ == "rule" else "skills"\n    filename = item\["name"\] \+ "\.md" if type_ == "rule" else "SKILL\.md"\n    path = root / "plugins" / item\["category"\] / folder / item\["name"\] / filename',
    'path = root / "plugins" / item["category"] / "skills" / item["name"] / "SKILL.md"',
    content
)

with open("scripts/validate", "w") as f:
    f.write(content)
