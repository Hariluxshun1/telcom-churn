# Decision Log — Telco Customer Churn Prediction

**Module:** IT3091 Machine Learning
**Group:** 2026-DS-37 (Y3.S1.WE.DS.0102)
**Track:** Guided Data Track
**Project:** Telco Customer Churn Prediction

## 1. Purpose

This decision log records important technical and project decisions made during our machine learning assignment.

It describes the alternatives considered, reasons for the decisions, supporting evidence, and responsible group members.

The dates below refer to confirmed work completion dates where the exact original decision dates were not recorded.

## 2. Project Decision Log

| # | Date | Decision | Options Considered | Reason / Evidence | Responsible |
|---|---|---|---|---|---|
| 1 | Not recorded | Selected Guided Data Track | Guided Data Track or Industry Explorer | The Guided Data Track was suitable for our available time, dataset and project scope. | Group |
| 2 | Not recorded | Selected customer churn prediction as the primary objective | Classification or customer segmentation | The dataset contains a labelled `Churn` column, making supervised binary classification possible. | Group |
| 3 | Not recorded | Selected high-risk customer profiling as the secondary objective | General customer analysis or model-based risk profiling | Risk profiling supports interpretation of model outputs and possible customer retention decisions. | Group |
| 4 | 2026-10-10 | Performed exploratory data analysis (Notebook 01) | Direct modelling or EDA before modelling | EDA helped us examine churn distribution, contract types, tenure, internet services and customer charges. | Hariluxshun R |
| 5 | 2026-10-10 | Replaced 11 missing `TotalCharges` values with 0 | Remove affected rows, use mean/median imputation, or fill with 0 | After converting `TotalCharges` to numeric, 11 blank values were identified. All 11 customers had `tenure = 0`, so filling with 0 was reasonable and preserved all customer records. Verified in Notebook 02. | Hariluxshun R |
| 6 | 2026-10-10 | Used a reusable preprocessing pipeline | Manual preprocessing or an integrated preprocessing pipeline | A pipeline helps apply consistent transformations to the training, testing and prediction data. | Hariluxshun R |
| 7 | 2026-10-10 | Used an 80:20 stratified train/test split | Ordinary random split or stratified splitting | Stratification helped preserve the churn class distribution in both training and testing sets. | Hariluxshun R |
| 7A | 2026-10-10 | Preserved service categories during categorical encoding | Merge "No internet service" and "No phone service" with "No", or retain separate categories | The preprocessing code uses OneHotEncoder to encode categories separately. Keeping these values preserves the distinction between customers without a service and customers who have the service but do not subscribe to a particular feature. The encoder is fitted only on training data to prevent data leakage. | Hariluxshun R |
| 8 | Not recorded | Used class-balanced Logistic Regression | Standard Logistic Regression or class-weighted Logistic Regression | Class balancing was used to account for the unequal distribution of churn and non-churn customers. | Sharanjan S |
| 9 | Not recorded | Included Random Forest for comparison | Logistic Regression alone or an additional ensemble model | Random Forest allowed us to evaluate a nonlinear tree-ensemble approach alongside Logistic Regression. | Sharanjan S |
| 10 | 2026-10-11 | Included XGBoost for advanced modelling | Baseline models alone or gradient-boosted trees | XGBoost was used to compare a boosting-based approach with the other classification algorithms. | Delshikan KT |
| 11 | 2026-10-11 | Included Decision Tree as an interpretable model | Decision Tree or no standalone tree model | A Decision Tree provides understandable classification rules and a useful comparison with ensemble methods. | Thilakshan R |
| 12 | 2026-10-11 | Tuned Decision Tree hyperparameters | Different `max_depth` and `min_samples_leaf` values | The original decision log records best CV F1 = 0.6251 with `max_depth=7` and `min_samples_leaf=50`. The configuration must be checked against the notebook outputs before final submission. | Thilakshan R |
| 13 | 2026-10-11 | Considered precision, recall and F1 rather than accuracy alone | Accuracy-only evaluation or multiple classification metrics | Churn recall was important for identifying customers at risk, while precision helped assess false-positive predictions. | Thilakshan R |
| 14 | 2026-10-11 | Used training out-of-fold predictions for Decision Tree profiling | In-sample prediction scores or out-of-fold scores | Out-of-fold scores supported exploratory risk profiling without using held-out test labels. This analysis was separate from the final selected model. | Thilakshan R |
| 15 | 2026-10-11 | Compared the four classification models | Select one baseline model or compare several algorithms | Comparing Logistic Regression, Random Forest, XGBoost and Decision Tree supported the final model selection process. | Delshikan KT / Group |
| 16 | 2026-10-11 | Selected Balanced Logistic Regression as the final model | Logistic Regression, Random Forest, XGBoost or Decision Tree | The final selection was based on training-only model comparison, competitive F1 performance and easier interpretation. | Group |
| 17 | 2026-10-11 | Selected a classification threshold of 0.60 | Default threshold of 0.50 or alternative thresholds | Training-only out-of-fold threshold analysis supported the selected threshold before final testing. | Delshikan KT / Group |
| 18 | 2026-10-11 | Evaluated the selected model on held-out test data | Report training performance or evaluate on previously unseen test data | The final evaluation used 1,409 test customers and achieved F1 = 0.6118, recall = 0.7059 and ROC-AUC = 0.8416. | Delshikan KT |
| 19 | 2026-10-11 | Used three churn-risk segments in Notebook 09 | Binary risk classification or Low, Medium and High risk groups | Three segments made the model-generated scores easier to interpret for customer profiling and possible retention planning. | Hariluxshun R |
| 20 | 2026-10-11 | Used risk thresholds of 0.30 and 0.60 | Different score boundaries or three defined risk intervals | Scores below 0.30 were classified as Low, from 0.30 to below 0.60 as Medium, and 0.60 or above as High. | Hariluxshun R |
| 21 | 2026-10-11 | Interpreted model features for churn profiling | Provide predictions only or examine model coefficients | Coefficient analysis helped identify features associated with model-generated churn scores, such as contract type and tenure. | Hariluxshun R |
| 22 | Not recorded | Deployed the selected model using Streamlit | Notebook-only demonstration or interactive web application | Streamlit provided a user interface for entering customer details and generating churn predictions. | Hariluxshun R |
| 23 | Not recorded | Saved the preprocessing and prediction pipeline together | Separate manual transformations or a saved integrated pipeline | The combined pipeline helps apply the same preprocessing steps when the model is used in the application. | Group |
| 24 | Not recorded | Treated model outputs as relative churn-risk scores | Present scores as calibrated probabilities or communicate their limitations | The model has not undergone probability calibration, so its scores should not be interpreted as guaranteed real-world churn probabilities. | Group |

## 3. Important Technical Decisions

### 3.1 Data Cleaning and Preprocessing

**Work completed:** 10 October 2026
**Responsible member:** Hariluxshun R

The dataset contained customer demographic information, subscribed services, billing information and churn labels.

During preprocessing:

- `TotalCharges` was converted into a numeric variable.
- Blank and missing values were addressed.
- Categorical variables were prepared for model training.
- Numerical variables were processed through the preprocessing pipeline.
- Customer identifiers were excluded from the predictive features.
- An 80:20 stratified train/test split was used.

**Reason:** These steps helped prepare consistent numerical model inputs and support reliable evaluation.

**Evidence:** `notebooks/01_eda.ipynb` and `notebooks/02_preprocessing.ipynb`.

The exact treatment of blank `TotalCharges` values and service-category normalization should be verified against the implemented code.

### 3.2 Model Development

**Responsible members:** Sharanjan S, Delshikan KT and Thilakshan R

Four machine learning algorithms were developed:

1. Logistic Regression
2. Random Forest
3. XGBoost
4. Decision Tree

**Reason:** Comparing different classification approaches allowed the group to assess model performance and interpretability rather than relying on a single algorithm.

**Evidence:** Notebooks 03–07.

### 3.3 Class Imbalance

**Responsible member:** Sharanjan S

The dataset contains more non-churning customers than churning customers.

Balanced Logistic Regression was used to account for this imbalance during model development.

**Reason:** Accuracy alone may not adequately describe the model's ability to identify customers who actually churn.

Precision, recall, F1-score and ROC-AUC were therefore considered alongside accuracy.

### 3.4 Final Model Selection

**Work completed:** 11 October 2026
**Responsible:** Delshikan KT / Group

The final selected model was **Balanced Logistic Regression**.

The model was chosen because its F1 performance was competitive with the other evaluated models while remaining relatively simple to interpret.

The selection was made using training-only comparisons before reporting the final held-out evaluation.

### 3.5 Classification Threshold

**Work completed:** 11 October 2026

A classification threshold of **0.60** was selected using training-only out-of-fold predictions.

The final classifier uses the following rule:

- Score below 0.60: Predicted not to churn.
- Score at or above 0.60: Predicted to churn.

**Reason:** Threshold selection was part of the training-stage model development process and was completed before held-out evaluation.

### 3.6 Final Model Evaluation

**Work completed:** 11 October 2026
**Responsible member:** Delshikan KT

The final model was evaluated using an unseen test set of 1,409 customers.

| Evaluation Metric | Result |
|---|---|
| Accuracy | 76.22% |
| Precision | 53.99% |
| Recall | 70.59% |
| F1-score | 0.6118 |
| ROC-AUC | 0.8416 |
| True Negatives | 810 |
| False Positives | 225 |
| False Negatives | 110 |
| True Positives | 264 |

**Evidence:** `notebooks/08_final_evaluation.ipynb` and `reports/final_evaluation_summary.csv`.

### 3.7 Secondary Lens — High-Risk Customer Profiling

**Work completed:** 11 October 2026
**Responsible member:** Hariluxshun R

The selected model's scores were used to group customers into three risk segments.

| Risk Level | Score Range |
|---|---|
| Low | Below 0.30 |
| Medium | 0.30 to below 0.60 |
| High | 0.60 and above |

The analysis also explored important model features and possible retention strategies.

**Reason:** Risk segmentation provides a simpler way to communicate model predictions to business users.

**Evidence:** `notebooks/09_high_risk_profiling.ipynb`.

The model's scores are not calibrated real-world churn probabilities, and suggested retention actions have not been tested experimentally.

### 3.8 Model Deployment

**Responsible member:** Hariluxshun R

The selected Logistic Regression pipeline was integrated into a Streamlit application.

The application supports customer input, churn prediction, risk classification, model analytics and explainability.

**Live application:** https://telcom-churn-predictor.streamlit.app/

**Reason:** An interactive application makes the completed machine learning workflow accessible beyond the notebooks.

## 4. Supporting Evidence

The following project files provide implementation evidence for the decisions documented above:

| File | Purpose |
|---|---|
| `notebooks/01_eda.ipynb` | Exploratory data analysis |
| `notebooks/02_preprocessing.ipynb` | Data preparation and preprocessing |
| `notebooks/03_logistic_regression.ipynb` | Logistic Regression |
| `notebooks/04_random_forest.ipynb` | Random Forest |
| `notebooks/05_xgboost.ipynb` | XGBoost |
| `notebooks/06_decision_tree.ipynb` | Decision Tree |
| `notebooks/07_model_comparison.ipynb` | Model comparison |
| `notebooks/08_final_evaluation.ipynb` | Held-out test evaluation |
| `notebooks/09_high_risk_profiling.ipynb` | Customer risk profiling |
| `reports/final_evaluation_summary.csv` | Final evaluation results |
| `docs/final_model_selection.md` | Final model selection rationale |

## 5. Conclusion

This decision log summarizes the reasoning behind the major choices made throughout our project.

Our group followed a structured workflow involving exploratory analysis, preprocessing, model development, model comparison, final evaluation and customer risk profiling.

Recording these decisions improves project transparency, teamwork and reproducibility.

Where the exact original decision date was unavailable, the log uses a confirmed work completion date or marks the date as not recorded.