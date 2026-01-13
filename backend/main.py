
# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import news_routes, summary_routes, audio_routes, analytics_routes

app = FastAPI(title="AI Newspaper Voice Assistant", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(news_routes.router, prefix="/news", tags=["News"])
app.include_router(summary_routes.router, prefix="/summary", tags=["Summary"])
app.include_router(audio_routes.router, prefix="/audio", tags=["Audio"])
app.include_router(analytics_routes.router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
def home():
    return {"message": "AI Newspaper Backend is Running"}
