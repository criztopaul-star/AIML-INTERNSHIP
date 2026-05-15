import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Pneumonia Detection",
    page_icon="🩺",
    layout="centered"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
    <style>

    .main {
        background-color: #0E1117;
    }

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: white;
    }

    .subtitle {
        text-align: center;
        color: gray;
        font-size: 18px;
    }

    </style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():

    model = tf.keras.models.load_model(
        "pneumonia_detector.h5"
    )

    return model

model = load_model()

# ==========================================
# TITLE
# ==========================================

st.markdown(
    '<p class="title">🩺 AI Pneumonia Detection</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Upload a Chest X-ray Image</p>',
    unsafe_allow_html=True
)

st.write("")

# ==========================================
# FILE UPLOADER
# ==========================================

uploaded_file = st.file_uploader(

    "📤 Upload X-ray Image",

    type=["jpg", "jpeg", "png"]
)

# ==========================================
# PREDICTION
# ==========================================

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Display image
    st.image(
        image,
        caption="Uploaded X-ray",
        use_container_width=True
    )

    # ======================================
    # IMAGE PREPROCESSING
    # ======================================

    img = image.resize((224,224))

    img_array = np.array(img)

    # Convert grayscale to RGB
    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,)*3, axis=-1)

    # Remove alpha channel
    if len(img_array.shape) == 3 and img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    # ======================================
    # PREDICT
    # ======================================

    with st.spinner("🔍 AI is analyzing the X-ray..."):

        prediction = model.predict(img_array)

        confidence = float(prediction[0][0])

    # ======================================
    # RESULTS
    # ======================================

    st.write("")
    st.subheader("Prediction Result")

    if confidence > 0.5:

        st.error(
            f"⚠️ Pneumonia Detected"
        )

        st.write(
            f"Confidence: {confidence*100:.2f}%"
        )

    else:

        st.success(
            f"✅ Normal"
        )

        st.write(
            f"Confidence: {(1-confidence)*100:.2f}%"
        )

    # ======================================
    # CONFIDENCE BAR
    # ======================================

    st.subheader("Confidence Level")

    st.progress(int(confidence * 100))

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("ℹ️ About")

st.sidebar.info(
    """
    This AI model detects pneumonia
    from chest X-ray images using
    Convolutional Neural Networks (CNN).

    Technologies:
    - TensorFlow
    - EfficientNetB0
    - Streamlit
    """
)

# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("---")

st.caption(
    "Built using CNN + Streamlit"
)