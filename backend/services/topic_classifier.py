
# backend/services/topic_classifier.py

import pickle
import os
from backend.utils.config import TOPIC_MODEL_PATH

# Load model if exists, else use keyword fallback
try:
    with open(TOPIC_MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except:
    model = None

KEYWORDS = {
    "politics": ["government", "election", "president", "policy", "congress", "senate"],
    "technology": ["ai", "tech", "software", "apple", "google", "microsoft", "cyber", "internet"],
    "sports": ["football", "soccer", "basketball", "nba", "nfl", "game", "match", "score"],
    "finance": ["market", "stock", "economy", "money", "bank", "inflation", "trade"],
    "health": ["virus", "hospital", "doctor", "health", "medicine", "pandemic"]
}

def classify_news(text):
    """
    Classifies news text into a category.
    """
    if not text:
        return "General"
        
    text_lower = text.lower()
    
    # Priority 1: Use ML Model if available
    if model:
        try:
            prediction = model.predict([text])
            return prediction[0]
        except:
            pass # Fallback to keywords
            
    # Priority 2: Keyword matching
    scores = {cat: 0 for cat in KEYWORDS}
    for cat, words in KEYWORDS.items():
        for word in words:
            if word in text_lower:
                scores[cat] += 1
                
    # Get max score
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] > 0:
        return best_cat.capitalize()
        
    return "General"
