# Decision Log — Telco Customer Churn

| # | Date | Decision | Options Considered | Reason / Evidence | Responsible |
|---|---|---|---|---|---|
| 1 | 2026-10-11 | Project track selection | Guided Data Track vs Industry Explorer | Selected based on project scope and available time | Group |
| 2 | 2026-10-11 | Primary problem framing | Churn prediction vs customer segmentation | A labelled churn target is available; segmentation is treated as a secondary analysis | Group |
| 3 | 2026-10-11 | Decision Tree baseline | Decision Tree vs no Decision Tree baseline | Provides interpretable rules for understanding customer churn patterns | M4 |
| 4 | 2026-10-11 | Hyperparameter tuning | Grid search over `max_depth` and `min_samples_leaf` | Best inner CV F1 = 0.6187; selected `max_depth=5` and `min_samples_leaf=5` | M4 |
| 5 | 2026-10-11 | Model evaluation criteria | Accuracy, precision, recall, F1-score and ROC-AUC | Recall is important for identifying customers at risk of churn; precision and F1 help assess predictive performance | M4 |
| 6 | 2026-10-11 | Customer risk profiling | Low, Medium and High predicted-risk groups | Training out-of-fold predictions were used to explore risk segmentation separately from the final selected model | M4 |
| 7 | 2026-10-11 | Final model selection | Balanced Logistic Regression vs comparison models | Selected based on training-only model comparison, F1 performance and interpretability; classification threshold = 0.60 | Group |

## Notes

- Decision Tree baseline development and final group model selection are separate decisions.
- Cross-validation results should not be described as held-out test results.
- Final model performance should be evaluated on an independent test set before deployment.
- Model predictions indicate risk, not certainty or causation.