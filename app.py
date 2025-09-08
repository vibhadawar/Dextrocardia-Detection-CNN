import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load model
model = load_model('dextro_model.h5')

st.title("Dextrocardia Detection App")

uploaded_file = st.file_uploader("Upload X-Ray Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, (128, 128)) / 255.0
    img_input = img_resized.reshape(1, 128, 128, 1)

    st.image(img_resized, caption="Uploaded Image", use_column_width=True)

    prediction = model.predict(img_input)
    class_idx = np.argmax(prediction)
    classes = ["Normal", "Dextrocardia"]

    st.write(f"Prediction: **{classes[class_idx]}**")


