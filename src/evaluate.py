from __future__ import annotations

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix


def save_confusion_matrix(y_true, y_pred, output_path: str = "reports/confusion_matrix.png"):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    fig, ax = plt.subplots(figsize=(5, 5))
    disp.plot(ax=ax)
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def print_classification_report(y_true, y_pred):
    print(classification_report(y_true, y_pred, digits=4))
