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
    page_title="Asset Prediction",
    page_icon="⚙️",
    layout="wide"
)

load_css()
render_sidebar()


# ============================================================
# HEADER
# ============================================================

st.title("Asset Prediction")

st.write(
    "Predict Remaining Useful Life for a single industrial asset "
    "using operational settings and sensor measurements."
)


# ============================================================
# INPUT SECTION
# ============================================================

st.header("Asset Sensor Data")

st.caption(
    "Enter the operational and sensor measurements required by "
    "the trained XGBoost model."
)


# ============================================================
# OPERATIONAL SETTINGS
# ============================================================

st.subheader("Operational Parameters")

c1, c2, c3, c4 = st.columns(4)

with c1:
    time_in_cycles = st.number_input(
        "Time in Cycles",
        value=1.0
    )

with c2:
    operational_setting_1 = st.number_input(
        "Operational Setting 1",
        value=0.0,
        format="%.6f"
    )

with c3:
    operational_setting_2 = st.number_input(
        "Operational Setting 2",
        value=0.0,
        format="%.6f"
    )

with c4:
    operational_setting_3 = st.number_input(
        "Operational Setting 3",
        value=0.0,
        format="%.6f"
    )


# ============================================================
# SENSOR INPUTS
# ============================================================

st.subheader("Sensor Measurements")

sensor_values = {}

sensor_names = [
    f"sensor_{i}"
    for i in range(1, 22)
]

for start in range(0, len(sensor_names), 4):

    cols = st.columns(4)

    for col, sensor in zip(
        cols,
        sensor_names[start:start + 4]
    ):

        with col:

            sensor_values[sensor] = st.number_input(
                sensor.replace("_", " ").title(),
                value=0.0,
                format="%.6f",
                key=sensor
            )


# ============================================================
# PREDICTION
# ============================================================

st.divider()

run_prediction = st.button(
    "Run RUL Prediction",
    type="primary",
    use_container_width=True
)


if run_prediction:

    input_data = {
        "time_in_cycles": time_in_cycles,
        "operational_setting_1": operational_setting_1,
        "operational_setting_2": operational_setting_2,
        "operational_setting_3": operational_setting_3
    }

    input_data.update(sensor_values)

    input_df = pd.DataFrame(
        [input_data],
        columns=feature_names
    )

    try:

        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)

        rul = float(np.asarray(prediction).reshape(-1)[0])

        rul = max(0.0, rul)

        # ----------------------------------------------------
        # HEALTH / RISK
        # ----------------------------------------------------

        health_score = min(100.0, rul)

        if rul > 100:
            risk = "Low"
            recommendation = (
                "Asset condition appears stable. "
                "Continue routine monitoring."
            )

        elif rul > 40:
            risk = "Medium"
            recommendation = (
                "Asset shows moderate degradation. "
                "Increase monitoring frequency and plan maintenance."
            )

        else:
            risk = "High"
            recommendation = (
                "Asset shows elevated degradation risk. "
                "Inspect the asset and consider maintenance action."
            )


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.success("Prediction completed successfully.")

        st.header("Prediction Result")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Predicted RUL",
                f"{rul:.2f} cycles"
            )

        with c2:
            st.metric(
                "Health Score",
                f"{health_score:.1f}%"
            )

        with c3:
            st.metric(
                "Risk Level",
                risk
            )


        st.subheader("Asset Health")

        st.progress(
            int(round(health_score))
        )

        if risk == "Low":
            st.success(recommendation)

        elif risk == "Medium":
            st.warning(recommendation)

        else:
            st.error(recommendation)


        # ----------------------------------------------------
        # INPUT SUMMARY
        # ----------------------------------------------------

        with st.expander("View Submitted Sensor Data"):

            st.dataframe(
                input_df,
                use_container_width=True
            )


    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )