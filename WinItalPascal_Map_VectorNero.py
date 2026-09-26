import os
import sys
import pymupdf as fitz

MAPPA = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\WinItalPascal_Map.pdf"

if os.path.exists(MAPPA):
    doc = fitz.open(MAPPA)
    page = doc[0]
    text = page.get_text()

    # se contiene almeno un nome dei nodi → NON rigenerare
    if any(k in text for k in ["Core", "Database", "Forms", "Logging", "Popup", "Report", "Msg"]):
        print("⚠️  Mappa già completa con testo, rigenerazione BLOCCATA.")
        sys.exit(0)


output = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\WinItalPascal_Map.pdf"

doc = fitz.open()
page = doc.new_page(width=595, height=842)
PAGE_W = 595
PAGE_H = 842
# INSERIMENTO TITIOLO E LOGO
# Logo
page.insert_image(
    fitz.Rect(150, 20, 450, 120),
    filename=r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\Logo.png"
)

# Titolo sotto il logo
page.insert_text(
    (PAGE_W/2 - 140, 140),
    "Architettura dei Moduli WinItalPascal",
    fontsize=20,
    color=(0, 0, 0)
)

# --- COORDINATE DEI RETTANGOLI ---
nodes = {
    "Core":     (97.5, 320, 257.5, 380),
    "Database": (397.5, 320, 557.5, 380),
    "Forms":    (47.5, 420, 207.5, 480),
    "Logging":  (347.5, 420, 507.5, 480),
    "Popup":    (97.5, 520, 257.5, 580),
    "Report":   (397.5, 520, 557.5, 580),
    "Msg":      (247.5, 620, 407.5, 680)
}

colori = {
    "Core":     (0.80, 1.00, 0.80),
    "Database": (0.75, 0.95, 1.00),
    "Forms":    (1.00, 0.90, 0.75),
    "Logging":  (1.00, 0.75, 0.75),
    "Popup":    (0.90, 0.80, 1.00),
    "Report":   (1.00, 1.00, 0.75),
    "Msg":      (0.80, 0.90, 1.00)
}

# --- CERCHIO CENTRALE ---
page.draw_circle((300, 250), 60, fill=(0.7, 0.9, 1), color=(0, 0, 0), width=2)
page.insert_text((260, 245), "WinItalPascaL", fontsize=14, color=(0, 0, 0))

# --- NODI ---
for nome, (x0, y0, x1, y1) in nodes.items():
    rect = fitz.Rect(x0, y0, x1, y1)

    # rettangolo pastello
    page.draw_rect(rect, fill=colori[nome], width=2, color=(0, 0, 0))

    # icona
    page.draw_circle((x0 + 12, y0 + 12), 6, fill=(1, 1, 1), color=(0, 0, 0))

    # testo NERO (leggibile)
    page.insert_text((x0 + 40, y0 + 25), nome, fontsize=12, color=(0, 0, 0))

doc.save(output)
doc.close()

print("Mappa vettoriale generata:", output)
