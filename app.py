%%writefile app.py
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load trained model
MODEL_PATH = "dextro_model.h5"   # make sure model is in same folder
model = load_model(MODEL_PATH)


st.title("🫀 Dextrocardia Detection using CNN")
st.write("Upload a chest X-ray image to detect whether it is **Normal** or **Dextrocardia**.")


uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
   
    img = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    st.image(img, caption="Uploaded Image", use_column_width=True)

  
    img = img.resize((128,128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # shape: (1,128,128,1)

    pred = model.predict(img_array)
    label = "Dextrocardia 🫀" if np.argmax(pred) == 1 else "Normal ✅"
    confidence = np.max(pred) * 100

  
    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2f}%")
