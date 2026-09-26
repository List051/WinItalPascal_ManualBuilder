import fitz  # PyMuPDF

pdf_in = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\WinItalPascal_Map.pdf"
pdf_out = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\WinItalPascal_Map_Text.pdf"

doc = fitz.open(pdf_in)
page = doc[0]

# --- COORDINATE DEI RETTANGOLI ---
nodes = {
    "Core":     (97.5, 320, 257.5, 380),
    "Database": (397.5, 320, 557.5, 380),
    "Forms":    (47.5, 420, 207.5, 480),
    "Logging":  (447.5, 420, 607.5, 480),
    "Popup":    (97.5, 520, 257.5, 580),
    "Report":   (397.5, 520, 557.5, 580),
    "Msg":      (247.5, 620, 407.5, 680)
}

# --- AGGIUNTA TESTO NERO SOPRA OGNI RETTANGOLO ---
for nome, (x0, y0, x1, y1) in nodes.items():
    text_x = x0 + 40
    text_y = y0 + 25

    page.insert_text(
        (text_x, text_y),
        nome,
        fontsize=14,
        fontname="helv",
        color=(0, 0, 0)  # testo nero leggibile
    )

doc.save(pdf_out)
doc.close()

print("Testo aggiunto correttamente:", pdf_out)
