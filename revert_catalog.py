import json

with open("catalog.json", "r") as f:
    catalog = json.load(f)

for skill in catalog["skills"]:
    if "type" in skill:
        del skill["type"]

with open("catalog.json", "w") as f:
    json.dump(catalog, f, indent=2)
