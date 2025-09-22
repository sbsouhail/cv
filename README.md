# Souhail SBOUI - CV Repository

This repository contains my Curriculum Vitae in multiple languages in Markdown format and the corresponding PDFs. You can view or download the PDF versions directly:

## Available CVs

- [English CV](cv-en.pdf)
- [French CV](cv-fr.pdf)

---

## About This Repository

- Contains **Markdown files** for each CV: `cv-en.md`, `cv-fr.md`.
- Includes a **Python script (`generate_pdf.py`)** to generate PDFs from these Markdown files.
- Designed for **easy reuse**: you can replace the Markdown files with your own CV content and generate professional PDFs.
- Includes a **GitHub Actions workflow** to automatically generate PDFs and create releases.

---

## How to Generate PDFs from Markdown Locally

### Step 1: Install Python 3.x

If Python is not installed, download it here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Step 2: Install Required Packages

Open a terminal or command prompt and run:

```bash
pip install markdown weasyprint
```

These packages are required to convert Markdown to HTML and then to PDF.

### Step 3: Run the PDF Generation Script

In the terminal, run:

```bash
python generate_pdf.py
```

The script will:

- Automatically read all Markdown files starting with `cv-` (e.g., `cv-en.md`, `cv-fr.md`).
- Generate corresponding PDFs in the same folder (e.g., `cv-en.pdf`, `cv-fr.pdf`).

---

## GitHub Actions Workflow

This repository includes a workflow to **automatically generate PDFs and create releases** whenever CV Markdown files are updated.

**Workflow file:** `.github/workflows/generate_cvs.yml`

```yaml
name: Generate CV PDFs

on:
  push:
    branches:
      - main
    paths:
      - "cv-*.md"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Install system dependencies for WeasyPrint
        run: |
          sudo apt-get update
          sudo apt-get install -y python3-pip libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install markdown weasyprint

      - name: Generate PDFs from Markdown
        run: |
          python generate_pdf.py

      - name: Upload PDFs as artifacts
        uses: actions/upload-artifact@v4
        with:
          name: CV-PDFs
          path: "*.pdf"

      - name: Create GitHub Release
        id: create_release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: "cv-pdfs-${{ github.run_number }}"
          name: "CV PDFs - Run #${{ github.run_number }}"
          body: "Automatically generated CV PDFs from Markdown files"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Upload PDFs to Release
        uses: softprops/action-gh-release@v1
        with:
          files: "*.pdf"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

- **Trigger:** Automatically on push to main branch if any `cv-*.md` changes, or manually via workflow dispatch.
- **Output:** PDFs uploaded as artifacts and attached to a GitHub Release.

---

## Customizing for Your Own CV

1. **Replace Markdown files**: Keep the naming format `cv-<language>.md` (e.g., `cv-de.md` for German).
2. **Edit your CV** in Markdown format. You can follow the structure of `cv-en.md` or `cv-fr.md`.
3. **Push changes** to main branch or run workflow manually to generate updated PDFs automatically.

---

## Notes

- The PDFs are **professionally formatted** with appropriate font sizes, spacing, and headings, ready for job applications.
- Adding more languages is simple: create a new Markdown file following the `cv-<language>.md` pattern and the workflow will generate PDFs automatically.
- This repository is designed for **personal CV management**, but can also serve as a template for others to generate professional PDFs from Markdown.
