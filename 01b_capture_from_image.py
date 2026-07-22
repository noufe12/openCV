

import cv2
import os

person_name = "Noufa"
person_id = 1
image_path = "img.jpg" 
dataset_dir = "dataset"
os.makedirs(dataset_dir, exist_ok=True)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread(image_path)
if img is None:
    print(f"[ERROR] Could not read '{image_path}'. Check the filename/path.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

if len(faces) == 0:
    print("[WARNING] No face detected in this image. Try a clearer photo.")
else:
    count = 0
    for (x, y, w, h) in faces:
        count += 1
        face_img = gray[y:y + h, x:x + w]
        filename = f"{dataset_dir}/user.{person_id}.{count}.jpg"
        cv2.imwrite(filename, face_img)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save a copy of the image with the detected face boxed, so you can check it
    cv2.imwrite("detected_preview.jpg", img)
    print(f"[INFO] {count} face(s) saved to '{dataset_dir}/'.")
    print("[INFO] Check 'detected_preview.jpg' to see the detected face box.")

print("[NOTE] For a real training set, repeat with several different photos")
print("       of the same person (different angles/lighting) for better accuracy.")