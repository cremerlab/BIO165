"""Post-render step for the website build.

- Copies the separately built PDF (_pdf/) into the website output (_book/).
- Publishes the dry lab notebooks for download under _book/drylabs/download/
  (links to drylabs/*.ipynb itself would point to the rendered page).
"""
import shutil
from pathlib import Path

out = Path("_book")

pdf = Path("_pdf/BIO165-lecture-script.pdf")
if pdf.exists():
    shutil.copy2(pdf, out / pdf.name)
else:
    print("Note: no PDF yet; build it with: quarto render --profile pdf --to pdf")

notebooks = sorted(Path("drylabs").glob("*.ipynb"))
if notebooks:
    dl = out / "drylabs" / "download"
    dl.mkdir(parents=True, exist_ok=True)
    for nb in notebooks:
        shutil.copy2(nb, dl / nb.name)
