PixelProof-Reborn 🛡️
PixelProof-Reborn er en modernisert (2026) videreutvikling av et bachelorprosjekt om deepfake-deteksjon. Systemet analyserer YouTube-videoer for å identifisere manipulerte ansikter ved hjelp av avansert maskinlæring (Vision Transformers).

Prosjektet er bygget som en fullstack webapplikasjon med fokus på skalerbarhet, ytelse og brukervennlighet.

✨ Nøkkelfunksjoner
📺 Automatisk Videoanalyse: Laster ned YouTube-videoer i høy kvalitet (1080p) via yt-dlp og ffmpeg.

🧠 Vision Transformer (ViT): Bruker en pre-trent Hugging Face-modell (dima806/deepfake_vs_real_image_detection) for state-of-the-art klassifisering.

👤 Presis Ansiktsdeteksjon: Benytter OpenCV DNN (ResNet-10 SSD) for å isolere ansikter og eliminere falske positiver (som bakgrunnsstøy).

🚀 Smart Caching & Versjonskontroll: Integrert SQLite-database som husker tidligere analyser. Systemet oppdager automatisk hvis algoritmen er oppdatert (versjonsnummer) og tvinger frem ny analyse ved behov.

⚡ Mac/Metal Optimalisert: Kjører maskinlæringen på GPU (MPS - Metal Performance Shaders) for lynrask ytelse på Apple Silicon.

🛠️ Teknologistack
Backend: Python 3.14, Flask

AI/ML: PyTorch, Transformers (Hugging Face), OpenCV

Database: SQLite

Verktøy: FFmpeg, yt-dlp, Git

📂 Prosjektstruktur
Plaintext

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
🚀 Installasjon og Kjøring
Forutsetter at du har Python 3.10+ og FFmpeg installert.

1. Klon repositoriet
Bash

git clone https://github.com/ditt-brukernavn/PixelProof-Reborn.git
cd PixelProof-Reborn
2. Sett opp virtuelt miljø
Bash

python -m venv .venv
source .venv/bin/activate  # På Windows: .venv\Scripts\activate
3. Installer avhengigheter
Bash

pip install -r requirements.txt
4. Installer FFmpeg (hvis du er på Mac)
Dette kreves for å laste ned videoer i 1080p.

Bash

brew install ffmpeg
5. Start applikasjonen
Første gang du kjører appen, vil den automatisk laste ned nødvendige AI-modeller (ca. 400 MB).

Bash

python app.py
Gå til http://127.0.0.1:5001 i nettleseren din.

🔄 Roadmap & Fremtidige Mål
[x] Implementere Deep Learning deteksjon (ViT)

[x] Fullverdig database-caching med versjonshåndtering

[ ] Legge til støtte for opplasting av lokale videofiler

[ ] Utvide frontend med CSS-rammeverk (Tailwind/Bootstrap)

[ ] Deploye til skyen (Render/Heroku/AWS)

📜 Lisens & Kreditering
Dette prosjektet er basert på arkitekturen fra bacheloroppgaven "PixelProof" (2025). Koden er skrevet på nytt fra bunnen av i 2026 for å utnytte nyere AI-teknologi.