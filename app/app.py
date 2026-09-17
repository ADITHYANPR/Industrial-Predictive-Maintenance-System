import streamlit as st

from styles import load_css
from sidebar import render_sidebar


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Industrial Predictive Maintenance System",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()


# ============================================================
# HEADER
# ============================================================

st.title("Predictive Maintenance & Asset Health")

st.write(
    "AI-powered Remaining Useful Life prediction and "
    "explainable asset intelligence for industrial equipment."
)

st.success("Prediction Engine Online")


# ============================================================
# SYSTEM OVERVIEW
# ============================================================

st.header("System Overview")

st.caption("Current model and platform capabilities")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("DATASET", "FD001")
    st.caption("NASA C-MAPSS turbofan dataset")

with c2:
    st.metric("PRIMARY MODEL", "XGBoost")
    st.caption("Production RUL prediction model")

with c3:
    st.metric("MODEL R²", "0.7184")
    st.caption("Evaluation on FD001 test data")

with c4:
    st.metric("EXPLAINABILITY", "SHAP")
    st.caption("Feature-level prediction analysis")


# ============================================================
# ASSET INTELLIGENCE MODULES
# ============================================================

st.header("Asset Intelligence Modules")

st.caption(
    "Tools for prediction, analysis and model interpretation"
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    with st.container(border=True):

        st.subheader("⚙️ Asset Prediction")

        st.write(
            "Predict Remaining Useful Life for an individual "
            "engine using sensor measurements and operational data."
        )

        st.page_link(
            "pages/2_Manual_Prediction.py",
            label="Open Module →"
        )


with c2:

    with st.container(border=True):

        st.subheader("📄 Batch Analysis")

        st.write(
            "Upload CSV data and perform RUL predictions "
            "across multiple engines simultaneously."
        )

        st.page_link(
            "pages/3_CSV_Batch_Prediction.py",
            label="Open Module →"
        )


with c3:

    with st.container(border=True):

        st.subheader("📈 Analytics Dashboard")

        st.write(
            "Explore prediction trends, asset health "
            "distributions and operational analytics."
        )

        st.page_link(
            "pages/4_Analytics.py",
            label="Open Dashboard →"
        )


with c4:

    with st.container(border=True):

        st.subheader("🧠 AI Explainability")

        st.write(
            "Understand model predictions using SHAP "
            "feature importance and local explanations."
        )

        st.page_link(
            "pages/5_SHAP_Explainability.py",
            label="Open Module →"
        )


# ============================================================
# MODEL INTELLIGENCE
# ============================================================

st.header("Model Intelligence")

st.caption(
    "Comparative evaluation of predictive approaches"
)

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.subheader("XGBoost")

        st.write(
            "Primary predictive model with an R² of "
            "**0.7184** and RMSE of **35.8687 cycles**."
        )

        st.success("Primary Production Model")


with c2:

    with st.container(border=True):

        st.subheader("TCN Benchmark")

        st.write(
            "Temporal Convolutional Network evaluated using "
            "30-cycle sensor windows with an R² of **0.4067** "
            "and RMSE of **42.0461 cycles**."
        )

        st.info("Experimental Temporal Benchmark")


# ============================================================
# MACHINE LEARNING PIPELINE
# ============================================================

st.header("Machine Learning Pipeline")

st.caption(
    "From industrial sensor data to explainable RUL prediction"
)

pipeline = [
    ("01", "Data Collection", "NASA C-MAPSS FD001"),
    ("02", "Preprocessing", "Cleaning & normalization"),
    ("03", "Feature Engineering", "Health indicators"),
    ("04", "Model Training", "XGBoost regression"),
    ("05", "Evaluation", "Performance metrics"),
    ("06", "Explainability", "SHAP analysis")
]

cols = st.columns(6)

for col, (number, title, description) in zip(cols, pipeline):

    with col:

        with st.container(border=True):

            st.subheader(number)

            st.write(f"**{title}**")

            st.caption(description)


# ============================================================
# PLATFORM CAPABILITIES
# ============================================================

st.header("Platform Capabilities")

st.caption(
    "Current capabilities of the predictive maintenance system"
)

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.subheader("⚙️ Predictive Monitoring")

        st.write(
            "Estimate Remaining Useful Life from industrial "
            "operational and sensor measurements."
        )


with c2:

    with st.container(border=True):

        st.subheader("🧠 Explainable AI")

        st.write(
            "Use SHAP-based analysis to understand which "
            "features influence model predictions."
        )


with c3:

    with st.container(border=True):

        st.subheader("📊 Decision Analytics")

        st.write(
            "Transform model predictions into asset health, "
            "risk and maintenance insights."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Industrial Predictive Maintenance System | "
    "Version 1.1 | "
    "Built with Python, XGBoost, SHAP and Streamlit"
)