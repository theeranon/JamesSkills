import json
import re

with open("catalog.json", "r") as f:
    catalog = json.load(f)

with open("docs/SKILLS.md", "r") as f:
    content = f.read()

# We can search for `- Canonical package: \`name\`` and replace the next line.
for skill in catalog["skills"]:
    name = skill["name"]
    cat = skill["category"]
    
    # regex: find `- Canonical package: `{name}`\n- Category: `[^`]+`
    pattern = rf"- Canonical package: `{name}`\n- Category: `[^`]+`"
    replacement = rf"- Canonical package: `{name}`\n- Category: `{cat}`"
    content = re.sub(pattern, replacement, content)

with open("docs/SKILLS.md", "w") as f:
    f.write(content)

