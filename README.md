# Telco Customer Churn Prediction — IT3091 Machine Learning

**Group:** 2026-DS-37 (Y3.S1.WE.DS.0102)
**Track:** Guided Data Track
**Domain:** Telecommunications
**Python Version:** 3.12.4

## 1. Project Overview

This project focuses on predicting customer churn in the telecommunications industry using machine learning.

Customer churn occurs when customers stop using a company's services. Predicting churn can help telecommunications companies identify customers who may leave and prioritize customer retention activities.

Our group developed and compared four machine learning classification models and deployed the selected model using Streamlit.

**Live Application:** https://telcom-churn-predictor.streamlit.app/

## 2. Business Problem

Telecommunication companies may lose revenue when customers discontinue their services.

Our business problem is to identify customers who are more likely to churn based on their demographic information, account details, and subscribed services.

The system aims to help businesses understand potential churn risks and make better data-driven retention decisions.

### Project Objectives

**Primary Objective — Churn Prediction**

Build a supervised machine learning classification model to predict whether a customer is likely to churn.

**Secondary Objective — High-Risk Customer Profiling**

Analyze factors associated with churn, categorize customers into different risk groups, and propose possible retention actions.

## 3. Dataset Information

**Dataset:** Telco Customer Churn (IBM sample dataset)

**Source:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn

**Dataset Filename:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

| Property | Description |
|---|---|
| Total Records | 7,043 |
| Original Columns | 21 |
| Target Variable | Churn |
| Problem Type | Binary Classification |
| Target Classes | Yes / No |
| Training Records | 5,634 |
| Testing Records | 1,409 |

The dataset contains customer information such as:

- Gender and senior citizen status
- Partner and dependent information
- Customer tenure
- Internet and telephone services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Customer churn status

### Downloading the Dataset

The original dataset is not committed to this GitHub repository.

1. Download the dataset from Kaggle.
2. Extract the downloaded ZIP file.
3. Find `WA_Fn-UseC_-Telco-Customer-Churn.csv`.
4. Place the CSV file inside the project's `data/` directory.

Expected location:

`data/Original/WA_Fn-UseC_-Telco-Customer-Churn.csv`

### Dataset Integrity Verification

On Windows PowerShell, calculate the SHA-256 fingerprint:

```powershell
Get-FileHash "data/Original/WA_Fn-UseC_-Telco-Customer-Churn.csv" -Algorithm SHA256
```

**Dataset SHA-256:** `88BE4B93FBE0CC83421AF1C503794C97C342ECA914C1576DB7C276E61D61358A`

This fingerprint allows another user to confirm that they are using the same dataset file.

## 4. Machine Learning Workflow

Our project followed these main stages:

1. Business problem identification
2. Dataset understanding
3. Exploratory Data Analysis (EDA)
4. Data cleaning and preprocessing
5. Training and testing data preparation
6. Logistic Regression modelling
7. Random Forest modelling
8. XGBoost modelling
9. Decision Tree modelling
10. Model comparison and selection
11. Final evaluation on unseen test data
12. Customer risk profiling and explainability
13. Streamlit application development and deployment

### Exploratory Data Analysis

We examined the dataset to understand customer characteristics and churn patterns.

The analysis focused on factors including:

- Contract type
- Customer tenure
- Monthly charges
- Internet service
- Payment method
- Customer churn distribution

Visualizations were used to explore relationships between these features and churn.

### Data Preprocessing

Preprocessing included:

- Handling missing and blank values
- Converting `TotalCharges` into a numeric variable
- Preparing categorical features
- Encoding categorical variables
- Scaling numerical features
- Removing identifiers that were not suitable as predictive features
- Creating an 80:20 stratified train/test split

A preprocessing pipeline was used to apply the required transformations consistently.

The customer ID was not used as a predictive feature.

## 5. Machine Learning Models

Four classification algorithms were implemented and compared.

| Model | Purpose |
|---|---|
| Logistic Regression | Interpretable linear classification baseline |
| Random Forest | Ensemble classification using multiple decision trees |
| XGBoost | Gradient-boosted tree classification |
| Decision Tree | Rule-based classification with interpretable splits |

Model development and comparison considered precision, recall, F1-score, ROC-AUC, cross-validation, and class imbalance.

### Selected Final Model

**Balanced Logistic Regression**

The model was selected because it achieved competitive F1 performance while providing simpler interpretation compared with more complex alternatives.

**Selected Classification Threshold:** 0.60

The threshold was selected using training-only out-of-fold predictions before final evaluation on the held-out test set.

## 6. Final Model Evaluation

The selected model was evaluated using an independent test set of 1,409 customers.

| Evaluation Metric | Result |
|---|---|
| Accuracy | 76.22% |
| Precision | 53.99% |
| Recall | 70.59% |
| F1-score | 0.6118 |
| ROC-AUC | 0.8416 |
| Test Customers | 1,409 |
| True Negatives | 810 |
| False Positives | 225 |
| False Negatives | 110 |
| True Positives | 264 |

### Interpretation

The model achieved approximately 70.59% recall, meaning it identified about 71% of customers who actually churned in the test dataset.

The F1-score of approximately 0.612 represents the balance between precision and recall.

ROC-AUC of approximately 0.842 indicates useful discrimination between customers who churn and those who do not.

These results are based on the selected model's performance on the held-out test set and should not be interpreted as a guarantee of performance on future customer data.

## 7. Secondary Analysis — Customer Risk Profiling

Our secondary analysis focused on understanding customer churn risk.

Customers were grouped using their model-generated risk scores:

| Risk Segment | Model Score |
|---|---|
| Low Risk | Below 0.30 |
| Medium Risk | 0.30 to below 0.60 |
| High Risk | 0.60 and above |

The analysis also examined important features associated with the model's predictions, including customer tenure, contract type, and internet service.

Possible retention actions were suggested for different risk groups.

These actions are recommendations based on analysis and have not been experimentally validated.

**Important limitation:** The model scores are not calibrated probabilities. They are used for relative risk ranking and segmentation, not as guaranteed real-world churn probabilities.

## 8. Streamlit Web Application

The final machine learning model was deployed using Streamlit Community Cloud.

**Live Streamlit Application:**

https://telcom-churn-predictor.streamlit.app/

### Application Features

- Customer information input form
- Churn risk prediction
- Classification into low, medium, and high-risk segments
- Likely-to-churn classification
- Model performance analytics
- Model explainability
- Suggested customer retention actions

The application loads the saved Logistic Regression model pipeline and applies the required preprocessing automatically.

### Run the Application Locally

From the root project directory, activate the virtual environment and run:

```powershell
python -m streamlit run app.py
```

The application should open in a local browser.

### Saved Model Files

The selected model artifacts are stored in:

```text
models/
├── selected_churn_model.joblib
└── selected_model_config.joblib
```

These files are intentionally included in the repository so that the deployed application and other users can load the selected model without retraining it.

Only load these serialized model files from trusted sources.

## 9. Project Folder Structure

```text
telcom-churn/
│
├── app.py
├── README.md
├── requirements.txt
├── requirements-streamlit.txt
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│       (download separately)
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_logistic_regression.ipynb
│   ├── 04_random_forest.ipynb
│   ├── 05_xgboost.ipynb
│   ├── 06_decision_tree.ipynb
│   ├── 07_model_comparison.ipynb
│   ├── 08_final_evaluation.ipynb
│   └── 09_high_risk_profiling.ipynb
│
├── models/
│   ├── selected_churn_model.joblib
│   └── selected_model_config.joblib
│
├── docs/
│   ├── decision_log.md
│   └── data_dictionary.md
│
├── reports/
│   └── final_evaluation_summary.csv
│
└── deployment/
    ├── streamlit_app.py
    └── requirements.txt
```

This structure shows the major project files. Additional documentation, plots, evaluation files, and source code may also be present.

## 10. Environment Setup and Reproducibility

### Python Version

The tested project environment uses:

**Python 3.12.4**

### Create a Virtual Environment

Open PowerShell in the root project directory.

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Verify Dependency Compatibility

```powershell
python -m pip check
```

### Verify the Saved Model

Run the following command to confirm that the trained model loads successfully:

```powershell
python -c "import joblib, sklearn; model = joblib.load('models/selected_churn_model.joblib'); print('scikit-learn:', sklearn.__version__); print('Model loaded successfully!')"
```

The saved model was created using **scikit-learn 1.6.1**, so that version is pinned to prevent compatibility problems.

The root `requirements.txt` contains dependencies for notebooks and the local application. `requirements-streamlit.txt` and `deployment/requirements.txt` contain the smaller set of dependencies intended for the Streamlit deployment.

The Streamlit Community Cloud deployment uses `deployment/streamlit_app.py` as its application entry point, with deployment-specific dependencies.

The additional notebook libraries should also be version-pinned after their working versions are verified to improve full reproducibility.

## 11. Notebook Execution Order

Open Jupyter Notebook:

```powershell
python -m jupyter notebook
```

Run the notebooks in the following order:

| Order | Notebook | Responsibility |
|---|---|---|
| 1 | `01_eda.ipynb` | Dataset exploration and visualizations |
| 2 | `02_preprocessing.ipynb` | Data cleaning and preprocessing |
| 3 | `03_logistic_regression.ipynb` | Logistic Regression modelling |
| 4 | `04_random_forest.ipynb` | Random Forest modelling |
| 5 | `05_xgboost.ipynb` | XGBoost modelling |
| 6 | `06_decision_tree.ipynb` | Decision Tree modelling |
| 7 | `07_model_comparison.ipynb` | Comparison of trained models |
| 8 | `08_final_evaluation.ipynb` | Final held-out model evaluation |
| 9 | `09_high_risk_profiling.ipynb` | Risk segmentation and interpretation |

Before reproducing results, ensure the dataset is in the expected location.

Some notebooks depend on model artifacts or outputs created by earlier notebooks. Follow their saved execution instructions and verify any required intermediate files are available.

## 12. Team Members and Contributions

| Student Name | Student ID | Main Contributions |
|---|---|---|
| Hariluxshun R | IT24102466 | EDA, preprocessing, high-risk customer profiling, Streamlit deployment and GitHub integration |
| Sharanjan S | IT24102361 | Logistic Regression, Random Forest, model training and evaluation |
| Delshikan KT | IT24102237 | XGBoost, model comparison, final model selection and held-out evaluation |
| Thilakshan R | IT24102152 | Decision Tree development, hyperparameter tuning and model interpretation |

The four members contributed to different parts of the machine learning workflow and integrated their work into the final GitHub repository.

## 13. Important Project Decisions

The major decisions made during the project included:

- Using the Telco Customer Churn dataset for supervised classification
- Using a stratified 80:20 train/test split
- Applying preprocessing consistently through a pipeline
- Comparing four classification algorithms
- Considering class imbalance during training and evaluation
- Selecting Balanced Logistic Regression as the final model
- Choosing the 0.60 decision threshold from training-only predictions
- Evaluating the selected model on the held-out test set
- Developing high-risk customer segments
- Deploying the final pipeline using Streamlit

Additional decision details are documented in `docs/decision_log.md`.

## 14. Limitations and Future Improvements

This project has several limitations:

1. The dataset is a sample dataset and may not represent current real-world telecom customers.
2. Churn predictions depend on the quality and representativeness of the training data.
3. The model can produce incorrect predictions, including false positives and false negatives.
4. The predicted risk scores are not calibrated probabilities.
5. Feature relationships do not establish causation.
6. Proposed retention strategies have not been tested for actual business impact.

Future improvements could include:

- Testing the model on newer customer data
- Monitoring model performance over time
- Calibrating prediction probabilities
- Performing additional feature engineering
- Evaluating retention strategies using business experiments
- Improving application input validation

## 15. AI-Use Declaration

Our group used ChatGPT as a supporting tool during the Telco Customer Churn Prediction project. AI assistance was used for debugging Python code and Jupyter notebooks, improving documentation, developing the Streamlit application, and reviewing machine learning evaluation results.

AI-generated suggestions were used to support project development and understanding. The group remains responsible for reviewing the suggested solutions, verifying the results, and ensuring the accuracy of the final submission.

### Individual AI-Use Declarations

**1. Hariluxshun R (IT24102466)**

I used ChatGPT to help debug Python and Jupyter notebook code, improve project documentation, develop and troubleshoot the Streamlit application, and review model evaluation results. AI assistance helped me identify possible solutions and improve my understanding of the implementation. I remained responsible for reviewing the suggestions and the work I submitted.

**2. Sharanjan S (IT24102361)**

I used ChatGPT to support debugging Python and Jupyter notebook code, improving documentation, assisting with Streamlit development, and reviewing model evaluation results. AI suggestions supported my work on machine learning model development and evaluation. I remained responsible for understanding and reviewing the final work.

**3. Delshikan KT (IT24102237)**

I used ChatGPT to assist with debugging Python and Jupyter notebook code, improving documentation, supporting Streamlit application development, and reviewing machine learning evaluation results. This assistance helped me examine modelling and evaluation issues. I remained responsible for reviewing the suggestions and final project results.

**4. Thilakshan R (IT24102152)**

I used ChatGPT for debugging Python and Jupyter notebook code, improving documentation, supporting Streamlit development, and reviewing model evaluation results. AI assistance supported my understanding of implementation and evaluation challenges. I remained responsible for reviewing the final work and ensuring that I understood my contributions.

### Responsible Use of AI

AI was used as an assistance tool rather than as a replacement

## 16. Project Links

**GitHub Repository:**
https://github.com/Hariluxshun1/telcom-churn

**Live Streamlit Application:**
https://telcom-churn-predictor.streamlit.app/

**Dataset Source:**
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

**YouTube Demonstration:**
[ADD VIDEO LINK AFTER UPLOADING]

## 17. Conclusion

This project demonstrates how machine learning can be used to analyze customer churn in the telecommunications industry.

We developed and evaluated four classification models and selected Balanced Logistic Regression based on its performance and interpretability.

We also analyzed customer risk segments and deployed the selected model using Streamlit, allowing users to interact with the prediction system through a web application.

The completed work provides an example of how machine learning can support customer retention analysis while recognizing the limitations of model predictions.