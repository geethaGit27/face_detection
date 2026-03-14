import streamlit as st
from PIL import Image, ImageFilter, ImageOps
import numpy as np

st.title("Lightweight Image Processing App with Contour Detection")
st.write("Upload an image and apply filters or contour detection (Pillow + NumPy only)")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Apply filters
    filter_option = st.selectbox(
        "Choose a filter:",
        ["Grayscale", "Invert", "Blur", "Edge Detection", "Contour Detection"]
    )
    
    if filter_option == "Grayscale":
        processed_img = img.convert("L")
    
    elif filter_option == "Invert":
        processed_img = ImageOps.invert(img)
    
    elif filter_option == "Blur":
        processed_img = img.filter(ImageFilter.BLUR)
    
    elif filter_option == "Edge Detection":
        processed_img = img.filter(ImageFilter.FIND_EDGES)
    
    elif filter_option == "Contour Detection":
        # Convert to grayscale
        gray = img.convert("L")
        # Apply edge detection
        edges = gray.filter(ImageFilter.FIND_EDGES)
        # Convert to NumPy array
        arr = np.array(edges)
        # Apply binary threshold to highlight edges as contours
        threshold = 50  # adjust for sensitivity
        arr = np.where(arr > threshold, 255, 0).astype(np.uint8)
        # Convert back to PIL image
        processed_img = Image.fromarray(arr)
    
    st.image(processed_img, caption=f"{filter_option} Applied", use_column_width=True)
