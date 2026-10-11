
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ---------------------------------------------------------
# Application configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"


@st.cache_resource
def load_model():
    model = joblib.load(MODEL_DIR / "selected_churn_model.joblib")
    config = joblib.load(MODEL_DIR / "selected_model_config.joblib")
    return model, config


model, config = load_model()
threshold = float(config["selected_threshold"])

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("Telco Customer Churn Prediction")
st.write(
    "Predict customer churn risk using our trained "
    "Balanced Logistic Regression model."
)

st.info(
    "The model score is a relative churn-risk estimate, "
    "not a precisely calibrated probability of churn."
)

st.divider()

# ---------------------------------------------------------
# Customer input form
# ---------------------------------------------------------

st.subheader("Customer Information")

with st.form("customer_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Personal Details")

        gender = st.selectbox("Gender", ["Male", "Female"])

        senior = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

        partner = st.selectbox("Partner", ["No", "Yes"])
        dependents = st.selectbox("Dependents", ["No", "Yes"])

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=100,
            value=12
        )

        st.markdown("#### Billing")

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=70.0,
            step=1.0
        )

        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            value=float(tenure * monthly_charges),
            step=1.0,
            help="Enter the actual total billed amount if known."
        )

    with col2:
        st.markdown("#### Internet and Phone Services")

        phone_service = st.selectbox(
            "Phone Service", ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes", "No phone service"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["Fiber optic", "DSL", "No"]
        )

        online_security = st.selectbox(
            "Online Security",
            ["No", "Yes", "No internet service"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No", "Yes", "No internet service"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["No", "Yes", "No internet service"]
        )

        tech_support = st.selectbox(
            "Tech Support",
            ["No", "Yes", "No internet service"]
        )

    with col3:
        st.markdown("#### Subscriptions and Payments")

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No", "Yes", "No internet service"]
        )

        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    submitted = st.form_submit_button(
        "Predict Customer Churn",
        type="primary",
        width="stretch"
    )

# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if submitted:

    if phone_service == "No" and multiple_lines != "No phone service":
        st.error(
            "Customers without phone service must select "
            "'No phone service' for Multiple Lines."
        )
        st.stop()

    internet_features = [
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies
    ]

    if internet_service == "No":
        if any(value != "No internet service" for value in internet_features):
            st.error(
                "Customers without internet service must select "
                "'No internet service' for all internet-related services."
            )
            st.stop()

    elif any(value == "No internet service" for value in internet_features):
        st.error(
            "Customers with internet service must select Yes or No "
            "for each internet-related service."
        )
        st.stop()

    customer_data = {
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    input_df = pd.DataFrame([customer_data])
    input_df = input_df[list(model.feature_names_in_)]

    risk_score = float(
        model.predict_proba(input_df)[0, 1]
    )

    prediction = int(risk_score >= threshold)

    if risk_score < 0.30:
        risk_segment = "Low"
    elif risk_score < 0.60:
        risk_segment = "Medium"
    else:
        risk_segment = "High"

    st.divider()
    st.subheader("Prediction Results")

    result1, result2, result3 = st.columns(3)

    with result1:
        st.metric(
            "Churn Risk Score",
            f"{risk_score:.4f}"
        )

    with result2:
        st.metric(
            "Risk Segment",
            risk_segment
        )

    with result3:
        st.metric(
            "Prediction",
            "Likely to Churn" if prediction else "Not Flagged"
        )

    st.progress(min(max(risk_score, 0.0), 1.0))

    st.caption(
        f"Classification threshold: {threshold:.2f}. "
        "The risk bands are descriptive and not calibrated probabilities."
    )

    if prediction:
        st.warning(
            "This customer has been flagged for possible churn. "
            "Consider reviewing customer support needs, billing "
            "concerns, and suitable retention options."
        )
    else:
        st.success(
            "This customer was not flagged at the selected threshold. "
            "Continue monitoring service satisfaction."
        )

    with st.expander("View model input data"):
        st.dataframe(input_df, width="stretch")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()
st.caption(
    "IT3091 Machine Learning Group Project | "
    "Telco Customer Churn Prediction"
)


# =========================================================
# MODEL ANALYTICS AND EXPLAINABILITY
# =========================================================

REPORTS_DIR = BASE_DIR / "reports"

st.divider()
st.header("Model Analytics & Explainability")

analytics_tab, explain_tab = st.tabs([
    "Model Analytics",
    "Model Explainability"
])

# ---------------------------------------------------------
# TAB 1: Model Analytics
# ---------------------------------------------------------

with analytics_tab:

    st.subheader("Final Model Performance")

    st.caption("Results from the final held-out test evaluation.")

    evaluation_file = (
        REPORTS_DIR / "final_evaluation_summary.csv"
    )

    if evaluation_file.exists():
        evaluation_df = pd.read_csv(evaluation_file)

        with st.expander("View evaluation data"):
            st.dataframe(evaluation_df, width="stretch")

    # Read metrics directly from the held-out evaluation CSV.
    if evaluation_file.exists() and not evaluation_df.empty:
        result = evaluation_df.iloc[0]
        metrics = [
            ("Accuracy", "Accuracy"),
            ("Precision", "Precision"),
            ("Recall", "Recall"),
            ("F1 Score", "F1"),
            ("ROC-AUC", "ROC_AUC"),
        ]
        for col, (label, column) in zip(st.columns(5), metrics):
            with col:
                st.metric(label, f"{float(result[column]) * 100:.2f}%")
    else:
        st.warning("Final model evaluation data is unavailable.")

    st.info(
        "Performance metrics are from the held-out test set. "
        f"The selected classification threshold is {threshold:.2f}."
    )

    st.divider()

    st.subheader("Customer Risk Segmentation")

    st.caption(
        "Descriptive segmentation of 5,634 training customers "
        "using model-estimated risk scores."
    )

    risk_file = REPORTS_DIR / "risk_segment_summary.csv"

    if risk_file.exists():

        risk_df = pd.read_csv(risk_file)
        risk_order = ["Low", "Medium", "High"]
        risk_df["Risk_Segment"] = pd.Categorical(
            risk_df["Risk_Segment"], categories=risk_order, ordered=True
        )
        risk_df = risk_df.sort_values("Risk_Segment")

        st.dataframe(risk_df, width="stretch")
        st.bar_chart(
            risk_df.set_index("Risk_Segment")[["Customer_Count"]],
            y="Customer_Count",
        )

    else:
        st.warning("Risk segment summary file not found.")

    st.caption(
        "Risk segments are descriptive groups based on "
        "training-data model scores, not calibrated "
        "churn probabilities."
    )


# ---------------------------------------------------------
# TAB 2: Model Explainability
# ---------------------------------------------------------

with explain_tab:

    st.subheader("Global Feature Explainability")

    st.write(
        "The selected Logistic Regression model contains "
        "45 transformed features. Its coefficients describe "
        "associations with predicted churn log-odds."
    )

    importance_image = (
        REPORTS_DIR / "churn_feature_importance.png"
    )

    if importance_image.exists():
        st.image(
            str(importance_image),
            caption="Top Logistic Regression coefficients",
            width="stretch"
        )
    else:
        st.warning("Feature importance chart not found.")

    st.caption(
        "Positive coefficients increase predicted churn log-odds, while "
        "negative coefficients decrease them, conditional on other features. "
        "Correlated predictors require careful interpretation."
    )

    explanation_file = REPORTS_DIR / "churn_feature_explanations.csv"
    if explanation_file.exists():
        feature_df = pd.read_csv(explanation_file)
        with st.expander("View all model coefficients"):
            st.dataframe(feature_df, width="stretch")
    else:
        st.warning("Coefficient report not found.")

    st.divider()
    st.subheader("Suggested Customer Retention Strategies")

    recommendations_file = REPORTS_DIR / "retention_recommendations.csv"
    if recommendations_file.exists():
        recommendations_df = pd.read_csv(recommendations_file)
        for _, row in recommendations_df.iterrows():
            with st.expander(f"{row['Risk_Segment']} Risk Customers"):
                st.write("**Customer profile:**", row["Customer_Profile"])
                st.write("**Suggested action:**", row["Recommended_Action"])
                st.write("**Business rationale:**", row["Business_Rationale"])
    else:
        st.warning("Retention recommendations report not found.")

    st.warning(
        "These recommendations are proposed business actions. "
        "Their effectiveness has not been experimentally evaluated."
    )
