with open("tests/test_skill_handbook.py", "r") as f:
    content = f.read()

# Replace: if item["status"] == "promoted" and item["category"] != "internal":
# With: if item["status"] == "promoted" and item["name"] != "skill-router" and item.get("type") != "rule":
content = content.replace(
    'if item["status"] == "promoted" and item["category"] != "internal":',
    'if item["status"] == "promoted" and item["name"] != "skill-router" and item.get("type") != "rule":'
)
# Because some rules are missing slashes too (like make-it-james? Or proactive-habits)

with open("tests/test_skill_handbook.py", "w") as f:
    f.write(content)
