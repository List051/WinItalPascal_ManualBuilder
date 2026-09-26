import os
from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

# === CONFIGURAZIONE ===

# Cartella radice dove si trovano gli Snodi con le sottocartelle PDF
root = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision"

# Cartella dove salvare il PDF finale
output_dir = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision"

# Nome file finale
output_file = os.path.join(output_dir, "Manuale_Unico_WinItalPascal.pdf")

# Cartella per i file temporanei (uso la stessa root)
temp_dir = root

# Percorso del diagramma della libreria
diagramma_path = os.path.join(root, "GrafoLibreria.png")


# === HEADER + FOOTER ===
def header_footer(c, title=""):
    w, h = A4

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w / 2, h - 40, "Manuale WinItalPascal")

    if title:
        c.setFont("Helvetica", 11)
        c.drawCentredString(w / 2, h - 60, f"Sezione: {title}")


def footer(c):
    w, h = A4
    c.setFont("Helvetica", 10)
    c.drawCentredString(w / 2, 30, "© 2026 ItalPascal – WinItalPascal")


# === PAGINA GENERICA ===
def crea_pagina(path, draw_fn, title=""):
    c = canvas.Canvas(path, pagesize=A4)

    header_footer(c, title)
    draw_fn(c)
    footer(c)

    c.showPage()
    c.save()


# === INDICE (SENZA LINK, SOLO TESTO) ===
def crea_indice(pdf_list):
    indice_temp = os.path.join(temp_dir, "indice_temp.pdf")

    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, h - 120, "Indice dei PDF Unificati")

        c.setFont("Helvetica", 14)
        y = h - 170

        for i, nome in enumerate(pdf_list, start=1):
            base = os.path.basename(nome)
            c.drawString(50, y, f"{i}. {base}")
            y -= 22

    crea_pagina(indice_temp, draw, "Indice dei PDF")
    return indice_temp


# === SEPARATORE GRAFICO (SENZA BOOKMARK) ===
def crea_separatore(nome_pdf):
    sep_path = os.path.join(temp_dir, f"sep_{os.path.basename(nome_pdf)}.pdf")

    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(w / 2, h - 150, os.path.basename(nome_pdf))

        c.setLineWidth(2)
        c.line(50, h - 170, w - 50, h - 170)

    crea_pagina(sep_path, draw, f"Documento: {os.path.basename(nome_pdf)}")
    return sep_path


# === STRUTTURA DELLA LIBRERIA (IMMAGINE DINAMICA) ===
def crea_struttura_libreria():
    struttura_temp = os.path.join(temp_dir, "struttura_libreria_temp.pdf")

    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, h - 120, "Struttura della Libreria WinItalPascal")

        try:
            img = ImageReader(diagramma_path)
            img_w, img_h = img.getSize()

            margin_top = 150
            margin_bottom = 50
            max_w = w - 100
            max_h = h - margin_top - margin_bottom

            scale = min(max_w / img_w, max_h / img_h)

            new_w = img_w * scale
            new_h = img_h * scale

            x = (w - new_w) / 2
            y = h - margin_top - new_h

            c.drawImage(diagramma_path, x, y, width=new_w, height=new_h)

        except Exception as e:
            c.setFont("Helvetica", 12)
            c.drawString(50, h - 150, f"[Diagramma non trovato] {e}")

    crea_pagina(struttura_temp, draw, "Struttura della Libreria")
    return struttura_temp


# === RACCOLTA PDF DAGLI SNODI ===
def raccogli_pdf():
    pdf_list = []

    for snodo in os.listdir(root):
        snodo_path = os.path.join(root, snodo)
        pdf_path = os.path.join(snodo_path, "PDF")

        if not os.path.isdir(pdf_path):
            continue

        for f in sorted(os.listdir(pdf_path)):
            if f.lower().endswith(".pdf"):
                pdf_list.append(os.path.join(pdf_path, f))

    return pdf_list


# === PULIZIA FILE TEMPORANEI ===
def pulizia_file_temporanei():
    for f in os.listdir(temp_dir):
        if f.endswith("_temp.pdf") or f.startswith("sep_"):
            try:
                os.remove(os.path.join(temp_dir, f))
            except:
                pass


# === UNIONE PDF ===
def unisci_pdf():
    os.makedirs(output_dir, exist_ok=True)

    pdf_files = raccogli_pdf()

    if not pdf_files:
        print("❌ Nessun PDF trovato nelle cartelle Snodo.")
        return

    merger = PdfMerger()

    # 1. Struttura della libreria
    struttura_pdf = crea_struttura_libreria()
    merger.append(struttura_pdf)

    # 2. Indice (solo testo)
    indice_pdf = crea_indice(pdf_files)
    merger.append(indice_pdf)

    # 3. Separatori + PDF originali
    for pdf in pdf_files:
        sep = crea_separatore(pdf)
        merger.append(sep)
        merger.append(pdf)

    merger.write(output_file)
    merger.close()

    pulizia_file_temporanei()

    print("\n✅ Manuale unico generato:")
    print(output_file)


# === ESECUZIONE ===
if __name__ == "__main__":
    unisci_pdf()
