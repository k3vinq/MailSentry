# Architecture

## 1. Project Goal
Build a course-project system for **text-based phishing email detection** using modern NLP techniques. The system demonstrates the use of a **Transformer-based model** (DistilBERT) for text classification.

## 2. Project Title
**Text-Based Phishing Email Detection Using DistilBERT**

## 3. High-Level Pipeline

```text
Dataset / Raw Email Text
        |
        v
Data Loading and Validation
        |
        v
  Text Preprocessing
        |
        v
  Tokenization
  (DistilBertTokenizer)
        |
        v
  DistilBERT
  Fine-tuning
        |
        v
  Classification
  Head Training
        |
        v
  Evaluation
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

**Important design note**
Do not over-clean the text. Some phishing indicators such as `http`, `verify`, `urgent`, and unusual punctuation can be useful context for the transformer model.

### 4.3 Model Layer — Transformer (DistilBERT)
Fine-tune a pre-trained **DistilBERT** (`distilbert-base-uncased`) model for sequence classification.

**Key features**
- BERT learns features directly from raw tokens.
- Uses HuggingFace `Trainer` API with `DistilBertForSequenceClassification`.
- Training config: 3 epochs, lr=2e-5, batch_size=16, max_length=512, fp16 mixed precision.
- Model saved to `models/distilbert/` (config.json + model.safetensors + tokenizer files).

**Why DistilBERT?**
- 40% smaller than BERT, 60% faster, retains 97% performance.
- Demonstrates understanding of Transformer architecture in an NLP course.
- Fine-tuning on 18K samples takes ~5-15 minutes on GPU (L40/A100).

### 4.4 Evaluation Layer
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
- Confusion matrix plot
- Classification report
- Error analysis examples

### 4.5 Demo Layer
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
│   └── streamlit_app.py         # Demo app
├── configs/
│   └── settings.yaml            # All hyperparameters
├── data/
│   └── Phishing_Email.csv
├── models/
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
│   ├── preprocess.py            # Text cleaning
│   ├── train_bert.py            # DistilBERT fine-tuning
│   ├── dataset_bert.py          # PyTorch Dataset for BERT
│   ├── evaluate.py              # Metrics, confusion matrix, error analysis
│   ├── predict.py               # Prediction
│   └── utils.py                 # Config loader
├── architecture.md
├── requirements.txt
└── README.md
```

## 6. Design Rationale
This architecture intentionally uses:
- the **experimental clarity** of a Kaggle workflow,
- and the **advanced contextual embeddings** provided by a DistilBERT Transformer.

It is not meant to be production-grade. It is meant to be:
- understandable,
- reproducible,
- defensible in a course presentation,
- and feasible within a student timeline.

## 7. Development Strategy
1. Start with Data Exploration and preprocessing.
2. Fine-tune DistilBERT on the dataset.
3. Build Streamlit demo.
4. Write report and slides around the pipeline evaluation.

## 8. Final Scope

> A modular NLP-based phishing email detection system using a fine-tuned DistilBERT Transformer, demonstrating modern deep learning approaches to text classification.
