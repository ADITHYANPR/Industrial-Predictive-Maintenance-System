from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap
import streamlit as st

from styles import load_css
from sidebar import render_sidebar


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Explainability",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "xgboost_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
EXPLAINER_PATH = BASE_DIR / "models" / "shap_explainer.pkl"


# =========================================================
# LOAD MODEL COMPONENTS
# =========================================================

@st.cache_resource
def load_components():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    explainer = joblib.load(EXPLAINER_PATH)

    return model, scaler, explainer


try:
    model, scaler, explainer = load_components()

except Exception as e:
    st.error(f"Unable to load model components: {e}")
    st.stop()


# =========================================================
# FEATURE NAMES
# =========================================================

feature_names = [
    "time_in_cycles",
    "operational_setting_1",
    "operational_setting_2",
    "operational_setting_3"
]

for i in range(1, 22):
    feature_names.append(f"sensor_{i}")


# =========================================================
# PAGE HEADER
# =========================================================

st.title("🧠 AI Explainability")

st.caption(
    "Understand how the XGBoost model produces "
    "Remaining Useful Life predictions using SHAP analysis."
)

st.success("Explainability Engine Ready")


# =========================================================
# UPLOAD SECTION
# =========================================================

st.header("Upload Prediction Data")

st.caption(
    "Upload a CSV containing the 25 model input features "
    "for SHAP-based model interpretation."
)

uploaded_file = st.file_uploader(
    "Upload CSV containing model features",
    type=["csv"],
    help="The CSV must contain all 25 features used by the XGBoost model."
)


# =========================================================
# WAIT FOR FILE
# =========================================================

if uploaded_file is None:

    st.info(
        "Upload a prediction CSV to begin SHAP analysis."
    )

    st.stop()


# =========================================================
# READ CSV
# =========================================================

try:
    df = pd.read_csv(uploaded_file)

except Exception as e:
    st.error(f"Unable to read the uploaded CSV: {e}")
    st.stop()


# =========================================================
# VALIDATE FEATURES
# =========================================================

missing_features = [
    feature
    for feature in feature_names
    if feature not in df.columns
]

if missing_features:

    st.error("The uploaded CSV is missing required model features.")

    st.write("Missing features:")

    st.code(
        "\n".join(missing_features),
        language="text"
    )

    st.stop()


# =========================================================
# MODEL INPUT
# =========================================================

X = df[feature_names].copy()


# =========================================================
# SCALE DATA
# =========================================================

try:
    X_scaled = scaler.transform(X)

except Exception as e:
    st.error(f"Feature scaling failed: {e}")
    st.stop()


# =========================================================
# SHAP ANALYSIS
# =========================================================

try:

    shap_values = explainer.shap_values(X_scaled)

    if isinstance(shap_values, list):
        shap_values = shap_values[0]

    shap_values = pd.DataFrame(
        shap_values,
        columns=feature_names
    )

except Exception as e:

    st.error(f"SHAP analysis failed: {e}")
    st.stop()


st.success("SHAP analysis completed successfully.")


# =========================================================
# OVERVIEW
# =========================================================

st.header("Explainability Overview")

st.caption(
    "Summary of the dataset and model used for interpretation."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Assets Analyzed",
        len(df)
    )

with col2:
    st.metric(
        "Features",
        len(feature_names)
    )

with col3:
    st.metric(
        "Model",
        "XGBoost"
    )


# =========================================================
# GLOBAL SHAP SUMMARY
# =========================================================

st.header("Global Feature Impact")

st.caption(
    "SHAP values show how each feature influences model output "
    "across the analyzed assets."
)

plt.close("all")

fig, ax = plt.subplots(figsize=(10, 7))

shap.summary_plot(
    shap_values.values,
    X,
    feature_names=feature_names,
    max_display=20,
    show=False
)

fig.patch.set_facecolor("#111827")
ax.set_facecolor("#111827")

ax.tick_params(
    axis="both",
    colors="#e2e8f0"
)

ax.xaxis.label.set_color("#cbd5e1")

for label in ax.get_yticklabels():
    label.set_color("#e2e8f0")

for label in ax.get_xticklabels():
    label.set_color("#cbd5e1")

ax.set_xlabel(
    "SHAP value (impact on model output)",
    color="#cbd5e1"
)

for spine in ax.spines.values():
    spine.set_color("#334155")

plt.tight_layout()

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)


# =========================================================
# FEATURE IMPORTANCE
# =========================================================

st.header("Feature Importance")

st.caption(
    "Mean absolute SHAP values indicate the average contribution "
    "magnitude of each feature."
)


importance = (
    shap_values.abs()
    .mean()
    .sort_values(ascending=False)
)

importance_df = importance.reset_index()

importance_df.columns = [
    "Feature",
    "Mean Absolute SHAP"
]


# =========================================================
# TOP FEATURES CHART
# =========================================================

top_n = min(15, len(importance_df))

top_features = (
    importance_df
    .head(top_n)
    .sort_values(
        "Mean Absolute SHAP",
        ascending=True
    )
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    top_features["Feature"],
    top_features["Mean Absolute SHAP"]
)

ax.set_title(
    "Top Features by SHAP Importance"
)

ax.set_xlabel(
    "Mean Absolute SHAP Value"
)

ax.tick_params(
    axis="both"
)

ax.grid(
    axis="x",
    alpha=0.25
)

plt.tight_layout()

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)


# =========================================================
# IMPORTANCE TABLE
# =========================================================

st.subheader("SHAP Importance Ranking")

display_importance = importance_df.copy()

display_importance["Mean Absolute SHAP"] = (
    display_importance["Mean Absolute SHAP"]
    .round(4)
)

st.dataframe(
    display_importance,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# INDIVIDUAL EXPLANATION
# =========================================================

st.header("Individual Asset Explanation")

st.caption(
    "Inspect how individual features influenced the selected "
    "asset's RUL prediction."
)


selected_index = st.number_input(
    "Select asset row",
    min_value=0,
    max_value=len(df) - 1,
    value=0,
    step=1
)

selected_index = int(selected_index)

st.info(
    f"Currently explaining asset row {selected_index}"
)


# =========================================================
# INDIVIDUAL SHAP WATERFALL
# =========================================================

try:

    # Get SHAP values for selected asset
    individual_values = (
        shap_values.iloc[selected_index].values
    )

    feature_values = (
        X.iloc[selected_index].values
    )

    # Expected/base value
    base_value = explainer.expected_value

    if isinstance(base_value, (list, tuple)):
        base_value = base_value[0]

    if hasattr(base_value, "item"):
        base_value = base_value.item()

    base_value = float(base_value)

    # -----------------------------------------------------
    # Select top 10 contributors
    # -----------------------------------------------------

    contribution_df = pd.DataFrame({
        "Feature": feature_names,
        "Feature Value": feature_values,
        "SHAP Value": individual_values
    })

    contribution_df["Absolute SHAP"] = (
        contribution_df["SHAP Value"].abs()
    )

    contribution_df = (
        contribution_df
        .sort_values(
            "Absolute SHAP",
            ascending=False
        )
        .head(10)
        .copy()
    )

    # Reverse for chart display
    contribution_df = contribution_df.iloc[::-1].reset_index(drop=True)

    # -----------------------------------------------------
    # Calculate cumulative positions
    # -----------------------------------------------------

    current_value = base_value

    starts = []
    ends = []

    # We need contributions in descending importance order
    calculation_df = (
        contribution_df
        .iloc[::-1]
        .copy()
    )

    for shap_value in calculation_df["SHAP Value"]:

        starts.append(current_value)

        current_value = (
            current_value + float(shap_value)
        )

        ends.append(current_value)

    calculation_df["Start"] = starts
    calculation_df["End"] = ends

    # Put calculated positions back into display order
    calculation_df = calculation_df.iloc[::-1].copy()

    # -----------------------------------------------------
    # Create chart
    # -----------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(12, 7)
    )

    fig.patch.set_facecolor("#111827")
    ax.set_facecolor("#111827")

    y_positions = range(
        len(calculation_df)
    )

    for y, (_, row) in enumerate(
        calculation_df.iterrows()
    ):

        start = float(row["Start"])
        end = float(row["End"])
        shap_value = float(row["SHAP Value"])

        width = end - start

        # Positive contribution
        if shap_value >= 0:

            bar_color = "#f43f5e"

        # Negative contribution
        else:

            bar_color = "#3b82f6"

        ax.barh(
            y,
            width,
            left=start,
            height=0.58,
            color=bar_color,
            edgecolor="none"
        )

        # Value shown inside/near the bar
        if abs(width) > 3:

            text_x = start + width / 2

            text_color = "white"

            ax.text(
                text_x,
                y,
                f"{shap_value:+.2f}",
                ha="center",
                va="center",
                fontsize=11,
                fontweight="bold",
                color=text_color
            )

        else:

            # For very small contributions,
            # place value outside the bar
            text_x = end

            ax.text(
                text_x,
                y,
                f" {shap_value:+.2f}",
                ha="left",
                va="center",
                fontsize=10,
                fontweight="bold",
                color="#e2e8f0"
            )

    # -----------------------------------------------------
    # Feature labels
    # -----------------------------------------------------

    labels = []

    for _, row in calculation_df.iterrows():

        feature = row["Feature"]
        value = row["Feature Value"]

        if isinstance(value, float):
            value_text = f"{value:.2f}"
        else:
            value_text = str(value)

        labels.append(
            f"{value_text} = {feature}"
        )

    ax.set_yticks(
        list(y_positions)
    )

    ax.set_yticklabels(
        labels,
        fontsize=10,
        color="#e2e8f0"
    )

    # -----------------------------------------------------
    # Prediction value
    # -----------------------------------------------------

    prediction_value = (
        base_value +
        contribution_df["SHAP Value"].sum()
    )

    ax.axvline(
        prediction_value,
        color="#94a3b8",
        linestyle="--",
        linewidth=1,
        alpha=0.7
    )

    # Prediction annotation
    ax.text(
        prediction_value,
        len(calculation_df) - 0.25,
        f"Predicted RUL: {prediction_value:.2f}",
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold",
        color="#f8fafc",
        bbox=dict(
            boxstyle="round,pad=0.35",
            facecolor="#1e293b",
            edgecolor="#475569"
        )
    )

    # -----------------------------------------------------
    # Base value
    # -----------------------------------------------------

    ax.axvline(
        base_value,
        color="#64748b",
        linestyle=":",
        linewidth=1,
        alpha=0.6
    )

    ax.text(
        base_value,
        -0.8,
        f"Base: {base_value:.2f}",
        ha="center",
        va="top",
        fontsize=9,
        color="#94a3b8"
    )

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    ax.set_title(
        "SHAP Contribution Analysis",
        fontsize=15,
        fontweight="bold",
        color="#f8fafc",
        pad=18
    )

    ax.set_xlabel(
        "Model Output (RUL)",
        fontsize=10,
        color="#cbd5e1"
    )

    # -----------------------------------------------------
    # Styling
    # -----------------------------------------------------

    ax.tick_params(
        axis="x",
        colors="#cbd5e1",
        labelsize=9
    )

    ax.tick_params(
        axis="y",
        colors="#e2e8f0",
        labelsize=10,
        length=0
    )

    ax.grid(
        axis="x",
        color="#334155",
        linestyle="--",
        linewidth=0.6,
        alpha=0.35
    )

    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    # Give enough space for feature labels
    plt.subplots_adjust(
        left=0.25,
        right=0.97,
        top=0.88,
        bottom=0.12
    )

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

except Exception as e:

    st.warning(
        f"Individual SHAP explanation could not be rendered: {e}"
    )
    
# =========================================================
# SELECTED ASSET FEATURES
# =========================================================

with st.expander("View Selected Asset Features"):

    selected_features = pd.DataFrame(
        {
            "Feature": feature_names,
            "Value": X.iloc[selected_index].values
        }
    )

    st.dataframe(
        selected_features,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# DOWNLOAD SHAP RESULTS
# =========================================================

st.subheader("Export")

csv_data = (
    importance_df
    .to_csv(index=False)
    .encode("utf-8")
)

st.download_button(
    label="Download SHAP Feature Importance",
    data=csv_data,
    file_name="SHAP_Feature_Importance.csv",
    mime="text/csv",
    use_container_width=True
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Industrial Predictive Maintenance System | "
    "AI Explainability | XGBoost + SHAP"
)