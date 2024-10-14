# validate_image.py
from flask import Blueprint, request, jsonify
import cv2
import requests
import numpy as np

validate_image_bp = Blueprint('validate_image', __name__)

@validate_image_bp.route('/validate-image', methods=['POST'])
def validate_image():
    results = []
    # Sample image URLs for testing; in a real scenario, you might get these from the request
    image_urls = request.json.get('image_urls', [])

    for url in image_urls:
        response = requests.get(url)
        image_np = np.asarray(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Check if the image is valid
        if image is None:
            results.append({'url': url, 'status': 'invalid image'})
            continue

        # Perform face detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            results.append({'url': url, 'status': 'no face detected'})
            continue

        # Validate face visibility and lighting (simplified)
        for (x, y, w, h) in faces:
            # Extract face region
            face_roi = image[y:y+h, x:x+w]
            brightness = cv2.mean(cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY))[0]
            if brightness < 50:  # Simple lighting check
                results.append({'url': url, 'status': 'face too dark'})
                continue

        # Final validation for the ID card (simplified)
        results.append({'url': url, 'status': 'valid image and face detected'})

    return jsonify(results)
