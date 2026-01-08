import cv2
import os
import numpy as np
import urllib.request

# Baner til modellfilene vi trenger for AI-deteksjon
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE_DIR, "res10_300x300_ssd_iter_140000.caffemodel")
CONFIG_FILE = os.path.join(BASE_DIR, "deploy.prototxt")

def download_model_files():
    """
    Sjekker om vi mangler AI-modellen. Hvis ja, lastes den ned automatisk
    fra OpenCV sine offisielle kilder.
    """
    model_url = "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"
    config_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt"

    if not os.path.exists(MODEL_FILE):
        print("--- Laster ned AI-modell (caffemodel)... dette tar noen sekunder ---")
        urllib.request.urlretrieve(model_url, MODEL_FILE)
    
    if not os.path.exists(CONFIG_FILE):
        print("--- Laster ned konfigurasjon (prototxt)... ---")
        urllib.request.urlretrieve(config_url, CONFIG_FILE)

def extract_faces(video_path, output_folder='static/processed_faces'):
    """
    Avansert ansiktsdeteksjon med Deep Neural Network (DNN).
    Lagrer ansikter i full JPEG-kvalitet for å unngå støy.
    """
    # 1. Sørg for at AI-modellen er på plass
    download_model_files()

    # 2. Rydd opp i mappen før start
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        for f in os.listdir(output_folder):
            if f.endswith(".jpg"):
                os.remove(os.path.join(output_folder, f))

    # 3. Last inn det nevrale nettverket
    print(f"Starter analyse av: {os.path.basename(video_path)}")
    net = cv2.dnn.readNetFromCaffe(CONFIG_FILE, MODEL_FILE)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_filenames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Sampler hver 15. frame for effektivitet
        if frame_count % 15 == 0:
            (h, w) = frame.shape[:2]
            
            # Skalerer til 300x300 for AI-modellen (men beholder original frame for cropping)
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                (300, 300), (104.0, 177.0, 123.0))
            
            net.setInput(blob)
            detections = net.forward()

            # Går gjennom alle deteksjoner i bildet
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                # Krav: 50% sikkerhet for at det er et ansikt
                if confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # Sikre at koordinatene er innenfor bildet
                    startX, startY = max(0, startX), max(0, startY)
                    endX, endY = min(w, endX), min(h, endY)

                    # Legg til 20% margin for kontekst (hake/panne)
                    face_w = endX - startX
                    face_h = endY - startY
                    margin_x = int(face_w * 0.2)
                    margin_y = int(face_h * 0.2)

                    y1, y2 = max(0, startY - margin_y), min(h, endY + margin_y)
                    x1, x2 = max(0, startX - margin_x), min(w, endX + margin_x)

                    face_img = frame[y1:y2, x1:x2]

                    # Lagre kun hvis bildet er stort nok (fjerner ørsmå ansikter i bakgrunnen)
                    if face_img.size > 0 and face_w > 30 and face_h > 30:
                        filename = f"face_{frame_count}_{len(saved_filenames)}.jpg"
                        filepath = os.path.join(output_folder, filename)
                        
                        # VIKTIG ENDRING: Lagre med maks kvalitet (100) i stedet for standard (95)
                        cv2.imwrite(filepath, face_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                        
                        saved_filenames.append(filename)

        frame_count += 1
        # Stopper etter 12 gode bilder for å spare tid/plass
        if len(saved_filenames) >= 12:
            break

    cap.release()
    return saved_filenames