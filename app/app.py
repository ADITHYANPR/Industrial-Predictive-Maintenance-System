from styles import load_css
import streamlit as st

st.set_page_config(
    page_title="Industrial Predictive Maintenance System",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_css()
st.title("⚙️ Industrial Predictive Maintenance System")

st.markdown("""
Welcome to the **Industrial Predictive Maintenance Dashboard**.

👈 Use the sidebar to navigate through the application.

### Available Modules

- 🏠 Home
- ✍️ Manual Prediction
- 📂 CSV Batch Prediction
- 📊 Analytics
- 🧠 Explainability (SHAP)
- ℹ️ About
""")

st.success("Application Loaded Successfully.")