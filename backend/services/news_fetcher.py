
# backend/services/news_fetcher.py

import feedparser
from backend.utils.config import RSS_FEEDS
from backend.utils.preprocess import clean_text
import datetime

def fetch_news():
    """
    Fetches news from configured RSS feeds.
    Returns a list of dictionaries with title, link, published, summary.
    """
    news_items = []
    
    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:5]:  # Limit to 5 per feed to avoid overwhelm
                # Extract Summary
                summary = entry.get('summary', '') or entry.get('description', '')
                
                # Basic cleaning
                clean_summary = clean_text(summary)
                
                news_item = {
                    "title": entry.get('title', 'No Title'),
                    "link": entry.get('link', '#'),
                    "published": entry.get('published', str(datetime.datetime.now())),
                    "summary": clean_summary,
                    "id": entry.get('link', '')  # Use link as ID
                }
                news_items.append(news_item)
        except Exception as e:
            print(f"Error fetching from {feed_url}: {e}")
            
    return news_items
