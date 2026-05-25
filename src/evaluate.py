from __future__ import annotations

import matplotlib.pyplot as plt
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    classification_report,
    confusion_matrix,
)


def save_confusion_matrix(
    y_true,
    y_pred,
    output_path: str = "reports/confusion_matrix.png",
    labels: list | None = None,
    display_labels: list[str] | None = None,
):
    """Save a confusion matrix plot to disk."""
    if display_labels is None:
        display_labels = ["Safe", "Phishing"]
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=display_labels)
    fig, ax = plt.subplots(figsize=(5, 5))
    disp.plot(ax=ax, cmap="Blues")
    ax.set_title(output_path.split("/")[-1].replace(".png", "").replace("_", " ").title())
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Confusion matrix saved to {output_path}")


def print_classification_report(y_true, y_pred):
    """Print a detailed classification report."""
    print(classification_report(y_true, y_pred, target_names=["Safe", "Phishing"], digits=4))


def save_misclassified_samples(y_true, y_pred, raw_texts: list[str], output_path: str, max_samples: int = 15):
    """Save False Positives and False Negatives to a markdown file for error analysis."""
    fps = []
    fns = []
    for i, (true, pred) in enumerate(zip(y_true, y_pred)):
        if true == 0 and pred == 1:
            fps.append(raw_texts[i])
        elif true == 1 and pred == 0:
            fns.append(raw_texts[i])
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Error Analysis: {output_path.split('/')[-1].replace('.md', '')}\n\n")
        
        f.write(f"## False Positives (Actual: Safe -> Predicted: Phishing)\n")
        f.write(f"*Total False Positives in test set: {len(fps)}*\n\n")
        for i, text in enumerate(fps[:max_samples]):
            f.write(f"### Sample FP #{i+1}\n```text\n{text}\n```\n\n")
            
        f.write(f"## False Negatives (Actual: Phishing -> Predicted: Safe)\n")
        f.write(f"*Total False Negatives in test set: {len(fns)}*\n\n")
        for i, text in enumerate(fns[:max_samples]):
            f.write(f"### Sample FN #{i+1}\n```text\n{text}\n```\n\n")
    
    print(f"Error analysis saved to {output_path}")
