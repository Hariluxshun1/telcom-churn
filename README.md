# Telco Customer Churn: IT3091 Group Assignment

**Group:** 2026-DS-37 (Y3.S1.WE.DS.0102)
**Track:** Guided Data Track | **Domain:** Telecommunications

## Business problem
A telecom company is losing customers and wants to use its existing data to find out who is likely to leave and why, so the retention team can act early.

## Lenses
- **Primary:** Churn risk prediction (binary classification on `Churn`)
- **Secondary:** High-risk customer profiling (feature importance and segments from the best model)

## Dataset
Telco Customer Churn (IBM sample data): https://www.kaggle.com/datasets/blastchar/telco-customer-churn
File: `WA_Fn-UseC_-Telco-Customer-Churn.csv` (7,043 rows, 21 columns).
Download it and place it in `data/`. SHA-256 fingerprint: *(add after downloading, see below)*

```
sha256sum data/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

## Workflow
1. Problem framing
2. EDA
3. Preprocessing
4. Baseline model (Logistic Regression)
5. Alternative models (Random Forest, XGBoost/LightGBM, SVM or Decision Tree)
6. Evaluation (precision, recall, F1, ROC-AUC, cross-validation)
7. Secondary lens: feature importance and risk profiles
8. Recommendation and limitations

## Team
| Student ID | Role |
|---|---|
| IT24102466 | Data Understanding & EDA |
| IT24102361 | Preprocessing & Core Modeling |
| IT24102237 | Advanced Modeling & Evaluation |
| IT24102152 | Profiling, Recommendation & Documentation |

## Repo structure
```
data/        dataset goes here (not committed)
notebooks/   one notebook per stage, e.g. 01_eda.ipynb
src/         reusable code (preprocessing functions etc.)
docs/        workflow diagram, decision log, data dictionary
reports/     final report and figures
```

## How to run
```
pip install -r requirements.txt
jupyter notebook
```
Run the notebooks in numbered order.

## AI-use declaration
*(to be completed honestly before final submission)*
