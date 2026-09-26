import subprocess
import sys
import os

ROOT = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision"
MAPPA = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision\WinItalPascal_Map.pdf"

# --- CANCELLA LA MAPPA PRIMA DI INIZIARE ---
if os.path.exists(MAPPA):
    print(f"🗑️  Rimuovo mappa esistente: {MAPPA}")
    os.remove(MAPPA)
else:
    print("ℹ️  Nessuna mappa precedente da rimuovere.")

# --- PIPELINE ---
pipeline = [
    "manTuttiSnodiOK.py",
    "UnicoPDFGenerated.py",
    "unisci_Snodo_PDFAvanzato.py",

    # --- GENERAZIONE MAPPA ---
    "WinItalPascal_Map_VectorNero.py",
    "WinItalPascal_Map_AddText.py",

    # --- UNIONE PDF ---
    "unisciPDFLink.py",

    # --- LINK INTERNI ---
    "WinItalPascal_Map_Link.py"
]

print("\n=== AVVIO PIPELINE COMPLETA ===\n")

for script in pipeline:
    path = os.path.join(ROOT, script)

    if not os.path.exists(path):
        print(f"❌ ERRORE: Script non trovato: {path}")
        sys.exit(1)

    print(f"▶️  Eseguo: {script}")
    result = subprocess.run(["python", path])

    if result.returncode != 0:
        print(f"❌ ERRORE durante l'esecuzione di {script}")
        sys.exit(1)

    print(f"✅ Completato: {script}\n")

print("\n=== PIPELINE COMPLETATA CON SUCCESSO ===")
