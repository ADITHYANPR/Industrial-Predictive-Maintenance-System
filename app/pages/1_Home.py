from styles import load_css
import streamlit as st

st.set_page_config(
    page_title="Industrial Predictive Maintenance System",
    layout="wide"
)

load_css()

# ==========================================
# HERO SECTION
# ==========================================

import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("app/assets/hero.png")

st.markdown(f"""
<style>

.hero {{
    background-image:
        linear-gradient(rgba(15,23,42,.78),
        rgba(15,23,42,.78)),
        url("data:image/jpg;base64,{img}");

    background-size:cover;
    background-position:center;

    padding:70px;

    border-radius:18px;

    margin-bottom:30px;
}}

.hero h1{{
color:white;
font-size:46px;
}}

.hero p{{
color:#CBD5E1;
font-size:22px;
}}

</style>

<div class="hero">

<h1>
Industrial Predictive Maintenance System
</h1>

<p>
AI-powered Remaining Useful Life Prediction
</p>

<p>
NASA CMAPSS Dataset | XGBoost | Explainable AI
</p>

</div>

""", unsafe_allow_html=True)
# ==================================================
# KPI CARDS
# ==================================================

# ==================================================
# CORE MODULES
# ==================================================

st.subheader("Core Modules")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):

        st.markdown("### Manual Prediction")

        st.write(
            "Predict Remaining Useful Life for a single engine using operational settings and sensor measurements."
        )

        st.button(
            "Open Module",
            key="manual_btn",
            use_container_width=True
        )

with c2:
    with st.container(border=True):

        st.markdown("### Batch Prediction")

        st.write(
            "Upload CSV datasets and predict Remaining Useful Life for multiple engines simultaneously."
        )

        st.button(
            "Open Module",
            key="batch_btn",
            use_container_width=True
        )

with c3:
    with st.container(border=True):

        st.markdown("### Analytics Dashboard")

        st.write(
            "Visualize prediction trends, risk levels, and model performance through interactive charts."
        )

        st.button(
            "Open Dashboard",
            key="analytics_btn",
            use_container_width=True
        )

with c4:
    with st.container(border=True):

        st.markdown("### Explainability (SHAP)")

        st.write(
            "Interpret model predictions using SHAP feature importance and local explanations."
        )

        st.button(
            "Open Module",
            key="shap_btn",
            use_container_width=True
        )

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------

# ==================================================
# MACHINE LEARNING PIPELINE
# ==================================================

st.subheader("Machine Learning Pipeline")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    with st.container(border=True):
        st.markdown("### 1")
        st.markdown("**Data Collection**")
        st.caption("NASA CMAPSS FD001 Dataset")

with col2:
    with st.container(border=True):
        st.markdown("### 2")
        st.markdown("**Preprocessing**")
        st.caption("Cleaning & Scaling")

with col3:
    with st.container(border=True):
        st.markdown("### 3")
        st.markdown("**Feature Engineering**")
        st.caption("Feature Selection")

with col4:
    with st.container(border=True):
        st.markdown("### 4")
        st.markdown("**Model Training**")
        st.caption("XGBoost Regressor")

with col5:
    with st.container(border=True):
        st.markdown("### 5")
        st.markdown("**Evaluation**")
        st.caption("RMSE • MAE • R²")

with col6:
    with st.container(border=True):
        st.markdown("### 6")
        st.markdown("**Deployment**")
        st.caption("Streamlit Dashboard")
st.divider()

st.caption(
"""
Industrial Predictive Maintenance System

Version 1.0

Developed using Python, Streamlit, XGBoost and SHAP
"""
)