from __future__ import annotations

import re
import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import TfidfVectorizer


URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)


def extract_heuristic_features(texts: list[str], suspicious_keywords: list[str]) -> np.ndarray:
    """Extract handcrafted phishing indicator features.

    IMPORTANT: These texts should be the RAW (un-lowercased) texts so that
    uppercase_ratio can capture meaningful signal. If lowercased text is passed,
    uppercase_ratio will always be 0.
    """
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


def build_features(
    train_texts_clean: list[str],
    test_texts_clean: list[str],
    suspicious_keywords: list[str],
    max_features: int = 5000,
    ngram_range: tuple[int, int] = (1, 2),
    train_texts_raw: list[str] | None = None,
    test_texts_raw: list[str] | None = None,
):
    """Build combined TF-IDF + heuristic feature matrices.

    Args:
        train_texts_clean: Preprocessed (lowercased) training texts for TF-IDF.
        test_texts_clean: Preprocessed (lowercased) test texts for TF-IDF.
        suspicious_keywords: List of phishing indicator keywords.
        max_features: Maximum number of TF-IDF features.
        ngram_range: N-gram range for TF-IDF vectorizer.
        train_texts_raw: Original (un-lowercased) training texts for heuristic
            features. Falls back to train_texts_clean if not provided.
        test_texts_raw: Original (un-lowercased) test texts for heuristic
            features. Falls back to test_texts_clean if not provided.
    """
    # TF-IDF uses cleaned (lowercased) text
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range)
    X_train_tfidf = vectorizer.fit_transform(train_texts_clean)
    X_test_tfidf = vectorizer.transform(test_texts_clean)

    # Heuristic features use RAW text to preserve uppercase signals
    h_train_input = train_texts_raw if train_texts_raw is not None else train_texts_clean
    h_test_input = test_texts_raw if test_texts_raw is not None else test_texts_clean

    H_train = csr_matrix(extract_heuristic_features(h_train_input, suspicious_keywords))
    H_test = csr_matrix(extract_heuristic_features(h_test_input, suspicious_keywords))

    X_train = hstack([X_train_tfidf, H_train])
    X_test = hstack([X_test_tfidf, H_test])
    return X_train, X_test, vectorizer
