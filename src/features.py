from __future__ import annotations

import re
import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import TfidfVectorizer


URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)


def extract_heuristic_features(texts: list[str], suspicious_keywords: list[str]) -> np.ndarray:
    rows = []
    for text in texts:
        t = text or ""
        lower = t.lower()
        url_count = len(URL_RE.findall(t))
        keyword_count = sum(lower.count(k) for k in suspicious_keywords)
        exclamation_count = t.count("!")
        uppercase_ratio = (sum(1 for ch in t if ch.isupper()) / max(len(t), 1))
        digit_ratio = (sum(1 for ch in t if ch.isdigit()) / max(len(t), 1))
        length = len(t)
        rows.append([url_count, keyword_count, exclamation_count, uppercase_ratio, digit_ratio, length])
    return np.asarray(rows, dtype=float)


def build_features(train_texts: list[str], test_texts: list[str], suspicious_keywords: list[str], max_features: int = 5000, ngram_range: tuple[int, int] = (1, 2)):
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range)
    X_train_tfidf = vectorizer.fit_transform(train_texts)
    X_test_tfidf = vectorizer.transform(test_texts)

    H_train = csr_matrix(extract_heuristic_features(train_texts, suspicious_keywords))
    H_test = csr_matrix(extract_heuristic_features(test_texts, suspicious_keywords))

    X_train = hstack([X_train_tfidf, H_train])
    X_test = hstack([X_test_tfidf, H_test])
    return X_train, X_test, vectorizer
