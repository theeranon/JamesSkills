with open("tests/test_skill_handbook.py", "r") as f:
    content = f.read()

content = content.replace(
    'elif item["name"] == "skill-router" or item.get("type") == "rule":',
    'elif item["name"] == "skill-router":'
)

# And if it is a rule, just pass? Or wait, rules still have a slash in the handbook?
# Yes, they have a slash because they used to be skills. 
# So let them fall into the "else" (which expects a slash).

with open("tests/test_skill_handbook.py", "w") as f:
    f.write(content)
