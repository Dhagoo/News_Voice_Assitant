
# backend/models/generate_dummy_models.py

import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as np

# Ensure directory exists
MODELS_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(MODELS_DIR, exist_ok=True)

def generate_topic_model():
    print("Generating dummy topic model...")
    # Dummy training data
    X = [
        "president election vote government", 
        "apple google python code ai", 
        "football score goal win", 
        "stock market price economy", 
        "virus vaccine health doctor"
    ]
    y = ["Politics", "Technology", "Sports", "Finance", "Health"]
    
    model = make_pipeline(CountVectorizer(), LogisticRegression())
    model.fit(X, y)
    
    path = os.path.join(MODELS_DIR, "topic_model.pkl")
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Saved to {path}")

def generate_trend_model():
    print("Generating dummy trend model...")
    # Dummy data: day_index -> trend_score
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([10, 20, 30, 40, 50])
    
    model = LinearRegression()
    model.fit(X, y)
    
    path = os.path.join(MODELS_DIR, "trend_model.pkl")
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Saved to {path}")

if __name__ == "__main__":
    generate_topic_model()
    generate_trend_model()
