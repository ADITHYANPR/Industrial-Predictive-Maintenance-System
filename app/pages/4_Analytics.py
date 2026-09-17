import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from styles import load_css
from sidebar import render_sidebar


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

load_css()
render_sidebar()


# ============================================================
# HEADER
# ============================================================

st.title("Analytics Dashboard")

st.write(
    "Analyze predicted Remaining Useful Life, asset health "
    "and risk distribution across the uploaded fleet."
)


# ============================================================
# FILE UPLOAD
# ============================================================

st.header("Prediction Dataset")

uploaded_file = st.file_uploader(
    "Upload Predicted_RUL.csv",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        if "Predicted_RUL" not in df.columns:

            st.error(
                "The uploaded file must contain a "
                "'Predicted_RUL' column."
            )

            st.stop()


        df["Predicted_RUL"] = pd.to_numeric(
            df["Predicted_RUL"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["Predicted_RUL"]
        )


        # ====================================================
        # KPIs
        # ====================================================

        st.header("Fleet Overview")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Total Assets",
                len(df)
            )

        with c2:
            st.metric(
                "Average RUL",
                f"{df['Predicted_RUL'].mean():.2f}"
            )

        with c3:
            st.metric(
                "Maximum RUL",
                f"{df['Predicted_RUL'].max():.2f}"
            )

        with c4:
            st.metric(
                "Minimum RUL",
                f"{df['Predicted_RUL'].min():.2f}"
            )


        # ====================================================
        # RISK LEVEL
        # ====================================================

        if "Risk_Level" not in df.columns:

            def classify_risk(rul):

                if rul > 100:
                    return "Low"

                elif rul > 40:
                    return "Medium"

                return "High"


            df["Risk_Level"] = (
                df["Predicted_RUL"]
                .apply(classify_risk)
            )


        st.header("Risk Intelligence")

        risk_counts = (
            df["Risk_Level"]
            .value_counts()
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Low Risk",
                int(risk_counts.get("Low", 0))
            )

        with c2:
            st.metric(
                "Medium Risk",
                int(risk_counts.get("Medium", 0))
            )

        with c3:
            st.metric(
                "High Risk",
                int(risk_counts.get("High", 0))
            )


        # ====================================================
        # RISK CHART
        # ====================================================

        chart1, chart2 = st.columns(2)


        with chart1:

            fig_risk = px.bar(
                x=risk_counts.index,
                y=risk_counts.values,
                labels={
                    "x": "Risk Level",
                    "y": "Number of Assets"
                },
                title="Risk Distribution"
            )

            st.plotly_chart(
                fig_risk,
                use_container_width=True
            )


        with chart2:

            fig_pie = px.pie(
                values=risk_counts.values,
                names=risk_counts.index,
                title="Fleet Risk Composition"
            )

            st.plotly_chart(
                fig_pie,
                use_container_width=True
            )


        # ====================================================
        # RUL DISTRIBUTION
        # ====================================================

        st.header("RUL Distribution")

        fig_hist = px.histogram(
            df,
            x="Predicted_RUL",
            nbins=30,
            title="Predicted Remaining Useful Life"
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )


        # ====================================================
        # GAUGE + BOX PLOT
        # ====================================================

        c1, c2 = st.columns(2)


        with c1:

            average_rul = df["Predicted_RUL"].mean()

            fig_gauge = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=average_rul,
                    title={
                        "text": "Average Fleet RUL"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 150]
                        },
                        "steps": [
                            {
                                "range": [0, 40],
                                "color": "#fecaca"
                            },
                            {
                                "range": [40, 100],
                                "color": "#fef3c7"
                            },
                            {
                                "range": [100, 150],
                                "color": "#dcfce7"
                            }
                        ]
                    }
                )
            )

            st.plotly_chart(
                fig_gauge,
                use_container_width=True
            )


        with c2:

            fig_box = px.box(
                df,
                y="Predicted_RUL",
                title="RUL Statistical Distribution"
            )

            st.plotly_chart(
                fig_box,
                use_container_width=True
            )


        # ====================================================
        # STATISTICS
        # ====================================================

        st.header("Statistical Summary")

        st.dataframe(
            df["Predicted_RUL"]
            .describe()
            .to_frame("Predicted_RUL"),
            use_container_width=True
        )


        # ====================================================
        # TOP / CRITICAL ASSETS
        # ====================================================

        c1, c2 = st.columns(2)


        with c1:

            st.subheader("Highest RUL Assets")

            highest = (
                df.sort_values(
                    "Predicted_RUL",
                    ascending=False
                )
                .head(10)
            )

            st.dataframe(
                highest,
                use_container_width=True
            )


        with c2:

            st.subheader("Critical Assets")

            critical = (
                df.sort_values(
                    "Predicted_RUL",
                    ascending=True
                )
                .head(10)
            )

            st.dataframe(
                critical,
                use_container_width=True
            )


    except Exception as e:

        st.error(
            f"Analytics processing failed: {e}"
        )

else:

    st.info(
        "Upload a prediction CSV to populate the analytics dashboard."
    )