import hashlib

def calculate_url_hash(url):
    """
    Genererer en SHA-256 hash av en gitt URL.
    Dette brukes som en unik identifikator i databasen for å unngå duplikater[cite: 442, 511].
    """
    # Vi koder URL-en til bytes før hashing
    encoded_url = url.encode('utf-8')
    
    # Lager en SHA-256 hash
    hash_object = hashlib.sha256(encoded_url)
    
    # Returnerer hashen som en hex-streng (varchar i databasen [cite: 511])
    return hash_object.hexdigest()