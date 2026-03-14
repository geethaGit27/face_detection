import streamlit as st
from PIL import Image, ImageFilter, ImageOps
import numpy as np

st.title("Lightweight Image Processing App")

st.write("Upload an image and apply filters or edge detection (Pillow + NumPy only)")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Apply filters
    filter_option = st.selectbox(
        "Choose a filter:",
        ["Grayscale", "Invert", "Blur", "Edge Detection"]
    )
    
    if filter_option == "Grayscale":
        processed_img = img.convert("L")
    elif filter_option == "Invert":
        processed_img = ImageOps.invert(img)
    elif filter_option == "Blur":
        processed_img = img.filter(ImageFilter.BLUR)
    elif filter_option == "Edge Detection":
        processed_img = img.filter(ImageFilter.FIND_EDGES)
    
    st.image(processed_img, caption=f"{filter_option} Applied", use_column_width=True)
