# The Open Source Community Cookbook

A crowd-sourced cookbook built entirely from pull requests. Every recipe contributed here gets automatically compiled into a single, nicely formatted PDF cookbook via GitHub Actions.

## How It Works

1. Contributors add recipes as Markdown files under `recipes/<category>/`.
2. Each recipe is registered in `manifest.yml`, which controls the sections and order of the final book.
3. On every push to `main`, a GitHub Action:
   - Runs `build_book.py` to merge all recipes (in manifest order) into `combined_cookbook.md`
   - Uses Pandoc to convert that file into `cookbook.pdf`
   - Uploads the PDF as a build artifact

## Repository Structure

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── recipe-template.md   # Template to copy for new recipe submissions
│   └── workflows/
│       └── build-pdf.yml        # Builds the PDF on every push to main
├── recipes/
│   ├── appetizers/
│   ├── bread/
│   └── mains/
├── templates/
│   └── eisvogel.tex             # LaTeX/Pandoc template assets
├── build_book.py                # Merges recipes into combined_cookbook.md
├── manifest.yml                 # Defines cookbook title, sections, and recipe order
├── combined_cookbook.md         # Auto-generated — do not edit by hand
└── cookbook.pdf                 # Auto-generated — do not edit by hand
```

## Contributing a Recipe

We'd love to have your recipe! Contributions are made via pull request — please don't push directly to `main`.

1. **Fork the repo** and create a new branch for your recipe.
2. **Copy the recipe template** from [`.github/ISSUE_TEMPLATE/recipe-template.md`](.github/ISSUE_TEMPLATE/recipe-template.md) into a new file.
3. **Add your recipe file** under `recipes/<category>/`, using a short, kebab-case filename (e.g. `recipes/desserts/lemon-tart.md`). If your category doesn't exist yet, create a new folder for it.
4. **Fill out the template** with your recipe's name, prep/cook time, servings, description, ingredients, and instructions.
5. **Register your recipe in `manifest.yml`** under the appropriate section (create a new section if needed) so it gets picked up by the build.
6. **Open a pull request** against `main`. Once merged, the Action will automatically rebuild `cookbook.pdf` with your recipe included.

### Recipe Template

```markdown
## [Recipe Name]

**Prep Time:** X mins | **Cook Time:** X mins | **Servings:** X
**Contributor:** @github_username

---

### Description
A brief, 1–2 sentence story or description of the dish. Why is it special?

### Ingredients
- [ ] Quantity Unit **Ingredient Name** (e.g., `- [ ] 2 tbsp **Olive Oil**`)
- [ ] Quantity Unit **Ingredient Name**

### Instructions
1. **First Action Keyword:** Describe the first step clearly.
2. **Second Action Keyword:** Describe the second step.

> 💡 **Chef's Tip:** Insert any special variations, ingredient substitutions, or pairing suggestions here!
```

## Building Locally

If you want to preview the PDF before opening a PR:

```bash
pip install pyyaml
python build_book.py
pandoc combined_cookbook.md -o cookbook.pdf \
  --toc \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V mainfont="DejaVu Serif" \
  -V sansfont="DejaVu Sans"
```

Requires [Pandoc](https://pandoc.org/) and a LaTeX distribution (e.g. TeX Live) with `xelatex`.

## License

This repository uses two licenses:

- **Code** (`build_book.py`, GitHub Actions workflows, configuration files) is licensed under the [MIT License](LICENSE).
- **Recipe content** (everything under `recipes/`) is licensed under [CC BY-SA 4.0](LICENSE-CONTENT) — you're free to share and adapt any recipe, even commercially, as long as you credit the original contributor and share adaptations under the same license.