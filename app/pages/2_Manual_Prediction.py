from styles import load_css
import streamlit as st
import pandas as pd
import numpy as np

from utils import model, scaler, feature_names

st.set_page_config(
    page_title="Manual Prediction",
    page_icon="🛠️",
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
st.title("🛠️ Manual Engine Prediction")

st.write(
    "Enter the operational settings and sensor values to predict the Remaining Useful Life (RUL) of the engine."
)

st.markdown("---")

# =====================================================
# Input Section
# =====================================================

st.header("📥 Engine Parameters")

inputs = {}

cols = st.columns(4)

for i, feature in enumerate(feature_names):

    with cols[i % 4]:

        inputs[feature] = st.number_input(
            feature,
            value=0.0,
            format="%.4f"
        )

input_df = pd.DataFrame([inputs])

st.markdown("---")

# =====================================================
# Prediction
# =====================================================

if st.button("🚀 Predict Remaining Useful Life", use_container_width=True):

    try:

        scaled_data = scaler.transform(input_df)

        prediction = float(model.predict(scaled_data)[0])

        prediction = max(prediction, 0)

        st.header("📊 Prediction Results")

        col1, col2, col3 = st.columns(3)

        # -----------------------------

        with col1:

            st.metric(
                "Predicted RUL",
                f"{prediction:.2f} Cycles"
            )

        # -----------------------------

        with col2:

            health = min(prediction, 150)

            st.metric(
                "Engine Health",
                f"{(health/150)*100:.1f}%"
            )

        # -----------------------------

        with col3:

            if prediction > 100:

                risk = "🟢 LOW"

            elif prediction > 40:

                risk = "🟡 MEDIUM"

            else:

                risk = "🔴 HIGH"

            st.metric(
                "Risk Level",
                risk
            )

        st.markdown("---")

        st.subheader("Engine Health")

        st.progress(int((health/150)*100))

        st.write(
            f"Health Score : **{(health/150)*100:.1f}%**"
        )

        st.markdown("---")

        st.subheader("Maintenance Recommendation")

        if prediction > 100:

            st.success(
                """
### 🟢 Low Risk

The engine is operating normally.

**Recommendation**

- Continue regular monitoring.
- No immediate maintenance required.
- Follow scheduled maintenance intervals.
"""
            )

        elif prediction > 40:

            st.warning(
                """
### 🟡 Medium Risk

Engine degradation has begun.

**Recommendation**

- Schedule inspection.
- Monitor sensor values.
- Plan preventive maintenance.
"""
            )

        else:

            st.error(
                """
### 🔴 High Risk

Engine failure may occur soon.

**Recommendation**

- Immediate inspection required.
- Maintenance should be performed before further operation.
- Avoid prolonged usage.
"""
            )

        st.markdown("---")

        st.subheader("📋 Input Summary")

        st.dataframe(
            input_df.T.rename(columns={0: "Value"}),
            use_container_width=True
        )

    except Exception as e:

        st.error(f"Prediction failed.\n\n{e}")