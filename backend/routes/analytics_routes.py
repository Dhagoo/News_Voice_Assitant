
# backend/routes/analytics_routes.py

from fastapi import APIRouter
from backend.services.trend_predictor import predict_trend
from backend.utils.db import get_raw_news
import pandas as pd
from collections import Counter

router = APIRouter()

@router.get("/topics")
async def get_topic_frequencies():
    """
    Returns frequency distribution of topics from current news.
    """
    news = get_raw_news()
    if not news:
        return {"data": []}
        
    categories = [item.get('category', 'General') for item in news]
    counts = Counter(categories)
    
    return {
        "labels": list(counts.keys()),
        "values": list(counts.values()),
        "most_frequent": counts.most_common(1)[0][0] if counts else "None"
    }

@router.get("/trend/predict")
async def get_trend_prediction():
    """
    Predicts the next trending category.
    """
    # In a real app, we'd pass historical data.
    # Here we just trigger the predictor service.
    prediction = predict_trend(None)
    return {"predicted_trend": prediction}
