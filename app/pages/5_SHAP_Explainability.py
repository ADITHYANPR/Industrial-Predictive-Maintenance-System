from styles import load_css
import streamlit as st
import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="SHAP Explainability",
    page_icon="🧠",
    layout="wide"
)
load_css()
st.sidebar.title("⚙️ Industrial Predictive Maintenance")

st.sidebar.markdown("---")

st.sidebar.success("Version 1.0")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Modules**
    
    🏠 Home
    
    🛠 Manual Prediction
    
    📂 Batch Prediction
    
    📊 Analytics
    
    🧠 Explainability
    
    ℹ️ About
    """
)
st.title("🧠 Explainable AI Dashboard")

st.write("""
Understand **why** the XGBoost model predicts a particular Remaining Useful Life (RUL)
using SHAP (SHapley Additive exPlanations).
""")

st.markdown("---")

# --------------------------------------------------------
# Load Model & Explainer
# --------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "xgboost_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
EXPLAINER_PATH = BASE_DIR / "models" / "shap_explainer.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
explainer = joblib.load(EXPLAINER_PATH)

feature_names = [
    "time_in_cycles",
    "operational_setting_1",
    "operational_setting_2",
    "operational_setting_3"
]

for i in range(1,22):
    feature_names.append(f"sensor_{i}")

# --------------------------------------------------------
# Upload Dataset
# --------------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if not all(col in df.columns for col in feature_names):

        st.error("Dataset does not contain all required features.")

    else:

        X = df[feature_names]

        X_scaled = scaler.transform(X)

        shap_values = explainer.shap_values(X_scaled)

        st.success("SHAP values generated successfully.")

        st.markdown("---")

        # ==========================================
        # Summary Plot
        # ==========================================

        st.subheader("📊 SHAP Summary Plot")

        fig, ax = plt.subplots(figsize=(10,6))

        shap.summary_plot(
            shap_values,
            X,
            show=False
        )

        st.pyplot(fig)

        plt.close()

        st.markdown("---")

        # ==========================================
        # Feature Importance
        # ==========================================

        st.subheader("⭐ Feature Importance")

        fig, ax = plt.subplots(figsize=(10,6))

        shap.summary_plot(
            shap_values,
            X,
            plot_type="bar",
            show=False
        )

        st.pyplot(fig)

        plt.close()

        st.markdown("---")

        # ==========================================
        # Individual Prediction
        # ==========================================

        st.subheader("🔍 Explain Individual Engine")

        row = st.number_input(
            "Select Engine Row",
            min_value=0,
            max_value=len(df)-1,
            value=0
        )

        fig, ax = plt.subplots(figsize=(10,6))

        shap.plots.waterfall(
            shap.Explanation(
                values=shap_values[row],
                base_values=explainer.expected_value,
                data=X.iloc[row],
                feature_names=feature_names
            ),
            show=False
        )

        st.pyplot(fig)

        plt.close()

        st.markdown("---")

        # ==========================================
        # Feature Ranking
        # ==========================================

        st.subheader("📋 Mean Absolute SHAP Values")

        importance = pd.DataFrame({

            "Feature": feature_names,

            "Importance":
                abs(shap_values).mean(axis=0)

        })

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        )

        st.dataframe(
            importance,
            use_container_width=True
        )

        st.download_button(

            "⬇ Download Feature Importance",

            importance.to_csv(index=False),

            "feature_importance.csv",

            "text/csv"

        )