# Final Held-Out Evaluation — Member 3

**Source notebook:** `notebooks/08_final_evaluation.ipynb`  
**Frozen selection:** Balanced Logistic Regression with threshold **0.60** selected before evaluation.

## Test-set protocol

The final model fitted in Notebook 7 was loaded from `models/selected_churn_model.joblib` together with `models/selected_model_config.joblib`. It was evaluated on **1,409** held-out customers: **1,035 non-churners** and **374 churners**. The threshold and model were not altered in response to these test scores.

## Final metrics

| Metric | Held-out result |
|---|---:|
| Accuracy | 0.762243 |
| Precision (Churn) | 0.539877 |
| Recall (Churn) | 0.705882 |
| F1 (Churn) | 0.611819 |
| ROC-AUC | 0.841634 |
| Average Precision | 0.632649 |
| Trapezoidal PR-AUC | 0.631553 |
| Brier score | 0.168706 |
| Log loss | 0.496660 |

The Average Precision and trapezoidal PR-AUC values use different integration conventions and need not be identical.

**Evidence:** `reports/final_evaluation_summary.csv`, `reports/final_test_metrics.csv`, and `reports/final_curve_summary.csv`.

## Confusion matrix at threshold 0.60

| Actual class / Predicted class | Predicted No Churn | Predicted Churn |
|---|---:|---:|
| Actual No Churn | **810** (TN) | **225** (FP) |
| Actual Churn | **110** (FN) | **264** (TP) |

The model identified **264 of 374 actual churners** (recall 70.59%) and missed 110. The 225 false positives indicate a possible retention-intervention cost if all flagged customers are contacted. The project did not estimate intervention cost or financial return.

**Evidence:** `reports/final_confusion_matrix.csv`, `reports/final_confusion_matrix.png`.

## Discrimination and calibration

ROC-AUC of **0.8416** indicates useful risk ranking. Average Precision of **0.6326** summarizes precision–recall performance for the positive class.

Calibration analysis yielded Brier **0.1687** and log loss **0.4967**. The reliability diagram lies mostly below the perfect-calibration line, implying **systematic overestimation of churn likelihood**. Balanced class weighting may contribute, but its causal role has not been separately tested. Do not call a score of 0.80 a validated 80% real-world churn probability.

**Evidence:** `reports/final_roc_curve.png`, `reports/final_pr_curve.png`, `reports/final_calibration_curve.png`, `reports/final_calibration_bins.csv`, `reports/final_calibration_metrics.csv`.

## Relationship to validation and business use

The final test F1 of **0.6118** was below the nested-threshold validation mean (**0.6354**). This difference is compatible with ordinary evaluation variation and does not justify tuning to the test set. The model can support **relative risk prioritization** and customer segmentation, but campaign effectiveness and retention ROI are not established by predictive metrics alone.

## Study limitations

- Candidate configuration settings were informed by earlier training-validation results; finalist threshold CV does not fully account for hyperparameter selection.
- An older Decision Tree notebook inspected the held-out test data prematurely. The team did not use those earlier test scores for model selection but must disclose the exposure.
- The selected balanced Logistic Regression probabilities are not well calibrated.
- These observational patterns and model explanations are **associations**, not causal statements.

## Downstream handover: Notebook 9

Use the frozen model and threshold, the same shared preprocessing, and documented probability-calibration caveat. Risk groups should be explicitly labeled **relative model-score segments**. Use coefficients and/or suitable explanation methods for interpretation; do not promise benefits from proposed interventions without testing them.
