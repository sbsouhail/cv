import glob
import markdown
from weasyprint import HTML, CSS

# CSS for professional PDF formatting
css = CSS(string="""
@page { size: A4; margin: 2cm; }
body { font-family: 'Arial', sans-serif; font-size: 12pt; line-height: 1.3; color: #222; }
h1 { font-size: 24pt; margin-bottom: 0.3em; }
h2 { font-size: 18pt; margin-top: 1em; margin-bottom: 0.3em; color: #1a1a1a; }
h3 { font-size: 14pt; margin-top: 0.8em; margin-bottom: 0.2em; color: #1a1a1a; }
p, li { font-size: 12pt; margin-bottom: 0.2em; }
ul { padding-left: 1em; margin-bottom: 0.5em; }
strong { font-weight: bold; }
""")

# Find all Markdown CV files starting with "cv-"
md_files = glob.glob("cv-*.md")

if not md_files:
    print("No Markdown CV files found (cv-*.md).")
else:
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        html = f"<html><head><meta charset='utf-8'></head><body>{html_content}</body></html>"

        pdf_file = md_file.replace(".md", ".pdf")
        HTML(string=html).write_pdf(pdf_file, stylesheets=[css])
        print(f"Generated {pdf_file}")
