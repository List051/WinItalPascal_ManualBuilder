import os
from datetime import datetime
from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# === CONFIGURAZIONE ===
base_dir = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision"
output_dir = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision"

output_file = os.path.join(output_dir, "SegueManuale.pdf")

diagramma_path = os.path.join(base_dir, "GrafoLibreria.png")

copertina_temp = os.path.join(base_dir, "copertina_temp.pdf")
info_temp = os.path.join(base_dir, "info_temp.pdf")
changelog_temp = os.path.join(base_dir, "changelog_temp.pdf")
struttura_temp = os.path.join(base_dir, "struttura_temp.pdf")
nuget_temp = os.path.join(base_dir, "nuget_temp.pdf")
indice_temp = os.path.join(base_dir, "indice_temp.pdf")
licenza_temp = os.path.join(base_dir, "licenza_temp.pdf")


# === HEADER + FOOTER ===
def header_footer(c, title=""):
    w, h = A4
    c.setFont("Helvetica", 10)
    c.drawCentredString(w / 2, 30, "WinItalPascal – Manuale Unico")


def crea_pagina(path, draw_fn, title=""):
    c = canvas.Canvas(path, pagesize=A4)
    header_footer(c, title)
    draw_fn(c)
    c.showPage()
    c.save()


# === COPERTINA ===
def crea_copertina():
    def draw(c):
        w, h = A4

        c.setFont("Helvetica-Bold", 32)
        c.drawCentredString(w / 2, h - 360, "WinItalPascal")

        c.setFont("Helvetica", 16)
        c.drawCentredString(w / 2, h - 390,
                            "Libreria di utilità per applicazioni VB.NET WinForms")

        c.setFont("Helvetica", 14)
        c.drawCentredString(w / 2, h - 430, "Autore: ItalPascal")

        data = datetime.now().strftime("%d/%m/%Y")
        c.drawCentredString(w / 2, h - 450, f"Data: {data}")

    crea_pagina(copertina_temp, draw, "-")


# === INFO ===
def crea_info():
    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, h - 120, "Informazioni sul progetto")

        c.setFont("Helvetica", 14)
        y = h - 170

        c.drawString(50, y, "WinItalPascal – Libreria VB.NET WinForms")
        y -= 25
        c.drawString(50, y, "Versione: 2.0.6")
        y -= 25
        c.drawString(50, y, "Autore: ItalPascal")
        y -= 25

        # === LINK GITHUB ===
        link = "https://github.com/List051/WinItalPascal_Lib"
        c.drawString(50, y, "Repository GitHub:")

        c.setFillColorRGB(0, 0, 1)
        c.drawString(200, y, link)

        text_width = c.stringWidth(link, "Helvetica", 14)
        c.line(200, y - 2, 200 + text_width, y - 2)

        c.setFillColorRGB(0, 0, 0)
        c.linkURL(link, (200, y - 5, 200 + text_width, y + 10), relative=0)

        y -= 25

        # === LINK NUGET ===
        link = "https://www.nuget.org/packages/WinItalPascal"
        c.drawString(50, y, "NuGet:")
        c.setFillColorRGB(0, 0, 1)
        c.drawString(200, y, link)
        text_width = c.stringWidth(link, "Helvetica", 14)
        c.line(200, y - 2, 200 + text_width, y - 2)
        c.setFillColorRGB(0, 0, 0)
        c.linkURL(link, (200, y - 5, 200 + text_width, y + 10), relative=0)

        y -= 25

        # === LINK DOCUMENTAZIONE ===
        link = "https://list051.github.io/WinVideoShowcase/"
        c.drawString(50, y, "Documentazione:")
        c.setFillColorRGB(0, 0, 1)
        c.drawString(200, y, link)
        text_width = c.stringWidth(link, "Helvetica", 14)
        c.line(200, y - 2, 200 + text_width, y - 2)
        c.setFillColorRGB(0, 0, 0)
        c.linkURL(link, (200, y - 5, 200 + text_width, y + 10), relative=0)

    crea_pagina(info_temp, draw, "Informazioni")


# === CHANGELOG ===
def crea_changelog():
    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, h - 120, "Cronologia Versioni – 2.0.6 (27 Luglio 2026)")

        c.setFont("Helvetica", 14)
        y = h - 170
        changes = [
            "• Introdotto ReportManager per la gestione centralizzata dei report RDLC.",
            "• Aggiunta la gestione della documentazione HTML tramite FrmDocumentazione.",
            "• Centralizzata nella libreria WinItalPascal la ricerca della cartella Help.",
            "• Il progetto host gestisce direttamente l'apertura della documentazione.",
            "• Migliorata la gestione dei DataGridView.",
            "• Aggiornato il pacchetto NuGet alla versione 2.0.6."
        ]
        for line in changes:
            c.drawString(50, y, line)
            y -= 25

    crea_pagina(changelog_temp, draw, "Changelog")


# === STRUTTURA LIBRERIA ===
def crea_struttura():
    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)

        try:
            c.drawImage(diagramma_path, 50, h - 900,
                        width=520, preserveAspectRatio=True)
        except:
            c.setFont("Helvetica", 12)
            c.drawString(50, h - 150, "[Diagramma non trovato]")

    crea_pagina(struttura_temp, draw, "Struttura")


# === INSTALLAZIONE NUGET ===
def crea_nuget():
    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, h - 120, "Installazione tramite NuGet")

        c.setFont("Helvetica", 14)
        y = h - 170
        lines = [
            "Per installare WinItalPascal:",
            "",
            "Package Manager Console:",
            "Install-Package WinItalPascal",
            "",
            "CLI:",
            "dotnet add package WinItalPascal"
        ]
        for line in lines:
            c.drawString(50, y, line)
            y -= 25

    crea_pagina(nuget_temp, draw, "NuGet")


# === INDICE ===
def crea_indice():
    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, h - 120, "Indice")

        c.setFont("Helvetica", 14)
        y = h - 170
        voci = [
            "1. Copertina",
            "2. Informazioni",
            "3. Changelog",
            "4. Struttura Libreria",
            "5. Installazione NuGet",
            "6. Licenza MIT"
        ]
        for voce in voci:
            c.drawString(50, y, voce)
            y -= 20

    crea_pagina(indice_temp, draw, "Indice")


# === LICENZA MIT ===
def crea_licenza():
    def draw(c):
        w, h = A4
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, h - 120, "Licenza MIT")

        c.setFont("Helvetica", 12)
        y = h - 170

        testo = [
            "MIT License",
            "",
            "Copyright (c) 2026 ItalPascal",
            "",
            "Permission is hereby granted, free of charge, to any person obtaining a copy",
            "of this software and associated documentation files (the \"Software\"), to deal",
            "in the Software without restriction, including without limitation the rights",
            "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell",
            "copies of the Software, and to permit persons to whom the Software is",
            "furnished to do so, subject to the following conditions:",
            "",
            "The above copyright notice and this permission notice shall be included in all",
            "copies or substantial portions of the Software.",
            "",
            "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR",
            "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,",
            "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE",
            "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER",
            "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,",
            "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE",
            "SOFTWARE."
        ]

        for line in testo:
            c.drawString(50, y, line)
            y -= 18

    crea_pagina(licenza_temp, draw, "Licenza MIT")


# === PULIZIA FILE TEMPORANEI ===
def pulizia_temp():
    for f in [
        copertina_temp, info_temp, changelog_temp, struttura_temp,
        nuget_temp, indice_temp, licenza_temp
    ]:
        if os.path.isfile(f):
            try:
                os.remove(f)
            except:
                pass


# === UNIONE PDF ===
def crea_unico_pdf():
    merger = PdfMerger()

    for pagina in [
        copertina_temp,
        info_temp,
        changelog_temp,
        struttura_temp,
        nuget_temp,
        indice_temp,
        licenza_temp
    ]:
        merger.append(pagina)

    os.makedirs(output_dir, exist_ok=True)

    merger.write(output_file)
    merger.close()

    pulizia_temp()
    print("SegueManuale.pdf creato con successo:", output_file)


# === ESECUZIONE ===
if __name__ == "__main__":
    crea_copertina()
    crea_info()
    crea_changelog()
    crea_struttura()
    crea_nuget()
    crea_indice()
    crea_licenza()
    crea_unico_pdf()
