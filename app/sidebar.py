import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown("## ⚙ Asset Intelligence")

        st.caption("Predictive Maintenance Platform")

        st.divider()

        st.markdown("**PLATFORM**")

        st.page_link(
            "app.py",
            label="Overview",
            icon="📊"
        )

        st.page_link(
            "pages/2_Manual_Prediction.py",
            label="Asset Prediction",
            icon="⚙️"
        )

        st.page_link(
            "pages/3_CSV_Batch_Prediction.py",
            label="Batch Analysis",
            icon="📄"
        )

        st.page_link(
            "pages/4_Analytics.py",
            label="Analytics",
            icon="📈"
        )

        st.page_link(
            "pages/5_SHAP_Explainability.py",
            label="AI Explainability",
            icon="🧠"
        )

        st.page_link(
            "pages/6_About.py",
            label="System Information",
            icon="ℹ️"
        )

        st.divider()

        st.markdown("**SYSTEM STATUS**")

        st.success(
            "Model Online\n\nXGBoost RUL Engine"
        )

        st.success(
            "Explainability Ready\n\nSHAP analysis available"
        )

        st.success(
            "Dataset Available\n\nNASA C-MAPSS FD001"
        )

        st.divider()

        st.caption(
            "Industrial Predictive Maintenance\n"
            "Version 1.1"
        )