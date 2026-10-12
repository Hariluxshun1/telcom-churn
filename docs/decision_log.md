# Decision Log

| # | Date | Decision | Options considered | Reason / evidence | Who |
|---|---|---|---|---|---|
| 1 | | Track: Guided Data Track | Guided vs Industry Explorer | Time and scope | Group |
| 2 | | Primary lens: churn prediction | Prediction vs segmentation | Labelled target exists | Group |
| 3 | 2026-10-11 | Decision Tree baseline | Decision Tree vs no tree | Interpretable baseline model for churn prediction | M4 |
| 4 | 2026-10-11 | Hyperparameter tuning | `max_depth` and `min_samples_leaf` grid search | Select the best parameters using cross-validation F1-score; record the confirmed score and parameters from the notebook | M4 |
| 5 | 2026-10-11 | Evaluation metric | Accuracy vs precision, recall and F1 | Churn recall is important to identify customers at risk of leaving; use precision and F1 to assess the balance of performance | M4 |
| 6 | 2026-10-11 | Risk profiling | Low, Medium and High risk groups | Group customers using predicted churn probabilities; record the confirmed churn rates for each group from the final evaluation | M4 |