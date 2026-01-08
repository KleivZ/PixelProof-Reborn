from transformers import pipeline
import os

# Vi bruker en pre-trent Vision Transformer-modell fra Hugging Face
# Denne lastes ned automatisk første gang koden kjøres
MODEL_ID = "dima806/deepfake_vs_real_image_detection"

# Vi laster inn modellen globalt så vi slipper å laste den på nytt for hvert bilde
print(f"--- Initialiserer AI-detektor: {MODEL_ID} ---")
try:
    pipe = pipeline("image-classification", model=MODEL_ID)
    print("--- AI-modell lastet og klar ---")
except Exception as e:
    print(f"--- Kunne ikke laste AI-modell: {e} ---")
    pipe = None

def analyze_face(image_path):
    """
    Analyserer et bilde og returnerer sannsynligheten for at det er FAKE (0.0 - 1.0).
    """
    if not pipe:
        return 0.0

    try:
        # Kjør modellen på bildet
        result = pipe(image_path)
        # Resultatet ser slik ut: [{'label': 'FAKE', 'score': 0.99}, ...]
        
        deepfake_score = 0.0

        for prediction in result:
            label = prediction['label'].upper()
            score = prediction['score']

            # Hvis modellen sier 'FAKE' eller 'AI', bruker vi den scoren direkte
            if label in ['FAKE', 'AI', 'DEEPFAKE']:
                deepfake_score = score
            # Hvis modellen sier 'REAL', er fake-scoren det motsatte (1 - score)
            elif label == 'REAL':
                if score > deepfake_score: # Bare oppdater hvis REAL-scoren er dominerende
                    deepfake_score = 1.0 - score
        
        return deepfake_score

    except Exception as e:
        print(f"Feil ved analyse av {image_path}: {e}")
        return 0.0

def analyze_video_faces(faces_list, base_folder='static/processed_faces'):
    """
    Går gjennom listen av ansikter, analyserer dem, og beregner snittscore.
    """
    total_score = 0
    count = 0
    detailed_results = []

    print(f"Starter analyse av {len(faces_list)} ansikter...")

    for face_file in faces_list:
        full_path = os.path.join(base_folder, face_file)
        
        if os.path.exists(full_path):
            # Få score (0.0 til 1.0)
            raw_score = analyze_face(full_path)
            
            # Gjør om til prosent for visning (f.eks 95.5)
            percent_score = round(raw_score * 100, 1)
            
            detailed_results.append({
                'file': face_file,
                'score': percent_score
            })
            
            total_score += raw_score
            count += 1
    
    # Beregn gjennomsnitt for hele videoen
    avg_score = 0
    if count > 0:
        avg_score = round((total_score / count) * 100, 1)
        
    return avg_score, detailed_results