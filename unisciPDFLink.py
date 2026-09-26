import pymupdf as fitz

root = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision"   # <-- QUESTA È QUELLA GIUSTA

pdf_segue   = root + r"\SegueManuale.pdf"
pdf_mappa   = root + r"\WinItalPascal_Map.pdf"
pdf_manual  = root + r"\Manuale_Unico_WinItalPascal.pdf"

output_pdf  = root + r"\Manuale_Completo_Map.pdf"

doc_finale = fitz.open()

for pdf in [pdf_segue, pdf_mappa, pdf_manual]:
    print("Apro:", pdf)
    d = fitz.open(pdf)
    doc_finale.insert_pdf(d)

doc_finale.save(output_pdf)
doc_finale.close()

print("Manuale completo generato:", output_pdf)
