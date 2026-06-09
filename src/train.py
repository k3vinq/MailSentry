from __future__ import annotations

from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.preprocessing import MaxAbsScaler

from src.utils import load_config
from src.data_loader import load_dataset, normalize_labels
from src.preprocess import clean_text
from src.features import build_features
from src.evaluate import (
    save_confusion_matrix,
    print_classification_report,
    save_misclassified_samples,
)


def evaluate_model(name, model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    p, r, f1, _ = precision_recall_fscore_support(y_test, preds, average="binary", zero_division=0)
    return {"model": name, "accuracy": acc, "precision": p, "recall": r, "f1": f1}, preds


def main():
    cfg = load_config()
    ds = cfg["dataset"]
    feats = cfg["features"]
    tr = cfg["training"]

    df = load_dataset(ds["path"], ds["text_column"], ds["label_column"])
    df = normalize_labels(df, ds["label_column"], ds["positive_labels"])

    # Keep a copy of raw text for heuristic features (uppercase_ratio, etc.)
    raw_text_col = "__raw_text__"
    df[raw_text_col] = df[ds["text_column"]].copy()

    # Clean text for TF-IDF
    df[ds["text_column"]] = df[ds["text_column"]].map(clean_text)

    X_train_clean, X_test_clean, y_train, y_test, X_train_raw, X_test_raw = train_test_split(
        df[ds["text_column"]].tolist(),
        df[ds["label_column"]].tolist(),
        df[raw_text_col].tolist(),
        test_size=tr["test_size"],
        random_state=tr["random_state"],
        stratify=df[ds["label_column"]].tolist(),
    )

    X_train, X_test, vectorizer = build_features(
        X_train_clean,
        X_test_clean,
        feats["suspicious_keywords"],
        max_features=feats["tfidf_max_features"],
        ngram_range=tuple(feats["tfidf_ngram_range"]),
        train_texts_raw=X_train_raw,
        test_texts_raw=X_test_raw,
    )

    scaler = MaxAbsScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        "naive_bayes": MultinomialNB(),
        "logistic_regression": LogisticRegression(max_iter=3000),
        "linear_svm": LinearSVC(),
    }

    results = []
    Path("models").mkdir(exist_ok=True)
    Path("reports/evaluation").mkdir(parents=True, exist_ok=True)
    Path("reports/error_analysis").mkdir(parents=True, exist_ok=True)

    for name, model in models.items():
        model.fit(X_train, y_train)
        metrics, preds = evaluate_model(name, model, X_test, y_test)
        results.append(metrics)
        joblib.dump(model, f"models/{name}.joblib")

        # Save confusion matrix and classification report for each model
        save_confusion_matrix(y_test, preds, output_path=f"reports/evaluation/confusion_matrix_{name}.png")
        print(f"\n--- {name} ---")
        print_classification_report(y_test, preds)

        # Save misclassified samples for error analysis
        save_misclassified_samples(y_test, preds, X_test_raw, output_path=f"reports/error_analysis/error_analysis_{name}.md")

    joblib.dump(vectorizer, "models/vectorizer.joblib")
    joblib.dump(scaler, "models/scaler.joblib")

    print("\n" + "=" * 60)
    print("Training complete. Summary:")
    print("=" * 60)
    for row in results:
        print(row)

    # Save results to file
    with open("results.md", "w", encoding="utf-8") as f:
        f.write("# Training Results\n\n")
        f.write("| Model | Accuracy | Precision | Recall | F1 |\n")
        f.write("|---|---|---|---|---|\n")
        for row in results:
            f.write(f"| {row['model']} | {row['accuracy']:.4f} | {row['precision']:.4f} | {row['recall']:.4f} | {row['f1']:.4f} |\n")
        f.write("\nConfusion matrices saved in `reports/evaluation/` folder.\n")


if __name__ == "__main__":
    main()
