# Architecture

## 1. Project Goal
Build a course-project system for **text-based phishing email detection** using NLP and classical machine learning. The system should be simple enough to implement in a limited academic timeline, but structured enough to demonstrate sound software and ML design.

## 2. Recommended Project Title
**Text-Based Phishing Email Detection Using NLP and Machine Learning**

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
Feature Engineering
   |                |
   |                +--> Heuristic phishing indicators
   |
   +--------------------> TF-IDF text features
        |
        v
Feature Fusion
        |
        v
Model Training and Comparison
        |
        v
Evaluation and Error Analysis
        |
        v
Prediction Demo / Small App
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

### 4.5 Model Layer
Train and compare several classical ML models.

**Recommended baseline and comparison models**
- Multinomial Naive Bayes
- Logistic Regression
- Linear SVM

**Optional extensions**
- Random Forest
- XGBoost

For a course project, the first three are already a strong and defensible set.

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

## 5. Proposed Repository Structure

```text
project/
├── app/
│   └── streamlit_app.py
├── configs/
│   └── settings.yaml
├── data/
│   └── README.md
├── models/
│   └── README.md
├── notebooks/
│   └── exploration.ipynb
├── reports/
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── utils.py
├── architecture.md
├── tasks.md
├── README.md
└── requirements.txt
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

## 7. Suggested Development Strategy
1. Start with TF-IDF + Naive Bayes baseline.
2. Add Logistic Regression and Linear SVM.
3. Add handcrafted phishing features.
4. Compare results.
5. Build a small prediction demo.
6. Write report and slides around the final pipeline.

## 8. What to Avoid
- Using too many models without explanation.
- Claiming “full phishing detection” if only email body text is used.
- Overcomplicating the project with deep learning unless clearly justified.
- Submitting only a messy notebook without modular code.

## 9. Final Recommended Scope
A strong final scope for this course project is:

> A modular NLP-based phishing email detection system using TF-IDF text features, phishing-specific heuristic indicators, and comparative evaluation of classical machine learning models.
