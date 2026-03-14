import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Face Detection App (Lightweight, Streamlit Cloud Friendly)")

st.write("Upload an image, and the app will detect faces using OpenCV Haar cascades.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert to OpenCV format
    img = np.array(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Load OpenCV pre-trained Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # Detect faces
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5)
    
    st.write(f"Found {len(faces)} face(s)!")
    
    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    
    st.image(img, caption="Faces Detected", use_column_width=True)
