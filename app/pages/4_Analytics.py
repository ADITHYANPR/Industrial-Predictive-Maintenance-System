from styles import load_css
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
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
st.title("📊 Analytics Dashboard")

st.write(
    "Analyze the prediction results generated from the Batch Prediction module."
)

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Prediction CSV (Predicted_RUL.csv)",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if "Predicted_RUL" not in df.columns:

        st.error(
            "Please upload the prediction file generated from the Batch Prediction page."
        )

    else:

        st.success("Prediction file loaded successfully.")

        st.markdown("---")

        # ======================================================
        # KPI Cards
        # ======================================================

        st.subheader("📌 Key Performance Indicators")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Engines",
                len(df)
            )

        with col2:
            st.metric(
                "Average RUL",
                f"{df['Predicted_RUL'].mean():.2f}"
            )

        with col3:
            st.metric(
                "Maximum RUL",
                f"{df['Predicted_RUL'].max():.2f}"
            )

        with col4:
            st.metric(
                "Minimum RUL",
                f"{df['Predicted_RUL'].min():.2f}"
            )

        st.markdown("---")

        # ======================================================
        # Distribution Histogram
        # ======================================================

        st.subheader("📈 Distribution of Predicted RUL")

        fig = px.histogram(
            df,
            x="Predicted_RUL",
            nbins=30,
            title="Distribution of Remaining Useful Life"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # ======================================================
        # Risk Level Pie Chart
        # ======================================================

        if "Risk_Level" in df.columns:

            st.subheader("🚦 Risk Level Distribution")

            risk_counts = df["Risk_Level"].value_counts().reset_index()
            risk_counts.columns = ["Risk_Level", "Count"]

            fig = px.pie(
                risk_counts,
                names="Risk_Level",
                values="Count",
                hole=0.4,
                title="Engine Risk Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")

        # ======================================================
        # Box Plot
        # ======================================================

        st.subheader("📦 RUL Box Plot")

        fig = px.box(
            df,
            y="Predicted_RUL",
            title="Box Plot of Predicted RUL"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # ======================================================
        # Gauge Chart
        # ======================================================

        avg_rul = df["Predicted_RUL"].mean()

        st.subheader("🎯 Average Engine Health")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=avg_rul,
            title={"text": "Average Remaining Useful Life"},
            gauge={
                "axis": {"range": [0, 150]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 40], "color": "#ff9999"},
                    {"range": [40, 100], "color": "#ffe680"},
                    {"range": [100, 150], "color": "#99ff99"}
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # ======================================================
        # Summary Table
        # ======================================================

        st.subheader("📋 Statistical Summary")

        st.dataframe(
            df.describe(),
            use_container_width=True
        )

        st.markdown("---")

        # ======================================================
        # Top & Bottom Engines
        # ======================================================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🏆 Top 10 Healthiest Engines")

            st.dataframe(
                df.nlargest(10, "Predicted_RUL"),
                use_container_width=True
            )

        with col2:

            st.subheader("⚠️ Top 10 Critical Engines")

            st.dataframe(
                df.nsmallest(10, "Predicted_RUL"),
                use_container_width=True
            )