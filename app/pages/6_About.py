import streamlit as st

from styles import load_css
from sidebar import render_sidebar


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="System Information",
    page_icon="ℹ️",
    layout="wide"
)

load_css()
render_sidebar()


# ============================================================
# HEADER
# ============================================================

st.title("System Information")

st.write(
    "Technical overview of the Industrial Predictive "
    "Maintenance System."
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.header("Project Overview")

st.write(
    "The Industrial Predictive Maintenance System is an "
    "AI-powered asset health platform designed to estimate "
    "Remaining Useful Life from industrial sensor data."
)

st.write(
    "The system combines machine learning prediction, "
    "batch analytics and explainable AI to provide a "
    "complete predictive maintenance workflow."
)


# ============================================================
# OBJECTIVE
# ============================================================

st.header("Objective")

st.write(
    "The primary objective is to estimate the remaining "
    "operational life of industrial equipment and transform "
    "the prediction into understandable asset-health and "
    "maintenance insights."
)


# ============================================================
# DATASET
# ============================================================

st.header("Dataset")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Dataset",
        "NASA C-MAPSS"
    )

with c2:
    st.metric(
        "Subset",
        "FD001"
    )

with c3:
    st.metric(
        "Task",
        "RUL Prediction"
    )


# ============================================================
# MODEL INTELLIGENCE
# ============================================================

st.header("Model Intelligence")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.subheader("XGBoost")

        st.write(
            "Primary production model used by the deployed "
            "prediction workflow."
        )

        st.metric(
            "R²",
            "0.7184"
        )

        st.metric(
            "RMSE",
            "35.8687 cycles"
        )


with c2:

    with st.container(border=True):

        st.subheader("TCN")

        st.write(
            "Temporal Convolutional Network developed as an "
            "experimental temporal benchmark."
        )

        st.metric(
            "R²",
            "0.4067"
        )

        st.metric(
            "RMSE",
            "42.0461 cycles"
        )


# ============================================================
# EXPLAINABILITY
# ============================================================

st.header("Explainable AI")

st.write(
    "SHAP is integrated into the platform to provide "
    "global feature importance and individual prediction "
    "explanations for the XGBoost model."
)


# ============================================================
# WORKFLOW
# ============================================================

st.header("System Workflow")

workflow = [
    "Data Collection",
    "Preprocessing",
    "Feature Engineering",
    "Model Training",
    "RUL Prediction",
    "Risk Classification",
    "SHAP Explainability",
    "Analytics"
]

for index, step in enumerate(
    workflow,
    start=1
):

    st.write(
        f"**{index}. {step}**"
    )


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.header("Technology Stack")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.subheader("Python")
    st.caption("Data processing and ML")

with c2:
    st.subheader("XGBoost")
    st.caption("Primary RUL model")

with c3:
    st.subheader("SHAP")
    st.caption("Model explainability")

with c4:
    st.subheader("Streamlit")
    st.caption("Interactive platform")


# ============================================================
# PLATFORM CAPABILITIES
# ============================================================

st.header("Platform Capabilities")

capabilities = [
    "Single-asset RUL prediction",
    "CSV batch prediction",
    "Asset risk classification",
    "Fleet analytics",
    "SHAP global explanations",
    "SHAP individual explanations",
    "Prediction result export",
    "Experimental TCN benchmark"
]

for capability in capabilities:

    st.write(
        f"✓ {capability}"
    )


# ============================================================
# ARCHITECTURE
# ============================================================

st.header("Platform Architecture")

st.code(
    """
Industrial Sensor Data
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
XGBoost RUL Prediction
        ↓
Asset Health & Risk
        ↓
Analytics Dashboard
        ↓
SHAP Explainability
    """,
    language="text"
)


# ============================================================
# ROADMAP
# ============================================================

st.header("Future Platform Direction")

st.write(
    "The current asset-level intelligence layer is designed "
    "as the foundation for future fleet-level predictive "
    "analytics, real-time monitoring, APIs, event streaming "
    "and digital-twin capabilities."
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Industrial Predictive Maintenance System | "
    "Version 1.1"
)