from __future__ import annotations

import argparse
import joblib
from scipy.sparse import csr_matrix, hstack

from src.preprocess import clean_text
from src.features import extract_heuristic_features
from src.utils import load_config


def predict_email(raw_text: str, model_path: str = "models/logistic_regression.joblib") -> int:
    """Predict whether an email is phishing (1) or safe (0).

    Args:
        raw_text: The original email text (not preprocessed).
        model_path: Path to the trained model file.

    Returns:
        1 for phishing, 0 for safe.
    """
    cfg = load_config()
    suspicious_keywords = cfg["features"]["suspicious_keywords"]

    vectorizer = joblib.load("models/vectorizer.joblib")
    scaler = joblib.load("models/scaler.joblib")
    model = joblib.load(model_path)

    # TF-IDF uses cleaned text
    cleaned = clean_text(raw_text)
    X_text = vectorizer.transform([cleaned])

    # Heuristic features use RAW text (to preserve uppercase_ratio signal)
    X_h = csr_matrix(extract_heuristic_features([raw_text], suspicious_keywords))

    X = hstack([X_text, X_h])
    X = scaler.transform(X)
    return model.predict(X)[0]


def predict_email_bert(raw_text: str, model_dir: str = "models/distilbert") -> dict:
    """Predict phishing using the fine-tuned DistilBERT model.

    Args:
        raw_text: The original email text.
        model_dir: Path to the saved DistilBERT directory.

    Returns:
        dict with keys: 'label' (int), 'label_name' (str), 'confidence' (float).
    """
    import torch
    from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast

    tokenizer = DistilBertTokenizerFast.from_pretrained(model_dir)
    model = DistilBertForSequenceClassification.from_pretrained(model_dir)
    model.eval()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    cfg = load_config()
    max_length = cfg.get("transformer", {}).get("max_length", 512)

    encoding = tokenizer(
        raw_text,
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

    return {
        "label": pred,
        "label_name": "phishing" if pred == 1 else "safe",
        "confidence": confidence,
    }


def main():
    parser = argparse.ArgumentParser(description="Predict phishing from email text.")
    parser.add_argument("text", type=str, help="Email text to classify")
    parser.add_argument("--model", default="models/logistic_regression.joblib")
    parser.add_argument("--bert", action="store_true", help="Use DistilBERT model instead of classical ML")
    args = parser.parse_args()

    if args.bert:
        result = predict_email_bert(args.text)
        print(f"Prediction: {result['label_name']} (confidence: {result['confidence']:.2%})")
    else:
        pred = predict_email(args.text, args.model)
        print("Prediction:", "phishing" if pred == 1 else "safe")


if __name__ == "__main__":
    main()

