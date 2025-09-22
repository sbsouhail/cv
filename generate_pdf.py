import glob
import markdown
from weasyprint import HTML, CSS

# CSS for professional PDF formatting
css = CSS(string="""
@page { size: A4; margin: 1.5cm; }  /* Reduced margins */
body { font-family: 'Arial', sans-serif; font-size: 11pt; line-height: 1.2; color: #222; }  /* Smaller font and tighter spacing */
h1 { font-size: 20pt; margin-bottom: 0.2em; }  /* Smaller headings */
h2 { font-size: 16pt; margin-top: 0.8em; margin-bottom: 0.2em; color: #1a1a1a; }
h3 { font-size: 13pt; margin-top: 0.5em; margin-bottom: 0.1em; color: #1a1a1a; }
p, li { font-size: 11pt; margin-bottom: 0.1em; }
ul { padding-left: 0.8em; margin-bottom: 0.3em; }
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
