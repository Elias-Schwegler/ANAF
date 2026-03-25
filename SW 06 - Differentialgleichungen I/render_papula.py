import fitz
import os

pdf_path = r"C:\Users\elias\Documents\HSLU_MODULE\Semester_2\ANAF\Literatur\Band 2 Papula - Mathematik fuer Ingenieure und Naturwissenschaftler Band 2.pdf"
out_dir = r"C:\Users\elias\Documents\HSLU_MODULE\Semester_2\ANAF\SW 06 - Differentialgleichungen I\papula_images"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# Pages to render (0-indexed, so we subtract 1 from the PDF page numbers)
# Theory: PDF pages 363-385 (Assuming Kap IV starts at 363)
# Exercises: PDF pages 540-545
# Solutions: PDF pages 773-776

ranges_to_render = [
    (362, 385, "theory"),
    (539, 545, "exercise"),
    (772, 776, "solution")
]

for start, end, prefix in ranges_to_render:
    for i in range(start, end + 1):
        if i < len(doc):
            page = doc.load_page(i)
            pix = page.get_pixmap(dpi=200)
            pix.save(os.path.join(out_dir, f"{prefix}_page_{i+1}.png"))
            print(f"Rendered {prefix} page {i+1}")

print("Done rendering Papula pages.")
