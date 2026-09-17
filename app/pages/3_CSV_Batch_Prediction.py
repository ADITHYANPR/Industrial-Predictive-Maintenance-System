import numpy as np
import pandas as pd
import streamlit as st

from styles import load_css
from sidebar import render_sidebar
from utils import model, scaler, feature_names


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Batch Analysis",
    page_icon="📄",
    layout="wide"
)

load_css()
render_sidebar()


# ============================================================
# HEADER
# ============================================================

st.title("Batch Analysis")

st.write(
    "Upload a CSV dataset and generate Remaining Useful Life "
    "predictions for multiple assets."
)


# ============================================================
# UPLOAD
# ============================================================

st.header("Upload Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        st.success("CSV loaded successfully.")

        # ----------------------------------------------------
        # DATASET OVERVIEW
        # ----------------------------------------------------

        st.subheader("Dataset Overview")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Rows",
                len(df)
            )

        with c2:
            st.metric(
                "Columns",
                len(df.columns)
            )

        with c3:
            st.metric(
                "Required Features",
                len(feature_names)
            )


        with st.expander("Preview Dataset"):

            st.dataframe(
                df.head(10),
                use_container_width=True
            )


        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        missing_features = [
            feature
            for feature in feature_names
            if feature not in df.columns
        ]

        if missing_features:

            st.error(
                "The uploaded CSV is missing required features."
            )

            st.write(
                missing_features
            )

        else:

            st.success(
                "All required model features are available."
            )

            st.divider()

            run_batch = st.button(
                "Run Batch Prediction",
                type="primary",
                use_container_width=True
            )


            if run_batch:

                try:

                    X = df[feature_names].copy()

                    X_scaled = scaler.transform(X)

                    predictions = model.predict(X_scaled)

                    predictions = np.asarray(
                        predictions
                    ).reshape(-1)

                    predictions = np.maximum(
                        predictions,
                        0
                    )

                    result_df = df.copy()

                    result_df["Predicted_RUL"] = predictions

                    # ------------------------------------------------
                    # RISK CLASSIFICATION
                    # ------------------------------------------------

                    def classify_risk(rul):

                        if rul > 100:
                            return "Low"

                        elif rul > 40:
                            return "Medium"

                        return "High"


                    result_df["Risk_Level"] = (
                        result_df["Predicted_RUL"]
                        .apply(classify_risk)
                    )


                    # ------------------------------------------------
                    # METRICS
                    # ------------------------------------------------

                    st.header("Batch Results")

                    c1, c2, c3, c4 = st.columns(4)

                    with c1:
                        st.metric(
                            "Total Assets",
                            len(result_df)
                        )

                    with c2:
                        st.metric(
                            "Average RUL",
                            f"{result_df['Predicted_RUL'].mean():.2f}"
                        )

                    with c3:
                        st.metric(
                            "Maximum RUL",
                            f"{result_df['Predicted_RUL'].max():.2f}"
                        )

                    with c4:
                        st.metric(
                            "Minimum RUL",
                            f"{result_df['Predicted_RUL'].min():.2f}"
                        )


                    # ------------------------------------------------
                    # RISK DISTRIBUTION
                    # ------------------------------------------------

                    st.subheader("Risk Distribution")

                    risk_counts = (
                        result_df["Risk_Level"]
                        .value_counts()
                    )

                    r1, r2, r3 = st.columns(3)

                    with r1:
                        st.metric(
                            "Low Risk",
                            int(risk_counts.get("Low", 0))
                        )

                    with r2:
                        st.metric(
                            "Medium Risk",
                            int(risk_counts.get("Medium", 0))
                        )

                    with r3:
                        st.metric(
                            "High Risk",
                            int(risk_counts.get("High", 0))
                        )


                    st.bar_chart(
                        risk_counts
                    )


                    # ------------------------------------------------
                    # RESULTS
                    # ------------------------------------------------

                    st.subheader("Prediction Results")

                    st.dataframe(
                        result_df,
                        use_container_width=True
                    )


                    # ------------------------------------------------
                    # DOWNLOAD
                    # ------------------------------------------------

                    csv_data = result_df.to_csv(
                        index=False
                    ).encode("utf-8")

                    st.download_button(
                        "Download Prediction Results",
                        data=csv_data,
                        file_name="Predicted_RUL.csv",
                        mime="text/csv",
                        use_container_width=True
                    )


                except Exception as e:

                    st.error(
                        f"Batch prediction failed: {e}"
                    )


    except Exception as e:

        st.error(
            f"Unable to read CSV file: {e}"
        )