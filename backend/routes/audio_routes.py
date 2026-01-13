
# backend/routes/audio_routes.py

from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import FileResponse
from backend.services.tts_engine import generate_audio
from backend.utils.config import AUDIO_DIR
import os

router = APIRouter()

@router.post("/generate")
async def create_audio(text: str = Body(..., embed=True)):
    """
    Generates MP3 from text and returns the filename.
    """
    filename = generate_audio(text)
    if not filename:
        raise HTTPException(status_code=500, detail="Audio generation failed")
    
    return {"filename": filename}

@router.get("/play/{filename}")
async def play_audio(filename: str):
    """
    Streams the audio file.
    """
    filepath = os.path.join(AUDIO_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Audio file not found")
        
    return FileResponse(filepath, media_type="audio/mpeg")
