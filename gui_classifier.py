import streamlit as st
import pandas as pd
import joblib

# === Load model ===
model_path = "models/logistic_regression_tuned_fitted.joblib"
pipeline = joblib.load(model_path)

# === Feature list ===
feature_names = [
    'PF', 'ET', 'DFE', 'SB', 'PL', 'VR', 'HFS', 'RFS',
    'ANG', 'HT', 'HL', 'BT', 'FF', 'ERF', 'RQD', 'SR'
]

# === Title ===
st.title("Drillhole Classification Tool (Tuned Logistic Regression Model)")

# === Input form ===
st.subheader("Enter Drillhole Parameters:")
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"{feature}", format="%.2f")

# === Prediction logic ===
if st.button("Predict Class"):
    X_input = pd.DataFrame([input_data])
    prediction = pipeline.predict(X_input)[0]
    class_map = {0: "Balanced", 1: "Overbreak-Prone", 2: "Underbreak-Prone"}
    st.success(f"🧠 Predicted Class: **{class_map[prediction]}**")

    # Optional design warnings
    if input_data['DFE'] >= 2.0:
        st.warning("⚠️ DFE is large — risk of edge overbreak.")
    if input_data['PL'] > 2:
        st.warning("⚠️ Primer location may be too far from the end of the hole.")
    if input_data['HL'] < 4:
        st.warning("⚠️ Hole length is short — potential confinement issue.")
