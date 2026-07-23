from styles import load_css
import streamlit as st
import pandas as pd

from utils import model, scaler, feature_names

st.set_page_config(
    page_title="CSV Batch Prediction",
    page_icon="📂",
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
st.title("📂 Batch Prediction using CSV")

st.write(
    "Upload a CSV file containing the engine features to predict the Remaining Useful Life (RUL) for multiple engines."
)

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        st.subheader("📄 Uploaded Dataset")

        st.dataframe(df.head(), use_container_width=True)

        st.write(f"Rows : {df.shape[0]}")
        st.write(f"Columns : {df.shape[1]}")

        st.markdown("---")

        missing_features = [
            feature for feature in feature_names
            if feature not in df.columns
        ]

        if missing_features:

            st.error(
                "The following required columns are missing:"
            )

            st.write(missing_features)

        else:

            if st.button(
                "🚀 Predict for All Engines",
                use_container_width=True
            ):

                X = df[feature_names]

                X_scaled = scaler.transform(X)

                predictions = model.predict(X_scaled)

                predictions = [max(0, value) for value in predictions]

                result = df.copy()

                result["Predicted_RUL"] = predictions

                def risk_level(rul):

                    if rul > 100:
                        return "Low"

                    elif rul > 40:
                        return "Medium"

                    return "High"

                result["Risk_Level"] = result["Predicted_RUL"].apply(risk_level)

                st.success("Prediction Completed Successfully!")

                st.markdown("---")

                st.subheader("📊 Prediction Summary")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Average RUL",
                        f"{result['Predicted_RUL'].mean():.2f}"
                    )

                with col2:
                    st.metric(
                        "Maximum RUL",
                        f"{result['Predicted_RUL'].max():.2f}"
                    )

                with col3:
                    st.metric(
                        "Minimum RUL",
                        f"{result['Predicted_RUL'].min():.2f}"
                    )

                with col4:
                    st.metric(
                        "Total Engines",
                        len(result)
                    )

                st.markdown("---")

                st.subheader("🚦 Risk Distribution")

                risk_counts = result["Risk_Level"].value_counts()

                st.bar_chart(risk_counts)

                st.markdown("---")

                st.subheader("📄 Prediction Results")

                st.dataframe(
                    result,
                    use_container_width=True
                )

                csv = result.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="⬇ Download Predictions",
                    data=csv,
                    file_name="Predicted_RUL.csv",
                    mime="text/csv",
                    use_container_width=True
                )

    except Exception as e:

        st.error(f"Error : {e}")