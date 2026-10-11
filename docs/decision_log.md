# Decision Log

|#|Date|Decision|Options considered|Reason / evidence|Who|
|-|-|-|-|-|-|
|1||Track: Guided Data Track|Guided vs Industry Explorer|Time and scope|Group|
|2||Primary lens: churn prediction|Prediction vs segmentation|Labelled target exists|Group|
|3|2026-10-11|Decision Tree baseline|Decision Tree vs no tree|Interpretable baseline model for churn prediction|M4|
|4|2026-10-11|Hyperparameter tuning|max\_depth and min\_samples\_leaf grid search|Best CV F1 = 0.6251; selected max\_depth=7 and min\_samples\_leaf=50|M4|
|5|2026-10-11|Evaluation metric|Accuracy vs precision, recall and F1|Churn recall is important to identify customers at risk of leaving|M4|
|6|2026-10-11|Decision Tree risk profiling|Low, Medium and High model-estimated risk groups|Used training out-of-fold predictions to explore customer risk segmentation; this analysis was separate from the final selected model|M4|
|7|2026-10-11|Final model selection|Balanced Logistic Regression selected over comparison models|Selected based on training-only model comparison, F1 performance and interpretability; final classification threshold = 0.60|Group|
