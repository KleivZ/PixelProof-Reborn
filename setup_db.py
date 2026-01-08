import sqlite3
import os

DB_FOLDER = 'database'
DB_FILE = os.path.join(DB_FOLDER, 'pixelproof.db')

def setup_database():
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Vi legger til 'algorithm_version' for å kunne skille mellom analyser
    c.execute('''CREATE TABLE IF NOT EXISTS videos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  url_hash TEXT UNIQUE,
                  deepfake_value REAL,
                  algorithm_version TEXT,
                  date_added TEXT)''')
    
    conn.commit()
    conn.close()
    print(f"Suksess! Database-filen '{os.path.basename(DB_FILE)}' er opprettet med versjonskontroll.")

if __name__ == '__main__':
    setup_database()