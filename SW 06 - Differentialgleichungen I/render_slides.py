import fitz
import os

pdf_file = 'ana-f-sw-06-folien.pdf'
out_dir = 'slides_images'
os.makedirs(out_dir, exist_ok=True)

if os.path.exists(pdf_file):
    doc = fitz.open(pdf_file)
    prefix = pdf_file.replace('.pdf', '')
    for i in range(len(doc)):
        page = doc.load_page(i)
        # Higher DPI for better text/math readability
        pix = page.get_pixmap(dpi=200)
        pix.save(os.path.join(out_dir, f"{prefix}_page_{i+1}.png"))
    print(f"Exported {len(doc)} pages for {pdf_file}")
else:
    print(f"File not found: {pdf_file}")
