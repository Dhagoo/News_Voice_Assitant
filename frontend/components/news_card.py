
# frontend/components/news_card.py

import streamlit as st

def render_news_card(title, summary, category, published, audio_url=None):
    """
    Renders a neat card for a news item.
    """
    with st.container():
        st.markdown(f"""
        <div style="
            padding: 20px;
            border-radius: 10px;
            background-color: #f0f2f6;
            margin-bottom: 20px;
            border-left: 5px solid #4B8BBE;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        ">
            <h3 style="color: #306998; margin-bottom: 5px;">{title}</h3>
            <span style="
                background-color: #FFD43B; 
                color: #306998; 
                padding: 2px 8px; 
                border-radius: 5px; 
                font-size: 0.8em; 
                font-weight: bold;
            ">{category}</span>
            <span style="color: grey; font-size: 0.8em; margin-left: 10px;">{published}</span>
            <p style="margin-top: 10px; font-size: 1.0em;">{summary}</p>
        </div>
        """, unsafe_allow_html=True)
