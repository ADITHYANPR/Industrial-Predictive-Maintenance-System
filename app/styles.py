import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* =========================================================
           GLOBAL APPLICATION
        ========================================================= */

        .stApp {
            background: #0b1120 !important;
            color: #f8fafc !important;
        }

        .main {
            background: #0b1120 !important;
        }

        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1450px;
        }


        /* =========================================================
           GLOBAL TEXT
        ========================================================= */

        h1, h2, h3, h4, h5, h6 {
            color: #f8fafc !important;
            font-weight: 700 !important;
        }

        .stMarkdown {
            color: #e2e8f0 !important;
        }

        .stMarkdown p {
            color: #cbd5e1 !important;
        }

        .stMarkdown li {
            color: #cbd5e1 !important;
        }

        .stCaption,
        [data-testid="stCaptionContainer"] {
            color: #94a3b8 !important;
        }

        label {
            color: #e2e8f0 !important;
        }

        .stTextInput label,
        .stNumberInput label,
        .stSelectbox label,
        .stMultiSelect label,
        .stFileUploader label,
        .stSlider label,
        .stTextArea label {
            color: #e2e8f0 !important;
            font-weight: 600 !important;
        }


        /* =========================================================
           STREAMLIT DEFAULT SIDEBAR NAVIGATION
           HIDE IT BECAUSE WE HAVE OUR OWN SIDEBAR
        ========================================================= */

        [data-testid="stSidebarNav"] {
            display: none !important;
        }


        /* =========================================================
           SIDEBAR
        ========================================================= */

        section[data-testid="stSidebar"] {
            background: #0f172a !important;
            border-right: 1px solid #1e293b !important;
        }

        section[data-testid="stSidebar"] > div {
            background: #0f172a !important;
            padding-top: 1.5rem;
        }

        section[data-testid="stSidebar"] * {
            color: #e2e8f0;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] h4 {
            color: #f8fafc !important;
        }

        section[data-testid="stSidebar"] p {
            color: #cbd5e1 !important;
        }

        section[data-testid="stSidebar"] label {
            color: #e2e8f0 !important;
        }

        section[data-testid="stSidebar"] hr {
            border-color: #334155 !important;
        }


        /* =========================================================
           SIDEBAR PAGE LINKS
        ========================================================= */

        section[data-testid="stSidebar"] a {
            color: #cbd5e1 !important;
            text-decoration: none !important;
        }

        section[data-testid="stSidebar"] a:hover {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stPageLink"] {
            border-radius: 8px;
        }


        /* =========================================================
           BUTTONS
        ========================================================= */

        .stButton > button {
            width: 100%;
            border-radius: 8px;

            border: 1px solid #2563eb !important;
            background: #2563eb !important;

            color: #ffffff !important;

            font-weight: 600;
            padding: 0.65rem 1rem;

            transition:
                background 0.2s ease,
                border-color 0.2s ease,
                transform 0.2s ease;
        }

        .stButton > button:hover {
            background: #1d4ed8 !important;
            border-color: #1d4ed8 !important;
            color: #ffffff !important;
            transform: translateY(-1px);
        }

        button[kind="primary"] {
            background: #2563eb !important;
            border-color: #2563eb !important;
            color: #ffffff !important;
        }

        button[kind="primary"]:hover {
            background: #1d4ed8 !important;
            border-color: #1d4ed8 !important;
        }


        /* =========================================================
           HERO
        ========================================================= */

        .hero {
            background: linear-gradient(
                135deg,
                #111827 0%,
                #1e3a8a 100%
            ) !important;

            border: 1px solid #263b73;

            border-radius: 16px;

            padding: 2.5rem 2.75rem;

            margin-bottom: 1.75rem;

            box-shadow:
                0 8px 30px rgba(0, 0, 0, 0.35);
        }

        .hero-eyebrow {
            color: #93c5fd !important;

            font-size: 0.8rem;

            font-weight: 700;

            letter-spacing: 1.5px;

            text-transform: uppercase;

            margin-bottom: 0.75rem;
        }

        .hero-title {
            color: #ffffff !important;

            font-size: 2.35rem;

            font-weight: 750;

            margin-bottom: 0.5rem;
        }

        .hero-description {
            color: #dbeafe !important;

            font-size: 1rem;

            max-width: 720px;

            line-height: 1.6;
        }


        /* =========================================================
           STATUS ONLINE
        ========================================================= */

        .status-online {
            display: inline-flex;

            align-items: center;

            gap: 8px;

            background: rgba(34, 197, 94, 0.12);

            border: 1px solid rgba(34, 197, 94, 0.35);

            color: #86efac !important;

            border-radius: 999px;

            padding: 5px 11px;

            font-size: 0.78rem;

            font-weight: 650;
        }

        .status-dot {
            width: 8px;
            height: 8px;

            background: #22c55e;

            border-radius: 50%;
        }


        /* =========================================================
           KPI CARDS
        ========================================================= */

        .kpi-card {
            background: #111827 !important;

            border: 1px solid #263244 !important;

            border-radius: 12px;

            padding: 1.25rem;

            min-height: 125px;

            box-shadow:
                0 4px 15px rgba(0, 0, 0, 0.22);
        }

        .kpi-label {
            font-size: 0.85rem;

            font-weight: 700;

            color: #94a3b8 !important;

            margin-bottom: 0.5rem;
        }

        .kpi-value {
            font-size: 2rem;

            font-weight: 750;

            color: #f8fafc !important;

            line-height: 1.1;
        }

        .kpi-description {
            margin-top: 0.5rem;

            font-size: 0.78rem;

            color: #94a3b8 !important;
        }


        /* =========================================================
           MODULE CARDS
        ========================================================= */

        .module-card {
            background: #111827 !important;

            border: 1px solid #263244 !important;

            border-radius: 12px;

            padding: 1.35rem;

            min-height: 220px;

            box-shadow:
                0 4px 15px rgba(0, 0, 0, 0.18);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                border-color 0.2s ease;
        }

        .module-card:hover {
            transform: translateY(-3px);

            border-color: #3b82f6 !important;

            box-shadow:
                0 10px 25px rgba(0, 0, 0, 0.3);
        }

        .module-icon {
            width: 42px;

            height: 42px;

            border-radius: 10px;

            background: #172554 !important;

            color: #60a5fa !important;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 1.2rem;

            margin-bottom: 1rem;
        }

        .module-title {
            color: #f8fafc !important;

            font-size: 1.05rem;

            font-weight: 700;

            margin-bottom: 0.5rem;
        }

        .module-description {
            color: #cbd5e1 !important;

            font-size: 0.86rem;

            line-height: 1.5;
        }


        /* =========================================================
           SECTION HEADERS
        ========================================================= */

        .section-header {
            margin-top: 2rem;

            margin-bottom: 1rem;
        }

        .section-title {
            color: #f8fafc !important;

            font-size: 1.35rem;

            font-weight: 700;
        }

        .section-subtitle {
            color: #94a3b8 !important;

            font-size: 0.85rem;

            margin-top: 0.2rem;
        }


        /* =========================================================
           RESULT CARDS
        ========================================================= */

        .result-card {
            background: #111827 !important;

            border: 1px solid #263244 !important;

            border-radius: 14px;

            padding: 2rem;

            text-align: center;

            box-shadow:
                0 5px 20px rgba(0, 0, 0, 0.25);
        }

        .result-label {
            color: #94a3b8 !important;

            font-size: 0.85rem;

            font-weight: 650;

            text-transform: uppercase;

            letter-spacing: 0.8px;
        }

        .result-value {
            color: #60a5fa !important;

            font-size: 3.2rem;

            font-weight: 800;

            margin: 0.4rem 0;
        }

        .result-unit {
            color: #94a3b8 !important;

            font-size: 0.9rem;
        }


        /* =========================================================
           INFO CARDS
        ========================================================= */

        .info-card {
            background: #172554 !important;

            border-left: 4px solid #3b82f6;

            border-radius: 8px;

            padding: 1rem 1.2rem;

            margin: 1rem 0;

            color: #dbeafe !important;
        }


        /* =========================================================
           STREAMLIT METRICS
        ========================================================= */

        div[data-testid="stMetric"] {
            background: #111827 !important;

            border: 1px solid #263244 !important;

            padding: 1rem;

            border-radius: 10px;

            box-shadow:
                0 4px 15px rgba(0, 0, 0, 0.2);
        }

        div[data-testid="stMetric"] label {
            color: #94a3b8 !important;
        }

        div[data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #f8fafc !important;
        }

        div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
            color: #cbd5e1 !important;
        }


        /* =========================================================
           NUMBER INPUTS
        ========================================================= */

        div[data-testid="stNumberInput"] {
            color: #e2e8f0 !important;
        }

        div[data-testid="stNumberInput"] input {
            background: #111827 !important;

            color: #f8fafc !important;

            border: 1px solid #334155 !important;

            border-radius: 8px;
        }

        div[data-testid="stNumberInput"] button {
            background: #1e293b !important;

            color: #e2e8f0 !important;

            border-color: #334155 !important;
        }

        div[data-testid="stNumberInput"] button:hover {
            background: #334155 !important;

            color: #ffffff !important;
        }


        /* =========================================================
           TEXT INPUTS
        ========================================================= */

        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea {
            background: #111827 !important;

            color: #f8fafc !important;

            border: 1px solid #334155 !important;
        }


        /* =========================================================
           SELECT BOX
        ========================================================= */

        div[data-testid="stSelectbox"] > div > div {
            background: #111827 !important;

            color: #f8fafc !important;

            border-color: #334155 !important;
        }


        /* =========================================================
           FILE UPLOADER
        ========================================================= */

        div[data-testid="stFileUploader"] {
            background: #111827 !important;

            border: 1px solid #263244 !important;

            border-radius: 12px;

            padding: 0.5rem;
        }

        div[data-testid="stFileUploader"] section {
            background: #111827 !important;
        }

        div[data-testid="stFileUploader"] p {
            color: #cbd5e1 !important;
        }

        div[data-testid="stFileUploader"] small {
            color: #94a3b8 !important;
        }


        /* =========================================================
           EXPANDERS
        ========================================================= */

        div[data-testid="stExpander"] {
            background: #111827 !important;

            border: 1px solid #263244 !important;

            border-radius: 10px;

            overflow: hidden;
        }

        div[data-testid="stExpander"] summary {
            color: #f8fafc !important;
        }

        div[data-testid="stExpander"] summary:hover {
            color: #60a5fa !important;
        }


        /* =========================================================
           DATAFRAME
        ========================================================= */

        div[data-testid="stDataFrame"] {
            background: #111827 !important;

            border: 1px solid #263244 !important;

            border-radius: 10px;

            overflow: hidden;
        }


        /* =========================================================
           ALERTS
        ========================================================= */

        div[data-testid="stAlert"] {
            border-radius: 10px;
        }


        /* =========================================================
           PROGRESS BAR
        ========================================================= */

        div[data-testid="stProgress"] > div {
            border-radius: 999px;
        }


        /* =========================================================
           DIVIDERS
        ========================================================= */

        hr {
            border-color: #263244 !important;
        }


        /* =========================================================
           FOOTER
        ========================================================= */

        .app-footer {
            margin-top: 3rem;

            padding: 1.25rem 0;

            border-top: 1px solid #263244;

            text-align: center;

            color: #64748b !important;

            font-size: 0.78rem;
        }


        /* =========================================================
           STREAMLIT HEADER
        ========================================================= */

        header[data-testid="stHeader"] {
            background: #0b1120 !important;
        }

        header[data-testid="stHeader"] * {
            color: #e2e8f0 !important;
        }


        /* =========================================================
           DEPLOY BUTTON
        ========================================================= */

        [data-testid="stToolbar"] {
            background: transparent !important;
        }


        /* =========================================================
           SCROLLBAR
        ========================================================= */

        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #0b1120;
        }

        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }


        /* =========================================================
           HIDE STREAMLIT DEFAULT MENU / FOOTER
        ========================================================= */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        </style>
        """,
        unsafe_allow_html=True
    )