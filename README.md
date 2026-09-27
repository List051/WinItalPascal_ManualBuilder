---
<p align="center">
  <img src="Logo_1.png" alt="Ital Pascal Logo" width="220">
</p>

---

<div align="center">
  <strong>📘 WinItalPascal_ManualBuilder</strong>
</div>

<p align="center">

  <a href="https://github.com/List051/WinItalPascal_ManualBuilder">
    <img src="https://img.shields.io/github/stars/List051/WinItalPascal_ManualBuilder?style=for-the-badge" alt="MB Stars">
  </a>

  <a href="https://github.com/List051/WinItalPascal_ManualBuilder">
    <img src="https://img.shields.io/github/forks/List051/WinItalPascal_ManualBuilder?style=for-the-badge" alt="MB Forks">
  </a>

  <a href="https://github.com/List051/WinItalPascal_ManualBuilder/issues">
    <img src="https://img.shields.io/github/issues/List051/WinItalPascal_ManualBuilder?style=for-the-badge" alt="MB Issues">
  </a>

  <a href="https://github.com/List051/WinItalPascal_ManualBuilder/commits/main">
    <img src="https://img.shields.io/github/last-commit/List051/WinItalPascal_ManualBuilder?style=for-the-badge" alt="MB Last Commit">
  </a>

  <a href="https://github.com/List051/WinItalPascal_ManualBuilder/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/List051/WinItalPascal_ManualBuilder?style=for-the-badge" alt="MB License">
  </a>

</p>

<!-- SEPARATORE -->
<div align="center" style="font-size:28px; margin: 10px 0;">⬤</div>

<!-- ========================= -->
<!--   BADGE - LIBRERIA VB.NET -->
<!-- ========================= -->

<div align="center">
  <strong>🧩 WinItalPascal_Lib</strong>
</div>

<p align="center">
  <!-- NuGet -->
  <a href="https://www.nuget.org/packages/WinItalPascal">
    <img src="https://img.shields.io/nuget/v/WinItalPascal?style=for-the-badge" alt="NuGet Version">
  </a>
  <a href="https://www.nuget.org/packages/WinItalPascal">
    <img src="https://img.shields.io/nuget/dt/WinItalPascal?style=for-the-badge" alt="NuGet Downloads">
  </a>

  <a href="https://github.com/List051/WinItalPascal_Lib">
    <img src="https://img.shields.io/github/stars/List051/WinItalPascal_Lib?style=for-the-badge" alt="Lib Stars">
  </a>

  <a href="https://github.com/List051/WinItalPascal_Lib">
    <img src="https://img.shields.io/github/forks/List051/WinItalPascal_Lib?style=for-the-badge" alt="Lib Forks">
  </a>

  <a href="https://github.com/List051/WinItalPascal_Lib/issues">
    <img src="https://img.shields.io/github/issues/List051/WinItalPascal_Lib?style=for-the-badge" alt="Lib Issues">
  </a>

  <a href="https://github.com/List051/WinItalPascal_Lib/commits/main">
    <img src="https://img.shields.io/github/last-commit/List051/WinItalPascal_Lib?style=for-the-badge" alt="Lib Last Commit">
  </a>

  <a href="https://github.com/List051/WinItalPascal_Lib/blob/main/License.txt">
    <img src="https://img.shields.io/github/license/List051/WinItalPascal_Lib?style=for-the-badge" alt="Lib License">
  </a>

</p>

---

# 🧩 WinItalPascal – Sistema di Generazione Manuali

Questo repository contiene il sistema completo utilizzato per generare automaticamente il manuale della libreria WinItalPascal.  
Raccoglie gli script Python, la struttura dei moduli (Snodi) e la pipeline che produce il manuale finale in PDF.  
È pensato per documentare il processo di costruzione del manuale, così da poterlo replicare o aggiornare facilmente nel tempo.

---
## 🎯 Obiettivo del progetto

Questo repository **non contiene la libreria WinItalPascal**, ma il sistema che permette di generare la sua documentazione ufficiale.  
L’obiettivo è fornire una pipeline chiara, modulare e automatizzata per creare:

- i manuali dei singoli Snodi (Core, DB, Forms, Logging, ecc.)  
- il manuale tecnico completo della libreria  
- la prefazione e la documentazione introduttiva  
- il PDF finale unificato pronto per la distribuzione

In questo modo la documentazione della libreria può essere aggiornata, ampliata o rigenerata in modo semplice e coerente.

# 📁 Struttura del progetto

La cartella principale è:

```
Script_UnisciPDF/UnisciPDF_OdVision
```

##  🔵  Contiene:

- **SnodoCore/**
- **SnodoDB/**
- **SnodoForms/**
- **SnodoLogging/**
- **SnodoMsg/**
- **SnodoPopup/**
- **SnodoReport/**
- **Script per generare e unire PDF**

---

#  🔵 Ogni Snodo contiene:

```
SnodoXYZ/
    PDF/                → PDF del manuale dello Snodo
    GENERATED/          → file temporanei
    Logo.png            → logo dello Snodo
    GrafoXYZ.png        → grafo dello Snodo
    manuale_SnodoXYZ.py → script generazione manuale Snodo
    manuale_SnodoXYZ.pdf→ manuale generato
```

---
# 🚀 Pipeline completa (4 fasi)

## 🔵 **1️⃣ Generazione dei manuali dei singoli Snodi**

Esegui:

```
python manTuttiSnodi.py
```

Questo script:

- entra automaticamente in ogni Snodo  
- esegue `manuale_SnodoXYZ.py`  
- genera:

```
SnodoXYZ/manuale_SnodoXYZ.pdf
```

### 📌 Nota importante
Se vuoi che il grafo sia la **prima pagina** del manuale Snodo:

Metti in:

```
SnodoXYZ/PDF/
```

un file chiamato:

```
00_GrafoXYZ.pdf
```

Il prefisso `00_` garantisce che venga unito per primo.

---
## 🟢 **2️⃣ Creazione del manuale tecnico completo**

Esegui:

```
python unisci_snodo_pdfAvanzato.py
```

Questo script:

- prende tutti i `manuale_SnodoXYZ.pdf`
- li unisce in ordine
- genera:

```
Manuale_Unico_WinItalPascal.pdf
```

Questo è il **manuale tecnico completo** della libreria.

---

## 🟣 **3️⃣ Creazione della prefazione / introduzione del manuale**

Esegui:

```
python UnicoPDFGenerated.py
```

Questo script genera:

```
SegueManuale.pdf
```

Contiene:

- Copertina  
- Informazioni  
- Changelog  
- Struttura libreria  
- Installazione NuGet  
- Esempio VB.NET  
- Licenza MIT  

I file temporanei vengono eliminati automaticamente.

---

## 🔴 **4️⃣ Unione finale dei due PDF**

Vai nella cartella:

```
Script_UnisciPDF/PDF_Odvision
```

Troverai:

```
01_SegueManuale.pdf
Manuale_Unico_WinItalPascal.pdf
```

Esegui:

```
python unisciFinale.py
```

Questo script:

- unisce prima **Manuale_Unico_WinItalPascal.pdf**
- poi **01_SegueManuale.pdf**
- genera:

```
Manuale_Completo.pdf
```

Questo è il **manuale finale definitivo**.

---
# 📂 File finali generati

### 📘 Manuale tecnico:
```
UnisciPDF_OdVision/Manuale_Unico_WinItalPascal.pdf
```

### 📗 Prefazione:
```
PDF_Odvision/01_SegueManuale.pdf
```

### 📙 Manuale completo:
```
PDF_Odvision/Manuale_Completo.pdf
```

---
# ⚠️ Note importanti

### ❗ NON copiare mai nel progetto testi tipo:
```
edge_all_open_tabs = [...]
```
Sono **solo dati tecnici del browser Edge**, NON fanno parte del progetto.

### ❗ I PDF degli Snodi devono essere nella cartella:
```
SnodoXYZ/PDF/
```

### ❗ Se vuoi che il grafo sia la prima pagina:
Rinomina il file in:

```
00_GrafoXYZ.pdf
```

---
# 🧩 Aggiungere un nuovo Snodo (tra mesi)

Se tra mesi aggiungi un nuovo Snodo:

1. crea la cartella `SnodoNuovo`
2. crea `PDF/` con i PDF
3. crea `Logo.png` e `GrafoNuovo.png`
4. copia uno script `manuale_SnodoXYZ.py` e rinominalo
5. aggiungi il nome dello Snodo in `manTuttiSnodi.py`
6. esegui la pipeline completa

---
### 📌 Grafico procedure

```mermaid
graph LR

    %% ====== PALETTE PASTELLO TECH (MODERNA) ======
    classDef core  fill:#A7C7E7,stroke:#7FA4C4,color:#000000,rx:12,ry:12;
    classDef db    fill:#A8E6CF,stroke:#7FBFA7,color:#000000,rx:12,ry:12;
    classDef forms fill:#FFD3B6,stroke:#E6B89C,color:#000000,rx:12,ry:12;
    classDef log   fill:#FFAAA5,stroke:#D98C87,color:#000000,rx:12,ry:12;
    classDef popup fill:#D5C6E0,stroke:#B6A9C4,color:#000000,rx:12,ry:12;
    classDef msg   fill:#C4E8FF,stroke:#9BBFD4,color:#000000,rx:12,ry:12;
    classDef ext   fill:#FFF9C4,stroke:#D8CCA8,color:#000000,rx:12,ry:12;

    %% ====== MAIN (ORA FUNZIONA) ======
    classDef main fill:#cba6f7,stroke:#BFBFBF,color:#000000,rx:12,ry:12;

    %% ====== NODO PRINCIPALE ======
    A([📘 WinItalPascal Manual Builder]):::main

    %% ====== CARTELLE SNODO ======
    A --> C1[📂 SnodoCore]:::core
    A --> C2[📂 SnodoDB]:::db
    A --> C3[📂 SnodoForms]:::forms
    A --> C4[📂 SnodoLogging]:::log
    A --> C5[📂 SnodoMsg]:::msg
    A --> C6[📂 SnodoPopup]:::popup
    A --> C7[📂 SnodoReport]:::ext

    %% ====== CONTENUTO SNODO ======
    C1 --> P1[📄 manuale_SnodoCore.py]:::core
    C2 --> P2[📄 manuale_SnodoDB.py]:::db
    C3 --> P3[📄 manuale_SnodoForms.py]:::forms
    C4 --> P4[📄 manuale_SnodoLogging.py]:::log
    C5 --> P5[📄 manuale_SnodoMsg.py]:::msg
    C6 --> P6[📄 manuale_SnodoPopup.py]:::popup
    C7 --> P7[📄 manuale_SnodoReport.py]:::ext

    %% ====== GENERAZIONE SNODO ======
    P1 --> O1[📘 manuale_SnodoCore.pdf]:::core
    P2 --> O2[📘 manuale_SnodoDB.pdf]:::db
    P3 --> O3[📘 manuale_SnodoForms.pdf]:::forms
    P4 --> O4[📘 manuale_SnodoLogging.pdf]:::log
    P5 --> O5[📘 manuale_SnodoMsg.pdf]:::msg
    P6 --> O6[📘 manuale_SnodoPopup.pdf]:::popup
    P7 --> O7[📘 manuale_SnodoReport.pdf]:::ext

    %% ====== SCRIPT MULTI-SNODO ======
    A --> MTS[⚙️ manTuttiSnodi.py]:::main
    MTS --> O1
    MTS --> O2
    MTS --> O3
    MTS --> O4
    MTS --> O5
    MTS --> O6
    MTS --> O7

    %% ====== UNIONE SNODO ======
    A --> US[🔗 unisci_snodo_pdfAvanzato.py]:::main
    US --> MU[📙 Manuale_Unico_WinItalPascal.pdf]:::main

    %% ====== PREFACE ======
    A --> UP[📝 UnicoPDFGenerated.py]:::main
    UP --> SM[📗 01_SegueManuale.pdf]:::main

    %% ====== UNIONE FINALE ======
    A --> UF[🔗 unisciFinale.py]:::main
    UF --> MC[📘 Manuale_Completo.pdf]:::main

    %% ====== OUTPUT ======
    MU --> MC
    SM --> MC

```
# 🔗 Link utili

## 📚 Documentazione della libreria WinItalPascal

- [📘 Documentazione Tecnica (*.md)](https://github.com/List051/WinItalPascal_Lib/tree/main/Documentation)
- [📄 Manuali PDF della libreria](https://github.com/List051/WinItalPascal_Lib/tree/main/Help/pdf)

---

## 🎬 Video dimostrativi

- [🎥 Video Esempi – WinVideoShowcase](https://list051.github.io/WinVideoShowcase/)
- [📺 Canale YouTube](https://www.youtube.com/@iaoraGo)
- [🎞️ Playlist completa WinItalPascal](https://www.youtube.com/watch?v=UboNebA_Irs&list=PLqYE2xAtyfEAiNY4qC2LeJJuCJPyUScXL)

---
<div align="center">
  <h2>⭐ Come supportare il progetto</h2>
  <p>Se questo progetto ti è utile, puoi supportarlo con un semplice gesto:</p>


<!-- Pulsante Star -->
  <a href="https://github.com/List051/WinTestGrid">
    <img src="https://img.shields.io/github/stars/List051/WinTestGrid?style=social" alt="Star this repo">
  </a>

  <!-- Pulsante Fork -->
  <a href="https://github.com/List051/WinItalPascal_Help/fork">
    <img src="https://img.shields.io/github/forks/List051/WinItalPascal_Help?label=fork&style=social" alt="Fork this repo">
  </a>
  <p>Mettere una ⭐ o fare un Fork aiuta il progetto a crescere e permette ad altri sviluppatori di scoprirlo.</p>

  <br>

  <!-- Pulsante Follow autore -->
  <p>Vuoi restare aggiornato sui nuovi progetti?</p>

  <a href="https://github.com/List051">
    <img src="https://img.shields.io/github/followers/List051?label=Follow%20%40List051&style=social" alt="Follow @List051">
  </a>

  <p>Grazie per il tuo supporto!</p>
</div>
---
<div class="page-break"></div>
