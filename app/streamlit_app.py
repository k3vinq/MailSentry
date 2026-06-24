from __future__ import annotations

import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.utils import load_config

st.set_page_config(page_title="Phishing Email Detector", page_icon="🛡️")
st.title("🛡️ Phishing Email Detector")
st.write("Paste an email body below to get a prediction.")

cfg = load_config()

# ---------------------------------------------------------------
# Asset loaders (cached)
# ---------------------------------------------------------------
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
    else:
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

