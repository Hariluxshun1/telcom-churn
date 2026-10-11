
# Decision Tree — Customer Churn Recommendations

Based on the Decision Tree model results.

1. **Prioritize high-risk customers:** Focus retention efforts on customers classified as high risk.

2. **Review month-to-month contracts:** This was the most important feature in the Decision Tree, so investigate retention options for these customers.

3. **Monitor customer tenure:** Provide suitable onboarding and support for new customers.

4. **Review fiber-optic customers:** Investigate service experience and support needs in this customer segment.

5. **Review monthly charges:** Examine whether pricing concerns are associated with churn risk.

6. **Offer suitable contract options:** Explain longer-term plans where they fit customer needs.

7. **Improve customer support:** Help customers resolve service and billing problems promptly.

8. **Use risk scores for prioritization:** Use predicted churn probability to prioritize outreach, not as a guarantee that a customer will leave.

9. **Test retention campaigns:** Compare churn outcomes before and after interventions to measure effectiveness.

10. **Monitor model performance:** Re-evaluate recall, precision, F1-score, and model performance over time.

## Evidence from Our Model

- Test accuracy: 75%
- Churn recall: 77%
- Churn F1-score: approximately 0.62
- Most important feature: Month-to-month contract
- High-risk test group actual churn rate: 56.1%

## Limitations

These findings show model associations, not proof of causation. Recommendations should be tested before deployment, and customer information must be handled responsibly.
