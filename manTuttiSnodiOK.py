import os
import subprocess

# Cartella principale dove si trovano gli Snodi
root = r"C:\Users\Utente\Desktop\ManualeAgo\PDF_Odvision"

# Lista delle cartelle Snodo
snodi = [
    "SnodoCore",
    "SnodoDB",
    "SnodoForms",
    "SnodoLogging",
    "SnodoMsg",
    "SnodoPopup",
    "SnodoReport"
]

print("=== GENERAZIONE DI TUTTI I MANUALI SNODO ===\n")

for snodo in snodi:
    snodo_path = os.path.join(root, snodo)
    script_path = os.path.join(snodo_path, f"manuale_{snodo}.py")
    pdf_path = os.path.join(snodo_path, "PDF")

    print(f"Snodo: {snodo}")

    # Verifica cartella Snodo
    if not os.path.isdir(snodo_path):
        print(f"  ❌ Cartella non trovata: {snodo_path}\n")
        continue

    # Verifica script Snodo
    if not os.path.isfile(script_path):
        print(f"  ❌ Script non trovato: {script_path}\n")
        continue

    # Verifica cartella PDF
    if not os.path.isdir(pdf_path):
        print(f"  ❌ Cartella PDF mancante: {pdf_path}\n")
        continue

    # Verifica presenza PDF
    pdf_files = [f for f in os.listdir(pdf_path) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print(f"  ⚠️ Nessun PDF trovato in {pdf_path} — manuale NON generato\n")
        continue

    # Esecuzione script Snodo
    try:
        print("  ▶️ Generazione manuale...")
        subprocess.run(["python", script_path], check=True)
        print("  ✅ Manuale generato con successo!\n")
    except Exception as e:
        print(f"  ❌ Errore durante l'esecuzione dello script: {e}\n")

print("=== COMPLETATO ===")
