# BIO 165/265 — Quantitative Approaches in Modern Biology

Lecture script and teaching material for BIO 165/265 (Stanford University),
published as a website with a downloadable PDF at
<https://cremerlab.github.io/BIO165>.

Built with [Quarto](https://quarto.org) (book format).

## Structure

| Path | Content |
|------|---------|
| `_quarto.yml` | Book configuration: chapter order, site settings, HTML/PDF options |
| `index.qmd` | Landing page |
| `chapters/` | Lecture script, one `.qmd` file per chapter, named by week (`3b-linear-regression.qmd` = week 3, 2nd chapter) |
| `figs/` | Figures used in the script |
| `drylabs/` | Dry labs: student versions of the weekly notebooks (**never solutions**) and the overview page |
| `images/` | Website images (favicon, logos) |
| `references.bib` | Bibliography |
| `styles.scss` | Website styling |
| `_quarto-web.yml`, `_quarto-pdf.yml` | Settings for the website and PDF builds |
| `scripts/post-render.py` | Copies the PDF and downloadable notebooks into the website |

## Editing

1. Install [Quarto](https://quarto.org/docs/get-started/) (and the Quarto
   extension for VS Code).
2. Run `quarto preview` in this folder: a live preview opens in the browser
   and refreshes on every save.
3. To add a chapter, create a `.qmd` file in `chapters/` and add it to the
   `chapters:` list in `_quarto.yml` under the right week.

The script was converted from the original Overleaf (LaTeX) project; the
`.qmd` files in `chapters/` are now the source to edit.

Two builds:

```bash
quarto render --profile pdf --to pdf   # PDF of the lecture script -> _pdf/
quarto render                          # website incl. dry labs -> _book/ (copies the PDF in)
```

The PDF contains only the lecture script; the dry labs are website-only.

## Adding a dry lab

1. Copy the **student version** of the notebook into `drylabs/` and clear all
   outputs (outputs can contain solution plots).
2. Add it to the chapter list in `_quarto-web.yml` and add a card for it in
   `drylabs/index.qmd`.

## Publishing

Pushing to `main` triggers a GitHub Action that renders the book and deploys
it to the `gh-pages` branch. In the repository settings, GitHub Pages must be
set to deploy from the `gh-pages` branch.

## Private material

This repository is public. Solutions stay in the instructors' private
repository; locally, `solutions/` and `private/` folders are git-ignored.
