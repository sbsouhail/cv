import glob, markdown, os
from weasyprint import HTML, CSS

# Optimized CSS for compact yet readable layout
css = CSS(string="""
@page {
    size: A4;
    margin: 1.2cm;
}
body {
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 10.5pt;
    line-height: 1.15;
    color: #222;
}
h1 { font-size: 18pt; margin-bottom: 0.2em; }
h2 { font-size: 15pt; margin-top: 0.5em; margin-bottom: 0.1em; color: #111; }
h3 { font-size: 12.5pt; margin-top: 0.3em; margin-bottom: 0.05em; color: #111; }
p, li { font-size: 10.5pt; margin-bottom: 0.1em; }
ul, ol { padding-left: 1em; margin-top: 0.1em; margin-bottom: 0.2em; }
strong { font-weight: bold; }
a { color: #1a0dab; text-decoration: none; }
hr { border: 0; border-top: 1px solid #ccc; margin: 0.5em 0; }

/* 2-column layout for contact, languages, soft skills */
.columns {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.2em;
}
.column {
    width: 48%;
}
""")

# Find all Markdown CV files starting with "cv-"
md_files = glob.glob("cv-*.md")

if not md_files:
    print("No Markdown CV files found (cv-*.md).")
else:
    for md_file in md_files:
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                md_content = f.read()
            
            # Add title for PDF metadata
            html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
            html = f"""
            <html>
                <head>
                    <meta charset='utf-8'>
                    <title>{md_file.replace('.md', '')} - CV</title>
                </head>
                <body>{html_content}</body>
            </html>
            """

            pdf_file = md_file.replace(".md", ".pdf")
            HTML(string=html).write_pdf(pdf_file, stylesheets=[css])
            print(f"✅ Generated {pdf_file}")
        except Exception as e:
            print(f"❌ Failed to generate PDF for {md_file}: {e}")
