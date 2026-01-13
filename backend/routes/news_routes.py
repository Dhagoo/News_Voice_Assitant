
# backend/routes/news_routes.py

from fastapi import APIRouter, HTTPException
from backend.services.news_fetcher import fetch_news
from backend.services.topic_classifier import classify_news
from backend.utils.db import save_raw_news, get_raw_news
import datetime

router = APIRouter()

@router.get("/fetch")
async def get_news(force_refresh: bool = False):
    """
    Fetches news from RSS feeds.
    """
    # Simple caching: check if we have data for today? 
    # For now, let's just fetch fresh if force_refresh is True or file empty
    current_news = get_raw_news()
    
    if force_refresh or not current_news:
        news_items = fetch_news()
        
        # Classify them immediately
        for item in news_items:
            item['category'] = classify_news(item['title'] + " " + item['summary'])
            
        save_raw_news(news_items)
        return news_items
        
    return current_news
