from streamlit_option_menu import option_menu
import streamlit as st

def show_sidebar():

    with st.sidebar:

        selected = option_menu(
            menu_title="⚙️ Industrial Predictive\nMaintenance",

            options=[
                "Home",
                "Manual Prediction",
                "CSV Batch Prediction",
                "Analytics",
                "SHAP Explainability",
                "About"
            ],

            icons=[
                "house",
                "cpu",
                "file-earmark-spreadsheet",
                "bar-chart",
                "activity",
                "info-circle"
            ],

            menu_icon="gear-fill",

            default_index=0,

            styles={
                "container": {
                    "padding": "10px",
                    "background-color": "#1E293B",
                },

                "icon": {
                    "color": "#60A5FA",
                    "font-size": "20px",
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "border-radius": "8px",
                },

                "nav-link-selected": {
                    "background-color": "#2563EB",
                    "color": "white",
                }
            }
        )

        st.markdown("---")

        st.success("Version 1.0")

        st.markdown("---")

        st.caption("Built using")

        st.write("• Streamlit")

        st.write("• XGBoost")

        st.write("• SHAP")

        st.write("• Plotly")

    return selected