# Decision Tree — Customer Churn Recommendations

Based on the Decision Tree model results, the following recommendations can help the Customer Retention Team identify customers who may be at risk of churning.

1. **Prioritize high-risk customers:** Focus retention efforts on customers classified as high risk.

2. **Review month-to-month contracts:** This was the most important feature in the Decision Tree. Investigate suitable retention options for customers with month-to-month contracts.

3. **Monitor customer tenure:** Provide suitable onboarding and support for new customers.

4. **Review fiber-optic customers:** Investigate service experience and support needs in this customer segment.

5. **Review monthly charges:** Examine whether pricing concerns are associated with churn risk.

6. **Offer suitable contract options:** Explain longer-term plans where they fit customer needs and preferences.

7. **Improve customer support:** Help customers resolve service and billing problems promptly.

8. **Use risk scores for prioritization:** Use predicted churn probability to prioritize outreach, not as a guarantee that a customer will leave.

9. **Test retention campaigns:** Evaluate whether retention interventions improve customer retention using appropriate comparisons.

10. **Monitor model performance:** Re-evaluate recall, precision, F1-score, and other relevant metrics over time.

## Evidence from Our Model

The following results are based on nested cross-validation and out-of-fold predictions from the training data.

- Accuracy: 73.89% (threshold 0.50).
- Churn recall: 79.46% (threshold 0.50).
- Churn F1-score: approximately 0.6176 (threshold 0.50).
- ROC-AUC: 0.8280.
- Most important feature: Month-to-month contract (importance approximately 0.6095).
- Low-risk group actual churn rate: 5.35%.
- Medium-risk group actual churn rate: 21.49%.
- High-risk group actual churn rate: 54.22%.

**Evaluation note:** These are cross-validation results, not held-out test-set results. Independent test-set evaluation is still required before deployment.

## Limitations

These findings show model associations, not proof of causation. Predictions are estimates, not guarantees. Recommendations should be tested before deployment, model performance should be monitored regularly, and customer information must be handled responsibly.