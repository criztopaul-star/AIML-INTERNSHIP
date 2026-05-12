import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("titanic_model.pkl")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🚢 Titanic ML Project")

st.sidebar.markdown("""
This app predicts whether a passenger would survive the Titanic disaster using Machine Learning.

### Features Used
- Passenger Class
- Sex
- Age
- SibSp
- Parch
- Fare
""")

st.sidebar.info("Built using Streamlit + Scikit-learn")

# -----------------------------
# Main Title
# -----------------------------
st.title("🚢 Titanic Survival Prediction")

st.markdown("Enter passenger details below and click **Predict**.")

st.divider()

# -----------------------------
# Input Fields
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])

    sex = st.selectbox("Sex", ["Male", "Female"])

    age = st.slider("Age", 0, 100, 25)

with col2:
    sibsp = st.number_input("Siblings/Spouse", min_value=0, step=1)

    parch = st.number_input("Parents/Children", min_value=0, step=1)

    fare = st.number_input("Fare", min_value=0.0, step=1.0)

# -----------------------------
# Convert Sex
# -----------------------------
sex_value = 0 if sex == "Male" else 1

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Survival"):

    input_data = pd.DataFrame(
        [[pclass, sex_value, age, sibsp, parch, fare]],
        columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    # -----------------------------
    # Prediction Output
    # -----------------------------
    if prediction == 1:
        st.success("✅ Passenger Survived")
        st.balloons()
    else:
        st.error("❌ Passenger Did Not Survive")

    st.subheader("Prediction Confidence")

    st.progress(int(probability * 100))

    st.write(f"Survival Probability: **{probability*100:.2f}%**")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Machine Learning Titanic Classifier using Logistic Regression")