
# backend/services/tts_engine.py

from gtts import gTTS
import os
import uuid
from backend.utils.config import AUDIO_DIR

def generate_audio(text):
    """
    Converts text to audio using gTTS and saves it.
    Returns the filename of the generated audio.
    """
    if not text:
        return None
        
    try:
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)
        
        tts = gTTS(text=text, lang='en')
        tts.save(filepath)
        
        return filename
    except Exception as e:
        print(f"TTS Error: {e}")
        return None
