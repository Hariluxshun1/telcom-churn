# Data Dictionary: Telco Customer Churn

**Source:** Kaggle `blastchar/telco-customer-churn`, file `WA_Fn-UseC_-Telco-Customer-Churn.csv`
**Row meaning:** one row = one telecom customer. 7,043 rows, 21 columns, no duplicate rows or customer IDs.
**Target:** `Churn` (Yes = customer left, No = customer stayed). 5,174 No (73.5%), 1,869 Yes (26.5%).

| # | Column | Meaning | Type | Allowed values | Notes for modeling |
|---|---|---|---|---|---|
| 1 | customerID | Unique customer identifier | Identifier (text) | 7,043 unique values | Not a feature; drop before modeling |
| 2 | gender | Customer gender | Binary categorical | Female, Male | Almost no link to churn (26.9% vs 26.2%) |
| 3 | SeniorCitizen | Whether the customer is a senior citizen | Binary (numeric) | 0, 1 | Already 0/1, unlike other yes/no columns |
| 4 | Partner | Whether the customer has a partner | Binary categorical | Yes, No | Overlaps partly with Dependents |
| 5 | Dependents | Whether the customer has dependents | Binary categorical | Yes, No | Overlaps partly with Partner |
| 6 | tenure | Number of months the customer has stayed with the company | Numeric (integer) | 0 to 72 | Strongest numeric signal; 0 for newly joined customers |
| 7 | PhoneService | Whether the customer has phone service | Binary categorical | Yes, No | |
| 8 | MultipleLines | Whether the customer has multiple phone lines | Categorical (3 levels) | Yes, No, No phone service | "No phone service" is redundant with PhoneService; can merge into No |
| 9 | InternetService | Type of internet service | Categorical (3 levels) | DSL, Fiber optic, No | One-hot encode; fiber customers pay more on average |
| 10 | OnlineSecurity | Online security add-on | Categorical (3 levels) | Yes, No, No internet service | "No internet service" is redundant with InternetService |
| 11 | OnlineBackup | Online backup add-on | Categorical (3 levels) | Yes, No, No internet service | Same as above |
| 12 | DeviceProtection | Device protection add-on | Categorical (3 levels) | Yes, No, No internet service | Same as above |
| 13 | TechSupport | Tech support add-on | Categorical (3 levels) | Yes, No, No internet service | Strong signal: 41.6% churn without it vs 15.2% with it |
| 14 | StreamingTV | Streaming TV add-on | Categorical (3 levels) | Yes, No, No internet service | Same redundancy as above |
| 15 | StreamingMovies | Streaming movies add-on | Categorical (3 levels) | Yes, No, No internet service | Same redundancy as above |
| 16 | Contract | Contract term | Categorical (3 levels) | Month-to-month, One year, Two year | Strong signal: 42.7% / 11.3% / 2.8% churn |
| 17 | PaperlessBilling | Whether the customer uses paperless billing | Binary categorical | Yes, No | Churn 33.6% (Yes) vs 16.3% (No) |
| 18 | PaymentMethod | How the customer pays | Categorical (4 levels) | Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic) | One-hot encode; electronic check has the highest churn (45.3%) |
| 19 | MonthlyCharges | Amount charged per month | Numeric (decimal) | about 18 to 119 | Right-sized, no outliers; correlates with TotalCharges |
| 20 | TotalCharges | Total amount charged over the customer's stay | Numeric (stored as text in the raw file) | about 0 to 8,700 | 11 blanks (tenure 0, not yet billed); convert to numeric and set to 0; correlates 0.83 with tenure |
| 21 | Churn | Whether the customer left | Binary categorical (target) | Yes, No | Target variable; imbalanced (73.5% / 26.5%) |

## Data quality notes
1. `TotalCharges` is read as text. 11 rows are blank spaces (not true nulls), all with tenure 0 and Churn = No.
2. `customerID` is unique for every row and carries no predictive information.
3. "No internet service" (six columns) and "No phone service" (`MultipleLines`) repeat information already in `InternetService` and `PhoneService`.
4. `SeniorCitizen` is numeric while the other yes/no columns use text.
5. No outliers were found by boxplot in tenure, MonthlyCharges or TotalCharges.

## Derived columns used in EDA only (not in the raw file)
- `ChurnFlag`: 1 if Churn = Yes, else 0.
- `tenure_band`: 0-12, 13-24, 25-48, 49-72 months.
