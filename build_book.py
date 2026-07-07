import yaml

with open("manifest.yml", "r") as f:
    manifest = yaml.safe_load(f)

with open("combined_cookbook.md", "w") as outlet:
    # --- Front matter / YAML metadata block ---
    outlet.write("---\n")
    outlet.write(f"title: {manifest['title']}\n")
    outlet.write(f"author: {manifest['author']}\n")
    outlet.write(f"date: {manifest['date']}\n")

    # Optional cover page styling, passed straight through to Eisvogel.
    # All keys are optional -- only emitted if present in manifest.yml.
    cover = manifest.get("cover", {})
    if cover:
        outlet.write("titlepage: true\n")
        for key in ("titlepage-color", "titlepage-text-color",
                    "titlepage-rule-color", "titlepage-rule-height",
                    "titlepage-background", "logo", "logo-width"):
            if key in cover:
                outlet.write(f"{key}: {cover[key]}\n")

    outlet.write("---\n\n")

    # --- Foreword (optional) ---
    # Points to a standalone markdown file with front-of-book text.
    if manifest.get("foreword"):
        with open(manifest["foreword"], "r") as ff:
            outlet.write("# Foreword {-}\n\n")
            outlet.write(ff.read())
            outlet.write("\n\n\\pagebreak\n\n")

    # --- Sections and recipes ---
    for section in manifest["sections"]:
        outlet.write(f"# {section['name']}\n\n")  # Level 1 Header for Section

        # Optional section intro text, written directly under the section heading.
        if section.get("intro"):
            outlet.write(f"{section['intro']}\n\n")

        for recipe_path in section["recipes"]:
            with open(recipe_path, "r") as rf:
                # Append recipe content (assuming recipes start with ## headings)
                outlet.write(rf.read())
                outlet.write("\n\n\\pagebreak\n\n")  # Force a page break between recipes