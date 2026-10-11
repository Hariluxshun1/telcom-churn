# Decision Log

| # | Date | Decision | Options considered | Reason / evidence | Who |
|---|---|---|---|---|---|
| 1 | | Track: Guided Data Track | Guided vs Industry Explorer | Time and scope | Group |
| 2 | | Primary lens: churn prediction | Prediction vs segmentation | Labelled target exists | Group |
| 3 | 2026-10-11 | Decision Tree baseline | Decision Tree vs no tree | Interpretable baseline model for churn prediction | M4 |
| 4 | 2026-10-11 | Hyperparameter tuning | max_depth and min_samples_leaf grid search | Best CV F1 = 0.6251; selected max_depth=7 and min_samples_leaf=50 | M4 |
| 5 | 2026-10-11 | Evaluation metric | Accuracy vs precision, recall and F1 | Churn recall is important to identify customers at risk of leaving | M4 |
| 6 | 2026-10-11 | Risk profiling | Low, Medium and High risk groups | Test-set churn rates: Low 6.3%, Medium 22.0%, High 56.1% | M4 |
