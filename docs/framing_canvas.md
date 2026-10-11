
# Problem Framing Canvas — Telco Customer Churn

## 1. Stakeholder
Customer Retention Team.

## 2. Decision Need
Identify customers who are likely to leave the telecom service so the retention team can prioritize suitable retention actions.

## 3. Primary Lens
Churn prediction: estimate whether a customer is likely to churn.

## 4. Secondary Lens
Customer segmentation based on predicted churn risk: Low, Medium, and High.

## 5. Unit of Analysis
One customer record.

## 6. Target Variable
Churn: Yes = 1, No = 0.

## 7. Task
Binary classification using customer account, service, contract, and billing information.

## 8. Expected Output
- Predicted churn class.
- Estimated churn probability.
- Risk group for profiling.
- Interpretable Decision Tree rules.

## 9. Rationale
The Decision Tree provides interpretable rules that can help the retention team understand patterns associated with churn risk.

## 10. Limitations and Responsible Use
- Predictions are estimates, not guarantees.
- Feature importance does not prove causation.
- Validate model performance before real customer use.
- Use customer data responsibly and avoid unfair treatment.
