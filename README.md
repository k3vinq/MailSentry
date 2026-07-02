# MailSentry: Text-Based Phishing Email Detection

A comprehensive course project for CS221 (Natural Language Processing) that detects phishing emails using **Transformer-based Deep Learning** (DistilBERT).

## Features
- **Deep Learning Pipeline**: Fine-tunes a `distilbert-base-uncased` transformer model to classify raw email sequences directly.
- **Web App**: An interactive Streamlit demo application that allows users to paste email text and get real-time predictions along with confidence scores.

## Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
*(Note: If you plan to train DistilBERT on a GPU, please install PyTorch with the correct CUDA version manually).*

## Usage

### 1. Run the Web Application
Launch the interactive Streamlit app to test models:
```bash
streamlit run app/streamlit_app.py
```

### 2. Predict from Command Line
Predict a single email text using the CLI:
```bash
python -m src.predict "URGENT! Please verify your account immediately."
```

### 3. Training Models

**Train DistilBERT:**
To train the Transformer model (GPU highly recommended):
```bash
python -m src.train_bert
```

## Project Structure
- `app/`: Streamlit web application.
- `configs/`: Hyperparameters configuration.
- `data/`: Dataset (`Phishing_Email.csv`).
- `models/`: Saved DistilBERT model directory.
- `reports/`: Evaluation metrics, error analysis, and Final Report Structure.
- `src/`: Core Python modules for data loading, preprocessing, and model training.

## Evaluation
The **DistilBERT** model achieved excellent performance on the test set:
- **Accuracy**: 97.77%
- **F1-score**: 97.20%

Confusion matrices and misclassified samples are automatically saved to the `reports/` folder during training for detailed error analysis.

