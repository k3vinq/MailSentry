"""PyTorch Dataset wrapper for DistilBERT fine-tuning on phishing email data."""

from __future__ import annotations

import torch
from torch.utils.data import Dataset


class PhishingDataset(Dataset):
    """Tokenizes email texts and wraps them for the HuggingFace Trainer.

    Unlike the classical ML pipeline (which needs TF-IDF + heuristic features),
    BERT-based models learn features directly from raw token sequences, so we
    only need input_ids and attention_mask.
    """

    def __init__(self, texts: list[str], labels: list[int], tokenizer, max_length: int = 512):
        self.encodings = tokenizer(
            texts,
            truncation=True,
            padding=True,
            max_length=max_length,
            return_tensors="pt",
        )
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __getitem__(self, idx: int):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item["labels"] = self.labels[idx]
        return item

    def __len__(self) -> int:
        return len(self.labels)
