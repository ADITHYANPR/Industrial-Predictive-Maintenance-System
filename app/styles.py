import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* Hide Streamlit branding */
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}

    /* Main App */
    .main{
        background:#F4F7FA;
        color:#1F2937;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background:#1E293B;
    }

    section[data-testid="stSidebar"] *{
        color:white;
    }

    /* Titles */
    h1{
        color:#0F172A;
        font-weight:700;
    }

    h2,h3{
        color:#334155;
    }

    /* Metric Cards */
    div[data-testid="metric-container"]{
        background:white;
        border-radius:12px;
        border:1px solid #E5E7EB;
        padding:18px;
        box-shadow:0 2px 8px rgba(0,0,0,.05);
    }

    /* Buttons */
    .stButton>button{
        width:100%;
        border-radius:8px;
        border:none;
        background:#2563EB;
        color:white;
        font-weight:600;
        height:45px;
    }

    .stButton>button:hover{
        background:#1D4ED8;
    }

    hr{
        border:none;
        border-top:1px solid #E5E7EB;
    }

    </style>
    """, unsafe_allow_html=True)