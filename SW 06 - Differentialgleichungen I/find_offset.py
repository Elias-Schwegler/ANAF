import fitz

pdf_path = r"C:\Users\elias\Documents\HSLU_MODULE\Semester_2\ANAF\Literatur\Band 2 Papula - Mathematik fuer Ingenieure und Naturwissenschaftler Band 2.pdf"
doc = fitz.open(pdf_path)

with open("output.txt", "w", encoding="utf-8") as f:
    for i in range(350, 370):
        text = doc.load_page(i).get_text()
        lines = text.split('\n')
        lines = [l.strip() for l in lines if l.strip()]
        f.write(f"PDF Page {i} (0-indexed) starts with: {lines[:3]}\n")
        
    toc = doc.get_toc()
    for item in toc:
        lvl, title, page = item
        if "Kapitel IV" in title or "Lösung" in title or "loesung" in title.lower():
            f.write(f"TOC: {title} -> {page}\n")
    
    # check the end to find solutions
    for item in toc[-30:]:
        lvl, title, page = item
        f.write(f"TOC END: {title} -> {page}\n")
