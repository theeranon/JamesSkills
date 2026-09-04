import os
import shutil
import json
import re

print("Starting migration to 3-Pillar Plugin Architecture...")

# 1. Create Plugin Directories
plugins = {
    "james-core": {
        "skills": [
            "plugins/james-core/skills/are-you-sure",
            "plugins/james-core/skills/done-for-me",
            "plugins/james-core/skills/prove-it",
            "plugins/james-core/skills/is-that-the-best-you-can-do",
            "plugins/james-core/skills/never-again",
            "plugins/james-core/skills/skill-router"
        ],
        "rules": [
            "plugins/james-core/rules/proactive-habits",
            "plugins/james-core/rules/make-it-james",
            "plugins/james-core/rules/i-have-adhd"
        ]
    },
    "james-productivity": {
        "skills": [
            "plugins/james-productivity/skills/sum-meet",
            "plugins/james-productivity/skills/one-page-pls",
            "plugins/james-productivity/skills/give-me-solutions",
            "plugins/james-productivity/skills/baseon",
            "plugins/james-productivity/skills/grill-me",
            "plugins/james-productivity/skills/zoom-out",
            "plugins/james-productivity/skills/final-it",
            "plugins/james-productivity/skills/coach-me"
        ],
        "rules": []
    },
    "james-software": {
        "skills": [
            "plugins/james-software/skills/proactive-dev",
            "plugins/james-software/skills/project-standard",
            "plugins/james-core/rules/make-it-james-ux",
            "plugins/james-software/skills/catchup"
        ],
        "rules": []
    }
}

os.makedirs("plugins", exist_ok=True)

# Update catalog.json
with open("catalog.json", "r") as f:
    catalog = json.load(f)

new_skills = []
for skill in catalog["skills"]:
    name = skill["name"]
    # Find which plugin this belongs to
    found = False
    for plugin_name, plugin_data in plugins.items():
        for s in plugin_data["skills"]:
            if s.endswith("/" + name):
                skill["category"] = plugin_name
                new_skills.append(skill)
                found = True
                break
        for r in plugin_data["rules"]:
            if r.endswith("/" + name):
                # It's a rule now, not a skill!
                # Wait, we might want to keep it in catalog for documentation, but mark it as a rule
                skill["category"] = plugin_name
                skill["type"] = "rule"
                new_skills.append(skill)
                found = True
                break
    if not found:
        print(f"Warning: {name} not found in mapping!")
        new_skills.append(skill)

catalog["skills"] = new_skills

with open("catalog.json", "w") as f:
    json.dump(catalog, f, indent=2)

# Move Files
for plugin_name, data in plugins.items():
    os.makedirs(f"plugins/{plugin_name}", exist_ok=True)
    os.makedirs(f"plugins/{plugin_name}/skills", exist_ok=True)
    os.makedirs(f"plugins/{plugin_name}/rules", exist_ok=True)
    
    # plugin.json
    with open(f"plugins/{plugin_name}/plugin.json", "w") as f:
        json.dump({"name": plugin_name}, f, indent=2)
    
    # Move Skills
    for s_path in data["skills"]:
        skill_name = os.path.basename(s_path)
        dest = f"plugins/{plugin_name}/skills/{skill_name}"
        if os.path.exists(s_path):
            shutil.move(s_path, dest)
    
    # Move Rules
    for r_path in data["rules"]:
        rule_name = os.path.basename(r_path)
        dest = f"plugins/{plugin_name}/rules/{rule_name}"
        if os.path.exists(r_path):
            # We move the entire directory, but maybe we should extract SKILL.md to AGENTS.md?
            # Actually, let's keep the directory structure for references/scripts, 
            # and just rename SKILL.md to AGENTS.md inside it. But Antigravity reads rules/*.md directly.
            # So let's rename SKILL.md to rule_name.md and put it in rules/.
            # If there are scripts, we move the directory to plugins/plugin_name/rules/rule_name/
            # Wait, Antigravity reads recursively? Yes, if we specify or just place them.
            # Let's just move the directory into rules/ and rename SKILL.md to {rule_name}.md
            shutil.move(r_path, dest)
            old_md = os.path.join(dest, "SKILL.md")
            new_md = os.path.join(dest, f"{rule_name}.md")
            if os.path.exists(old_md):
                os.rename(old_md, new_md)

# Clean up empty skills dirs
for d in ["skills/core", "skills/internal", "skills/modes", "skills/outputs", "skills/standards", "skills"]:
    if os.path.exists(d) and not os.listdir(d):
        os.rmdir(d)

print("Files moved.")
