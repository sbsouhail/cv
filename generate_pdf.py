import glob
import markdown
from weasyprint import HTML, CSS

# CSS optimized for readable layout
css = CSS(string="""
@page {
    size: A4;
    margin: 1.3cm;
}
body {
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 11pt;
    line-height: 1.25;
    color: #222;
}
h1 { font-size: 20pt; margin-bottom: 0.3em; }
h2 { font-size: 16pt; margin-top: 0.8em; margin-bottom: 0.3em; color: #111; }
h3 { font-size: 13pt; margin-top: 0.5em; margin-bottom: 0.2em; color: #111; }
p, li { font-size: 11pt; margin-bottom: 0.2em; }
ul, ol { padding-left: 1em; margin-top: 0.3em; margin-bottom: 0.3em; }
strong { font-weight: bold; }
a { color: #1a0dab; text-decoration: none; }
hr { border: 0; border-top: 1px solid #ccc; margin: 0.5em 0; }
""")

# Generate PDFs from all Markdown files starting with "cv-"
md_files = glob.glob("cv-*.md")

if not md_files:
    print("No Markdown CV files found (cv-*.md).")
else:
    for md_file in md_files:
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                md_content = f.read()

            html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
            html = f"<html><head><meta charset='utf-8'></head><body>{html_content}</body></html>"

            pdf_file = md_file.replace(".md", ".pdf")
            HTML(string=html).write_pdf(pdf_file, stylesheets=[css])
            print(f"✅ Generated {pdf_file}")
        except Exception as e:
            print(f"❌ Failed to generate PDF for {md_file}: {e}")
