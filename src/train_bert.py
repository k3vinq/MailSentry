"""Fine-tune DistilBERT for phishing email classification.

Usage (local):
    python -m src.train_bert

Usage (Slurm):
    sbatch train_bert.sh   # see example script below

The script reuses the same data-loading and evaluation utilities as the
classical ML pipeline, so results are directly comparable.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)
from sklearn.model_selection import train_test_split
from transformers import (
    DistilBertForSequenceClassification,
    DistilBertTokenizerFast,
    Trainer,
    TrainingArguments,
)

from src.utils import load_config
from src.data_loader import load_dataset, normalize_labels
from src.evaluate import (
    save_confusion_matrix,
    print_classification_report,
    save_misclassified_samples,
)
from src.dataset_bert import PhishingDataset


# ---------------------------------------------------------------------------
# Metrics callback for HuggingFace Trainer
# ---------------------------------------------------------------------------

def compute_metrics(eval_pred):
    """Compute accuracy, precision, recall, F1 for the Trainer."""
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = accuracy_score(labels, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, preds, average="binary", zero_division=0
    )
    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    cfg = load_config()
    ds = cfg["dataset"]
    tr = cfg["training"]
    tf_cfg = cfg["transformer"]

    # ------------------------------------------------------------------
    # 1. Load & split data (identical split as classical ML pipeline)
    # ------------------------------------------------------------------
    df = load_dataset(ds["path"], ds["text_column"], ds["label_column"])
    df = normalize_labels(df, ds["label_column"], ds["positive_labels"])

    texts = df[ds["text_column"]].tolist()
    labels = df[ds["label_column"]].tolist()

    X_train_texts, X_test_texts, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=tr["test_size"],
        random_state=tr["random_state"],
        stratify=labels,
    )

    print(f"Train size: {len(X_train_texts)}, Test size: {len(X_test_texts)}")
    print(f"Label distribution (train): {sum(y_train)} phishing / {len(y_train) - sum(y_train)} safe")

    # ------------------------------------------------------------------
    # 2. Tokenize
    # ------------------------------------------------------------------
    model_name = tf_cfg["model_name"]
    max_length = tf_cfg["max_length"]
    print(f"\nLoading tokenizer: {model_name}")
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

    train_dataset = PhishingDataset(X_train_texts, y_train, tokenizer, max_length=max_length)
    test_dataset = PhishingDataset(X_test_texts, y_test, tokenizer, max_length=max_length)

    # ------------------------------------------------------------------
    # 3. Model
    # ------------------------------------------------------------------
    print("Loading pre-trained model...")
    model = DistilBertForSequenceClassification.from_pretrained(
        model_name,
        num_labels=2,
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")
    if device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f} GB")

    # ------------------------------------------------------------------
    # 4. Training arguments
    # ------------------------------------------------------------------
    output_dir = tf_cfg["output_dir"]
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path("reports/evaluation").mkdir(parents=True, exist_ok=True)
    Path("reports/error_analysis").mkdir(parents=True, exist_ok=True)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=tf_cfg["epochs"],
        per_device_train_batch_size=tf_cfg["batch_size"],
        per_device_eval_batch_size=tf_cfg["batch_size"] * 2,
        learning_rate=tf_cfg["learning_rate"],
        weight_decay=tf_cfg["weight_decay"],
        warmup_steps=tf_cfg["warmup_steps"],
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        logging_steps=50,
        report_to="none",  # disable wandb / tensorboard
        fp16=torch.cuda.is_available(),  # mixed precision on GPU
        seed=tr["random_state"],
    )

    # ------------------------------------------------------------------
    # 5. Train
    # ------------------------------------------------------------------
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        compute_metrics=compute_metrics,
    )

    print("\n" + "=" * 60)
    print("Starting DistilBERT fine-tuning...")
    print("=" * 60)
    trainer.train()

    # ------------------------------------------------------------------
    # 6. Evaluate
    # ------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("Evaluating on test set...")
    print("=" * 60)
    eval_results = trainer.evaluate()
    print(f"Results: {eval_results}")

    # Get predictions for detailed analysis
    predictions = trainer.predict(test_dataset)
    preds = np.argmax(predictions.predictions, axis=-1)

    # Classification report
    print_classification_report(y_test, preds)

    # Confusion matrix
    save_confusion_matrix(
        y_test, preds,
        output_path="reports/evaluation/confusion_matrix_distilbert.png",
    )

    # Error analysis
    save_misclassified_samples(
        y_test, preds, X_test_texts,
        output_path="reports/error_analysis/error_analysis_distilbert.md",
    )

    # ------------------------------------------------------------------
    # 7. Save model & tokenizer
    # ------------------------------------------------------------------
    print(f"\nSaving model to {output_dir}/")
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)

    # ------------------------------------------------------------------
    # 8. Append results to results.md
    # ------------------------------------------------------------------
    acc = accuracy_score(y_test, preds)
    p, r, f1, _ = precision_recall_fscore_support(y_test, preds, average="binary", zero_division=0)

    with open("results.md", "a", encoding="utf-8") as f:
        f.write(f"\n| distilbert | {acc:.4f} | {p:.4f} | {r:.4f} | {f1:.4f} |\n")

    print("\n" + "=" * 60)
    print("DistilBERT training complete!")
    print(f"  Accuracy:  {acc:.4f}")
    print(f"  Precision: {p:.4f}")
    print(f"  Recall:    {r:.4f}")
    print(f"  F1-score:  {f1:.4f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
