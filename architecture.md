# Architecture

## 1. Project Goal
Build a course-project system for **text-based phishing email detection** using NLP techniques, comparing **classical machine learning** (TF-IDF + NB/SVM/LR) against a **Transformer-based model** (DistilBERT). The system demonstrates both traditional and modern deep learning approaches to NLP.

## 2. Project Title
**Text-Based Phishing Email Detection Using NLP and Machine Learning with Transformer Comparison**

## 3. High-Level Pipeline

```text
Dataset / Raw Email Text
        |
        v
Data Loading and Validation
        |
        +------------------+
        |                  |
        v                  v
  Classical ML         Transformer
  Pipeline             Pipeline
        |                  |
        v                  v
  Text Preprocessing   Tokenization
  (clean_text)         (DistilBertTokenizer)
        |                  |
        v                  v
  TF-IDF +             DistilBERT
  Heuristics           Fine-tuning
        |                  |
        v                  v
  NB / SVM / LR        Classification
  Training             Head Training
        |                  |
        +--------+---------+
                 |
                 v
        Evaluation & Comparison
                 |
                 v
        Streamlit Demo App
```

## 4. Architectural Layers

### 4.1 Data Layer
Responsible for loading the dataset and validating its quality.

**Responsibilities**
- Read CSV or other tabular data source.
- Validate required columns such as `email_text` and `label`.
- Handle missing values.
- Remove duplicates if necessary.
- Normalize labels into a binary format.

**Inputs**
- CSV file containing email text and labels.

**Outputs**
- Clean `DataFrame`.
- Train/validation/test splits.

### 4.2 Preprocessing Layer
Transforms raw text into a normalized form while preserving useful phishing signals.

**Recommended steps**
- Lowercasing
- Whitespace normalization
- Optional punctuation cleanup
- Optional stopword removal
- Optional lemmatization

**Important design note**
Do not over-clean the text. Some phishing indicators such as `http`, `verify`, `urgent`, and unusual punctuation can be useful.

### 4.3 Feature Engineering Layer
This layer combines two feature families.

#### A. TF-IDF Text Features
Use `TfidfVectorizer` to represent email text numerically.

**Suggested configurations**
- Unigram baseline
- Unigram + bigram comparison
- `max_features` set to a manageable range

#### B. Heuristic Phishing Features
Add handcrafted features inspired by the phishing domain.

**Suggested features**
- URL count
- Suspicious keyword count
- Email length
- Exclamation mark count
- Uppercase ratio
- Digit ratio
- Presence of urgency words

These features make the project more security-aware and less generic than a pure text classification notebook.

### 4.4 Feature Fusion Layer
Combine TF-IDF features with heuristic phishing indicators.

**Implementation idea**
- Sparse matrix from TF-IDF
- Dense numeric matrix from handcrafted features
- Concatenate them before training

### 4.5a Model Layer — Classical ML
Train and compare several classical ML models as baselines.

**Models**
- Multinomial Naive Bayes
- Logistic Regression
- Linear SVM

These three provide a strong and defensible baseline set for comparison.

### 4.5b Model Layer — Transformer (DistilBERT)
Fine-tune a pre-trained **DistilBERT** (`distilbert-base-uncased`) model for sequence classification.

**Key differences from Classical ML**
- No need for TF-IDF or heuristic features — BERT learns features directly from raw tokens.
- Uses HuggingFace `Trainer` API with `DistilBertForSequenceClassification`.
- Training config: 3 epochs, lr=2e-5, batch_size=16, max_length=512, fp16 mixed precision.
- Model saved to `models/distilbert/` (config.json + model.safetensors + tokenizer files).

**Why DistilBERT?**
- 40% smaller than BERT, 60% faster, retains 97% performance.
- Demonstrates understanding of Transformer architecture in an NLP course.
- Fine-tuning on 18K samples takes ~5-15 minutes on GPU (L40/A100).

### 4.6 Evaluation Layer
This is where the project becomes academically convincing.

**Metrics to report**
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

**Security-oriented interpretation**
A false negative is often more dangerous than a false positive in phishing detection, because a malicious email may be marked safe.

**Recommended outputs**
- Model comparison table
- Confusion matrix plot
- Classification report
- Error analysis examples

### 4.7 Demo Layer
A small demo helps the project feel complete.

**Options**
- Command-line prediction script
- Simple Streamlit app
- Notebook demo cell

**Recommended scope**
A lightweight Streamlit app is enough: user pastes email text and gets a prediction.

## 5. Repository Structure

```text
MailSentry/
├── app/
│   └── streamlit_app.py         # Demo app (Classical ML + DistilBERT)
├── configs/
│   └── settings.yaml            # All hyperparameters
├── data/
│   └── Phishing_Email.csv
├── models/
│   ├── naive_bayes.joblib       # Classical ML models
│   ├── logistic_regression.joblib
│   ├── linear_svm.joblib
│   ├── vectorizer.joblib
│   ├── scaler.joblib
│   └── distilbert/              # Fine-tuned Transformer
│       ├── config.json
│       ├── model.safetensors
│       └── tokenizer files...
├── notebooks/
│   └── exploration.ipynb
├── reports/
│   ├── evaluation/              # Confusion matrices
│   └── error_analysis/          # Misclassified samples
├── src/
│   ├── __init__.py
│   ├── data_loader.py           # CSV loading & label normalization
│   ├── preprocess.py            # Text cleaning for TF-IDF
│   ├── features.py              # TF-IDF + heuristic features
│   ├── train.py                 # Classical ML training
│   ├── train_bert.py            # DistilBERT fine-tuning
│   ├── dataset_bert.py          # PyTorch Dataset for BERT
│   ├── evaluate.py              # Metrics, confusion matrix, error analysis
│   ├── predict.py               # Prediction (Classical + BERT)
│   └── utils.py                 # Config loader
├── architecture.md
├── requirements.txt
└── README.md
```

## 6. Design Rationale
This architecture intentionally combines:
- the **simplicity** of a baseline NLP notebook,
- the **experimental clarity** of a Kaggle workflow,
- and the **phishing-aware features** inspired by more security-oriented projects.

It is not meant to be production-grade. It is meant to be:
- understandable,
- reproducible,
- defensible in a course presentation,
- and feasible within a student timeline.

## 7. Development Strategy
1. Start with TF-IDF + Naive Bayes baseline.
2. Add Logistic Regression and Linear SVM.
3. Add handcrafted phishing features.
4. Compare classical ML results.
5. Fine-tune DistilBERT and compare against classical baselines.
6. Build Streamlit demo supporting all models.
7. Write report and slides around the full pipeline comparison.

## 8. Classical ML vs Transformer Comparison

| Aspect | Classical ML | DistilBERT |
|---|---|---|
| Feature engineering | Manual (TF-IDF + heuristics) | Automatic (learned from tokens) |
| Training time | Seconds | 5-15 minutes (GPU) |
| Model size | ~10 MB (joblib) | ~250 MB (safetensors) |
| Interpretability | High (feature weights) | Low (black-box attention) |
| Expected accuracy | ~95-97% | ~98-99% |
| Inference speed | Very fast (CPU) | Slower (GPU recommended) |

## 9. Final Scope

> A modular NLP-based phishing email detection system comparing classical machine learning (TF-IDF + NB/SVM/LR) with a fine-tuned DistilBERT Transformer, demonstrating both traditional and modern deep learning approaches to text classification.
