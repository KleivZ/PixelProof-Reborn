import sqlite3
import os
from datetime import datetime

# Vi bruker absolutt sti for å være sikre på at vi treffer riktig fil
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database', 'pixelproof.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def check_if_exists(url_hash):
    """Sjekker om videoen finnes i databasen."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos WHERE url_hash=?", (url_hash,))
        data = cursor.fetchone()
        conn.close()
        return data
    except Exception as e:
        print(f"Database-feil (lesing): {e}")
        return None

def insert_video_data(url_hash, deepfake_score, version):
    """Lagrer data i databasen med 'INSERT OR REPLACE' for automatisk oppdatering."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("""
            INSERT OR REPLACE INTO videos (url_hash, deepfake_value, algorithm_version, date_added)
            VALUES (?, ?, ?, ?)
        """, (url_hash, deepfake_score, version, date_now))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database-feil (lagring): {e}")