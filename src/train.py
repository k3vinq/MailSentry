from __future__ import annotations

from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

from src.utils import load_config
from src.data_loader import load_dataset, normalize_labels
from src.preprocess import clean_text
from src.features import build_features


def evaluate_model(name, model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    p, r, f1, _ = precision_recall_fscore_support(y_test, preds, average="binary", zero_division=0)
    return {"model": name, "accuracy": acc, "precision": p, "recall": r, "f1": f1}


def main():
    cfg = load_config()
    ds = cfg["dataset"]
    feats = cfg["features"]
    tr = cfg["training"]

    df = load_dataset(ds["path"], ds["text_column"], ds["label_column"])
    df = normalize_labels(df, ds["label_column"], ds["positive_labels"])
    df[ds["text_column"]] = df[ds["text_column"]].map(clean_text)

    X_train_text, X_test_text, y_train, y_test = train_test_split(
        df[ds["text_column"]].tolist(),
        df[ds["label_column"]].tolist(),
        test_size=tr["test_size"],
        random_state=tr["random_state"],
        stratify=df[ds["label_column"]].tolist(),
    )

    X_train, X_test, vectorizer = build_features(
        X_train_text,
        X_test_text,
        feats["suspicious_keywords"],
        max_features=feats["tfidf_max_features"],
        ngram_range=tuple(feats["tfidf_ngram_range"]),
    )

    models = {
        "naive_bayes": MultinomialNB(),
        "logistic_regression": LogisticRegression(max_iter=1000),
        "linear_svm": LinearSVC(),
    }

    results = []
    Path("models").mkdir(exist_ok=True)
    for name, model in models.items():
        model.fit(X_train, y_train)
        results.append(evaluate_model(name, model, X_test, y_test))
        joblib.dump(model, f"models/{name}.joblib")

    joblib.dump(vectorizer, "models/vectorizer.joblib")

    print("Training complete. Results:")
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
