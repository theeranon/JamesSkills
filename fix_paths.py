import os
import json

with open("catalog.json", "r") as f:
    catalog = json.load(f)

# Build a mapping from old skills/path -> plugins/path
mapping = {}

plugins = {
    "james-core": {
        "skills": ["skills/core/are-you-sure", "skills/core/done-for-me", "skills/core/prove-it", "skills/core/is-that-the-best-you-can-do", "skills/core/never-again", "skills/internal/skill-router"],
        "rules": ["skills/modes/proactive-habits", "skills/standards/make-it-james", "skills/modes/i-have-adhd"]
    },
    "james-productivity": {
        "skills": ["outputs/sum-meet", "outputs/one-page-pls", "core/give-me-solutions", "core/baseon", "core/grill-me", "core/zoom-out", "outputs/final-it", "modes/coach-me"],
        "rules": []
    },
    "james-software": {
        "skills": ["standards/proactive-dev", "standards/project-standard", "standards/make-it-james-ux", "core/catchup"],
        "rules": []
    }
}

# Actually, the easiest way to map is to look at catalog.json
for skill in catalog["skills"]:
    name = skill["name"]
    category = skill["category"]
    type_ = skill.get("type", "skill")
    
    # But wait, we need to map OLD paths to NEW paths.
    # The easiest is to just walk the old files in the repo and replace them.
    pass

# A simpler way: we know the new paths. We can just search for `skills/.*/name/` and replace with `plugins/category/type/name/`
import re

def update_file(path):
    with open(path, "r") as f:
        content = f.read()
    
    orig_content = content
    for skill in catalog["skills"]:
        name = skill["name"]
        cat = skill["category"] # james-core etc
        t = skill.get("type", "skill")
        folder = "rules" if t == "rule" else "skills"
        
        # We need to replace things like `skills/core/done-for-me/` with `plugins/james-core/skills/done-for-me/`
        # Using regex to catch `skills/[^/]+/{name}`
        pattern = r"skills/[^/]+/" + re.escape(name)
        replacement = f"plugins/{cat}/{folder}/{name}"
        
        content = re.sub(pattern, replacement, content)
        
        # Fix `SKILL.md` to `name.md` if it's a rule
        if t == "rule":
            pattern_rule = f"plugins/{cat}/rules/{name}/SKILL.md"
            replacement_rule = f"plugins/{cat}/rules/{name}/{name}.md"
            content = content.replace(pattern_rule, replacement_rule)
            
    if content != orig_content:
        with open(path, "w") as f:
            f.write(content)

# Update all tests and scripts
for root, dirs, files in os.walk("."):
    if ".git" in root: continue
    for file in files:
        if file.endswith((".py", ".js", ".cjs", ".sh", ".md", ".json")) and file != "catalog.json" and file != "fix_paths.py":
            update_file(os.path.join(root, file))

print("Paths updated.")
