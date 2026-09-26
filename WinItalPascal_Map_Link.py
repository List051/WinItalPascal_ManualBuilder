import pymupdf as fitz
import re

# === FILE ===
pdf_finale = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\Manuale_Completo_Map.pdf"
pdf_finale_linked = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\Manuale_Completo_Map_Linked.pdf"

# === NOMI REALI DEI PDF DEI GRAFI ===
snodi = {
    "Core":     "01_Grafo_Core",
    "Database": "01_Grafo_DataBase",
    "Forms":    "01_Grafo_Forms",
    "Logging":  "01_Grafo_Logging",
    "Popup":    "01_Grafo_Popup",
    "Report":   "01_Grafo_Report",
    "Msg":      "01_Grafo_MsgBox"
}

# === COLORI PASTELLO PER OGNI NODO ===
# colori = {
    # "Core":     (0.80, 1.00, 0.80),   # verde pastello
    # "Database": (0.75, 0.95, 1.00),   # azzurro pastello
    # "Forms":    (1.00, 0.90, 0.75),   # arancione pastello
    # "Logging":  (1.00, 0.75, 0.75),   # rosso pastello
    # "Popup":    (0.90, 0.80, 1.00),   # viola pastello
    # "Report":   (1.00, 1.00, 0.75),   # giallo pastello
    # "Msg":      (0.80, 0.90, 1.00)    # blu pastello
# }

# === COORDINATE DEI RETTANGOLI NELLA MAPPA VETTORIALE ===
nodes_rects = {
    "Core":     fitz.Rect( 97.5, 320, 257.5, 380 ),
    "Database": fitz.Rect( 397.5, 320, 557.5, 380 ),
    "Forms":    fitz.Rect( 47.5, 420, 207.5, 480 ),
    "Logging":  fitz.Rect( 347.5, 420, 507.5, 480), # Riposizionare 
    "Popup":    fitz.Rect( 97.5, 520, 257.5, 580 ),
    "Report":   fitz.Rect( 397.5, 520, 557.5, 580 ),
    "Msg":      fitz.Rect( 247.5, 620, 407.5, 680 )
}

PAGE_W = 595
PAGE_H = 842

# === APRE IL PDF UNITO ===
doc = fitz.open(pdf_finale)

# === LA MAPPA È NELLA PAGINA 7 ===
MAP_PAGE = 7
page_mappa = doc[MAP_PAGE]

# === L’INDICE È NELLA PAGINA 10 (quindi resta 10 in PyMuPDF) ===
START_SEARCH = 10

# === TROVA LE PAGINE REALI DEI GRAFI ===
pages_real = {}

for nome, search_text in snodi.items():
    pattern = re.compile(search_text, re.IGNORECASE)

    for page_number in range(START_SEARCH, len(doc)):
        text = doc[page_number].get_text("text")
        if pattern.search(text):
            pages_real[nome] = page_number
            break

print("\nPagine trovate:")
for nome, pag in pages_real.items():
    print(f"{nome}: pagina {pag+1}")

# === 1) LINK + GRAFICA MIGLIORATA SULLA MAPPA ===
for nome, rect in nodes_rects.items():
    if nome not in pages_real:
        continue

    # --- LINK INTERNO ---
    link = {
        "kind": fitz.LINK_GOTO,
        "page": pages_real[nome],
        "rect": rect,
        "from": rect
    }
    page_mappa.insert_link(link)

    # --- RIEMPIMENTO PASTELLO ---
   # page_mappa.draw_rect(rect, fill=colori[nome], width=0)

    # --- BORDO SPESSO ---
    page_mappa.draw_rect(rect, color=(0, 0, 0), width=3)

    # --- GLOW LEGGERO ---
    glow_rect = rect + (-4, -4, 4, 4)
    page_mappa.draw_rect(glow_rect, color=(0.5, 0.5, 1), width=1)

    # --- OMBRA STILE PULSANTE ---
    shadow_rect = rect + (3, 3, 3, 3)
    page_mappa.draw_rect(shadow_rect, color=(0.3, 0.3, 0.3), width=1)

    # --- ICONA VETTORIALE ---
    icon_x = rect.x0 + 10
    icon_y = rect.y0 + 10
    page_mappa.draw_circle((icon_x, icon_y), 6, fill=(1, 1, 1), color=(0, 0, 0), width=1)

    # --- ANNOTAZIONE UNDERLINE (non copre il testo) ---
    annot = page_mappa.add_underline_annot(rect)
    annot.set_colors(stroke=(0, 0, 0))
    annot.update()

# === 2) LINK “TORNA ALLA MAPPA” ===
for nome, pag in pages_real.items():
    page = doc[pag]

    rect = fitz.Rect(PAGE_W - 150, 20, PAGE_W - 20, 50)

    link = {
        "kind": fitz.LINK_GOTO,
        "page": MAP_PAGE,
        "rect": rect,
        "from": rect
    }

    page.insert_link(link)
    page.insert_text((PAGE_W - 145, 35), "Torna alla mappa",
                     fontsize=10, color=(0, 0, 1))

# === 3) BOOKMARK ===
toc = []
for nome, pag in pages_real.items():
    toc.append([1, nome, pag])

doc.set_toc(toc)

# === SALVA ===
doc.save(pdf_finale_linked)
doc.close()

print("\nManuale completo con link interni generato:")
print(pdf_finale_linked)
