import yaml

with open("manifest.yml", "r") as f:
    manifest = yaml.safe_load(f)

with open("combined_cookbook.md", "w") as outlet:
    # Write global metadata for Pandoc
    outlet.write(f"---\ntitle: {manifest['title']}\nauthor: {manifest['author']}\ndate: {manifest['date']}\n---\n\n")
    
    # Loop through sections and recipes
    for section in manifest["sections"]:
        outlet.write(f"# {section['name']}\n\n")  # Level 1 Header for Section
        for recipe_path in section["recipes"]:
            with open(recipe_path, "r") as rf:
                # Append recipe content (assuming recipes start with ## headings)
                outlet.write(rf.read())
                outlet.write("\n\n\\pagebreak\n\n") # Force a page break between recipes