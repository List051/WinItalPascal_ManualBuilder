import os
from PyPDF2 import PdfMerger

snodo_nome = "SnodoForms"
root = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\SnodoForms"

pdf_dir = os.path.join(root, "PDF")
output_pdf = os.path.join(root, f"manuale_{snodo_nome}.pdf")

def genera_manual_snodo():
    if not os.path.isdir(pdf_dir):
        print(f"❌ Cartella PDF non trovata: {pdf_dir}")
        return

    pdf_files = sorted(
        f for f in os.listdir(pdf_dir)
        if f.lower().endswith(".pdf")
    )

    if not pdf_files:
        print(f"⚠️ Nessun PDF trovato in {pdf_dir}")
        return

    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(os.path.join(pdf_dir, pdf))

    merger.write(output_pdf)
    merger.close()

    print(f"✅ Manuale Snodo generato: {output_pdf}")


if __name__ == "__main__":
    genera_manual_snodo()
