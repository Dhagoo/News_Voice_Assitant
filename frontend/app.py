
# frontend/app.py

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from components.news_card import render_news_card

# Configuration
import os
API_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(
    page_title="AI Newspaper Voice Assistant",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("📰 AI News Assistant")
page = st.sidebar.radio("Navigate", ["Home", "Analytics", "Trend Prediction"])

# --- PAGE: HOME ---
if page == "Home":
    st.title("🎙️ AI Newspaper Voice Assistant")
    st.markdown("Listen to the latest news summarized just for you.")
    
    if st.button("🔄 Read Today's News"):
        with st.spinner("Fetching and processing news..."):
            try:
                response = requests.get(f"{API_URL}/news/fetch?force_refresh=true")
                if response.status_code == 200:
                    st.session_state['news'] = response.json()
                    st.success("News fetched successfully!")
                else:
                    st.error("Failed to fetch news.")
            except Exception as e:
                st.error(f"Error checking backend: {e}. Is it running?")

    if 'news' in st.session_state:
        for idx, item in enumerate(st.session_state['news']):
            col1, col2 = st.columns([0.8, 0.2])
            
            with col1:
                render_news_card(
                    item['title'], 
                    item['summary'], 
                    item.get('category', 'General'), 
                    item['published']
                )
            
            with col2:
                st.write("")
                st.write("")
                if st.button(f"▶️ Play", key=f"play_{idx}"):
                    with st.spinner("Generating audio..."):
                        try:
                            # 1. Summary (already done in simple fetch, but could refine here)
                            text_to_speak = f"{item['title']}. {item['summary']}"
                            
                            # 2. TTS
                            tts_res = requests.post(
                                f"{API_URL}/audio/generate", 
                                json={"text": text_to_speak}
                            )
                            
                            if tts_res.status_code == 200:
                                filename = tts_res.json()["filename"]
                                audio_url = f"{API_URL}/audio/play/{filename}"
                                st.audio(audio_url)
                            else:
                                st.error("Failed to generate audio")
                        except Exception as e:
                            st.error(str(e))

# --- PAGE: ANALYTICS ---
elif page == "Analytics":
    st.title("📊 News Analytics")
    
    try:
        response = requests.get(f"{API_URL}/analytics/topics")
        if response.status_code == 200:
            data = response.json()
            
            if data['labels']:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Topic Distribution")
                    df = pd.DataFrame({'Topic': data['labels'], 'Count': data['values']})
                    fig = px.bar(df, x='Topic', y='Count', color='Topic')
                    st.plotly_chart(fig, use_container_width=True)
                    
                with col2:
                    st.subheader("Topic Share")
                    fig2 = px.pie(df, names='Topic', values='Count', hole=0.3)
                    st.plotly_chart(fig2, use_container_width=True)
                    
                st.info(f"Most Frequent Topic Today: **{data['most_frequent']}**")
            else:
                st.warning("No data available. Fetch news on Home page first.")
        else:
            st.error("Could not fetch analytics.")
    except Exception as e:
        st.error(f"Connection error: {e}")

# --- PAGE: TREND PREDICTION ---
elif page == "Trend Prediction":
    st.title("📈 Trend Prediction")
    st.markdown("predicting what will be hot tomorrow based on historical data.")
    
    if st.button("🔮 Predict Tomorrow's Trend"):
        try:
            response = requests.get(f"{API_URL}/analytics/trend/predict")
            if response.status_code == 200:
                trend = response.json()["predicted_trend"]
                st.balloons()
                st.success(f"🚀 Predicted Trending Category for Tomorrow: **{trend}**")
            else:
                st.error("Prediction failed.")
        except Exception as e:
            st.error(f"Connection error: {e}")
            
    # Dummy chart for visualization
    st.subheader("Last 7 Days Activity")
    dummy_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Politics": [10, 12, 15, 8, 12, 14, 18],
        "Technology": [5, 8, 12, 15, 20, 18, 22],
        "Sports": [20, 18, 15, 22, 25, 30, 28]
    })
    st.line_chart(dummy_data.set_index("Day"))
