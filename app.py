import os
import re
from flask import Flask, render_template, request, flash
from dotenv import load_dotenv

# Import av våre egne moduler
from core.hashing import calculate_url_hash
from core.downloader import download_video, delete_video
from core.face_logic import extract_faces
from core.detector import analyze_video_faces
from database.db_handler import check_if_exists, insert_video_data

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "pixelproof_dev_key_2026")

# --- KONFIGURASJON ---
# Versjonskontroll: Endre denne når du oppgraderer AI-modellen
CURRENT_VERSION = "0.01"
# ---------------------

YOUTUBE_PATTERN = r"^((https?:\/\/)?(www\.)?youtube\.com\/|(https?:\/\/)?youtu.be\/)(watch\?v=|shorts\/)?([\w\-]{11}).*$"

@app.route('/', methods=['GET', 'POST'])
def index():
    faces_data = [] 
    
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        
        if re.match(YOUTUBE_PATTERN, url):
            # 1. Generer hash
            url_hash = calculate_url_hash(url)
            
            # 2. Sjekk database
            existing_entry = check_if_exists(url_hash)
            run_new_analysis = False
            
            # 3. Cache-logikk
            if existing_entry and existing_entry['algorithm_version'] == CURRENT_VERSION:
                # TREFF: Vis lagret resultat
                score = existing_entry['deepfake_value']
                verdict = "Sannsynligvis DEEPFAKE" if score > 50 else "Sannsynligvis EKTE"
                category = "error" if score > 50 else "success"
                
                flash(f"Hentet fra arkivet (v{CURRENT_VERSION}): {verdict} (Risiko: {score}%)", category)
            else:
                # BOM eller GAMMEL VERSJON: Kjør ny analyse
                if existing_entry:
                    old_v = existing_entry['algorithm_version']
                    flash(f"Oppdaterer analyse fra v{old_v} til v{CURRENT_VERSION}...", "info")
                else:
                    flash("Ny video. Starter analyse...", "info")
                
                run_new_analysis = True

            # 4. Kjør analyse ved behov
            if run_new_analysis:
                video_path = download_video(url)
                
                if video_path:
                    face_files = extract_faces(video_path)
                    
                    if face_files:
                        avg_score, detailed_results = analyze_video_faces(face_files)
                        
                        # Lagre til database
                        insert_video_data(url_hash, avg_score, CURRENT_VERSION)
                        
                        # Vis resultat
                        verdict = "Sannsynligvis DEEPFAKE" if avg_score > 50 else "Sannsynligvis EKTE"
                        category = "error" if avg_score > 50 else "success"
                        flash(f"Analyse ferdig! {verdict} (Risiko: {avg_score}%)", category)
                        
                        faces_data = detailed_results
                    else:
                        flash("Fant ingen ansikter i videoen å analysere.", "warning")
                    
                    delete_video(video_path)
                else:
                    flash("Nedlasting feilet. Sjekk at videoen er tilgjengelig og under 10 min.", "error")
                    
        else:
            flash("Ugyldig YouTube-URL.", "error")
            
    return render_template('index.html', faces=faces_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)