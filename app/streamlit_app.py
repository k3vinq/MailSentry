from __future__ import annotations

import joblib
import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from scipy.sparse import csr_matrix, hstack

from src.preprocess import clean_text
from src.features import extract_heuristic_features
from src.utils import load_config

st.set_page_config(page_title="Phishing Email Detector", page_icon="🛡️")
st.title("🛡️ Phishing Email Detector")
st.write("Paste an email body below to get a prediction.")

cfg = load_config()
keywords = cfg["features"]["suspicious_keywords"]


model_options = {
    "Logistic Regression (Best Overall)": "logistic_regression",
    "Linear SVM": "linear_svm",
    "Naive Bayes (Baseline)": "naive_bayes",
}
selected_model_label = st.selectbox("Select Model", list(model_options.keys()))


@st.cache_resource
def load_assets(model_filename: str):
    vectorizer = joblib.load("models/vectorizer.joblib")
    scaler = joblib.load("models/scaler.joblib")
    model = joblib.load(f"models/{model_filename}.joblib")
    return vectorizer, scaler, model


text = st.text_area("Email text", height=220)

if st.button("Predict"):
    if not text.strip():
        st.warning("Please paste some email text first.")
    else:
        vectorizer, scaler, model = load_assets(model_options[selected_model_label])

        # TF-IDF uses cleaned (lowercased) text
        cleaned = clean_text(text)
        X_text = vectorizer.transform([cleaned])

        # Heuristic features use RAW text (preserves uppercase_ratio signal)
        X_h = csr_matrix(extract_heuristic_features([text], keywords))

        X = hstack([X_text, X_h])
        X = scaler.transform(X)
        pred = model.predict(X)[0]

        if pred == 1:
            st.error("⚠️ Prediction: **PHISHING**")
        else:
            st.success("✅ Prediction: **Safe Email**")
