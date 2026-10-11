# Four-Algorithm Model Comparison — Member 3

**Project:** IT3091 Machine Learning — Telco Customer Churn  
**Source notebook:** `notebooks/07_model_comparison.ipynb`

## Comparison objective

Compare Logistic Regression, Random Forest, XGBoost, and Decision Tree under a shared training split and five-fold stratified CV. The primary evaluation criterion was **F1**, with **recall**, **Average Precision**, **ROC-AUC**, and **interpretability** considered alongside it. Identifying missed churners is important, but retention costs from false positives were not quantified.

## Preliminary historical comparison

The notebook first consolidated each member's previously produced reports into `reports/model_comparison_all.csv`. This table mixes pooled out-of-fold metrics, mean fold scores, nested validation, and exploratory thresholds, so it is **descriptive only** and must not be used as a fair ranking of candidate models.

## Standardized five-fold comparison

The next stage evaluated four specified candidate configurations on the same 5,634 training customers, with matching `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` splits. Pipelines applied preprocessing within folds.

| Model configuration | Accuracy | Precision | Recall | F1 | ROC-AUC | Average Precision |
|---|---:|---:|---:|---:|---:|---:|
| XGBoost | 0.7572 | 0.5289 | 0.7786 | **0.6298** | **0.8472** | **0.6704** |
| Balanced Logistic Regression | 0.7483 | 0.5167 | **0.8013** | 0.6281 | 0.8460 | 0.6599 |
| Balanced Decision Tree | 0.7423 | 0.5098 | 0.7806 | 0.6163 | 0.8296 | 0.6138 |
| Tuned Random Forest | **0.8056** | **0.6760** | 0.5157 | 0.5848 | 0.8462 | 0.6623 |

**Evidence:** `reports/model_comparison_standardized_cv.csv`.

The candidate settings had been chosen earlier using training-validation evidence. Accordingly, this standardized pass was a **consistent descriptive comparison**, not a fully independent nested estimate of model selection.

## Finalist comparison

XGBoost and balanced Logistic Regression were retained because their F1 results were nearly tied. Nested **threshold** validation used five outer folds and three inner folds to select a threshold within each outer training partition, then evaluated it on the outer validation fold. The underlying candidate hyperparameters remained fixed from earlier selection.

| Finalist | Mean F1 | F1 SD | Mean recall | ROC-AUC | Average Precision | Mean chosen threshold |
|---|---:|---:|---:|---:|---:|---:|
| Balanced Logistic Regression | 0.6354 | 0.0285 | 0.7458 | 0.8460 | 0.6599 | 0.57 |
| XGBoost | 0.6355 | 0.0162 | 0.7465 | 0.8472 | 0.6704 | 0.54 |

**Evidence:** `reports/finalist_nested_threshold_folds.csv` and `reports/finalist_nested_threshold_summary.csv`.

The mean F1 difference is roughly **0.00004**, not persuasive evidence of superiority. The standard deviations are descriptive; no statistical significance claim is made.

## Decision and limitations

Balanced Logistic Regression was selected pragmatically because its performance was essentially tied with XGBoost and its parameters are simpler to explain. The model-selection decision and threshold are documented in `docs/final_model_selection.md`.

The original Decision Tree workflow had inspected the held-out test data before correction. These earlier test results were excluded from model selection, but prior exposure must be disclosed in the final report. Candidate hyperparameters were not fully re-selected within the finalist threshold-validation outer folds, so residual selection bias remains.

**Figures:** `reports/model_comparison_preliminary.png`, `reports/model_comparison_all.png`. These illustrate the earlier heterogeneous comparison and should be labeled preliminary/descriptive.
