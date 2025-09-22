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

---

## How to Generate PDFs from Markdown

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

## Customizing for Your Own CV

1. **Replace Markdown files**: Keep the naming format `cv-<language>.md` (e.g., `cv-de.md` for German).
2. **Edit your CV** in Markdown format. You can follow the structure of `cv-en.md` or `cv-fr.md`.
3. **Run the script** again to generate updated PDFs.

---

## Notes

- The PDFs are **professionally formatted** with appropriate font sizes, spacing, and headings, ready for job applications.
- Adding more languages is simple: create a new Markdown file following the `cv-<language>.md` pattern and re-run the script.
- This repository is designed for **personal CV management**, but can also serve as a template for others to generate professional PDFs from Markdown.
