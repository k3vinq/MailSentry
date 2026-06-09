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

# ---------------------------------------------------------------
# Model selector — Classical ML + DistilBERT
# ---------------------------------------------------------------
model_options = {
    "DistilBERT (Transformer)": "distilbert",
    "Logistic Regression": "logistic_regression",
    "Linear SVM": "linear_svm",
    "Naive Bayes (Baseline)": "naive_bayes",
}
selected_model_label = st.selectbox("Select Model", list(model_options.keys()))
is_bert = model_options[selected_model_label] == "distilbert"


# ---------------------------------------------------------------
# Asset loaders (cached)
# ---------------------------------------------------------------
@st.cache_resource
def load_classical_assets(model_filename: str):
    vectorizer = joblib.load("models/vectorizer.joblib")
    scaler = joblib.load("models/scaler.joblib")
    model = joblib.load(f"models/{model_filename}.joblib")
    return vectorizer, scaler, model


@st.cache_resource
def load_bert_assets(model_dir: str = "models/distilbert"):
    import torch
    from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast

    tokenizer = DistilBertTokenizerFast.from_pretrained(model_dir)
    model = DistilBertForSequenceClassification.from_pretrained(model_dir)
    model.eval()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    return tokenizer, model, device


# ---------------------------------------------------------------
# Email input
# ---------------------------------------------------------------
text = st.text_area("Email text", height=220)

if st.button("Predict"):
    if not text.strip():
        st.warning("Please paste some email text first.")
    elif is_bert:
        # ---------- DistilBERT inference ----------
        import torch

        tokenizer, model, device = load_bert_assets()
        max_length = cfg.get("transformer", {}).get("max_length", 512)

        encoding = tokenizer(
            text,
            truncation=True,
            padding=True,
            max_length=max_length,
            return_tensors="pt",
        )
        encoding = {k: v.to(device) for k, v in encoding.items()}

        with torch.no_grad():
            outputs = model(**encoding)
            probs = torch.softmax(outputs.logits, dim=-1)
            pred = torch.argmax(probs, dim=-1).item()
            confidence = probs[0][pred].item()

        if pred == 1:
            st.error(f"⚠️ Prediction: **PHISHING** (confidence: {confidence:.1%})")
        else:
            st.success(f"✅ Prediction: **Safe Email** (confidence: {confidence:.1%})")
    else:
        # ---------- Classical ML inference ----------
        vectorizer, scaler, model = load_classical_assets(model_options[selected_model_label])

        cleaned = clean_text(text)
        X_text = vectorizer.transform([cleaned])
        X_h = csr_matrix(extract_heuristic_features([text], keywords))
        X = hstack([X_text, X_h])
        X = scaler.transform(X)
        pred = model.predict(X)[0]

        if pred == 1:
            st.error("⚠️ Prediction: **PHISHING**")
        else:
            st.success("✅ Prediction: **Safe Email**")

