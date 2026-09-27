import streamlit as st

def style_background_home():
    st.markdown(
        """
        <style>
        .stApp {
            background: #586F2A !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background: #E0E3FF !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
        
        /* Hide Top Bar of streamlit */
        #MainMenu, footer, header {
            visibility: hidden;
        }
        
        .block-container {
            padding-top: 1.5rem !important;
        }
        
        h1 {
            front-famliy: 'Climate Crisis', sans-serif; !important;
            front-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )