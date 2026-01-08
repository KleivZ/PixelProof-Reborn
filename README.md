# PixelProof-Reborn 🛡️

**PixelProof-Reborn** er en modernisert (2026) videreutvikling av et bachelorprosjekt om deepfake-deteksjon. Systemet analyserer YouTube-videoer for å identifisere manipulerte ansikter ved hjelp av avansert maskinlæring (Vision Transformers).

Prosjektet er bygget som en fullstack webapplikasjon med fokus på skalerbarhet, ytelse og brukervennlighet.

## ✨ Nøkkelfunksjoner

* **📺 Automatisk Videoanalyse:** Laster ned YouTube-videoer i høy kvalitet (1080p) via `yt-dlp` og `ffmpeg`.
* **🧠 Vision Transformer (ViT):** Bruker en pre-trent Hugging Face-modell (*dima806/deepfake_vs_real_image_detection*) for state-of-the-art klassifisering.
* **👤 Presis Ansiktsdeteksjon:** Benytter OpenCV DNN (ResNet-10 SSD) for å isolere ansikter og eliminere falske positiver (som bakgrunnsstøy).
* **🚀 Smart Caching & Versjonskontroll:** Integrert SQLite-database som husker tidligere analyser. Systemet oppdager automatisk hvis algoritmen er oppdatert (versjonsnummer) og tvinger frem ny analyse ved behov.
* **⚡ Mac/Metal Optimalisert:** Kjører maskinlæringen på GPU (MPS - Metal Performance Shaders) for lynrask ytelse på Apple Silicon.

## 🛠️ Teknologistack

* **Backend:** Python 3.14, Flask
* **AI/ML:** PyTorch, Transformers (Hugging Face), OpenCV
* **Database:** SQLite
* **Verktøy:** FFmpeg, yt-dlp, Git

## 📂 Prosjektstruktur

```text
PixelProof-Reborn/
├── app.py                 # Hovedapplikasjon (Flask server)
├── requirements.txt       # Avhengigheter
├── setup_db.py            # Script for å initialisere databasen
├── core/
│   ├── detector.py        # AI-logikk (Vision Transformer)
│   ├── downloader.py      # Videonedlasting og FFmpeg-håndtering
│   ├── face_logic.py      # Ansiktsdeteksjon (OpenCV DNN)
│   └── hashing.py         # Generering av unike ID-er for videoer
├── database/
│   ├── db_handler.py      # CRUD-operasjoner mot SQLite
│   └── pixelproof.db      # Lokal database (ignorert av git)
├── static/
│   └── processed_faces/   # Midlertidig lagring av ansiktsbilder
└── templates/
    └── index.html         # Frontend (Jinja2)