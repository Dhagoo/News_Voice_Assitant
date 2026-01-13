
# backend/utils/config.py

import os

# RSS Feeds to fetch news from
RSS_FEEDS = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "http://rss.cnn.com/rss/edition.rss",
    "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
]

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
AUDIO_DIR = os.path.join(DATA_DIR, "audio")
MODELS_DIR = os.path.join(BASE_DIR, "backend", "models")

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

# Files
RAW_NEWS_FILE = os.path.join(DATA_DIR, "raw_news.json")
CLEANED_NEWS_FILE = os.path.join(DATA_DIR, "cleaned_news.json")
TOPIC_COUNTS_FILE = os.path.join(DATA_DIR, "topic_counts.csv")
PREDICTIONS_FILE = os.path.join(DATA_DIR, "predictions.csv")

# Model Paths
TOPIC_MODEL_PATH = os.path.join(MODELS_DIR, "topic_model.pkl")
TREND_MODEL_PATH = os.path.join(MODELS_DIR, "trend_model.pkl")
