# Tasks

## 1. Project Setup
- [ ] Create project folders: `src/`, `data/`, `models/`, `app/`, `reports/`, `notebooks/`.
- [ ] Create Python virtual environment.
- [ ] Install dependencies from `requirements.txt`.
- [ ] Confirm notebook or script runs locally.

## 2. Dataset Preparation
- [ ] Choose final dataset.
- [ ] Verify whether labels represent phishing/safe or spam/ham.
- [ ] Place dataset inside `data/`.
- [ ] Document dataset source in README.
- [ ] Inspect missing values.
- [ ] Inspect duplicate rows.
- [ ] Check class distribution.

## 3. Exploratory Data Analysis
- [ ] Count samples per class.
- [ ] Measure average email length.
- [ ] Inspect common words or phrases.
- [ ] Identify potential phishing-related keywords.
- [ ] Save a few visualizations for the report.

## 4. Text Preprocessing
- [ ] Implement text cleaning function.
- [ ] Normalize casing and spacing.
- [ ] Decide whether to remove stopwords.
- [ ] Decide whether to keep punctuation and URLs.
- [ ] Test preprocessing on a few sample emails.

## 5. Feature Engineering

### 5.1 Baseline Text Features
- [ ] Build TF-IDF unigram baseline.
- [ ] Build TF-IDF unigram + bigram variant.
- [ ] Compare both settings.

### 5.2 Heuristic Phishing Features
- [ ] Count URLs.
- [ ] Count suspicious keywords.
- [ ] Count exclamation marks.
- [ ] Compute uppercase ratio.
- [ ] Compute digit ratio.
- [ ] Measure email length.
- [ ] Combine all handcrafted features into a numeric matrix.

### 5.3 Feature Fusion
- [ ] Merge TF-IDF and heuristic features.
- [ ] Verify feature shapes.
- [ ] Save feature configuration for reproducibility.

## 6. Model Training
- [ ] Train Multinomial Naive Bayes baseline.
- [ ] Train Logistic Regression.
- [ ] Train Linear SVM.
- [ ] Optionally train Random Forest or XGBoost.
- [ ] Save trained models.

## 7. Evaluation
- [ ] Compute accuracy.
- [ ] Compute precision.
- [ ] Compute recall.
- [ ] Compute F1-score.
- [ ] Plot confusion matrix.
- [ ] Generate classification report.
- [ ] Build model comparison table.
- [ ] Analyze false positives.
- [ ] Analyze false negatives.

## 8. Model Selection
- [ ] Compare baseline and improved pipelines.
- [ ] Choose final model based on metrics and explainability.
- [ ] Justify why the selected model is best for the project scope.

## 9. Prediction Demo
- [ ] Implement `predict.py`.
- [ ] Add a simple CLI example.
- [ ] Build a small Streamlit app.
- [ ] Test prediction on custom email text.

## 10. Documentation
- [ ] Write project overview in `README.md`.
- [ ] Explain dataset source and label meaning.
- [ ] Explain preprocessing decisions.
- [ ] Explain feature engineering choices.
- [ ] Explain model comparison results.
- [ ] Add instructions for running training and demo.

## 11. Report Preparation
- [ ] Write introduction and problem statement.
- [ ] Define phishing email detection scope clearly.
- [ ] Include architecture diagram.
- [ ] Include methodology section.
- [ ] Include results and discussion.
- [ ] Include limitations and future work.

## 12. Presentation Preparation
- [ ] Create 8–12 slide presentation.
- [ ] Add problem motivation.
- [ ] Add architecture diagram.
- [ ] Add dataset summary.
- [ ] Add model comparison results.
- [ ] Add demo screenshots.
- [ ] Prepare answers for likely questions from lecturer.

## 13. Likely Lecturer Questions to Prepare For
- [ ] Why is this phishing detection and not only spam detection?
- [ ] Why did you choose TF-IDF instead of embeddings?
- [ ] Why did you compare these three models?
- [ ] Which metric matters most and why?
- [ ] What are the limitations of using only email text?
- [ ] How could the system be improved in future work?

## 14. Minimum Viable Submission
If time is limited, finish these first:
- [ ] Clean dataset
- [ ] TF-IDF features
- [ ] Naive Bayes + Logistic Regression + Linear SVM
- [ ] Evaluation metrics and confusion matrix
- [ ] Small prediction demo
- [ ] Clear README and report outline
