import streamlit as st
from PIL import Image
import numpy as np
import random

# Simulated model output for demo purposes
SKIN_PROBLEMS = {
    "Acne": "Use salicylic acid face wash and lightweight moisturizers.",
    "Blackhead": "Exfoliate regularly and use retinoid-based products.",
    "Dark Spot": "Try vitamin C serum and sunscreen daily.",
    "Dry Skin": "Hydrating cleansers and hyaluronic acid-based moisturizers work well.",
    "Eye Bags": "Use caffeine eye serums and get sufficient sleep.",
    "Oily Skin": "Oil-free products and clay masks are recommended.",
    "Wrinkles": "Retinol creams and collagen-boosting treatments help.",
    "Pores": "Niacinamide serums can minimize pore appearance.",
    "Skin Redness": "Use calming products with centella asiatica.",
    "Normal Skin": "Maintain a balanced skincare routine."
}

# Simulated skin detection function
def detect_skin_problems(image):
    detected = random.sample(list(SKIN_PROBLEMS.keys()), k=random.randint(1, 3))
    return detected

# UI
st.set_page_config(page_title="Skin Problem Detection & Care", layout="wide")
st.title("🧴 Skin Analyzer & Skincare Recommender")
st.markdown("---")

# Upload
uploaded_files = st.file_uploader("Upload a facial image", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        st.image(file, width=250, caption="Uploaded Image")

        # Simulate detection
        image = Image.open(file)
        detected_problems = detect_skin_problems(image)

        st.markdown("### 🩺 Detected Skin Issues")
        cols = st.columns(len(detected_problems))
        for i, prob in enumerate(detected_problems):
            with cols[i]:
                st.success(prob)
        
        st.markdown("### 🧪 Personalized Recommendations")
        for prob in detected_problems:
            with st.expander(f"💡 {prob}"):
                st.write(SKIN_PROBLEMS[prob])

        st.markdown("---")
