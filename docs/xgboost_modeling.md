# XGBoost Modeling — Member 3

**Project:** IT3091 Machine Learning — Telco Customer Churn  
**Group:** 2026-DS-37  
**Source notebook:** `notebooks/05_xgboost.ipynb`  
**Scope:** Training-set modeling and validation, not the final held-out test evaluation.

## Objective and data

XGBoost was developed as an advanced nonlinear alternative for predicting binary churn (`Churn`: 0 = No, 1 = Yes). It used the shared **5,634-row, 19-feature** raw training split created by Notebook 2. The training class counts were **4,139 non-churners** and **1,495 churners**. The 1,409-row held-out test split was not used in this notebook.

## Preprocessing and baseline

The model was built as a scikit-learn `Pipeline` with a `ColumnTransformer` to impute numeric fields and impute/one-hot encode categorical fields inside each training fold. Tree boosting did not require feature scaling. Five-fold stratified cross-validation was used for the baseline.

| Baseline metric | Mean | Fold standard deviation |
|---|---:|---:|
| Accuracy | 0.8032 | 0.0129 |
| Precision | 0.6600 | 0.0327 |
| Recall | 0.5338 | 0.0323 |
| F1 | 0.5898 | 0.0289 |
| ROC-AUC | 0.8468 | 0.0102 |
| Average Precision | 0.6667 | 0.0209 |

**Evidence:** `reports/xgboost_baseline_cv_results.csv`.

## Hyperparameter search

`GridSearchCV` used three inner stratified folds and F1 as its selection metric. The search explored 32 combinations: `n_estimators` (200/300), `max_depth` (3/4), `learning_rate` (0.03/0.05), `min_child_weight` (1/5), and `scale_pos_weight` (1 or training-class ratio), with `subsample=0.8` and `colsample_bytree=0.8` fixed.

Best full-training search settings:

| Hyperparameter | Value |
|---|---:|
| n_estimators | 200 |
| max_depth | 4 |
| learning_rate | 0.05 |
| min_child_weight | 1 |
| subsample | 0.8 |
| colsample_bytree | 0.8 |
| scale_pos_weight | 2.7686 |

Best **inner** CV F1 was **0.6391**. Because this score was used to select hyperparameters, it is potentially optimistic and should not be presented as independent generalization performance.

**Evidence:** `notebooks/05_xgboost.ipynb`, `reports/xgboost_tuning_results.csv`.

## Nested cross-validation

A five-fold **outer** stratified CV evaluated an inner three-fold search on the training portions only. At classification threshold 0.50:

| Metric | Mean | Fold standard deviation |
|---|---:|---:|
| Accuracy | 0.7536 | 0.0122 |
| Precision | 0.5236 | 0.0154 |
| Recall | 0.7960 | 0.0257 |
| F1 | 0.6316 | 0.0180 |
| ROC-AUC | 0.8482 | 0.0104 |
| Average Precision | 0.6691 | 0.0207 |

A threshold sweep over nested out-of-fold probabilities identified **0.55** as the highest exploratory F1 candidate (**0.6345**). This threshold was chosen and scored using the same OOF predictions, so the 0.6345 figure is **exploratory**, not independently validated.

**Evidence:** `reports/xgboost_nested_cv_results.csv`, `reports/xgboost_threshold_results.csv`.

## Model interpretation and outputs

The fitted model's encoded-feature importance was exported to `reports/xgboost_feature_importance.csv` and `reports/xgboost_feature_importance.png`. Importance describes the trained model's use of variables; it does not establish causal effects or prove the direction of a relationship.

The notebook also saved `models/xgboost_pipeline.joblib` and `models/xgboost_config.json` locally. These are reproducible training artifacts and may be excluded from version control.

## Limitations and next use

- The training-wide imbalance ratio was used in the search, rather than recomputing it in every fold; stratification reduces but does not remove the methodological concern.
- The F1-optimal threshold from the OOF sweep is exploratory.
- Selection of the overall project model requires comparison against Logistic Regression, Random Forest, and Decision Tree (Notebook 7).
- No XGBoost held-out test score should be inferred from the training CV results.

The team ultimately selected **balanced Logistic Regression** for final testing due to nearly identical finalist validation performance and simpler interpretation (see `docs/final_model_selection.md`).
