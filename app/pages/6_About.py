from styles import load_css
import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
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
st.title("ℹ️ About This Project")

st.markdown("""
# ⚙️ Industrial Predictive Maintenance System

An AI-powered predictive maintenance dashboard developed using the
**NASA CMAPSS Turbofan Engine Degradation Dataset**.

This application predicts the **Remaining Useful Life (RUL)** of aircraft engines
using Machine Learning and provides explainable predictions through SHAP.
""")

st.markdown("---")

# ===========================================================
# Project Objective
# ===========================================================

st.header("🎯 Project Objective")

st.write("""
Unexpected equipment failures are expensive and can compromise operational safety.

This project aims to predict engine failures before they occur by estimating the
Remaining Useful Life (RUL) of turbofan engines using operational settings and
sensor measurements.

The goal is to help industries move from reactive maintenance to predictive maintenance.
""")

st.markdown("---")

# ===========================================================
# Dataset
# ===========================================================

st.header("📂 Dataset")

st.info("""
**NASA CMAPSS FD001 Dataset**

The dataset contains simulated turbofan engine degradation data.

Features include:

• Time in Cycles

• 3 Operational Settings

• 21 Sensor Measurements

Target Variable:

Remaining Useful Life (RUL)
""")

st.markdown("---")

# ===========================================================
# Workflow
# ===========================================================

st.header("⚙️ Machine Learning Workflow")

st.markdown("""
1. Data Collection
2. Data Understanding
3. Exploratory Data Analysis
4. Data Preprocessing
5. Feature Engineering
6. Model Training
7. Model Evaluation
8. Explainable AI (SHAP)
9. Streamlit Deployment
""")

st.markdown("---")

# ===========================================================
# Technologies
# ===========================================================

st.header("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
### Programming

- Python
- Pandas
- NumPy
""")

with col2:

    st.markdown("""
### Machine Learning

- XGBoost
- Scikit-learn
- SHAP
""")

with col3:

    st.markdown("""
### Deployment

- Streamlit
- Plotly
- Joblib
""")

st.markdown("---")

# ===========================================================
# Folder Structure
# ===========================================================

st.header("📁 Project Structure")

st.code("""
Industrial-Predictive-Maintenance-System/

├── app/
├── data/
├── models/
├── notebooks/
├── reports/
├── images/
├── README.md
└── requirements.txt
""")

st.markdown("---")

# ===========================================================
# Features
# ===========================================================

st.header("✨ Features")

st.success("""
✔ Manual Prediction

✔ Batch CSV Prediction

✔ Analytics Dashboard

✔ SHAP Explainability

✔ Download Prediction Results

✔ Interactive Charts

✔ Industrial Dashboard
""")

st.markdown("---")

# ===========================================================
# Future Improvements
# ===========================================================

st.header("🚀 Future Scope")

st.markdown("""
- Deep Learning Models (LSTM)
- Real-time IoT Sensor Integration
- Cloud Deployment (AWS/Azure)
- REST API Integration
- Predictive Maintenance Scheduling
- Automated Alert System
- Live Sensor Monitoring Dashboard
""")

st.markdown("---")

# ===========================================================
# Developer
# ===========================================================

st.header("👨‍💻 Developer")

st.write("""
**Project:** Industrial Predictive Maintenance System

Developed as an end-to-end Machine Learning project for predictive maintenance,
model explainability, and deployment using Streamlit.
""")

st.markdown("---")

st.caption(
    "© 2026 Industrial Predictive Maintenance System | "
    "Built with ❤️ using Streamlit, XGBoost & SHAP"
)