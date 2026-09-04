with open("tests/test_skill_handbook.py", "r") as f:
    content = f.read()

content = content.replace(
    'elif item["category"] == "internal":',
    'elif item["name"] == "skill-router" or item.get("type") == "rule":'
)

with open("tests/test_skill_handbook.py", "w") as f:
    f.write(content)
