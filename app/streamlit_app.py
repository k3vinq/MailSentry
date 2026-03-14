from __future__ import annotations

import joblib
import streamlit as st
from scipy.sparse import csr_matrix, hstack

from src.preprocess import clean_text
from src.features import extract_heuristic_features
from src.utils import load_config

st.title("Phishing Email Detector")
st.write("Paste an email body below to get a prediction.")

cfg = load_config()
keywords = cfg["features"]["suspicious_keywords"]

@st.cache_resource
def load_assets():
    vectorizer = joblib.load("models/vectorizer.joblib")
    model = joblib.load("models/logistic_regression.joblib")
    return vectorizer, model

text = st.text_area("Email text", height=220)

if st.button("Predict"):
    if not text.strip():
        st.warning("Please paste some email text first.")
    else:
        vectorizer, model = load_assets()
        cleaned = clean_text(text)
        X_text = vectorizer.transform([cleaned])
        X_h = csr_matrix(extract_heuristic_features([cleaned], keywords))
        X = hstack([X_text, X_h])
        pred = model.predict(X)[0]
        st.success("Prediction: phishing" if pred == 1 else "Prediction: safe")
