
# backend/utils/db.py

import json
import os
import pandas as pd
from .config import RAW_NEWS_FILE, CLEANED_NEWS_FILE, TOPIC_COUNTS_FILE, PREDICTIONS_FILE

def load_json(filepath):
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return []

def save_json(data, filepath):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving {filepath}: {e}")

def load_csv(filepath):
    if not os.path.exists(filepath):
        return pd.DataFrame()
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return pd.DataFrame()

def save_csv(df, filepath):
    try:
        df.to_csv(filepath, index=False)
    except Exception as e:
        print(f"Error saving {filepath}: {e}")

# Methods specifically for our app
def get_raw_news():
    return load_json(RAW_NEWS_FILE)

def save_raw_news(news_list):
    save_json(news_list, RAW_NEWS_FILE)

def get_cleaned_news():
    return load_json(CLEANED_NEWS_FILE)

def save_cleaned_news(news_list):
    save_json(news_list, CLEANED_NEWS_FILE)
