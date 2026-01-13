
# backend/services/trend_predictor.py

import pickle
import os
import pandas as pd
import random # For dummy fallback
from backend.utils.config import TREND_MODEL_PATH

# Load model
try:
    with open(TREND_MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except:
    model = None

CATEGORIES = ["Politics", "Technology", "Sports", "Finance", "Health", "General"]

def predict_trend(days_data):
    """
    Predicts the next trending topic based on past counts.
    Input: DataFrame or list of dicts with 'date', 'category', 'count'
    """
    # Real implementation would use Linear Regression on time-series data
    # Here providing a robust fallback for the prototype
    
    if model:
        try:
            # Assume model takes formatted input
            # This part depends heavily on how we trained it (which we haven't yet)
            pass 
        except:
            pass
            
    # Fallback Logic:
    # Just return a mock prediction based on random choice weighted or simple logic
    # In a real app, this would use the SKLearn model.
    
    # For prototype visualization, we'll return a random category as the "Predicted Trending Topic"
    predicted_category = random.choice(CATEGORIES)
    return predicted_category
