from __future__ import annotations

import argparse
import joblib
from scipy.sparse import csr_matrix, hstack

from src.preprocess import clean_text
from src.features import extract_heuristic_features
from src.utils import load_config


def main():
    parser = argparse.ArgumentParser(description="Predict phishing from email text.")
    parser.add_argument("text", type=str, help="Email text to classify")
    parser.add_argument("--model", default="models/logistic_regression.joblib")
    args = parser.parse_args()

    cfg = load_config()
    suspicious_keywords = cfg["features"]["suspicious_keywords"]

    vectorizer = joblib.load("models/vectorizer.joblib")
    model = joblib.load(args.model)

    text = clean_text(args.text)
    X_text = vectorizer.transform([text])
    X_h = csr_matrix(extract_heuristic_features([text], suspicious_keywords))
    X = hstack([X_text, X_h])

    pred = model.predict(X)[0]
    print("Prediction:", "phishing" if pred == 1 else "safe")


if __name__ == "__main__":
    main()
