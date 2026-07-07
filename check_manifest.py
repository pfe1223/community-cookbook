import sys
import glob
import yaml

with open("manifest.yml", "r") as f:
    manifest = yaml.safe_load(f)

registered = set()
for section in manifest.get("sections", []):
    for path in section.get("recipes", []):
        registered.add(path)

all_recipes = set(glob.glob("recipes/**/*.md", recursive=True))

unregistered = sorted(all_recipes - registered)
missing = sorted(registered - all_recipes)

if unregistered:
    print("Recipe file(s) found but not listed in manifest.yml:")
    for path in unregistered:
        print(f"  - {path}")

if missing:
    print("manifest.yml references file(s) that don't exist:")
    for path in missing:
        print(f"  - {path}")

if unregistered or missing:
    sys.exit(1)

print("All recipe files are registered in manifest.yml.")